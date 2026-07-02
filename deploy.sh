#!/bin/zsh
# Déploiement manuel du site — contourne l'intégration GitHub↔Netlify (gelée par le flag GitHub).
# Usage : ./deploy.sh "message de commit"   (ou double-clic sur "Déployer myxavier — Claude.command")
set -e
cd "$(dirname "$0")"

MSG="${1:-Mise à jour du site}"

rm -f .git/index.lock .git/HEAD.lock 2>/dev/null || true

if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "$MSG"
  echo "✔ Commit créé : $MSG"
else
  echo "ℹ Aucun changement à committer."
fi

git push origin main && echo "✔ Poussé sur GitHub (sauvegarde du code)" || echo "⚠ Push GitHub échoué — le déploiement continue quand même."

npx -y netlify-cli deploy --prod --dir . | grep -E "Deploy complete|Production URL|Error" || true
echo ""
echo "✅ Terminé. Vérifie : https://www.myxavier.finance"
