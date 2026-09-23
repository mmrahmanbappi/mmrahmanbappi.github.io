"""Builds the home page (index.html) and 404.html for mmrahmanbappi.github.io.
Edit PROJECTS below to add a project, then run: python3 _build/build.py"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "https://mmrahmanbappi.github.io"
GH = "https://github.com/mmrahmanbappi"
e = lambda s: html.escape(str(s), quote=True)

# slug, name, category, count (None if not a set), count label, one line, card image
PROJECTS = [
    ("100-free-admin-dashboards", "100 Free Admin Dashboards", "Templates", 100, "dashboards, 3,400+ pages",
     "Complete admin dashboards with more than 30 pages each, light and dark themes.", "work-dashboard"),
    ("100-free-ai-ui-components", "100 Free AI UI Components", "Components", 90, "components so far",
     "Prompt boxes, thinking states, token meters and more for AI apps. One file each.", "work-ai-ui"),
    ("tantu-c-framework", "Tantu C Framework", "Tools", None, "",
     "A free website builder and web framework written in C. Markdown in, fast website out.", "tantu-c-framework"),
    ("100-free-html-templates", "100 Free HTML Templates", "Templates", 100, "templates",
     "One-file website templates you can edit and upload in minutes.", "work-template"),
    ("100-css-designs", "100 Free CSS Designs", "Components", 100, "designs",
     "Popular UI styles built in plain CSS, each with a live demo.", "work-css"),
    ("70-free-data-charts", "70 Free Data Charts", "Components", 70, "charts",
     "Charts in plain HTML, CSS and JavaScript, with no chart library.", "work-chart"),
    ("100-free-404-pages", "100 Free 404 Pages", "Templates", 100, "pages",
     "Friendly error pages that keep visitors on your site, one file each.", "work-404"),
    ("100-vanilla-javascript-projects", "100 Vanilla JavaScript Projects", "Learning", 100, "projects",
     "Small projects in plain JavaScript with live demos and source code.", "100-vanilla-javascript-projects"),
    ("chrome-extensions", "Free SEO Chrome Extensions", "Tools", 7, "extensions",
     "Chrome extensions for technical SEO checks on any website.", "chrome-extensions"),
]
TOTAL = sum(p[3] or 0 for p in PROJECTS)
CATS = ["Templates", "Components", "Tools", "Learning"]
MOVED = {"tantu": "tantu-c-framework", "seo-tools": "chrome-extensions", "seo-chrome-extensions": "chrome-extensions",
         "vanilla-javascript-projects": "100-vanilla-javascript-projects", "free-html-templates": "100-free-html-templates",
         "100-free-data-charts": "70-free-data-charts"}

TITLE = "MM Rahman Bappi: Free Web Templates, Tools and a C Framework"
DESC = (f"Free, open-source web projects by MM Rahman Bappi: {TOTAL}+ templates, AI UI components, admin dashboards, "
        "charts and tools, plus a C framework.")

CSS = """
:root{--bg:#eeeeea;--surface:#f6f6f2;--card:#fff;--ink:#171518;--text:#403b42;--muted:#5f5d61;--line:#d9d8d2;--acc:#b23a0a;--acc-ink:#fff;--acc-soft:#f6e3d9;
 --r:18px;--shadow:0 1px 2px rgba(23,21,24,.06),0 18px 40px -22px rgba(23,21,24,.28);color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#141316;--surface:#1b1a1e;--card:#222126;--ink:#f2f1ed;--text:#d7d5d9;--muted:#a3a1a6;--line:#302f35;--acc:#ff7b4f;--acc-ink:#141316;--acc-soft:#3a2219;
 --shadow:0 1px 2px rgba(0,0,0,.4),0 18px 40px -22px rgba(0,0,0,.7);color-scheme:dark}}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1.02rem/1.6 "Inter",system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,"Helvetica Neue",sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}img{max-width:100%;display:block}
:focus-visible{outline:3px solid var(--acc);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:var(--ink);color:var(--bg);padding:.5rem 1rem;z-index:9;border-radius:8px}
.wrap{max-width:78rem;margin:0 auto;padding:0 1.5rem}
h1,h2,h3{color:var(--ink);letter-spacing:-.035em;line-height:1.04;font-weight:600;margin:0}
.btn{display:inline-flex;align-items:center;gap:.75rem;border-radius:999px;font-weight:600;text-decoration:none;font-size:.98rem;padding:.72rem 1.2rem;border:1.5px solid var(--ink);color:var(--ink);background:none;cursor:pointer}
.btn.dark{background:var(--ink);color:var(--bg);padding:.45rem .45rem .45rem 1.25rem}
.btn.dark .arr{width:2.2rem;height:2.2rem;border-radius:50%;background:var(--acc);color:var(--acc-ink);display:grid;place-items:center;transition:transform .2s}
.btn.dark:hover .arr{transform:translateX(3px)}
.btn:hover{opacity:.92}
header.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:saturate(1.4) blur(10px)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;height:4.6rem}
.logo{display:flex;align-items:center;gap:.6rem;text-decoration:none;font-weight:700;color:var(--ink);letter-spacing:-.01em}
.logo i{width:2.1rem;height:2.1rem;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;font-style:normal;font-size:.78rem;font-weight:800;letter-spacing:.02em}
nav.main{display:flex;gap:1.8rem;font-size:.95rem}nav.main a{text-decoration:none;color:var(--text)}nav.main a:hover{color:var(--ink)}
.hero{padding:2.5rem 0 3rem}
.hero .grid{display:grid;grid-template-columns:1.05fr 1.2fr .95fr;gap:1.5rem;align-items:center;min-height:32rem}
.badge{display:inline-flex;align-items:center;gap:.5rem;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:.25rem .7rem .25rem .3rem}
.badge b{background:var(--acc);color:var(--acc-ink);border-radius:999px;padding:.1rem .5rem}
.hero h1{font-size:clamp(2.5rem,4.6vw,4rem);font-weight:560;margin:1.1rem 0 1.1rem}
.hero .by{font-size:.95rem;color:var(--muted);margin:0 0 .2rem}
.hero .lead{font-size:1.12rem;max-width:26rem;margin:0 0 1.8rem;color:var(--text)}
.acts{display:flex;gap:.8rem;flex-wrap:wrap;align-items:center}
.proof{display:flex;align-items:center;gap:.8rem;margin-top:2.6rem;font-size:.9rem;color:var(--muted)}
.proof .dots{display:flex}.proof .dots span{width:2rem;height:2rem;border-radius:50%;border:2px solid var(--bg);margin-left:-.5rem;background-size:cover;background-position:center}
.proof .dots span:first-child{margin-left:0}.proof b{color:var(--ink);display:block;font-size:.95rem}
.stack{position:relative;height:30rem;-webkit-mask-image:linear-gradient(#000 70%,transparent);mask-image:linear-gradient(#000 70%,transparent)}
.stack figure{position:absolute;margin:0;width:62%;aspect-ratio:16/10;border-radius:14px;overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--line);background:var(--card);animation:float 7s ease-in-out infinite}
.stack figure img{width:100%;height:100%;object-fit:cover}
.stack figure:nth-child(1){left:2%;top:4%;transform:rotate(-7deg);animation-delay:-1s}
.stack figure:nth-child(2){right:0;top:0;transform:rotate(5deg);animation-delay:-3s}
.stack figure:nth-child(3){left:18%;top:26%;transform:rotate(-1deg);z-index:3;width:70%;animation-delay:-2s}
.stack figure:nth-child(4){left:0;top:52%;transform:rotate(4deg);animation-delay:-4s}
.stack figure:nth-child(5){right:2%;top:48%;transform:rotate(-5deg);animation-delay:-5s}
.stack figure:nth-child(6){left:24%;top:70%;transform:rotate(2deg);animation-delay:-6s}
@keyframes float{50%{translate:0 -8px}}
.side{display:flex;flex-direction:column;gap:1.1rem}
.cycle{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:1rem 1.1rem}
.cycle .hd{display:flex;align-items:center;gap:.7rem}
.cycle .hd i{width:2.3rem;height:2.3rem;border-radius:10px;background:var(--ink);color:var(--bg);display:grid;place-items:center;font-style:normal;font-weight:800;font-size:.75rem;flex:none}
.cycle small{display:block;color:var(--muted);font-size:.78rem}.cycle strong{color:var(--ink);font-size:.95rem;display:block;min-height:1.5em;transition:opacity .35s}
.cycle ul{list-style:none;margin:.8rem 0 0;padding:0 0 0 3rem;font-size:.9rem;display:flex;flex-direction:column;gap:.45rem}
.cycle li{transition:opacity .35s,transform .35s}
.cycle li:nth-child(1){opacity:.9}.cycle li:nth-child(2){opacity:.65}.cycle li:nth-child(3){opacity:.4}.cycle li:nth-child(4){opacity:.18}
.stat{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:1rem 1.1rem;display:flex;justify-content:space-between;align-items:flex-start;gap:1rem}
.stat small{color:var(--muted);font-size:.85rem}.stat b{display:block;font-size:2rem;color:var(--ink);letter-spacing:-.03em;line-height:1;text-align:right}
.stat em{font-style:normal;font-size:.78rem;color:var(--acc);font-weight:600;display:block;text-align:right;margin-top:.35rem}
.big{font-size:clamp(2rem,3.4vw,2.9rem);line-height:1.02;color:var(--ink);font-weight:560;letter-spacing:-.035em;margin:0}
.facts{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.facts ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr)}
.facts li{padding:1.4rem 1rem;text-align:center;border-left:1px solid var(--line)}.facts li:first-child{border-left:0}
.facts b{display:block;font-size:1.6rem;color:var(--ink);letter-spacing:-.02em}.facts span{font-size:.9rem;color:var(--muted)}
section.band{padding:5rem 0}
.sh{display:flex;justify-content:space-between;align-items:flex-end;gap:1.5rem;flex-wrap:wrap;margin-bottom:2rem}
.sh h2{font-size:clamp(2rem,4vw,3rem)}.sh p{margin:.6rem 0 0;max-width:34rem}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--acc);margin:0 0 .6rem}
.chips{display:flex;gap:.5rem;flex-wrap:wrap}
.chips button{font:inherit;font-size:.9rem;border:1.5px solid var(--line);background:var(--surface);color:var(--text);border-radius:999px;padding:.4rem 1rem;cursor:pointer}
.chips button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:var(--bg)}
.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:1.3rem}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column;transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-3px);box-shadow:var(--shadow)}
.card .im{aspect-ratio:16/10;overflow:hidden;border-bottom:1px solid var(--line);background:var(--surface)}
.card .im img{width:100%;height:100%;object-fit:cover;transition:transform .4s}.card:hover .im img{transform:scale(1.03)}
.card .in{padding:1.1rem 1.2rem 1.25rem;display:flex;flex-direction:column;gap:.45rem;flex:1}
.card .meta{display:flex;justify-content:space-between;gap:.5rem;font-size:.8rem;color:var(--muted)}
.card .meta span:first-child{color:var(--acc);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.card h3{font-size:1.2rem;letter-spacing:-.02em}.card h3 a{text-decoration:none}.card h3 a:hover{color:var(--acc)}
.card p{margin:0;font-size:.95rem;flex:1}
.card .links{display:flex;gap:1.1rem;margin-top:.5rem;font-size:.92rem;font-weight:600}
.card .links a{text-decoration:none;color:var(--ink);border-bottom:1.5px solid var(--acc)}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:1.3rem;counter-reset:s}
.steps li{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:1.5rem;counter-increment:s}
.steps li::before{content:"0" counter(s);display:block;font-size:.85rem;font-weight:700;color:var(--acc);margin-bottom:1.2rem}
.steps h3{font-size:1.3rem;margin-bottom:.5rem}.steps p{margin:0}
.about{display:grid;grid-template-columns:1fr 1.2fr;gap:3rem;align-items:start}.faqs details:first-child{border-top:0;padding-top:0}
.about p{font-size:1.1rem;margin:0 0 1rem}
details{border-top:1px solid var(--line);padding:1.1rem 0}details:last-child{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:650;color:var(--ink);list-style:none;display:flex;justify-content:space-between;gap:1rem}
summary::-webkit-details-marker{display:none}summary::after{content:"+";font-size:1.4rem;line-height:1;color:var(--acc)}details[open] summary::after{content:"-"}
details p{margin:.7rem 0 0}
footer{border-top:1px solid var(--line);padding:2rem 0;font-size:.92rem;color:var(--muted)}
footer .wrap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}
footer a{color:var(--ink)}
@media (max-width:1060px){.hero .grid{grid-template-columns:1fr 1fr}.hero .side{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;align-items:start}.hero .big{grid-column:1/-1}.cards{grid-template-columns:repeat(2,1fr)}}
@media (max-width:760px){nav.main{display:none}.hero .grid{grid-template-columns:1fr;min-height:0}.stack{height:19rem;order:2}.hero .side{grid-template-columns:1fr;order:3}
 .facts ul{grid-template-columns:repeat(2,1fr)}.facts li:nth-child(3){border-left:0}.facts li:nth-child(n+3){border-top:1px solid var(--line)}
 .cards,.steps,.about{grid-template-columns:1fr}section.band{padding:3.5rem 0}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}html{scroll-behavior:auto}}
"""


def head(title, desc, canonical, robots="index, follow, max-image-preview:large", schema=None):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="author" content="MM Rahman Bappi">
<meta name="theme-color" content="#eeeeea" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141316" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website"><meta property="og:site_name" content="MM Rahman Bappi">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{B}/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Free web projects by MM Rahman Bappi">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{B}/img/og.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='32' fill='%23171518'/%3E%3Ctext x='32' y='41' font-family='Arial' font-weight='800' font-size='24' fill='%23eeeeea' text-anchor='middle'%3EMM%3C/text%3E%3C/svg%3E">
{('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>') if schema else ''}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>{CSS.strip()}</style>
</head>
"""


def header():
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap"><a class="logo" href="{B}/"><i aria-hidden="true">MM</i>MM Rahman Bappi</a>
<nav class="main" aria-label="Main"><a href="{B}/#projects">Projects</a><a href="{B}/#how">How to use</a><a href="{B}/#about">About</a><a href="{B}/#faq">FAQ</a></nav>
<a class="btn" href="{GH}" style="padding:.5rem 1.1rem">GitHub</a></div></header>"""


def footer():
    return f"""<footer><div class="wrap"><p style="margin:0">Made by MM Rahman Bappi. Free and open source.</p><p style="margin:0"><a href="{GH}">GitHub</a> &nbsp; <a href="https://mmseo.app/">mmseo.app</a></p></div></footer>"""


ARROW = '<span class="arr" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'

FAQ = [
    ("Are these projects really free?", "Yes. You can use them in personal and business projects without paying. Every project uses the MIT license."),
    ("Do I need to sign up or install anything?", "No. Most projects are plain HTML, CSS and JavaScript. Open the file in a browser, or copy it into your site."),
    ("Can I use them for client work?", "Yes. Every project uses the MIT license, so client work is fine. Please keep the license file in your copy."),
    ("Can I ask for a new template or report a problem?", "Yes. Open an issue in the GitHub repository of the project, and describe what you need or what went wrong."),
]


def build():
    work = ["work-dashboard", "work-template", "work-ai-ui", "work-chart", "work-css", "work-404"]
    cycle = [p[1] for p in PROJECTS]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": B + "/#website", "url": B + "/", "name": "MM Rahman Bappi", "inLanguage": "en", "publisher": {"@id": B + "/#person"}},
        {"@type": "Person", "@id": B + "/#person", "name": "MM Rahman Bappi", "url": B + "/", "sameAs": [GH, "https://mmseo.app/"]},
        {"@type": "CollectionPage", "@id": B + "/#webpage", "url": B + "/", "name": TITLE, "description": DESC, "isPartOf": {"@id": B + "/#website"},
         "about": {"@id": B + "/#person"}, "primaryImageOfPage": B + "/img/og.jpg",
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(PROJECTS), "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "url": f"{B}/{p[0]}/", "name": p[1]} for i, p in enumerate(PROJECTS)]}},
        {"@type": "FAQPage", "@id": B + "/#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
    cards = "".join(f"""<li class="card" data-cat="{p[2]}"><a class="im" href="{B}/{p[0]}/" tabindex="-1" aria-hidden="true"><img src="img/{p[6]}.webp" alt="" width="800" height="500" loading="lazy"></a>
<div class="in"><div class="meta"><span>{e(p[2])}</span><span>{(str(p[3]) + ' ' + e(p[4])) if p[3] else 'Open source'}</span></div>
<h3><a href="{B}/{p[0]}/">{e(p[1])}</a></h3><p>{e(p[5])}</p>
<div class="links"><a href="{B}/{p[0]}/">Website</a><a href="{GH}/{p[0]}">Source code</a></div></div></li>""" for p in PROJECTS)
    chips = '<button type="button" aria-pressed="true" data-f="all">All</button>' + "".join(f'<button type="button" aria-pressed="false" data-f="{c}">{c}</button>' for c in CATS)
    body = f"""<body>
{header()}
<main id="main">
<section class="hero"><div class="wrap grid">
  <div>
    <span class="badge"><b>Free</b>Open source web projects</span>
    <h1>Web projects you can use today</h1>
    <p class="lead">Templates, AI components, dashboards and tools, built by MM Rahman Bappi and shared for free. Download a file and it just works.</p>
    <div class="acts"><a class="btn dark" href="#projects">Browse projects{ARROW}</a></div>
    <div class="proof"><span><b>{len(PROJECTS)} projects, {TOTAL}+ free files</b>Free for personal and business use</span></div>
  </div>
  <div class="stack" aria-hidden="true">{"".join(f'<figure><img src="img/{w}.webp" alt="" width="800" height="500"></figure>' for w in work)}</div>
  <div class="side">
    <div class="cycle" aria-live="polite"><div class="hd"><i aria-hidden="true">MM</i><div><small>I build and share</small><strong id="cur">{e(cycle[0])}</strong></div></div>
      <ul id="next" aria-hidden="true">{"".join(f"<li>{e(c)}</li>" for c in cycle[1:5])}</ul></div>
    <div class="stat"><small>Free templates, components<br>and tools</small><div><b>{TOTAL}+</b><em>New: AI UI components</em></div></div>
    <p class="big">Free. Open source. Ready to use.</p>
  </div>
</div></section>
<div class="facts"><div class="wrap"><ul>
  <li><b>{len(PROJECTS)}</b><span>open source projects</span></li>
  <li><b>3,400+</b><span>dashboard pages</span></li>
  <li><b>MIT</b><span>license on every project</span></li>
  <li><b>0</b><span>sign ups needed</span></li>
</ul></div></div>
<section class="band" id="projects"><div class="wrap">
  <div class="sh"><div><p class="eyebrow">Projects</p><h2>Everything I have built</h2><p>Each project has a live website where you can try things, and the full source on GitHub.</p></div>
    <div class="chips" role="group" aria-label="Filter projects">{chips}</div></div>
  <ul class="cards" id="cards">{cards}</ul>
</div></section>
<section class="band" id="how" style="background:var(--surface);border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap">
  <div class="sh"><div><p class="eyebrow">How to use</p><h2>Three steps, no setup</h2></div></div>
  <ol class="steps"><li><h3>Pick</h3><p>Open a project website and try the live demos until you find what you need.</p></li>
    <li><h3>Copy</h3><p>Download the file or copy the code. Most things are a single HTML file with no library.</p></li>
    <li><h3>Ship</h3><p>Change the text and colors, then upload it to any host, including free GitHub Pages.</p></li></ol>
</div></section>
<section class="band" id="about"><div class="wrap about">
  <div><p class="eyebrow">About</p><h2 style="font-size:clamp(2rem,4vw,3rem)">Hi, I am MM Rahman Bappi</h2></div>
  <div><p>I build templates, components and tools for the web, and share every one of them as open source. I care about pages that load fast, read clearly and work on every screen.</p>
    <p>Most projects work without a build step, so you can open a file and start. If something is missing or broken, tell me on GitHub.</p>
    <div class="acts"><a class="btn dark" href="{GH}">Follow on GitHub{ARROW}</a><a class="btn" href="https://mmseo.app/">Visit mmseo.app</a></div></div>
</div></section>
<section class="band" id="faq" style="padding-top:0"><div class="wrap about">
  <div><p class="eyebrow">FAQ</p><h2 style="font-size:clamp(2rem,4vw,3rem)">Questions people ask</h2></div>
  <div class="faqs">{"".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)}</div>
</div></section>
</main>
{footer()}
<script>
(function(){{var items={json.dumps(cycle)},cur=document.getElementById('cur'),next=document.getElementById('next'),i=0;
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)setInterval(function(){{i=(i+1)%items.length;cur.style.opacity=0;
setTimeout(function(){{cur.textContent=items[i];cur.style.opacity=1;next.innerHTML='';for(var k=1;k<5;k++){{var li=document.createElement('li');li.textContent=items[(i+k)%items.length];next.appendChild(li);}}}},350);}},2600);
var bs=[].slice.call(document.querySelectorAll('.chips button')),cs=[].slice.call(document.querySelectorAll('#cards .card'));
bs.forEach(function(b){{b.addEventListener('click',function(){{bs.forEach(function(x){{x.setAttribute('aria-pressed',x===b);}});var f=b.dataset.f;cs.forEach(function(c){{c.hidden=f!=='all'&&c.dataset.cat!==f;}});}});}});}})();
</script>
</body>
</html>
"""
    open(os.path.join(ROOT, "index.html"), "w").write(head(TITLE, DESC, B + "/", schema=schema) + body)

    # 404: sends old links to the new address, otherwise lists the projects
    links = "".join(f'<li class="card" style="flex-direction:row;align-items:center;padding:.9rem 1.1rem;gap:1rem"><div class="in" style="padding:0"><h3 style="font-size:1.05rem"><a href="{B}/{p[0]}/">{e(p[1])}</a></h3><p style="font-size:.9rem">{e(p[5])}</p></div></li>' for p in PROJECTS)
    page404 = head("Page not found | MM Rahman Bappi", "This page does not exist or has moved.", B + "/404.html", robots="noindex, follow") + f"""<body>
<script>(function(){{var moved={json.dumps(MOVED)};var p=location.pathname.split("/");if(p.length>1&&moved[p[1]]){{p[1]=moved[p[1]];location.replace(p.join("/")+location.search+location.hash);}}}})();</script>
{header()}
<main id="main"><section class="band"><div class="wrap" style="max-width:52rem"><p class="eyebrow">Error 404</p><h1 style="font-size:clamp(2.4rem,6vw,4rem);margin-bottom:1rem">Page not found</h1>
<p style="font-size:1.1rem;margin:0 0 2rem">This page does not exist or has moved. Here are all the projects:</p>
<ul class="cards" style="grid-template-columns:1fr;gap:.7rem">{links}</ul></div></section></main>
{footer()}
</body></html>
"""
    open(os.path.join(ROOT, "404.html"), "w").write(page404)
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n\n" + "\n".join(f"Sitemap: {B}/{p[0]}/sitemap.xml" for p in PROJECTS) + f"\nSitemap: {B}/sitemap.xml\n")
    print("built: index.html, 404.html, robots.txt |", len(PROJECTS), "projects,", TOTAL, "free files | title", len(TITLE), "| desc", len(DESC))


if __name__ == "__main__":
    build()
