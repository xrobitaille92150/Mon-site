# -*- coding: utf-8 -*-
"""Produit une entree de books_toc.json depuis le blocks.json d'un livre.

books_toc.json est maintenu a la main : ce script evite la ressaisie et
garantit que l'apercu du site reflete exactement le manuscrit construit.

Usage :
  python3 gen/make_toc_entry.py <blocks.json> <book.json> <cle> [--apply]

Sans --apply, affiche un resume sans rien ecrire.
"""
import json, os, re, sys

INTRO_KINDS = {'p', 'q', 'li', 'quote'}

# Le site attend l'etiquette et le titre sur deux lignes distinctes :
#   ['NumroPartie', 'PARTIE I'] puis ['Titre1', 'titre de la partie']
#   ['NumroChapitre', 'CHAPITRE 3'] puis ['Titre2', 'titre du chapitre']
# Les manuscrits, eux, portent tout sur une seule ligne h1/h2.
RE_PART = re.compile(r'^(PARTIE\s+[IVXLC]+|PART\s+[IVXLC]+)\s*[—–-]\s*(.+)$', re.I)
RE_CHAP = re.compile(r'^(Chapitre\s+\d+|Chapter\s+\d+)\s*[.:]\s*(.+)$', re.I)
RE_ANX = re.compile(r'^(Annexe\s+[A-Z]|Appendix\s+[A-Z])\s*[.:—–-]\s*(.+)$', re.I)


def strip_md(t):
    """Retire le gras/italique markdown : la TdM du site est en texte brut."""
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t or '')
    t = re.sub(r'\*(.+?)\*', r'\1', t)
    return t.strip()


def build_titlepage(bk):
    """Reproduit la page de titre + l'amorce de TdM, comme les entrees existantes."""
    def L(s):
        return ["", s]
    title = ' '.join(x for x in (bk.get('title1'), bk.get('title2')) if x)
    sub = ' '.join(x for x in (bk.get('subtitle1'), bk.get('subtitle2')) if x)
    ref = bk.get('refline', '')
    author = bk.get('author', '')
    return [
        L(title), L(sub), L(ref), L(author), L('www.myxavier.fr'),
        L('XAVIER'), L('ADVISORY'),
        L(title), L(sub),
        ["Titre4", ref],
        L(author),
        ["En-ttedetabledesmatires", bk.get('tocTitle', 'Table des matières')],
    ]


def build_toc(blocks):
    out = []
    for b in blocks:
        t = b.get('t')
        txt = strip_md(b.get('text'))
        if not txt or t not in ('h1', 'h2', 'h3', 'h4'):
            continue
        if t == 'h1':
            m = RE_PART.match(txt)
            if m:
                # « PARTIE I — Titre » -> deux lignes.
                out.append(['NumroPartie', m.group(1).upper()])
                out.append(['Titre1', m.group(2).strip()])
            else:
                out.append(['Titre6', txt])          # Introduction, Conclusion...
        elif t == 'h2':
            m = RE_CHAP.match(txt)
            if m:
                out.append(['NumroChapitre', m.group(1).upper()])
                out.append(['Titre2', m.group(2).strip()])
                continue
            m = RE_ANX.match(txt)
            if m:
                # Annexes : le site les rend apres le dernier chapitre.
                out.append(['NumroChapitre', m.group(1).upper()])
                out.append(['Titre7', m.group(2).strip()])
            else:
                out.append(['Titre2', txt])
        elif t == 'h3':
            continue      # les sections N.N ne figurent pas dans la TdM du site
        else:
            out.append(['Titre7', txt])              # annexes
    return out


def build_intro(blocks, limit=21):
    """Les premiers paragraphes de l'introduction, pour l'apercu du site."""
    out, started = [], False
    for b in blocks:
        t = b.get('t')
        if t == 'h1' and not started:
            started = True
            continue
        if not started:
            continue
        if t in ('h1', 'part', 'chapter'):
            break
        if t in INTRO_KINDS:
            txt = strip_md(b.get('text'))
            if txt:
                out.append(['q' if not out else 'p', txt])
        if len(out) >= limit:
            break
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    apply_ = '--apply' in sys.argv
    if len(args) < 3:
        print(__doc__)
        sys.exit(1)
    blocks_p, book_p, key = args[0], args[1], args[2]

    blocks = json.load(open(blocks_p, encoding='utf-8'))
    bk = json.load(open(book_p, encoding='utf-8'))

    entry = {
        'titlepage': build_titlepage(bk),
        'toc': build_toc(blocks),
        'pages': None,
        'intro': build_intro(blocks),
    }

    print(f"cle           : {key}")
    print(f"titre         : {bk.get('title1')} {bk.get('title2')}")
    print(f"entrees TdM   : {len(entry['toc'])}")
    print(f"paragr. intro : {len(entry['intro'])}")
    if entry['toc'][:3]:
        print("debut TdM     :", entry['toc'][:3])
    if not entry['toc']:
        print("!! aucune entree de TdM — verifier les styles du blocks.json")
        sys.exit(2)

    if not apply_:
        print("\n(simulation — relancer avec --apply pour ecrire)")
        return

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'books_toc.json')
    data = json.load(open(dest, encoding='utf-8'))
    data[key] = entry
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"\necrit dans books_toc.json — cles : {list(data)}")


if __name__ == '__main__':
    main()
