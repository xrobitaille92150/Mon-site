# -*- coding: utf-8 -*-
"""Mesure d'audience Umami Cloud pour www.myxavier.finance — source unique.

Sans cookie, sans donnée personnelle : exempté de bandeau de consentement
(délibération CNIL n° 2020-091 ; identifiant visiteur = empreinte hachée avec
un sel quotidien, jamais d'adresse IP stockée). Décision Xavier du 20/09/2026.

Mise en service (une seule fois) :
  1. Créer le compte sur https://cloud.umami.is (plan Hobby, gratuit), ajouter
     le site « www.myxavier.finance » et copier son Website ID (UUID).
  2. Coller l'UUID dans UMAMI_WEBSITE_ID ci-dessous. Vérifier dans l'onglet
     « Tracking code » du tableau de bord que l'URL du script est bien
     UMAMI_SCRIPT ; sinon, la corriger ici.
  3. Lancer ./deploy_actuarius.sh "analytics" : le script s'insère dans les
     deux pages d'accueil (marqueurs <!-- analytics -->) et dans toutes les
     pages générées.

Tant que UMAMI_WEBSITE_ID est vide, aucune balise n'est émise.

Événements suivis (attributs data-umami-event posés sur les liens) :
  calendly  — clic vers la prise de rendez-vous
  email     — clic sur welcome@myxavier.finance
  linkedin  — clic vers le profil LinkedIn
L'attribut data-umami-event-placement précise l'emplacement (hero, contact,
cta, footer).
"""
import os, re, sys

UMAMI_WEBSITE_ID = "ca7b8fbb-2534-4848-83ef-28415b404c16"                                   # ← UUID du site dans Umami Cloud
UMAMI_SCRIPT = "https://cloud.umami.is/script.js"       # URL donnée par l'onglet « Tracking code »
DOMAINS = "www.myxavier.finance"                        # ignore localhost et les Deploy Previews Netlify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PAGES = ["index.html", "fr/index.html"]          # pages non générées
START, END = "<!-- analytics -->", "<!-- /analytics -->"

def snippet():
    """Balise à insérer dans <head> ; chaîne vide tant que l'ID n'est pas renseigné."""
    if not UMAMI_WEBSITE_ID:
        return ""
    return (f'<script defer src="{UMAMI_SCRIPT}" data-website-id="{UMAMI_WEBSITE_ID}" '
            f'data-domains="{DOMAINS}" data-do-not-track="true"></script>')

def head_block():
    """Bloc balisé, pour les pages statiques (remplaçable à chaque exécution)."""
    return f"{START}{snippet()}{END}"

def apply_static():
    """Insère ou remplace le bloc dans les pages d'accueil, juste avant </head>."""
    for rel in STATIC_PAGES:
        path = os.path.join(ROOT, rel)
        s = open(path, encoding="utf-8").read()
        block = "    " + head_block() + "\n"
        if START in s:
            s2 = re.sub(r"[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", block, s, count=1, flags=re.S)
        else:
            if s.count("</head>") != 1:
                sys.exit(f"{rel} : </head> introuvable ou multiple")
            s2 = s.replace("</head>", block + "</head>", 1)
        if s2 != s:
            open(path, "w", encoding="utf-8").write(s2)
        print(f"{rel} : bloc analytics {'actif' if UMAMI_WEBSITE_ID else 'vide (ID non renseigné)'}")

if __name__ == "__main__":
    apply_static()
