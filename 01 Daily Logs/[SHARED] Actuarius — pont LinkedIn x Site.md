# [SHARED] Actuarius — ressources communes projets « Présence LinkedIn » et « Mon site »
*Créé le 25/08/2026 par la session LinkedIn. Version canonique : Drive `_shared/daily_logs/[SHARED] Actuarius — pont LinkedIn x Site.md` (id 1gG1GnvFYaoUGV38LErXGEjeN9VKqx4gY). Cette copie est un pointeur pour la session Site.*

## L'essentiel pour la session Site

- Les pages livres sont les CTA des posts LinkedIn des 01 et 03/09 — **ne pas changer ces URL** (301 sinon) :
  - FR : https://www.editionsactuarius.com/chantiers-2027-2028/
  - EN : https://www.actuariuspress.com/2027-2028-agenda/ (page créée le 25/08, commit 863d8b8)
- Dates réglementaires de référence (vérifiées sources officielles le 25/08) : IRRD (2025/1) et S2 révisée (2025/2) = transposition ≤ 29/01/2027, APPLICATION 30/01/2027 ; WS2016 : 12/01/2027. Corrigé sur la page FR (commit 186f79a). Garder `books_toc.json` clés `transformations` et `transformations-en` synchrones.
- Lexique : « traité » banni ; « mises en pension » (FR) / « repo » ; livre obligations HORS communication.
- Trafic entrant attendu : posts LinkedIn 01/09 8h30 et 03/09 8h30, puis 2-3/semaine ; lancement commercial courant septembre. Étage suivant du funnel : formulaire chapitre offert contre email (HubSpot) sur les pages livres.
- Journal détaillé côté LinkedIn : projet claude.ai « Présence LinkedIn », doc `claude/journal-operations.md`.
- `_to_delete/` à la racine du repo : verrous git orphelins déposés par la VM du pont (pas de droit de suppression) — à vider.

Détail complet (inventaire, interfaces, points ouverts) : voir la version canonique sur le Drive.

## Couverture et 4e de couverture finales (version navy) — 01/09/2026, session « 4e de couverture »

- **Source unique** : Claude Design « Couverture de livre française », piste **1b navy**, texte de 4e final de Xavier (31/08).
  Fichiers source (HTML export + assets) archivés dans `10_Work/Livres/transformations_2027-2028/couverture/source_design/`.
  ⚠ Les PNG `export/1b-*.png` du zip Claude Design sont **périmés** (ancien texte « Tout part de là ») : ne jamais les réutiliser ;
  les finaux ont été rendus depuis les HTML.
- **Fichiers finaux** (`10_Work/Livres/transformations_2027-2028/couverture/`) : `Couverture_1b_navy_FINALE_recto.png`,
  `_4e.png`, `_dos.png` — 2240 × 3176 px (A5 à ≈ 384 dpi), dos 140 px.
- **Site** (repo Mon-site, build du 01/09, **non commité, non déployé**) : couverture réelle à la place du SVG fictif partout où le livre
  apparaît (accueil editionsactuarius.com, catalogue myxavier.finance/fr/publications, page livre), nouvelle section
  « Quatrième de couverture » (image + texte HTML) sur `editionsactuarius.com/chantiers-2027-2028/`, `og:image` de la page livre =
  recto navy (aperçu du lien LinkedIn). Assets : `brand_assets/actuarius/covers/` → copiés par le build dans `actuarius/covers/`.
  Générateur : champs `cover_img`, `back_img`, `og_img`, `backcover` dans `publications_data.BOOKS`, helper `cover_html()`.
  Page EN `actuariuspress.com/2027-2028-agenda/` : inchangée sur le fond (CSS seulement).
- **LinkedIn** : visuels du post 1b dans `10_Work/LinkedIn/visuels/Livre_2027-2028/` (recto et 4e en 1080×1350, spread 1200×628) ;
  fiche Airtable 1b (recKnGeA0d3uAv3xf) mise à jour. Le rendu 3D du 24/08 portait un sous-titre périmé (IRRD) : à regénérer ou à
  abandonner.
- **Incohérence à trancher** : le site affiche « Aperçu — Parution août 2026 » (`ui['release']`, `datePublished 2026-08`) ; les posts et
  le rendu 3D disent « septembre 2026 ». À aligner avant le 03/09.
- **Séquence avant le post 1b (03/09)** : Xavier commit + déploie Netlify (editionsactuarius + racine myxavier.finance) → vérifier
  `https://www.editionsactuarius.com/covers/chantiers-2027-2028-og.jpg` → poster avec les 2 images.
