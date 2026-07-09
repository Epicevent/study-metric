# L6 — 사상 가지: conic / Veronese pullback $\big(\nu_2^*ds^2_{\mathbb{CP}^2}=2\,ds^2_{\mathbb{CP}^1},\ \rho_{\mathbb{CP}^1}=\nu_2^*\omega_{\mathrm{FS}},\ \mathrm{Ric}=\nu_{n+1}^*\omega\big)$

> **이 층의 역할 — 등뼈가 아니라 가지.** L0–L4가 *하나의 포텐셜에서 $\partial\bar\partial$로 흘러나온* 등뼈라면, L6은 그 결과($g$·Ricci)를 **다른 사상으로 재획득**하는 옆가지다. 핵심 깨달음: 포텐셜 $\Phi=\log S=\log\|v\|^2$는 *처음부터* universal FS 포텐셜 $\log\|w\|^2$의 **pullback**이었다(올림 $v$가 곧 embedding). 그래서 곡률 계산은 전부 "어떤 사상으로 FS form을 당겼는가"의 문제이고, 특히 **CP¹의 Ricci form = conic(2차 Veronese)으로 당긴 CP²의 FS form**과 글자 그대로 같은 form이다.

학습용이라 작은 계단으로 쪼개고, 검산은 부록에. **모든 상수는 독립 계산으로 검증되었다.**

---

## 0. 표기와 규약

- $z\in\mathbb C$, $s=|z|^2$, $S=1+s$. 포텐셜 $\Phi=\log S$, $\omega=\partial\bar\partial\Phi$ (계수 $h=1/S^2$).
- universal FS 포텐셜: CPⁿ 동차좌표 $w$에 대해 $\Phi_{\mathrm{FS}}=\log\|w\|^2$, $\omega_{\mathrm{FS}}=\partial\bar\partial\log\|w\|^2$.
- Veronese $\nu_m:\mathbb{CP}^1\to\mathbb{CP}^m$. $m=2$가 **conic**.

---

## 1. Block 1 — $\log S$는 이미 pullback이었다 *(conic note §1)*

### 연습 1.1 — 사상이 포텐셜을 당기는 법

- **(a)** 정칙사상 $f=[f_0:\cdots:f_N]:M\to\mathbb{CP}^N$. 좌표를 당기면 $w_i\circ f=f_i$, 따라서
$$
f^*\Phi_{\mathrm{FS}}=\log\textstyle\sum_i|f_i|^2=\log\|f\|^2.
$$
- **(b)** $\partial\bar\partial$는 pullback과 교환하므로 $\boxed{f^*\omega_{\mathrm{FS}}=\partial\bar\partial\log\|f\|^2}$.

### 연습 1.2 — 그래서 너의 $S$는 $f^*$였다

- **(a)** 표준 차트 올림 $v=(1,z)$는 사상 $z\mapsto[1:z]$의 동차표현 ($f=v$, $N=1$). $\|f\|^2=1+|z|^2=S$.
- **(b)** 즉 $\Phi=\log S=f^*\Phi_{\mathrm{FS}}$. **"올림"이 곧 embedding이었고, $S=\|v\|^2$는 당겨진 포텐셜.**

### 연습 1.3 — 올림 모호성은 form을 못 본다

- **(a)** $f\mapsto hf$ ($h$ 정칙, $\ne0$): $\log\|hf\|^2=\log|h|^2+\log\|f\|^2$, $\partial\bar\partial\log|h|^2=0$ (pluriharmonic).
- **(b)** 따라서 $\partial\bar\partial\log\|hf\|^2=\partial\bar\partial\log\|f\|^2$ — well-defined. *(conic §1.4)*

---

## 2. Block 2 — conic(2차 Veronese)을 손으로 당기기 *(conic note §2)*

### 연습 2.1 — 정의

- **(a)** $SU(2)$-등변이 되도록 이항계수 제곱근을 붙인 2차 Veronese:
$$
\nu_2([z_0:z_1])=\big[\,z_0^2:\sqrt2\,z_0z_1:z_1^2\,\big]\in\mathbb{CP}^2.
$$
상은 conic $XZ=Y^2$. 그래서 "conic embedding".

### 연습 2.2 — 당긴 포텐셜 = $2\Phi$ (이항정리가 핵심)

- **(a)** affine 차트 $z_0=1$, $\nu_2(z)=[1:\sqrt2 z:z^2]$:
$$
\|\nu_2\|^2=1+2|z|^2+|z|^4=(1+|z|^2)^2=S^2.
$$
($\sqrt2$ 덕에 가운데 항 $2=\binom21$ → 완전제곱.)
- **(b)** §1.1로
$$
\boxed{\ \nu_2^*\Phi_{\mathrm{FS}}=\log\|\nu_2\|^2=\log S^2=2\log S=2\Phi\ },\qquad
\nu_2^*\omega_{\mathrm{FS},\mathbb{CP}^2}=2\,\omega_{\mathrm{FS},\mathbb{CP}^1}.
$$
계수 $2$는 conic의 **차수**. 계량 수준에서 $\boxed{\nu_2^*ds^2_{\mathbb{CP}^2}=2\,ds^2_{\mathbb{CP}^1}}$.

### 연습 2.3 — 일반 $m$ (맥락)

- **(a)** $\nu_m([z_0:z_1])=\big[\binom mk^{1/2}z_0^{m-k}z_1^k\big]_{k=0}^m$. 이항정리로
$$
\|\nu_m\|^2=\sum_{k=0}^m\binom mk|z|^{2k}=(1+|z|^2)^m=S^m\ \Rightarrow\ \nu_m^*\omega=m\,\omega.
$$
- **(b)** "차수 $m$ embedding = 포텐셜 $\times m$ = 계량 $\times m$." 차수가 곡률 form의 스케일을 정한다.

---

## 3. Block 3 — 결정타: Ricci form = conic pullback *(conic note §3)*

두 계산을 나란히:

- **(a) $\det g$ 쪽 (L3):** $\rho_{\mathbb{CP}^1}=-\partial\bar\partial\log\det g=-\partial\bar\partial\log S^{-2}=2\,\partial\bar\partial\log S=2\,\omega_{\mathrm{FS},\mathbb{CP}^1}$.
- **(b) conic 쪽 (§2.2):** $\nu_2^*\omega_{\mathrm{FS},\mathbb{CP}^2}=\partial\bar\partial\log S^2=2\,\partial\bar\partial\log S=2\,\omega_{\mathrm{FS},\mathbb{CP}^1}$.
- **(c)** 두 우변이 **글자 그대로 같다**:
$$
\boxed{\ \rho_{\mathbb{CP}^1}=\nu_2^*\,\omega_{\mathrm{FS},\mathbb{CP}^2}\ }.
$$

> **심장.** $\det g=S^{-2}$의 지수 $2$와 conic의 차수 $2$는 **같은 $2$**다 — $\det g$ 계산은 사실 *몰래* conic pullback을 계산하고 있었다. (L5의 $c_1=2[\tau]$의 $2$도 같은 뿌리.)

---

## 4. Block 4 — 왜: $\det g$는 anticanonical, 그 embedding이 Veronese *(conic note §4)*

- **(a)** $\det g=S^{-(n+1)}$의 지수 $n+1$은 부피형식 = **반표준선다발** $-K_{\mathbb{CP}^n}=\mathcal O(n+1)$의 데이터. 곡률 수준에서 $\mathrm{Ric}=(n+1)\omega_{\mathrm{FS}}$의 진짜 의미는 "Ricci form = $\mathcal O(n+1)$의 곡률".
- **(b)** $\mathcal O(n+1)$의 정칙단면 = $(n+1)$차 동차다항식 → 차수 $n+1$ Veronese $\nu_{n+1}:\mathbb{CP}^n\hookrightarrow\mathbb{CP}^N$. §2 논리(포텐셜 $\times(n+1)$) 그대로:
$$
\boxed{\ \mathrm{Ric}_{\mathbb{CP}^n}=\nu_{n+1}^*\,\omega_{\mathrm{FS}}\ }\qquad(n=1:\ \nu_2=\text{conic}).
$$

> **전체 그림 한 장.**
> $$
> \underbrace{K=-\tfrac1{2\lambda}\Delta\log\lambda}_{\text{L0·L1 곡면}}
> \xrightarrow{\log\lambda\to\log\det g}
> \underbrace{-\partial\bar\partial\log\det g=c\,g}_{\text{L3·L4 KE}}
> \xrightarrow{\det g=S^{-(n+1)}=\text{당김}}
> \underbrace{\mathrm{Ric}=\nu_{n+1}^*\omega_{\mathrm{FS}}}_{\text{L6 pullback}}
> $$

---

## 5. ⚠ 주의 박스 — 정직한 단서

- **pullback이 항상 계량은 아니다.** $f^*\omega_{\mathrm{FS}}$는 일반적으로 (반양의) Kähler **form**일 뿐; $f$가 immersion일 때만 비퇴화 **계량**. Veronese·표준차트 올림은 embedding이라 OK. *(conic §6)*
- **form 등식이지 "정의"는 아님.** "$\mathrm{Ric}=\nu_{n+1}^*\omega$"는 같은 닫힌 $(1,1)$-form($\partial\bar\partial$-수준)이라는 뜻. 배경은 Picard 군의 사실 $-K=(n+1)H$.
- **숫자 $n+1$은 정규화 무관**(차수). L3 §3의 "$c=1$ vs $c=n+1$" 함정과 헷갈리지 말 것 — 그건 계량 스케일 선택, 이건 선다발 차수.
- **이것은 가지지 등뼈가 아니다.** conic은 FS를 *짓는* 또 하나의 길(L1 §3의 사영자 $n=1$ 경우)이자, 이미 계산된 $\rho$를 *재획득*하는 길. 등뼈(포텐셜→$\partial\bar\partial$)에 부착되는 해석 층이다.

---

## 부록 A. 한 줄 한 줄 (검산용)

**A1** $w_i\circ f=f_i\Rightarrow f^*\log\sum|w_i|^2=\log\|f\|^2$; $\partial\bar\partial$ 교환 → $f^*\omega=\partial\bar\partial\log\|f\|^2$. 올림 모호성: $\partial\bar\partial\log|h|^2=0$. ✔

**A2** $\nu_2(z)=[1:\sqrt2 z:z^2]$, $\|\nu_2\|^2=1+2s+s^2=(1+s)^2=S^2$, $\nu_2^*\Phi=2\log S$, $\nu_2^*\omega=2\omega$. 일반 $m$: $\sum\binom mk s^k=(1+s)^m=S^m$ (이항정리). ✔

**A3** $\rho=-\partial\bar\partial\log S^{-2}=2\partial\bar\partial\log S$; $\nu_2^*\omega=\partial\bar\partial\log S^2=2\partial\bar\partial\log S$. 둘 다 $2\omega$, 계수 $2/S^2$. ⟹ $\rho_{\mathbb{CP}^1}=\nu_2^*\omega_{\mathbb{CP}^2}$. ✔

**A4** $-K_{\mathbb{CP}^n}=\mathcal O(n+1)$, 단면 = $(n+1)$차 동차식 → $\nu_{n+1}$; $\nu_{n+1}^*\Phi=(n+1)\Phi\Rightarrow\nu_{n+1}^*\omega=(n+1)\omega=\rho$; $n=1\Rightarrow\nu_2$=conic. ✔

---

## 결과 요약

| 블록 | 한 일 | 결과 |
|---|---|---|
| B1 | $\log S$의 정체 | 포텐셜은 늘 pullback $f^*\log\|w\|^2$; 올림=embedding |
| B2 | conic 손으로 당김 | $\|\nu_2\|^2=S^2\Rightarrow\nu_2^*\Phi=2\Phi$, $\nu_2^*ds^2=2ds^2$ (차수 2) |
| B3 | det 쪽 vs conic 쪽 | $\rho_{\mathbb{CP}^1}=\nu_2^*\omega_{\mathbb{CP}^2}$ — Ricci form = conic pullback |
| B4 | $n+1$의 정체 | anticanonical 차수; $\mathrm{Ric}=\nu_{n+1}^*\omega$ |

**한 문장.** 포텐셜 $\log S=\log\|v\|^2$는 처음부터 universal FS form의 pullback이었고 차수 $m$ embedding은 포텐셜을 $m$배 한다 — 그래서 $\det g=S^{-(n+1)}$의 지수가 곧 반표준선다발 차수이고, **CP¹의 Ricci form은 conic(2차 Veronese)으로 당긴 CP²의 FS form과 같은 form**이다. 이는 등뼈에서 흘러나온 결과를 다른 사상으로 재획득하는 가지다.

*출처: cp1_ricci_as_conic_pullback_note.md, fs_via_projector_conic_pullback_path_note.md, fubini_study_from_constant_curvature_part2_note.md(§4.3).*
