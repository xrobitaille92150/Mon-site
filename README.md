# Mon-site — Xavier Advisory

Site bilingue publié sur https://www.myxavier.finance. Refonte du 16 octobre 2026.

## Construction et déploiement

Node 22 et Python 3.12 sont requis. Installer les dépendances avec `npm ci`, puis lancer `npm run build` et `npm run verify`. Le répertoire de publication est **`dist-advisory/`**, jamais la racine du dépôt. `./deploy.sh "message"` construit, contrôle et publie uniquement ce site ; le script ne crée aucun commit et ne modifie pas les journaux.

Les anciens fichiers HTML à la racine sont conservés comme références historiques. Ils ne sont plus la source de la version publiée. Les sites Éditions Actuarius et Actuarius Press restent distincts : ne pas leur appliquer ce déploiement.

## Sources

- `gen/build_advisory.py` : structure, pages et métadonnées.
- `gen/advisory_content.py` : missions, domaines et ressources FR/EN.
- `gen/advisory_expertise.py` : expertises détaillées.
- `gen/advisory_translations.py` : versions anglaises des articles.
- `assets/advisory.css` / `advisory.js` : interface, animations, filtres, démonstration, consentement d’audience.
- `assets/members.source.js` : compte abonné ; `members.js` est généré.
- `netlify/functions/member-download.mjs` : téléchargement après vérification du compte confirmé.
- Stockage privé Netlify Blobs `xa-member-templates-v1` : huit fichiers Excel originaux, servis uniquement par la fonction après vérification du compte confirmé. Ne pas ajouter leur contenu au dépôt public. Mise à jour : `netlify blobs:set xa-member-templates-v1 NOM-fr.xlsx --input CHEMIN_ABSOLU` (même principe pour EN).

L’espace est gratuit, avec confirmation de l’email. L’inscription n’abonne à aucune newsletter. Ne pas remplacer la vérification serveur par un simple masquage des liens. Aucun document client, CV source ou secret ne doit entrer dans le répertoire de publication.

## Vérification

`npm run verify` contrôle les liens internes, les ressources, les titres, les H1, les descriptions, les URL canoniques et les données structurées. La recette fonctionnelle couvre aussi FR/EN, le mobile, les filtres, la démonstration, la confirmation d’un compte et les téléchargements autorisés/refusés. Un déploiement réussi ne prouve ni l’indexation ni une hausse des demandes de mission.
