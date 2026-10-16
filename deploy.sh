#!/bin/zsh
# Déploiement Xavier Advisory uniquement. Aucun commit automatique ni ajout global.
set -euo pipefail
cd "$(dirname "$0")"

npm run build
npm run verify
./node_modules/.bin/netlify deploy --prod --no-build --dir=dist-advisory --functions=netlify/functions --message="${1:-Mise à jour Xavier Advisory}"
echo "Déploiement terminé. Contrôler : https://www.myxavier.finance/fr/"
