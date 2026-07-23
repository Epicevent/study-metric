# -*- coding: utf-8 -*-
"""Gr(2,4) 핵심계산 모음 → 주제별 self-contained 책 (단일 HTML) 조립기."""
import re, os, sys, html, json

BASE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(BASE, "transcribe")

# ---------------------------------------------------------------- PART A: parse
PROB_HEAD = re.compile(r"^#{2,4} \[(W|★|★★)\] (?:문제 )?([A-Z]?\d{1,3})(?:[.\s]\s*(.*))?$")
FOUR_HEAD = re.compile(r"^\*\*\[(W|★|★★)\] (\d{1,3})\.\s*(.*?)\*\*\s*$")
SETUP_HEAD = re.compile(r"^#{2,4} 필요한 정의\s*$")
STAGE_HEAD = re.compile(r"^## (?:(\d)단계|병렬 트랙)")
PART_HEAD = re.compile(r"^#{2,4} (?:Part )?([A-Z0-9])\.\s+(.*)$")
FPART_HEAD = re.compile(r"^### Part (\d+)\.\s*(.*)$")
CONV_HEAD = re.compile(r"^#{2,4} 0\.\s*(전체 convention|정규화 convention|Convention)\s*$")
ANSKEY_HEAD = re.compile(r"^## 검산용 정답")
PAGE_MARK = re.compile(r"^<!-- PAGE \d+ -->\s*$")

def read(fn):
    with open(os.path.join(TR, fn), encoding="utf-8") as f:
        return f.read().splitlines()

lines = []
for fn in ["part2_p13-24.md", "part3_p25-36.md", "part4_p37-48.md",
           "part5_p49-60.md", "part6_p61-72.md", "part7_p73-84.md",
           "part8_p85-94.md"]:
    lines += read(fn)

problems = {}        # (stage,id) -> dict(tag,id,title,body,setup,part)
order = []           # source order of (stage,id)
stage_intro = {}     # stage -> text right after stage head (before first part/prob)
stage_conv = {}      # stage -> convention block text
answers1 = {}        # 1단계: id -> answer text
fourier_parts = []   # [(num,title)]
fourier_key = {}     # num -> answer text
fourier_key_extra = []  # entries with no matching problem

stage = "1"          # part2 starts inside 1단계 (LRG map tail handled below)
part = None
mode = None          # None|'prob'|'setup'|'conv'|'intro'|'anskey1'|'anskeyF'|'skip'
cur = None
setup_pending = None
cur_fpart = None

def flush():
    global cur
    if cur is not None:
        key = (cur["stage"], cur["id"])
        cur["body"] = "\n".join(cur["body"]).strip()
        problems[key] = cur
        order.append(key)
    cur = None

def start_prob(stage_, tag, pid, title):
    global cur, setup_pending
    flush()
    cur = dict(stage=stage_, tag=tag, id=pid, title=(title or "").strip().rstrip("."),
               body=[], setup=setup_pending, part=part, fpart=cur_fpart)
    setup_pending = None

i = 0
# skip LRG-map tail + 연계표 at top of part2 (lines until '## 1단계')
while i < len(lines) and not lines[i].startswith("## 1단계"):
    i += 1

collect = None  # list being appended for intro/conv/setup
while i < len(lines):
    ln = lines[i]
    if PAGE_MARK.match(ln):
        i += 1; continue
    m = STAGE_HEAD.match(ln)
    if m:
        flush()
        stage = m.group(1) if m.group(1) else "F"
        part = None; cur_fpart = None
        mode = "intro"; stage_intro[stage] = []
        collect = stage_intro[stage]
        i += 1; continue
    if ANSKEY_HEAD.match(ln):
        flush()
        mode = "anskey1" if stage == "1" else "anskeyF"
        collect = None
        i += 1; continue
    m = CONV_HEAD.match(ln)
    if m:
        flush()
        mode = "conv"; stage_conv[stage] = []
        collect = stage_conv[stage]
        i += 1; continue
    if SETUP_HEAD.match(ln):
        flush()
        mode = "setup"; setup_pending = []
        collect = setup_pending
        i += 1; continue
    m = FPART_HEAD.match(ln) if stage == "F" else None
    if m:
        flush()
        if mode == "anskeyF":
            cur_fpart = int(m.group(1))
            i += 1; continue
        cur_fpart = int(m.group(1))
        fourier_parts.append((int(m.group(1)), m.group(2).strip()))
        mode = None; collect = None
        i += 1; continue
    m = PROB_HEAD.match(ln)
    if m and stage != "F":
        start_prob(stage, m.group(1), m.group(2), m.group(3))
        mode = "prob"; collect = cur["body"]
        i += 1; continue
    m = FOUR_HEAD.match(ln)
    if m and stage == "F" and mode != "anskeyF":
        start_prob("F", m.group(1), m.group(2), m.group(3))
        mode = "prob"; collect = cur["body"]
        i += 1; continue
    m = PART_HEAD.match(ln)
    if m and stage != "F" and not CONV_HEAD.match(ln):
        flush()
        part = m.group(1)
        mode = None; collect = None
        i += 1; continue
    # answer key items
    if mode == "anskey1":
        m = re.match(r"^- \*\*([A-Z]\d{2})\.\*\*\s*(.*)$", ln)
        if m:
            answers1[m.group(1)] = m.group(2).strip()
        elif ln.strip() and not ln.startswith("#") and not ln.startswith("---") and answers1:
            answers1[list(answers1)[-1]] += " " + ln.strip()
        i += 1; continue
    if mode == "anskeyF":
        m = re.match(r"^(\d{1,3})\.\s+(.*)$", ln)
        if m:
            fourier_key[int(m.group(1))] = m.group(2).strip()
            lastk = int(m.group(1))
        elif ln.strip() and not ln.startswith("#") and fourier_key:
            fourier_key[lastk] += " " + ln.strip()
        i += 1; continue
    if ln.startswith("# ") or ln.startswith("## "):  # stray headings end blocks
        flush(); mode = None; collect = None
        i += 1; continue
    if collect is not None:
        collect.append(ln)
    i += 1
flush()

for st in list(stage_intro):
    stage_intro[st] = "\n".join(stage_intro[st]).strip().strip("-").strip()
for st in list(stage_conv):
    stage_conv[st] = "\n".join(stage_conv[st]).strip()
for k, v in problems.items():
    if v["setup"] is not None:
        v["setup"] = "\n".join(v["setup"]).strip()

# LRG selected
lrg = {}
lrg_front = ""
lp = os.path.join(TR, "lrg_selected.md")
if os.path.exists(lp):
    txt = open(lp, encoding="utf-8").read()
    txt = re.sub(r"<!-- LRG p\.\d+ -->", "", txt)
    mfront = re.split(r"^### LRG Problem \d+.*$", txt, flags=re.M)[0]
    lrg_front = mfront.strip()
    for m in re.finditer(r"^### LRG Problem (\d+)(.*?)(?=^### LRG Problem \d+|\Z)",
                         txt, flags=re.M | re.S):
        n = int(m.group(1))
        body = m.group(2).strip()
        title = ""
        tm = re.match(r"^[.:\s—-]*(.*)$", body.splitlines()[0]) if body else None
        lrg[n] = dict(title="", body=body)

print(f"parsed problems: {len(problems)}")
from collections import Counter
print(Counter(k[0] for k in problems))

# ------------------------------------------------------- PART B: topic spec
CIRC = {"1": "①", "2": "②", "3": "③", "4": "④", "5": "⑤", "F": "Ⓕ"}

def ex(stage_, *ids):
    """existing (stage,id) refs in given order"""
    out = []
    for pid in ids:
        if (stage_, pid) in problems:
            out.append(("p", stage_, pid))
        else:
            print(f"  !! missing ref {stage_}-{pid}")
    return out

def rng(stage_, prefix, a, b):
    out = []
    w = len(str(a))
    for n in range(a, b + 1):
        pid = f"{prefix}{n:0{w}d}" if prefix in ("P",) else f"{prefix}{n}"
        if (stage_, pid) in problems:
            out.append(("p", stage_, pid))
    return out

def lr(*ns):
    return [("lrg", n) for n in ns]

CH = []
CH.append(dict(num=1, title="S²의 계량·면적 — stereographic",
    intro="모든 것의 출발점. 구면을 평면 좌표 하나 $z$로 읽는 법(입체사영)과, 그 좌표에서 계량·넓이가 $\\lambda=\\frac{2}{1+|z|^2}$, $dA=\\frac{4\\,dx\\wedge dy}{(1+|z|^2)^2}$ 로 읽히는 것을 손에 붙인다. 이 장의 $\\lambda$와 $dA$가 이후 모든 장의 재료다.",
    see=[("in", "① 상단 고정 규칙 (orientation!) — 아래 인라인"),
         ("gone", "QFIM노트 §3–6 (제외된 타자 노트) — 이 장의 규약·문제가 해당 내용을 대체"),
         ("gone", "손노트 1쪽 — 부록 C 사례연구 참조")],
    refs=[("conv", "1")] + rng("1", "A0", 1, 6) + rng("1", "D0", 1, 4) + rng("1", "F0", 1, 4)
         + lr(1, 2) + ex("1", "D05", "D06", "D07", "D08", "D09", "D10")
         + rng("1", "F0", 5, 8) + rng("1", "G0", 1, 3),
    check="전체 면적 $4\\pi$ · $dz\\wedge d\\bar z=-2i\\,dx\\wedge dy$"))

CH.append(dict(num=2, title="Wirtinger 복소화",
    intro="실좌표 $(x,y)$ 미분을 복소좌표 $z,\\bar z$ 미분으로 재조립하는 기술. 뒤의 QFIM·Kähler 계산 전체가 이 표기로 돌아간다. 핵심 산출물은 $\\partial_z\\partial_{\\bar z}\\log D=1/D^2$ 한 줄이다.",
    see=[("in", "⑤ 상단 convention — 아래 인라인"),
         ("gone", "손노트 복소화 쪽 · 피드백 §7 (factor 2) — 8장의 정규화 convention이 같은 경고를 담는다")],
    refs=[("conv", "5")] + ex("5", "P003", "P008", "P065", "P066", "P068", "P070"),
    check="$\\langle\\partial_z n,\\partial_z n\\rangle=0$ (손노트에서 멈췄던 그 계산)"))

CH.append(dict(num=3, title="쌍곡 보충 — 상반평면·원판·Cayley",
    intro="메인 축 밖의 보충 트랙. 곡률이 $-1$인 세계를 guided로 한 번 만져보고 돌아온다. 202제에서는 뺀 내용이라 LRG 원문 3제가 전부다.",
    see=[("note", "202제에서 뺀 트랙 — 아래 LRG 원문 3제로만 커버")],
    refs=lr(5, 6, 7),
    check="$K=-1$ · Cayley가 경계를 경계로"))

CH.append(dict(num=4, title="Christoffel·공변미분·측지선",
    intro="곡면 위에서 벡터를 미분하면 답이 곡면을 살짝 떠난다. 떠난 만큼을 도로 곡면에 사영하는 것이 공변미분이고, Christoffel 기호는 그 회계장부다. 값 대입(①B)으로 감을 잡고 LRG guided로 정식 유도를 밟는다.",
    see=[("in", "LRG 맨 앞 Basic Formulas — 아래 인라인")],
    refs=[("lrgfront",)] + ex("1", "B02", "B01", "B03") + lr(24, 25, 22, 23, 30, 31),
    check="$\\nabla_{\\partial_\\theta}\\partial_\\theta=0$ · 대원이 측지선"))

CH.append(dict(num=5, title="Lie bracket·flow·Killing",
    intro="흐름(flow)으로 벡터장을 밀 때 무엇이 변하고(Lie derivative) 무엇이 안 변하는가(Killing). $S^1$ 작용 — Hopf 올의 회전 — 이 다음 장들의 주인공이므로, 여기서 그 언어를 깐다.",
    see=[("gone", "피드백 §3 ($S^1$ action이 왜 중요한지) — 9장 인트로에 요지")],
    refs=lr(9, 10, 11, 12, 13) + ex("2", "E1", "E2", "E3", "E4", "E5"),
    check="회전장 $[X,Y]$ 부호 · $L_k$가 Hopf fiber 방향"))

CH.append(dict(num=6, title="Quaternion·Hopf·SU(2)→SO(3)",
    intro="사원수 곱셈 한 줄 $h(q)=qkq^{-1}$로 $S^3\\to S^2$ (Hopf)와 SU(2)→SO(3) 2:1 덮개를 손으로 만든다. $2\\pi$ 돌리면 $-1$, $4\\pi$ 돌려야 $1$ — 그 유명한 사실이 D7에서 손계산으로 나온다.",
    see=[("in", "② 상단 convention ($ij=k$ 규칙) — 아래 인라인"),
         ("gone", "손노트 Pauli 고유벡터 표 — 보충 문제(⑤ Part E 손노트 복습)가 같은 내용을 재구성")],
    refs=[("conv", "2")] + ex("2", "A0", "A1", "A2", "A3", "A4", "A5", "A6",
                              "B1", "B2", "B3", "C2", "C3", "C4", "C6",
                              "D1", "D2", "D6", "D7", "D3", "D4", "D5"),
    extra=ex("2", "F2", "F4", "F5") + ex("5", "P049", "P051", "P058", "P060", "P062"),
    extra_note="②Part F(미분 pushforward)와 ⑤Part E(손노트 복습: Pauli·Bloch·Hopf)는 네비게이터 경로에 없던 원문 문제들이다. 이 장 주제의 연장이라 여기 둔다.",
    check="$h(-q)=h(q)$ · 세 번째 열 = Hopf map"))

CH.append(dict(num=7, title="Contact form·connection·Euler number",
    intro="$S^3$ 위의 1-형식 $\\alpha$ 하나가 아래 구면의 넓이를 기억한다: $d\\alpha=2\\,dA_{FS}$. 그 factor 2가 이 책 전체에서 가장 사고가 잦은 지점이다. 마지막에 Euler number $-1$까지.",
    see=[("in", "③ §0 정규화 경고 — 전문은 8장 인라인; 요지: $d\\alpha=2dA_{FS}$, factor 2 사고다발지역")],
    refs=lr(12) + ex("2", "G1", "G2", "G3", "G4", "G5", "H3", "H4", "H5", "H6", "I1", "I2") + lr(32),
    check="$\\int\\omega_{FS}=2\\pi$인데 Hopf Euler number는 $-1$ (부호·factor 구분)"))

CH.append(dict(num=8, title="QFIM 세 방식 — state vector / projector / Bloch",
    intro="이 책의 심장. 같은 양자정보계량을 <b>상태벡터 미분 / 사영자 $\\mathrm{Tr}(dP\\,dP)$ / Bloch 벡터 $|d\\vec n|^2$</b> 세 길로 계산해서 한 답 $4/D^2$에 수렴시킨다. 장 끝의 사례연구는 실제 손계산(Notes_260704)이 어디서 왜 멈췄는지를 줄 단위로 보여준다.",
    see=[("in", "③ §0 정규화 convention (Assertion 1–5 + 경고) — 아래 인라인"),
         ("in", "⑤ convention — 2장에 인라인"),
         ("gone", "QFIM노트 §2–9 · 피드백 §3, §7 (제외) — 규약·문제·사례연구가 대체"),
         ("case", "손노트 사례연구 — 이 장 끝 박스 + 부록 C + 걸음 문서 5")],
    refs=[("conv", "3")] + ex("3", "P001", "P002", "P003", "P004", "P007", "P008", "P009",
                              "P012", "P013", "P014", "P015", "P017", "P018", "P019",
                              "P021", "P022", "P023", "P024", "P025", "P026", "P028",
                              "P031", "P037", "P032", "P033", "P034", "P035", "P036", "P038")
         + ex("5", "P031", "P033", "P037", "P040", "P044", "P036", "P105") + [("case8",)],
    extra=ex("3", "P005", "P020", "P030") + ex("5", "P021", "P028"),
    extra_note="③P005·P020·P030, ⑤P021(QFIM 정의 유도)·P028(gauge 불변)은 네비게이터 경로 밖의 원문 문제. 특히 ⑤P021·P028은 이 장의 공식이 <i>왜</i> 성립하는지를 캐는 문제라 먼저 풀어도 좋다.",
    check="$4/D^2$가 세 방식에서 모두 · $H_{xy}=0$ · $\\mathrm{Tr}(dPdP)=\\tfrac12\\langle dp,dp\\rangle$"))

CH.append(dict(num=9, title="껍데기 기하 — II·submersion (세미나 확인과제)",
    intro="계량(I)이 같아도 껍데기의 굽음(II)은 다를 수 있다 — 세미나 피드백의 본체. 반지름 $r$ 구면의 $\\mathrm{II}=(1/r)\\mathrm{I}$을 직접 재고, $VV^*$가 이미 $S^1$ 몫공간을 수행한다는 것(리만 submersion)을 확인한다. 피드백 §3의 요지: $S^1$ 작용은 게이지(위상) 방향이고, 계량은 그 방향에 수직인 곳에서만 정보를 갖는다.",
    see=[("gone", "피드백 §2, §3 (제외) — 아래 P101–P103이 바로 그 확인과제")],
    refs=lr(22, 33) + ex("5", "P101") + lr(10, 13) + ex("5", "P102", "P103"),
    check="$\\mathrm{II}=(1/r)\\mathrm{I}$ · vertical 방향 $=i\\psi$"))

CH.append(dict(num=10, title="곡률 K 삼중검산",
    intro="곡률 하나를 네 가지 방법(복소공식 / Gauss–Bonnet / QFIM 규격 / 곡률텐서)으로 재서, 규격 차이(단위구면 $K=1$ vs FS $K=4$)를 몸에 박는다.",
    see=[("gone", "피드백 §2 (곡률은 II에서 온다) — 9장 인트로 참조")],
    refs=ex("3", "P070", "P073") + ex("5", "P070") + lr(36),
    extra=ex("3", "P076"),
    extra_note="③P076('두 개의 2 구분')은 경로 밖 원문 문제 — 이 장의 규격 감각을 그대로 시험한다.",
    check="네 방법 모두 $K=1$ (단위구면 규격) · FS 규격이면 $K=4$"))

CH.append(dict(num=11, title="고전 Fisher·Bernoulli·mixed state (IG 다리)",
    intro="고전 통계의 Fisher 정보와 QFIM 사이의 다리. Bernoulli 한 번 던지기에서 시작해, 구면 위 확률질량($4\\times$round), mixed qubit Bures까지. pure 극한에서 radial 방향이 발산하는 것이 rank가 떨어지는 신호다.",
    see=[("gone", "IG 과제 Problem 6, 10, 18, 20 (Bregman 과제 PDF — 제외) · 피드백 §6 — 아래 P095·P104가 해당 확인계산")],
    refs=lr(28) + ex("3", "P079", "P080") + ex("5", "P095", "P104")
         + ex("3", "P041", "P042", "P043", "P044"),
    extra=ex("3", "P084") + ex("5", "P097"),
    extra_note="③P084($\\theta$-방향 QFI)와 ⑤P097(측정이 주는 classical Fisher vs QFIM, $F\\le H$)은 경로 밖 원문 문제 — mixed qubit 뒤에 이어 풀면 맞다.",
    check="$\\psi''=p(1-p)$ · Fisher $=4\\times$round · pure 극한에서 radial 발산"))

CH.append(dict(num=12, title="$\\mathbb{CP}^n$ 일반화·product state",
    intro="1-qubit에서 $n$-qubit로: 같은 공식이 $\\mathbb{CP}^{N-1}$에서 문자 그대로 돌아간다. $H=4\\mathrm{Var}$ — QFIM이 왜 '정보'인지의 답. product state 부분다양체가 못 보는 방향이 얽힘 방향이다.",
    see=[("gone", "QFIM노트 §11–12 (제외) — ⑤ Part G 문제들이 그 계산 판")],
    refs=ex("5", "P072", "P073", "P076", "P074", "P082")
         + ex("3", "P094", "P095", "P096", "P097"),
    extra=ex("3", "P086"),
    extra_note="③P086(fidelity 전개)은 경로 밖 원문 문제.",
    check="$N=2$에서 $4/D^2$ 복원 · 원점에서 $H=4I$"))

CH.append(dict(num=13, title="Veronese·$\\mathbb{CP}^5$ — Plücker 준비",
    intro="Gr(2,4)에 오르기 전 마지막 사다리. Veronese로 $\\mathbb{CP}^1$을 $\\mathbb{CP}^m$에 넣으면 계량이 정확히 $m$배가 되는 것을 $m=1..5$로 손계산하고, $\\mathbb{CP}^5$ FS에 익숙해진다.",
    see=[("in", "④ §0 convention (식 0.1, 0.2) — 아래 인라인")],
    refs=[("conv", "4")] + ex("4", "P001", "P007", "P008", "P010", "P002", "P003", "P004", "P006",
                              "P011", "P012", "P016", "P017",
                              "P024", "P025", "P026", "P027", "P028",
                              "P031", "P033", "P038", "P032"),
    check="normalize 전후 scaling 차이 (P020 계열의 함정)"))

CH.append(dict(num=14, title="Grassmannian·Plücker·Gr(2,4) — 최종 목적지",
    intro="폴더 이름이 목적지다. 접공간(block 행렬) → Plücker 좌표 → Klein quadric → $p_{12}\\ne0$ chart → matrix metric·Kähler potential $\\log\\det(I+Z^\\dagger Z)$ 순서로 오른다. $\\mathbb{CP}^1$에서 한 모든 계산의 각 부품이 행렬 하나씩으로 승격된다.",
    see=[("gone", "QFIM노트 §13–17 · Reineke 연결 코멘트 · 피드백 §8 (제외)"),
         ("case", "완성 손계산: 걸음 문서 5 (같은 폴더 정리_L0-L6/손계산_걸음별/) — 이 장 끝 요지 박스")],
    refs=ex("5", "P083", "P085", "P086", "P088", "P091", "P089", "P090")
         + ex("4", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049")
         + ex("4", "P051", "P053", "P052", "P056", "P059", "P058", "P060")
         + ex("4", "P063", "P064", "P065", "P066", "P067") + lr(27)
         + ex("4", "P076", "P084", "P085", "P088") + lr(26, 28) + [("case14",)],
    extra=ex("4", "P050"),
    extra_note="④P050(차원 세기)은 경로 밖 원문 문제 — quadric 다음에 풀면 맞다.",
    check="$\\mathrm{Gr}(1,2)=\\mathbb{CP}^1$로 후퇴시켜 $4/D^2$ 복원 · $\\dim_{\\mathbb R}\\mathrm{Gr}(2,4)=8$"))

CH.append(dict(num=15, title="푸리에 병렬 트랙 (독립)",
    intro="메인 축과 독립인 손풀기 30제. 막힌 날의 시동용. 예외: winding form 문제(71–74)는 7장(Euler number)과 같은 시기가 좋다. 정답 키는 각 문제 아래 접어 두었다.",
    see=[("note", "원본 Ⓕ 파일 자체로 완결 (정답 키 포함) — 전체를 이 장에 인라인")],
    refs=[("fourier",)],
    check="각 문제 아래 정답 키 참조"))

# leftover coverage check
used = set()
for ch in CH:
    for r in ch.get("refs", []) + ch.get("extra", []):
        if r[0] == "p":
            used.add((r[1], r[2]))
if True:
    allf = set((s, i) for (s, i) in problems if s == "F")
    used |= allf  # fourier chapter includes all
left = [k for k in order if k not in used]
print("uncovered problems:", left)

# ------------------------------------------------------- PART C: md -> html
import markdown as mdlib

def md2html(text):
    if not text:
        return ""
    mathblocks = []
    def stash(m):
        mathblocks.append(m.group(0))
        return f"⟪M{len(mathblocks)-1}⟫"
    text = re.sub(r"\$\$.*?\$\$", stash, text, flags=re.S)
    text = re.sub(r"\$[^$\n]+\$", stash, text)
    h = mdlib.markdown(text, extensions=["tables"])
    def unstash(m):
        raw = mathblocks[int(m.group(1))]
        return raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    h = re.sub(r"⟪M(\d+)⟫", unstash, h)
    return h

TAGCLS = {"W": "w", "★": "s1", "★★": "s2"}
TAGLBL = {"W": "W 웜업", "★": "★ 본운동", "★★": "★★ 도전"}

rendered_once = set()

def prob_html(stage_, pid):
    p = problems[(stage_, pid)]
    key = (stage_, pid)
    again = key in rendered_once
    rendered_once.add(key)
    disp = f"{CIRC[stage_]}{pid}"
    prov = (f"1단계 {p['part']}절" if stage_ == "1" else
            f"병렬 Part {p['fpart']}" if stage_ == "F" else
            f"{stage_}단계 Part {p['part']}")
    out = [f'<article class="prob" id="p-{stage_}-{pid}">']
    out.append('<div class="phead">'
               f'<span class="tag {TAGCLS[p["tag"]]}">{TAGLBL[p["tag"]]}</span>'
               f'<span class="pid">{disp}</span>'
               f'<span class="ptitle">{html.escape(p["title"])}</span>'
               + ('<span class="again">재등장</span>' if again else '')
               + f'<span class="prov">{prov}</span></div>')
    if p.get("setup"):
        out.append(f'<div class="setup"><div class="setuplbl">필요한 정의</div>{md2html(p["setup"])}</div>')
    out.append(f'<div class="pbody">{md2html(p["body"])}</div>')
    ans = None
    if stage_ == "1":
        ans = answers1.get(pid)
    elif stage_ == "F":
        ans = fourier_key.get(int(pid))
    if ans:
        out.append(f'<details class="ans"><summary>검산 정답</summary><div>{md2html(ans)}</div></details>')
    out.append("</article>")
    return "\n".join(out)

def lrg_html(n):
    again = ("L", n) in rendered_once
    rendered_once.add(("L", n))
    b = lrg[n]["body"]
    return (f'<article class="prob lrgp" id="lrg-{n}"><div class="phead">'
            f'<span class="tag lrg">LRG</span><span class="pid">LRG {n}</span>'
            + ('<span class="again">재등장</span>' if again else '')
            + '<span class="prov">교수님 리만기하 PDF (원문)</span></div>'
            f'<div class="pbody">{md2html(b)}</div></article>')

def conv_html(stage_):
    if stage_ == "1":
        body = stage_intro.get("1", "")
        label = "① 1단계 상단 고정 규칙 (원문)"
    else:
        body = (stage_intro.get(stage_, "") + "\n\n" + stage_conv.get(stage_, "")).strip()
        label = f"{CIRC[stage_]} {stage_}단계 convention (원문)"
    return (f'<div class="conv"><div class="convlbl">{label}</div>{md2html(body)}</div>')

CASE8 = """
<div class="case"><div class="caselbl">사례연구 — 남극사영 손계산이 멈춘 세 지점 (Notes 26-07-04)</div>
<p>이 장의 P012–P017을 실제 손으로 갔던 계산이 세 곳에서 깨졌다. 셋 다 이 장의 규약으로 즉시 잡힌다.</p>
<table><thead><tr><th></th><th>깨진 줄</th><th>증상 / 검출법</th></tr></thead><tbody>
<tr><td><b>E1</b></td><td>입체사영 $z=\\dfrac{e^{i\\theta_1}}{1+\\cos\\theta_2}$ — 분자의 $\\sin\\theta_2$ 누락 (P017의 $w=e^{i\\phi}\\tan\\frac\\theta2$가 정답)</td><td>북극($\\theta_2=0$)이 원점이 아니라 $z=\\tfrac12e^{i\\theta_1}$로 간다</td></tr>
<tr><td><b>E2</b></td><td>정규화 $\\dfrac{1}{1+|z|^2}$ — 제곱근 누락</td><td>$\\|\\psi\\|^2=\\dfrac{c^2}{1+c^2}\\ne1$ (Assertion 1 위반, $c=1+\\cos\\theta_2$)</td></tr>
<tr><td><b>E3</b></td><td>$\\mathrm{Re}[(\\partial_1\\psi)^*\\psi\\cdot\\psi^*(\\partial_1\\psi)]$에서 분모 $(1+c^2)^2$ 하나 증발</td><td>$H_{11}=\\frac{4(c^2-c^4)}{(1+c^2)^2}&lt;0$ — $H=4\\mathrm{Var}\\ge0$ (⑤P082)과 모순</td></tr>
</tbody></table>
<p>세 줄을 고치면 $\\psi=(\\cos\\frac{\\theta_2}2,\\ e^{i\\theta_1}\\sin\\frac{\\theta_2}2)$ (P012의 상태), $H=\\mathrm{diag}(\\sin^2\\theta_2,\\,1)$, $H_{12}=0$. 그리고 손노트의 마지막 관찰 "여튼 복소부가 있기는 하다"는 옳았다 — $Q_{12}=-\\tfrac i4\\sin\\theta_2$의 허수부가 FS 넓이형식(= Berry curvature의 절반, $d\\alpha=2dA_{FS}$의 그 factor)이다. 전체 전개·sympy 검산: <b>걸음 문서 5</b> (정리_L0-L6/손계산_걸음별/5_QFIM_남극사영_완성_Gr24.md).</p></div>
"""

CASE14 = """
<div class="case"><div class="caselbl">완성 계산 요지 — Gr(2,4)의 양자정보계량 (걸음 문서 5 §4, sympy 검산 완료)</div>
<p>$\\mathbb{CP}^1$의 $S=1+|z|^2$ 자리에 $\\det(I+Z^\\dagger Z)=1+\\sum_{ij}|z_{ij}|^2+|\\det Z|^2$가 들어오는 것이 유일한 변화다.</p>
$$ds^2_{QFIM}=2\\,\\mathrm{Tr}(dP\\,dP)=4\\,\\mathrm{Re}\\,\\mathrm{Tr}\\!\\left[(I+Z^\\dagger Z)^{-1}dZ^\\dagger\\,(I+ZZ^\\dagger)^{-1}dZ\\right]$$
<p>이 값 = Plücker(2-fermion Slater) 순수상태의 QFIM (무작위 곡선 수치검산 상대오차 $\\sim10^{-11}$). $\\rho=P/2$ 혼합으로 읽으면 정확히 절반. $\\mathrm{Gr}(1,2)$로 후퇴시키면 $4/D^2$ 복원 — 이 장의 검산 기준 그대로.</p></div>
"""

def see_html(items):
    rows = []
    ICON = {"in": "✓ 인라인", "gone": "✕ 제외 문서", "note": "·", "case": "★ 사례"}
    for kind, txt in items:
        rows.append(f'<li class="see-{kind}"><span class="seeicon">{ICON[kind]}</span> {txt}</li>')
    return '<div class="seebox"><div class="seelbl">볼 것 — 이 판에서의 상태</div><ul>' + "".join(rows) + "</ul></div>"

def fourier_html():
    out = []
    cur_p = None
    for (s, i_) in order:
        if s != "F":
            continue
        p = problems[(s, i_)]
        if p["fpart"] != cur_p:
            cur_p = p["fpart"]
            title = next((t for n, t in fourier_parts if n == cur_p), "")
            out.append(f'<h3 class="fpart">Part {cur_p}. {html.escape(title)}</h3>')
        out.append(prob_html("F", i_))
    extras = sorted(set(fourier_key) - set(int(i_) for (s, i_) in problems if s == "F"))
    if extras:
        items = "".join(f"<li><b>{n}.</b> {md2html(fourier_key[n])}</li>" for n in extras)
        out.append('<div class="conv"><div class="convlbl">정답 키의 나머지 항목 (원문 그대로 — 이 선별판에 해당 문제가 없는 번호)</div><ul>'
                   + items + "</ul></div>")
    return "\n".join(out)

# ------------------------------------------------------- PART D: assemble
toc = []
chapters_html = []
for ch in CH:
    n = ch["num"]
    cnt = sum(1 for r in ch["refs"] + ch.get("extra", []) if r[0] == "p") + \
          sum(1 for r in ch["refs"] if r[0] == "lrg") + \
          (30 if any(r[0] == "fourier" for r in ch["refs"]) else 0)
    toc.append(f'<li><a href="#ch{n}"><span class="tocn">{n}장</span> {ch["title"]}<span class="toccnt">{cnt}문제</span></a></li>')
    parts = [f'<section class="chapter" id="ch{n}">',
             f'<h2><span class="chn">{n}장</span> {ch["title"]}</h2>',
             f'<p class="chintro">{ch["intro"]}</p>',
             see_html(ch["see"])]
    parts.append(f'<div class="checkbox"><span class="checklbl">검산 기준</span> {ch["check"]}</div>')
    for r in ch["refs"]:
        if r[0] == "p":
            parts.append(prob_html(r[1], r[2]))
        elif r[0] == "lrg":
            parts.append(lrg_html(r[1]))
        elif r[0] == "conv":
            parts.append(conv_html(r[1]))
        elif r[0] == "lrgfront":
            parts.append(f'<div class="conv"><div class="convlbl">LRG Basic Formulas (원문)</div>{md2html(lrg_front)}</div>')
        elif r[0] == "case8":
            parts.append(CASE8)
        elif r[0] == "case14":
            parts.append(CASE14)
        elif r[0] == "fourier":
            parts.append(fourier_html())
    if ch.get("extra"):
        parts.append(f'<h3 class="extrah">보충 — 경로 밖 원문 문제</h3><p class="extranote">{ch.get("extra_note","")}</p>')
        for r in ch["extra"]:
            parts.append(prob_html(r[1], r[2]))
    parts.append("</section>")
    chapters_html.append("\n".join(parts))

print("chapters assembled:", len(chapters_html))

# ------------------------------------------------------- PART E: front/back matter
p1 = read("part1_p01-12.md")
p2raw = read("part2_p13-24.md")

def section(lines_, start_pat, end_pat=None):
    out, on = [], False
    for ln in lines_:
        if re.match(start_pat, ln):
            on = True
            continue
        if on and end_pat and re.match(end_pat, ln):
            break
        if on:
            out.append(ln)
    return "\n".join(l for l in out if not PAGE_MARK.match(l)).strip()

usage_src = section(p1, r"^## Gr\(2,4\) — 메인 축", r"^## 교수님")
common_rules = section(p1, r"^### 공통 규칙", r"^---")
lrgmap_a = section(p1, r"^## 교수님")
lrgmap_b = section(p2raw, r"\A", r"^## 202제 연계표")
lrgmap_b = "\n".join(l for l in p2raw[: next(i for i, l in enumerate(p2raw) if l.startswith("## 202제"))]
                     if not PAGE_MARK.match(l)).strip()

FRONT = """
<header class="titlepage">
<p class="series">study metric — Gr(2,4) 트랙</p>
<h1>Gr(2,4) 핵심계산</h1>
<p class="subtitle">주제별 완전판 — 원문 202제 + 병렬 30제 + LRG 발췌 22제, 참조 없이 한 권으로</p>
<p class="edition">원전: <i>Gr24_핵심계산모음.pdf</i> (94쪽) · 이 판은 문제 원문을 그대로 두고 <b>배치만</b> 주제별 15장으로 재편성했다.<br>
편집: Claude (2026-07-09) · 검산 사례연구는 걸음 문서 5와 연동</p>
</header>

<section class="chapter" id="preface">
<h2><span class="chn">머리말</span> 이 판에서 바뀐 것</h2>
<p>원전(모음집)은 문제를 <b>출처 파일 순서(1–5단계)</b>로 담고, 주제별 네비게이터가 "몇 단계 몇 번"을 가리키는 구조였다. 이 판은 그 네비게이터의 주제 15개를 그대로 <b>장(章)</b>으로 삼고, 가리키던 문제의 <b>원문 전체를 해당 장에 옮겨 심었다</b>. 따라서:</p>
<ul>
<li>각 장은 <b>볼 것</b>(규약 — 원문 인라인) → <b>풀 것</b>(문제 원문, 네비게이터의 순서 그대로) → <b>검산 기준</b>으로 완결된다. 다른 파일을 열 일이 없다.</li>
<li>네비게이터가 참조하던 <b>LRG(교수님 리만기하 PDF)</b> 문제 22개는 영어 원문 그대로 발췌해 넣었다. 제외된 문서(QFIM노트·피드백·IG 과제)를 가리키던 자리는 각 장 "볼 것" 박스에 상태를 명시했다.</li>
<li>문제 번호는 원전 그대로, 앞에 출처 단계만 붙였다: <b>①A01</b>(1단계) ··· <b>⑤P105</b>(5단계), <b>Ⓕ</b>(병렬). 원전과 1:1 대조 가능하다.</li>
<li>네비게이터 경로에 없던 원문 문제들은 버리지 않고 가장 가까운 장의 <b>보충</b> 절에 두었다 — 202+30문제 전부가 이 책 안에 있다.</li>
<li>8장에는 실제 손계산(Notes 26-07-04)이 멈춘 세 지점의 <b>사례연구</b>를, 14장에는 <b>완성된 Gr(2,4) 계량의 요지</b>를 박스로 넣었다 (전문: 걸음 문서 5).</li>
</ul>
<div class="checkbox"><span class="checklbl">규약 지뢰 3개 (원전 '사용 규칙'에서)</span> FS vs QFIM의 factor 4 · $d\\alpha=2dA_{FS}$ · $\\mathrm{Tr}(dPdP)=\\tfrac12\\langle dp,dp\\rangle$ — 3·5단계 출신 문제에 반복 배치되어 있으니 그때마다 검산할 것.</div>
</section>

<section class="chapter" id="howto">
<h2><span class="chn">사용법</span> 원전의 규칙 (원문)</h2>
__USAGE__
<h3>공통 규칙 (네비게이터 원문)</h3>
__COMMON__
</section>
"""
FRONT = FRONT.replace("__USAGE__", md2html(usage_src)).replace("__COMMON__", md2html(common_rules))

APPENDIX = """
<section class="chapter" id="appA">
<h2><span class="chn">부록 A</span> LRG 50문제 난이도 맵 (원문)</h2>
__LRGA__
__LRGB__
</section>

<section class="chapter" id="appB">
<h2><span class="chn">부록 B</span> 원전 ↔ 이 판 대응</h2>
<p>원전의 단계·Part가 이 판의 어느 장으로 갔는지의 지도. (개별 문제는 본문 각 문제의 출처 칩으로 확인.)</p>
<table><thead><tr><th>원전</th><th>이 판</th></tr></thead><tbody>
<tr><td>1단계 A·D·F·G절</td><td>1장</td></tr><tr><td>1단계 B절</td><td>4장</td></tr>
<tr><td>2단계 A–D + F</td><td>6장</td></tr><tr><td>2단계 E</td><td>5장</td></tr><tr><td>2단계 G–I</td><td>7장</td></tr>
<tr><td>3단계 A–D</td><td>8장 (P041–P044는 11장)</td></tr><tr><td>3단계 G</td><td>10장</td></tr><tr><td>3단계 H</td><td>11장</td></tr><tr><td>3단계 I</td><td>12장</td></tr>
<tr><td>4단계 A–D</td><td>13장</td></tr><tr><td>4단계 E–I</td><td>14장</td></tr>
<tr><td>5단계 A·F</td><td>2장</td></tr><tr><td>5단계 C·D</td><td>8장</td></tr><tr><td>5단계 E</td><td>6장 보충</td></tr><tr><td>5단계 G</td><td>12장</td></tr><tr><td>5단계 H</td><td>14장</td></tr><tr><td>5단계 I</td><td>11장</td></tr><tr><td>5단계 J</td><td>9장 (P104→11장, P105→8장)</td></tr>
<tr><td>병렬 트랙 (푸리에)</td><td>15장</td></tr>
</tbody></table>
<p>원전에서 이 판이 <b>바꾸지 않은 것</b>: 문제 본문·난이도 태그·번호·정답 키·규약 문구(전부 원문). <b>바꾼 것</b>: 배치(주제별), 외부 참조의 인라인화, 장 도입문·사례연구 박스(편집자 추가, 박스로 구분됨).</p>
</section>

<section class="chapter" id="appC">
<h2><span class="chn">부록 C</span> 사례연구 전문 포인터</h2>
<p>8장 사례연구(E1·E2·E3)와 14장 완성 요지의 전체 전개 — 남극 입체사영 유도, 내적 다섯 개, $H=\\mathrm{diag}(\\sin^2\\theta_2,1)$, 복소부=Kähler/Berry, $\\mathrm{Gr}(2,4)$ 닫힌형과 sympy 검산 로그 — 는 같은 폴더의</p>
<p style="text-align:center"><b>정리_L0-L6/손계산_걸음별/5_QFIM_남극사영_완성_Gr24.md</b> (+ <b>verify5_qfim.py</b>)</p>
<p>에 있다. 이 책의 8장 P012–P017, 12장 P074·P082, 14장 P083–P091이 그 문서의 손계산 재료다.</p>
</section>
"""
APPENDIX = APPENDIX.replace("__LRGA__", md2html(lrgmap_a)).replace("__LRGB__", md2html(lrgmap_b))

# ------------------------------------------------------- PART F: shell + emit
# KaTeX 는 공유 자산(assets/)을 링크한다 — 페이지마다 인라인하지 않는다.
NAV_CSS = """
.sitenav{position:sticky;top:0;z-index:50;display:flex;gap:1em;align-items:center;
padding:.5em 1.2em;background:var(--bg);border-bottom:1px solid var(--line);font-size:.95em}
.sitenav a.home{color:var(--accent);text-decoration:none;font-weight:700;white-space:nowrap}
.sitenav a.home:hover{text-decoration:underline}
.sitenav .navtitle{color:var(--muted);font-size:.88em;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sitenav-bottom{max-width:46em;margin:0 auto;padding:0 1.2em 3em;text-align:center}
.sitenav-bottom a{color:var(--accent);text-decoration:none;font-weight:600}
"""

CSS = """
:root{--bg:#faf8f4;--fg:#1e1e20;--muted:#6b6862;--line:#ddd8ce;--card:#fff;--accent:#8a3033;
--w:#2c7a3d;--s1:#245a8f;--s2:#a33d2a;--lrg:#6a4a8a;--box:#f3efe6;--case:#fdf3e4;--casebd:#e0b36a}
@media (prefers-color-scheme: dark){:root{--bg:#191a1c;--fg:#e8e6e1;--muted:#96938c;--line:#3a3b3e;
--card:#222326;--accent:#e0888a;--w:#7bc78c;--s1:#8ab8e8;--s2:#e8987f;--lrg:#b79ad6;--box:#26272b;--case:#2b2620;--casebd:#8a6a35}}
:root[data-theme="light"]{--bg:#faf8f4;--fg:#1e1e20;--muted:#6b6862;--line:#ddd8ce;--card:#fff;--accent:#8a3033;
--w:#2c7a3d;--s1:#245a8f;--s2:#a33d2a;--lrg:#6a4a8a;--box:#f3efe6;--case:#fdf3e4;--casebd:#e0b36a}
:root[data-theme="dark"]{--bg:#191a1c;--fg:#e8e6e1;--muted:#96938c;--line:#3a3b3e;
--card:#222326;--accent:#e0888a;--w:#7bc78c;--s1:#8ab8e8;--s2:#e8987f;--lrg:#b79ad6;--box:#26272b;--case:#2b2620;--casebd:#8a6a35}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font-family:"Noto Serif KR","Source Serif Pro",Georgia,"Apple SD Gothic Neo","Malgun Gothic",serif;
line-height:1.72;font-size:16.5px}
main{max-width:46em;margin:0 auto;padding:2em 1.2em 6em}
.titlepage{max-width:46em;margin:0 auto;padding:4.5em 1.2em 2em;text-align:center;border-bottom:3px double var(--line)}
.titlepage h1{font-size:2.6em;margin:.2em 0;letter-spacing:.04em}
.series{color:var(--muted);letter-spacing:.2em;font-size:.85em;margin:0}
.subtitle{font-size:1.05em;color:var(--fg)}
.edition{color:var(--muted);font-size:.85em;margin-top:1.4em}
nav.toc{max-width:46em;margin:0 auto;padding:1.5em 1.2em}
nav.toc h2{font-size:1.1em;letter-spacing:.15em;color:var(--muted)}
nav.toc ol{list-style:none;padding:0;margin:0}
nav.toc li{border-bottom:1px dotted var(--line)}
nav.toc a{display:flex;gap:.7em;align-items:baseline;color:var(--fg);text-decoration:none;padding:.42em .2em}
nav.toc a:hover{color:var(--accent)}
.tocn{color:var(--accent);font-weight:700;min-width:3.2em}
.toccnt{margin-left:auto;color:var(--muted);font-size:.8em}
.chapter{margin-top:4em}
h2{font-size:1.55em;border-bottom:2px solid var(--line);padding-bottom:.3em;margin-top:0}
.chn{display:inline-block;color:var(--accent);margin-right:.5em;font-size:.75em;vertical-align:.12em;letter-spacing:.1em}
.chintro{font-size:1.02em}
h3{margin-top:2.2em;font-size:1.15em}
h3.fpart{border-bottom:1px solid var(--line);padding-bottom:.2em}
.seebox,.conv,.checkbox,.case,.setup{border-radius:8px;margin:1.3em 0;padding:.9em 1.1em}
.seebox{background:var(--box);border:1px solid var(--line)}
.seelbl,.convlbl,.setuplbl,.caselbl{font-weight:700;font-size:.85em;letter-spacing:.08em;color:var(--muted);margin-bottom:.4em}
.seebox ul{margin:.3em 0 0;padding-left:1.1em;list-style:none}
.seebox li{margin:.2em 0}
.seeicon{font-size:.8em;color:var(--muted);margin-right:.3em}
.conv{background:var(--box);border:1px solid var(--line)}
.checkbox{background:transparent;border:1.5px dashed var(--accent)}
.checklbl{font-weight:700;color:var(--accent);margin-right:.5em;font-size:.9em}
.case{background:var(--case);border:1.5px solid var(--casebd)}
.caselbl{color:var(--casebd)}
article.prob{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:1.4em 0;padding:1em 1.25em;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.phead{display:flex;align-items:baseline;gap:.6em;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:.5em;margin-bottom:.7em}
.tag{font-size:.72em;font-weight:700;padding:.12em .55em;border-radius:99px;color:#fff;white-space:nowrap}
.tag.w{background:var(--w)}.tag.s1{background:var(--s1)}.tag.s2{background:var(--s2)}.tag.lrg{background:var(--lrg)}
.pid{font-weight:700;color:var(--accent)}
.ptitle{font-weight:600}
.again{font-size:.72em;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:.08em .5em}
.prov{margin-left:auto;font-size:.72em;color:var(--muted)}
.setup{background:var(--box);border-left:3px solid var(--lrg);border-radius:4px}
details.ans{margin-top:.7em;border-top:1px dotted var(--line);padding-top:.5em}
details.ans summary{cursor:pointer;color:var(--accent);font-size:.88em;font-weight:600}
details.ans>div{padding:.4em 0 .1em}
.extrah{color:var(--muted)}
.extranote{color:var(--muted);font-size:.9em}
table{border-collapse:collapse;margin:1em 0;width:100%;font-size:.93em}
th,td{border:1px solid var(--line);padding:.4em .6em;text-align:left;vertical-align:top}
th{background:var(--box)}
.tablewrap{overflow-x:auto}
blockquote{border-left:3px solid var(--line);margin:1em 0;padding:.1em 1em;color:var(--muted)}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.2em 0}
hr{border:none;border-top:1px solid var(--line)}
a{color:var(--accent)}
@media print{body{font-size:11pt;background:#fff;color:#000}
article.prob{break-inside:avoid;box-shadow:none}
details.ans{display:block}details.ans[open],details.ans{}
nav.toc a{color:#000}.chapter{margin-top:2em}}
"""

toc_full = "\n".join(toc) + """
<li><a href="#appA"><span class="tocn">부록A</span> LRG 50문제 난이도 맵</a></li>
<li><a href="#appB"><span class="tocn">부록B</span> 원전 ↔ 이 판 대응</a></li>
<li><a href="#appC"><span class="tocn">부록C</span> 사례연구 전문 포인터</a></li>"""

html_doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Gr(2,4) 핵심계산 — 주제별 완전판</title>
<link rel="stylesheet" href="assets/katex.min.css">
<style>{CSS}</style>
<style>{NAV_CSS}</style>
</head>
<body>
<nav class="sitenav"><a class="home" href="index.html">← 목록</a><span class="navtitle">Gr(2,4) 핵심계산 — 주제별 완전판</span></nav>
{FRONT.split('<section class="chapter" id="preface">')[0]}
<nav class="toc"><h2>차례</h2><ol>
<li><a href="#preface"><span class="tocn">머리말</span> 이 판에서 바뀐 것</a></li>
<li><a href="#howto"><span class="tocn">사용법</span> 원전의 규칙</a></li>
{toc_full}
</ol></nav>
<main>
<section class="chapter" id="preface">{FRONT.split('<section class="chapter" id="preface">')[1].split('</section>')[0]}</section>
{'<section class="chapter" id="howto">' + FRONT.split('<section class="chapter" id="howto">')[1]}
{"".join(chapters_html)}
{APPENDIX}
<footer style="margin-top:5em;color:var(--muted);font-size:.85em;border-top:1px solid var(--line);padding-top:1em">
Gr(2,4) 핵심계산 — 주제별 완전판 · 원전: Gr24_핵심계산모음.pdf · 문제 원문 무변경, 배치·인라인화만 편집 · 2026-07-09
</footer>
</main>
<div class="sitenav-bottom"><a href="index.html">← 목록으로 돌아가기</a></div>
<script defer src="assets/katex.min.js"></script>
<script defer src="assets/auto-render.min.js"></script>
<script defer src="assets/render.js"></script>
</body>
</html>"""

OUT = r"C:\\Users\\com\\Documents\\study metric\\Gr24_핵심계산_주제별완전판.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_doc)
print("BOOK written:", OUT, f"({len(html_doc)//1024} KB)")
