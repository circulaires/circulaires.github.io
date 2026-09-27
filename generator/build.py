# -*- coding: utf-8 -*-
"""
Générateur du site statique « Circulaires Hebdo » (nom provisoire — à changer
dans SITE_NOM ci-dessous si vous voulez autre chose).

Utilisation :
    python3 build.py

Régénère TOUT le site dans ../ (racine du dépôt), à partir de :
  - data/magasins.json      → liste des magasins (slug, nom, couleur, type)
  - data/highlights/*.json  → (optionnel) aubaines réelles de la semaine par magasin
  - contenu.py               → banque de textes originaux par catégorie

Le site est 100% statique (HTML/CSS, aucun PHP, aucune base de données) afin
d'être compatible avec GitHub Pages. Pour que « cette semaine » / « semaine
prochaine » restent à jour, relancez ce script chaque semaine (voir le workflow
GitHub Actions fourni dans .github/workflows/regenerer.yml qui le fait pour vous).
"""
import json, os, re, hashlib, html
from datetime import date, timedelta
from pathlib import Path

import contenu

ROOT = Path(__file__).resolve().parent.parent  # racine du dépôt
GEN = Path(__file__).resolve().parent
DATA = GEN / "data"

SITE_NOM = "Circulaires Hebdo Canada"
SITE_SLOGAN = "Le résumé des circulaires de vos magasins, semaine après semaine"
SITE_URL = "https://circulaires.github.io"  # ajustez si vous utilisez un domaine personnalisé
SITE_DESCRIPTION = "Circulaires Hebdo Canada résume chaque semaine les aubaines des magasins canadiens : épicerie, pharmacie, quincaillerie et plus, avec un aperçu de la semaine en cours et de la semaine prochaine."

# ────────────────────────────────────────────────────────────────────────────
# Dates : semaine du jeudi au mercredi, comme les circulaires habituelles
# ────────────────────────────────────────────────────────────────────────────
def debut_semaine_courante(today: date) -> date:
    # jeudi = weekday() 3 (lundi=0)
    jours_depuis_jeudi = (today.weekday() - 3) % 7
    return today - timedelta(days=jours_depuis_jeudi)

TODAY = date.today()
DEBUT_COURANTE = debut_semaine_courante(TODAY)
FIN_COURANTE = DEBUT_COURANTE + timedelta(days=6)
DEBUT_PROCHAINE = DEBUT_COURANTE + timedelta(days=7)
FIN_PROCHAINE = DEBUT_PROCHAINE + timedelta(days=6)

MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet",
           "août", "septembre", "octobre", "novembre", "décembre"]

def fmt_date(d: date) -> str:
    return f"{d.day} {MOIS_FR[d.month]}"

def fmt_periode(d1: date, d2: date) -> str:
    if d1.month == d2.month:
        return f"du {d1.day} au {fmt_date(d2)}"
    return f"du {fmt_date(d1)} au {fmt_date(d2)}"

PERIODE_COURANTE = fmt_periode(DEBUT_COURANTE, FIN_COURANTE)
PERIODE_PROCHAINE = fmt_periode(DEBUT_PROCHAINE, FIN_PROCHAINE)

# ────────────────────────────────────────────────────────────────────────────
# Données
# ────────────────────────────────────────────────────────────────────────────
with open(DATA / "magasins.json", encoding="utf-8") as f:
    MAGASINS = json.load(f)

MAGASINS.sort(key=lambda s: s["nom"])
PAR_SLUG = {s["slug"]: s for s in MAGASINS}

def pige(slug: str, liste, sel: int = 0):
    """Choix déterministe (mais varié) d'une variante de texte selon le slug."""
    h = int(hashlib.md5(f"{slug}-{sel}".encode()).hexdigest(), 16)
    return liste[h % len(liste)]

def highlights_reels(slug: str):
    p = DATA / "highlights" / f"{slug}.json"
    if p.exists():
        try:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

def esc(s: str) -> str:
    return html.escape(s, quote=True)

# ────────────────────────────────────────────────────────────────────────────
# Gabarit HTML commun
# ────────────────────────────────────────────────────────────────────────────
def page(titre, description, canonical, corps, *, couleur="#B4562A", og_type="website",
         jsonld=""):
    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titre)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(SITE_NOM)}">
<meta property="og:title" content="{esc(titre)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="{couleur}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
{jsonld}
</head>
<body style="--marque: {couleur}">
<header class="entete">
  <div class="entete-int">
    <a href="/" class="logo">
      <span class="logo-icone" aria-hidden="true">🗞️</span>
      <span class="logo-texte">{esc(SITE_NOM)}</span>
    </a>
    <nav class="nav">
      <a href="/">Accueil</a>
      <a href="/magasins/">Tous les magasins</a>
      <a href="/a-propos/">À propos</a>
    </nav>
  </div>
</header>
<main>
{corps}
</main>
<footer class="pied">
  <div class="pied-int">
    <p>{esc(SITE_NOM)} — {esc(SITE_SLOGAN)}.</p>
    <nav class="pied-nav">
      <a href="/">Accueil</a>
      <a href="/magasins/">Magasins</a>
      <a href="/a-propos/">À propos</a>
      <a href="/conditions-utilisation/">Conditions d'utilisation</a>
      <a href="/confidentialite/">Confidentialité</a>
      <a href="/sitemap.xml">Plan du site</a>
    </nav>
    <p class="pied-legal">Site indépendant à titre informatif seulement. Les noms de magasins appartiennent à leurs détenteurs respectifs. Vérifiez toujours les prix et conditions en succursale.</p>
  </div>
</footer>
</body>
</html>"""

def carte_magasin(m, sous_titre=""):
    lettre = m["nom"][0].upper()
    return f"""<a class="carte-magasin" href="/circulaire/{m['slug']}/" style="--marque:{m['couleur']}">
  <span class="carte-mockup" aria-hidden="true">
    <span class="carte-mockup-initiale">{esc(lettre)}</span>
  </span>
  <span class="carte-corps">
    <span class="carte-nom">{esc(m['nom'])}</span>
    <span class="carte-type">{esc(m['type'])}</span>
    {f'<span class="carte-sous">{esc(sous_titre)}</span>' if sous_titre else ''}
  </span>
</a>"""

def mockup_catalogue(m, periode, badge):
    """Bloc décoratif CSS façon « livret de circulaire » — aucune image, juste le nom du magasin."""
    lettre = m["nom"][0].upper()
    return f"""<div class="mockup-livret" style="--marque:{m['couleur']}">
  <div class="mockup-couverture">
    <span class="mockup-badge">{esc(badge)}</span>
    <span class="mockup-initiale">{esc(lettre)}</span>
    <span class="mockup-nom">{esc(m['nom'])}</span>
    <span class="mockup-periode">{esc(periode)}</span>
  </div>
  <div class="mockup-page mockup-page-2" aria-hidden="true"></div>
  <div class="mockup-page mockup-page-3" aria-hidden="true"></div>
</div>"""

def rayons_html(rayons):
    li = "\n".join(
        f'<li><strong>{esc(nom)}</strong><span>{esc(txt)}</span></li>'
        for nom, txt in rayons
    )
    return f'<ul class="liste-rayons">{li}</ul>'

def faq_html(slug, faq, jsonld_id):
    items = "\n".join(
        f"""<details class="faq-item">
  <summary>{esc(q)}</summary>
  <p>{esc(r)}</p>
</details>""" for q, r in faq
    )
    jsonld_entities = ",\n".join(f'''{{
  "@type": "Question",
  "name": {json.dumps(q, ensure_ascii=False)},
  "acceptedAnswer": {{"@type": "Answer", "text": {json.dumps(r, ensure_ascii=False)}}}
}}''' for q, r in faq)
    jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{jsonld_entities}]}}
</script>"""
    return f'<section class="bloc-faq"><h2>Questions fréquentes</h2>{items}</section>', jsonld

def internes_meme_categorie(m, n=6):
    memes = [x for x in MAGASINS if x["type"] == m["type"] and x["slug"] != m["slug"]]
    h = int(hashlib.md5(m["slug"].encode()).hexdigest(), 16)
    memes = sorted(memes, key=lambda x: x["slug"])
    if not memes:
        return []
    start = h % len(memes)
    out = []
    for i in range(min(n, len(memes))):
        out.append(memes[(start + i) % len(memes)])
    return out

# ────────────────────────────────────────────────────────────────────────────
# Page magasin (cette semaine / semaine prochaine)
# ────────────────────────────────────────────────────────────────────────────
def page_magasin(m, semaine_prochaine=False):
    slug = m["slug"]
    cat = contenu.CATEGORIES.get(m["type"], contenu.CATEGORIES["Magasin général"])
    intro = pige(slug, cat["intros"], 1)
    rayons = pige(slug, cat["rayons"], 2)
    conseil = pige(slug, cat["conseils"], 3)
    faq = pige(slug, cat["faqs"], 4)

    periode = PERIODE_PROCHAINE if semaine_prochaine else PERIODE_COURANTE
    intro_txt = intro.format(nom=m["nom"], periode="de la semaine prochaine" if semaine_prochaine else "de cette semaine")
    faq_txt = [(q.format(nom=m["nom"]), r.format(nom=m["nom"])) for q, r in faq]

    reel = highlights_reels(slug)
    badge = "En primeur — semaine prochaine" if semaine_prochaine else "Cette semaine"
    url_path = f"/circulaire/{slug}/semaine-prochaine/" if semaine_prochaine else f"/circulaire/{slug}/"
    canonical = SITE_URL + url_path

    titre = f"Circulaire {m['nom']} — {'semaine prochaine' if semaine_prochaine else 'cette semaine'} ({periode}) | {SITE_NOM}"
    description = f"Circulaire {m['nom']} {'de la semaine prochaine' if semaine_prochaine else 'de cette semaine'} ({periode}) : aperçu des rayons et aubaines à surveiller."

    mockup = mockup_catalogue(m, periode, badge)

    # section aubaines réelles (si un fichier highlights a été rempli pour cette semaine)
    aubaines_html = ""
    if reel and reel.get("aubaines") and reel.get("semaine") == ("prochaine" if semaine_prochaine else "courante"):
        li = "\n".join(f"<li>{esc(a)}</li>" for a in reel["aubaines"])
        aubaines_html = f"""<section class="bloc-aubaines">
  <h2>Aubaines repérées {('pour la semaine prochaine' if semaine_prochaine else 'cette semaine')}</h2>
  <ul class="liste-aubaines">{li}</ul>
</section>"""

    lien_autre = f'<a class="bouton-secondaire" href="/circulaire/{slug}/">← Voir la circulaire de cette semaine</a>' if semaine_prochaine \
        else f'<a class="bouton-secondaire" href="/circulaire/{slug}/semaine-prochaine/">Voir la semaine prochaine en primeur →</a>'

    autres = internes_meme_categorie(m)
    autres_html = ""
    if autres:
        cartes = "\n".join(carte_magasin(a) for a in autres)
        autres_html = f"""<section class="bloc-autres">
  <h2>Autres circulaires « {esc(m['type'])} »</h2>
  <div class="grille-cartes">{cartes}</div>
</section>"""

    faq_section, faq_jsonld = faq_html(slug, faq_txt, slug)

    jsonld_page = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
 {{"@type":"ListItem","position":1,"name":"Accueil","item":"{SITE_URL}/"}},
 {{"@type":"ListItem","position":2,"name":"Magasins","item":"{SITE_URL}/magasins/"}},
 {{"@type":"ListItem","position":3,"name":"{esc(m['nom'])}","item":"{canonical}"}}
]}}
</script>
{faq_jsonld}"""

    corps = f"""
<nav class="fil-ariane"><a href="/">Accueil</a> › <a href="/magasins/">Magasins</a> › <span>{esc(m['nom'])}</span></nav>
<article class="page-magasin">
  <div class="entete-magasin">
    <div class="entete-magasin-texte">
      <p class="etiquette">{esc(m['type'])}</p>
      <h1>Circulaire {esc(m['nom'])} <span class="souligne">{ 'semaine prochaine' if semaine_prochaine else 'cette semaine' }</span></h1>
      <p class="periode">{esc(periode)}</p>
      <p class="intro">{esc(intro_txt)}</p>
      {lien_autre}
    </div>
    {mockup}
  </div>

  {aubaines_html}

  <section class="bloc-rayons">
    <h2>Ce qu'on surveille {('la semaine prochaine' if semaine_prochaine else 'cette semaine')} chez {esc(m['nom'])}</h2>
    {rayons_html(rayons)}
  </section>

  <section class="bloc-conseil">
    <h2>Conseil de la semaine</h2>
    <p>{esc(conseil)}</p>
  </section>

  {faq_section}

  {autres_html}
</article>
"""
    return page(titre, description, canonical, corps, couleur=m["couleur"], jsonld=jsonld_page), url_path

# ────────────────────────────────────────────────────────────────────────────
# Page d'accueil
# ────────────────────────────────────────────────────────────────────────────
def page_accueil():
    h = int(hashlib.md5(str(TODAY).encode()).hexdigest(), 16)
    vedette = sorted(MAGASINS, key=lambda s: s["slug"])
    start = h % len(vedette)
    en_vedette = [vedette[(start + i) % len(vedette)] for i in range(18)]
    cartes = "\n".join(carte_magasin(m, "cette semaine") for m in en_vedette)

    categories = sorted(set(m["type"] for m in MAGASINS))
    cat_html = "\n".join(
        f'<a class="puce-categorie" href="/magasins/#{re.sub(r"[^a-z0-9]+","-",c.lower())}">{esc(c)} <span>({sum(1 for m in MAGASINS if m["type"]==c)})</span></a>'
        for c in categories
    )

    corps = f"""
<section class="heros">
  <h1>{esc(SITE_NOM)}</h1>
  <p class="heros-slogan">{esc(SITE_SLOGAN)}. Un résumé clair de {len(MAGASINS)} magasins canadiens, semaine après semaine — {esc(PERIODE_COURANTE)}.</p>
  <a class="bouton-principal" href="/magasins/">Parcourir tous les magasins</a>
</section>

<section class="bloc-categories">
  <h2>Par catégorie</h2>
  <div class="puces-categories">{cat_html}</div>
</section>

<section class="bloc-vedette">
  <h2>En vedette cette semaine ({esc(PERIODE_COURANTE)})</h2>
  <div class="grille-cartes grille-cartes-accueil">{cartes}</div>
  <p class="voir-tout"><a href="/magasins/">Voir les {len(MAGASINS)} magasins →</a></p>
</section>

<section class="bloc-explication">
  <h2>Comment fonctionne ce site</h2>
  <div class="explication-grille">
    <div>
      <h3>Une page par magasin, chaque semaine</h3>
      <p>Chaque magasin a sa propre page « cette semaine », mise à jour selon le cycle habituel du jeudi au mercredi.</p>
    </div>
    <div>
      <h3>Un aperçu de la semaine prochaine</h3>
      <p>Quand l'information est disponible en primeur, on l'affiche sur une page distincte pour planifier à l'avance.</p>
    </div>
    <div>
      <h3>Contenu écrit, pas seulement des images</h3>
      <p>On résume les rayons à surveiller et on donne des conseils concrets, pour que l'information reste utile même sans avoir la circulaire sous les yeux.</p>
    </div>
  </div>
</section>
"""
    return page(SITE_NOM, SITE_DESCRIPTION, SITE_URL + "/", corps)

# ────────────────────────────────────────────────────────────────────────────
# Page liste des magasins
# ────────────────────────────────────────────────────────────────────────────
def page_magasins():
    categories = sorted(set(m["type"] for m in MAGASINS))
    sections = []
    for c in categories:
        anchor = re.sub(r"[^a-z0-9]+", "-", c.lower())
        items = sorted([m for m in MAGASINS if m["type"] == c], key=lambda s: s["nom"])
        cartes = "\n".join(carte_magasin(m) for m in items)
        sections.append(f"""<section class="section-categorie" id="{anchor}">
  <h2>{esc(c)} <span class="compte">({len(items)})</span></h2>
  <div class="grille-cartes">{cartes}</div>
</section>""")
    corps = f"""
<nav class="fil-ariane"><a href="/">Accueil</a> › <span>Magasins</span></nav>
<section class="entete-liste">
  <h1>Tous les magasins ({len(MAGASINS)})</h1>
  <p>Liste complète des magasins suivis, regroupés par catégorie. Chaque magasin a une page « cette semaine » et une page « semaine prochaine ».</p>
</section>
{''.join(sections)}
"""
    return page(f"Tous les magasins — {SITE_NOM}",
                f"Liste complète des {len(MAGASINS)} magasins suivis par {SITE_NOM}, regroupés par catégorie.",
                SITE_URL + "/magasins/", corps)

# ────────────────────────────────────────────────────────────────────────────
# Pages statiques
# ────────────────────────────────────────────────────────────────────────────
def page_a_propos():
    corps = f"""
<nav class="fil-ariane"><a href="/">Accueil</a> › <span>À propos</span></nav>
<article class="page-texte">
  <h1>À propos de {esc(SITE_NOM)}</h1>
  <p>{esc(SITE_NOM)} est un site indépendant qui résume, chaque semaine, ce qu'on retrouve habituellement dans les circulaires d'une sélection de magasins canadiens : épiceries, pharmacies, quincailleries, magasins de meubles et plusieurs autres.</p>
  <p>Notre objectif est simple : vous donner un aperçu rapide, en texte, des rayons et catégories à surveiller avant même d'ouvrir la circulaire complète — pratique pour planifier vos achats ou comparer plusieurs magasins d'un coup d'œil.</p>
  <h2>Ce que nous ne sommes pas</h2>
  <p>Nous ne sommes affiliés à aucun des magasins mentionnés. Les prix, promotions et dates exactes doivent toujours être confirmés directement auprès du magasin ou dans sa circulaire officielle.</p>
  <h2>Mises à jour</h2>
  <p>Le site est régénéré régulièrement pour refléter le cycle habituel des circulaires (généralement du jeudi au mercredi suivant).</p>
</article>
"""
    return page(f"À propos — {SITE_NOM}", f"En savoir plus sur {SITE_NOM} et notre façon de résumer les circulaires canadiennes.",
                SITE_URL + "/a-propos/", corps)

def page_conditions():
    corps = f"""
<nav class="fil-ariane"><a href="/">Accueil</a> › <span>Conditions d'utilisation</span></nav>
<article class="page-texte">
  <h1>Conditions d'utilisation</h1>
  <p>En consultant {esc(SITE_NOM)}, vous acceptez que le contenu soit fourni à titre informatif seulement. Les prix et promotions mentionnés sont des résumés généraux et peuvent différer de l'offre réelle en succursale.</p>
  <h2>Marques et noms de commerce</h2>
  <p>Les noms de magasins mentionnés sur ce site appartiennent à leurs détenteurs respectifs. Leur mention sert uniquement à identifier les commerces concernés et ne constitue ni un partenariat, ni une affiliation, ni un endossement.</p>
  <h2>Exactitude de l'information</h2>
  <p>Nous faisons des efforts raisonnables pour que l'information soit à jour, sans garantir son exactitude complète. Vérifiez toujours les prix en succursale ou sur le site officiel du magasin avant un achat.</p>
  <h2>Modifications</h2>
  <p>Ces conditions peuvent être mises à jour en tout temps sans préavis.</p>
</article>
"""
    return page(f"Conditions d'utilisation — {SITE_NOM}", f"Conditions d'utilisation de {SITE_NOM}.",
                SITE_URL + "/conditions-utilisation/", corps)

def page_confidentialite():
    corps = f"""
<nav class="fil-ariane"><a href="/">Accueil</a> › <span>Confidentialité</span></nav>
<article class="page-texte">
  <h1>Politique de confidentialité</h1>
  <p>{esc(SITE_NOM)} est un site statique qui ne requiert pas de création de compte et ne collecte pas d'informations personnelles directement.</p>
  <h2>Journaux d'hébergement</h2>
  <p>L'hébergeur (GitHub Pages) peut collecter des données techniques standards (adresse IP, navigateur) à des fins de sécurité et de performance, indépendamment de ce site.</p>
  <h2>Cookies</h2>
  <p>Ce site n'utilise pas de cookies de suivi publicitaire par défaut. Si un outil de mesure d'audience est ajouté plus tard, cette page sera mise à jour en conséquence.</p>
  <h2>Contact</h2>
  <p>Pour toute question relative à la confidentialité, référez-vous aux informations de contact du dépôt GitHub de ce site.</p>
</article>
"""
    return page(f"Politique de confidentialité — {SITE_NOM}", f"Politique de confidentialité de {SITE_NOM}.",
                SITE_URL + "/confidentialite/", corps)

# ────────────────────────────────────────────────────────────────────────────
# CSS — design original « papier / catalogue », distinct de l'ancien site
# ────────────────────────────────────────────────────────────────────────────
CSS = """
:root {
  --papier: #FBF4E7;
  --papier-2: #F3E7D2;
  --encre: #23201B;
  --sourdine: #6E655A;
  --ligne: #E2D3B4;
  --accent: #B4562A;
  --accent-2: #1F6B5C;
  --marque: var(--accent);
  --rayon: 14px;
  --rayon-s: 8px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Space Grotesk', system-ui, sans-serif;
  color: var(--encre);
  background: var(--papier);
  background-image:
    radial-gradient(circle at 1px 1px, rgba(35,32,27,.06) 1px, transparent 0);
  background-size: 22px 22px;
  line-height: 1.6;
}
h1, h2, h3 { font-family: 'Fraunces', Georgia, serif; font-weight: 700; margin: 0 0 .5em; }
a { color: var(--accent); }
p { margin: 0 0 1em; color: var(--encre); }
.entete {
  position: sticky; top: 0; z-index: 20;
  background: var(--papier); border-bottom: 3px solid var(--encre);
}
.entete-int {
  max-width: 1120px; margin: 0 auto; padding: 14px 20px;
  display: flex; align-items: center; justify-content: space-between; gap: 20px;
}
.logo { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--encre); }
.logo-icone { font-size: 1.4rem; }
.logo-texte { font-family: 'Fraunces', serif; font-weight: 700; font-size: 1.15rem; }
.nav { display: flex; gap: 18px; flex-wrap: wrap; }
.nav a { text-decoration: none; color: var(--encre); font-weight: 500; border-bottom: 2px solid transparent; padding-bottom: 2px; }
.nav a:hover { border-color: var(--accent); }
main { max-width: 1120px; margin: 0 auto; padding: 32px 20px 60px; }
.fil-ariane { font-size: .85rem; color: var(--sourdine); margin-bottom: 18px; }
.fil-ariane a { color: var(--sourdine); text-decoration: none; }
.fil-ariane a:hover { color: var(--accent); }

/* Accueil */
.heros { text-align: center; padding: 40px 0 16px; }
.heros h1 { font-size: clamp(2rem, 5vw, 3rem); }
.heros-slogan { max-width: 640px; margin: 0 auto 22px; color: var(--sourdine); font-size: 1.05rem; }
.bouton-principal, .bouton-secondaire {
  display: inline-block; text-decoration: none; font-weight: 700;
  padding: 12px 22px; border-radius: 999px; border: 2px solid var(--encre);
}
.bouton-principal { background: var(--encre); color: var(--papier); }
.bouton-principal:hover { background: var(--accent); border-color: var(--accent); }
.bouton-secondaire { background: transparent; color: var(--encre); margin-top: 12px; }
.bouton-secondaire:hover { background: var(--encre); color: var(--papier); }

.bloc-categories { margin: 36px 0; }
.puces-categories { display: flex; flex-wrap: wrap; gap: 10px; }
.puce-categorie {
  text-decoration: none; color: var(--encre); background: var(--papier-2);
  border: 1px solid var(--ligne); border-radius: 999px; padding: 8px 16px; font-size: .9rem;
}
.puce-categorie span { color: var(--sourdine); }
.puce-categorie:hover { border-color: var(--accent); }

.bloc-vedette { margin: 40px 0; }
.voir-tout { text-align: center; margin-top: 18px; }
.voir-tout a { text-decoration: none; font-weight: 700; }

.grille-cartes { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px,1fr)); gap: 14px; }

.carte-magasin {
  display: flex; gap: 12px; align-items: center; text-decoration: none; color: var(--encre);
  background: #fff; border: 1px solid var(--ligne); border-radius: var(--rayon-s);
  padding: 12px; transition: transform .15s ease, box-shadow .15s ease;
}
.carte-magasin:hover { transform: translateY(-2px); box-shadow: 0 6px 0 var(--marque); }
.carte-mockup {
  flex: 0 0 46px; width: 46px; height: 46px; border-radius: 8px;
  background: var(--marque); display: flex; align-items: center; justify-content: center;
}
.carte-mockup-initiale { color: #fff; font-family: 'Fraunces', serif; font-weight: 700; font-size: 1.2rem; }
.carte-corps { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.carte-nom { font-weight: 700; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.carte-type { font-size: .78rem; color: var(--sourdine); }
.carte-sous { font-size: .78rem; color: var(--marque); font-weight: 600; }

.bloc-explication { margin: 48px 0; }
.explication-grille { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 20px; }
.explication-grille > div { background: #fff; border: 1px solid var(--ligne); border-radius: var(--rayon); padding: 18px; }
.explication-grille h3 { font-size: 1.05rem; }

/* Liste magasins */
.entete-liste { margin-bottom: 30px; }
.section-categorie { margin: 34px 0; }
.section-categorie h2 { font-size: 1.3rem; }
.compte { color: var(--sourdine); font-weight: 400; font-size: 1rem; }

/* Page magasin */
.page-magasin { }
.entete-magasin {
  display: grid; grid-template-columns: 1.3fr 1fr; gap: 30px; align-items: center;
  background: #fff; border: 1px solid var(--ligne); border-radius: var(--rayon);
  padding: 26px; margin-bottom: 28px;
}
.etiquette { text-transform: uppercase; letter-spacing: .08em; font-size: .75rem; color: var(--marque); font-weight: 700; margin: 0 0 6px; }
.entete-magasin h1 { font-size: clamp(1.6rem, 4vw, 2.3rem); margin-bottom: 4px; }
.souligne { text-decoration: underline; text-decoration-color: var(--marque); text-decoration-thickness: 4px; text-underline-offset: 4px; }
.periode { color: var(--sourdine); font-weight: 600; margin-bottom: 12px; }
.intro { max-width: 46ch; }

.mockup-livret { position: relative; height: 220px; }
.mockup-couverture {
  position: absolute; inset: 0; background: var(--marque); border-radius: 10px;
  display: flex; flex-direction: column; align-items: flex-start; justify-content: flex-end;
  padding: 18px; color: #fff; box-shadow: 0 10px 0 rgba(0,0,0,.08);
  background-image: repeating-linear-gradient(135deg, rgba(255,255,255,.06) 0 2px, transparent 2px 14px);
}
.mockup-badge {
  align-self: flex-start; background: rgba(255,255,255,.22); border-radius: 999px;
  padding: 4px 10px; font-size: .7rem; font-weight: 700; margin-bottom: auto;
}
.mockup-initiale { font-family: 'Fraunces', serif; font-size: 2.6rem; font-weight: 700; line-height: 1; opacity: .35; position: absolute; top: 14px; right: 18px; }
.mockup-nom { font-family: 'Fraunces', serif; font-weight: 700; font-size: 1.3rem; }
.mockup-periode { font-size: .85rem; opacity: .9; }
.mockup-page { position: absolute; top: 10px; bottom: -10px; width: 100%; background: #fff; border: 1px solid var(--ligne); border-radius: 10px; z-index: -1; }
.mockup-page-2 { transform: rotate(3deg) translateX(6px); }
.mockup-page-3 { transform: rotate(-2deg) translateX(-4px); z-index: -2; }

.bloc-aubaines, .bloc-rayons, .bloc-conseil, .bloc-faq, .bloc-autres {
  background: #fff; border: 1px solid var(--ligne); border-radius: var(--rayon); padding: 22px; margin-bottom: 22px;
}
.liste-aubaines { margin: 0; padding-left: 1.2em; }
.liste-aubaines li { margin-bottom: 6px; }

.liste-rayons { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.liste-rayons li { border-left: 3px solid var(--marque); padding-left: 12px; }
.liste-rayons li strong { display: block; }
.liste-rayons li span { color: var(--sourdine); font-size: .92rem; }

.faq-item { border-bottom: 1px solid var(--ligne); padding: 10px 0; }
.faq-item summary { cursor: pointer; font-weight: 700; }
.faq-item p { margin-top: 8px; color: var(--sourdine); }

.bloc-autres h2 { font-size: 1.15rem; }

/* Pages texte */
.page-texte { max-width: 70ch; }
.page-texte h1 { font-size: 2rem; }
.page-texte h2 { font-size: 1.2rem; margin-top: 1.6em; }

.pied { border-top: 3px solid var(--encre); margin-top: 60px; background: var(--papier-2); }
.pied-int { max-width: 1120px; margin: 0 auto; padding: 26px 20px; }
.pied-nav { display: flex; flex-wrap: wrap; gap: 14px; margin: 10px 0; }
.pied-nav a { color: var(--encre); text-decoration: none; font-size: .9rem; }
.pied-nav a:hover { text-decoration: underline; }
.pied-legal { font-size: .78rem; color: var(--sourdine); max-width: 70ch; }

@media (max-width: 720px) {
  .entete-magasin { grid-template-columns: 1fr; }
  .mockup-livret { height: 180px; order: -1; }
}
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#B4562A"/><text x="32" y="42" font-family="Georgia, serif" font-size="30" font-weight="700" fill="#FBF4E7" text-anchor="middle">C</text></svg>"""

# ────────────────────────────────────────────────────────────────────────────
# Écriture des fichiers
# ────────────────────────────────────────────────────────────────────────────
def write(path: Path, contenu_str: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contenu_str, encoding="utf-8")

def build():
    urls = []  # pour le sitemap: (path, priority, changefreq)

    write(ROOT / "index.html", page_accueil())
    urls.append(("/", "1.0", "weekly"))

    write(ROOT / "magasins" / "index.html", page_magasins())
    urls.append(("/magasins/", "0.8", "weekly"))

    write(ROOT / "a-propos" / "index.html", page_a_propos())
    urls.append(("/a-propos/", "0.3", "monthly"))

    write(ROOT / "conditions-utilisation" / "index.html", page_conditions())
    urls.append(("/conditions-utilisation/", "0.2", "yearly"))

    write(ROOT / "confidentialite" / "index.html", page_confidentialite())
    urls.append(("/confidentialite/", "0.2", "yearly"))

    for m in MAGASINS:
        html_courant, path_courant = page_magasin(m, semaine_prochaine=False)
        write(ROOT / path_courant.strip("/") / "index.html", html_courant)
        urls.append((path_courant, "0.9", "weekly"))

        html_prochain, path_prochain = page_magasin(m, semaine_prochaine=True)
        write(ROOT / path_prochain.strip("/") / "index.html", html_prochain)
        urls.append((path_prochain, "0.6", "weekly"))

    write(ROOT / "assets" / "style.css", CSS)
    write(ROOT / "assets" / "favicon.svg", FAVICON_SVG)

    # sitemap.xml
    entries = "\n".join(
        f"""  <url>
    <loc>{SITE_URL}{p}</loc>
    <changefreq>{cf}</changefreq>
    <priority>{pr}</priority>
  </url>""" for p, pr, cf in urls
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>"""
    write(ROOT / "sitemap.xml", sitemap)

    robots = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""
    write(ROOT / "robots.txt", robots)

    write(ROOT / ".nojekyll", "")

    print(f"OK — {len(urls)} URLs générées ({len(MAGASINS)} magasins x 2 pages + pages fixes).")
    print(f"Semaine courante : {PERIODE_COURANTE}")
    print(f"Semaine prochaine : {PERIODE_PROCHAINE}")

if __name__ == "__main__":
    build()
