/* ============================================================
   VATS — Cambio de Paradigma · interacción
   ============================================================ */
(function(){
  "use strict";

  /* ---------- scroll-driven reveal + counters (robust; no IntersectionObserver) ---------- */
  var reveals = [].slice.call(document.querySelectorAll('.r'));
  var counters = [].slice.call(document.querySelectorAll('[data-count]'));

  function vh(){ return window.innerHeight || document.documentElement.clientHeight || 600; }
  function topOf(el){ return el.getBoundingClientRect().top; }

  function runCounter(el){
    if(el.__done) return; el.__done = true;
    var target = parseFloat(el.getAttribute('data-count'));
    var dec = (el.getAttribute('data-dec')|0), dur = 1100, t0 = null;
    var prefix = el.getAttribute('data-pre')||'', suffix = el.getAttribute('data-suf')||'';
    function step(ts){
      if(!t0) t0 = ts; var p = Math.min((ts-t0)/dur,1);
      var v = (target*(1-Math.pow(1-p,3))).toFixed(dec);
      el.textContent = prefix + v + suffix;
      if(p<1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function check(){
    var h = vh();
    for(var i=reveals.length-1;i>=0;i--){
      if(topOf(reveals[i]) < h*0.92){ reveals[i].classList.add('in'); reveals.splice(i,1); }
    }
    for(var j=counters.length-1;j>=0;j--){
      if(topOf(counters[j]) < h*0.82){ runCounter(counters[j]); counters.splice(j,1); }
    }
  }

  check();
  document.addEventListener('scroll', check, {passive:true});
  window.addEventListener('resize', check);
  window.addEventListener('load', check);
  // belt-and-suspenders: ensure first paint reveals above-the-fold even if events are quiet
  setTimeout(check, 60); setTimeout(check, 400);
  // failsafe: if CSS transitions are paused (e.g. offscreen render) and content is stuck invisible,
  // force everything visible without animation so the page is never blank.
  setTimeout(function(){
    var t = document.querySelector('.r.in');
    if(t && parseFloat(getComputedStyle(t).opacity) < 0.6){
      document.documentElement.classList.add('reveal-now');
      reveals.forEach(function(el){ el.classList.add('in'); }); reveals.length = 0;
    }
  }, 1500);

  /* ---------- progress bar ---------- */
  var bar = document.querySelector('.progress');
  function onScroll(){
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var p = max>0 ? (h.scrollTop||document.body.scrollTop)/max : 0;
    if(bar) bar.style.width = (p*100).toFixed(2)+'%';
  }
  document.addEventListener('scroll', onScroll, {passive:true});
  onScroll();

})();
