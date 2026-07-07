# Plan d'action — xavier-robitaille.fr

*Audit du 2 juillet 2026. Repo Mon-site = production (vérifié). Benchmarks : SeaBird, Nexialog, VNCA.*

**État au 2 juillet, fin de journée : P0, P1 et P2 livrés et déployés sur www.myxavier.finance** (rebranding Xavier Advisory inclus — domaine, email welcome@, DNS Hostinger, 301 depuis xavier-robitaille.fr). Restent : P3 (sous-pages expertise), P4 (SEO continu, Search Console), P5 (effets). Déploiement auto GitHub→Netlify suspendu tant que le flag GitHub n'est pas levé (support contacté) ; déploiement manuel : `npx netlify-cli deploy --prod --dir .`

**État au 7 juillet : P3, P5 et P3.6 livrés.** P3 : 5 sous-pages expertise EN+FR + section Insights + article TIE/EIR (03/07). P5 : compteurs animés, grain hero, purge du bleu hors charte — décision n°3 tranchée : supprimé (07/07, commit `945caff`). P3.6 : page `/formation/` + `/fr/formation/` (IA pour les professionnels de la finance), nav Training/Formation, sitemap 18 URLs (07/07, commit `cb1dc86`). **Restent** : P4 continu (vérification Search Console — action Xavier ; 2-3 articles de fond), image OG à tester avec LinkedIn Post Inspector. ⚠️ Le déploiement auto GitHub→Netlify ne fonctionne toujours pas. Diagnostic du 07/07 (Netlify + GitHub vérifiés en session) : l'auto-publish est actif et chaque push déclenche un build, mais tous échouent à « preparing repo » (*Unable to access repository*). Cause racine : **le compte GitHub est toujours flaggé** (« This account is flagged, and therefore cannot authorize a third party application ») → l'autorisation Netlify ne peut pas être renouvelée. Action Xavier : relancer le ticket support GitHub. En attendant : déployer via `./deploy.sh` après chaque push.

---

## Synthèse

Le site est solide sur le fond (positionnement rare, preuves, SEO technique correct) mais il présente trois défauts :

1. **Il date** : « Available from June 2026 » partout alors qu'on est en juillet. Un prospect conclut à un site abandonné.
2. **Il ignore le Brand Book** : palette et typographie n'ont aucun rapport avec la charte Xavier Advisory.
3. **Il est plat en profondeur** : one-page sans sous-pages, donc aucune position SEO possible sur « consultant IFRS 17 », « SimCorp Dimension consultant », « Clearwater implementation », etc.

Ordre de traitement : P0 (corrections, 1h) → P1 (brand, 1 session) → P2 (réécriture, 1 session) → P3 (sous-pages, 2-3 sessions) → P4 (SEO continu) → P5 (effets, 1 session).

---

## P0 — Corrections immédiates (avant tout le reste)

| # | Action | Détail |
|---|---|---|
| 0.1 | Remplacer toutes les mentions « June 2026 » / « juin 2026 » | « Available now » / « Disponible immédiatement ». 5+ occurrences EN, 5+ FR. |
| 0.2 | Reformuler « Transitioning from an active 18-month engagement » | En preuve livrée : « Just delivered an 18-month Clearwater Analytics implementation — OMS go-live Dec 2025, Core go-live Jan 2026 ». |
| 0.3 | Corriger « ClearWater » → « Clearwater » | 2 occurrences minimum par langue (section expertise 05 + Full Coverage). |
| 0.4 | **Décision Xavier** : TJM « €1k Daily Rate » en hero | Recommandation : retirer. Ancre la négociation vers le bas (facturations passées > 1 200 €) et gêne les mandats internationaux. Remplacer par « Immediate availability » ou « 25+ yrs — zero ramp-up ». |
| 0.5 | **Décision Xavier** : email | Site : `xro@xavier-robitaille.fr`. context.md : `xro@xavier-robitaille.com`. Confirmer lequel reçoit les messages. |
| 0.6 | Image OG 1200×630 | Créer à partir de IMG_6047 + logo + tagline. Tester avec LinkedIn Post Inspector après déploiement. (Reste ouvert depuis le 15 mai.) |

## P1 — Alignement Brand Book

Le site utilise une identité qui n'existe pas dans la charte :

| Élément | Brand Book Xavier Advisory | Site actuel |
|---|---|---|
| Navy | `#0B1530` | `#060756` / texte `#111349` |
| Gold | `#C79A3B` | `#C4922C` / `#D4A94A` |
| Fond clair | Ivory `#F5F2EB` | Gris froid `#F4F4F7` |
| Accent | — (pas de bleu dans la charte) | Bleu `#3773FE` |
| Titres | Playfair Display (serif) | Figtree |
| Corps | Montserrat | Figtree |

Actions :

- Basculer les variables CSS `:root` sur la palette charte (navy, gold, ivory, light-grey `#E6EBEC`).
- Charger Playfair Display pour les titres, Montserrat pour le corps. Supprimer Figtree.
- Statuer sur le bleu `#3773FE` : hors charte. Le supprimer ou l'entériner dans le Brand Book.
- Vérifier le rendu écran par écran (workflow screenshot localhost, 2 passes minimum, cf. CLAUDE.md du repo).

Bénéfice secondaire : le duo serif/sans respecte la règle anti-générique du repo (interdiction d'une police unique), aujourd'hui violée.

## P2 — Réécriture du contenu existant

Positionnement : le site vendait « occupé et bientôt libre ». Il doit vendre « vient de livrer, opérationnel dès demain ».

- **Hero** : intégrer la livraison Clearwater comme preuve fraîche. Chiffres disponibles : 18 mois, 2 go-lives tenus (déc. 2025, janv. 2026), gouvernance C-suite, environnement multi-dépositaires.
- **Section Profile** : ajouter PMP (2025) et certificats GenAI (Vanderbilt, Yale 2026). Le PMP crédibilise le volet PMO ; l'IA différencie (« AI-driven investment reporting » est déjà mentionné mais sans preuve).
- **Section Approach** : ajouter un bloc « réalisations » chiffré. Matière disponible : CCR/Clearwater (ci-dessus), Coface IFRS 9 (4 ans, ECL, coordination CACEIS), CNP (fast-close investissements, SimCorp Palladio), SCOR (SimCorp full-stack, budget 3 M€).
- **Passer les deux versions au filtre des règles d'écriture** (REGLES-ECRITURE-FR / WRITING RULES) : chasse aux nominalisations, au vocabulaire gonflé (« structurally rare » est bien ; vérifier le reste).
- Parité FR/EN stricte après réécriture.

## P3 — Sous-pages expertise (le chantier de fond)

Ce que font les trois concurrents et pas le site :

| Pratique | SeaBird | Nexialog | VNCA | Site XR |
|---|---|---|---|---|
| Pages expertise dédiées | 4 | 7 | 7 | 0 |
| Pages secteur | 2 | 2 | — | 0 |
| Publications / articles | Oui (Décryptons, labs) | Oui (newsletters, R&D) | Oui | 0 |
| Réalisations / cas clients | Études de cas | Logos + chiffres | « Nos réalisations » | Logos seuls |
| Offre formation | Oui | — | Oui (catalogue) | 0 |

Pages à créer, par ordre de valeur SEO et commerciale :

1. `/expertise/ifrs-17-ifrs-9-solvency-ii/` — le mot-clé le plus cherché du positionnement. Matière : AXA (TOM, dry-run, ORSA), Coface ECL.
2. `/expertise/simcorp-clearwater/` — requête ultra-niche, quasi aucun consultant indépendant positionné dessus. Matière : SCOR, CNP Palladio, CCR/Luxempart. Deux plateformes majeures implémentées = argument unique.
3. `/expertise/investment-accounting-reporting/` — sous-ledger titres, schémas comptables, ALM, réconciliations.
4. `/expertise/pmo-programme-delivery/` — gouvernance, RAID, SteerCo C-suite, bilingue. Appuyer sur le PMP.
5. `/expertise/interim-management/` — CNP 4 ans, Coface Head of Technical Accounting (16 personnes).
6. Optionnel, lié à la priorité 5 : `/formation/` — l'IA pour les professionnels de la finance. SeaBird et VNCA ont un onglet Formations ; c'est un standard du secteur, pas une excentricité.

Chaque page : 600-900 mots, structure problème → intervention → résultats chiffrés, maillage vers Contact, version FR + EN, entrée sitemap + hreflang.

À terme (P4 continu) : 2-3 articles de fond réutilisant les livrables existants (ex. « Les pièges d'une implémentation OMS », « ECL : ce que 4 ans chez un credit insurer enseignent »). C'est le levier crédibilité + SEO que les trois concurrents exploitent.

## P4 — SEO

- Title FR actuel OK, méta description OK. Après création des sous-pages : title + méta uniques par page.
- Sitemap.xml à étendre aux nouvelles pages ; ping Google Search Console.
- Schema.org : ajouter `Service` par page expertise (Person + ProfessionalService déjà en place).
- Alt text des 19 logos clients : vides aujourd'hui (`![]()`). Nommer les clients citables → signal SEO gratuit.
- Vérifier l'indexation actuelle (Search Console) avant/après.

## P5 — Effets et finitions

Dans les limites des règles du repo (transform/opacity uniquement, pas de `transition-all`) :

- Révélations au scroll (IntersectionObserver) sur les cartes expertise et les chiffres.
- Compteurs animés sur les stats (25+, 3×...).
- Ombres teintées navy en système de profondeur (base → élevé → flottant).
- Grain/texture légère sur le hero (SVG noise) pour l'effet premium.
- Micro-interactions hover sur toutes les cartes cliquables.

---

## Décisions attendues de Xavier

1. TJM affiché en hero : retirer ou garder ? (0.4)
2. Email de contact : `.fr` ou `.com` ? (0.5)
3. Bleu `#3773FE` : supprimer ou l'ajouter officiellement à la charte ? (P1)
4. Page Formation IA : dans le périmètre ou plus tard ? (P3.6)
