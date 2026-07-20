# -*- coding: utf-8 -*-
"""걸음 6 완전판을 '한 페이지 웹 판'으로 빌드 (목차 레일 + 진행률 + 오프라인 수식).

사용: python _책빌드/build_step6_artifact.py [출력경로]

build_step6.py 와 같은 소스(정리_L0-L6/손계산_걸음별/6*.md)를 쓰지만, 출력이
문서 골격(<!doctype>/<html>/<head>/<body>) 없이 본문만 나온다 — 외부 호스트에
그대로 얹을 수 있는 형태. 디자인은 저장소의 기존 시스템(build_page.py의 토큰·서체)을
그대로 따르고, 78쪽 문서에 실제로 필요한 것(파트 목차·현재 위치·진행률)만 더한다.
"""
import html
import os
import re
import sys

import markdown as mdlib

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
STEPS = os.path.join(ROOT, "정리_L0-L6", "손계산_걸음별")
KATEX = os.path.join(BASE, "katex")

# (파일, 순번 라벨, 파트 제목, 한 줄 요지) — 순번은 이 책이 주장하는 읽기 순서다
PARTS = [
    ("6_Gr24_플뤼커_뚝떨어진것들_착륙.md", "지도",
     "뚝 떨어진 것들 착륙시키기",
     "노트가 던진 것 ↔ 걸음 0–5b에서 이미 손으로 한 것"),
    ("6a_그라스만과_플뤼커_바닥부터.md", "1부",
     "그라스만과 플뤼커, 바닥부터",
     "소행렬식이 좌표가 되는 단 하나의 관찰"),
    ("6ab_퍼텐셜은_공짜가_아니다.md", "막간",
     "퍼텐셜은 공짜가 아니다",
     "K는 함수가 아니다 — 함수일 수도 없다"),
    ("6b_퍼텐셜에서_계량까지_전면전개.md", "2부",
     "퍼텐셜에서 계량까지, 전면 전개",
     "16성분 인수분해의 정체는 여인수 크로네커 곱"),
    ("6c_부피와_차수_길1과의_합류.md", "3부",
     "부피와 차수, 길 1과의 합류",
     "π⁴/12의 정체 = ℙ³의 직선 4개와 만나는 직선 2개"),
    ("6f_원_하나로_전부_설명하기.md", "4부",
     "원 하나로 전부 설명하기",
     "θ는 함수가 아니지만 dθ는 전역 — 걸음 6 전체가 이 한 줄"),
    ("6e_쌍대성인가_올적분인가.md", "5부",
     "같은 이야기의 학술 명칭",
     "올적분·푸앵카레 쌍대·Gysin·오일러류는 앞의 세 문장에 붙인 이름"),
    ("6d_손계산_풀이집.md", "부록",
     "손계산 0–11 풀이집",
     "열두 과제의 전체 풀이와 '어디서 막히나' 표"),
]

TITLE = "걸음 6 — Gr(2,4) ↪ ℂP⁵, 바닥부터"
SUB = ("플뤼커 당김 계산 노트를 이론 중간이 아니라 <em>바닥</em>에서 다시 세운 기록. "
       "모든 등식은 sympy·numpy로 줄 단위 검산했다.")


def md_to_html(text):
    """build_page.py 와 같은 파이프라인: 수식을 숨겨두고 마크다운 → 되돌리며 이스케이프."""
    stash = []

    def hide(m):
        stash.append(m.group(0))
        return f"⟪M{len(stash) - 1}⟫"

    text = re.sub(r"\$\$.*?\$\$", hide, text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", hide, text)
    body = mdlib.markdown(text, extensions=["tables"])

    def show(m):
        return html.escape(stash[int(m.group(1))], quote=False)

    return re.sub(r"⟪M(\d+)⟫", show, body)


def build_body():
    """각 파트를 <section>으로. 파트 h1 → h2, 이하 한 단계씩 강등."""
    out = []
    for i, (fname, label, title, _) in enumerate(PARTS):
        path = os.path.join(STEPS, fname)
        if not os.path.exists(path):
            sys.exit(f"소스 없음: {path}")
        lines = open(path, encoding="utf-8").read().split("\n")
        demoted, seen_h1 = [], False
        for ln in lines:
            if ln.startswith("# ") and not seen_h1:
                seen_h1 = True            # 파트 제목은 헤더에서 따로 조판하므로 버린다
                continue
            demoted.append("#" + ln if ln.startswith("#") else ln)
        inner = md_to_html("\n".join(demoted))
        # 절 제목에 앵커
        n = [0]

        def anchor(m):
            n[0] += 1
            return f'<h3 id="p{i}s{n[0]}">{m.group(1)}</h3>'

        inner = re.sub(r"<h3>(.*?)</h3>", anchor, inner, flags=re.S)
        out.append(
            f'<section class="part" id="part{i}" aria-labelledby="part{i}-h">\n'
            f'  <header class="part-head">\n'
            f'    <p class="part-label">{label}</p>\n'
            f'    <h2 id="part{i}-h">{html.escape(title)}</h2>\n'
            f'  </header>\n{inner}\n</section>'
        )
    return "\n\n".join(out)


NAV = "\n".join(
    f'      <li><a href="#part{i}" data-part="{i}">'
    f'<span class="nav-label">{label}</span>'
    f'<span class="nav-title">{html.escape(title)}</span></a></li>'
    for i, (_, label, title, _) in enumerate(PARTS)
)

CARDS = "\n".join(
    f'      <a class="toc-card" href="#part{i}">'
    f'<span class="toc-label">{label}</span>'
    f'<span class="toc-title">{html.escape(title)}</span>'
    f'<span class="toc-note">{html.escape(note)}</span></a>'
    for i, (_, label, title, note) in enumerate(PARTS)
)

CSS = r"""
/* ── 저장소 기존 토큰 (build_page.py) 를 그대로 승계 ───────────────── */
:root{
  --bg:#faf8f4; --fg:#1e1e20; --muted:#6b6862; --line:#ddd8ce;
  --card:#fff; --accent:#8a3033; --box:#f3efe6; --pen:#fdf3e4; --penbd:#e0b36a;
  --rail:#f5f2ec; --shadow:0 1px 3px rgba(30,26,20,.06);
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#191a1c; --fg:#e8e6e1; --muted:#96938c; --line:#3a3b3e;
    --card:#222326; --accent:#e0888a; --box:#26272b; --pen:#2b2620; --penbd:#8a6a35;
    --rail:#1e1f22; --shadow:0 1px 3px rgba(0,0,0,.35);
  }
}
:root[data-theme="light"]{
  --bg:#faf8f4; --fg:#1e1e20; --muted:#6b6862; --line:#ddd8ce;
  --card:#fff; --accent:#8a3033; --box:#f3efe6; --pen:#fdf3e4; --penbd:#e0b36a;
  --rail:#f5f2ec; --shadow:0 1px 3px rgba(30,26,20,.06);
}
:root[data-theme="dark"]{
  --bg:#191a1c; --fg:#e8e6e1; --muted:#96938c; --line:#3a3b3e;
  --card:#222326; --accent:#e0888a; --box:#26272b; --pen:#2b2620; --penbd:#8a6a35;
  --rail:#1e1f22; --shadow:0 1px 3px rgba(0,0,0,.35);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font-family:"Noto Serif KR","Source Serif Pro",Georgia,"Apple SD Gothic Neo","Malgun Gothic",serif;
  line-height:1.78; font-size:16.5px; overflow-x:hidden;
}
@media (prefers-reduced-motion: reduce){ *{animation:none!important;transition:none!important;scroll-behavior:auto!important} }
html{scroll-behavior:smooth}

/* ── 진행률 ────────────────────────────────────────────────────── */
#progress{position:fixed;top:0;left:0;height:2px;width:0;background:var(--accent);z-index:60}

/* ── 레이아웃: 데스크톱은 좌측 레일 + 본문 ─────────────────────── */
.shell{display:block;max-width:100%}
.rail{display:none}
@media (min-width:1120px){
  .shell{display:grid;grid-template-columns:16rem minmax(0,1fr);gap:3rem;
         max-width:74rem;margin:0 auto;padding:0 1.5rem;align-items:start}
  .rail{display:block;position:sticky;top:0;max-height:100vh;overflow-y:auto;
        padding:3.5rem 0 3rem;border-right:1px solid var(--line)}
  .flow{padding-top:3.5rem;min-width:0}
  .masthead-wrap{grid-column:1 / -1}
}
.flow{max-width:46rem;margin:0 auto;padding:0 1.2rem 6rem}
@media (min-width:1120px){ .flow{margin:0;padding-right:2rem} }

/* ── 표제 ──────────────────────────────────────────────────────── */
.masthead{max-width:46rem;margin:0 auto;padding:4rem 1.2rem 0}
.eyebrow{
  font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;
  color:var(--accent);margin:0 0 1rem;font-weight:600;
}
.masthead h1{
  font-size:clamp(1.7rem,4.2vw,2.5rem);line-height:1.25;margin:0;
  letter-spacing:-.005em;text-wrap:balance;
}
.masthead .lede{color:var(--muted);margin:1rem 0 0;font-size:1.02rem;text-wrap:pretty}
.facts{
  display:flex;flex-wrap:wrap;gap:.5rem;margin:1.6rem 0 0;padding:0;list-style:none;
  font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
  font-size:.76rem;font-variant-numeric:tabular-nums;
}
.facts li{border:1px solid var(--line);border-radius:999px;padding:.25rem .7rem;color:var(--muted);background:var(--card)}
.facts li b{color:var(--accent);font-weight:600}
.thesis{
  margin:2.2rem 0 0;padding:1.1rem 1.3rem;background:var(--box);
  border-left:3px solid var(--accent);border-radius:0 6px 6px 0;
}
.thesis p{margin:.2em 0}
.thesis .lead{font-weight:600}

/* ── 목차 카드 ─────────────────────────────────────────────────── */
.toc{max-width:46rem;margin:2.6rem auto 0;padding:0 1.2rem}
.toc h2{
  font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);
  border:0;margin:0 0 .9rem;padding:0;font-weight:600;
}
.toc-grid{display:grid;gap:.55rem}
@media (min-width:680px){ .toc-grid{grid-template-columns:1fr 1fr} }
.toc-card{
  display:grid;grid-template-columns:3.2rem minmax(0,1fr);gap:.1rem .8rem;
  align-items:baseline;text-decoration:none;color:inherit;background:var(--card);
  border:1px solid var(--line);border-radius:7px;padding:.7rem .9rem;box-shadow:var(--shadow);
}
.toc-card:hover,.toc-card:focus-visible{border-color:var(--accent)}
.toc-label{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-size:.72rem;color:var(--accent);letter-spacing:.06em;grid-row:1 / span 2;
}
.toc-title{font-weight:600;font-size:.95rem;line-height:1.4}
.toc-note{color:var(--muted);font-size:.82rem;line-height:1.5}

/* ── 레일 ──────────────────────────────────────────────────────── */
.rail-h{
  font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);
  margin:0 0 .8rem;font-weight:600;
}
.rail ol{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.1rem}
.rail a{
  display:grid;grid-template-columns:2.6rem minmax(0,1fr);gap:.6rem;align-items:baseline;
  text-decoration:none;color:var(--muted);padding:.42rem .6rem .42rem 0;
  border-left:2px solid transparent;padding-left:.7rem;border-radius:0 4px 4px 0;
}
.rail a:hover{color:var(--fg);background:var(--rail)}
.rail a.on{color:var(--fg);border-left-color:var(--accent);background:var(--rail)}
.nav-label{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-size:.68rem;letter-spacing:.05em;color:var(--accent);
}
.nav-title{font-size:.86rem;line-height:1.4}

/* ── 본문 ──────────────────────────────────────────────────────── */
.part{border-top:1px solid var(--line);padding-top:2.2rem;margin-top:3.4rem}
.part:first-of-type{border-top:0}
.part-head{margin-bottom:1.4rem}
.part-label{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-size:.72rem;letter-spacing:.16em;color:var(--accent);margin:0 0 .35rem;
}
.part h2{font-size:1.6rem;margin:0;line-height:1.3;text-wrap:balance;border:0;padding:0}
.flow h3{
  font-size:1.12rem;margin:2.4rem 0 .6rem;color:var(--fg);
  border-bottom:1px solid var(--line);padding-bottom:.3rem;text-wrap:balance;scroll-margin-top:1.5rem;
}
.flow h4{font-size:1rem;margin:1.8rem 0 .5rem;color:var(--accent);text-wrap:balance}
.flow p{margin:0 0 1.05em}
.flow blockquote{
  background:var(--pen);border:1px solid var(--penbd);border-left:4px solid var(--penbd);
  border-radius:7px;margin:1.35em 0;padding:.75em 1.15em;
}
.flow blockquote p{margin:.35em 0}
.flow ol,.flow ul{padding-left:1.35em}
.flow li{margin:.3em 0}
.flow hr{border:0;border-top:1px solid var(--line);margin:2.2em 0}
.flow a{color:var(--accent)}
.flow em{color:var(--muted);font-style:normal}
.flow code{background:var(--box);padding:.08em .38em;border-radius:4px;font-size:.86em;
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.flow pre{background:var(--card);border:1px solid var(--line);border-radius:6px;
  padding:.85em 1em;overflow-x:auto;font-size:.8em;line-height:1.55}
.flow pre code{background:none;padding:0}
.flow strong{font-weight:600}

/* 넓은 것은 자기 컨테이너 안에서만 가로 스크롤 */
.tablewrap{overflow-x:auto;margin:1.25em 0;border:1px solid var(--line);border-radius:7px;background:var(--card)}
.flow table{border-collapse:collapse;width:100%;font-size:.9em;margin:0}
.flow th,.flow td{border-bottom:1px solid var(--line);padding:.5em .75em;text-align:left;vertical-align:top}
.flow th{background:var(--box);font-weight:600;white-space:nowrap}
.flow tr:last-child td{border-bottom:0}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.25em 0;margin:1.1em 0}

:where(a,button,summary):focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}

footer.book{
  max-width:46rem;margin:4rem auto 0;padding:1.4rem 1.2rem 4rem;
  border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;
}
@media (min-width:1120px){ footer.book{margin-left:0} }
footer.book a{color:var(--accent)}
"""

JS = r"""
document.addEventListener("DOMContentLoaded", function () {
  // 오프라인 수식 렌더링
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "$",  right: "$",  display: false}
    ],
    throwOnError: false,
    ignoredTags: ["script","noscript","style","textarea","pre","code","svg"]
  });

  // 표는 각자 가로 스크롤 컨테이너에 담아 본문이 옆으로 밀리지 않게
  document.querySelectorAll(".flow table").forEach(function (t) {
    if (t.parentElement && t.parentElement.classList.contains("tablewrap")) return;
    var w = document.createElement("div");
    w.className = "tablewrap";
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  // 진행률
  var bar = document.getElementById("progress");
  function onScroll() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
  }
  window.addEventListener("scroll", onScroll, {passive: true});
  onScroll();

  // 현재 파트 표시
  var links = Array.prototype.slice.call(document.querySelectorAll(".rail a"));
  var parts = links.map(function (a) { return document.getElementById("part" + a.dataset.part); });
  if ("IntersectionObserver" in window) {
    var seen = new Map();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { seen.set(e.target, e); });
      var best = null;
      seen.forEach(function (e) {
        if (!e.isIntersecting) return;
        if (!best || e.target.offsetTop < best.target.offsetTop) best = e;
      });
      if (!best) return;
      links.forEach(function (a) {
        a.classList.toggle("on", a.dataset.part === best.target.id.replace("part", ""));
      });
    }, {rootMargin: "-10% 0px -70% 0px"});
    parts.forEach(function (p) { if (p) io.observe(p); });
  }
});
"""


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "_step6_artifact.html")
    kcss = open(os.path.join(KATEX, "katex.inline.css"), encoding="utf-8").read()
    kjs = open(os.path.join(KATEX, "katex.min.js"), encoding="utf-8").read()
    ar = open(os.path.join(KATEX, "auto-render.min.js"), encoding="utf-8").read()

    doc = f"""<title>{html.escape(TITLE)}</title>
<style>{kcss}</style>
<style>{CSS}</style>

<div id="progress" aria-hidden="true"></div>

<div class="masthead-wrap">
  <header class="masthead">
    <p class="eyebrow">study metric · 걸음 6</p>
    <h1>{html.escape(TITLE)}</h1>
    <p class="lede">{SUB}</p>
    <ul class="facts">
      <li>8부작 · 약 <b>78</b>쪽</li>
      <li>손계산 과제 <b>12</b></li>
      <li>sympy·numpy 검산 <b>58/58</b></li>
      <li>대상 원문: <b>외부 노트</b></li>
    </ul>
    <div class="thesis">
      <p class="lead">이 책이 주장하는 것은 하나다 — 걸음 6 전체가 세 문장이다.</p>
      <p>① 퍼텐셜은 차트마다. &nbsp;② 그 미분은 전역. &nbsp;③ 안 붙는 정도 = 감김수 = ∫ω.</p>
      <p>Gysin·오일러류·천류는 ①②③을 일반 차원에서 부르는 <em>이름</em>일 뿐이고,
         셋 다 <em>원 위의 각도</em> 하나로 손에 잡힌다(4부).</p>
    </div>
  </header>

  <nav class="toc" aria-label="차례">
    <h2>차례 — 이 순서로 읽을 것</h2>
    <div class="toc-grid">
{CARDS}
    </div>
  </nav>
</div>

<div class="shell">
  <nav class="rail" aria-label="파트 이동">
    <p class="rail-h">걸음 6</p>
    <ol>
{NAV}
    </ol>
  </nav>

  <main class="flow">
{build_body()}
    <footer class="book">
      원문 마크다운은 저장소 <code>정리_L0-L6/손계산_걸음별/6*.md</code>,
      검산은 <code>verify6_plucker.py</code> (58/58).
      이 페이지는 <code>python _책빌드/build_step6_artifact.py</code> 로 재생성된다.
    </footer>
  </main>
</div>

<script>{kjs}</script>
<script>{ar}</script>
<script>{JS}</script>
"""
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print("written:", out, f"{len(doc) // 1024} KB")


if __name__ == "__main__":
    main()
