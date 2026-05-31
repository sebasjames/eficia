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
      { title: "Soporte Técnico", desc: "Reporte de incidencia.", q: "El equipo no enciende y muestra luz roja.", rep: ["Analizando manual de servicio técnico...", "Ese código indica fallo de alimentación. Por favor verifica que el cable esté conectado a un tomacorriente directo. Si persiste, generaré un ticket de soporte."] },
      { title: "Cotización de Obra", desc: "Presupuesto de materiales.", q: "Necesito cotizar 50 bultos de cemento y 20 varillas de 1/2.", rep: ["Calculando con precios actualizados...", "El total es $1.850.000 COP con entrega mañana en la mañana. ¿Te genero la orden de compra?"] },
      { title: "Agendamiento Médico", desc: "Reserva de citas.", q: "Quiero una cita con dermatología lo más pronto posible.", rep: ["Revisando agenda de especialistas...", "Tengo disponibilidad el próximo martes a las 10:30 am con el Dr. Pérez. ¿Confirmo tu cita?"] },
      { title: "Rastreo de Envío", desc: "Estado de entrega.", q: "¿Dónde viene mi pedido número #9942?", rep: ["Conectando con el sistema logístico...", "Tu pedido está en ruta de reparto y se entregará hoy entre las 2:00 pm y las 4:00 pm."] }
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
      const empEl = document.getElementById('emp');
      const salEl = document.getElementById('sal');
      const repEl = document.getElementById('rep');
      const emp = +empEl.value;
      const sal = +salEl.value;
      const rep = +repEl.value;
      
      // Update custom properties for slider backgrounds
      [empEl, salEl, repEl].forEach(el => {
        const percent = ((el.value - el.min) / (el.max - el.min)) * 100;
        el.style.setProperty('--val', percent + '%');
      });

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

    // Interactive Mesh Background & Interactivity
    document.addEventListener('DOMContentLoaded', () => {
      const blob1 = document.querySelector('.blob-1');
      if (blob1 && window.matchMedia("(hover: hover)").matches) {
        window.addEventListener('mousemove', (e) => {
          blob1.style.setProperty('--mouse-x', `${e.clientX}px`);
          blob1.style.setProperty('--mouse-y', `${e.clientY}px`);
        });
      }

      // Flashlight Toggle
      const flashlightBtn = document.getElementById('flashlightToggle');
      if (flashlightBtn) {
        flashlightBtn.addEventListener('click', () => {
          const isOn = document.documentElement.getAttribute('data-flashlight') === 'on';
          if (isOn) {
            document.documentElement.removeAttribute('data-flashlight');
            flashlightBtn.style.color = '';
            flashlightBtn.style.borderColor = 'var(--border)';
          } else {
            document.documentElement.setAttribute('data-flashlight', 'on');
            flashlightBtn.style.color = 'var(--eficia-lime)';
            flashlightBtn.style.borderColor = 'var(--eficia-lime)';
          }
        });
      }

      // Theme Switcher
      const themeBtn = document.getElementById('themeToggle');
      const sunIcon = document.querySelector('.sun-icon');
      const moonIcon = document.querySelector('.moon-icon');
      const savedTheme = localStorage.getItem('eficia-theme');
      
      if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        sunIcon.style.display = 'block';
        moonIcon.style.display = 'none';
      }
      
      themeBtn.addEventListener('click', () => {
        const isLight = document.documentElement.getAttribute('data-theme') === 'light';
        if (isLight) {
          document.documentElement.removeAttribute('data-theme');
          localStorage.setItem('eficia-theme', 'dark');
          sunIcon.style.display = 'none';
          moonIcon.style.display = 'block';
        } else {
          document.documentElement.setAttribute('data-theme', 'light');
          localStorage.setItem('eficia-theme', 'light');
          sunIcon.style.display = 'block';
          moonIcon.style.display = 'none';
        }
      });
    });

// Expose functions to global window for inline HTML handlers
window.selectSector = selectSector;
window.runScenario = runScenario;
window.sendChat = sendChat;
window.calcROI = calcROI;
window.toggleFaq = toggleFaq;

// Modal Logic
window.openContactModal = function() {
  document.getElementById('contactModal').classList.add('active');
  document.getElementById('modalFormContainer').style.display = 'block';
  document.getElementById('modalSuccessMsg').style.display = 'none';
  document.getElementById('contactForm').reset();
};

window.closeContactModal = function() {
  document.getElementById('contactModal').classList.remove('active');
};

window.submitContactForm = function(e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  formData.append('form-name', form.getAttribute('name'));

  fetch('/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(formData).toString()
  })
  .then(() => {
    document.getElementById('modalFormContainer').style.display = 'none';
    document.getElementById('modalSuccessMsg').style.display = 'block';
  })
  .catch(error => {
    console.error('Form submission error:', error);
    alert('Hubo un error al enviar el formulario. Por favor intenta de nuevo.');
  });
};

// Counters Animation
const counterObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseFloat(el.getAttribute('data-target'));
      const suffix = el.getAttribute('data-suffix') || '';
      const prefix = el.getAttribute('data-prefix') || '';
      const decimals = parseInt(el.getAttribute('data-decimals')) || 0;
      const duration = 2000;
      let start = null;
      
      const step = (timestamp) => {
        if (!start) start = timestamp;
        const progress = Math.min((timestamp - start) / duration, 1);
        // Easing out cubic
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        const current = easeProgress * target;
        
        el.textContent = prefix + current.toFixed(decimals) + suffix;
        
        if (progress < 1) {
          window.requestAnimationFrame(step);
        } else {
          el.textContent = prefix + target.toFixed(decimals) + suffix;
        }
      };
      
      window.requestAnimationFrame(step);
      observer.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.counter').forEach(c => counterObserver.observe(c));
