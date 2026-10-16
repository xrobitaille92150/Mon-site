# Xavier Advisory — site myxavier.finance

Lire les règles globales et `CLAUDE.md`. Ce fichier ne concerne que ce dépôt.

## Validation locale et consommation Netlify

Décision de travail du 16 octobre 2026 : regrouper les modifications et faire valider la page dans un aperçu local avant de publier le lot.

- Utiliser `npm run preview` pour construire, tester et servir uniquement `dist-advisory/` sur `127.0.0.1:3000`. Si le serveur existe, le réutiliser ; après une correction, relancer `npm run build && npm run verify` et actualiser le navigateur.
- Les fonctions serveur et le parcours abonné complet ne sont pas simulés par cet aperçu statique. Prévoir les contrôles adaptés au lot avant/après publication.
- Ne pas publier chaque annotation séparément. Attendre la validation explicite de Xavier du lot/page avant une mise en production.
- Les commits intermédiaires envoyés à GitHub portent `[skip netlify]` pour éviter un déploiement automatique. Cette marque concerne les déploiements, pas la sauvegarde du code.
- Un seul canal de publication par lot : soit Git, soit l’envoi manuel. Ne jamais faire les deux pour la même version.
- Pour un envoi manuel après validation, construire/tester localement puis utiliser `./deploy.sh "message du lot validé"`, sans nouveau push déclenchant aussi une publication automatique.
- Vérifier la version publique après publication. Un succès de commande ne suffit pas.
- Ne modifier ni abonnement, ni recharge automatique, ni budget, ni réglages du compte Netlify sans demande explicite de Xavier. Ne pas désactiver globalement les builds à son insu.

La version courante conserve l’anonymisation des retours d’expérience et des tiers, la séparation des trois compétences comptables et le bilinguisme FR/EN.
