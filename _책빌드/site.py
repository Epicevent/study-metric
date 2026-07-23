# -*- coding: utf-8 -*-
"""site — 사이트 전체를 한 명령으로 빌드.

    python _책빌드/site.py            # 전부 (md/body 페이지 + 책 + 걸음6 + index)
    python _책빌드/site.py --fast     # cmd 빌더(책·걸음6) 건너뛰고 md/body + index 만

새 문서 추가 = manifest.py 에 항목 하나 + 이 명령. index 는 손대지 않는다(자동 생성).
"""
import os, sys, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
sys.path.insert(0, BASE)

import common
from manifest import TRACKS, DOCS, INDEX_HEADER

FAST = "--fast" in sys.argv


def neighbors():
    """목록(카드 있는 문서)의 선형 순서로 이전/다음 계산."""
    listed = [d for d in DOCS if d.get("card")]
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
            cards.append(f'<a class="card" href="{d["out"]}"><b>{t}</b><span>{desc}</span></a>')
    body = "\n\n".join(cards)
    doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{h['title']}</title>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<main class="indexmain">
<p class="series">{h['series']}</p>
<h1>{h['title']}</h1>
<p class="sub">{h['sub']}</p>

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
    # 크기 요약
    total = 0
    for d in DOCS:
        p = os.path.join(ROOT, d["out"])
        if os.path.exists(p):
            total += os.path.getsize(p)
    print(f"완료 — 문서 {len(DOCS)}개, HTML 총 {total//1024} KB (+ assets 공유 1벌)")


if __name__ == "__main__":
    main()
