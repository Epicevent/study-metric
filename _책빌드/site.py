# -*- coding: utf-8 -*-
"""site — 사이트 전체를 한 명령으로 빌드.

    python _책빌드/site.py            # 전부 (md/body 페이지 + 책 + 걸음6 + index)
    python _책빌드/site.py --fast     # cmd 빌더(책·걸음6) 건너뛰고 md/body + index 만

본문 source는 manifest.py에 둔다. 표시 순서와 빈 문서는 site_order.py가 덧씌운다.
"""
import os, sys, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, BASE)

import common
from manifest import DOCS as BASE_DOCS, INDEX_HEADER as BASE_INDEX_HEADER, TRACKS as BASE_TRACKS

try:
    from site_order import apply_order, INDEX_HEADER, INDEX_NOTICE, TRACKS
    DOCS = apply_order(BASE_DOCS)
except ImportError:
    DOCS = BASE_DOCS
    INDEX_HEADER = BASE_INDEX_HEADER
    INDEX_NOTICE = ""
    TRACKS = BASE_TRACKS

FAST = "--fast" in sys.argv


def neighbors():
    """목록에 실리고 nav=True인 문서만 선형 이전/다음으로 연결."""
    listed = [d for d in DOCS if d.get("card") and d.get("nav", True)]
    nb = {}
    for i, d in enumerate(listed):
        prev = listed[i - 1] if i > 0 else None
        nxt = listed[i + 1] if i < len(listed) - 1 else None
        nb[d["out"]] = (
            (prev["out"], prev["card"][0]) if prev else None,
            (nxt["out"], nxt["card"][0]) if nxt else None,
        )
    return nb


def build_docs():
    nb = neighbors()
    for d in DOCS:
        prev, nxt = nb.get(d["out"], (None, None))
        if d["kind"] == "md":
            common.build_md(d["src"], d["out"], d["series"], prev=prev, nxt=nxt)
            print(f"  md   → {d['out']}")
        elif d["kind"] == "body":
            body = open(os.path.join(ROOT, d["src"]), encoding="utf-8").read()
            common.page(d["out"], d["title"], d["series"], body,
                        prev=prev, nxt=nxt, titlepage=False,
                        footer=f"본문 소스: {d['src']} — 재빌드: python _책빌드/site.py")
            print(f"  body → {d['out']}")
        elif d["kind"] == "existing":
            # Existing standalone HTML is catalogued and ordered, but its body is never rewritten.
            # ASSERTION: an existing document must already be published at its output path.
            out = os.path.join(ROOT, d["out"])
            if not os.path.exists(out):
                sys.exit(f"기존 HTML 없음: {d['out']}")
            print(f"  keep → {d['out']}")
        elif d["kind"] == "static":
            src = os.path.join(ROOT, d["src"])
            doc = open(src, encoding="utf-8").read()
            back = (
                '<style>.study-metric-back{position:fixed;left:16px;top:16px;z-index:9999;'
                'padding:9px 13px;border:1px solid rgba(127,127,127,.35);border-radius:999px;'
                'background:rgba(255,255,255,.94);color:#18221b;text-decoration:none;'
                'font:700 13px/1.2 system-ui,sans-serif;box-shadow:0 4px 18px rgba(0,0,0,.12)}'
                '.study-metric-back:hover{transform:translateY(-1px)}</style>'
                '<a class="study-metric-back" href="index.html">← study metric 목록</a>'
            )
            doc = doc.replace("</body>", back + "\n</body>", 1) if "</body>" in doc else doc + back
            out = os.path.join(ROOT, d["out"])
            open(out, "w", encoding="utf-8").write(doc)
            print(f"  html → {d['out']}")
        elif d["kind"] == "cmd":
            if FAST:
                print(f"  skip → {d['out']}  (--fast)")
                continue
            r = subprocess.run(d["cmd"], cwd=ROOT, capture_output=True, text=True,
                               encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
            tail = (r.stdout or "").strip().splitlines()
            print(f"  cmd  → {d['out']}  ({tail[-1] if tail else 'ok'})")
            if r.returncode != 0:
                sys.exit(f"빌더 실패: {d['cmd']}\n{r.stderr}")


def build_index():
    h = INDEX_HEADER
    cards = []
    for tid, theading in TRACKS:
        docs = [d for d in DOCS if d["track"] == tid and d.get("card")]
        if not docs:
            continue
        cards.append(f'<p class="trackhead">{theading}</p>')
        for d in docs:
            t, desc = d["card"]
            cls = "card stub" if d.get("stub") else "card"
            mark = '<small class="stubmark">빈 문서</small>' if d.get("stub") else ""
            cards.append(
                f'<a class="{cls}" href="{d["out"]}"><b>{t}{mark}</b><span>{desc}</span></a>'
            )
    body = "\n\n".join(cards)
    extra_style = """
<style>
.route{margin:1.5em 0 2.2em;padding:.9em 1.05em;background:var(--box);border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:10px}
.route p{margin:.35em 0}
a.card.stub{border-style:dashed;background:var(--box)}
a.card.stub:hover{border-color:var(--accent)}
.stubmark{display:inline-block;margin-left:.55em;padding:.08em .45em;border:1px solid var(--accent);border-radius:999px;color:var(--accent);font-size:.68em;vertical-align:.12em}
</style>
""".strip()
    notice = f"\n{INDEX_NOTICE}\n" if INDEX_NOTICE else ""
    doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{h['title']}</title>
<link rel="stylesheet" href="assets/site.css">
{extra_style}
</head>
<body>
<main class="indexmain">
<p class="series">{h['series']}</p>
<h1>{h['title']}</h1>
<p class="sub">{h['sub']}</p>
{notice}
{body}

<footer>{h['footer']}</footer>
</main>
</body>
</html>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(doc)
    print("  idx  → index.html")


def main():
    print("문서 빌드:")
    build_docs()
    print("목록 생성:")
    build_index()
    total = 0
    for d in DOCS:
        p = os.path.join(ROOT, d["out"])
        if os.path.exists(p):
            total += os.path.getsize(p)
    print(f"완료 — 문서 {len(DOCS)}개, HTML 총 {total//1024} KB (+ assets 공유 1벌)")


if __name__ == "__main__":
    main()
