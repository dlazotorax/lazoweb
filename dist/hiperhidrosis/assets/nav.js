/* Navegación: dropdown "Tratamientos" (hover + click/tap) y menú hamburguesa móvil.
   Patrón disclosure accesible: aria-expanded en los botones, Escape cierra,
   click fuera cierra. */
(function () {
  // Dropdown de escritorio
  document.querySelectorAll('.nav-drop').forEach(function (drop) {
    var btn = drop.querySelector('.nav-drop__btn');
    if (!btn) return;
    function close() { drop.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    btn.addEventListener('click', function () {
      var open = drop.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', function (e) { if (!drop.contains(e.target)) close(); });
    drop.addEventListener('focusout', function (e) { if (!drop.contains(e.relatedTarget)) close(); });
    drop.addEventListener('keydown', function (e) { if (e.key === 'Escape') { close(); btn.focus(); } });
  });

  // Hamburguesa móvil
  var burger = document.querySelector('.nav-burger');
  var panel = document.getElementById('mobile-nav');
  if (burger && panel) {
    burger.addEventListener('click', function () {
      var willOpen = panel.hasAttribute('hidden');
      if (willOpen) panel.removeAttribute('hidden'); else panel.setAttribute('hidden', '');
      burger.setAttribute('aria-expanded', String(willOpen));
      burger.classList.toggle('open', willOpen);
    });
  }

  // Submenú Tratamientos dentro del panel móvil
  document.querySelectorAll('.mnav-drop__btn').forEach(function (btn) {
    var menu = document.getElementById(btn.getAttribute('aria-controls'));
    if (!menu) return;
    btn.addEventListener('click', function () {
      var willOpen = menu.hasAttribute('hidden');
      if (willOpen) menu.removeAttribute('hidden'); else menu.setAttribute('hidden', '');
      btn.setAttribute('aria-expanded', String(willOpen));
      btn.classList.toggle('open', willOpen);
    });
  });
})();
