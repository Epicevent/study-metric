document.addEventListener("DOMContentLoaded", function () {
  // HTML parses a raw '<' followed by a letter inside TeX as a bogus tag
  // before KaTeX sees it. Recover the swallowed TeX fragment first.
  // ASSERTION: only malformed elements ending in '<' with the synthetic
  // closing-</p> attribute are rewritten; ordinary HTML is untouched.
  for (const el of Array.from(document.querySelectorAll("*"))) {
    const name = el.localName;
    if (
      !name.includes("<") ||
      !name.endsWith("<") ||
      !el.hasAttribute("p") ||
      !el.parentElement
    ) {
      continue;
    }

    const recovered = "<" + name.slice(0, -1);
    el.parentElement.insertBefore(document.createTextNode(recovered), el);
    el.remove();
  }

  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false }
    ],
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "svg"]
  });
});