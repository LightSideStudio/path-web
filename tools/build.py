#!/usr/bin/env python3
"""Genera la web de Path en español e inglés: portada, privacidad y soporte.

    python3 tools/build.py

Las dos versiones salen de la misma plantilla, así que dicen siempre lo
mismo; el texto de cada idioma está en COPY. Escribe:
  index.html, privacidad.html, soporte.html          (español, raíz)
  en/index.html, en/privacy.html, en/support.html    (inglés)
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://lightsidestudio.github.io/path-web/"
EMAIL = "path@lightsidestudio.com"
# Cuando la app esté publicada, su enlace aquí: el botón se activa solo.
APPSTORE_URL = ""
UPDATED = {"es": "11 de octubre de 2026", "en": "October 11, 2026"}

COPY = {
    "es": {
        "lang": "es", "locale": "es_ES", "dir": "", "other": "en/", "other_label": "English",
        "pages": {"index": "index.html", "privacy": "privacidad.html", "support": "soporte.html"},
        "title": "Path: Rutas GPS en tu reloj · The way is yours",
        "description": "Graba y navega cualquier ruta con el Apple Watch. Mapa topográfico, aviso si te sales y análisis de cada salida. Gratis y sin anuncios.",
        "nav": ["Qué hace", "Capturas", "Soporte"],
        "download": "Descargar",
        "appstore": "Descargar en el App Store",
        "soon": "Muy pronto en el App Store",
        "kicker": "The way is yours",
        "h1": "Tu montaña, <em>en la muñeca</em>.",
        "sub": "Graba y navega cualquier ruta con el Apple Watch. El iPhone, solo para prepararla.",
        "note": "Gratis · Sin anuncios · Sin suscripciones",
        "features_label": "Qué hace",
        "features_title": "Todo lo de la montaña, sin complicaciones.",
        "features": [
            ("Navega", "Mapa topográfico, el rastro de lo que llevas y un aviso en cuanto te sales."),
            ("Graba", "Distancia, desnivel, ritmo y pulso en directo. Senderismo, trail o bici."),
            ("Conectadas", "Envía rutas GPX al reloj en un toque y recibe cada actividad al terminar."),
            ("Analiza", "Perfil, parciales, zonas cardíacas y mejores marcas de cada salida."),
        ],
        "demo": {"left": "destino", "km": "km", "time": "tiempo", "gain": "desnivel +",
                 "phone": "iPhone", "watch": "Apple Watch", "route": "Ruta GPX", "activity": "Actividad",
                 "splits": "Parciales", "off": "Fuera de ruta"},
        "standalone_title": "El reloj funciona solo.",
        "standalone": "Graba, navega y guarda en Salud aunque te dejes el iPhone en casa. Con la muñeca bajada, el punto sigue avanzando.",
        "shots_label": "Capturas",
        "shots_title": "Así se ve.",
        "shots": ["01-hero", "02-navegar", "03-conectadas", "04-mapas", "05-analisis", "06-deportes", "07-independiente", "08-zonas"],
        "free_title": "Gratis. Sin letra pequeña.",
        "free": ["Sin anuncios", "Sin suscripciones", "Sin cuenta ni registro", "Tus datos se quedan en tus dispositivos"],
        "close_title": "Sal a la <em>montaña</em>.",
        "close": "Carga una ruta, levanta la muñeca y a caminar.",
        "footer_support": "Soporte", "footer_privacy": "Privacidad",
        "footer_note": "Path es una app de LightSide Studio. Apple Watch e iPhone son marcas de Apple Inc.",
        "back": "Path",
    },
    "en": {
        "lang": "en", "locale": "en_US", "dir": "en/", "other": "../", "other_label": "Español",
        "pages": {"index": "index.html", "privacy": "privacy.html", "support": "support.html"},
        "title": "Path: GPS Routes on Your Watch · The way is yours",
        "description": "Record and navigate any route with your Apple Watch. Topo map, off-route alerts and an analysis of every outing. Free, no ads.",
        "nav": ["Features", "Screenshots", "Support"],
        "download": "Download",
        "appstore": "Download on the App Store",
        "soon": "Coming soon to the App Store",
        "kicker": "The way is yours",
        "h1": "Your mountain, <em>on your wrist</em>.",
        "sub": "Record and navigate any route with your Apple Watch. Your iPhone is just for planning.",
        "note": "Free · No ads · No subscriptions",
        "features_label": "Features",
        "features_title": "Everything for the mountains, without the hassle.",
        "features": [
            ("Navigate", "Topo map, the trail of where you've been and an alert the moment you stray."),
            ("Record", "Distance, elevation, pace and heart rate live. Hiking, trail or bike."),
            ("Connected", "Send GPX routes to your watch in one tap and get every activity back when you finish."),
            ("Analyze", "Profile, splits, heart rate zones and best efforts for every outing."),
        ],
        "demo": {"left": "to go", "km": "km", "time": "time", "gain": "elev. gain",
                 "phone": "iPhone", "watch": "Apple Watch", "route": "GPX route", "activity": "Activity",
                 "splits": "Splits", "off": "Off route"},
        "standalone_title": "Your watch works on its own.",
        "standalone": "Record, navigate and save to Health even if you leave your iPhone at home. With your wrist down, the dot keeps moving.",
        "shots_label": "Screenshots",
        "shots_title": "Take a look.",
        "shots": ["01-hero", "02-navigate", "03-connected", "04-maps", "05-analysis", "06-sports", "07-standalone", "08-zones"],
        "free_title": "Free. No fine print.",
        "free": ["No ads", "No subscriptions", "No account, no sign-up", "Your data stays on your devices"],
        "close_title": "Head for the <em>mountains</em>.",
        "close": "Load a route, raise your wrist and go.",
        "footer_support": "Support", "footer_privacy": "Privacy",
        "footer_note": "Path is an app by LightSide Studio. Apple Watch and iPhone are trademarks of Apple Inc.",
        "back": "Path",
    },
}

# MARK: Textos legales y de soporte (cortos y claros)

PRIVACY = {
    "es": {
        "title": "Política de privacidad",
        "intro": "Path no recoge tus datos. Todo lo que mide se queda en tu Apple Watch y en tu iPhone, y solo sale de ahí cuando tú decides compartirlo.",
        "sections": [
            ("Responsable", [f"LightSide Studio, estudio dirigido por Lucas Longueira. Contacto para cualquier cuestión de privacidad: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
            ("Qué datos usa la app y dónde se quedan", [
                "<strong>Ubicación</strong>: para situarte en el mapa, medir la distancia y avisarte si te sales de la ruta. En segundo plano solo se usa mientras grabas una actividad.",
                "<strong>Salud</strong>: la app lee tu frecuencia cardíaca y tus calorías durante la actividad, y guarda en la app Salud los entrenamientos que tú elijas (con su recorrido, distancia, pulso y calorías). Los datos de Salud nunca se usan para publicidad ni se comparten con terceros.",
                "<strong>Movimiento</strong>: el podómetro, para contar pasos y cadencia.",
                "<strong>Rutas y actividades</strong>: los archivos GPX que importas y el registro de tus actividades se guardan en tus dispositivos. Entre el iPhone y el Apple Watch viajan directamente, con la conexión del propio sistema de Apple.",
                "Todo esto se guarda solo en tus dispositivos. <strong>No tenemos servidores, no hay cuentas y no recibimos ningún dato tuyo.</strong>",
            ]),
            ("Mapas", [
                "Para dibujar el mapa, la app descarga imágenes de Apple Maps y de OpenTopoMap. Esos servicios reciben la petición de la zona del mapa que se muestra y tu dirección IP, como cualquier página web, pero no tu identidad ni tu actividad. Se rigen por sus propias políticas: <a href=\"https://www.apple.com/es/legal/privacy/\">Apple</a> y <a href=\"https://opentopomap.org/about\">OpenTopoMap</a>.",
            ]),
            ("Lo que compartes tú", [
                "Si exportas una actividad o compartes una ruta, el archivo va a donde tú elijas (Mail, Mensajes, Archivos…). Si guardas una actividad en Salud, las apps a las que tú hayas dado permiso en Salud, como Strava, podrán leerla.",
            ]),
            ("Publicidad y analítica", ["Path no lleva publicidad ni herramientas de analítica o seguimiento de terceros."]),
            ("Tus derechos", [
                "Como no guardamos datos tuyos, no hay nada que pedirnos que borremos: para eliminarlos basta con borrar las actividades en la app o desinstalarla. Los entrenamientos guardados en Salud se gestionan desde la app Salud. Para cualquier duda, escríbenos; si crees que algo no se ha atendido bien, puedes reclamar ante la Agencia Española de Protección de Datos (<a href=\"https://www.aepd.es\">www.aepd.es</a>).",
            ]),
            ("Menores", ["Path no está dirigida a menores de 13 años y no recoge datos de nadie."]),
            ("Cambios", ["Si esta política cambia, se actualizará aquí con su fecha."]),
        ],
    },
    "en": {
        "title": "Privacy Policy",
        "intro": "Path doesn't collect your data. Everything it measures stays on your Apple Watch and your iPhone, and only leaves them when you choose to share it.",
        "sections": [
            ("Who we are", [f"LightSide Studio, a studio run by Lucas Longueira. Contact for any privacy matter: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
            ("What the app uses and where it stays", [
                "<strong>Location</strong>: to show you on the map, measure distance and warn you if you leave the route. In the background it's only used while you're recording an activity.",
                "<strong>Health</strong>: the app reads your heart rate and calories during the activity, and saves the workouts you choose to the Health app (with their route, distance, heart rate and calories). Health data is never used for advertising or shared with third parties.",
                "<strong>Motion</strong>: the pedometer, to count steps and cadence.",
                "<strong>Routes and activities</strong>: the GPX files you import and your activity records are stored on your devices. They travel directly between your iPhone and your Apple Watch over Apple's own connection.",
                "All of this is stored only on your devices. <strong>We have no servers, there are no accounts and we receive none of your data.</strong>",
            ]),
            ("Maps", [
                "To draw the map, the app downloads images from Apple Maps and OpenTopoMap. Those services receive the request for the map area being shown and your IP address, like any website, but not your identity or your activity. They follow their own policies: <a href=\"https://www.apple.com/legal/privacy/\">Apple</a> and <a href=\"https://opentopomap.org/about\">OpenTopoMap</a>.",
            ]),
            ("What you share", [
                "If you export an activity or share a route, the file goes wherever you choose (Mail, Messages, Files…). If you save an activity to Health, the apps you've allowed in Health, such as Strava, can read it.",
            ]),
            ("Ads and analytics", ["Path has no ads and no third-party analytics or tracking."]),
            ("Your rights", [
                "Since we don't store any of your data, there's nothing to ask us to delete: to remove it, just delete activities in the app or uninstall it. Workouts saved to Health are managed in the Health app. For any question, write to us; if you feel something wasn't handled properly, you can complain to the Spanish Data Protection Agency (<a href=\"https://www.aepd.es\">www.aepd.es</a>).",
            ]),
            ("Children", ["Path isn't directed at children under 13 and collects no one's data."]),
            ("Changes", ["If this policy changes, it will be updated here with its date."]),
        ],
    },
}

SUPPORT = {
    "es": {
        "title": "Soporte",
        "intro": f"¿Algo no va como esperabas? Aquí tienes lo más habitual. Si no lo encuentras, escríbenos a <a href=\"mailto:{EMAIL}\">{EMAIL}</a> y te respondemos.",
        "faq": [
            ("¿Necesito el iPhone para usar Path?", "No. El Apple Watch graba, navega y guarda en Salud por sí solo. El iPhone sirve para importar rutas, enviarlas al reloj y ver el análisis de cada actividad."),
            ("¿Cómo paso una ruta al reloj?", "Abre el archivo GPX en el iPhone (desde Archivos, Mail, AirDrop o WhatsApp) y elige Path, o toca + en Rutas. Después, «Enviar al reloj». Si el reloj no está cerca, la ruta queda en cola y se envía sola al reconectar."),
            ("El iPhone dice «Sin conexión» con el reloj", "Abre Path en el reloj, comprueba que el Bluetooth del iPhone está activado y que el reloj está emparejado en la app Watch. Si sigue igual, reinicia el reloj y luego el iPhone."),
            ("¿Cómo subo mis actividades a Strava?", "Conecta Strava con Salud una vez (en Strava: Ajustes → Aplicaciones, servicios y dispositivos → Salud). Después, en Path, toca «Guardar en Salud» en las actividades que quieras y llegarán a Strava solas."),
            ("Rechacé el permiso de Salud por error", "En el reloj: Ajustes → Privacidad y seguridad → Salud → Path, y actívalo todo. En el iPhone: Ajustes → Privacidad y seguridad → Salud → Path."),
            ("¿Puedo ver el mapa con la muñeca bajada?", "Sí. Con una actividad en marcha, al bajar la muñeca la pantalla se queda como estaba, atenuada: el recorrido y tu posición siguen avanzando sobre negro. Si quieres ver también el mapa, activa «Siempre activa» en los ajustes de Path en el reloj (gasta más batería). En el reloj, Ajustes → Pantalla y brillo → Siempre activa tiene que estar activado, también para Path."),
            ("¿Funciona sin cobertura?", "Sí. La grabación y el GPS no necesitan conexión. El mapa topográfico se descarga al cargar la ruta, así que puedes navegar sin cobertura; zonas nuevas fuera de la ruta necesitan conexión."),
        ],
    },
    "en": {
        "title": "Support",
        "intro": f"Something not working as expected? Here are the most common questions. If yours isn't here, write to <a href=\"mailto:{EMAIL}\">{EMAIL}</a> and we'll get back to you.",
        "faq": [
            ("Do I need my iPhone to use Path?", "No. Your Apple Watch records, navigates and saves to Health on its own. The iPhone is for importing routes, sending them to your watch and viewing each activity's analysis."),
            ("How do I get a route onto my watch?", "Open the GPX file on your iPhone (from Files, Mail, AirDrop or WhatsApp) and choose Path, or tap + in Routes. Then tap “Send to watch”. If the watch isn't nearby, the route is queued and sent automatically when it reconnects."),
            ("My iPhone says the watch is “Offline”", "Open Path on your watch, make sure Bluetooth is on on your iPhone and that the watch is paired in the Watch app. If it still doesn't connect, restart the watch and then the iPhone."),
            ("How do I upload my activities to Strava?", "Connect Strava to Health once (in Strava: Settings → Applications, Services, and Devices → Health). Then, in Path, tap “Save to Health” on the activities you want and they'll reach Strava on their own."),
            ("I denied Health access by mistake", "On your watch: Settings → Privacy & Security → Health → Path, and turn everything on. On your iPhone: Settings → Privacy & Security → Health → Path."),
            ("Can I see the map with my wrist down?", "Yes. During an activity, when you lower your wrist the screen stays as it was, dimmed: your track and position keep moving on black. To see the map too, turn on “Always On” in Path's settings on your watch (it uses more battery). On your watch, Settings → Display & Brightness → Always On must be on, including for Path."),
            ("Does it work without signal?", "Yes. Recording and GPS don't need a connection. The topo map is downloaded when you load the route, so you can navigate without coverage; new areas off the route need a connection."),
        ],
    },
}


def esc(s):
    return html.escape(s, quote=True)


def head(c, title, description, path, og):
    url = BASE + c["dir"] + path
    alt = BASE + (COPY["en"]["dir"] if c["lang"] == "es" else COPY["es"]["dir"])
    return f"""<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{c['lang']}" href="{url}">
<link rel="alternate" hreflang="{'en' if c['lang'] == 'es' else 'es'}" href="{alt}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Path">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/{c['lang']}/og.jpg">
<meta property="og:locale" content="{c['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#191B1C">
<link rel="icon" href="{og}assets/icon.png">
<link rel="apple-touch-icon" href="{og}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="{og}assets/site.css">
</head>
<body>
<div class="aura" aria-hidden="true"><span></span></div>
"""


def nav(c, up, anchors=True):
    p = c["pages"]
    home = p["index"]
    links = (f'<a href="#que" class="oculta-movil">{c["nav"][0]}</a>'
             f'<a href="#capturas" class="oculta-movil">{c["nav"][1]}</a>') if anchors else ""
    return f"""<header class="nav" id="nav"><div class="nav-inner"><div class="wrap">
  <a href="{home}" class="marca"><img src="{up}assets/icon.png" alt="" width="28" height="28"><span>Path</span></a>
  <nav>{links}<a href="{p['support']}" class="oculta-movil">{c['nav'][2]}</a>
    <a href="{c['other']}{'' if c['lang'] == 'en' else ''}" class="idioma" lang="{'en' if c['lang'] == 'es' else 'es'}">{c['other_label']}</a>
    <a class="btn btn--cta btn--peq js-appstore" href="#">{c['download']}</a></nav>
</div></div></header>
"""


def footer(c, up):
    p = c["pages"]
    return f"""<footer class="pie"><div class="wrap">
  <div class="col"><div class="marca"><img src="{up}assets/icon.png" alt="" width="28" height="28"><span>Path</span></div>
    <p>{c['footer_note']}</p><p class="copy">The way is yours · © 2026 LightSide Studio</p></div>
  <nav><a href="{p['support']}">{c['footer_support']}</a><a href="{p['privacy']}">{c['footer_privacy']}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a><a href="{c['other']}" lang="{'en' if c['lang'] == 'es' else 'es'}">{c['other_label']}</a></nav>
</div></footer>
<script>window.PATH = {{ appstore: {APPSTORE_URL!r}, soon: {c['soon']!r} }};</script>
<script src="{up}assets/site.js" defer></script>
</body></html>
"""


ROUTE_D = "M-20,250 C60,230 90,180 150,175 S240,205 300,160 S380,70 460,90 S560,150 640,110"


def demos(c):
    d = c["demo"]
    return [
        # Navega: la ruta se dibuja, el punto avanza dejando su rastro.
        f"""<div class="demo demo-nav"><svg viewBox="0 0 640 280" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <g class="curvas">{''.join(f'<path d="M-40,{60 + i * 34} C160,{30 + i * 34} 320,{120 + i * 30} 680,{50 + i * 36}"/>' for i in range(7))}</g>
  <path class="ruta-borde" d="{ROUTE_D}"/><path class="ruta" d="{ROUTE_D}"/>
  <path class="rastro" id="rastro" d="{ROUTE_D}"/>
  <circle class="yo" r="11"><animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;0.85;0.85" keyTimes="0;0.85;1" calcMode="linear" path="{ROUTE_D}"/></circle>
</svg><div class="hud"><b class="num">{'3,0' if c['lang'] == 'es' else '3.0'}</b><span>{d['km']} · {d['left']}</span></div></div>""",
        # Graba: cifras que avanzan.
        f"""<div class="demo demo-cifras">
  <div><b class="num js-tiempo">41:59</b><span>{d['time']}</span></div>
  <div><b class="num js-km">{'4,48' if c['lang'] == 'es' else '4.48'}</b><span>{d['km']}</span></div>
  <div><b class="num naranja js-desnivel">+198</b><span>{d['gain']}</span></div>
</div>""",
        # Conectadas: iPhone y reloj, con rutas y actividades yendo y viniendo.
        f"""<div class="demo demo-sync">
  <div class="aparato"><svg viewBox="0 0 24 24"><rect x="6" y="2" width="12" height="20" rx="3"/></svg><span>{d['phone']}</span></div>
  <div class="carril"><i class="ida">{d['route']}</i><i class="vuelta">{d['activity']}</i></div>
  <div class="aparato"><svg viewBox="0 0 24 24"><rect x="5" y="5" width="14" height="14" rx="4"/><path d="M8 5V2h8v3M8 19v3h8v-3"/></svg><span>{d['watch']}</span></div>
</div>""",
        # Analiza: perfil que se rellena y parciales que crecen.
        f"""<div class="demo demo-analisis js-analisis"><svg viewBox="0 0 300 90" preserveAspectRatio="none" aria-hidden="true">
  <path class="area" d="M0,88 L0,70 C40,64 60,40 100,38 S160,20 200,26 S260,52 300,46 L300,88 Z"/>
  <path class="linea" d="M0,70 C40,64 60,40 100,38 S160,20 200,26 S260,52 300,46"/></svg>
  <div class="parciales"><span>{d['splits']}</span>{''.join(f'<i style="--w:{w}%"></i>' for w in (62, 48, 80, 70, 92, 58))}</div>
</div>""",
    ]


def index(c):
    up = "../" if c["dir"] else ""
    features = "".join(
        f"""<article class="card rv" data-d="{i}"><h3><span class="n">{i + 1}</span>{esc(t)}</h3><p>{esc(s)}</p>{demo}</article>"""
        for i, ((t, s), demo) in enumerate(zip(c["features"], demos(c))))
    shots = "".join(f'<figure><img src="{up}assets/{c["lang"]}/{s}.jpg" alt="" loading="lazy" width="540" height="1173"></figure>'
                    for s in c["shots"])
    free = "".join(f"<li><i></i>{esc(f)}</li>" for f in c["free"])
    return head(c, c["title"], c["description"], c["pages"]["index"], up) + nav(c, up) + f"""
<main id="top">
<section class="hero">
  <div class="hero-texto">
    <p class="kicker entra">{c['kicker']}</p>
    <h1 class="entra" data-d="1">{c['h1']}</h1>
    <p class="sub entra" data-d="2">{c['sub']}</p>
    <div class="botonera entra" data-d="3"><a class="btn btn--cta js-appstore" href="#">{c['appstore']}</a></div>
    <p class="nota entra" data-d="4">{c['note']}</p>
  </div>
  <div class="hero-visual entra" data-d="2" aria-hidden="true">
    <svg class="hero-mapa" viewBox="0 0 600 600">
      <g class="curvas">{''.join(f'<ellipse cx="300" cy="320" rx="{60 + i * 34}" ry="{40 + i * 26}" transform="rotate(-18 300 320)"/>' for i in range(9))}</g>
      <path class="ruta-borde" d="M-20,470 C90,430 140,360 230,350 S360,330 400,250 S500,120 640,90"/>
      <path class="ruta dibuja" d="M-20,470 C90,430 140,360 230,350 S360,330 400,250 S500,120 640,90"/>
    </svg>
    <img class="reloj flota" src="{up}assets/{c['lang']}/w-nav.png" alt="">
    <img class="reloj reloj-2 flota-2" src="{up}assets/{c['lang']}/w-metrics.png" alt="">
  </div>
</section>

<section class="wrap" id="que">
  <p class="label rv">{c['features_label']}</p>
  <h2 class="grande rv">{c['features_title']}</h2>
  <div class="cards">{features}</div>
</section>

<section class="wrap solo rv">
  <img src="{up}assets/{c['lang']}/w-overview.png" alt="" loading="lazy">
  <div><h2 class="grande">{c['standalone_title']}</h2><p>{c['standalone']}</p></div>
</section>

<section class="capturas" id="capturas">
  <div class="wrap"><p class="label rv">{c['shots_label']}</p><h2 class="grande rv">{c['shots_title']}</h2></div>
  <div class="tira">{shots}</div>
</section>

<section class="wrap"><div class="gratis rv"><div class="brillo"></div><h2>{c['free_title']}</h2><ul>{free}</ul></div></section>

<section class="wrap cierre rv">
  <h2>{c['close_title']}</h2><p>{c['close']}</p>
  <div class="botonera"><a class="btn btn--cta js-appstore" href="#">{c['appstore']}</a></div>
</section>
</main>
""" + footer(c, up)


def document(c, kind):
    up = "../" if c["dir"] else ""
    if kind == "privacy":
        t = PRIVACY[c["lang"]]
        updated = ("Última actualización: " if c["lang"] == "es" else "Last updated: ") + UPDATED[c["lang"]]
        body = "".join(f"<h2>{esc(h)}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in t["sections"])
        meta = f'<p class="meta">{updated}</p>'
    else:
        t = SUPPORT[c["lang"]]
        body = "".join(f"<details class=\"faq rv\"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in t["faq"])
        meta = ""
    return head(c, f"{t['title']} · Path", t["intro"][:150], c["pages"][kind], up) + nav(c, up, anchors=False) + f"""
<main class="doc wrap">
  <header class="doc-cab"><h1 class="entra">{t['title']}</h1>{meta}<p class="entradilla entra" data-d="1">{t['intro']}</p></header>
  {body}
</main>
""" + footer(c, up)


def main():
    for c in COPY.values():
        folder = os.path.join(ROOT, c["dir"])
        os.makedirs(folder, exist_ok=True)
        open(os.path.join(folder, c["pages"]["index"]), "w").write(index(c))
        open(os.path.join(folder, c["pages"]["privacy"]), "w").write(document(c, "privacy"))
        open(os.path.join(folder, c["pages"]["support"]), "w").write(document(c, "support"))
    print("Listo")


if __name__ == "__main__":
    main()
