import os

new_css = """
    /* ── TOKENS ESTILO APPLE / FUTURISTA ────────────────────────────────────── */
    :root {
      --bg: #000000;
      --surface: rgba(255, 255, 255, 0.03);
      --surface-hover: rgba(255, 255, 255, 0.08);
      
      --text: #F5F5F7;
      --text-dim: #86868B;
      --border: rgba(255, 255, 255, 0.1);
      --border-light: rgba(255, 255, 255, 0.05);
      
      --accent: #2997FF;
      --accent-glow: rgba(41, 151, 255, 0.3);
      --eficia-lime: #90C31F;
      
      --ff-display: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --ff-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

      --transition: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      --shadow-glass: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
    html { scroll-behavior: smooth; background: var(--bg); }
    body { font-family: var(--ff-body); background: var(--bg); color: var(--text); overflow-x: hidden; line-height: 1.5; font-weight: 400; letter-spacing: -0.01em; }
    a { color: inherit; text-decoration: none; }
    button { cursor: pointer; font-family: var(--ff-body); border: none; background: none; color: inherit; }
    img, svg { max-width: 100%; display: block; }

    /* ── MESH BACKGROUND (SUBTLE) ────────────────────────────────────────── */
    .mesh-bg { position: fixed; inset: 0; z-index: -1; background: #000; overflow: hidden; }
    .mesh-blob { position: absolute; border-radius: 50%; filter: blur(140px); opacity: 0.4; animation: float 30s infinite alternate ease-in-out; }
    .blob-1 { top: -20%; right: -10%; width: 60vw; height: 60vw; background: radial-gradient(circle, rgba(41,151,255,0.4) 0%, transparent 70%); }
    .blob-2 { bottom: -20%; left: -10%; width: 70vw; height: 70vw; background: radial-gradient(circle, rgba(144,195,31,0.2) 0%, transparent 70%); animation-duration: 40s; animation-direction: alternate-reverse; }
    @keyframes float { 0% { transform: translate(0, 0); } 100% { transform: translate(-5vw, 5vw); } }

    /* ── TYPOGRAPHY ─────────────────────────────────────────────────────── */
    .section-heading { font-size: clamp(40px, 5vw, 64px); font-weight: 700; letter-spacing: -0.04em; line-height: 1.05; color: var(--text); margin-bottom: 24px; }
    .section-sub { font-size: clamp(18px, 2vw, 24px); color: var(--text-dim); font-weight: 400; max-width: 700px; margin-bottom: 80px; line-height: 1.4; letter-spacing: -0.015em; }
    .section-label { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-dim); margin-bottom: 16px; display: block; }
    
    .text-gradient { background: linear-gradient(90deg, #FFF 0%, #86868B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

    /* ── BUTTONS ────────────────────────────────────────────────────────── */
    .btn { display: inline-flex; align-items: center; justify-content: center; padding: 16px 32px; font-size: 15px; font-weight: 500; border-radius: 99px; transition: var(--transition); cursor: pointer; letter-spacing: -0.01em; }
    .btn-primary { background: #FFFFFF; color: #000000; }
    .btn-primary:hover { transform: scale(1.02); background: #E5E5EA; }
    .btn-secondary { background: var(--surface); color: var(--text); border: 1px solid var(--border); backdrop-filter: blur(20px); }
    .btn-secondary:hover { background: var(--surface-hover); }

    /* ── NAV ────────────────────────────────────────────────────────────── */
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 20px 48px; display: flex; justify-content: space-between; align-items: center; transition: var(--transition); border-bottom: 1px solid transparent; }
    nav.scrolled { padding: 16px 48px; background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(24px) saturate(180%); border-bottom: 1px solid var(--border-light); }
    .nav-name { font-size: 24px; font-weight: 700; letter-spacing: -0.05em; color: #fff; }

    /* ── SECTIONS BASE ──────────────────────────────────────────────────── */
    section { padding: 160px 48px; position: relative; }
    .section-inner { max-width: 1200px; margin: 0 auto; }

    /* ── TICKER ─────────────────────────────────────────────────────────── */
    .ticker { background: rgba(255,255,255,0.02); border-bottom: 1px solid var(--border-light); padding: 12px 0; overflow: hidden; white-space: nowrap; backdrop-filter: blur(10px); }
    .ticker-inner { display: inline-flex; gap: 64px; animation: ticker 40s linear infinite; }
    .ticker-item { font-size: 13px; color: var(--text-dim); display: flex; align-items: center; gap: 12px; font-weight: 400; letter-spacing: 0.02em; }
    .ticker-dot { width: 6px; height: 6px; background: var(--text-dim); border-radius: 50%; opacity: 0.5; }

    /* ── HERO ───────────────────────────────────────────────────────────── */
    .hero { min-height: 100vh; display: flex; align-items: center; padding-top: 180px; justify-content: center; text-align: center; }
    .hero-content { max-width: 900px; position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 500; color: var(--text-dim); border: 1px solid var(--border); padding: 8px 16px; border-radius: 99px; margin-bottom: 32px; background: var(--surface); backdrop-filter: blur(20px); }
    .hero-headline { font-size: clamp(48px, 8vw, 96px); font-weight: 700; letter-spacing: -0.05em; line-height: 1; margin-bottom: 32px; color: #fff; }
    .hero-sub { max-width: 600px; font-size: 20px; margin-bottom: 48px; }
    .hero-ctas { display: flex; gap: 16px; justify-content: center; }

    /* ── GLASS CARDS (BENTO BOX) ────────────────────────────────────────── */
    .bento-grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px; }
    .glass-card { background: var(--surface); backdrop-filter: blur(40px) saturate(180%); border: 1px solid var(--border-light); border-radius: 32px; padding: 40px; box-shadow: var(--shadow-glass); transition: var(--transition); overflow: hidden; position: relative; }
    .glass-card:hover { border-color: rgba(255,255,255,0.2); background: var(--surface-hover); }

    /* ── METRICS ────────────────────────────────────────────────────────── */
    .metrics-section { padding: 0 48px 120px; margin-top: -60px; z-index: 10; position: relative; }
    .metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1200px; margin: 0 auto; }
    .metric-card { padding: 32px; display: flex; flex-direction: column; gap: 16px; }
    .metric-icon-svg { width: 32px; height: 32px; stroke: var(--text); stroke-width: 1.5; fill: none; opacity: 0.8; }
    .metric-value { font-size: 36px; font-weight: 600; letter-spacing: -0.04em; color: #fff; line-height: 1; }
    .metric-label { font-size: 14px; color: var(--text-dim); }

    /* ── LOGOS ──────────────────────────────────────────────────────────── */
    .logos-bar { padding: 60px 48px; display: flex; align-items: center; justify-content: center; gap: 48px; border-top: 1px solid var(--border-light); border-bottom: 1px solid var(--border-light); flex-wrap: wrap; }
    .logo-text { font-size: 16px; font-weight: 600; color: var(--text-dim); letter-spacing: -0.02em; }

    /* ── PROCESO / COMO FUNCIONA ───────────────────────────────────────── */
    .step-card { grid-column: span 3; display: flex; flex-direction: column; gap: 24px; }
    @media(max-width: 1024px) { .step-card { grid-column: span 6; } }
    @media(max-width: 768px) { .step-card { grid-column: span 12; } }
    .step-num { font-size: 14px; font-weight: 600; color: var(--text-dim); }
    .step-title { font-size: 24px; font-weight: 600; color: #fff; letter-spacing: -0.03em; }
    .step-desc { font-size: 16px; color: var(--text-dim); line-height: 1.5; }

    /* ── SECTORES (BENTO) ──────────────────────────────────────────────── */
    .sector-item { padding: 32px; border-bottom: 1px solid var(--border-light); cursor: pointer; transition: var(--transition); display: flex; justify-content: space-between; align-items: center; }
    .sector-item:last-child { border-bottom: none; }
    .sector-item:hover { background: var(--surface-hover); padding-left: 40px; }
    .sector-name { font-size: 32px; font-weight: 600; letter-spacing: -0.03em; color: var(--text-dim); transition: var(--transition); }
    .sector-item.active .sector-name { color: #fff; }
    
    .sector-detail { padding: 48px; height: 100%; display: flex; flex-direction: column; justify-content: center; }
    .use-case { margin-bottom: 32px; }
    .use-case-title { font-size: 20px; font-weight: 600; color: #fff; margin-bottom: 8px; letter-spacing: -0.02em; }
    .use-case p { font-size: 16px; color: var(--text-dim); }

    /* ── DEMO CHAT (NATIVE APPLE STYLE) ────────────────────────────────── */
    .chat-window { background: rgba(20, 20, 22, 0.6); backdrop-filter: blur(40px) saturate(180%); border-radius: 32px; overflow: hidden; border: 1px solid var(--border-light); height: 600px; display: flex; flex-direction: column; }
    .chat-header { padding: 24px; border-bottom: 1px solid var(--border-light); display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.02); }
    .chat-avatar { width: 48px; height: 48px; background: linear-gradient(135deg, #2997FF, #000); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 20px; color: #fff; border: 1px solid rgba(255,255,255,0.1); }
    .chat-name { font-size: 16px; font-weight: 600; color: #fff; }
    .chat-status { font-size: 13px; color: var(--text-dim); }
    .chat-messages { padding: 24px; flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; }
    .msg { max-width: 75%; padding: 14px 20px; font-size: 16px; line-height: 1.4; letter-spacing: -0.01em; }
    .msg.bot { background: rgba(255,255,255,0.08); color: #fff; align-self: flex-start; border-radius: 20px 20px 20px 4px; }
    .msg.user { background: var(--accent); color: #fff; align-self: flex-end; border-radius: 20px 20px 4px 20px; }
    .chat-input-row { padding: 20px 24px; border-top: 1px solid var(--border-light); display: flex; gap: 12px; background: rgba(255,255,255,0.02); }
    .chat-input-row input { flex: 1; background: rgba(255,255,255,0.05); border: 1px solid var(--border-light); border-radius: 99px; padding: 16px 24px; color: #fff; font-size: 16px; outline: none; transition: var(--transition); }
    .chat-input-row input:focus { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.2); }
    .chat-send { background: #fff; color: #000; border-radius: 50%; width: 52px; height: 52px; display: flex; align-items: center; justify-content: center; transition: var(--transition); cursor:pointer; }
    .chat-send svg { width: 24px; height: 24px; stroke: #000; stroke-width: 2; fill: none; }
    
    .scenario-btn { background: var(--surface); border: 1px solid var(--border-light); border-radius: 24px; padding: 24px; cursor: pointer; text-align: left; transition: var(--transition); margin-bottom: 16px; }
    .scenario-btn:hover, .scenario-btn.active { background: var(--surface-hover); border-color: rgba(255,255,255,0.2); transform: scale(1.02); }
    .scenario-title { font-size: 18px; font-weight: 600; color: #fff; margin-bottom: 8px; letter-spacing: -0.02em; }
    .scenario-desc { font-size: 14px; color: var(--text-dim); }

    /* ── ROI CALCULATOR (NATIVE iOS STYLE) ─────────────────────────────── */
    .roi-left { padding-right: 64px; }
    .calc-field { margin-bottom: 40px; }
    .calc-label { font-size: 16px; color: #fff; font-weight: 500; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; }
    .calc-label span { font-size: 20px; font-weight: 600; color: var(--text-dim); }
    input[type=range] { width: 100%; height: 4px; background: rgba(255,255,255,0.2); border-radius: 99px; appearance: none; outline: none; }
    input[type=range]::-webkit-slider-thumb { appearance: none; width: 28px; height: 28px; background: #fff; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    
    .roi-result { text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%; }
    .roi-big { font-size: clamp(64px, 8vw, 120px); font-weight: 700; letter-spacing: -0.05em; background: linear-gradient(180deg, #FFFFFF 0%, #86868B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; margin-bottom: 16px; }
    .roi-sub { font-size: 18px; color: var(--text-dim); margin-bottom: 48px; }
    .roi-row { display: flex; justify-content: space-between; font-size: 16px; padding: 16px 0; border-bottom: 1px solid var(--border-light); }
    .roi-row-label { color: var(--text-dim); }
    .roi-row-val { font-weight: 600; color: #fff; }

    /* ── ECOSISTEMA ─────────────────────────────────────────────────────── */
    .eco-item { padding: 40px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    .eco-name { font-size: 20px; font-weight: 600; color: #fff; margin-bottom: 8px; letter-spacing: -0.02em; }
    .eco-desc { font-size: 14px; color: var(--text-dim); }

    /* ── COMPARADOR ─────────────────────────────────────────────────────── */
    .compare-grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 1px; background: var(--border-light); border-radius: 32px; overflow: hidden; border: 1px solid var(--border-light); margin-top: 64px; }
    .compare-col { background: #000; display: flex; flex-direction: column; }
    .compare-col.eficia { background: rgba(255,255,255,0.03); }
    .compare-header { padding: 40px 32px; }
    .compare-col-name { font-size: 24px; font-weight: 600; color: #fff; letter-spacing: -0.03em; }
    .compare-col-sub { font-size: 14px; color: var(--text-dim); margin-top: 8px; }
    .compare-row { padding: 24px 32px; border-top: 1px solid var(--border-light); font-size: 16px; color: var(--text-dim); display: flex; align-items: center; gap: 16px; }
    .compare-col.eficia .compare-row { color: #fff; }
    .compare-feature { padding: 24px 32px; border-top: 1px solid var(--border-light); font-size: 16px; font-weight: 500; color: #fff; display: flex; align-items: center; }
    
    .icon-check, .icon-cross { width: 20px; height: 20px; stroke-width: 2.5; fill: none; }
    .icon-check { stroke: #fff; }
    .icon-cross { stroke: var(--text-dim); }

    /* ── TESTIMONIOS ────────────────────────────────────────────────────── */
    .test-card { padding: 48px; display: flex; flex-direction: column; gap: 32px; }
    .test-quote { font-size: 20px; line-height: 1.5; color: #fff; font-weight: 400; letter-spacing: -0.01em; flex: 1; }
    .test-author { display: flex; align-items: center; gap: 16px; }
    .test-name { font-size: 16px; font-weight: 600; color: #fff; }
    .test-role { font-size: 14px; color: var(--text-dim); }

    /* ── PRICING ────────────────────────────────────────────────────────── */
    .price-card { padding: 48px; display: flex; flex-direction: column; }
    .price-card.featured { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.2); }
    .price-plan { font-size: 24px; font-weight: 600; color: #fff; letter-spacing: -0.03em; margin-bottom: 8px; }
    .price-amount { font-size: 64px; font-weight: 700; color: #fff; letter-spacing: -0.05em; line-height: 1; margin-bottom: 16px; }
    .price-period { font-size: 16px; color: var(--text-dim); margin-bottom: 48px; }
    .price-features { list-style: none; display: flex; flex-direction: column; gap: 20px; margin-bottom: 48px; flex: 1; }
    .price-features li { display: flex; gap: 16px; font-size: 16px; color: var(--text-dim); align-items: center; }
    .price-features li svg { width: 16px; height: 16px; stroke: #fff; flex-shrink: 0; }
    .price-card.featured .price-features li { color: #fff; }

    /* ── FAQ ────────────────────────────────────────────────────────────── */
    .faq-item { border-bottom: 1px solid var(--border-light); }
    .faq-q { padding: 32px 0; font-size: 20px; font-weight: 500; color: #fff; cursor: pointer; display: flex; justify-content: space-between; align-items: center; letter-spacing: -0.02em; }
    .faq-toggle { width: 24px; height: 24px; position: relative; }
    .faq-toggle::before, .faq-toggle::after { content: ''; position: absolute; background: #fff; top: 50%; left: 50%; transform: translate(-50%, -50%); transition: var(--transition); }
    .faq-toggle::before { width: 16px; height: 2px; }
    .faq-toggle::after { width: 2px; height: 16px; }
    .faq-item.open .faq-toggle::after { transform: translate(-50%, -50%) rotate(90deg); opacity: 0; }
    .faq-a { max-height: 0; overflow: hidden; transition: max-height 0.5s cubic-bezier(0.16, 1, 0.3, 1); font-size: 16px; color: var(--text-dim); line-height: 1.6; }
    .faq-item.open .faq-a { max-height: 300px; padding-bottom: 32px; }

    /* ── CTA FINAL ──────────────────────────────────────────────────────── */
    .cta-final { text-align: center; padding: 160px 48px; }
    .cta-final h2 { font-size: clamp(48px, 6vw, 80px); font-weight: 700; letter-spacing: -0.05em; color: #fff; margin-bottom: 32px; line-height: 1.05; }
    .cta-final p { font-size: 24px; color: var(--text-dim); margin-bottom: 48px; }

    /* ── FOOTER ─────────────────────────────────────────────────────────── */
    footer { padding: 80px 48px; border-top: 1px solid var(--border-light); }
    .footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 48px; max-width: 1200px; margin: 0 auto; }
    .footer-col h4 { font-size: 14px; font-weight: 600; color: #fff; margin-bottom: 24px; letter-spacing: 0.05em; }
    .footer-col a { display: block; font-size: 14px; color: var(--text-dim); margin-bottom: 16px; transition: var(--transition); }
    .footer-col a:hover { color: #fff; }
"""

new_html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eficia — Inteligencia Artificial</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>__NEW_CSS__</style>
</head>
<body>
  <div class="mesh-bg">
    <div class="mesh-blob blob-1"></div>
    <div class="mesh-blob blob-2"></div>
  </div>

  <div class="ticker">
    <div class="ticker-inner" id="ticker"></div>
  </div>

  <nav id="nav">
    <div class="nav-name">eficia</div>
    <a href="#contacto" class="btn btn-secondary" style="padding: 10px 24px; font-size: 13px;">Agendar Demo</a>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <div class="hero-badge">IA Diseñada para Colombia</div>
      <h1 class="hero-headline">
        La automatización<br><span class="text-gradient">reimaginada.</span>
      </h1>
      <p class="hero-sub">
        Transforma tareas repetitivas en procesos inteligentes. Eficia se integra de forma invisible en tu operación para que tú tomes las decisiones importantes.
      </p>
      <div class="hero-ctas">
        <a href="#proceso" class="btn btn-primary">Descubrir Eficia</a>
      </div>
    </div>
  </section>

  <section class="metrics-section">
    <div class="metrics-grid glass-card" style="padding: 0; border: none; background: transparent; backdrop-filter: none; box-shadow: none;">
      <div class="bento-grid" style="gap: 24px;">
        <div class="glass-card" style="grid-column: span 3; display:flex; flex-direction:column; justify-content:space-between; height: 200px;">
          <svg class="metric-icon-svg" viewBox="0 0 24 24"><path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 6V12L16 14" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div>
            <div class="metric-value">12h</div>
            <div class="metric-label">Tiempo ahorrado por semana</div>
          </div>
        </div>
        <div class="glass-card" style="grid-column: span 3; display:flex; flex-direction:column; justify-content:space-between; height: 200px;">
          <svg class="metric-icon-svg" viewBox="0 0 24 24"><path d="M22 12H18L15 21L9 3L6 12H2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div>
            <div class="metric-value">78%</div>
            <div class="metric-label">Reducción de errores manuales</div>
          </div>
        </div>
        <div class="glass-card" style="grid-column: span 3; display:flex; flex-direction:column; justify-content:space-between; height: 200px;">
          <svg class="metric-icon-svg" viewBox="0 0 24 24"><path d="M12 1V23" stroke-linecap="round" stroke-linejoin="round"/><path d="M17 5H9.5C8.57174 5 7.6815 5.36875 7.02513 6.02513C6.36875 6.6815 6 7.57174 6 8.5C6 9.42826 6.36875 10.3185 7.02513 10.9749C7.6815 11.6313 8.57174 12 9.5 12H14.5C15.4283 12 16.3185 12.3687 16.9749 13.0251C17.6313 13.6815 18 14.5717 18 15.5C18 16.4283 17.6313 17.3185 16.9749 17.9749C16.3185 18.6313 15.4283 19 14.5 19H6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div>
            <div class="metric-value">3.2x</div>
            <div class="metric-label">Retorno de inversión (90 días)</div>
          </div>
        </div>
        <div class="glass-card" style="grid-column: span 3; display:flex; flex-direction:column; justify-content:space-between; height: 200px;">
          <svg class="metric-icon-svg" viewBox="0 0 24 24"><path d="M3 21H21" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 7H15" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 11H15" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 15H15" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div>
            <div class="metric-value">+150</div>
            <div class="metric-label">Empresas activas</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="logos-bar">
    <span class="logo-text" style="color: #fff; opacity: 0.5;">Sectores Activos</span>
    <span class="logo-text">Restaurantes</span>
    <span class="logo-text">Construcción</span>
    <span class="logo-text">Salud</span>
    <span class="logo-text">Retail</span>
    <span class="logo-text">Logística</span>
    <span class="logo-text">Legal</span>
    <span class="logo-text">Educación</span>
  </div>

  <section id="proceso">
    <div class="section-inner">
      <span class="section-label">Metodología</span>
      <h2 class="section-heading">Integración invisible.</h2>
      <p class="section-sub">Un proceso estructurado para garantizar resultados desde el primer día, sin fricción operativa ni curvas de aprendizaje complejas.</p>

      <div class="bento-grid">
        <div class="glass-card step-card">
          <div class="step-num">01</div>
          <h3 class="step-title">Diagnóstico</h3>
          <p class="step-desc">Analizamos procesos, datos y herramientas actuales para encontrar los puntos de mayor impacto automatizable.</p>
        </div>
        <div class="glass-card step-card">
          <div class="step-num">02</div>
          <h3 class="step-title">Diseño</h3>
          <p class="step-desc">Estructuramos un plan alineado a objetivos con métricas de éxito claras y flujos de trabajo simplificados.</p>
        </div>
        <div class="glass-card step-card">
          <div class="step-num">03</div>
          <h3 class="step-title">Despliegue</h3>
          <p class="step-desc">Conectamos los modelos de lenguaje directamente en tus plataformas (WhatsApp, correo, CRMs) en menos de 2 semanas.</p>
        </div>
        <div class="glass-card step-card">
          <div class="step-num">04</div>
          <h3 class="step-title">Evolución</h3>
          <p class="step-desc">Ajuste y optimización continua de los modelos según el uso real y la retroalimentación de tu equipo.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="sectores">
    <div class="section-inner">
      <span class="section-label">Especialización</span>
      <h2 class="section-heading">Entiende tu industria.</h2>
      <p class="section-sub">Modelos pre-entrenados para resolver los retos específicos de cada sector en el mercado colombiano.</p>

      <div class="bento-grid">
        <div class="glass-card" style="grid-column: span 5; padding: 0;">
          <div class="sector-item active" onclick="selectSector(this,0)">
            <span class="sector-name">Restaurantes</span>
          </div>
          <div class="sector-item" onclick="selectSector(this,1)">
            <span class="sector-name">Construcción</span>
          </div>
          <div class="sector-item" onclick="selectSector(this,2)">
            <span class="sector-name">Salud</span>
          </div>
          <div class="sector-item" onclick="selectSector(this,3)">
            <span class="sector-name">Retail</span>
          </div>
          <div class="sector-item" onclick="selectSector(this,4)">
            <span class="sector-name">Logística</span>
          </div>
        </div>
        <div class="glass-card" style="grid-column: span 7; display:flex; flex-direction:column; justify-content:center;" id="sectorDetail">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>
  </section>

  <section id="demo">
    <div class="section-inner">
      <span class="section-label">Experiencia en Vivo</span>
      <h2 class="section-heading">Interacción natural.</h2>
      <p class="section-sub">Prueba cómo responde nuestro asistente cognitivo a escenarios reales, comprendiendo el contexto y resolviendo dudas instantáneamente.</p>

      <div class="bento-grid">
        <div style="grid-column: span 5;">
          <div id="scenarioBtns"></div>
        </div>
        <div style="grid-column: span 7;">
          <div class="chat-window">
            <div class="chat-header">
              <div class="chat-avatar">E</div>
              <div>
                <div class="chat-name">Eficia Intelligence</div>
                <div class="chat-status">Conectado</div>
              </div>
            </div>
            <div class="chat-messages" id="chatMessages"></div>
            <div class="chat-input-row">
              <input type="text" id="chatInput" placeholder="Escribe un mensaje..." onkeydown="if(event.key==='Enter')sendChat()">
              <button class="chat-send" onclick="sendChat()">
                <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="calculadora">
    <div class="section-inner">
      <div class="glass-card" style="padding: 80px;">
        <div class="bento-grid">
          <div class="roi-left" style="grid-column: span 6;">
            <span class="section-label">Impacto Financiero</span>
            <h2 class="section-heading" style="font-size: 40px;">Proyección de ahorro.</h2>
            <p class="section-sub" style="margin-bottom: 40px; font-size: 16px;">Calcula el retorno de inversión al liberar a tu equipo de tareas manuales repetitivas.</p>

            <div class="calc-field">
              <div class="calc-label">Empleados en tareas repetitivas <span id="emp-val">5</span></div>
              <input type="range" min="1" max="30" value="5" step="1" oninput="calcROI()" id="emp">
            </div>
            <div class="calc-field">
              <div class="calc-label">Salario mensual promedio <span id="sal-val">$2.5M</span></div>
              <input type="range" min="1000000" max="8000000" value="2500000" step="100000" oninput="calcROI()" id="sal">
            </div>
            <div class="calc-field">
              <div class="calc-label">Tiempo en procesos manuales <span id="rep-val">40%</span></div>
              <input type="range" min="10" max="80" value="40" step="5" oninput="calcROI()" id="rep">
            </div>
          </div>
          <div style="grid-column: span 6;">
            <div class="roi-result">
              <div class="roi-big" id="roiBig">$4.8M</div>
              <div class="roi-sub">Ahorro mensual proyectado (COP)</div>
              
              <div class="roi-row">
                <span class="roi-row-label">Costo operativo manual</span>
                <span class="roi-row-val" id="r1">$5.0M</span>
              </div>
              <div class="roi-row">
                <span class="roi-row-label">Inversión Eficia</span>
                <span class="roi-row-val" style="color: var(--text-dim);">-$590K</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="ecosistema">
    <div class="section-inner">
      <span class="section-label">Conectividad</span>
      <h2 class="section-heading">Se integra con todo.</h2>
      <p class="section-sub">Operamos detrás de escena. Eficia se conecta silenciosamente con las herramientas que tu equipo ya domina.</p>

      <div class="bento-grid">
        <div class="glass-card eco-item" style="grid-column: span 3;">
          <div class="eco-name">WhatsApp</div>
          <div class="eco-desc">Gestión nativa</div>
        </div>
        <div class="glass-card eco-item" style="grid-column: span 6; background: rgba(255,255,255,0.08);">
          <div class="eco-name" style="font-size: 28px;">Eficia Core</div>
          <div class="eco-desc" style="font-size: 16px;">Motor de Procesamiento IA</div>
        </div>
        <div class="glass-card eco-item" style="grid-column: span 3;">
          <div class="eco-name">Google Workspace</div>
          <div class="eco-desc">Datos y Agenda</div>
        </div>
        <div class="glass-card eco-item" style="grid-column: span 4;">
          <div class="eco-name">ERP / SIIGO</div>
          <div class="eco-desc">Facturación automatizada</div>
        </div>
        <div class="glass-card eco-item" style="grid-column: span 4;">
          <div class="eco-name">Sistemas POS</div>
          <div class="eco-desc">Sincronización en tiempo real</div>
        </div>
        <div class="glass-card eco-item" style="grid-column: span 4;">
          <div class="eco-name">API Rest</div>
          <div class="eco-desc">Conexión universal</div>
        </div>
      </div>
    </div>
  </section>

  <section id="faq">
    <div class="section-inner">
      <div class="bento-grid">
        <div style="grid-column: span 5; padding-right: 48px;">
          <span class="section-label">Soporte</span>
          <h2 class="section-heading" style="font-size: 48px;">Dudas comunes.</h2>
          <p class="section-sub" style="font-size: 16px;">Resoluciones claras sobre privacidad, implementación y capacidades técnicas.</p>
        </div>
        <div style="grid-column: span 7;">
          <div id="faqList"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-final">
    <div class="section-inner">
      <h2>El futuro de tu empresa <br>comienza aquí.</h2>
      <p>Automatización inteligente, diseño impecable, resultados inmediatos.</p>
      <a href="#contacto" class="btn btn-primary" style="padding: 24px 48px; font-size: 20px;">Iniciar Transformación</a>
    </div>
  </section>

  <footer>
    <div class="footer-grid">
      <div class="footer-col">
        <div class="nav-name" style="margin-bottom: 16px; font-weight: 700;">eficia</div>
        <p style="font-size: 14px; color: var(--text-dim);">Inteligencia Artificial diseñada<br>para el crecimiento empresarial.</p>
      </div>
      <div class="footer-col">
        <h4>Plataforma</h4>
        <a href="#">Arquitectura</a>
        <a href="#">Seguridad</a>
        <a href="#">Integraciones</a>
      </div>
      <div class="footer-col">
        <h4>Compañía</h4>
        <a href="#">Nosotros</a>
        <a href="#">Casos de Uso</a>
        <a href="#">Contacto</a>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <a href="#">Privacidad</a>
        <a href="#">Términos de Servicio</a>
      </div>
    </div>
    <div style="text-align: center; margin-top: 80px; padding-top: 40px; border-top: 1px solid var(--border-light); color: var(--text-dim); font-size: 12px;">
      &copy; 2026 Eficia. Todos los derechos reservados.
    </div>
  </footer>

  <script>
    // Nav Scroll
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    });

    // Ticker
    const tickerItems = ["Seguridad ISO 27001", "Respuesta en <0.8s", "Modelos de Lenguaje Avanzados", "Procesamiento Paralelo", "Integración Nativa", "Análisis Predictivo", "Soporte 24/7"];
    const t = document.getElementById('ticker');
    t.innerHTML = [...tickerItems, ...tickerItems].map(i => `<span class="ticker-item"><span class="ticker-dot"></span>${i}</span>`).join('');

    // Sectores
    const sectorData = [
      { cases: [{ title: "Pedidos Autónomos", desc: "Gestión conversacional de órdenes y pagos directamente por mensajería, sincronizado con POS." }, { title: "Inventario Predictivo", desc: "Análisis de demanda estacional para optimizar reposición de stock." }] },
      { cases: [{ title: "Cotización Dinámica", desc: "Generación de presupuestos de obra a partir de procesamiento de lenguaje natural." }, { title: "Control de Avance", desc: "Reportes automatizados de proveedores y subcontratistas." }] },
      { cases: [{ title: "Triaje Inteligente", desc: "Pre-evaluación y agendamiento clínico automático con recordatorios." }, { title: "Gestión de Historias", desc: "Estructuración de datos médicos a partir de notas de voz del especialista." }] },
      { cases: [{ title: "Asistencia de Compra", desc: "Recomendación de productos basada en historial y disponibilidad en tiempo real." }, { title: "Soporte Posventa", desc: "Resolución de garantías y devoluciones sin intervención humana." }] },
      { cases: [{ title: "Ruteo Optimizado", desc: "Asignación dinámica de rutas considerando tráfico y ventanas horarias." }, { title: "Trazabilidad", desc: "Actualizaciones proactivas al cliente final sobre el estado de su envío." }] }
    ];

    function selectSector(el, idx) {
      document.querySelectorAll('.sector-item').forEach(c => c.classList.remove('active'));
      el.classList.add('active');
      const d = sectorData[idx];
      document.getElementById('sectorDetail').innerHTML = d.cases.map(c => `<div class="use-case"><div class="use-case-title">${c.title}</div><p>${c.desc}</p></div>`).join('');
    }
    selectSector(document.querySelector('.sector-item'), 0);

    // Chat
    const scenarios = [
      { title: "Consultar Stock", desc: "Pregunta sobre disponibilidad.", q: "¿Tienen disponibilidad de la referencia A-42?", rep: ["Consultando base de datos...", "Sí, tenemos 14 unidades en bodega principal y 3 en tienda norte. ¿Deseas reservarlo?"] },
      { title: "Soporte Técnico", desc: "Reporte de incidencia.", q: "El equipo no enciende y muestra luz roja.", rep: ["Analizando manual de servicio técnico...", "Ese código indica fallo de alimentación. Por favor verifica que el cable esté conectado a un tomacorriente directo. Si persiste, generaré un ticket de soporte."] }
    ];

    document.getElementById('scenarioBtns').innerHTML = scenarios.map((s, i) => `<div class="scenario-btn" onclick="runScenario(${i})" id="sb${i}"><div class="scenario-title">${s.title}</div><div class="scenario-desc">${s.desc}</div></div>`).join('');

    let isTyping = false;
    function addMsg(text, type) {
      const msgs = document.getElementById('chatMessages');
      const d = document.createElement('div');
      d.className = `msg ${type}`;
      d.textContent = text;
      msgs.appendChild(d);
      msgs.scrollTop = msgs.scrollHeight;
    }
    function showTyping() {
      const msgs = document.getElementById('chatMessages');
      const d = document.createElement('div');
      d.className = 'msg bot typing'; d.id = 'typing';
      d.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
      msgs.appendChild(d); msgs.scrollTop = msgs.scrollHeight;
    }
    function removeTyping() { const t = document.getElementById('typing'); if (t) t.remove(); }

    async function runScenario(idx) {
      if(isTyping) return;
      isTyping = true;
      document.querySelectorAll('.scenario-btn').forEach((b, i) => b.classList.toggle('active', i === idx));
      document.getElementById('chatMessages').innerHTML = '';
      const s = scenarios[idx];
      addMsg(s.q, 'user');
      for (let i = 0; i < s.rep.length; i++) {
        showTyping();
        await new Promise(r => setTimeout(r, 800 + i * 400));
        removeTyping();
        addMsg(s.rep[i], 'bot');
        await new Promise(r => setTimeout(r, 300));
      }
      isTyping = false;
    }
    runScenario(0);

    function sendChat() {
      const inp = document.getElementById('chatInput');
      const val = inp.value.trim(); if (!val) return;
      addMsg(val, 'user'); inp.value = '';
      showTyping();
      setTimeout(() => {
        removeTyping();
        addMsg('Esta es una demostración. En producción, la IA buscaría en tu base de conocimientos corporativa para responder con total precisión.', 'bot');
      }, 1500);
    }

    // ROI
    function calcROI() {
      const emp = +document.getElementById('emp').value;
      const sal = +document.getElementById('sal').value;
      const rep = +document.getElementById('rep').value;
      document.getElementById('emp-val').textContent = emp;
      document.getElementById('sal-val').textContent = '$' + (sal / 1000000).toFixed(1) + 'M';
      document.getElementById('rep-val').textContent = rep + '%';
      
      const costoRep = Math.round(emp * sal * (rep / 100));
      const ahorro = Math.round(costoRep * 0.7 - 590000); // 70% reduction minus plan cost
      
      document.getElementById('r1').textContent = '$' + (costoRep / 1000000).toFixed(1) + 'M';
      document.getElementById('roiBig').textContent = '$' + Math.max(ahorro / 1000000, 0).toFixed(1) + 'M';
    }
    calcROI();

    // FAQ
    const faqs = [
      { q: "Arquitectura y Seguridad de Datos", a: "Operamos sobre infraestructura cifrada de extremo a extremo. Los modelos LLM están aislados y tus datos propietarios nunca se utilizan para entrenar modelos públicos." },
      { q: "Tiempos de Implementación", a: "El despliegue estándar toma entre 7 y 14 días. No requiere modificaciones en tu código base actual; utilizamos APIs y conectores nativos." },
      { q: "Mantenimiento y Evolución", a: "Nuestros sistemas incluyen monitoreo 24/7. Las actualizaciones de los modelos subyacentes son automáticas y transparentes para el usuario final." }
    ];
    document.getElementById('faqList').innerHTML = faqs.map((f, i) => `<div class="faq-item" id="faq${i}"><div class="faq-q" onclick="toggleFaq(${i})">${f.q}<div class="faq-toggle"></div></div><div class="faq-a">${f.a}</div></div>`).join('');
    function toggleFaq(i) {
      const el = document.getElementById('faq' + i);
      const was = el.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(f => f.classList.remove('open'));
      if (!was) el.classList.add('open');
    }
  </script>
</body>
</html>"""

new_html_content = new_html_content.replace("__NEW_CSS__", new_css)

with open('Eficia - Official Branding.html', 'w', encoding='utf-8') as f:
    f.write(new_html_content)
