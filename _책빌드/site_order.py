# -*- coding: utf-8 -*-
"""사이트 표시 순서 overlay.

manifest.py의 기존 본문 source와 카드 문구는 건드리지 않는다.
이 파일은 실제 학습 순서, 이전/다음 순서, 빈 문서 정의만 맡는다.
"""

TRACKS = [
    ('cp1', '01 — S²에서 ℂP¹까지: 계량·Hopf·접속·QFIM'),
    ('ig', '02 — 평행선: 고전 Fisher와 정보기하'),
    ('bundle', '03 — 두 차트의 line bundle에서 Chern·Ricci·degree까지'),
    ('projective', '04 — 사영공간 일반화와 통합 재현'),
    ('gr', '05 — ℂP¹의 계산을 Gr(2,4)로 올리기'),
    ('checkpoint', '06 — Gr(2,4) 종합 검문'),
    ('relative', '07 — Relative Grassmannian과 Reineke tower'),
    ('ricci', '08 — Twisted tower metric과 Ricci positivity'),
    ('quantum', '09 — 양자회로 응용'),
    ('archive', '기록 — 이전 계획'),
]

ORDER = [
    '발표계산_완전판.html',
    'Reeb벡터장_완전계산.html',
    'CP1_A와_Q_두벌계산.html',
    'A1_워크시트.html',
    '손노트완성본_CP1_QFIM.html',
    '해설_왜_하나는_살고_하나는_죽는가.html',
    '정보기하_IG0_한_변수에서_지표_없이.html',
    '정보기하_IG1_Bregman에서_Hessian계량.html',
    'CP1_라인번들_두차트_관찰노트_10문제.html',
    '계수합0에서_line_bundle까지.html',
    'H1_S2_쌩좌표계산.html',
    'Winding_Form에서_Degree까지_한노트.html',
    'First_Chern과_Ricci_CP1에서_fold까지.html',
    'TwoBand_Fold_Sheet_하루손계산.html',
    '라플라시안에서_RR의_+1로.html',
    '사영공간_두계산선_단항식과_HRR.html',
    '행렬한장에서시작하여_번들_자립완전판.html',
    '사전_1z에서_IZ로.html',
    '걸음6_Gr24_플뤼커_완전판.html',
    'Projector로_Gr24에_metric주기.html',
    '성분대조_5b와_6b는_한_물건.html',
    '차트갈아타기_1z에서_Z역행렬로.html',
    'Reeb_CP1에서_Gr24로.html',
    '플뤼커_determinant_line_bundle의_곡률.html',
    '부피나란히_π에서_π4_12로.html',
    '전수조사_k1에서_한몸이던_것들.html',
    'Gr24_핵심계산_주제별완전판.html',
    'Relative_Grassmannian과_Relative_Plucker.html',
    'Quiver_Grassmannian에서_Reineke_Tower까지.html',
    'Grassmann_bundle의_수직접다발과_canonical_class.html',
    'Griffiths_positivity와_Ricci_positivity.html',
    'Twisted_Reineke_Tower_Kahler_metric.html',
    'Schur_complement와_수평수직_block_positivity.html',
    'Fano_chamber와_Ricci_positivity.html',
    '양자회로_QFIM_Grassmannian_Reineke_응용.html',
    '다음트랙.html',
]

TRACK_OVERRIDE = {
    '발표계산_완전판.html': 'cp1',
    'Reeb벡터장_완전계산.html': 'cp1',
    'CP1_A와_Q_두벌계산.html': 'cp1',
    'A1_워크시트.html': 'cp1',
    '손노트완성본_CP1_QFIM.html': 'cp1',
    '해설_왜_하나는_살고_하나는_죽는가.html': 'cp1',
    '정보기하_IG0_한_변수에서_지표_없이.html': 'ig',
    '정보기하_IG1_Bregman에서_Hessian계량.html': 'ig',
    'CP1_라인번들_두차트_관찰노트_10문제.html': 'bundle',
    '계수합0에서_line_bundle까지.html': 'bundle',
    'H1_S2_쌩좌표계산.html': 'bundle',
    'Winding_Form에서_Degree까지_한노트.html': 'bundle',
    'First_Chern과_Ricci_CP1에서_fold까지.html': 'bundle',
    'TwoBand_Fold_Sheet_하루손계산.html': 'bundle',
    '라플라시안에서_RR의_+1로.html': 'bundle',
    '사영공간_두계산선_단항식과_HRR.html': 'projective',
    '행렬한장에서시작하여_번들_자립완전판.html': 'projective',
    '사전_1z에서_IZ로.html': 'gr',
    '걸음6_Gr24_플뤼커_완전판.html': 'gr',
    'Projector로_Gr24에_metric주기.html': 'gr',
    '성분대조_5b와_6b는_한_물건.html': 'gr',
    '차트갈아타기_1z에서_Z역행렬로.html': 'gr',
    'Reeb_CP1에서_Gr24로.html': 'gr',
    '플뤼커_determinant_line_bundle의_곡률.html': 'gr',
    '부피나란히_π에서_π4_12로.html': 'gr',
    '전수조사_k1에서_한몸이던_것들.html': 'gr',
    'Gr24_핵심계산_주제별완전판.html': 'checkpoint',
    'Relative_Grassmannian과_Relative_Plucker.html': 'relative',
    'Quiver_Grassmannian에서_Reineke_Tower까지.html': 'relative',
    'Grassmann_bundle의_수직접다발과_canonical_class.html': 'relative',
    'Griffiths_positivity와_Ricci_positivity.html': 'ricci',
    'Twisted_Reineke_Tower_Kahler_metric.html': 'ricci',
    'Schur_complement와_수평수직_block_positivity.html': 'ricci',
    'Fano_chamber와_Ricci_positivity.html': 'ricci',
    '양자회로_QFIM_Grassmannian_Reineke_응용.html': 'quantum',
    '다음트랙.html': 'archive',
}

# 이전 계획은 기록으로 남기되 현재 학습 사슬에서는 제외한다.
NAV_EXCLUDED = {"다음트랙.html"}

EXTRA_DOCS = [
    dict(
        track='bundle', kind="existing", out='CP1_라인번들_두차트_관찰노트_10문제.html',
        card=('두 차트에서 라인번들을 붙여 보기 — ℂP¹ 관찰노트와 10문제', '풀이와 분류 해설을 싣지 않은 관찰용 계산서. base·fiber·total space를 고정하고 quotient의 벡터연산 검문에서 시작하여 tautological frame, 임의 transition, 전역단면, 영점·극점, metric·curvature, 적도 경계적분, 접다발, Veronese, Čech·HRR 대조를 열 문제로 배치한다. 마지막에는 계산값만 모으는 기록표를 둔다.'),
    ),
    dict(
        track='projective', kind="existing", out='사영공간_두계산선_단항식과_HRR.html',
        card=('비례좌표 한 줄에서 시작하여 — 사영공간의 두 계산선 (자립완전판)', '$[x_0:\\cdots:x_n]=[\\lambda x_0:\\cdots:\\lambda x_n]$에서 출발해 $\\mathcal O(k)$의 전역단면을 세는 계산과 Chern form·Todd factor를 적분하는 계산을 각각 닫는다.'),
    ),
    dict(
        track='gr', kind="existing", out='플뤼커_determinant_line_bundle의_곡률.html',
        card=('Plücker determinant line bundle의 곡률', '빈 문서 · ordinary Grassmannian의 local potential을 Chern curvature form으로 읽는 다리.'),
        stub=True,
    ),
    dict(
        track='relative', kind="existing", out='Relative_Grassmannian과_Relative_Plucker.html',
        card=('Relative Grassmannian과 relative Plücker embedding', '빈 문서 · vector space의 Grassmannian 계산을 vector bundle의 fiberwise 계산으로 올리는 다리.'),
        stub=True,
    ),
    dict(
        track='relative', kind="existing", out='Quiver_Grassmannian에서_Reineke_Tower까지.html',
        card=('Quiver Grassmannian에서 Reineke tower까지', '빈 문서 · incidence condition, tautological bundle, acyclic ordering을 tower construction으로 묶는 자리.'),
        stub=True,
    ),
    dict(
        track='relative', kind="existing", out='Grassmann_bundle의_수직접다발과_canonical_class.html',
        card=('Grassmann bundle의 수직접다발과 canonical class', '빈 문서 · relative tangent sequence와 Grassmann bundle canonical class formula를 계산할 자리.'),
        stub=True,
    ),
    dict(
        track='ricci', kind="existing", out='Griffiths_positivity와_Ricci_positivity.html',
        card=('Griffiths positivity와 Ricci positivity — 무엇이 같고 무엇이 다른가', '빈 문서 · vector-bundle curvature positivity와 Kähler metric의 Ricci positivity를 섞지 않기 위한 비교 자리.'),
        stub=True,
    ),
    dict(
        track='ricci', kind="existing", out='Twisted_Reineke_Tower_Kahler_metric.html',
        card=('Twisted Reineke–tower Kähler metric', '빈 문서 · 각 단계의 Plücker curvature와 horizontal–vertical block을 조합하는 metric construction.'),
        stub=True,
    ),
    dict(
        track='ricci', kind="existing", out='Schur_complement와_수평수직_block_positivity.html',
        card=('Schur complement와 수평–수직 block positivity', '빈 문서 · tower metric의 block matrix와 큰 twisting parameter에서의 positivity를 계산할 자리.'),
        stub=True,
    ),
    dict(
        track='ricci', kind="existing", out='Fano_chamber와_Ricci_positivity.html',
        card=('Fano chamber와 Ricci positivity', '빈 문서 · anticanonical class, twisting parameter, Ricci-positive Kähler metric의 결론을 정리할 자리.'),
        stub=True,
    ),
    dict(
        track='quantum', kind="existing", out='양자회로_QFIM_Grassmannian_Reineke_응용.html',
        card=('양자회로 응용 — QFIM·Grassmannian·Reineke tower', '빈 문서 · projective state, QFIM pullback, quiver-constrained circuit를 하나의 응용 지도에 놓는 자리.'),
        stub=True,
    ),
]

INDEX_HEADER = dict(
    series="study metric",
    title="CP¹에서 Gr(2,4), Reineke tower까지",
    sub="분류표가 아니라 위에서 아래로 읽는 실제 순서. 기존 본문은 그대로 두고, 예제풀이·일반론·응용을 필요한 지점에 끼워 넣었다.",
    footer='기존 문서 본문은 수정하지 않았다. 점선 카드는 아직 본문을 쓰지 않은 빈 문서다. 소스·검산 스크립트·원본 노트는 <a href="https://github.com/Epicevent/study-metric">저장소</a>에서.',
)

INDEX_NOTICE = """
<div class="route">
<p><strong>주축.</strong> S²·ℂP¹의 metric과 QFIM → 두 차트의 line bundle과 curvature → 사영공간 일반화 → Gr(2,4)의 Plücker·metric·곡률 → relative Grassmannian → quiver/Reineke tower → twisted Kähler metric과 Ricci positivity.</p>
<p><strong>배치 원칙.</strong> 정보기하는 QFIM 직후, fold 응용은 Chern·Ricci 직후, 양자회로 응용은 Reineke tower 뒤에 둔다. 종합 문제집은 시작점이 아니라 Gr(2,4) 본선을 한 번 통과한 뒤의 검문으로 둔다.</p>
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

    # ASSERTION: every published document occurs exactly once in the curriculum.
    assert len(ORDER) == len(set(ORDER)), "ORDER contains duplicate output paths"
    missing = [out for out in ORDER if out not in by_out]
    unlisted = [out for out in by_out if out not in ORDER]
    assert not missing, f"ORDER refers to unknown documents: {missing}"
    assert not unlisted, f"documents missing from ORDER: {unlisted}"
    return [by_out[out] for out in ORDER]
