(() => {
  "use strict";

  const options = {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
      { left: "$", right: "$", display: false },
    ],
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "svg"],
    ignoredClasses: ["katex", "katex-display"],
  };

  function render(root) {
    if (!root || typeof renderMathInElement !== "function") return;
    renderMathInElement(root, options);
  }

  document.addEventListener("DOMContentLoaded", () => {
    render(document.body);

    const root = document.querySelector("[data-markdown-source]");
    if (!root) return;

    const finish = () => {
      if (root.classList.contains("loading") || !root.firstElementChild) return false;
      render(root);
      render(document.getElementById("note-toc"));
      return true;
    };

    if (finish()) return;

    const observer = new MutationObserver(() => {
      if (finish()) observer.disconnect();
    });

    observer.observe(root, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ["class"],
    });
  });
})();
