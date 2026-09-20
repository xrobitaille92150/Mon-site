# -*- coding: utf-8 -*-
"""Données légales partagées par les trois sites.

Source : avis de situation INSEE du 14/08/2026 + confirmations Xavier.
Toute page légale (mentions, confidentialité, CGV) se génère à partir
de ce module : une correction ici se propage partout.
"""

COMPANY = dict(
    name="Expert Zone Finance Group",
    forme="SAS (société par actions simplifiée)",
    forme_en="SAS (société par actions simplifiée, a French simplified "
             "joint-stock company)",
    capital="100 €",
    capital_en="EUR 100",
    siege="47 rue Vivienne, 75002 Paris, France",
    siren="106 290 687",
    siret="106 290 687 00016",
    rcs="RCS Paris 106 290 687",
    rcs_en="Paris Trade and Companies Register (RCS Paris) no. 106 290 687",
    tva="FR93 106 290 687",
    naf="70.22Z — Conseil pour les affaires et autres conseils de gestion",
    email="welcome@myxavier.finance",
    tel="+33 6 64 89 09 43",
    directeur="Xavier Robitaille, Président",
    directeur_en="Xavier Robitaille, President",
)

HOST = dict(
    name="Netlify, Inc.",
    addr="101 2nd Street, San Francisco, CA 94105, États-Unis",
    addr_en="101 2nd Street, San Francisco, CA 94105, United States",
    email="support@netlify.com",
    url="https://www.netlify.com",
)

# Marques exploitées par la société.
BRANDS_NOTE_FR = ("<strong>Xavier Advisory</strong> est le nom commercial "
                  "sous lequel Expert Zone Finance Group exerce son activité "
                  "de conseil. <strong>Éditions Actuarius</strong> et "
                  "<strong>Actuarius Press</strong> sont ses marques "
                  "d'édition.")
BRANDS_NOTE_EN = ("<strong>Xavier Advisory</strong> is the trade name under "
                  "which Expert Zone Finance Group carries out its advisory "
                  "business. <strong>Éditions Actuarius</strong> and "
                  "<strong>Actuarius Press</strong> are its publishing "
                  "imprints.")

UPDATED_FR = "14 août 2026"
UPDATED_EN = "14 August 2026"

# Politique de confidentialité du site vitrine (ajout de la mesure d'audience Umami).
PRIVACY_UPDATED_FR = "20 septembre 2026"
PRIVACY_UPDATED_EN = "20 September 2026"
