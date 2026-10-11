(function () {
  'use strict';

  // ── El enlace de la App Store ───────────────────────────────────
  // Se pone en tools/build.py (APPSTORE_URL). Mientras esté vacío, los
  // botones dicen «Muy pronto» y no llevan a ninguna parte.
  var cfg = window.PATH || {};
  [].forEach.call(document.querySelectorAll('.js-appstore'), function (a) {
    if (cfg.appstore) {
      a.href = cfg.appstore;
      a.rel = 'noopener';
    } else {
      a.removeAttribute('href');
      a.setAttribute('aria-disabled', 'true');
      if (!a.classList.contains('btn--peq')) a.textContent = cfg.soon;
    }
  });

  var quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ── Barra que se compacta ───────────────────────────────────────
  var nav = document.getElementById('nav');
  function alScroll() { nav.classList.toggle('compacta', window.scrollY > 80); }
  window.addEventListener('scroll', alScroll, { passive: true });
  alScroll();

  // ── Aparición al entrar en pantalla ─────────────────────────────
  function alEntrar(sel, cb, umbral) {
    var els = document.querySelectorAll(sel);
    if (!('IntersectionObserver' in window)) { [].forEach.call(els, cb); return; }
    var io = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { io.unobserve(e.target); cb(e.target); }
      });
    }, { threshold: umbral || 0.18 });
    [].forEach.call(els, function (el) { io.observe(el); });
  }
  alEntrar('.rv', function (el) { el.classList.add('dentro'); });
  alEntrar('.js-analisis', function (el) { el.classList.add('dentro'); }, 0.4);

  if (quieto) return;

  // ── El rastro sigue al punto de la tarjeta «Navega» ─────────────
  // El punto recorre el 85 % de la ruta en el 85 % del ciclo (ver el
  // animateMotion del SVG); el rastro pinta puntos sólo hasta donde va.
  var rastro = document.getElementById('rastro');
  if (rastro && rastro.getTotalLength) {
    var largo = rastro.getTotalLength(), t0 = performance.now(), ciclo = 9000;
    (function paso(ahora) {
      var f = Math.min(((ahora - t0) % ciclo) / ciclo, 0.85);
      var n = Math.floor(f * largo / 15), dash = [];
      for (var i = 0; i < n; i++) dash.push(0, 15);
      dash.push(0, largo + 15);
      rastro.style.strokeDasharray = dash.join(' ');
      requestAnimationFrame(paso);
    })(t0);
  }

  // ── Cifras de «Graba», que avanzan como en el reloj ─────────────
  var tiempo = document.querySelector('.js-tiempo');
  var km = document.querySelector('.js-km');
  var desnivel = document.querySelector('.js-desnivel');
  if (tiempo) {
    var seg = 41 * 60 + 59, dist = 4.48, sube = 198;
    var coma = document.documentElement.lang === 'es';
    setInterval(function () {
      seg += 1; dist += 0.0013; if (seg % 9 === 0) sube += 1;
      var h = Math.floor(seg / 3600), m = Math.floor(seg % 3600 / 60), s = seg % 60;
      tiempo.textContent = (h ? h + ':' + String(m).padStart(2, '0') : m) + ':' + String(s).padStart(2, '0');
      var d = dist.toFixed(2);
      km.textContent = coma ? d.replace('.', ',') : d;
      desnivel.textContent = '+' + sube;
    }, 1000);
  }
})();
