/* Hero slideshow — crossfade automático (3.8s) con puntos clickeables. */
(function () {
  var root = document.querySelector('[data-slideshow]');
  if (!root) return;
  var slides = Array.prototype.slice.call(root.querySelectorAll('.hero-slides img'));
  var dots = Array.prototype.slice.call(root.querySelectorAll('.hero-dots button'));
  if (!slides.length) return;

  var INTERVAL = 3800;
  var i = 0;
  var timer;

  function render() {
    slides.forEach(function (el, n) { el.classList.toggle('is-active', n === i); });
    dots.forEach(function (el, n) { el.classList.toggle('is-active', n === i); });
  }
  function advance() { i = (i + 1) % slides.length; render(); }
  function start() { timer = setInterval(advance, INTERVAL); }

  dots.forEach(function (dot, n) {
    dot.addEventListener('click', function () {
      i = n; render();
      clearInterval(timer); start();
    });
  });

  render();
  start();
})();
