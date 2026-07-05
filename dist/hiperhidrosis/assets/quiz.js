/* Test de nivel de severidad — mismo puntaje que el sitio original:
   No = 0 · Rara Vez = 1 · A Veces = 2 · A Diario = 3  (10 preguntas, 0–30)
   1–9 LEVE · 10–19 MODERADA · 20–30 SEVERA */
(function () {
  var form = document.getElementById('form-test');
  if (!form) return;

  var VALUES = { 'No': 0, 'Rara Vez': 1, 'A Veces': 2, 'A Diario': 3 };
  var LEVELS = [
    { min: 1, max: 9, name: 'LEVE', url: '/hiperhidrosis-localizada-leve',
      text: 'Tu sudoración corresponde a una hiperhidrosis leve. La primera línea de tratamiento son los antitranspirantes médicos en base a cloruro de aluminio, indicados por un dermatólogo.' },
    { min: 10, max: 19, name: 'MODERADA', url: '/hiperhidrosis-localizada-moderada',
      text: 'Tu sudoración corresponde a una hiperhidrosis moderada. Alternativas como la iontoforesis, los medicamentos orales y la toxina botulínica (Botox) pueden ayudarte, siempre indicadas por un especialista.' },
    { min: 20, max: 30, name: 'SEVERA', url: '/cirugia-hiperhidrosis',
      text: 'Tu sudoración corresponde a una hiperhidrosis severa. La cirugía (simpatectomía por videotoracoscopía) es el tratamiento con mejores resultados; agenda una evaluación con el Dr. David Lazo.' }
  ];

  var result = document.getElementById('quiz-result');
  var resultLevel = document.getElementById('quiz-result-level');
  var resultText = document.getElementById('quiz-result-text');
  var resultLink = document.getElementById('quiz-result-link');
  var error = document.getElementById('quiz-error');

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
      resultLink.style.display = 'none';
    } else {
      var level;
      for (var i = 0; i < LEVELS.length; i++) {
        if (score >= LEVELS[i].min && score <= LEVELS[i].max) { level = LEVELS[i]; break; }
      }
      resultLevel.textContent = 'Resultado: Hiperhidrosis ' + level.name;
      resultText.textContent = level.text;
      resultLink.href = level.url;
      resultLink.style.display = '';
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
