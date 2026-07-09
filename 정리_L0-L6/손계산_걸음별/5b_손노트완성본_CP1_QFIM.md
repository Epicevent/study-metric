# 5b. 손노트 완성본 — 「ℂP¹의 QFIM 계산하기」

> **이 문서가 무엇인가.** `Notes_260704_170213.pdf`(6쪽 손노트)를 **그 결·그 기호·그 순서 그대로** 끝까지 밀고 간 완성본이다. 원본이 미끄러진 세 줄은 🖍 빨간펜으로 그 자리에서 잡는다.
> **Example 1의 역할.** 이 예시는 공식 연습용이 아니다. QFIM 공식을 fact로 받아쓰지 않고, **공식이 하는 일 — 위상 방향을 사영으로 제거하고, 남은 것의 길이가 진짜 유클리드 길이임 — 을 구면 위에서 목격**하기 위한 장치다. 그 목격이 §「사영을 눈으로 보기」다.
> **검산**: 같은 폴더 `verify5b_note_completion.py` — 아래 모든 표시 [n], [Pn], [Nn]은 그 스크립트의 검산 번호. **55/55 통과** (부록 A). 진단 상세·Gr(2,4) 기술은 문서 5, 문제 원문은 책 8장.

---

## ▢ ℂP¹의 QFIM 계산하기  *(노트 1쪽 — 그대로)*

$$
\mathbb C^2\setminus\{0\}\ \longrightarrow\ \mathbb{CP}^1,\qquad
\begin{bmatrix}\alpha\\ \beta\end{bmatrix}\longmapsto[\alpha:\beta],\qquad
\begin{bmatrix}0\\ 1\end{bmatrix}\longmapsto[0:1],\qquad
\begin{bmatrix}1\\ z\end{bmatrix}\in\mathbb C^2\ \longmapsto\ [1:z]\in\mathbb{CP}^1 .
$$

$$
\psi(z):=\frac{1}{\sqrt{1+|z|^2}}\begin{bmatrix}1\\ z\end{bmatrix}\in\mathbb C^2
\qquad\text{— }[1:z]\text{에 대응하는 pure state를 그림함.}
$$

$$
P(z):=\psi(z)\,\psi(z)^* .
$$

$$
\{\text{rank-1 projector}\}\ \cong\ \mathbb{CP}^1:\qquad
P^2=P,\ P=P^*\ \xrightarrow{\ \text{spectral thm}\ }\
P=vv^*,\ v\in\mathbb C^2,\ \|v\|=1
$$

($P=0$은 rank 0, $P=I$는 rank 2 — 제외).

---

## ▢ QFIM의 기본정의 — 라고 적혀 있지만, 아직 믿지 않는다  *(노트 2쪽)*

순수상태가 모수 $(\theta_1,\dots,\theta_m)$에 의존한다고 하자. 순수상태의 QFIM은

$$
H_{ij}=4\,\mathrm{Re}\Bigl[(\partial_i\psi)^*(\partial_j\psi)-(\partial_i\psi)^*\psi\cdot\psi^*(\partial_j\psi)\Bigr].
$$

이 줄을 여기서는 **주장**으로만 받아 둔다. 왜 하필 이 조합인지 — 특히 둘째 항이 무엇을 **빼는** 것인지 — 는 정의가 아니라 계산으로 보여야 한다. Example 1이 있는 이유가 그것이다: 아래에서 $\psi$와 그 미분을 손에 쥔 다음, §「사영을 눈으로 보기」에서 이 괄호가 문자 그대로

$$
\bigl\langle(1-P)\,\partial_i\psi,\ (1-P)\,\partial_j\psi\bigr\rangle
$$

— **위상 성분을 사영으로 제거한 뒤의 내적** — 임을 확인하고, 그 길이가 구면의 진짜 유클리드 길이 $|d\vec n|^2$와 일치하는 것까지 본다. 그때부터만 이 공식을 쓴다.

> ★ **전제 하나는 지금 별표 쳐 둔다**: 위 식은 $\|\psi\|=1$일 때의 식이다(기준집 ③ Assertion 1). — 노트 4쪽 사고의 절반이 여기서 났다.

---

## ▢ Example 1  *(노트 2쪽 — 🖍 두 곳)*

$$
p(\theta_1,\theta_2)=(\cos\theta_1\sin\theta_2,\ \sin\theta_1\sin\theta_2,\ \cos\theta_2)
\qquad(\theta_1=\text{방위각},\ \theta_2=\text{극각, 노트의 }\theta,\varphi).
$$

$p(\theta_1,\theta_2)$에 대응하는 순수상태를 **남극점에서 입체사영**하여 얻는다. 남극 $S=(0,0,-1)$에서 $p$를 지나는 직선을 성분별로 쓰면 ($t=0$에서 $S$, $t=1$에서 $p$):

$$
\ell(t)=S+t\,(p-S)
=\bigl(\,t\sin\theta_2\cos\theta_1,\ \ t\sin\theta_2\sin\theta_1,\ \ -1+t(1+\cos\theta_2)\,\bigr).
$$

적도평면과 만나는 곳, 즉 셋째 성분 $=0$:

$$
-1+t^\ast(1+\cos\theta_2)=0\qquad\Longrightarrow\qquad t^\ast=\frac{1}{1+\cos\theta_2}. \tag{[1a]}
$$

> 🖍 **빨간펜 (E1).** 노트는 여기서 $z=\dfrac{1}{1+\cos\theta_2}e^{i\theta_1}$로 적었다 — **직선 매개변수 $t^\ast$를 그대로 평면 반지름으로 쓴 것**이다. 평면점은 $t^\ast$가 아니라 $\ell(t^\ast)$의 앞 두 성분이다. $\sin\theta_2$가 여기서 빠졌다: $z_{\text{노트}}\cdot\sin\theta_2=z$ [1c].

앞 두 성분을 실제로 대입하면:

$$
z=t^\ast\sin\theta_2\,(\cos\theta_1+i\sin\theta_1)
=\frac{\sin\theta_2}{1+\cos\theta_2}\,e^{i\theta_1}.
$$

반지름을 반각으로 정리한다. $\theta_2=2u$로 놓고 배각을 전개하면

$$
\frac{\sin 2u}{1+\cos 2u}
=\frac{2\sin u\cos u}{1+(2\cos^2u-1)}
=\frac{2\sin u\cos u}{2\cos^2u}
=\tan u,
$$

따라서

$$
\boxed{\ z=\tan\!\frac{\theta_2}{2}\,e^{i\theta_1}\ }\tag{[1b]}
$$

**특수값으로 사영을 검문한다** (기준집 ②A5의 습관):

| $\theta_2$ | 구면점 | $z$ (고친 것) | $z_{\text{노트}}$ (E1) |
|---|---|---|---|
| $0$ | 북극 | $0$ ✓ 원점 | $\tfrac12 e^{i\theta_1}$ — 북극이 원점에 안 감. 사영이 아니라는 신호 |
| $\pi/2$ | 적도 | $\lvert z\rvert=1$ ✓ 단위원 | $\lvert z\rvert=1$ (우연히 일치) |
| $\to\pi$ | 남극 | $\to\infty$ ✓ | $\to\tfrac12$ — 남극이 유한한 점에 감 |

---

## ▢ $\psi(\theta_1,\theta_2)$ 만들기  *(노트 2쪽 아래 — 🖍 한 곳)*

$1+|z|^2$부터. $|e^{i\theta_1}|=1$이므로

$$
1+|z|^2=1+\tan^2\!\frac{\theta_2}{2}
=\frac{\cos^2\frac{\theta_2}{2}+\sin^2\frac{\theta_2}{2}}{\cos^2\frac{\theta_2}{2}}
=\frac{1}{\cos^2\frac{\theta_2}{2}}. \tag{[2a]}
$$

> 🖍 **빨간펜 (E2).** 정규화 인자는 $\dfrac{1}{\sqrt{1+|z|^2}}$인데 노트는 $\dfrac{1}{1+|z|^2}$를 곱했다 — **제곱근 누락**. 그 결과 노트의 $\tilde\psi$는 $\|\tilde\psi\|^2=\dfrac{c^2}{1+c^2}\neq1$ ($c=1+\cos\theta_2$) [8a] — 위의 ★ 별표 조건 위반이고, 이 시점 이후의 모든 내적이 오염된다.

제대로 쓰면, $\theta_2\in(0,\pi)$에서 $\cos\frac{\theta_2}{2}>0$이므로

$$
\text{☆}:=\sqrt{1+|z|^2}=\frac{1}{\cos\frac{\theta_2}{2}},
\qquad
\psi=\frac{1}{\text{☆}}\begin{bmatrix}1\\ z\end{bmatrix}
=\cos\frac{\theta_2}{2}\begin{bmatrix}1\\[2pt] \tan\frac{\theta_2}{2}e^{i\theta_1}\end{bmatrix}
$$

$$
\boxed{\ \psi(\theta_1,\theta_2)=\begin{bmatrix}\cos\frac{\theta_2}{2}\\[4pt] e^{i\theta_1}\sin\frac{\theta_2}{2}\end{bmatrix}\ }\tag{[2b]}
$$

별표 조건 검문:

$$
\|\psi\|^2=\cos^2\frac{\theta_2}{2}+\Bigl|e^{i\theta_1}\Bigr|^2\sin^2\frac{\theta_2}{2}
=\cos^2\frac{\theta_2}{2}+\sin^2\frac{\theta_2}{2}=1.\ \checkmark \tag{[2c]}
$$

---

## ▢ $\partial_1\psi$, $\partial_2\psi$  *(노트 3쪽의 자리)*

노트 3쪽의 quotient rule 전개 자체는 **입력(E1·E2 상태의 ψ) 기준으로 정확했다**(문서 5 §1.1 — 재주는 멀쩡했고 재료가 나빴다). 고친 $\psi$는 성분이 단순해서 미분이 짧다.

**$\partial_1$ (방위각).** 첫 성분엔 $\theta_1$이 없고, 둘째 성분은 $e^{i\theta_1}$의 미분:

$$
\partial_1\psi=\begin{bmatrix}0\\[2pt] \dfrac{\partial}{\partial\theta_1}\bigl(e^{i\theta_1}\bigr)\sin\frac{\theta_2}{2}\end{bmatrix}
=\boxed{\begin{bmatrix}0\\[2pt] i\,e^{i\theta_1}\sin\frac{\theta_2}{2}\end{bmatrix}}\tag{[3a]}
$$

**$\partial_2$ (극각).** 반각의 연쇄법칙 $\frac{d}{d\theta_2}\cos\frac{\theta_2}{2}=-\frac12\sin\frac{\theta_2}{2}$, $\frac{d}{d\theta_2}\sin\frac{\theta_2}{2}=\frac12\cos\frac{\theta_2}{2}$:

$$
\partial_2\psi=\boxed{\begin{bmatrix}-\frac12\sin\frac{\theta_2}{2}\\[4pt] \frac12\,e^{i\theta_1}\cos\frac{\theta_2}{2}\end{bmatrix}}\tag{[3b]}
$$

---

## ▢ 내적 다섯 개  *(H 조립에 필요한 전부)*

표기: $\langle a,b\rangle=a^*b$ (첫 인자에 켤레). 성분을 전부 쓴다.

**(1)** $\langle\partial_1\psi,\partial_1\psi\rangle
=0\cdot0+\overline{\bigl(i e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)}\bigl(i e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)
=(-i)(i)\,e^{-i\theta_1}e^{i\theta_1}\sin^2\tfrac{\theta_2}{2}
=\sin^2\tfrac{\theta_2}{2}.$  [4]

**(2)** $\langle\psi,\partial_1\psi\rangle
=\cos\tfrac{\theta_2}{2}\cdot0+\overline{\bigl(e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)}\bigl(i e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)
=i\sin^2\tfrac{\theta_2}{2}.$  [4]
— **순허수**: $\|\psi\|=1$을 미분하면 $\langle\psi,\partial\psi\rangle+\overline{\langle\psi,\partial\psi\rangle}=0$ (기준집 ③P001). 실부가 나왔다면 그 자체가 경보다.

**(3)** $\langle\partial_2\psi,\partial_2\psi\rangle
=\bigl(-\tfrac12\sin\tfrac{\theta_2}{2}\bigr)^2+\bigl(\tfrac12\cos\tfrac{\theta_2}{2}\bigr)^2\bigl|e^{i\theta_1}\bigr|^2
=\tfrac14\bigl(\sin^2+\cos^2\bigr)=\tfrac14.$  [4]

**(4)** $\langle\psi,\partial_2\psi\rangle
=\cos\tfrac{\theta_2}{2}\bigl(-\tfrac12\sin\tfrac{\theta_2}{2}\bigr)+\overline{\bigl(e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)}\bigl(\tfrac12 e^{i\theta_1}\cos\tfrac{\theta_2}{2}\bigr)
=-\tfrac12\sin\tfrac{\theta_2}{2}\cos\tfrac{\theta_2}{2}+\tfrac12\sin\tfrac{\theta_2}{2}\cos\tfrac{\theta_2}{2}=0.$  [4]

**(5)** $\langle\partial_1\psi,\partial_2\psi\rangle
=0\cdot\bigl(-\tfrac12\sin\tfrac{\theta_2}{2}\bigr)+\overline{\bigl(i e^{i\theta_1}\sin\tfrac{\theta_2}{2}\bigr)}\bigl(\tfrac12 e^{i\theta_1}\cos\tfrac{\theta_2}{2}\bigr)
=-\tfrac{i}{2}\sin\tfrac{\theta_2}{2}\cos\tfrac{\theta_2}{2}
=-\tfrac{i}{4}\sin\theta_2.$  [4]

---

## ▢ 사영을 눈으로 보기 — 공식이 무엇을 재는가

여기가 Example 1을 꺼낸 이유다. 공식 없이, 사영만으로 간다.

### (a) 가짜 움직임 — 위상 원

$e^{i\alpha}\psi$는 $\psi$와 같은 점이다: $(e^{i\alpha}\psi)(e^{i\alpha}\psi)^*=\psi\psi^*=P$. 즉 각 구면점 위에는 위상 원이 하나씩 떠 있고, 그 원을 따라 도는 속도

$$
\frac{d}{d\alpha}\Bigl(e^{i\alpha}\psi\Bigr)\Big|_{\alpha=0}=i\psi
$$

는 **구면 위에서는 아무 데도 안 가는** 방향이다. 그런데 (2)에서 본 대로 $\langle\psi,\partial_1\psi\rangle=i\sin^2\frac{\theta_2}{2}\neq0$ — 즉 $\partial_1\psi$는 이 가짜 방향의 성분을 실제로 갖고 있다. 위도를 돌면($\theta_1$) 상태벡터가 구면 이동과 **동시에 위상도 감는다**는 뜻이다. 이걸 빼지 않으면 길이를 과대평가한다.

### (b) 사영 — 가짜 성분을 실제로 빼 본다

$\psi$ 방향 성분을 빼는 사영:

$$
(\partial_i\psi)_\perp:=\partial_i\psi-\psi\,\langle\psi,\partial_i\psi\rangle=(1-P)\,\partial_i\psi .
$$

$\partial_1$에 대해 성분을 전부 쓰면 ((2)를 대입):

$$
(\partial_1\psi)_\perp
=\begin{bmatrix}0\\[2pt] i e^{i\theta_1}\sin\frac{\theta_2}{2}\end{bmatrix}
-\begin{bmatrix}\cos\frac{\theta_2}{2}\\[2pt] e^{i\theta_1}\sin\frac{\theta_2}{2}\end{bmatrix}\,i\sin^2\tfrac{\theta_2}{2}
=\boxed{\begin{bmatrix}-i\,\sin^2\frac{\theta_2}{2}\cos\frac{\theta_2}{2}\\[4pt] i\,e^{i\theta_1}\sin\frac{\theta_2}{2}\cos^2\frac{\theta_2}{2}\end{bmatrix}}\tag{[P5a]}
$$

(둘째 성분: $i e^{i\theta_1}\sin\frac{\theta_2}{2}\bigl(1-\sin^2\frac{\theta_2}{2}\bigr)=ie^{i\theta_1}\sin\frac{\theta_2}{2}\cos^2\frac{\theta_2}{2}$.) 검문 $\langle\psi,(\partial_1\psi)_\perp\rangle=0$ ✓ [P5b] — 가짜 성분이 정확히 제거됐다. $\partial_2\psi$는 (4)$=0$이라 이미 수직: $(\partial_2\psi)_\perp=\partial_2\psi$ [P5c].

사영된 것의 길이:

$$
\bigl\|(\partial_1\psi)_\perp\bigr\|^2
=\sin^4\tfrac{\theta_2}{2}\cos^2\tfrac{\theta_2}{2}+\sin^2\tfrac{\theta_2}{2}\cos^4\tfrac{\theta_2}{2}
=\sin^2\tfrac{\theta_2}{2}\cos^2\tfrac{\theta_2}{2}\underbrace{\bigl(\sin^2+\cos^2\bigr)}_{=1}
=\tfrac14\sin^2\theta_2. \tag{[P5d]}
$$

### (c) 공식은 이 사영의 전개형이다

일반 항등식 하나로 (b)가 공식과 같은 것임을 확정한다. $\|\psi\|^2=1$이면

$$
\bigl\langle(\partial_i\psi)_\perp,(\partial_j\psi)_\perp\bigr\rangle
=\langle\partial_i\psi,\partial_j\psi\rangle
-\underbrace{\langle\partial_i\psi,\psi\rangle\langle\psi,\partial_j\psi\rangle}_{\text{교차항 ①}}
-\underbrace{\langle\partial_i\psi,\psi\rangle\langle\psi,\partial_j\psi\rangle}_{\text{교차항 ②}}
+\underbrace{\langle\partial_i\psi,\psi\rangle\|\psi\|^2\langle\psi,\partial_j\psi\rangle}_{\text{사영끼리}}
$$

$$
=\langle\partial_i\psi,\partial_j\psi\rangle-\langle\partial_i\psi,\psi\rangle\langle\psi,\partial_j\psi\rangle. \tag{[P6]}
$$

**둘째 항이 빼는 것 = 위상 성분, 그게 전부다.** "QFIM의 기본정의"라고 적었던 줄은 정의가 아니라 $4\,\mathrm{Re}\langle(\partial\psi)_\perp,(\partial\psi)_\perp\rangle$의 전개형이었다. 따라서 (b)에서 이미

$$
H_{11}=4\bigl\|(\partial_1\psi)_\perp\bigr\|^2=\sin^2\theta_2
$$

— 공식을 쓰기 전에 답이 나와 있다.

### (d) 유클리드 다리 — trace가 내적인 이유, 그 논법 그대로

남은 질문: 사영된 길이가 **무슨** 길이인가. 이전 노트에서 $\mathrm{Tr}$가 내적인 이유를 유클리드로 보였던 그 다리를 여기 놓는다.

**Bloch 좌표가 구면점을 되돌려준다.** $n_a:=\mathrm{Tr}(P\sigma_a)$로 정의하면, 우리 $\psi$에 대해 성분별로

$$
n_1=2\,\mathrm{Re}(\bar\psi_1\psi_2)=2\cos\tfrac{\theta_2}{2}\sin\tfrac{\theta_2}{2}\cos\theta_1=\sin\theta_2\cos\theta_1,\quad
n_2=\sin\theta_2\sin\theta_1,\quad
n_3=|\psi_1|^2-|\psi_2|^2=\cos\theta_2,
$$

$$
\boxed{\ \vec n=p(\theta_1,\theta_2)\ }\tag{[P1]}
$$

— 입체사영으로 내려갔다가 $\psi$로 올라온 것이 **정확히 그 구면점**으로 돌아온다. Example 1이 예시인 진짜 이유가 이 줄이다.

**사영자의 접공간은 $\sum x_i\sigma_i$ 꼴이고, 거기서 trace 내적은 유클리드다.** $P=\tfrac12(I+\vec n\cdot\vec\sigma)$이므로 $I$-부분은 상수라서

$$
dP=\tfrac12\,d\vec n\cdot\vec\sigma\ \in\ \mathrm{span}\{\sigma_1,\sigma_2,\sigma_3\}, \tag{[P3]}
$$

즉 $dn_1,dn_2,dn_3$은 $\sigma_1,\sigma_2,\sigma_3$ — $x,y,z$ 방향 — 에 대한 진짜 변위 성분이다. 그 공간에서 $\sigma_a\sigma_b=\delta_{ab}I+i\varepsilon_{abc}\sigma_c$이고 $\mathrm{Tr}\,\sigma_c=0$, $\mathrm{Tr}\,I=2$이므로

$$
\mathrm{Tr}\bigl[(\vec x\cdot\vec\sigma)(\vec y\cdot\vec\sigma)\bigr]=2\,\vec x\cdot\vec y
\qquad\text{— 계수 2만 빼면 유클리드 내적 그 자체.}\tag{[P2]}
$$

따라서

$$
\mathrm{Tr}(dP\,dP)=\tfrac14\cdot2\,|d\vec n|^2=\tfrac12\,|d\vec n|^2. \tag{[P4]}
$$

**같은 $\mathrm{Tr}(dP\,dP)$를 $\psi$ 쪽에서 열면 사영이 나온다.** $dP=d\psi\,\psi^*+\psi\,d\psi^*$를 넣고 네 항을 전부 쓴다 ($\mathrm{Tr}[ab^*]=\langle b,a\rangle$, $s:=\langle\psi,d\psi\rangle$):

$$
\mathrm{Tr}(dP\,dP)
=\underbrace{s^2}_{d\psi\psi^*d\psi\psi^*}
+\underbrace{\langle d\psi,d\psi\rangle}_{d\psi\psi^*\psi d\psi^*}
+\underbrace{\langle d\psi,d\psi\rangle}_{\psi d\psi^*d\psi\psi^*}
+\underbrace{\bar s^2}_{\psi d\psi^*\psi d\psi^*}
$$

$s$는 순허수((2)의 관찰)이므로 $s^2+\bar s^2=-2|s|^2$:

$$
\mathrm{Tr}(dP\,dP)=2\bigl[\langle d\psi,d\psi\rangle-|\langle\psi,d\psi\rangle|^2\bigr]
=2\,\bigl\langle d\psi_\perp,d\psi_\perp\bigr\rangle .
$$

두 줄을 붙이면 사슬이 닫힌다:

$$
\boxed{\ H=4\,\langle d\psi_\perp,d\psi_\perp\rangle=2\,\mathrm{Tr}(dP\,dP)=|d\vec n|^2\ }\tag{[P7]}
$$

**공식이 재는 것은 구면 변위 $d\vec n$의 진짜 유클리드 길이다.** 우리 예시에서 $\vec n=p$이므로 $H_{ij}=\partial_i p\cdot\partial_j p$ — 아래 조립은 이 사실을 성분으로 읽어내는 일일 뿐이다.

### (e) 같은 사슬을 숫자로 — $\theta_1=\tfrac\pi2,\ \theta_2=\tfrac\pi3$ 에서

기호로 본 현상을 이제 **값**으로 본다. 이 점을 고른 이유: $\sin\frac{\theta_2}{2}=\frac12$, $\cos\frac{\theta_2}{2}=\frac{\sqrt3}{2}$, $e^{i\theta_1}=i$ — 전부 정확한 수로 떨어진다. 구면점은

$$
p=\bigl(\cos\tfrac\pi2\sin\tfrac\pi3,\ \sin\tfrac\pi2\sin\tfrac\pi3,\ \cos\tfrac\pi3\bigr)=\Bigl(0,\ \tfrac{\sqrt3}{2},\ \tfrac12\Bigr).
$$

**사영 값.** $z=\tan30°\,e^{i\pi/2}=\dfrac{i}{\sqrt3}$, $|z|=\tfrac{1}{\sqrt3}\approx0.577$ [N1]. 노트의 E1 식이면 $z=\tfrac23 i$, $|z|\approx0.667$ — **같은 점이 다른 곳에 떨어진다.** 이 차이가 아래 모든 값을 오염시켰던 것.

**상태 값.** $\psi=\bigl(\tfrac{\sqrt3}{2},\ \tfrac i2\bigr)$, $\|\psi\|^2=\tfrac34+\tfrac14=1$ [N2a]. 노트의 $\tilde\psi=\bigl(\tfrac9{13},\tfrac6{13}i\bigr)$이면 $\|\tilde\psi\|^2=\tfrac{81+36}{169}=\tfrac9{13}\approx0.692$ [N2b] — 별표 조건 위반이 **숫자로** 보인다.

**가짜 성분이 실제로 있다.** $\partial_1\psi=\bigl(0,\ i\cdot i\cdot\tfrac12\bigr)=\bigl(0,-\tfrac12\bigr)$ [N3a]. 위상 성분:

$$
\langle\psi,\partial_1\psi\rangle=\overline{\bigl(\tfrac i2\bigr)}\bigl(-\tfrac12\bigr)=\tfrac i4\ \neq0\quad\text{[N3b]},
\qquad
\psi\cdot\tfrac i4=\Bigl(\tfrac{\sqrt3}{8}i,\ -\tfrac18\Bigr)\quad\text{[N3c]}.
$$

빼면:

$$
(\partial_1\psi)_\perp=\bigl(0,-\tfrac12\bigr)-\Bigl(\tfrac{\sqrt3}{8}i,-\tfrac18\Bigr)
=\Bigl(-\tfrac{\sqrt3}{8}i,\ -\tfrac38\Bigr)\quad\text{[N3d]}.
$$

**길이의 회계** — 사영이 무엇을 빼는지가 값으로 갈라진다 [N4]:

$$
\underbrace{\|\partial_1\psi\|^2=\tfrac14}_{\text{전체}}
\;=\;
\underbrace{\bigl|\tfrac i4\bigr|^2=\tfrac1{16}}_{\text{가짜(위상)}}
\;+\;
\underbrace{\|(\partial_1\psi)_\perp\|^2=\tfrac{3}{16}}_{\text{진짜(구면 이동)}}
$$

$4$배 하면: 사영 없이 조립하면 $H_{11}=1$로 **과대평가**, 사영하면 $H_{11}=\tfrac34=\sin^2 60°$ — 정답.

**되돌아오는 값.** $\bar\psi_1\psi_2=\tfrac{\sqrt3}{2}\cdot\tfrac i2=\tfrac{\sqrt3}{4}i$ 에서

$$
\vec n=\Bigl(2\,\mathrm{Re}\tfrac{\sqrt3}{4}i,\ 2\,\mathrm{Im}\tfrac{\sqrt3}{4}i,\ \tfrac34-\tfrac14\Bigr)
=\Bigl(0,\ \tfrac{\sqrt3}{2},\ \tfrac12\Bigr)=p\quad\text{[N5]}.
$$

**같은 $\tfrac34$이 세 번 나온다** [N6]: $\partial_1\vec n=(-\tfrac{\sqrt3}{2},0,0)$이므로

$$
4\|(\partial_1\psi)_\perp\|^2=\tfrac34,\qquad
2\,\mathrm{Tr}(\partial_1P\,\partial_1P)=2\cdot\tfrac38=\tfrac34,\qquad
|\partial_1\vec n|^2=\tfrac34 .
$$

상태벡터의 사영 길이, 사영자의 trace, 구면의 유클리드 길이 — §(d) 사슬의 세 고리가 한 숫자에서 만난다.

**교차 성분도 값으로.** $\partial_2\psi=\bigl(-\tfrac14,\ \tfrac{\sqrt3}{4}i\bigr)$ (위상 성분 $0$, $4\|\cdot\|^2=1=|\partial_2\vec n|^2$ [N8]),

$$
Q_{12}=\overline{\bigl(-\tfrac12\bigr)}\cdot\tfrac{\sqrt3}{4}i=-\tfrac{\sqrt3}{8}i
\quad\text{[N7]}\qquad
\Longrightarrow\quad H_{12}=4\,\mathrm{Re}=0,\qquad F_{12}=-2\,\mathrm{Im}=\tfrac{\sqrt3}{4}=\tfrac12\sin60°.
$$

"여튼 복소부가 있기는 하다"의 그 복소부가 $-\tfrac{\sqrt3}{8}i$라는 **구체적인 수**로 잡힌다.

**노트 식의 값.** 원본 4쪽 마지막 줄에 $c=1+\cos60°=\tfrac32$를 넣으면

$$
\frac{4c^2(1-c^2)}{(1+c^2)^2}=-\frac{180}{169}\approx-1.065\quad\text{[N9]}
$$

— 길이의 제곱이 $-1.065$. 참값 $+\tfrac34$와 나란히 놓으면, 이 계산이 멈출 수밖에 없었던 이유가 숫자 하나로 요약된다.

---

## ▢ $H_{11}$  *(노트 4쪽의 자리 — 🖍 한 곳)*

위 §(b)에서 사영만으로 $H_{11}=4\|(\partial_1\psi)_\perp\|^2=\sin^2\theta_2$를 이미 얻었다. 공식(=전개형)으로 다시 조립해 일치를 확인한다. (1)·(2)를 넣고, 둘째 항은 구조상 $\bigl|\langle\psi,\partial_1\psi\rangle\bigr|^2$ (실수):

$$
H_{11}=4\Bigl[\sin^2\tfrac{\theta_2}{2}-\sin^4\tfrac{\theta_2}{2}\Bigr]
=4\sin^2\tfrac{\theta_2}{2}\cos^2\tfrac{\theta_2}{2}
=\boxed{\sin^2\theta_2}\tag{[5a]}
$$

> 🖍 **빨간펜 (E3).** 노트 4쪽은 같은 조립에서 둘째 항을 $\dfrac{c^4}{(1+c^2)^2}$로 적었다 — 올바른 값은 $\Bigl|\dfrac{-ic^2}{(1+c^2)^2}\Bigr|^2=\dfrac{c^4}{(1+c^2)^4}$. **분모의 $(1+c^2)^2$ 하나가 증발**했고, 그 결과가 4쪽 마지막 줄 $H_{11}=\dfrac{4c^2(1-c^2)}{(1+c^2)^2}$이다 [8d]. 이 식은 $c>1$(북반구)에서 **음수** [8f].

**음수가 나올 수 없는 이유** — $\partial_1\psi=iN\psi$, $N=\mathrm{diag}(0,1)$ [5e] 이므로

$$
H_{11}=4\Bigl[\langle\psi,N^2\psi\rangle-\langle\psi,N\psi\rangle^2\Bigr]=4\,\mathrm{Var}_\psi(N)\ \ge 0. \tag{[5f]}
$$

QFIM 대각성분 = 생성원의 분산 네 배 (기준집 ⑤P082). 사영의 언어로는: 분산 $=$ 사영된 벡터의 길이제곱이니 음수일 수 없다. 분산이 음수로 나온 순간이 노트의 경보였다.

---

## ▢ $H_{12}$ — "여튼 복소부가 있기는 하다"  *(노트 5–6쪽의 자리)*

괄호를 통째로 이름 붙인다 — §(c)에 의해 이것은 **사영된 것끼리의 내적**이다:

$$
Q_{12}:=\langle\partial_1\psi,\partial_2\psi\rangle-\langle\partial_1\psi,\psi\rangle\langle\psi,\partial_2\psi\rangle
=\bigl\langle(\partial_1\psi)_\perp,(\partial_2\psi)_\perp\bigr\rangle .
$$

(5)와, (2)의 켤레 $\langle\partial_1\psi,\psi\rangle=-i\sin^2\tfrac{\theta_2}{2}$, 그리고 (4)$=0$:

$$
Q_{12}=-\tfrac{i}{4}\sin\theta_2-\bigl(-i\sin^2\tfrac{\theta_2}{2}\bigr)\cdot 0
=\boxed{-\tfrac{i}{4}\sin\theta_2}\tag{[5d]}
$$

**순허수다.** 따라서

$$
H_{12}=4\,\mathrm{Re}\,Q_{12}=0. \tag{[5b]}
$$

노트 5쪽이 $\mathrm{Re}(\cdots)=0$을 얻고 6쪽에서 "여튼 복소부가 있기는 하다"고 적은 것 — **둘 다 옳았다** (E1·E2 상태에서도 이 구조는 살아남는다). 사영된 두 접벡터가 복소 내적을 갖는 공간에서 만나므로, 내적의 실부(길이·각도)와 허부(면적)가 함께 나온다. 버릴 관찰이 아니라 계량의 쌍둥이다:

$$
F_{12}:=-2\,\mathrm{Im}\,Q_{12}=\tfrac12\sin\theta_2\quad\text{[7a]},\qquad
F=\tfrac12\sin\theta_2\,d\theta_1\wedge d\theta_2 .
$$

$F$는 Berry curvature이고, FS 넓이형식 $dA_{FS}=\sqrt{\det(H/4)}\;d\theta_1\wedge d\theta_2=\tfrac14\sin\theta_2\,d\theta_1\wedge d\theta_2$와 비교하면

$$
F=2\,dA_{FS}\quad\text{[7b]}\qquad\text{— 기준집 ③ 정규화 경고의 그 }d\alpha=2dA_{FS}\text{와 같은 factor 2,}
$$

$$
\int_{S^2}F=\int_0^{2\pi}\!\!\int_0^\pi \tfrac12\sin\theta_2\,d\theta_2\,d\theta_1=\tfrac12\cdot2\pi\cdot\Bigl[-\cos\theta_2\Bigr]_0^\pi=2\pi
\qquad(c_1=1).\ \text{[7c]}
$$

즉 $Q=\underbrace{\tfrac14 H}_{\text{실부: 계량}}-\underbrace{\tfrac i2 F_{(\cdot)}}_{\text{허부: Kähler/Berry}}$ 한 몸이다.

---

## ▢ $H_{22}$ — 노트가 멈춘 자리

한 줄이었다. (3)과 (4):

$$
H_{22}=4\Bigl[\langle\partial_2\psi,\partial_2\psi\rangle-\bigl|\langle\psi,\partial_2\psi\rangle\bigr|^2\Bigr]
=4\Bigl[\tfrac14-0\Bigr]=\boxed{1}\tag{[5c]}
$$

---

## ▢ 조립 — 설계대로인지 확인

$$
\boxed{\ H=\begin{pmatrix}\sin^2\theta_2&0\\[2pt]0&1\end{pmatrix}\ }
\qquad\text{— 단위 Bloch 구면의 round 계량.}
$$

§(d)가 예고한 대로 $H_{ij}=\partial_i\vec n\cdot\partial_j\vec n=\partial_ip\cdot\partial_jp$여야 한다. 성분으로 확인:

$$
\partial_1 p=(-\sin\theta_1\sin\theta_2,\ \cos\theta_1\sin\theta_2,\ 0),\qquad
\partial_2 p=(\cos\theta_1\cos\theta_2,\ \sin\theta_1\cos\theta_2,\ -\sin\theta_2),
$$

$$
\partial_1p\cdot\partial_1p=\sin^2\theta_2,\quad
\partial_1p\cdot\partial_2p=0,\quad
\partial_2p\cdot\partial_2p=1.\ \checkmark\ \text{[6a]}
$$

QFIM은 새 계량이 아니라 **ambient 내적이 유도한 그 계량**이다 (기준집 ⑤P101). 나머지 두 방향 교차검산:

- **$z$-좌표로 내리기.** $z=\tan\frac{\theta_2}{2}e^{i\theta_1}$의 pullback으로 $\dfrac{4|dz|^2}{(1+|z|^2)^2}$를 당기면 성분별로 정확히 $H$ [6b] — 검산 기준 "$4/D^2$가 세 방식에서 모두"의 state-vector 방식 완료.
- **사영자 방식.** $2\,\mathrm{Tr}(\partial_iP\,\partial_jP)$를 직접 조립해도 성분별로 $H$ [6c] — §(d) 사슬의 가운데 고리를 독립적으로 재확인.

> **factor 지도** (한 줄): $\ H\ =\ \text{round}(K{=}1)\ =\ 2\,\mathrm{Tr}(dP\,dP)\ =\ 4\,g_{FS}$, $\quad F=2\,dA_{FS}$.

---

## ▢ 원본 노트에서 바뀐 줄 — 정확히 세 줄

| 쪽 | 원본 | 고침 | 검산 |
|---|---|---|---|
| 2 | $z=\dfrac{e^{i\theta_1}}{1+\cos\theta_2}$ | $z=\dfrac{\sin\theta_2\,e^{i\theta_1}}{1+\cos\theta_2}=\tan\dfrac{\theta_2}{2}e^{i\theta_1}$ | [1a–c] |
| 2 | $\psi=\dfrac{1}{1+\lvert z\rvert^2}\begin{bmatrix}1\\z\end{bmatrix}$ | $\psi=\dfrac{1}{\sqrt{1+\lvert z\rvert^2}}\begin{bmatrix}1\\z\end{bmatrix}$ | [2a–c, 8a] |
| 4 | 둘째 항 분모 $(1+c^2)^2$ | $(1+c^2)^4$ | [8b–d] |

그 외 — 3쪽의 미분 전개, 5쪽의 $\mathrm{Re}=0$, 6쪽의 "복소부가 있다" — 는 **전부 유효**했다.

**원본 재현 검산** (진단이 추측이 아님을 실측): E1·E2 상태의 $\tilde\psi=\dfrac{1}{1+c^2}\begin{bmatrix}c^2\\ce^{i\theta_1}\end{bmatrix}$로 4쪽 파이프라인을 돌리면 첫 항 $\dfrac{c^2}{(1+c^2)^2}$은 노트와 일치하고 [8b], 둘째 항의 분모를 $(1+c^2)^4\to(1+c^2)^2$로 바꾸는 순간 노트 4쪽 마지막 줄 $\dfrac{4c^2(1-c^2)}{(1+c^2)^2}$이 문자 그대로 나온다 [8d]. E3만 고쳐도 E1·E2 때문에 $\sin^2\theta_2$는 안 된다 [8e] — 세 줄이 각각 독립적으로 필요했다.

---

## ▢ 다음 — 이 결 그대로 Gr(2,4)

사영 구조가 그대로 승격된다: $z\to Z$ (2×2 복소행렬), $1+|z|^2\to\det(I+Z^\dagger Z)$, $\psi\to V=\begin{bmatrix}I\\Z\end{bmatrix}(I+Z^\dagger Z)^{-1/2}$, 그리고 위상 원 $e^{i\alpha}$의 자리에 **frame 회전 $U(2)$**가 들어와 가짜 방향이 1개에서 4개로 늘어난다 — 사영 $(1-P)dV$가 그것들을 제거하고:

$$
H=4\,\mathrm{Re}\,\mathrm{tr}\Bigl[(I+Z^\dagger Z)^{-1}dZ^\dagger\,(I+ZZ^\dagger)^{-1}dZ\Bigr].
$$

유도·검산·Plücker 대응은 문서 5 §4, 문제 트랙은 책 14장 (⑤P083–P091 → ④P041–P088).

---

## 부록 A. verify5b 실행 로그 (sympy, 55/55)

```
[OK] [1a] t* = 1/(1+cos θ2)
[OK] [1b] z = sinθ2/(1+cosθ2) e^{iθ1} = tan(θ2/2) e^{iθ1}
[OK] [1c] E1 확인: 노트의 z는 sinθ2 배 빠져 있다 (z = sinθ2 · z_note)
[OK] [2a] 1+|z|² = 1/cos²(θ2/2)
[OK] [2b] ψ = (1/√(1+|z|²))(1,z)ᵀ = (cos(θ2/2), e^{iθ1} sin(θ2/2))ᵀ
[OK] [2c] ‖ψ‖² = 1  (E2 해소: Assertion 1)
[OK] [3a] ∂₁ψ = (0, i e^{iθ1} sin(θ2/2))ᵀ
[OK] [3b] ∂₂ψ = (−½sin(θ2/2), ½e^{iθ1} cos(θ2/2))ᵀ
[OK] [4] ⟨∂₁ψ,∂₁ψ⟩ = sin²(θ2/2)
[OK] [4] ⟨ψ,∂₁ψ⟩ = i sin²(θ2/2)
[OK] [4] ⟨∂₂ψ,∂₂ψ⟩ = 1/4
[OK] [4] ⟨ψ,∂₂ψ⟩ = 0
[OK] [4] ⟨∂₁ψ,∂₂ψ⟩ = −(i/4) sinθ2
[OK] [P1] Bloch 좌표 n_a = Tr(Pσ_a) 가 정확히 Example 1의 구면점 p
[OK] [P2] 접공간 Σx_iσ_i 위의 trace 내적: Tr[(x·σ)(y·σ)] = 2 x·y  (계수 2 빼고 유클리드)
[OK] [P3] ∂_iP = ½ (∂_i n⃗)·σ⃗  (I-성분 없음: 사영자의 접공간은 Σx_iσ_i 꼴)
[OK] [P4] Tr(∂_iP ∂_jP) = ½ ∂_i n⃗·∂_j n⃗  (P2+P3 의 귀결)
[OK] [P5a] (∂₁ψ)_⊥ = (−i sin²(θ2/2)cos(θ2/2),  i e^{iθ1} sin(θ2/2)cos²(θ2/2))ᵀ
[OK] [P5b] ⟨ψ,(∂₁ψ)_⊥⟩ = 0  (위상 성분이 정확히 제거됨)
[OK] [P5c] (∂₂ψ)_⊥ = ∂₂ψ  (∂₂ψ 는 애초에 위상 성분이 없다)
[OK] [P5d] 4‖(∂₁ψ)_⊥‖² = sin²θ2  (공식 없이, 사영된 길이만으로 H11)
[OK] [P6] 항등식: ⟨(∂_iψ)_⊥,(∂_jψ)_⊥⟩ = ⟨∂_iψ,∂_jψ⟩−⟨∂_iψ,ψ⟩⟨ψ,∂_jψ⟩  (공식의 괄호 = 사영된 내적)
[OK] [P7] H_ij = ∂_i n⃗·∂_j n⃗  (H = 진짜 유클리드 길이 |dn⃗|²)
[OK] [5a] H11 = sin²θ2
[OK] [5b] H12 = H21 = 0
[OK] [5c] H22 = 1
[OK] [5d] Q12 = −(i/4) sinθ2 (순허수 — '여튼 복소부가 있기는 하다')
[OK] [5e] ∂₁ψ = iNψ, N=diag(0,1)
[OK] [5f] H11 = 4·Var_ψ(N) ≥ 0 (기준집 ⑤P082)
[OK] [6a] H = (∂_i p·∂_j p)  — 단위구면 제1기본형식과 성분 일치
[OK] [6b] (4/D² round 계량의 pullback) = H — '4/D²가 세 방식 모두'
[OK] [6c] 2Tr(∂_iP ∂_jP) = H  (사영자 방식)
[OK] [7a] F12 := −2 Im Q12 = ½ sinθ2
[OK] [7b] F = 2·dA_FS  (기준집 경고 dα = 2dA_FS 의 그 factor)
[OK] [7c] ∫F = 2π  (c₁ = 1)
[OK] [8a] ‖ψ̃‖² = c²/(1+c²) ≠ 1  (E2의 증상)
[OK] [8b] 첫 항 = c²/(1+c²)²  (노트 4쪽과 일치)
[OK] [8c] 둘째 항 = c⁴/(1+c²)⁴  (올바른 값)
[OK] [8d] E3 재현: 둘째 항의 분모를 (1+c²)⁴→(1+c²)² 로 쓰면 노트 4쪽 식 그대로
[OK] [8e] E3만 고쳐도 (E1·E2 때문에) sin²θ2 가 아니다
[OK] [8f] 노트 4쪽 식은 c>1 (북반구 θ2<π/2) 에서 음수 — H=4Var≥0 모순
[OK] [N1] z = i/√3  (|z| = 1/√3 ≈ 0.577;  노트의 z라면 (2/3)i, |z| = 0.667)
[OK] [N2a] ψ = (√3/2, i/2),  ‖ψ‖² = 3/4 + 1/4 = 1
[OK] [N2b] 노트의 ψ̃ = (9/13, 6i/13),  ‖ψ̃‖² = 117/169 = 9/13 ≠ 1
[OK] [N3a] ∂₁ψ = (0, −1/2)
[OK] [N3b] ⟨ψ,∂₁ψ⟩ = i/4  (가짜 위상 성분의 크기)
[OK] [N3c] 위상 성분 벡터 ψ·(i/4) = (√3i/8, −1/8)
[OK] [N3d] (∂₁ψ)_⊥ = (−√3i/8, −3/8)
[OK] [N4] 길이의 회계: ‖∂₁ψ‖² = 1/4 = (가짜 1/16) + (진짜 3/16);  4·(3/16) = 3/4 = sin²60°
[OK] [N5] Bloch 값: n⃗ = (0, √3/2, 1/2) = p(π/2, π/3)  (숫자로 되돌아옴)
[OK] [N6] 같은 3/4 세 번: 4‖(∂₁ψ)_⊥‖² = 2Tr(∂₁P∂₁P) = |∂₁n⃗|² = 3/4
[OK] [N7] Q12 = −√3i/8 (순허수 → H12 = 0),  F12 = −2ImQ12 = √3/4 = ½sin60°
[OK] [N8] H22 값: ∂₂ψ = (−1/4, √3i/4) 는 위상 성분 0 → 4‖∂₂ψ‖² = 1 = |∂₂n⃗|²
[OK] [N9] 노트 4쪽 식의 값: c = 3/2 에서 −180/169 ≈ −1.065 < 0  (참값 +3/4)
```
