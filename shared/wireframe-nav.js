/* Mein Pragati Wireframes — Inter-wireframe navigation helper
   Every wireframe includes this. When a user clicks an element with
   data-link-to="<screen-id>", the click is intercepted and forwarded
   to the parent navigator via postMessage. The navigator then switches
   the displayed wireframe.

   Also makes any [data-link-to] element show a pointer cursor + subtle
   hover state, and tags external links to open in a new tab. */

(function () {
  'use strict';

  function findLink(target) {
    return target.closest && target.closest('[data-link-to]');
  }

  function navigate(screenId) {
    if (!screenId) return;
    if (window.parent !== window) {
      window.parent.postMessage({ type: 'navigate', screenId: screenId }, '*');
    } else {
      // Standalone (opened directly) — just log; nothing to navigate.
      console.log('[wireframe-nav] Standalone mode — would navigate to', screenId);
    }
  }

  document.addEventListener('click', function (e) {
    var link = findLink(e.target);
    if (!link) return;
    e.preventDefault();
    e.stopPropagation();
    navigate(link.dataset.linkTo);
  });

  // Visual cue for linkable elements
  var styleEl = document.createElement('style');
  styleEl.textContent =
    '[data-link-to]{cursor:pointer;transition:transform 80ms ease, filter 120ms ease;}' +
    '[data-link-to]:hover{filter:brightness(0.97);}' +
    '[data-link-to]:active{transform:scale(0.995);}';
  document.head.appendChild(styleEl);

  // Announce ready to parent (for any "in-flight" indicators)
  if (window.parent !== window) {
    try {
      window.parent.postMessage({ type: 'wireframe-ready', screen: document.title }, '*');
    } catch (e) { /* noop */ }
  }
})();
