# -*- coding: utf-8 -*-
"""범용 md → self-contained HTML (KaTeX 인라인) 변환기.

사용: python build_page.py <src.md> <out.html> [시리즈 라벨]
첫 h1이 표제지 제목이 된다. 디자인은 build_5b와 동일 계열.
"""
import os, re, sys
import markdown as mdlib

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

src = sys.argv[1] if len(sys.argv) > 1 else "다음트랙_2026-07-10.md"
out = sys.argv[2] if len(sys.argv) > 2 else "다음트랙.html"
series = sys.argv[3] if len(sys.argv) > 3 else "study metric"
SRC = src if os.path.isabs(src) else os.path.join(ROOT, src)
OUT = out if os.path.isabs(out) else os.path.join(ROOT, out)

text = open(SRC, encoding="utf-8").read()
m = re.match(r"^# (.+)\n", text)
title = m.group(1).strip() if m else os.path.basename(SRC)
if m:
    text = text[m.end():]

mathblocks = []
def stash(mm):
    mathblocks.append(mm.group(0))
    return f"⟪M{len(mathblocks)-1}⟫"
text = re.sub(r"\$\$.*?\$\$", stash, text, flags=re.S)
text = re.sub(r"\$[^$\n]+\$", stash, text)
body = mdlib.markdown(text, extensions=["tables"])
def unstash(mm):
    raw = mathblocks[int(mm.group(1))]
    return raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
body = re.sub(r"⟪M(\d+)⟫", unstash, body)

kcss = open(os.path.join(BASE, "katex", "katex.inline.css"), encoding="utf-8").read()
kjs = open(os.path.join(BASE, "katex", "katex.min.js"), encoding="utf-8").read()
ar = open(os.path.join(BASE, "katex", "auto-render.min.js"), encoding="utf-8").read()

CSS = """
:root{--bg:#faf8f4;--fg:#1e1e20;--muted:#6b6862;--line:#ddd8ce;--card:#fff;--accent:#8a3033;
--box:#f3efe6;--pen:#fdf3e4;--penbd:#e0b36a}
@media (prefers-color-scheme: dark){:root{--bg:#191a1c;--fg:#e8e6e1;--muted:#96938c;--line:#3a3b3e;
--card:#222326;--accent:#e0888a;--box:#26272b;--pen:#2b2620;--penbd:#8a6a35}}
:root[data-theme="light"]{--bg:#faf8f4;--fg:#1e1e20;--muted:#6b6862;--line:#ddd8ce;--card:#fff;--accent:#8a3033;--box:#f3efe6;--pen:#fdf3e4;--penbd:#e0b36a}
:root[data-theme="dark"]{--bg:#191a1c;--fg:#e8e6e1;--muted:#96938c;--line:#3a3b3e;--card:#222326;--accent:#e0888a;--box:#26272b;--pen:#2b2620;--penbd:#8a6a35}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font-family:"Noto Serif KR","Source Serif Pro",Georgia,"Apple SD Gothic Neo","Malgun Gothic",serif;
line-height:1.78;font-size:16.5px}
main,header.titlepage{max-width:46em;margin:0 auto;padding:0 1.2em}
header.titlepage{padding-top:3.5em;text-align:center;border-bottom:3px double var(--line);padding-bottom:1.6em}
header.titlepage h1{font-size:1.75em;margin:.2em 0;letter-spacing:.01em}
.series{color:var(--muted);letter-spacing:.2em;font-size:.85em;margin:0}
main{padding-top:1.8em;padding-bottom:5em}
h2{font-size:1.3em;border-bottom:1.5px solid var(--line);padding-bottom:.25em;margin-top:2.4em}
h3{font-size:1.08em;margin-top:1.8em;color:var(--accent)}
blockquote{background:var(--pen);border:1.5px solid var(--penbd);border-left:5px solid var(--penbd);
border-radius:8px;margin:1.3em 0;padding:.7em 1.1em}
blockquote p{margin:.35em 0}
table{border-collapse:collapse;margin:1.2em 0;width:100%;font-size:.93em}
th,td{border:1px solid var(--line);padding:.45em .7em;text-align:left;vertical-align:top}
th{background:var(--box)}
ol,ul{padding-left:1.4em}
li{margin:.3em 0}
pre{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:.8em 1em;overflow-x:auto;font-size:.8em;line-height:1.55}
code{background:var(--box);padding:.08em .35em;border-radius:4px;font-size:.9em}
pre code{background:none;padding:0}
hr{border:none;border-top:1px solid var(--line);margin:2.2em 0}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.2em 0}
a{color:var(--accent)}
footer{margin-top:3.5em;color:var(--muted);font-size:.85em;border-top:1px solid var(--line);padding-top:1em}
em{color:var(--muted)}
"""

doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<style>{kcss}</style>
<style>{CSS}</style>
</head>
<body>
<header class="titlepage">
<p class="series">{series}</p>
<h1>{title}</h1>
</header>
<main>
{body}
<footer>원문 마크다운: {os.path.basename(SRC)} (저장소 루트) — 진행 기록은 마크다운에 적고 이 페이지는 재빌드: python _책빌드/build_page.py</footer>
</main>
<script>{kjs}</script>
<script>{ar}</script>
<script>
document.addEventListener("DOMContentLoaded", function() {{
  renderMathInElement(document.body, {{
    delimiters: [
      {{left: "$$", right: "$$", display: true}},
      {{left: "$", right: "$", display: false}}
    ],
    throwOnError: false,
    ignoredTags: ["script","noscript","style","textarea","pre","code","svg"]
  }});
}});
</script>
</body>
</html>"""

open(OUT, "w", encoding="utf-8").write(doc)
print("written:", OUT, len(doc) // 1024, "KB")
