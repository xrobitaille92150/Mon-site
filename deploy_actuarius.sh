#!/bin/zsh
# =============================================================================
# deploy_actuarius.sh — Rebuild + commit + déploiement Netlify des trois sites
#
#   ~/Documents/GitHub/Mon-site
#     .                → myxavier.finance          (site b15fc9a7-…)
#     actuarius/       → editionsactuarius.com     (site fb270035-…)
#     actuarius-press/ → actuariuspress.com        (site 1a8e240b-…)
#
# Usage :
#   ./deploy_actuarius.sh "message de commit"            # tout : build, commit, push, 3 déploiements, vérifs
#   ./deploy_actuarius.sh --no-build "message"           # sans regénérer les pages
#   ./deploy_actuarius.sh --no-git  "message"            # sans commit ni push (déploie l'état courant du disque)
#   ./deploy_actuarius.sh --only editions "message"      # un seul site : root | editions | press
#   ./deploy_actuarius.sh --dry-run                      # montre ce qui serait fait, ne déploie rien
#
# Prérequis (déjà en place au 11/08/2026) : netlify-cli dans ~/.npm-global/bin,
# authentifié (`netlify status` doit afficher le compte). Python 3 pour les générateurs.
# Complète deploy.sh (qui ne déploie que la racine) — ne le remplace pas.
# =============================================================================
set -e
set -o pipefail

export PATH="$HOME/.npm-global/bin:$PATH"
cd "$(dirname "$0")"

# ---- Sites Netlify ---------------------------------------------------------
SITE_ROOT="b15fc9a7-542e-4e10-8cdd-80ddc5d40f51"      # myxavier.finance
SITE_EDITIONS="fb270035-f014-48fd-997a-3454629e88ad"  # editionsactuarius.com
SITE_PRESS="1a8e240b-550b-41b6-8097-7f91ca9101e8"     # actuariuspress.com

# ---- Options ---------------------------------------------------------------
DO_BUILD=1; DO_GIT=1; DRY=0; ONLY=""
while [[ "$1" == --* ]]; do
  case "$1" in
    --no-build) DO_BUILD=0 ;;
    --no-git)   DO_GIT=0 ;;
    --dry-run)  DRY=1 ;;
    --only)     shift; ONLY="$1" ;;
    *) echo "Option inconnue : $1"; exit 1 ;;
  esac
  shift
done
MSG="${1:-Mise à jour des sites (couverture navy finale + 4e de couverture)}"

run() { if [[ $DRY -eq 1 ]]; then echo "  [dry-run] $*"; else eval "$@"; fi }

echo "== 0. Contrôles préalables"
command -v netlify >/dev/null || { echo "✘ netlify-cli introuvable dans le PATH (~/.npm-global/bin)"; exit 1; }
if netlify status 2>&1 | grep -q -i "not logged in\|please log in\|netlify login"; then
  echo "✘ netlify-cli non authentifié : lancer 'netlify login' puis relancer."; exit 1
fi
[[ -f gen/build_actuarius.py ]] || { echo "✘ Pas dans le repo Mon-site"; exit 1; }
rm -f .git/index.lock .git/HEAD.lock 2>/dev/null || true
echo "  ✔ netlify-cli OK, repo OK"

if [[ $DO_BUILD -eq 1 ]]; then
  echo "== 1. Regénération des pages (generateurs Python)"
  run "python3 gen/build_publications.py"
  run "python3 gen/build_actuarius.py"
  # Garde-fous : la couverture réelle et la 4e doivent être dans la sortie
  if [[ $DRY -eq 0 ]]; then
    grep -q 'covers/chantiers-2027-2028-recto.jpg' actuarius/index.html \
      || { echo "✘ Accueil Actuarius : couverture réelle absente"; exit 1; }
    grep -q 'class="bc"' actuarius/chantiers-2027-2028/index.html \
      || { echo "✘ Page livre : section « Quatrième de couverture » absente"; exit 1; }
    grep -q 'covers/chantiers-2027-2028-og.jpg' actuarius/chantiers-2027-2028/index.html \
      || { echo "✘ Page livre : og:image absent"; exit 1; }
    [[ -f actuarius/covers/chantiers-2027-2028-recto.jpg && -f actuarius/covers/chantiers-2027-2028-4e.jpg \
       && -f actuarius/covers/chantiers-2027-2028-og.jpg ]] \
      || { echo "✘ actuarius/covers/ incomplet"; exit 1; }
    echo "  ✔ Build OK (couverture, section 4e, og:image, 3 fichiers covers/)"
  fi
fi

if [[ $DO_GIT -eq 1 ]]; then
  echo "== 2. Git"
  if [[ -n "$(git status --porcelain 2>/dev/null | grep -v '^?? _to_delete/\|^?? node_modules/\|^?? package-lock.json')" ]]; then
    run "git add -A -- . ':(exclude)_to_delete' ':(exclude)node_modules' ':(exclude)package-lock.json'"
    run "git commit -m \"$MSG\""
    echo "  ✔ Commit : $MSG"
  else
    echo "  ℹ Rien à committer."
  fi
  run "git push origin main" && echo "  ✔ Poussé sur GitHub" || echo "  ⚠ Push GitHub échoué (flag GitHub) — on déploie quand même."
fi

echo "== 3. Déploiement Netlify (production)"
deploy() {  # $1 dossier, $2 site id, $3 libellé
  echo "  → $3"
  run "netlify deploy --prod --dir=$1 --site=$2 --message \"$MSG\" | grep -E 'Deploy complete|Deployed to production|Website URL|Production URL|Error|error' || true"
}
case "$ONLY" in
  "")        deploy actuarius       "$SITE_EDITIONS" "editionsactuarius.com (FR)"
             deploy actuarius-press "$SITE_PRESS"    "actuariuspress.com (EN)"
             deploy .               "$SITE_ROOT"     "myxavier.finance (racine)" ;;
  editions)  deploy actuarius       "$SITE_EDITIONS" "editionsactuarius.com (FR)" ;;
  press)     deploy actuarius-press "$SITE_PRESS"    "actuariuspress.com (EN)" ;;
  root)      deploy .               "$SITE_ROOT"     "myxavier.finance (racine)" ;;
  *) echo "✘ --only attend root | editions | press"; exit 1 ;;
esac

if [[ $DRY -eq 0 ]]; then
  echo "== 4. Vérifications en production (attendre la propagation CDN, ~30 s)"
  sleep 30
  check() {  # $1 url, $2 motif attendu dans la réponse ("" = code 200 seulement)
    local code body
    body="$(curl -sL --max-time 20 "$1")"; code="$(curl -sL -o /dev/null -w '%{http_code}' --max-time 20 "$1")"
    if [[ "$code" == "200" && ( -z "$2" || "$body" == *"$2"* ) ]]; then echo "  ✔ $1"; else echo "  ✘ $1 (HTTP $code, motif « $2 » ${body:+non trouvé})"; fi
  }
  if [[ -z "$ONLY" || "$ONLY" == "editions" ]]; then
    check "https://www.editionsactuarius.com/covers/chantiers-2027-2028-og.jpg" ""
    check "https://www.editionsactuarius.com/covers/chantiers-2027-2028-recto.jpg" ""
    check "https://www.editionsactuarius.com/covers/chantiers-2027-2028-4e.jpg" ""
    check "https://www.editionsactuarius.com/chantiers-2027-2028/" 'class="bc"'
    check "https://www.editionsactuarius.com/chantiers-2027-2028/" 'og:image" content="https://www.editionsactuarius.com/covers/chantiers-2027-2028-og.jpg'
    check "https://www.editionsactuarius.com/" 'covers/chantiers-2027-2028-recto.jpg'
  fi
  if [[ -z "$ONLY" || "$ONLY" == "press" ]]; then
    check "https://www.actuariuspress.com/2027-2028-agenda/" ""
  fi
  if [[ -z "$ONLY" || "$ONLY" == "root" ]]; then
    check "https://www.myxavier.finance/fr/publications/" 'covers/chantiers-2027-2028-recto.jpg'
  fi
  echo ""
  echo "✅ Terminé. Avant le post LinkedIn 1b : ouvrir https://www.linkedin.com/post-inspector/ et y coller"
  echo "   https://www.editionsactuarius.com/chantiers-2027-2028/ pour forcer LinkedIn à recharger l'og:image (recto navy)."
fi
