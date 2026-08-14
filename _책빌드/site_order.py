# -*- coding: utf-8 -*-
"""사이트 표시 순서 overlay.

manifest.py의 기존 문서 정의와 본문 source는 건드리지 않는다.
이 파일은 index 분류·표시 순서, 이전/다음 순서, 빈 문서 정의만 맡는다.
"""

TRACKS = [
    ("tools", "읽는 법 — 문제집과 통합 참고서는 전 구간에서 병행"),
    ("gr", "I. 현재 본선 A — Gr(2,4)의 로컬 기계"),
    ("tower", "II. 현재 본선 B — Plücker 곡률에서 Reineke tower·Ricci positivity로"),
    ("grplus", "III. Gr(2,4) 완결 계산 — 부피와 k=1 대비"),
    ("cp1", "IV. 로컬 모델 — ℂP¹ 예제와 손계산"),
    ("bundle", "V. 일반론 — line bundle·Chern·Ricci·HRR"),
    ("app", "VI. 응용 — QFIM·정보기하·fold·양자회로"),
    ("archive", "이전 계획 기록"),
]

ORDER = [
    "Gr24_핵심계산_주제별완전판.html",
    "행렬한장에서시작하여_번들_자립완전판.html",
    "사전_1z에서_IZ로.html",
    "걸음6_Gr24_플뤼커_완전판.html",
    "Projector로_Gr24에_metric주기.html",
    "성분대조_5b와_6b는_한_물건.html",
    "차트갈아타기_1z에서_Z역행렬로.html",
    "Reeb_CP1에서_Gr24로.html",
    "플뤼커_determinant_line_bundle의_곡률.html",
    "Relative_Grassmannian과_Relative_Plucker.html",
    "Quiver_Grassmannian에서_Reineke_Tower까지.html",
    "Twisted_Reineke_Tower_Kahler_metric.html",
    "Fano_chamber와_Ricci_positivity.html",
    "부피나란히_π에서_π4_12로.html",
    "전수조사_k1에서_한몸이던_것들.html",
    "발표계산_완전판.html",
    "Reeb벡터장_완전계산.html",
    "A1_워크시트.html",
    "손노트완성본_CP1_QFIM.html",
    "해설_왜_하나는_살고_하나는_죽는가.html",
    "CP1_A와_Q_두벌계산.html",
    "CP1_라인번들_두차트_관찰노트_10문제.html",
    "계수합0에서_line_bundle까지.html",
    "H1_S2_쌩좌표계산.html",
    "First_Chern과_Ricci_CP1에서_fold까지.html",
    "라플라시안에서_RR의_+1로.html",
    "사영공간_두계산선_단항식과_HRR.html",
    "Griffiths_positivity와_Ricci_positivity.html",
    "양자회로_QFIM_Grassmannian_Reineke_응용.html",
    "정보기하_IG0_한_변수에서_지표_없이.html",
    "정보기하_IG1_Bregman에서_Hessian계량.html",
    "Winding_Form에서_Degree까지_한노트.html",
    "TwoBand_Fold_Sheet_하루손계산.html",
    "다음트랙.html",
]

TRACK_OVERRIDE = {
    "Gr24_핵심계산_주제별완전판.html": "tools",
    "행렬한장에서시작하여_번들_자립완전판.html": "tools",
    "사전_1z에서_IZ로.html": "gr",
    "걸음6_Gr24_플뤼커_완전판.html": "gr",
    "Projector로_Gr24에_metric주기.html": "gr",
    "성분대조_5b와_6b는_한_물건.html": "gr",
    "차트갈아타기_1z에서_Z역행렬로.html": "gr",
    "Reeb_CP1에서_Gr24로.html": "gr",
    "플뤼커_determinant_line_bundle의_곡률.html": "tower",
    "Relative_Grassmannian과_Relative_Plucker.html": "tower",
    "Quiver_Grassmannian에서_Reineke_Tower까지.html": "tower",
    "Twisted_Reineke_Tower_Kahler_metric.html": "tower",
    "Fano_chamber와_Ricci_positivity.html": "tower",
    "부피나란히_π에서_π4_12로.html": "grplus",
    "전수조사_k1에서_한몸이던_것들.html": "grplus",
    "발표계산_완전판.html": "cp1",
    "Reeb벡터장_완전계산.html": "cp1",
    "A1_워크시트.html": "cp1",
    "손노트완성본_CP1_QFIM.html": "cp1",
    "해설_왜_하나는_살고_하나는_죽는가.html": "cp1",
    "CP1_A와_Q_두벌계산.html": "cp1",
    "CP1_라인번들_두차트_관찰노트_10문제.html": "bundle",
    "계수합0에서_line_bundle까지.html": "bundle",
    "H1_S2_쌩좌표계산.html": "bundle",
    "First_Chern과_Ricci_CP1에서_fold까지.html": "bundle",
    "라플라시안에서_RR의_+1로.html": "bundle",
    "사영공간_두계산선_단항식과_HRR.html": "bundle",
    "Griffiths_positivity와_Ricci_positivity.html": "bundle",
    "양자회로_QFIM_Grassmannian_Reineke_응용.html": "app",
    "정보기하_IG0_한_변수에서_지표_없이.html": "app",
    "정보기하_IG1_Bregman에서_Hessian계량.html": "app",
    "Winding_Form에서_Degree까지_한노트.html": "app",
    "TwoBand_Fold_Sheet_하루손계산.html": "app",
    "다음트랙.html": "archive",
}

# 문제집·통합 참고서·옛 계획은 목록에는 있으나 본선의 이전/다음 사슬에서는 뺀다.
NAV_EXCLUDED = {
    "Gr24_핵심계산_주제별완전판.html",
    "행렬한장에서시작하여_번들_자립완전판.html",
    "다음트랙.html",
}

EXTRA_DOCS = [
    dict(
        track="bundle", kind="existing",
        out="CP1_라인번들_두차트_관찰노트_10문제.html",
        card=(
            "두 차트에서 라인번들을 붙여 보기 — ℂP¹ 관찰노트와 10문제",
            "풀이와 분류 해설을 싣지 않은 관찰용 계산서. base·fiber·total space를 고정하고 quotient의 벡터연산 검문에서 시작하여 tautological frame, 임의 transition, 전역단면, 영점·극점, metric·curvature, 적도 경계적분, 접다발, Veronese, Čech·HRR 대조를 열 문제로 배치한다. 마지막에는 계산값만 모으는 기록표를 둔다.",
        ),
    ),
    dict(
        track="bundle", kind="existing",
        out="사영공간_두계산선_단항식과_HRR.html",
        card=(
            "비례좌표 한 줄에서 시작하여 — 사영공간의 두 계산선 (자립완전판)",
            "$[x_0:\\cdots:x_n]=[\\lambda x_0:\\cdots:\\lambda x_n]$에서 출발해 $\\mathcal O(k)$의 전역단면을 세는 계산과 Chern form·Todd factor를 적분하는 계산을 각각 닫는다.",
        ),
    ),
    dict(track="tower", kind="existing",
         out="플뤼커_determinant_line_bundle의_곡률.html",
         card=("Plücker determinant line bundle의 곡률",
               "빈 문서 · ordinary Grassmannian의 local potential을 Chern curvature form으로 읽는 다리."),
         stub=True),
    dict(track="tower", kind="existing",
         out="Relative_Grassmannian과_Relative_Plucker.html",
         card=("Relative Grassmannian과 relative Plücker embedding",
               "빈 문서 · vector space의 Grassmannian 계산을 vector bundle의 fiberwise 계산으로 올리는 다리."),
         stub=True),
    dict(track="tower", kind="existing",
         out="Quiver_Grassmannian에서_Reineke_Tower까지.html",
         card=("Quiver Grassmannian에서 Reineke tower까지",
               "빈 문서 · incidence condition, tautological bundle, acyclic ordering을 tower construction으로 묶는 자리."),
         stub=True),
    dict(track="tower", kind="existing",
         out="Twisted_Reineke_Tower_Kahler_metric.html",
         card=("Twisted Reineke–tower Kähler metric",
               "빈 문서 · 각 단계의 Plücker curvature와 horizontal–vertical block을 조합하는 metric construction."),
         stub=True),
    dict(track="tower", kind="existing",
         out="Fano_chamber와_Ricci_positivity.html",
         card=("Fano chamber와 Ricci positivity",
               "빈 문서 · anticanonical class, twisting parameter, Ricci-positive Kähler metric의 결론을 정리할 자리."),
         stub=True),
    dict(track="bundle", kind="existing",
         out="Griffiths_positivity와_Ricci_positivity.html",
         card=("Griffiths positivity와 Ricci positivity — 무엇이 같고 무엇이 다른가",
               "빈 문서 · vector-bundle curvature positivity와 Kähler metric의 Ricci positivity를 섞지 않기 위한 비교 자리."),
         stub=True),
    dict(track="app", kind="existing",
         out="양자회로_QFIM_Grassmannian_Reineke_응용.html",
         card=("양자회로 응용 — QFIM·Grassmannian·Reineke tower",
               "빈 문서 · projective state, QFIM pullback, quiver-constrained circuit를 하나의 응용 지도에 놓는 자리."),
         stub=True),
]

INDEX_HEADER = dict(
    series="study metric",
    title="CP¹에서 Gr(2,4)까지, 손계산으로",
    sub="기존 문서의 본문과 카드 설명은 그대로 두고, 현재 연구 본선과 보조 트랙이 보이도록 목록과 이동 순서만 다시 세웠다.",
    footer='기존 문서의 본문은 수정하지 않았다. 점선 카드는 아직 본문을 쓰지 않은 빈 문서이며, 목차와 완료 조건만 예약되어 있다. 소스·검산 스크립트·원본 노트는 <a href="https://github.com/Epicevent/study-metric">저장소</a>에서.',
)

INDEX_NOTICE = """
<div class="route">
<p><strong>현재 본선</strong> — Gr(2,4)의 로컬 계산 → Plücker determinant line bundle의 곡률 → relative Grassmannian → quiver/Reineke tower → twisted Kähler metric → Ricci positivity.</p>
<p><strong>병행 원칙</strong> — 예제풀이·일반론·응용 중 하나를 버리지 않는다. 문제집은 계속 풀고, CP¹ 계산은 정규화 검산에 쓰며, 양자·정보기하 응용은 별도 트랙으로 유지한다.</p>
</div>
""".strip()


def apply_order(base_docs):
    """기존 카드·본문 정의는 보존하고 분류와 순서만 덧씌운다."""
    docs = []
    for original in base_docs:
        d = dict(original)
        out = d["out"]
        d["track"] = TRACK_OVERRIDE.get(out, d["track"])
        if out in NAV_EXCLUDED:
            d["nav"] = False
        docs.append(d)

    by_out = {d["out"]: d for d in docs}
    for extra in EXTRA_DOCS:
        if extra["out"] in by_out:
            raise ValueError(f"extra document duplicates existing output: {extra['out']}")
        d = dict(extra)
        if d["out"] in NAV_EXCLUDED:
            d["nav"] = False
        by_out[d["out"]] = d

    # ASSERTION: published order contains every document exactly once.
    assert len(ORDER) == len(set(ORDER)), "ORDER contains duplicate output paths"
    missing = [out for out in ORDER if out not in by_out]
    unlisted = [out for out in by_out if out not in ORDER]
    assert not missing, f"ORDER refers to unknown documents: {missing}"
    assert not unlisted, f"documents missing from ORDER: {unlisted}"

    return [by_out[out] for out in ORDER]
