# -*- coding: utf-8 -*-
"""inject_nav — 저장소 루트의 모든 (git 추적) HTML 문서에 사이트 내비게이션 주입.

- 상단 고정 바: ← 목록 (index.html) + 문서 제목
- 문서 끝: ← 목록으로 돌아가기
- 마커(<!-- site-nav-start/end -->)로 멱등: 재실행하면 교체(디자인 갱신 전파)
- index.html 자신과 외부 원문(git 미추적)은 건드리지 않음

사용: 어떤 빌더로든 페이지를 (재)빌드한 뒤  python _책빌드/inject_nav.py
"""
import os, re, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)

NAV_CSS = """
.sitenav{position:sticky;top:0;z-index:50;display:flex;gap:1em;align-items:center;
padding:.5em 1.2em;background:var(--bg,#faf8f4);border-bottom:1px solid var(--line,#ddd8ce);
font-size:.95em}
.sitenav a.home{color:var(--accent,#8a3033);text-decoration:none;font-weight:700;white-space:nowrap}
.sitenav a.home:hover{text-decoration:underline}
.sitenav .navtitle{color:var(--muted,#6b6862);font-size:.88em;overflow:hidden;
text-overflow:ellipsis;white-space:nowrap;min-width:0}
.sitenav-bottom{max-width:46em;margin:0 auto;padding:0 1.2em 3em;text-align:center}
.sitenav-bottom a{color:var(--accent,#8a3033);text-decoration:none;font-weight:600}
.sitenav-bottom a:hover{text-decoration:underline}
""".strip()

START = "<!-- site-nav-start -->"
END = "<!-- site-nav-end -->"
BSTART = "<!-- site-nav-bottom-start -->"
BEND = "<!-- site-nav-bottom-end -->"


def tracked_root_htmls():
    out = subprocess.run(["git", "-c", "core.quotepath=false", "ls-files", "*.html"],
                         cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    files = [f for f in out.stdout.splitlines()
             if "/" not in f and f != "index.html"]
    return files


def inject(path):
    fp = os.path.join(ROOT, path)
    h = open(fp, encoding="utf-8").read()
    m = re.search(r"<title>(.*?)</title>", h, re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else path
    nav = (f"{START}\n<style>{NAV_CSS}</style>\n"
           f'<nav class="sitenav"><a class="home" href="index.html">← 목록</a>'
           f'<span class="navtitle">{title}</span></nav>\n{END}')
    bottom = (f"{BSTART}\n"
              f'<div class="sitenav-bottom"><a href="index.html">← 목록으로 돌아가기</a></div>'
              f"\n{BEND}")

    # 기존 블록 제거 (멱등)
    h = re.sub(re.escape(START) + r".*?" + re.escape(END), "", h, flags=re.S)
    h = re.sub(re.escape(BSTART) + r".*?" + re.escape(BEND), "", h, flags=re.S)

    # 상단: <body...> 바로 뒤
    mb = re.search(r"<body[^>]*>", h)
    if not mb:
        print(f"  건너뜀 (body 없음): {path}")
        return False
    h = h[: mb.end()] + "\n" + nav + h[mb.end():]

    # 하단: </body> 바로 앞
    idx = h.rfind("</body>")
    if idx != -1:
        h = h[:idx] + bottom + "\n" + h[idx:]

    open(fp, "w", encoding="utf-8").write(h)
    return True


def main():
    files = tracked_root_htmls()
    done = 0
    for f in files:
        if inject(f):
            done += 1
            print(f"  nav 주입: {f}")
    print(f"완료: {done}/{len(files)}")


if __name__ == "__main__":
    main()
