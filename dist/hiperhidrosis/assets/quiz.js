/* Test de nivel de severidad — mismo puntaje que el sitio original:
   No = 0 · Rara Vez = 1 · A Veces = 2 · A Diario = 3  (10 preguntas, 0–30)
   1–9 LEVE · 10–19 MODERADA · 20–30 SEVERA

   El resultado actúa como filtro de derivación: leve y moderada se orientan
   al dermatólogo (link informativo, sin agenda); solo severa —candidata
   quirúrgica— recibe CTA de agenda con el Dr. Lazo. */
(function () {
  var form = document.getElementById('form-test');
  if (!form) return;

  var VALUES = { 'No': 0, 'Rara Vez': 1, 'A Veces': 2, 'A Diario': 3 };
  var AGENDA_CLC = 'https://reserva.clinicalascondes.cl/AgendaWeb/reserva-horas?nombre=DAVID%20RENE&apellidoPat=LAZO&apellidoMat=PEREZ';

  var LEVELS = [
    {
      min: 1, max: 9, name: 'LEVE',
      text: 'Tu sudoración corresponde a una hiperhidrosis leve. En este nivel el tratamiento lo maneja el dermatólogo, con antitranspirantes médicos en base a cloruro de aluminio, con excelentes resultados. La cirugía no está indicada en este grado.',
      primary: { label: 'Ver tratamiento para hiperhidrosis leve', href: '/hiperhidrosis-localizada-leve' }
    },
    {
      min: 10, max: 19, name: 'MODERADA',
      text: 'Tu sudoración corresponde a una hiperhidrosis moderada. En este nivel el manejo también recae en el dermatólogo, con alternativas como iontoforesis, medicamentos orales o toxina botulínica (Botox). La cirugía se reserva para casos que no responden a estas terapias.',
      primary: { label: 'Ver tratamientos para hiperhidrosis moderada', href: '/hiperhidrosis-localizada-moderada' }
    },
    {
      min: 20, max: 30, name: 'SEVERA',
      text: 'Tu sudoración corresponde a una hiperhidrosis severa. La cirugía (simpatectomía por videotoracoscopía) es el tratamiento con mejores resultados en este grado. Si buscas una solución definitiva, agenda una evaluación con el Dr. David Lazo, cirujano torácico.',
      primary: { label: 'Agendar evaluación quirúrgica', href: AGENDA_CLC, external: true },
      secondary: { label: 'Conocer la cirugía', href: '/cirugia-hiperhidrosis' }
    }
  ];

  var result = document.getElementById('quiz-result');
  var resultLevel = document.getElementById('quiz-result-level');
  var resultText = document.getElementById('quiz-result-text');
  var primary = document.getElementById('quiz-result-primary');
  var secondary = document.getElementById('quiz-result-secondary');
  var error = document.getElementById('quiz-error');

  function setButton(btn, cfg) {
    if (!cfg) { btn.setAttribute('hidden', ''); return; }
    btn.removeAttribute('hidden');
    btn.innerHTML = '';
    btn.appendChild(document.createTextNode(cfg.label));
    var arrow = document.createElement('span');
    arrow.className = 'arrow';
    arrow.textContent = '→';
    btn.appendChild(arrow);
    btn.href = cfg.href;
    if (cfg.external) {
      btn.target = '_blank';
      btn.rel = 'noopener';
    } else {
      btn.removeAttribute('target');
      btn.removeAttribute('rel');
    }
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var score = 0;
    var answered = 0;
    for (var q = 1; q <= 10; q++) {
      var checked = form.querySelector('input[name="q' + q + '"]:checked');
      if (checked) { answered++; score += VALUES[checked.value] || 0; }
    }
    if (answered < 10) {
      error.style.display = 'block';
      return;
    }
    error.style.display = 'none';

    if (score === 0) {
      resultLevel.textContent = 'Sin indicios de hiperhidrosis significativa';
      resultText.textContent = 'Tus respuestas no muestran un impacto relevante de la sudoración en tu vida diaria. Si igualmente tienes dudas, puedes agendar una consulta.';
      setButton(primary, null);
      setButton(secondary, null);
    } else {
      var level;
      for (var i = 0; i < LEVELS.length; i++) {
        if (score >= LEVELS[i].min && score <= LEVELS[i].max) { level = LEVELS[i]; break; }
      }
      resultLevel.textContent = 'Resultado: Hiperhidrosis ' + level.name;
      resultText.textContent = level.text;
      setButton(primary, level.primary);
      setButton(secondary, level.secondary);
    }

    form.style.display = 'none';
    result.style.display = 'block';
    result.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  document.getElementById('quiz-retry').addEventListener('click', function () {
    form.reset();
    form.style.display = '';
    result.style.display = 'none';
    form.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
})();
