(() => {
  "use strict";

  const escapeHtml = (value) => String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");

  function slugify(text, used) {
    const base = text
      .replace(/\$[^$]+\$/g, "")
      .replace(/<[^>]+>/g, "")
      .replace(/[^\p{L}\p{N}]+/gu, "-")
      .replace(/^-+|-+$/g, "")
      .toLowerCase() || "section";
    let slug = base;
    let suffix = 2;
    while (used.has(slug)) slug = `${base}-${suffix++}`;
    used.add(slug);
    return slug;
  }

  function inlineMarkdown(source) {
    const tokens = [];
    const stash = (html) => {
      const key = `\u0000T${tokens.length}\u0000`;
      tokens.push(html);
      return key;
    };

    let text = String(source);

    text = text.replace(/`([^`]+)`/g, (_, code) =>
      stash(`<code>${escapeHtml(code)}</code>`)
    );

    text = text.replace(/\$([^$\n]+)\$/g, (_, math) =>
      stash(`$${escapeHtml(math)}$`)
    );

    text = escapeHtml(text);

    text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+|[^\s)]+)\)/g,
      '<a href="$2">$1</a>');
    text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    text = text.replace(/__([^_]+)__/g, "<strong>$1</strong>");
    text = text.replace(/(?<!\*)\*([^*\n]+)\*(?!\*)/g, "<em>$1</em>");

    text = text.replace(/\u0000T(\d+)\u0000/g, (_, index) => tokens[Number(index)]);
    return text;
  }

  function splitTableRow(line) {
    let value = line.trim();
    if (value.startsWith("|")) value = value.slice(1);
    if (value.endsWith("|")) value = value.slice(0, -1);
    return value.split("|").map((cell) => cell.trim());
  }

  function isTableDivider(line) {
    const cells = splitTableRow(line);
    return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
  }

  function listMatch(line) {
    return line.match(/^(\s*)([-+*]|\d+\.)\s+(.*)$/);
  }

  function isHeading(line) {
    return /^\s*#{1,6}\s+/.test(line);
  }

  function isBlockStart(lines, index) {
    const line = lines[index] ?? "";
    const trimmed = line.trim();
    if (!trimmed) return true;
    if (trimmed === "$$" || /^\$\$.*\$\$$/.test(trimmed)) return true;
    if (isHeading(line)) return true;
    if (/^(-{3,}|\*{3,}|_{3,})$/.test(trimmed)) return true;
    if (/^>\s?/.test(line)) return true;
    if (listMatch(line)) return true;
    if (trimmed === "<details>" || trimmed.startsWith("<details ")) return true;
    if (/^<\/?(div|section|aside|figure|table|blockquote|details|summary)\b/i.test(trimmed)) return true;
    if (line.includes("|") && index + 1 < lines.length && isTableDivider(lines[index + 1])) return true;
    return false;
  }

  function normalizeKnownSource(source, markdown) {
    let text = String(markdown).replace(/\r\n?/g, "\n");

    // A previous generated revision accidentally joined a display delimiter to
    // a variable named u, producing the TeX command \nu. Repair only those
    // display starts; the legitimate Veronese symbol \nu_2 is left untouched.
    if (source === "사전은_관찰이_아니다_함수에서_공간으로.md") {
      text = text.replace(/\$\$\\nu(?==|\\longmapsto|_\{)/g, "$$\n" + "u");
    }

    const standaloneDisplayDelimiters = text
      .split("\n")
      .filter((line) => line.trim() === "$$")
      .length;
    if (standaloneDisplayDelimiters % 2 !== 0) {
      throw new Error(`짝이 맞지 않는 $$ 수식 구분자: ${standaloneDisplayDelimiters}개`);
    }
    return text;
  }

  function parseMarkdown(source, options = {}) {
    const lines = String(source).replace(/\r\n?/g, "\n").split("\n");
    const html = [];
    const usedSlugs = options.usedSlugs || new Set();
    let i = 0;
    let skippedHeadings = 0;
    const skipHeadings = options.skipHeadings || 0;
    const headingOffset = options.headingOffset ?? 1;

    while (i < lines.length) {
      const raw = lines[i];
      const trimmed = raw.trim();

      if (!trimmed) {
        i += 1;
        continue;
      }

      if (trimmed === "$$") {
        const block = [];
        i += 1;
        while (i < lines.length && lines[i].trim() !== "$$") {
          block.push(lines[i]);
          i += 1;
        }
        if (i < lines.length) i += 1;
        html.push(`<div class="mathblock">$$\n${escapeHtml(block.join("\n"))}\n$$</div>`);
        continue;
      }

      if (/^\$\$.*\$\$$/.test(trimmed) && trimmed.length > 4) {
        html.push(`<div class="mathblock">${escapeHtml(trimmed)}</div>`);
        i += 1;
        continue;
      }

      const heading = raw.match(/^\s*(#{1,6})\s+(.+)$/);
      if (heading) {
        if (skippedHeadings < skipHeadings) {
          skippedHeadings += 1;
          i += 1;
          continue;
        }
        const sourceLevel = heading[1].length;
        const level = Math.min(6, sourceLevel + headingOffset);
        const plain = heading[2].replace(/\*\*/g, "").replace(/`/g, "");
        const id = slugify(plain, usedSlugs);
        html.push(`<h${level} id="${id}">${inlineMarkdown(heading[2])}</h${level}>`);
        i += 1;
        continue;
      }

      if (/^(-{3,}|\*{3,}|_{3,})$/.test(trimmed)) {
        html.push("<hr>");
        i += 1;
        continue;
      }

      if (/^>\s?/.test(raw)) {
        const quote = [];
        while (i < lines.length && (/^>\s?/.test(lines[i]) || !lines[i].trim())) {
          quote.push(lines[i].replace(/^>\s?/, ""));
          i += 1;
        }
        html.push(`<blockquote>${parseMarkdown(quote.join("\n"), {
          usedSlugs,
          headingOffset,
        })}</blockquote>`);
        continue;
      }

      if (trimmed === "<details>" || trimmed.startsWith("<details ")) {
        const openTag = trimmed;
        i += 1;
        let summary = "";
        if (i < lines.length && /^\s*<summary>.*<\/summary>\s*$/.test(lines[i])) {
          const summaryMatch = lines[i].match(/^\s*<summary>(.*)<\/summary>\s*$/);
          summary = `<summary>${inlineMarkdown(summaryMatch ? summaryMatch[1] : "")}</summary>`;
          i += 1;
        }
        const inner = [];
        let depth = 1;
        while (i < lines.length && depth > 0) {
          const value = lines[i].trim();
          if (value === "<details>" || value.startsWith("<details ")) depth += 1;
          if (value === "</details>") {
            depth -= 1;
            if (depth === 0) {
              i += 1;
              break;
            }
          }
          if (depth > 0) inner.push(lines[i]);
          i += 1;
        }
        html.push(`${openTag}${summary}<div class="details-body">${parseMarkdown(inner.join("\n"), {
          usedSlugs,
          headingOffset,
        })}</div></details>`);
        continue;
      }

      if (raw.includes("|") && i + 1 < lines.length && isTableDivider(lines[i + 1])) {
        const header = splitTableRow(raw);
        i += 2;
        const rows = [];
        while (i < lines.length && lines[i].trim() && lines[i].includes("|")) {
          rows.push(splitTableRow(lines[i]));
          i += 1;
        }
        const headHtml = header.map((cell) => `<th>${inlineMarkdown(cell)}</th>`).join("");
        const bodyHtml = rows.map((row) => {
          const padded = [...row];
          while (padded.length < header.length) padded.push("");
          return `<tr>${padded.slice(0, header.length).map((cell) => `<td>${inlineMarkdown(cell)}</td>`).join("")}</tr>`;
        }).join("");
        html.push(`<div class="tablewrap"><table><thead><tr>${headHtml}</tr></thead><tbody>${bodyHtml}</tbody></table></div>`);
        continue;
      }

      const firstList = listMatch(raw);
      if (firstList) {
        const baseIndent = firstList[1].length;
        const ordered = /\d+\./.test(firstList[2]);
        const tag = ordered ? "ol" : "ul";
        const items = [];

        while (i < lines.length) {
          const match = listMatch(lines[i]);
          if (!match || match[1].length !== baseIndent || (/\d+\./.test(match[2])) !== ordered) break;

          const item = [match[3]];
          i += 1;
          while (i < lines.length) {
            const next = lines[i];
            const nextMatch = listMatch(next);
            if (nextMatch && nextMatch[1].length === baseIndent && (/\d+\./.test(nextMatch[2])) === ordered) break;
            if (next.trim() && next.length - next.trimStart().length <= baseIndent && isBlockStart(lines, i)) break;
            if (!next.trim()) {
              item.push("");
              i += 1;
              continue;
            }
            const remove = Math.min(next.length - next.trimStart().length, baseIndent + 3);
            item.push(next.slice(remove));
            i += 1;
          }
          items.push(item.join("\n"));
        }

        html.push(`<${tag}>${items.map((item) => `<li>${parseMarkdown(item, {
          usedSlugs,
          headingOffset: 0,
        })}</li>`).join("")}</${tag}>`);
        continue;
      }

      if (/^<\/?[a-z][^>]*>/i.test(trimmed)) {
        html.push(raw);
        i += 1;
        continue;
      }

      const paragraph = [trimmed];
      i += 1;
      while (i < lines.length && lines[i].trim() && !isBlockStart(lines, i)) {
        paragraph.push(lines[i].trim());
        i += 1;
      }
      html.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    }

    return html.join("\n");
  }

  function buildToc(root, toc) {
    if (!toc) return;
    const headings = [...root.querySelectorAll("h2, h3")];
    if (!headings.length) {
      toc.remove();
      return;
    }
    const list = document.createElement("ol");
    for (const heading of headings) {
      const item = document.createElement("li");
      if (heading.tagName === "H3") item.className = "subsection";
      const anchor = document.createElement("a");
      anchor.href = `#${heading.id}`;
      anchor.textContent = heading.textContent || heading.id;
      item.appendChild(anchor);
      list.appendChild(item);
    }
    toc.appendChild(list);
  }

  async function loadNote() {
    const root = document.querySelector("[data-markdown-source]");
    if (!root) return;
    const source = root.getAttribute("data-markdown-source");
    if (!source) return;

    try {
      const response = await fetch(source, { cache: "no-cache" });
      if (!response.ok) throw new Error(`${response.status} ${response.statusText}`);
      const markdown = normalizeKnownSource(source, await response.text());
      root.innerHTML = parseMarkdown(markdown, {
        skipHeadings: 2,
        headingOffset: 1,
      });
      root.classList.remove("loading");
      buildToc(root, document.getElementById("note-toc"));

      if (typeof renderMathInElement === "function") {
        renderMathInElement(root, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
          ],
          throwOnError: false,
          ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "svg"],
        });
      }
    } catch (error) {
      root.classList.remove("loading");
      root.innerHTML = `<div class="load-error"><strong>노트를 불러오지 못했습니다.</strong><br>${escapeHtml(error.message || error)}</div>`;
    }
  }

  document.addEventListener("DOMContentLoaded", loadNote);
})();
