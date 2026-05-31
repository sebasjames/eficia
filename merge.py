import re
import os

with open('Eficia - Official Branding.html', 'r', encoding='utf-8') as f:
    old_html = f.read()
    
with open(r'C:\Users\sebas\Downloads\eficia_landing_v2_full.html', 'r', encoding='utf-8') as f:
    new_html = f.read()

# CSS extraction (I will just hardcode the mapped CSS in the python script to make it robust)
new_css = """
    /* ── TICKER ─────────────────────────────────────────────── */
    .ticker { background: var(--eficia-blue-dark); padding: 12px 0; overflow: hidden; white-space: nowrap; }
    .ticker-inner { display: inline-flex; gap: 48px; animation: ticker 30s linear infinite; }
    @keyframes ticker { from { transform: translateX(0); } to { transform: translateX(-50%); } }
    .ticker-item { font-size: 14px; color: rgba(255,255,255,0.9); display: flex; align-items: center; gap: 8px; font-weight: 500; }
    .ticker-dot { width: 8px; height: 8px; background: var(--eficia-lime); border-radius: 50%; flex-shrink: 0; }

    /* ── NEW HERO METRICS ──────────────────────────────────────── */
    .metrics-section { padding: 20px 48px 60px; position: relative; z-index: 10; }
    .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto; }
    .metric-card { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); border: 1px solid var(--border); border-radius: 16px; padding: 24px; display: flex; align-items: center; gap: 16px; box-shadow: var(--shadow-sm); transition: var(--transition); }
    .metric-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); border-color: var(--eficia-blue-light); }
    .metric-icon { width: 48px; height: 48px; background: rgba(0, 136, 204, 0.1); color: var(--eficia-blue-dark); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0; }
    .metric-label { font-size: 12px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; font-weight: 600; }
    .metric-value { font-family: var(--ff-display); font-size: 24px; font-weight: 700; color: var(--text); }
    .metric-value span { font-size: 13px; color: var(--eficia-teal); font-weight: 500; font-family: var(--ff-body); margin-left: 8px; }

    /* ── LOGOS BAR ────────────────────────────────────────────── */
    .logos-bar { background: var(--bg); padding: 20px 48px; display: flex; align-items: center; justify-content: center; gap: 32px; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); flex-wrap: wrap; position: relative; z-index: 10; }
    .logos-label { color: var(--text-dim); font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; white-space: nowrap; flex-shrink: 0; }
    .logo-pill { display: inline-flex; align-items: center; gap: 8px; color: var(--text); font-size: 14px; font-weight: 500; white-space: nowrap; padding: 6px 16px; border: 1px solid var(--border); border-radius: 100px; background: rgba(255,255,255,0.5); }

    /* ── SECTORES ─────────────────────────────────────────────── */
    .sectores { background: rgba(0, 150, 136, 0.03); }
    .sectores-header { text-align: center; margin-bottom: 48px; }
    .sectores-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 24px; overflow: hidden; }
    .sector-card { background: var(--bg); padding: 32px; cursor: pointer; transition: var(--transition); }
    .sector-card:hover { background: rgba(0, 136, 204, 0.02); }
    .sector-card.active { background: var(--eficia-blue-dark); color: #fff; }
    .sector-icon { font-size: 32px; margin-bottom: 12px; display: block; }
    .sector-name { font-family: var(--ff-display); font-weight: 700; font-size: 20px; color: var(--text); margin-bottom: 8px; transition: var(--transition); }
    .sector-card.active .sector-name { color: #fff; }
    .sector-desc { font-size: 15px; color: var(--text-dim); line-height: 1.5; transition: var(--transition); }
    .sector-card.active .sector-desc { color: rgba(255,255,255,0.7); }
    .sector-detail { margin-top: 24px; background: var(--bg); border: 1px solid var(--border); border-radius: 24px; padding: 40px; display: none; box-shadow: var(--shadow-sm); }
    .sector-detail.visible { display: block; animation: fadeIn 0.4s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    .detail-inner { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; }
    .use-case { background: rgba(0, 71, 171, 0.03); border-radius: 16px; padding: 24px; border: 1px solid rgba(0, 71, 171, 0.1); }
    .use-case-title { font-family: var(--ff-display); font-weight: 700; color: var(--eficia-blue-dark); font-size: 18px; margin-bottom: 12px; }
    .use-case p { font-size: 15px; color: var(--text-dim); line-height: 1.6; }

    /* ── DEMO CHAT ────────────────────────────────────────────── */
    .demo-chat-section { background: var(--eficia-blue-dark); padding: 120px 48px; color: #fff; }
    .demo-chat-section .section-heading, .demo-chat-section .section-sub, .demo-chat-section .section-label { color: #fff; }
    .demo-chat-section .section-label { color: var(--eficia-lime); }
    .demo-chat-section .section-sub { color: rgba(255,255,255,0.7); }
    .demo-header { text-align: center; margin-bottom: 48px; }
    .demo-wrapper { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; max-width: 1200px; margin: 0 auto; }
    .chat-window { background: #fff; border-radius: 24px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); color: var(--text); }
    .chat-header { background: rgba(0, 71, 171, 0.05); padding: 16px 24px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid var(--border); }
    .chat-avatar { width: 40px; height: 40px; background: var(--eficia-blue-light); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; }
    .chat-name { font-family: var(--ff-display); font-weight: 700; color: var(--text); font-size: 16px; }
    .chat-status { font-size: 12px; color: var(--eficia-teal); font-weight: 500; }
    .chat-messages { padding: 24px; height: 400px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background: #fff; }
    .msg { max-width: 80%; padding: 12px 16px; font-size: 15px; line-height: 1.5; }
    .msg.bot { background: rgba(0, 136, 204, 0.1); color: var(--text); align-self: flex-start; border-radius: 4px 16px 16px 16px; }
    .msg.user { background: var(--eficia-blue-dark); color: #fff; align-self: flex-end; border-radius: 16px 4px 16px 16px; }
    .msg.typing { display: flex; gap: 6px; align-items: center; padding: 16px; }
    .dot { width: 8px; height: 8px; background: rgba(0,0,0,0.3); border-radius: 50%; animation: bounce 1.2s infinite; }
    .dot:nth-child(2) { animation-delay: 0.2s; }
    .dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce { 0%, 60%, 100% { transform: translateY(0); } 30% { transform: translateY(-6px); } }
    .chat-input-row { padding: 16px 24px; border-top: 1px solid var(--border); display: flex; gap: 12px; background: #fff; }
    .chat-input-row input { flex: 1; background: rgba(0,0,0,0.03); border: 1px solid var(--border); border-radius: 99px; padding: 12px 20px; color: var(--text); font-size: 15px; font-family: var(--ff-body); outline: none; transition: var(--transition); }
    .chat-input-row input:focus { border-color: var(--eficia-blue-light); background: #fff; box-shadow: 0 0 0 3px rgba(0, 136, 204, 0.1); }
    .chat-send { background: var(--eficia-blue-dark); border: none; border-radius: 50%; width: 44px; height: 44px; cursor: pointer; color: #fff; font-size: 18px; display: flex; align-items: center; justify-content: center; transition: var(--transition); }
    .chat-send:hover { background: var(--eficia-teal); transform: scale(1.05); }
    .demo-scenarios { display: flex; flex-direction: column; gap: 16px; }
    .scenario-label { font-size: 13px; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; font-weight: 600; }
    .scenario-btn { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; cursor: pointer; text-align: left; transition: var(--transition); color: rgba(255,255,255,0.8); font-size: 15px; font-family: var(--ff-body); }
    .scenario-btn:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.2); color: #fff; }
    .scenario-btn.active { background: rgba(255,255,255,0.15); border-color: var(--eficia-lime); color: #fff; }
    .scenario-tag { display: inline-block; font-size: 11px; background: var(--eficia-lime); color: var(--eficia-blue-dark); padding: 4px 10px; border-radius: 100px; margin-bottom: 8px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; }
    .scenario-title { font-family: var(--ff-display); font-weight: 700; font-size: 16px; margin-bottom: 4px; }

    /* ── ROI CALCULATOR ────────────────────────────────────────── */
    .roi-section { background: var(--bg); }
    .roi-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; max-width: 1200px; margin: 0 auto; }
    .roi-left h2 { margin-bottom: 16px; }
    .roi-left p { margin-bottom: 40px; }
    .calc-field { margin-bottom: 24px; }
    .calc-label { font-size: 14px; color: var(--text-dim); font-weight: 600; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; }
    .calc-label span { font-family: var(--ff-display); font-weight: 800; color: var(--eficia-blue-dark); font-size: 18px; }
    input[type=range] { width: 100%; accent-color: var(--eficia-blue-light); height: 6px; cursor: pointer; background: var(--border); border-radius: 99px; appearance: none; }
    input[type=range]::-webkit-slider-thumb { appearance: none; width: 20px; height: 20px; background: var(--eficia-blue-dark); border-radius: 50%; cursor: pointer; box-shadow: var(--shadow-sm); }
    .roi-result { background: var(--eficia-blue-dark); color: #fff; border-radius: 24px; padding: 48px; position: sticky; top: 120px; box-shadow: var(--shadow-lg); }
    .roi-result .section-label { color: var(--eficia-lime); }
    .roi-big { font-family: var(--ff-display); font-size: 64px; font-weight: 800; color: #fff; line-height: 1; margin-bottom: 8px; }
    .roi-sub { font-size: 15px; color: rgba(255,255,255,0.7); margin-bottom: 40px; }
    .roi-breakdown { display: flex; flex-direction: column; gap: 16px; }
    .roi-row { display: flex; justify-content: space-between; align-items: center; font-size: 15px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .roi-row:last-child { border-bottom: none; }
    .roi-row-label { color: rgba(255,255,255,0.7); }
    .roi-row-val { font-family: var(--ff-display); font-weight: 700; color: #fff; }
    .roi-row-val.pos { color: var(--eficia-lime); }

    /* ── ECOSISTEMA ────────────────────────────────────────────── */
    .ecosistema { background: rgba(0, 71, 171, 0.02); }
    .eco-header { text-align: center; margin-bottom: 48px; }
    .eco-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; max-width: 1200px; margin: 0 auto; }
    .eco-card { background: #fff; border: 1px solid var(--border); border-radius: 20px; padding: 32px 24px; text-align: center; cursor: pointer; transition: var(--transition); box-shadow: var(--shadow-sm); }
    .eco-card:hover { transform: translateY(-5px); border-color: var(--eficia-blue-light); box-shadow: var(--shadow-md); }
    .eco-card.center-card { background: var(--accent-gradient); border: none; grid-column: 2/4; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px; color: #fff; box-shadow: var(--shadow-lg); }
    .eco-icon { font-size: 40px; margin-bottom: 16px; }
    .eco-name { font-family: var(--ff-display); font-weight: 700; font-size: 16px; color: var(--text); margin-bottom: 8px; }
    .eco-card.center-card .eco-name { color: #fff; font-size: 24px; }
    .eco-desc { font-size: 14px; color: var(--text-dim); line-height: 1.5; }
    .eco-card.center-card .eco-desc { color: rgba(255,255,255,0.9); font-size: 16px; }
    .eco-badge { display: inline-block; background: rgba(0, 136, 204, 0.1); color: var(--eficia-blue-dark); font-size: 11px; padding: 4px 12px; border-radius: 100px; margin-top: 16px; text-transform: uppercase; font-weight: 700; }

    /* ── COMPARADOR ────────────────────────────────────────────── */
    .compare-section { background: var(--bg); }
    .compare-grid { display: grid; grid-template-columns: 1.2fr 1fr 1fr; border: 1px solid var(--border); border-radius: 24px; overflow: hidden; margin-top: 48px; box-shadow: var(--shadow-sm); max-width: 1200px; margin: 48px auto 0; }
    .compare-col { display: flex; flex-direction: column; }
    .compare-header { padding: 32px 24px; background: rgba(0,0,0,0.02); border-bottom: 1px solid var(--border); }
    .compare-col.eficia .compare-header { background: var(--eficia-blue-dark); color: #fff; }
    .compare-col-name { font-family: var(--ff-display); font-weight: 800; font-size: 20px; color: var(--text); }
    .compare-col.eficia .compare-col-name { color: #fff; }
    .compare-col-sub { font-size: 14px; color: var(--text-dim); margin-top: 8px; font-weight: 500; }
    .compare-col.eficia .compare-col-sub { color: rgba(255,255,255,0.7); }
    .compare-row { padding: 16px 24px; border-bottom: 1px solid var(--border); font-size: 14px; color: var(--text-dim); display: flex; align-items: center; gap: 12px; min-height: 64px; }
    .compare-col.eficia .compare-row { background: rgba(0, 136, 204, 0.03); color: var(--text); font-weight: 500; }
    .check { color: var(--eficia-teal); font-size: 18px; font-weight: 700; }
    .cross { color: #EF4444; font-size: 18px; font-weight: 700; }
    .compare-feature { padding: 16px 24px; border-bottom: 1px solid var(--border); font-size: 14px; font-weight: 600; color: var(--text); background: #fff; min-height: 64px; display: flex; align-items: center; }

    /* ── RESULTADOS ────────────────────────────────────────────── */
    .resultados { background: var(--eficia-blue-dark); padding: 120px 48px; color: #fff; }
    .resultados .section-label { color: var(--eficia-lime); }
    .resultados-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 48px; max-width: 1200px; margin-left: auto; margin-right: auto; }
    .resultados-header h2 { color: #fff; margin-bottom: 0; }
    .resultados-header p { color: rgba(255,255,255,0.7); font-size: 16px; max-width: 350px; text-align: right; line-height: 1.6; }
    .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1200px; margin: 0 auto; }
    .stat { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 40px 32px; border-radius: 24px; text-align: center; }
    .stat-num { font-family: var(--ff-display); font-size: 48px; font-weight: 800; color: var(--eficia-lime); line-height: 1; margin-bottom: 16px; }
    .stat-desc { font-size: 15px; color: rgba(255,255,255,0.8); line-height: 1.5; }

    /* ── TESTIMONIOS ───────────────────────────────────────────── */
    .testimonios { background: var(--bg); }
    .test-header { text-align: center; margin-bottom: 48px; }
    .test-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1200px; margin: 0 auto; }
    .test-card { background: #fff; border: 1px solid var(--border); border-radius: 24px; padding: 40px 32px; transition: var(--transition); box-shadow: var(--shadow-sm); }
    .test-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); border-color: var(--eficia-blue-light); }
    .test-stars { color: #F59E0B; font-size: 18px; margin-bottom: 20px; letter-spacing: 2px; }
    .test-quote { font-size: 15px; color: var(--text-dim); line-height: 1.7; margin-bottom: 24px; font-style: italic; }
    .test-author { display: flex; align-items: center; gap: 16px; }
    .test-avatar { width: 48px; height: 48px; border-radius: 50%; background: rgba(0, 136, 204, 0.1); display: flex; align-items: center; justify-content: center; font-family: var(--ff-display); font-weight: 700; color: var(--eficia-blue-dark); font-size: 16px; flex-shrink: 0; }
    .test-name { font-family: var(--ff-display); font-weight: 700; color: var(--text); font-size: 15px; }
    .test-role { font-size: 13px; color: var(--text-dim); margin-top: 4px; }
    .test-sector { display: inline-block; font-size: 11px; background: rgba(144, 195, 31, 0.15); color: var(--eficia-teal); padding: 4px 10px; border-radius: 100px; margin-top: 8px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; }

    /* ── CIUDADES ──────────────────────────────────────────────── */
    .mapa-section { background: rgba(0, 71, 171, 0.03); padding: 120px 48px; }
    .mapa-header { text-align: center; margin-bottom: 48px; }
    .ciudades-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto; }
    .ciudad-card { background: #fff; border: 1px solid var(--border); border-radius: 20px; padding: 24px; text-align: center; box-shadow: var(--shadow-sm); }
    .ciudad-name { font-family: var(--ff-display); font-weight: 800; font-size: 18px; color: var(--text); margin-bottom: 8px; }
    .ciudad-count { font-size: 13px; color: var(--text-dim); margin-bottom: 16px; font-weight: 500; }
    .ciudad-bar-bg { height: 6px; background: rgba(0,0,0,0.05); border-radius: 99px; overflow: hidden; }
    .ciudad-bar-fill { height: 100%; background: var(--accent-gradient); border-radius: 99px; }

    /* ── PRICING ───────────────────────────────────────────────── */
    .pricing-section { background: var(--bg); }
    .pricing-header { text-align: center; margin-bottom: 48px; }
    .pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; max-width: 1200px; margin: 0 auto; }
    .price-card { background: #fff; border: 1px solid var(--border); border-radius: 24px; padding: 40px; display: flex; flex-direction: column; box-shadow: var(--shadow-sm); }
    .price-card.featured { background: var(--eficia-blue-dark); color: #fff; border-color: transparent; position: relative; transform: scale(1.05); box-shadow: var(--shadow-lg); }
    .price-badge { position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: var(--eficia-lime); color: var(--eficia-blue-dark); font-size: 12px; font-weight: 800; padding: 6px 20px; border-radius: 100px; white-space: nowrap; font-family: var(--ff-display); text-transform: uppercase; letter-spacing: 0.05em; }
    .price-plan { font-family: var(--ff-display); font-weight: 800; font-size: 20px; color: var(--text); margin-bottom: 8px; }
    .price-card.featured .price-plan { color: #fff; }
    .price-amount { font-family: var(--ff-display); font-size: 48px; font-weight: 800; color: var(--eficia-blue-dark); line-height: 1; margin: 16px 0 8px; }
    .price-card.featured .price-amount { color: var(--eficia-lime); }
    .price-period { font-size: 14px; color: var(--text-dim); margin-bottom: 32px; font-weight: 500; }
    .price-card.featured .price-period { color: rgba(255,255,255,0.7); }
    .price-features { list-style: none; flex: 1; display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px; }
    .price-features li { font-size: 15px; color: var(--text-dim); display: flex; align-items: flex-start; gap: 12px; }
    .price-card.featured .price-features li { color: rgba(255,255,255,0.9); }
    .price-features li::before { content: '✓'; color: var(--eficia-teal); font-weight: 700; flex-shrink: 0; font-size: 16px; }
    .price-card.featured .price-features li::before { color: var(--eficia-lime); }
    .price-cta { background: rgba(0, 136, 204, 0.1); color: var(--eficia-blue-dark); border: none; padding: 16px; border-radius: 12px; font-weight: 600; font-size: 15px; cursor: pointer; font-family: var(--ff-body); text-align: center; transition: var(--transition); }
    .price-cta:hover { background: rgba(0, 136, 204, 0.2); }
    .price-card.featured .price-cta { background: var(--eficia-lime); color: var(--eficia-blue-dark); }
    .price-card.featured .price-cta:hover { background: #a2db23; transform: translateY(-2px); }

    /* ── FAQ ───────────────────────────────────────────────────── */
    .faq-section { background: rgba(0, 71, 171, 0.02); }
    .faq-inner { display: grid; grid-template-columns: 1fr 2fr; gap: 64px; max-width: 1200px; margin: 0 auto; }
    .faq-left h2 { margin-bottom: 16px; }
    .faq-list { display: flex; flex-direction: column; gap: 0; }
    .faq-item { border-bottom: 1px solid var(--border); overflow: hidden; }
    .faq-q { padding: 24px 0; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: var(--ff-display); font-weight: 700; font-size: 16px; color: var(--text); transition: var(--transition); }
    .faq-q:hover { color: var(--eficia-blue-dark); }
    .faq-toggle { width: 32px; height: 32px; border-radius: 50%; background: rgba(0, 136, 204, 0.1); display: flex; align-items: center; justify-content: center; font-size: 18px; color: var(--eficia-blue-dark); flex-shrink: 0; transition: var(--transition); font-weight: 400; }
    .faq-item.open .faq-toggle { background: var(--eficia-blue-dark); color: #fff; transform: rotate(45deg); }
    .faq-a { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; font-size: 15px; color: var(--text-dim); line-height: 1.7; }
    .faq-item.open .faq-a { max-height: 250px; padding-bottom: 24px; }

    /* ── COMO FUNCIONA (Alternative to Proceso) ───────────────── */
    .como-section { background: var(--bg); }
    .como-inner { display: grid; grid-template-columns: 1fr 2fr; gap: 64px; align-items: start; max-width: 1200px; margin: 0 auto; }
    .steps { display: flex; flex-direction: column; gap: 0; position: relative; }
    .step { display: flex; gap: 24px; padding-bottom: 48px; position: relative; }
    .step:last-child { padding-bottom: 0; }
    .step-line { position: absolute; left: 24px; top: 48px; width: 2px; bottom: 0; background: var(--border); }
    .step:last-child .step-line { display: none; }
    .step-num { width: 48px; height: 48px; background: rgba(0, 136, 204, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: var(--ff-display); font-weight: 800; font-size: 16px; color: var(--eficia-blue-dark); flex-shrink: 0; position: relative; z-index: 1; border: 2px solid #fff; }
    .step-content h3 { font-family: var(--ff-display); font-weight: 700; font-size: 20px; margin-bottom: 12px; color: var(--text); }
    .step-content p { font-size: 15px; color: var(--text-dim); line-height: 1.6; }

    /* ── CTA FINAL ─────────────────────────────────────────────── */
    .cta-final { background: var(--accent-gradient); text-align: center; padding: 100px 48px; position: relative; overflow: hidden; }
    .cta-final::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCI+CjxyZWN0IHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgZmlsbD0ibm9uZSI+PC9yZWN0Pgo8Y2lyY2xlIGN4PSIyIiBjeT0iMiIgcj0iMiIgZmlsbD0icmdiYSgyNTUsMjU1LDI1NSwwLjEpIj48L2NpcmNsZT4KPC9zdmc+') repeat; opacity: 0.5; }
    .cta-final-inner { position: relative; z-index: 2; max-width: 800px; margin: 0 auto; }
    .cta-final h2 { color: #fff; font-size: clamp(32px, 4vw, 48px); margin-bottom: 24px; font-family: var(--ff-display); font-weight: 800; letter-spacing: -0.02em; }
    .cta-final p { color: rgba(255,255,255,0.9); font-size: 18px; margin-bottom: 40px; font-weight: 500; }
    .btn-cta-final { background: var(--eficia-lime); color: var(--eficia-blue-dark); padding: 20px 40px; border-radius: 99px; font-weight: 700; font-size: 18px; border: none; cursor: pointer; font-family: var(--ff-display); transition: var(--transition); box-shadow: 0 10px 25px rgba(144, 195, 31, 0.3); }
    .btn-cta-final:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(144, 195, 31, 0.4); background: #a2db23; }
    .cta-secondary { display: inline-block; margin-top: 24px; color: rgba(255,255,255,0.7); font-size: 14px; font-weight: 500; }
"""

# Extract the body of the new landing page
ticker = re.search(r'<div class="ticker">.*?</div>', new_html, re.DOTALL).group(0)
logos = re.search(r'<div class="logos-bar">.*?</div>', new_html, re.DOTALL).group(0)
metrics = re.search(r'<div class="hero-visual">.*?</div>\s*</section>', new_html, re.DOTALL).group(0)
metrics = metrics.replace('hero-visual', 'metrics-grid').replace('</section>', '')
metrics_section = f'<section class="metrics-section">{metrics}</section>'

sectores = re.search(r'<section class="sectores">.*?</section>', new_html, re.DOTALL).group(0)
demo_chat = re.search(r'<section class="demo-chat-section">.*?</section>', new_html, re.DOTALL).group(0)
roi = re.search(r'<section class="roi-section">.*?</section>', new_html, re.DOTALL).group(0)
ecosistema = re.search(r'<section class="ecosistema">.*?</section>', new_html, re.DOTALL).group(0)
comparador = re.search(r'<section class="compare-section">.*?</section>', new_html, re.DOTALL).group(0)
como = re.search(r'<section class="como">.*?</section>', new_html, re.DOTALL).group(0).replace('class="como"', 'class="como-section"')
resultados = re.search(r'<section class="resultados">.*?</section>', new_html, re.DOTALL).group(0)
testimonios = re.search(r'<section class="testimonios">.*?</section>', new_html, re.DOTALL).group(0)
ciudades = re.search(r'<section class="mapa-section">.*?</section>', new_html, re.DOTALL).group(0)
pricing = re.search(r'<section class="pricing-section">.*?</section>', new_html, re.DOTALL).group(0)
faq = re.search(r'<section class="faq-section">.*?</section>', new_html, re.DOTALL).group(0)
cta_final = re.search(r'<section class="cta-final">.*?</section>', new_html, re.DOTALL).group(0)

# Wrap CTA final inner content
cta_final = cta_final.replace('<section class="cta-final">', '<section class="cta-final"><div class="cta-final-inner">').replace('</section>', '</div></section>')

# Change generic html tags from new page to match branding classes where applicable
# Not fully modifying inner HTML as it relies on CSS mapping
new_scripts = re.search(r'<script>.*?</script>', new_html, re.DOTALL).group(0)

# Merge styles
style_insert_idx = old_html.rfind('</style>')
old_html = old_html[:style_insert_idx] + new_css + old_html[style_insert_idx:]

# Insert Ticker after body
body_idx = old_html.find('<div class="mesh-bg">')
old_html = old_html[:body_idx] + ticker + "\n" + old_html[body_idx:]

# Insert Logos after Hero
hero_end_idx = old_html.find('</section>', old_html.find('<section class="hero"')) + 10
old_html = old_html[:hero_end_idx] + "\n" + metrics_section + "\n" + logos + "\n" + old_html[hero_end_idx:]

# Insert rest after proceso
proceso_end_idx = old_html.find('</section>', old_html.find('<section id="proceso"')) + 10

blocks = [
    sectores, demo_chat, roi, ecosistema, comparador, como,
    resultados, testimonios, ciudades, pricing, faq
]

old_html = old_html[:proceso_end_idx] + "\n" + "\n".join(blocks) + "\n" + old_html[proceso_end_idx:]

# Insert CTA final before footer
footer_idx = old_html.find('<footer')
old_html = old_html[:footer_idx] + cta_final + "\n" + old_html[footer_idx:]

# Merge scripts
script_end_idx = old_html.rfind('</script>')
old_html = old_html[:script_end_idx] + new_scripts.replace('<script>', '').replace('</script>', '') + old_html[script_end_idx:]

with open('Eficia - Official Branding.html', 'w', encoding='utf-8') as f:
    f.write(old_html)
