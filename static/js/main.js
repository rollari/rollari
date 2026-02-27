/* ══════════════════════════════════════════════════════
   ROLLARI · AMETHYST  —  Main JS  2026
   ══════════════════════════════════════════════════════ */

/* ── PRELOADER ──────────────────────────────────────── */
window.addEventListener('load', () => {
  const pre = document.getElementById('preloader');
  if (pre) {
    setTimeout(() => pre.classList.add('done'), 400);
  }
});

/* ── SCROLL: navbar + scroll-bar + back-to-top ──────── */
(function () {
  const nav  = document.getElementById('nav');
  const bar  = document.getElementById('scrollBar');
  const btt  = document.getElementById('btt');

  function onScroll() {
    const scrollTop = window.scrollY;
    const docH      = document.documentElement.scrollHeight - window.innerHeight;
    const pct       = docH > 0 ? (scrollTop / docH) * 100 : 0;

    if (nav) nav.classList.toggle('scrolled', scrollTop > 60);
    if (bar) bar.style.width = pct + '%';
    if (btt) btt.classList.toggle('visible', scrollTop > 400);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (btt) btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
})();

/* ── MOBILE MENU ────────────────────────────────────── */
(function () {
  const burger  = document.getElementById('burger');
  const menu    = document.getElementById('mobMenu');
  const close   = document.getElementById('mobClose');
  if (!burger || !menu) return;

  const open  = () => { menu.classList.add('open'); burger.classList.add('open'); document.body.style.overflow = 'hidden'; };
  const shut  = () => { menu.classList.remove('open'); burger.classList.remove('open'); document.body.style.overflow = ''; };

  burger.addEventListener('click', open);
  close?.addEventListener('click', shut);
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', shut));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') shut(); });
})();

/* ── SMOOTH ANCHOR SCROLL ───────────────────────────── */
(function () {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
      const id = this.getAttribute('href');
      if (id === '#') return;
      const el = document.querySelector(id);
      if (el) {
        e.preventDefault();
        window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' });
      }
    });
  });
})();

/* ── REVEAL ON SCROLL ───────────────────────────────── */
(function () {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.08, rootMargin: '0px 0px -44px 0px' });

  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
})();

/* ── COUNTER ANIMATION ──────────────────────────────── */
(function () {
  function run(el) {
    const target = +el.dataset.t;
    const start  = performance.now();
    const dur    = 2400;
    (function step(now) {
      const p = Math.min((now - start) / dur, 1);
      const e = 1 - Math.pow(1 - p, 3); // ease-out cubic
      el.textContent = Math.floor(e * target).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = target.toLocaleString();
    })(start);
  }

  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { run(e.target); obs.unobserve(e.target); } });
  }, { threshold: 0.6 });

  document.querySelectorAll('.counter').forEach(el => obs.observe(el));
})();

/* ── HERO CANVAS PARTICLES ──────────────────────────── */
(function () {
  const canvas = document.getElementById('heroCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, pts = [];

  const COLS = ['168,85,247', '192,132,252', '201,164,82', '124,58,237', '240,220,255'];

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }

  function makeParticle() {
    return {
      x: Math.random() * W,
      y: H + Math.random() * H * .5,
      r: Math.random() * 1.8 + .4,
      vy: Math.random() * .55 + .2,
      vx: (Math.random() - .5) * .28,
      op: Math.random() * .5 + .15,
      col: COLS[Math.floor(Math.random() * COLS.length)],
    };
  }

  function init() { pts = Array.from({ length: 30 }, makeParticle); }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    pts.forEach((p, i) => {
      p.y  -= p.vy;
      p.x  += p.vx;
      p.op -= 0.0005;
      if (p.y < -10 || p.op <= 0) pts[i] = makeParticle();

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${p.col},${p.op})`;
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', () => { resize(); }, { passive: true });
  resize(); init(); draw();
})();

/* ── BOOKING FORM: pre-select experience from URL ───── */
(function () {
  const sel = document.querySelector('select[name="experience"]');
  if (!sel) return;
  const params = new URLSearchParams(window.location.search);
  const exp    = params.get('experience');
  if (exp) {
    const opt = sel.querySelector(`option[value="${exp}"]`);
    if (opt) opt.selected = true;
  }
})();

/* ── GALLERY FILTER (handled inline in gallery.html) ── */

/* ── TOUCH: show fishing card desc on tap ───────────── */
(function () {
  if (!('ontouchstart' in window)) return;
  document.querySelectorAll('.fcard').forEach(c => {
    c.addEventListener('click', () => c.classList.toggle('touch-active'));
  });
})();
