# -*- coding: utf-8 -*-
"""걸음 6 (Gr(2,4) 플뤼커) 4부작을 한 권의 self-contained HTML로 빌드.

사용: python _책빌드/build_step6.py
소스는 정리_L0-L6/손계산_걸음별/6*.md 네 개 — 이 스크립트는 원본을 복사하지 않고
빌드 시점에 이어붙인 뒤 build_page.py의 렌더러를 그대로 쓴다 (단일 진실 원천 유지).
"""
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
STEPS = os.path.join(ROOT, "정리_L0-L6", "손계산_걸음별")

PARTS = [
    ("6_Gr24_플뤼커_뚝떨어진것들_착륙.md",      "지도 — 뚝 떨어진 것들 착륙시키기"),
    ("6a_그라스만과_플뤼커_바닥부터.md",        "1부 — 그라스만과 플뤼커, 바닥부터"),
    ("6ab_퍼텐셜은_공짜가_아니다.md",           "막간 — 퍼텐셜은 공짜가 아니다"),
    ("6b_퍼텐셜에서_계량까지_전면전개.md",      "2부 — 퍼텐셜에서 계량까지, 전면 전개"),
    ("6c_부피와_차수_길1과의_합류.md",          "3부 — 부피와 차수, 길 1과의 합류"),
    ("6f_원_하나로_전부_설명하기.md",           "4부 — 원 하나로 전부 설명하기 (가장 단순한 상황)"),
    ("6e_쌍대성인가_올적분인가.md",             "5부 — 같은 이야기의 학술 명칭 (올적분·쌍대성·오일러류)"),
    ("6d_손계산_풀이집.md",                     "부록 — 손계산 0–11 풀이집"),
]

TITLE = "걸음 6 — Gr(2,4) ↪ ℂP⁵, 바닥부터 (완전판)"

chunks = [f"# {TITLE}\n"]
chunks.append(
    "> 대상 원문: `Gr24_플뤼커당김_계산노트.html` (외부 노트 — 저장소에 포함하지 않는다). 그 노트는 계산은 완결이나 **전개가 이론 중간부터 시작한다** —\n"
    "> 그라스만·플뤼커·Boothby–Wang이 동기 없이 등장한다. 이 책은 그 전부를 걸음 0–5b에서 이미 손으로 한 것 위에 착륙시킨다.\n"
    "> 검산: `정리_L0-L6/손계산_걸음별/verify6_plucker.py`\n"
)

chunks.append("\n## 차례\n")
for i, (_, label) in enumerate(PARTS, 1):
    chunks.append(f"{i}. {label}")
chunks.append("")

for fname, label in PARTS:
    path = os.path.join(STEPS, fname)
    if not os.path.exists(path):
        sys.exit(f"소스 없음: {path}")
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    # 각 파트의 h1은 책의 h2로 강등 (표제지 제목과 충돌 방지)
    body = []
    for ln in lines:
        if ln.startswith("# "):
            body.append("## " + ln[2:])
        elif ln.startswith("#"):
            body.append("#" + ln)      # h2→h3, h3→h4 …
        else:
            body.append(ln)
    chunks.append("\n---\n")
    chunks.append("\n".join(body))

combined = "\n".join(chunks)
tmp = os.path.join(BASE, "_step6_combined.md")
open(tmp, "w", encoding="utf-8").write(combined)

out = os.path.join(ROOT, "걸음6_Gr24_플뤼커_완전판.html")
subprocess.run(
    [sys.executable, os.path.join(BASE, "build_page.py"), tmp, out, "study metric · 걸음 6"],
    check=True,
)
os.remove(tmp)
print("parts:", len(PARTS), "| chars:", len(combined))
