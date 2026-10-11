# Path · web pública

La web de [Path](https://github.com/lDarkSid3/Path), la app de rutas para Apple Watch de
LightSide Studio: <https://lightsidestudio.github.io/path-web/>

- `/` en español y `/en/` en inglés: portada, privacidad y soporte. Son las URL que van en
  App Store Connect (privacidad: `privacidad.html` / `en/privacy.html`; soporte:
  `soporte.html` / `en/support.html`).

## Se genera, no se edita a mano

Las seis páginas salen de `tools/build.py`, con el texto de los dos idiomas en el mismo
archivo para que digan siempre lo mismo:

```bash
python3 tools/build.py
```

El enlace de la App Store está en una línea, `APPSTORE_URL`. Mientras esté vacío, los
botones dicen «Muy pronto en el App Store»; en cuanto se pegue el enlace, se activan solos.

Estilos y animaciones: `assets/site.css` y `assets/site.js`, sin build ni dependencias.
Las imágenes de `assets/es/` y `assets/en/` salen de las de la App Store de la app
(`marketing/appstore/` y la skill `appstore-assets` del repositorio de Path).

## Por qué un repositorio aparte

GitHub Pages no funciona en repositorios privados con plan gratuito. Aquí sólo hay HTML
público.

Contacto: path@lightsidestudio.com
