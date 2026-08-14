const SITE_NAV_ORDER = [
  {"file":"사전_1z에서_IZ로.html","title":"사전 — (1,z)에서 (I,Z)로"},
  {"file":"걸음6_Gr24_플뤼커_완전판.html","title":"걸음 6 — Gr(2,4) ↪ ℂP⁵, 바닥부터 (완전판)"},
  {"file":"Projector로_Gr24에_metric주기.html","title":"Projector들의 모임에 metric 주기 — CP¹ 손노트에서 Gr(2,4)로"},
  {"file":"성분대조_5b와_6b는_한_물건.html","title":"성분 대조 — 5b의 QFIM과 6b의 계량은 한 물건"},
  {"file":"차트갈아타기_1z에서_Z역행렬로.html","title":"차트 갈아타기 — z′=1/z에서 Z′=Z⁻¹로"},
  {"file":"Reeb_CP1에서_Gr24로.html","title":"Reeb 벡터장 — S³에서 Σ⁹로, CP¹에서 Gr(2,4)로 (+§10 곡률)"},
  {"file":"플뤼커_determinant_line_bundle의_곡률.html","title":"Plücker determinant line bundle의 곡률"},
  {"file":"Relative_Grassmannian과_Relative_Plucker.html","title":"Relative Grassmannian과 relative Plücker embedding"},
  {"file":"Quiver_Grassmannian에서_Reineke_Tower까지.html","title":"Quiver Grassmannian에서 Reineke tower까지"},
  {"file":"Twisted_Reineke_Tower_Kahler_metric.html","title":"Twisted Reineke–tower Kähler metric"},
  {"file":"Fano_chamber와_Ricci_positivity.html","title":"Fano chamber와 Ricci positivity"},
  {"file":"부피나란히_π에서_π4_12로.html","title":"부피 나란히 — π에서 π⁴/12로, 적분을 실제로 하기"},
  {"file":"전수조사_k1에서_한몸이던_것들.html","title":"전수조사 — k=1에서 한 몸이던 것들 (사전 §9 완결)"},
  {"file":"발표계산_완전판.html","title":"발표 계산 완전판 — Hopf에서 ∫ω_FS=2π까지"},
  {"file":"Reeb벡터장_완전계산.html","title":"파트 IV 완전 상세 — 접속형식 α와 Reeb 벡터장"},
  {"file":"A1_워크시트.html","title":"A1 워크시트 — 허수부 = 2-형식 (책 7장에서 풀 것)"},
  {"file":"손노트완성본_CP1_QFIM.html","title":"손노트 완성본 — 「ℂP¹의 QFIM 계산하기」"},
  {"file":"해설_왜_하나는_살고_하나는_죽는가.html","title":"해설 — 왜 하나는 살고, 하나는 죽는가"},
  {"file":"CP1_A와_Q_두벌계산.html","title":"ℂP¹ 계산 대조표 — A→dA와 Q→(Re Q, Im Q)"},
  {"file":"CP1_라인번들_두차트_관찰노트_10문제.html","title":"두 차트에서 라인번들을 붙여 보기 — ℂP¹ 관찰노트와 10문제"},
  {"file":"계수합0에서_line_bundle까지.html","title":"1+2−2−1=0에서 line bundle까지"},
  {"file":"H1_S2_쌩좌표계산.html","title":"구면의 closed 1-form을 쌩좌표로 적분하기"},
  {"file":"First_Chern과_Ricci_CP1에서_fold까지.html","title":"First Chern class와 Ricci curvature — CP¹에서 fold까지"},
  {"file":"라플라시안에서_RR의_+1로.html","title":"라플라시안에서 RR의 +1로 — 무한대의 −2log|z|가 기억한 것"},
  {"file":"사영공간_두계산선_단항식과_HRR.html","title":"비례좌표 한 줄에서 시작하여 — 사영공간의 두 계산선 (자립완전판)"},
  {"file":"Griffiths_positivity와_Ricci_positivity.html","title":"Griffiths positivity와 Ricci positivity — 무엇이 같고 무엇이 다른가"},
  {"file":"양자회로_QFIM_Grassmannian_Reineke_응용.html","title":"양자회로 응용 — QFIM·Grassmannian·Reineke tower"},
  {"file":"정보기하_IG0_한_변수에서_지표_없이.html","title":"IG0 — 한 변수에서, 지표 없이"},
  {"file":"정보기하_IG1_Bregman에서_Hessian계량.html","title":"IG1 — Bregman divergence에서 Hessian 계량까지"},
  {"file":"Winding_Form에서_Degree까지_한노트.html","title":"원을 세던 적분이 구면의 degree가 되기까지"},
  {"file":"TwoBand_Fold_Sheet_하루손계산.html","title":"구면의 양의 곡률면적이 토러스에서 뒤집히는 순간"}
];

// ASSERTION: every filename occurs at most once in SITE_NAV_ORDER.
if (new Set(SITE_NAV_ORDER.map((item) => item.file)).size !== SITE_NAV_ORDER.length) {
  throw new Error("SITE_NAV_ORDER contains duplicate filenames");
}

function siteCurrentFile() {
  const raw = window.location.pathname.split("/").pop() || "index.html";
  try { return decodeURIComponent(raw); } catch (_) { return raw; }
}

function siteNavAnchor(item, label) {
  const a = document.createElement("a");
  a.href = item.file;
  a.textContent = label;
  a.title = item.title;
  return a;
}

function siteNavPlaceholder() {
  return document.createElement("span");
}

function rewriteSiteNavigation() {
  const current = siteCurrentFile();
  const index = SITE_NAV_ORDER.findIndex((item) => item.file === current);
  if (index < 0) return;

  const prev = index > 0 ? SITE_NAV_ORDER[index - 1] : null;
  const next = index + 1 < SITE_NAV_ORDER.length ? SITE_NAV_ORDER[index + 1] : null;

  const top = document.querySelector(".sitenav");
  let pn = top ? top.querySelector(".pn") : null;
  if (top && !pn) {
    pn = document.createElement("span");
    pn.className = "pn";
    top.appendChild(pn);
  }
  if (pn) {
    pn.replaceChildren();
    if (prev) pn.appendChild(siteNavAnchor(prev, "‹ 이전"));
    if (next) pn.appendChild(siteNavAnchor(next, "다음 ›"));
  }

  let bottom = document.querySelector(".sitenav-bottom");
  if (!bottom) {
    bottom = document.createElement("div");
    bottom.className = "sitenav-bottom";
    document.body.appendChild(bottom);
  }
  bottom.replaceChildren(
    prev ? siteNavAnchor(prev, `‹ ${prev.title}`) : siteNavPlaceholder(),
    (() => {
      const home = document.createElement("a");
      home.href = "index.html";
      home.textContent = "← 목록으로 돌아가기";
      return home;
    })(),
    next ? siteNavAnchor(next, `${next.title} ›`) : siteNavPlaceholder()
  );
}

document.addEventListener("DOMContentLoaded", function () {
  // HTML parses a raw '<' followed by a letter inside TeX as a bogus tag
  // before KaTeX sees it. Recover the swallowed TeX fragment first.
  // ASSERTION: only malformed elements ending in '<' with the synthetic
  // closing-</p> attribute are rewritten; ordinary HTML is untouched.
  for (const el of Array.from(document.querySelectorAll("*"))) {
    const name = el.localName;
    if (!name.includes("<") || !name.endsWith("<") || !el.hasAttribute("p") || !el.parentElement) {
      continue;
    }
    const recovered = "<" + name.slice(0, -1);
    el.parentElement.insertBefore(document.createTextNode(recovered), el);
    el.remove();
  }

  if (typeof renderMathInElement === "function") {
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
      ],
      throwOnError: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "svg"]
    });
  }

  rewriteSiteNavigation();
});