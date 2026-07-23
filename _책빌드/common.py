# -*- coding: utf-8 -*-
"""common — 모든 페이지가 쓰는 공용 렌더러.

- 수식 보호 md→html (tables, md_in_html)
- 공유 자산 링크 (assets/katex.min.css, site.css, katex.min.js, auto-render, render.js)
- 사이트 내비 내장 (상단 sticky: ← 목록 + 제목 + 이전/다음, 하단: 돌아가기)
- noindex

모든 출력은 저장소 루트에 놓인다 (assets/ 상대경로 전제).
"""
import os, re
import markdown as mdlib

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)


def md2html(text):
    mathblocks = []

    def stash(mm):
        mathblocks.append(mm.group(0))
        return f"⟪M{len(mathblocks)-1}⟫"

    text = re.sub(r"\$\$.*?\$\$", stash, text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", stash, text)
    body = mdlib.markdown(text, extensions=["tables", "md_in_html"])

    def unstash(mm):
        raw = mathblocks[int(mm.group(1))]
        return raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    return re.sub(r"⟪M(\d+)⟫", unstash, body)


def split_title(md_text):
    """첫 h1을 표제로 승격."""
    m = re.match(r"^# (.+)\n", md_text)
    if m:
        return m.group(1).strip(), md_text[m.end():]
    return None, md_text


def _nav(title, prev=None, nxt=None):
    pn = ""
    if prev or nxt:
        parts = []
        if prev:
            parts.append(f'<a href="{prev[0]}" title="{prev[1]}">‹ 이전</a>')
        if nxt:
            parts.append(f'<a href="{nxt[0]}" title="{nxt[1]}">다음 ›</a>')
        pn = f'<span class="pn">{" ".join(parts)}</span>'
    return (f'<nav class="sitenav"><a class="home" href="index.html">← 목록</a>'
            f'<span class="navtitle">{title}</span>{pn}</nav>')


def _bottom(prev=None, nxt=None):
    left = f'<a href="{prev[0]}">‹ {prev[1]}</a>' if prev else "<span></span>"
    mid = '<a href="index.html">← 목록으로 돌아가기</a>'
    right = f'<a href="{nxt[0]}">{nxt[1]} ›</a>' if nxt else "<span></span>"
    return f'<div class="sitenav-bottom">{left}{mid}{right}</div>'


def page(out_name, title, series, body_html, extra_css="", extra_head="",
         prev=None, nxt=None, footer=None, titlepage=True):
    """공용 페이지 셸. out_name 은 루트 기준 파일명."""
    head_extra = f"<style>{extra_css}</style>" if extra_css else ""
    header = ""
    if titlepage:
        header = (f'<header class="titlepage"><p class="series">{series}</p>'
                  f"<h1>{title}</h1></header>")
    foot = f"<footer>{footer}</footer>" if footer else ""
    doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<link rel="stylesheet" href="assets/katex.min.css">
<link rel="stylesheet" href="assets/site.css">
{head_extra}{extra_head}
</head>
<body>
{_nav(title, prev, nxt)}
{header}
<main>
{body_html}
{foot}
</main>
{_bottom(prev, nxt)}
<script defer src="assets/katex.min.js"></script>
<script defer src="assets/auto-render.min.js"></script>
<script defer src="assets/render.js"></script>
</body>
</html>"""
    out = os.path.join(ROOT, out_name)
    open(out, "w", encoding="utf-8").write(doc)
    return out


def build_md(src, out_name, series, prev=None, nxt=None):
    """마크다운 파일 하나 → 페이지. 첫 h1이 제목."""
    path = src if os.path.isabs(src) else os.path.join(ROOT, src)
    text = open(path, encoding="utf-8").read()
    title, rest = split_title(text)
    title = title or os.path.basename(src)
    body = md2html(rest)
    footer = f"원문 마크다운: {os.path.relpath(path, ROOT)} — 재빌드: python _책빌드/site.py"
    return page(out_name, title, series, body, prev=prev, nxt=nxt, footer=footer)
