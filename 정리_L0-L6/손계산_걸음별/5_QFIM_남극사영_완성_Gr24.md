# 5. QFIM 손계산 완성 — 남극 입체사영에서 막힌 지점부터 Gr(2,4) 기술까지

> **대상 손노트**: `Notes_260704_170213.pdf` (6쪽, "ℂP¹의 QFIM 계산하기").
> **기준 문서**: `원본노트/Gr24_핵심계산모음.pdf` (이하 **기준집**). 이 문서의 모든 규약·검산 기준값은 기준집의 문제 번호(P0xx)로 지시한다.
> **검산 스크립트**: 같은 폴더의 `verify5_qfim.py` (sympy + numpy, 실행 출력은 부록 A).

---

## 0. 한눈에

손노트는 세 군데에서 깨졌고(§1), 그 중 두 개(E2·E3)가 합쳐져 **H₁₁이 음수가 되는 식**을 만들었다. 분산이 음수로 나오는 순간 더 갈 수 없었던 것. 세 줄을 고치면 계산은 끝까지 닫히고, 답은

$$
\boxed{\ H=\begin{pmatrix}\sin^2\theta_2&0\\0&1\end{pmatrix}\ }\qquad(\theta_1=\text{방위각},\ \theta_2=\text{극각})
$$

— **QFIM = 단위 Bloch 구면의 round 계량**이다 (기준집 P015: $ds^2_{FS}=\tfrac14(d\theta_2^2+\sin^2\theta_2\,d\theta_1^2)$, QFIM $=4\,ds^2_{FS}$).

마지막 쪽의 관찰 "**여튼 복소부가 있기는 하다**"는 옳았고, 버릴 게 아니라 **계량의 쌍둥이**다: 그 복소부가 Kähler 형식(= FS 넓이형식 = Berry curvature의 절반)이다(§3). Gr(2,4)로 올라가면 이 구조 전체(계량 + 복소부)가 그대로 살아남는다(§4).

---

## 1. 진단 — 손노트를 줄 단위로 재현하기

### 1.1 손노트의 흐름

| 쪽 | 내용 | 판정 |
|---|---|---|
| 1 | $\mathbb C^2\setminus\{0\}\to\mathbb{CP}^1$, $[1:z]$, $\psi(z)=\tfrac{1}{\sqrt{1+\lvert z\rvert^2}}\binom1z$, rank-1 사영자 | ✔ |
| 2 | 구면점 $p(\theta_1,\theta_2)$ 남극 입체사영 → $z$, 그걸로 $\psi(\theta_1,\theta_2)$ | ✘ **E1, E2** |
| 3 | $\partial_1\psi$, $\partial_2\psi$ (quotient rule 전개) | ✔ (입력 기준 정확) |
| 4 | $H_{11}$ 조립 | ✘ **E3** |
| 5–6 | $H_{12}$: 실부 $=0$, "복소부가 있기는 하다" | ✔ (관찰 옳음) |

미분 자체(3쪽)는 **입력 기준으로 정확했다**. sympy로 3쪽의 $\partial_1\psi$ 줄과 $\partial_2\psi$ 최종 줄을 그대로 옮겨 직접 미분과 비교하면 성분별 일치한다(부록 [1b][1c]). 깨진 것은 입력 두 줄(2쪽)과 조립 한 줄(4쪽)이다.

### 1.2 E1 — 입체사영에서 $\sin\theta_2$가 빠졌다

손노트 2쪽:

$$
z \overset{\text{노트}}{=} \frac{1}{1+\cos\theta_2}\,e^{i\theta_1}.\tag{E1}
$$

남극 입체사영을 처음부터 유도한다. 구면점과 남극:

$$
p(\theta_1,\theta_2)=(\sin\theta_2\cos\theta_1,\ \sin\theta_2\sin\theta_1,\ \cos\theta_2),\qquad S=(0,0,-1).
$$

$S$에서 $p$를 지나는 직선을 매개변수 $t$로 쓰면 ($t=0$에서 $S$, $t=1$에서 $p$):

$$
\ell(t)=S+t\,(p-S)=\bigl(t\sin\theta_2\cos\theta_1,\ \ t\sin\theta_2\sin\theta_1,\ \ -1+t(\cos\theta_2+1)\bigr).
$$

적도평면($3$성분 $=0$)과 만나는 $t^\*$:

$$
-1+t^\*(1+\cos\theta_2)=0\quad\Longrightarrow\quad t^\*=\frac{1}{1+\cos\theta_2}.
$$

이 $t^\*$를 앞 두 성분에 **곱해서** 교점을 얻는다:

$$
(x,y)=\frac{(\sin\theta_2\cos\theta_1,\ \sin\theta_2\sin\theta_1)}{1+\cos\theta_2},
\qquad
\boxed{\ z=x+iy=\frac{\sin\theta_2}{1+\cos\theta_2}\,e^{i\theta_1}\ }.
$$

노트의 (E1)은 $t^\*=\frac1{1+\cos\theta_2}$ 까지만 쓰고 **분자의 $\sin\theta_2$를 곱하지 않은 형태**다. 즉시 검출법: 북극 $\theta_2=0$은 원점 $z=0$으로 가야 하는데 (E1)은 $z=\tfrac12 e^{i\theta_1}$을 준다 — 북극이 반지름 $\tfrac12$ 원으로 퍼진다.

반각으로 정리(모든 단계):

$$
\sin\theta_2=2\sin\tfrac{\theta_2}2\cos\tfrac{\theta_2}2,\qquad
1+\cos\theta_2=1+\bigl(2\cos^2\tfrac{\theta_2}2-1\bigr)=2\cos^2\tfrac{\theta_2}2,
$$

$$
\Longrightarrow\quad
z=\frac{2\sin\frac{\theta_2}2\cos\frac{\theta_2}2}{2\cos^2\frac{\theta_2}2}\,e^{i\theta_1}
=\boxed{\ \tan\tfrac{\theta_2}2\ e^{i\theta_1}\ }.
$$

이것이 기준집 **P017**의 $w=e^{i\phi}\tan\frac\theta2$ 와 문자 그대로 같다(기호만 $\phi\to\theta_1$, $\theta\to\theta_2$).

### 1.3 E2 — 정규화에서 제곱근이 빠졌다

손노트 2쪽은 $\psi=\dfrac{1}{1+\frac{1}{(1+\cos\theta_2)^2}}\binom{1}{z}$ 로 썼다. 올바른 정규화는 $\dfrac{1}{\sqrt{1+|z|^2}}$ 인데 **제곱근이 없다**. 노트의 $c:=1+\cos\theta_2$ 표기로 노트의 $\psi$는

$$
\psi_{\text{노트}}=\frac{1}{1+c^2}\binom{c^2}{c\,e^{i\theta_1}},\qquad
\|\psi_{\text{노트}}\|^2=\frac{c^4+c^2}{(1+c^2)^2}=\frac{c^2(c^2+1)}{(1+c^2)^2}=\frac{c^2}{1+c^2}\ \ne 1.
$$

예: $\theta_2=\tfrac\pi2$이면 $c=1$이고 $\|\psi\|^2=\tfrac12$. 기준집 3단계의 **Assertion 1**("모든 pure state는 normalize한다, $\langle\psi|\psi\rangle=1$")이 깨졌으므로, 그 아래에서 쓰는 QFIM 공식

$$
H_{ij}=4\,\mathrm{Re}\bigl[(\partial_i\psi)^*(\partial_j\psi)-(\partial_i\psi)^*\psi\cdot\psi^*(\partial_j\psi)\bigr]
$$

의 전제(P021 유도에서 $\psi^*\psi=1$을 명시적으로 사용)가 성립하지 않는다. 이후의 모든 값은 **공식의 적용 범위 밖**이다.

### 1.4 E3 — 4쪽 조립에서 분모 $(1+c^2)^2$ 하나가 증발했다

4쪽 중간, $\mathrm{Re}\bigl[(\partial_1\psi)^*\psi\cdot\psi^*(\partial_1\psi)\bigr]$ 계산. 괄호 **각각**이 $\tfrac1{1+c^2}$ 짜리 벡터 두 개의 내적이므로 **각각 $\tfrac{1}{(1+c^2)^2}$ 인자를 갖고**, 곱은 $\tfrac{1}{(1+c^2)^4}$이어야 한다:

$$
(\partial_1\psi)^*\psi=\frac{-i\,c^2}{(1+c^2)^2},\qquad
\psi^*(\partial_1\psi)=\frac{+i\,c^2}{(1+c^2)^2}
\quad\Longrightarrow\quad
\text{곱}=\frac{c^4}{(1+c^2)^{4}}.
$$

노트는 이것을 $\dfrac{c^4}{(1+c^2)^{2}}$ 로 적었다(제곱 하나 누락). 그 결과 4쪽 마지막 줄이

$$
H_{11}\overset{\text{노트}}{=}\frac{4}{(1+c^2)^2}\bigl[c^2-c^4\bigr]
$$

이 되는데, $c>1$ (즉 $\theta_2<\tfrac\pi2$)이면 $c^2-c^4<0$ — **음수**다. 수치로 $\theta_2=\tfrac\pi3$ ($c=\tfrac32$): $H_{11}^{\text{노트}}=-1.0651$. 기준집 **P082**가 $H_{\theta\theta}=4\,\mathrm{Var}_\psi(A)\ge0$ 임을 못 박으므로 이 식은 그 자리에서 모순이다. **여기가 계산이 멈춘 실제 지점이다.**

참고로 E3만 고치고 (E1·E2를 둔 채) 공식을 노트의 $\psi$에 기계적으로 적용하면

$$
H_{11}=\frac{4c^2\bigl[(1+c^2)^2-c^2\bigr]}{(1+c^2)^4}
\qquad(\theta_2=\tfrac\pi3:\ 0.6706)
$$

로 양수는 되지만 여전히 $\sin^2\tfrac\pi3=0.75$가 아니다. 즉 **세 군데를 모두 고쳐야** 답이 닫힌다(부록 [1d]).

### 1.5 살릴 것

- 3쪽의 quotient rule 전개 두 줄: 입력 기준 정확(부록 [1b][1c]).
- 5쪽의 결론 "$H_{12}$의 실부는 $0$, 복소부는 남는다": 노트의 $\psi$ 기준으로도 재현되고(부록 [1e]), 교정 후에도 참이며, §3에서 그 복소부의 정체가 밝혀진다.

---

## 2. 완성 — 같은 결로 끝까지

경로는 손노트 그대로: **남극 입체사영 → $z$ 차트 → $\psi=(1,z)/\sqrt{1+|z|^2}$ → $\partial_i\psi$ → 내적 4개 → $H$ 조립.**

### 2.1 좌표

§1.2에서 유도한 대로

$$
z(\theta_1,\theta_2)=\tan\tfrac{\theta_2}2\,e^{i\theta_1},\qquad 0<\theta_2<\pi .
$$

### 2.2 상태벡터

$$
S:=1+|z|^2=1+\tan^2\tfrac{\theta_2}2=\frac{\cos^2\frac{\theta_2}2+\sin^2\frac{\theta_2}2}{\cos^2\frac{\theta_2}2}=\frac{1}{\cos^2\frac{\theta_2}2},
\qquad
\frac{1}{\sqrt S}=\cos\tfrac{\theta_2}2\quad(0<\theta_2<\pi\text{에서 }\cos\tfrac{\theta_2}2>0).
$$

$$
\psi=\frac{1}{\sqrt S}\binom1z
=\binom{\cos\frac{\theta_2}2}{\ e^{i\theta_1}\sin\frac{\theta_2}2}\qquad
\Bigl(\tfrac{\tan}{\sec}=\sin\Bigr).
$$

이것이 기준집 **P012**의 $|\psi(\theta,\phi)\rangle=\cos\frac\theta2|0\rangle+e^{i\phi}\sin\frac\theta2|1\rangle$ 그 자체다. 검산: $\|\psi\|^2=\cos^2\frac{\theta_2}2+\sin^2\frac{\theta_2}2=1$ ✔ (Assertion 1 회복).

**노트의 $c$-변수로 같은 길** (손노트의 대수 스타일 유지). $c=1+\cos\theta_2$로 두면 올바른 $z=\frac{\sin\theta_2}{c}e^{i\theta_1}$에서

$$
|z|^2=\frac{\sin^2\theta_2}{c^2}=\frac{(1-\cos\theta_2)(1+\cos\theta_2)}{c^2}=\frac{(2-c)\,c}{c^2}=\frac{2-c}{c},
\qquad
S=1+|z|^2=\frac{2}{c}.
$$

$$
\psi=\sqrt{\frac c2}\,\binom{1}{\frac{\sin\theta_2}{c}e^{i\theta_1}}
=\binom{\sqrt{c/2}}{\ e^{i\theta_1}\sqrt{1-c/2}},
\qquad
\frac c2=\cos^2\tfrac{\theta_2}2,\quad 1-\frac c2=\sin^2\tfrac{\theta_2}2 .
$$

노트가 만들던 $\frac{1}{1+(1+\cos\theta_2)^2}$ 꼴의 "☆" 분모는 애초에 생기지 않는다 — $S=2/c$ 로 훨씬 단순해진다. 반각 상태는 노트 자신의 변수에서 저절로 나온다.

### 2.3 미분 (연쇄법칙 전부)

$\partial_1:=\partial_{\theta_1}$: 첫 성분은 $\theta_1$ 무관, 둘째 성분은 $e^{i\theta_1}$의 미분 $=i\,e^{i\theta_1}$:

$$
\partial_1\psi=\binom{0}{\,i\,e^{i\theta_1}\sin\frac{\theta_2}2}.
$$

$\partial_2:=\partial_{\theta_2}$: 내부미분 $\frac{d}{d\theta_2}\frac{\theta_2}2=\frac12$:

$$
\partial_2\psi=\binom{-\frac12\sin\frac{\theta_2}2}{\ \frac12 e^{i\theta_1}\cos\frac{\theta_2}2}.
$$

### 2.4 내적 다섯 개 (물리 convention: $\langle a|b\rangle=a^\dagger b$)

이하 $s:=\sin\frac{\theta_2}2,\ k:=\cos\frac{\theta_2}2$.

$$
\langle\partial_1\psi|\partial_1\psi\rangle=\overline{(ie^{i\theta_1}s)}\,(ie^{i\theta_1}s)=(-i)(i)\,s^2=s^2 .
$$

$$
\langle\partial_1\psi|\psi\rangle=\overline{(ie^{i\theta_1}s)}\,(e^{i\theta_1}s)=-i\,e^{-i\theta_1}e^{i\theta_1}s^2=-i\,s^2
\quad\Longrightarrow\quad
\langle\partial_1\psi|\psi\rangle\langle\psi|\partial_1\psi\rangle=(-is^2)(+is^2)=s^4 .
$$

$$
\langle\partial_2\psi|\partial_2\psi\rangle=\tfrac14 s^2+\tfrac14 k^2=\tfrac14 .
$$

$$
\langle\partial_2\psi|\psi\rangle=-\tfrac12 s\,k+\tfrac12 k\,s=0 .
$$

$$
\langle\partial_1\psi|\partial_2\psi\rangle=\overline{(ie^{i\theta_1}s)}\cdot\tfrac12 e^{i\theta_1}k
=-\tfrac i2\,s\,k=-\tfrac i4\sin\theta_2\quad(2sk=\sin\theta_2).
$$

### 2.5 $H$ 조립

$$
H_{11}=4\bigl[s^2-s^4\bigr]=4s^2(1-s^2)=4s^2k^2=(2sk)^2=\boxed{\sin^2\theta_2}
$$

— 노트 4쪽이 만들려던 바로 그 대각원소. $c^2-c^4$가 아니라 $s^2-s^4$가 나와야 했고, $s^2\le1$이므로 **절대 음수가 되지 않는다.**

$$
H_{22}=4\bigl[\tfrac14-0\bigr]=\boxed{1},
\qquad
H_{12}=4\,\mathrm{Re}\bigl[-\tfrac i4\sin\theta_2-(-is^2)\cdot 0\bigr]=\boxed{0}.
$$

$$
\therefore\quad
H=\begin{pmatrix}\sin^2\theta_2&0\\0&1\end{pmatrix},
\qquad
ds^2_{FS}=\tfrac{H}{4}=\tfrac14\bigl(d\theta_2^2+\sin^2\theta_2\,d\theta_1^2\bigr)\ \text{(P015와 일치)}.
$$

### 2.6 검산 4종 (기준집의 검산 기준 그대로)

**(i) affine 차트 "4/D²"** (주제 8 검산값, P008·P074). $v=(1,z)$ 정규화 전 벡터로 P074 공식을 돌리면 $g^{FS}_{z\bar z}=\frac1{(1+|z|^2)^2}$, QFIM $=4/D^2$. 위 $H$를 $z$ 차트로 당겨도 같은 값(부록 [2j]).

**(ii) Bloch 방식** $H_{ij}=\partial_i\vec n\cdot\partial_j\vec n$. $\vec n=(\sin\theta_2\cos\theta_1,\sin\theta_2\sin\theta_1,\cos\theta_2)$에서

$$
\partial_1\vec n=(-\sin\theta_2\sin\theta_1,\ \sin\theta_2\cos\theta_1,\ 0),\qquad
\partial_2\vec n=(\cos\theta_2\cos\theta_1,\ \cos\theta_2\sin\theta_1,\ -\sin\theta_2),
$$

$$
|\partial_1\vec n|^2=\sin^2\theta_2,\quad|\partial_2\vec n|^2=\cos^2\theta_2+\sin^2\theta_2=1,\quad
\partial_1\vec n\cdot\partial_2\vec n=-\sin\theta_2\cos\theta_2\sin\theta_1\cos\theta_1+\sin\theta_2\cos\theta_2\sin\theta_1\cos\theta_1=0 .
$$

일치(부록 [2h]).

**(iii) projector 방식** (P031–P037, P036의 항등식 $2\,\mathrm{Tr}(\partial_iP\,\partial_jP)=H_{ij}$). $P=\psi\psi^\dagger=\tfrac12(I+\vec n\cdot\vec\sigma)$ 이므로 $\partial_iP=\tfrac12\,\partial_i\vec n\cdot\vec\sigma$ 이고, $\mathrm{tr}(\sigma_a\sigma_b)=2\delta_{ab}$에서

$$
\mathrm{Tr}(\partial_iP\,\partial_jP)=\tfrac14\,\partial_i n_a\,\partial_j n_b\,\mathrm{tr}(\sigma_a\sigma_b)=\tfrac12\,\partial_i\vec n\cdot\partial_j\vec n
\quad\Longrightarrow\quad
2\,\mathrm{Tr}(\partial_iP\,\partial_jP)=\partial_i\vec n\cdot\partial_j\vec n=H_{ij}.
$$

직접 sympy로도 일치(부록 [2i]). — **세 방식(state vector / Bloch / projector)이 한 답**: 주제 8의 검산 조건 충족.

**(iv) 곡률** (주제 10). $ds^2=d\rho^2+f(\rho)^2d\phi^2$ 꼴($\rho=\theta_2$, $f=\sin\theta_2$, $\phi=\theta_1$)의 Gauss 곡률은 $K=-f''/f$:

$$
K_{\text{QFIM}}=-\frac{(\sin\theta_2)''}{\sin\theta_2}=-\frac{-\sin\theta_2}{\sin\theta_2}=1\quad(\text{단위구면 규격}),
$$

상수배 $\lambda g$의 곡률은 $K/\lambda$이므로 $ds^2_{FS}=H/4$이면 $K_{FS}=4$. — "네 방법 모두 $K=1$(단위구면 규격) · FS 규격이면 $K=4$" 충족(부록 [2k]).

---

## 3. "여튼 복소부가 있기는 하다" — 그 복소부의 정체

quantum geometric tensor(P014·P021의 괄호를 실부 취하기 **전** 상태로 둔 것)를

$$
Q_{ij}:=\langle\partial_i\psi|\partial_j\psi\rangle-\langle\partial_i\psi|\psi\rangle\langle\psi|\partial_j\psi\rangle
$$

로 부르면, §2.4의 값으로

$$
Q_{12}=-\tfrac i4\sin\theta_2\ \ (\text{순허수}),\qquad H_{ij}=4\,\mathrm{Re}\,Q_{ij}.
$$

즉 노트 5쪽의 관찰 그대로: 실부는 $0$, 복소부는 남는다. 그 복소부의 정체가 세 겹으로 확인된다.

**(a) FS 넓이형식.** $\sqrt{\det(H/4)}=\tfrac{\sin\theta_2}{4}=\bigl|\mathrm{Im}\,Q_{12}\bigr|$. 즉

$$
\omega:=-\,\mathrm{Im}\,Q_{12}\ d\theta_1\wedge d\theta_2=\frac{\sin\theta_2}{4}\,d\theta_1\wedge d\theta_2=dA_{FS},
\qquad
\int_{S^2}\omega=\frac{1}{4}\cdot 2\cdot 2\pi=\pi
$$

— 반지름 $\tfrac12$ 구의 넓이(기준집 43쪽 "FS metric은 round sphere 반지름 1/2"과 정합).

**(b) Berry curvature.** $A_i:=i\langle\psi|\partial_i\psi\rangle$로 두면 $A_1=-\sin^2\frac{\theta_2}2$, $A_2=0$이고

$$
F_{12}=\partial_1A_2-\partial_2A_1=\frac{d}{d\theta_2}\sin^2\tfrac{\theta_2}2=2\sin\tfrac{\theta_2}2\cos\tfrac{\theta_2}2\cdot\tfrac12=\frac{\sin\theta_2}{2}=2\,\omega_{12},
\qquad \int F=2\pi .
$$

기준집 43쪽의 정규화 경고 $d\alpha=2\,dA_{FS}$, $\int\Omega=2\pi$ 가 **여기서 그대로 재현**된다(부록 [2l]).

**(c) Kähler 구조.** $g=\mathrm{Re}\,Q$ (계량), $\omega=-\mathrm{Im}\,Q$ (닫힌 2-형식) — 실부·허부가 한 텐서 $Q$의 두 얼굴이다. 걸음 2–3에서 $\partial\bar\partial\log S$ 하나에서 계량과 Ricci가 다 나온 것과 같은 사정. **복소부는 오차가 아니라 CP¹이 Kähler라는 사실 자체다.** 그리고 이 구조는 Gr(2,4)에서도 그대로 산다(§4.5).

---

## 4. Gr(2,4)의 양자정보계량 — 정확한 기술

이 절은 기준집 5단계 **Part H (P083–P091)** 의 규약을 그대로 쓴다. CP¹에서 한 계산의 각 부품이 무엇으로 바뀌는지 대응표부터:

| CP¹ = Gr(1,2) | Gr(2,4) |
|---|---|
| $z\in\mathbb C$ | $Z\in M_2(\mathbb C)$ (복소 4, 실 8차원) |
| $\tilde v=\binom1z$ | $\widetilde V=\binom{I_2}{Z}$ (P089) |
| $S=1+\lvert z\rvert^2=\tilde v^\dagger\tilde v$ | $G=I_2+Z^\dagger Z=\widetilde V^\dagger\widetilde V$ (Gram 행렬) |
| $P=\tilde v\,S^{-1}\tilde v^\dagger$ | $P=\widetilde V\,G^{-1}\widetilde V^\dagger$, $\mathrm{Tr}P=2$ (P089) |
| 포텐셜 $\log S$ | $\log\det G$ |
| $\psi=\tilde v/\sqrt S$ (순수상태) | $\psi_\wedge=\dfrac{\tilde v_1\wedge\tilde v_2}{\sqrt{\det G}}\in\Lambda^2\mathbb C^4=\mathbb C^6$ (Plücker·Slater) |

### 4.1 접공간과 원점 QFIM (P085·P086·P088·P090)

$P^2=P,\ P^\dagger=P$를 미분하면 $T_P\mathrm{Gr}=\{A^\dagger=A,\ AP+PA=A\}$. 기준점 $P_0=\begin{pmatrix}I_2&0\\0&0\end{pmatrix}$에서 블록 계산으로

$$
A=\begin{pmatrix}0&B^\dagger\\ B&0\end{pmatrix},\quad B\in M_2(\mathbb C),
\qquad
g^{QFIM}_{P_0}(A,A)=2\,\mathrm{Tr}(A^2)=4\,\mathrm{Tr}(B^\dagger B).
$$

그리고 $Z(t)=tB$ 곡선에서 $\dot P(0)=A$ (P090; 수치 재확인 부록 [3e]).

### 4.2 일반점의 닫힌형

$$
\boxed{\ ds^2_{QFIM}=2\,\mathrm{Tr}(dP\,dP)=4\,\mathrm{Re}\,\mathrm{Tr}\Bigl[(I+Z^\dagger Z)^{-1}\,dZ^\dagger\,(I+ZZ^\dagger)^{-1}\,dZ\Bigr]\ }
$$

- 좌변 $2\mathrm{Tr}(dPdP)$가 QFIM인 것은 P036(CP¹)·P088(Gr) 규약.
- 우변 등식의 근거: 원점($Z=0$)에서는 §4.1로 즉시 $4\mathrm{Tr}(dZ^\dagger dZ)$가 되어 성립하고, 임의의 점은 $U(4)$ 작용으로 원점으로 옮겨진다(P076의 논리가 Gr(2,4)에서도 그대로: $P\mapsto UPU^\dagger$는 $\mathrm{Tr}(dPdP)$를 보존). 독립 검산으로 무작위 $Z_0$, 방향 $W$에서 좌우변을 수치 비교: 상대오차 $1.5\times10^{-11}$ (부록 [3a][3b]).
- CP¹ 환원(P091): $k=1,N=2$로 같은 코드를 돌리면 $4|dz|^2/S^2$ — §2.6(i)과 일치(부록 [3f]).

### 4.3 순수상태 실현 — Plücker = 2-fermion Slater 상태

$\widetilde V$의 두 열 $\tilde v_1,\tilde v_2$의 쐐기곱(= Slater determinant 상태)의 성분은 $2\times2$ 소행렬식이다. $Z=\begin{pmatrix}a&b\\c&d\end{pmatrix}$일 때 여섯 성분을 전부 쓰면

$$
p_{12}=1,\quad p_{13}=b,\quad p_{14}=d,\quad p_{23}=-a,\quad p_{24}=-c,\quad p_{34}=ad-bc=\det Z,
$$

Plücker 관계 $p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=(ad-bc)+bc-ad=0$ ✔ (Gr(2,4)가 $\mathbb{CP}^5$ 안의 4차원 quadric인 이유; 부록 [2m]).

**노름 항등식** ($2\times2$에서 $\det(I+M)=1+\mathrm{tr}M+\det M$ — 직접 전개로: $\det\begin{pmatrix}1+m_{11}&m_{12}\\m_{21}&1+m_{22}\end{pmatrix}=1+m_{11}+m_{22}+m_{11}m_{22}-m_{12}m_{21}$):

$$
\|p\|^2=1+|a|^2+|b|^2+|c|^2+|d|^2+|\det Z|^2
=1+\mathrm{tr}(Z^\dagger Z)+\det(Z^\dagger Z)=\det(I_2+Z^\dagger Z)=\det G .
$$

(부록 [2m][3d].) 그러므로 **CP¹의 $S=1+|z|^2$ 자리에 $\det G=1+\sum|z_{ij}|^2+|\det Z|^2$가 들어온다** — 포텐셜이 $\log S\to\log\det G$로 바뀌는 것이 유일한 변화이고, 마지막 항 $|\det Z|^2$ 하나가 Gr(2,4)를 $\mathbb{CP}^4$가 아닌 quadric으로 만든다.

**양자정보 해석.** 정규화된 순수상태 $\psi_\wedge=(\tilde v_1\wedge\tilde v_2)/\sqrt{\det G}\in\mathbb{CP}^5$ 는 4-모드 2-fermion Slater 상태다. 이 상태에 P074의 QFIM 공식(정규화 전 벡터용)을 적용한 값과 §4.2의 $2\mathrm{Tr}(dPdP)$가 **같다**: 무작위 곡선에서 상대오차 $3.4\times10^{-11}$ (부록 [3c]). 즉

$$
\boxed{\ \text{Gr(2,4) QFIM}\ =\ \text{Slater 상태의 QFIM}\ =\ 4\times\bigl(\text{Plücker로 당긴 }\mathbb{CP}^5\text{ FS}\bigr)\ =\ 2\,\mathrm{Tr}(dP\,dP).\ }
$$

CP¹에서 세 방식이 한 답이던 구조(주제 8)가 Gr(2,4)에서 문자 그대로 반복된다.

### 4.4 복소부도 그대로 산다

$Q_{ij}$의 정의는 $\psi_\wedge$에 대해 그대로 쓸 수 있고, $g=\mathrm{Re}\,Q$가 위의 계량, $\omega=-\mathrm{Im}\,Q$가 Kähler 형식(포텐셜 $\log\det G$의 $\partial\bar\partial$)이다. §3에서 본 "복소부 = 넓이형식/Berry curvature" 구조가 8차원에서도 성립한다 — CP¹은 그 최저차원 단면이다.

### 4.5 혼합상태 선택지 (각주)

"Gr(2,4) 위의 양자상태"를 순수 Slater가 아니라 **2차원 부분공간 위의 균등 혼합** $\rho=P/2$로 읽는 길도 있다. 이 경우 SLD 기반 QFIM을 수치로 재면(무작위 3점) 항상

$$
F_{\rho=P/2}=\tfrac12\cdot 2\,\mathrm{Tr}(dPdP)=\mathrm{Tr}(dPdP)
$$

— 순수 Slater QFIM의 정확히 절반이다(부록 [3g]; 3점 모두 비율 $0.5000000000$). 어느 쪽을 "Gr(2,4)의 양자정보계량"이라 부를지는 상태 해석의 선택이며, **기준집 P088의 규약($2\mathrm{Tr}(AC)$)은 순수 Slater 쪽과 일치**한다.

### 4.6 다음 손계산 순서 (기준집 문제 번호로)

이 문서의 §4를 손으로 재현하려면: **P083 → P085 → P086 → P088 → P089 → P090 → P091** (그다음 P074를 $\mathbb{CP}^5$에 적용해 [3c]를 손으로).

---

## 5. 참고문서

**폴더 안 (기준집 문제 번호 매핑):**

| 주제 | 기준집 |
|---|---|
| 상태 미분·내적 (이 손계산) | 3단계 Part B **P012–P015**, **P017** |
| QFIM 정의·게이지 불변 | 5단계 Part C **P021**, **P028**; **P082** ($H=4\mathrm{Var}\ge0$) |
| projector 방식 | 3단계 Part D **P031–P037**, 특히 **P036** |
| affine 공식 | **P008**, **P074**, **P076** |
| Grassmannian | 5단계 Part H **P083–P091** |
| classical Fisher 다리 | **P095**, **P097** |
| 정규화 규약 | 3단계 §0 Assertion 1–5, 43쪽 정규화 경고 |

그 외 폴더: `원본노트/Learning Riemannian Geometry.pdf`(LRG; 곡률 공식·주제 10), `원본노트/QFIM 계산.pdf`, 걸음 문서 `2_공하나…`(사영자·Bloch 전단사), `3_…곡률…`(제1·2기본형식).

**외부 (표준 문헌, 본문 계산은 전부 자체 검산):** Liu–Yuan–Lu–Wang, *Quantum Fisher information matrix and multiparameter estimation*, J. Phys. A **53** 023001 (2020) — QFIM 규약·순수/혼합 공식. Bengtsson–Życzkowski, *Geometry of Quantum States* — FS·Bures·Grassmann 장. Edelman–Arias–Smith, SIAM J. Matrix Anal. (1998) — Grassmann 계산 기하.

---

## 부록 A. 검산 (`verify5_qfim.py`, sympy 1.x + numpy, 2026-07-09 실행)

```
[1a] ||psi_노트||^2 = c^2/(1+c^2)  (≠1; θ2=π/2에서 1/2)
[1b] 손노트 d1psi 라인 == 직접미분?  True
[1c] 손노트 d2psi 최종라인 == 직접미분?  True
[1d-i] p4 중간줄 Re항: 노트 c^4/(1+c^2)^2, 실제 c^4/(1+c^2)^4  → 다름 (E3)
[1d-ii] 노트 H11(π/3) = -1.0651 (<0, P082 위반); 공식-on-노트ψ = 0.6706 ≠ sin²(π/3)=0.75
[1e] 노트 ψ로도 Re H12 = 0 재현
[1f] 남극 직선 교점 zeta = e^{iθ1} sinθ2/(1+cosθ2) = tan(θ2/2)e^{iθ1} (E1 확정)
[2a] 1+tan² = sec² : True          [2b] (1,z)/√S = (cos½θ2, e^{iθ1}sin½θ2): True
[2c] ||ψ||²=1                      [2e] <∂1|∂1>=sin²½θ2, <∂1|ψ>=-i sin²½θ2,
     <∂2|∂2>=1/4, <∂2|ψ>=0, <∂1|∂2>=-i sinθ2/4
[2f] H = diag(sin²θ2, 1)
[2g] Q12 = -i sinθ2/4; |ImQ12| = √det(H/4); ∫|ImQ12| = π
[2h] Bloch |dn|² 일치: True        [2i] 2tr(dPdP) 일치: True
[2j] P074 → 4/S² ('4/D²'): True   [2k] K(QFIM)=1, K(FS)=4
[2l] A1=-sin²½θ2, A2=0, F12=sinθ2/2=2ω12, ∫F=2π  (dα=2dA_FS 재현)
[2m] Plücker quadric = 0;  det(I+Z†Z) − (1+Σ|z|²+|detZ|²) = 0
[3a] 2tr(dPdP)            = 0.9020027306602072
[3b] 4Re tr[G⁻¹dZ†G'⁻¹dZ] = 0.9020027306737755   (상대오차 1.5e-11)
[3c] Plücker 순수상태 QFIM = 0.9020027306910894   (상대오차 3.4e-11)
[3d] ||v1∧v2||² vs det(I+Z†Z): 상대오차 1.7e-16
[3e] 원점 2tr(A²)=4tr(B†B)=49.6846…; ||dP/dt−A||=6.0e-11 (P090)
[3f] Gr(1,2) 환원: 23.60394080377 vs 23.60394080366
[3g] ρ=P/2 SLD-QFIM 비율 (무작위 3점): 0.5000000000000002, 0.5, 0.5000000000000002
```

수치 검산([3a]–[3g])은 무작위 한 점(+[3g]는 3점)에서의 확인이며, [1]–[2]의 기호 검산은 항등식 수준으로 확정이다.
