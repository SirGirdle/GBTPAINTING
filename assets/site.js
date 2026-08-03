/* GBT Painting & Decorating — site interactions */
(function () {
  'use strict';

  /* Mobile nav drawer ---------------------------------------------------- */
  var drawer = document.getElementById('navMobile');
  var openBtn = document.getElementById('navToggle');
  var closeBtn = document.getElementById('navClose');
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
    if (openBtn) openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (openBtn) openBtn.addEventListener('click', function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setDrawer(false); });
  if (drawer) {
    drawer.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setDrawer(false);
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { setDrawer(false); closeLightbox(); }
  });

  /* FAQ accordion -------------------------------------------------------- */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var answer = item.querySelector('.faq-a');
      var isOpen = item.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      answer.style.maxHeight = isOpen ? answer.scrollHeight + 'px' : null;
    });
  });

  /* Lightbox ------------------------------------------------------------- */
  var lb = document.getElementById('lightbox');
  var lbImg = lb ? lb.querySelector('img') : null;
  function openLightbox(src, alt) {
    if (!lb) return;
    lbImg.src = src; lbImg.alt = alt || '';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeLightbox() {
    if (!lb) return;
    lb.classList.remove('open');
    document.body.style.overflow = '';
  }
  document.querySelectorAll('.ba-slot').forEach(function (slot) {
    slot.addEventListener('click', function () {
      var img = slot.querySelector('img');
      if (img) openLightbox(img.src, img.alt);
    });
  });
  if (lb) {
    lb.addEventListener('click', function (e) {
      if (e.target === lb || e.target.closest('.lightbox-close')) closeLightbox();
    });
  }

  /* Sticky header shadow on scroll -------------------------------------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.style.boxShadow = window.scrollY > 8
        ? '0 6px 22px rgba(16,39,65,.12)' : '';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Quote form: reflect multi-select services into a hidden field -------- */
  document.querySelectorAll('.qc-form').forEach(function (form) {
    form.addEventListener('submit', function () {
      var picked = Array.prototype.map.call(
        form.querySelectorAll('.qc-services input:checked'),
        function (i) { return i.value; }
      );
      var hidden = form.querySelector('input[name="Services requested"]');
      if (hidden) hidden.value = picked.join(', ') || 'Not specified';
    });
  });

  /* Lightweight click tracking (console only in demo) -------------------- */
  document.querySelectorAll('[data-track]').forEach(function (el) {
    el.addEventListener('click', function () {
      try { console.log('[track]', el.getAttribute('data-track')); } catch (e) {}
    });
  });

  /* Footer year ---------------------------------------------------------- */
  var yr = document.getElementById('footYear');
  if (yr) yr.textContent = new Date().getFullYear();
})();
