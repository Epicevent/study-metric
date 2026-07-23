# -*- coding: utf-8 -*-
"""manifest — 사이트 문서 대장 (단일 진실 원천).

새 문서를 추가하려면 여기 항목 하나를 넣고  python _책빌드/site.py  를 돌린다.
- kind="md":   src 마크다운 → common.build_md 로 빌드 (첫 h1 = 제목, 이전/다음 내비 자동)
- kind="body": src 가 이미 HTML 본문 (titlepage 포함) — common.page 로 감싼다
- kind="cmd":  전용 빌더 스크립트를 실행 (책·걸음6처럼 조립이 특수한 것)
card = (제목 HTML, 설명 HTML) — index 카드. None 이면 목록에 안 실린다(내비만).
"""

TRACKS = [
    ("plan", "계획"),
    ("dict", "사전 — (1,z)에서 (I,Z)로, 그리고 후속"),
    ("kahler", "켈러 트랙 — 본편"),
    ("ig", "정보기하 트랙"),
]

DOCS = [
    # ---------------- 계획 ----------------
    dict(track="plan", kind="md", src="다음트랙_2026-07-10.md", out="다음트랙.html",
         series="study metric — 공부 계획",
         card=("다음 트랙 — 2026-07-10 발표 피드백 이후",
               "공부 계획: 피드백 소화(A) → II·mixed(B) → CP³·Gr(2,4) 본진(C) → 연구 씨앗(D)")),
    dict(track="plan", kind="md", src="A1_워크시트_7장.md", out="A1_워크시트.html",
         series="study metric — 트랙 A1 워크시트",
         card=("A1 워크시트 — 허수부 = 2-형식 (책 7장에서 풀 것)",
               "풀이 없는 워크시트: ②G1–G5·H3–H6 원문 + A1 고유 과제 3개(alternating 논증 재현·허수부 계수 대조·한 점에서 두 얼굴). 검산 기준 스크립트 verifyA1_targets.py 는 다 푼 뒤에")),

    # ---------------- 사전과 후속 ----------------
    dict(track="dict", kind="md", src="사전_1z에서_IZ로.md", out="사전_1z에서_IZ로.html",
         series="study metric — 사전",
         card=("사전 — (1,z)에서 (I,Z)로",
               "ℂP¹의 계산 줄 하나하나가 Gr(2,4)의 무엇인지: 게이지 λ→GL(2) · 차트 2개→6개(=플뤼커 좌표 수) · 노름²→그람 행렬식(코시–비네) · 사영자 vv†/‖v‖²→V(V†V)⁻¹V† · det g=K⁻ⁿ. <b>§0에서 먼저 답하는 것</b>: ω는 계량이 <i>아니다</i> — ω(X,X)=0이고, ω(X,JX)=|X|²로 J가 값을 치러야 계량이 된다(대칭성 축 vs 차수 축). 그리고 5b의 Q = g_FS + i·ω_FS. 검산 31/31. <b>§9의 다섯 구멍은 아래 후속 글들로 전부 닫혔다.</b>")),
    dict(track="dict", kind="md", src="Projector로_Gr24에_metric주기.md", out="Projector로_Gr24에_metric주기.html",
         series="study metric — 사전 후속",
         card=("Projector들의 모임에 metric 주기 — CP¹ 손노트에서 Gr(2,4)로",
               "<b>Projector가 metric의 본선이다.</b> 두 행렬곡선으로 기저변화와 실제 평면변화를 구별하고, CP¹ 한 칸을 거쳐 임의의 Z에서 g<sub>FS</sub>=½Tr(dP²)를 얻는다. metric만 원하면 §6에서 끝. §7.2는 왜 추가로 정칙·전역 기록을 요구할 때만 Plücker와 ℂP⁵가 필요한지 실제 v∧w 계산으로 밝히고, 걸음 6a의 가우스 소거→소행렬식→쐐기→역복원→6b Cauchy–Binet를 절별 링크로 왕복한다. 검산 32/32")),
    dict(track="dict", kind="md", src="Reeb_CP1에서_Gr24로.md", out="Reeb_CP1에서_Gr24로.html",
         series="study metric — 사전 후속",
         card=("Reeb 벡터장 — S³에서 Σ⁹로, CP¹에서 Gr(2,4)로",
               "CP¹에서 올린 속도로부터 계량을 직접 만든 뒤 Gr(2,4)의 여섯 성분에 같은 계산을 적용한다. §5에서는 기저쌍 Q → 단위 Plücker 벡터 p=v∧w → 평면 [p]의 세 층을 먼저 구별하고, 기저회전·Plücker 위상·실제 평면변화를 곡선으로 비교한 뒤에야 SU(2)와 S¹이라는 이름을 붙인다. 검산 48/48")),
    dict(track="dict", kind="md", src="부피나란히_π에서_π4_12로.md", out="부피나란히_π에서_π4_12로.html",
         series="study metric — 사전 후속",
         card=("부피 나란히 — π에서 π⁴/12로, 적분을 실제로 하기",
               "사전 §9-2를 닫는 후속: 6c가 위상(차수 2)으로 예측만 하던 ∫K⁻⁴dV(8차원)를 <b>미적분으로 직접</b> — 특이값 좌표에서 K=(1+x₁)(1+x₂)로 인수분해, 측도의 보정상수는 가우스 검문 2개로 실측(c₂=π⁴/2), 반지름 적분은 베타 세 개(⅓·⅙·⅓)로 정확히 1/6 → <b>π⁴/12</b>. ℂP¹의 π = π·∫(1+x)⁻²dx와 같은 기계, 새 재료는 밴더몬드 (x₁−x₂)²(특이값 반발) 하나. 차수 경로와 일치 + MC 끝-대-끝 8.10±0.15. 검산 15/15")),
    dict(track="dict", kind="md", src="성분대조_5b와_6b는_한_물건.md", out="성분대조_5b와_6b는_한_물건.html",
         series="study metric — 사전 후속",
         card=("성분 대조 — 5b의 QFIM과 6b의 계량은 한 물건",
               "사전 §9-3을 닫는 후속: 트레이스형 tr[F⁻¹dZ†G⁻¹dZ]의 16계수(세 줄 손계산: E_dc G⁻¹E_ab가 숫자로 접힘)와 Hessian ∂∂̄logK의 16성분이 <b>다항식 항등식</b>으로 동일 — K∂∂̄K−∂K∂̄K = adjG_ca·adjF_bd. 상수배 사슬 1:2:4 (∂∂̄logK : Tr dPdP : QFIM, k=1 닻), 플뤼커 상태 QFIM과의 일치를 부동소수점에서 <b>유리수 정확산술</b>로 승격 (Z₀=I, Ż=E₁₁ → H=1). 검산 7/7")),
    dict(track="dict", kind="md", src="차트갈아타기_1z에서_Z역행렬로.md", out="차트갈아타기_1z에서_Z역행렬로.html",
         series="study metric — 사전 후속",
         card=("차트 갈아타기 — z′=1/z에서 Z′=Z⁻¹로",
               "사전 §9-4를 닫는 후속: 풀스왑 Z′=Z⁻¹은 정칙 게이지 하나(K′=K/|det Z|², 어긋남 log|det Z|²는 ∂∂̄가 죽임 — 6ab 실물), 계량·ω는 <b>밀어넘기기 두 번</b>으로 문자 그대로 불변. 그리고 <b>k=1엔 없던 것</b>: 혼합 차트 {1,3} 실물 계산 — Z′=[[−a/b,1/b],[−detZ/b,d/b]], 분모가 전부 p₁₃ (\"차트 유효 ⟺ 소행렬식≠0\"의 실물화). 전역 그림: K_chart = Σ|p|²/|p_chart|² — 코시–비네가 여섯 차트를 한 식으로. 검산 15/15")),
    dict(track="dict", kind="md", src="전수조사_k1에서_한몸이던_것들.md", out="전수조사_k1에서_한몸이던_것들.html",
         series="study metric — 사전 후속 (완결)",
         card=("전수조사 — k=1에서 한 몸이던 것들 (사전 §9 완결)",
               "갈라지는 것 10행: 가환→비가환 게이지 · 분모 하나→F≠G 둘 · 분해가능성 제약(ω∧ω, e₁₂+e₃₄ 반례) · Hessian 십자항 = |det Z|²의 소행 · <b>정칙 단면곡률이 상수 2에서 방향의존 [1,2]로</b>(H=2Σσ⁴/(Σσ²)², 둥긂은 k=1의 우연 — 아인슈타인이지만 둥글지 않다) · 한 사영자의 두 양자 읽기(wedge 순수 vs P/2 혼합). 유지되는 것 6행: 정칙 널·멱영 (∂P)²=0(걸음 2 §3의 승격), Q=g+iω, K⁻ⁿ… 갈라짐의 뿌리는 하나 — k=1엔 특이값이 하나뿐이었다. 검산 18/18")),

    # ---------------- 켈러 트랙 본편 ----------------
    dict(track="kahler", kind="cmd", cmd=["python", "_책빌드/build_book.py"],
         out="Gr24_핵심계산_주제별완전판.html",
         card=("Gr(2,4) 핵심계산 — 주제별 완전판",
               "메인 문제집. 202제 + 병렬 30제를 주제별 15장으로 재편한 책")),
    dict(track="kahler", kind="md", src="정리_L0-L6/손계산_걸음별/5b_손노트완성본_CP1_QFIM.md",
         out="손노트완성본_CP1_QFIM.html", series="study metric — 손계산 걸음 5b",
         card=("손노트 완성본 — 「ℂP¹의 QFIM 계산하기」",
               "손노트(Notes 26-07-04)를 그 결·그 기호·그 순서 그대로 끝까지 민 완성본. 빨간펜 세 곳 + sympy 검산 55/55")),
    dict(track="kahler", kind="body", src="_책빌드/pages/해설_body.html",
         out="해설_왜_하나는_살고_하나는_죽는가.html",
         title="왜 하나는 살고, 하나는 죽는가 — ⟨ψ,∂ψ⟩ 허수부의 해석",
         series="study metric — 해설 한 편",
         card=("해설 — 왜 하나는 살고, 하나는 죽는가",
               "⟨ψ,∂ψ⟩ 허수부의 정체를 값으로 보는 한 편")),
    dict(track="kahler", kind="md", src="발표계산_완전판.md", out="발표계산_완전판.html",
         series="study metric — 발표 계산",
         card=("발표 계산 완전판 — Hopf에서 ∫ω_FS=2π까지",
               "발표의 모든 계산을 정의→대입→미분 규칙 한 줄 단위로: 구면 계량=ℝ³ 내적 → Hopf 사상 → FS=ℂ² 내적−S¹ → α·Reeb → ω_FS → 2π → χ=2. 검산: verify_talk.py (32)")),
    dict(track="kahler", kind="md", src="CP1_A와_Q_두벌계산.md", out="CP1_A와_Q_두벌계산.html",
         series="study metric — 발표 계산 부속",
         card=("ℂP¹ 계산 대조표 — A→dA와 Q→(Re Q, Im Q)",
               "<b>두 벌을 끝까지 섞지 않는다.</b> [e<sup>it</sup>s]=[s]를 먼저 확인하고 임의의 속도를 c·is+h로 실제 분해하여 A가 읽는 값을 밝힌다. Q 쪽에서는 q 방향을 빼는 정사영을 직접 전개한다. 이어 z(t)=1+it를 양쪽에 넣어 한 방향 Q(V,V)에서는 왜 허수부가 안 보이는지 확인하고, 마지막 문에서만 ½dA=Im Q와 g_FS=Re Q를 대조한다. 검산 17/17")),
    dict(track="kahler", kind="md", src="Reeb벡터장_완전계산.md", out="Reeb벡터장_완전계산.html",
         series="study metric — 파트 IV 완전 상세",
         card=("파트 IV 완전 상세 — 접속형식 α와 Reeb 벡터장",
               "약점 보강 최대 해상도 판: 쌍대 규칙·생성원·α(R)=1·수직/수평 분해·(1−P)(iψ)=0 다리·ι_R dα=−dN→0·fiber pullback, 정의부터 모든 줄. 검산: verify_reeb.py (16)")),
    dict(track="kahler", kind="cmd", cmd=["python", "_책빌드/build_step6.py"],
         out="걸음6_Gr24_플뤼커_완전판.html",
         card=("걸음 6 — Gr(2,4) ↪ ℂP⁵, 바닥부터 (완전판)",
               "플뤼커 당김 계산 노트(외부 원문)를 걸음 0–5b 위에 착륙시키는 8부작: 소행렬식이 좌표가 되는 <i>단 하나의 관찰</i> · <b>퍼텐셜은 공짜가 아니다</b>(K는 함수가 아니라 선다발 계량) · K=det(I+Z†Z)=평행사변형 넓이²(코시–비네) · N=adj(G)ᵀ⊗adj(F) · det g=K⁻ⁿ ⟹ Ric=n·g · 부피=π⁴/12 = <i>직선 4개와 만나는 직선 2개</i> · <b>원 하나로 전부 설명하기</b>(∫ω=π의 π는 감김수 1). 손계산 12과제 + 풀이집 + 검산 58/58")),

    # ---------------- 정보기하 트랙 ----------------
    dict(track="ig", kind="md", src="정보기하/IG0_한_변수에서_지표_없이.md",
         out="정보기하_IG0_한_변수에서_지표_없이.html", series="study metric — 정보기하 트랙",
         card=("IG0 — 한 변수에서, 지표 없이",
               "<b>여기서 시작.</b> §3.1에서 막히는 건 계산이 아니라 표기다 — F<sub>a</sub>(y)는 \"미분 먼저, 대입 나중\"이고 두 슬롯은 그냥 평범한 편미분이다. 변수를 하나로 줄이면 <b>곱의 미분 한 번</b>이 전부: D = 접선과 곡선의 세로 간격 → g = F″. 그리고 <b>동전 하나</b>에서 로짓·Fisher 정보 1/(η(1−η))·KL이 전부 나온다. 검산: verify_ig0_onevar.py (43/43)")),
    dict(track="ig", kind="md", src="정보기하/IG1_Bregman에서_Hessian계량.md",
         out="정보기하_IG1_Bregman에서_Hessian계량.html", series="study metric — 정보기하 트랙",
         card=("IG1 — Bregman divergence에서 Hessian 계량까지",
               "IG0를 지표로 올린 판. <i>Dually Flat Geometry</i> §3.1의 네 줄을 한 줄도 건너뛰지 않고 편다: D(x,y)=F(x)−F(y)−F<sub>a</sub>(y)(x<sup>a</sup>−y<sup>a</sup>) → g<sub>ij</sub>=F<sub>ij</sub>. 원문이 안 짚는 것 셋 — 부호의 마이너스 · 미분 순서 교차검증 · <b>비대칭은 3차에서 처음</b>(그래서 접속이 둘). 검산: verify_ig1_bregman.py (25/25)")),
]

INDEX_HEADER = dict(
    series="study metric",
    title="CP¹에서 Gr(2,4)까지, 손계산으로",
    sub="푸비니–스터디 계량과 양자정보계량(QFIM)을 미적분학 레벨의 손계산으로 쌓는 스터디 기록. 모든 핵심 등식은 sympy로 줄 단위 검산.",
    footer='손계산 문서(걸음 0→5b, 6)·정보기하 트랙·검산 스크립트·원본 노트는 <a href="https://github.com/Epicevent/study-metric">저장소</a>에서. 두 트랙이 다루는 대상 원문은 외부 자료라 저장소에 포함하지 않는다.',
)
