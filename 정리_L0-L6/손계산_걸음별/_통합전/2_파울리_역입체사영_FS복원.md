# 2 — 공 $S^2$ 하나: 여러 계산이 $1/S^2$ 로 수렴한다

> **이 노트는 전부 공 $S^2$ 이야기다.** $S^2$ $=$ Bloch 공 $=\mathbb{CP}^1$ $=$ 순수상태. 그 위에서 하는 서로 다른 *기초 계산* — 입체사영, 복소화 $\partial_z$, 파울리·밀도행렬, 사영자 $\operatorname{tr}(dP\,dP)$ — 이 **$1\!\to\!2\!\to\!3$ 직선이 아니라 한 점으로 수렴**한다: 계량이 전부 $S=1+|z|^2$ 의 $1/S^2$ 꼴이다. 아래는 그 수렴을 *공 위에서* 손으로 짓는 것.
>
> **퀄리티(Part1·Part2 계승).** 관찰 먼저, 추상 서술 대신 **실제 손계산 예시**, 모든 줄 검산.

**수렴하는 곳 (전부 공 위의 계산, $S=1+|z|^2$):**

| 공 위의 계산 | 어디서 | 결과 |
|---|---|---|
| 입체사영 제1기본형식 | Part1 (손노트) | $\lvert d\vec n\rvert^2=4/S^2$ |
| 복소화 $\partial_z\vec n$ | Notes (손노트) | $\langle\partial_z\vec n,\partial_{\bar z}\vec n\rangle=2/S^2$ |
| 밀도행렬·사영자 $\operatorname{tr}(dP\,dP)$ | §2·§4·§5 | $2/S^2$ |
| 사영자에 $\partial_z$ ($g_{z\bar z}$) | §5 | $1/S^2$ |

전부 $\propto 1/S^2$ — **같은 공**, 규약($2$ vs $4$)만 다르다(등거리 $\tfrac12$). CPⁿ은 $S\mapsto1+\sum|z_i|^2$ 로 같은 꼴이 그대로 확장.

---

## 0. 세팅 — 파울리 행렬과 그 곱 (다 직접)

$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
직접 곱하면(부록 A0) **$\sigma_a^2=I$, $\sigma_1\sigma_2=i\sigma_3$(순환), $\operatorname{tr}\sigma_a=0$, $\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}$.** 그리고 임의의 무대각합 $2\times2$ 에르미트는 실 3-벡터 $\vec x$ 로 $\vec x\cdot\vec\sigma$ 로 적힌다. 표기: $z=x+iy$, $s=x^2+y^2=|z|^2$, $S=1+s$, $N=\|v\|^2$, $\langle a,b\rangle=a^*b$.

---

## 1. Block 1 — 손노트의 구면 점을 행렬로 (계량까지 보존되는가)

손노트는 구면 점을 $\mathbb R^3$ 의 단위법선 $\vec P(x,y)$ 로 두고 다뤘다 (Part1: 그 점으로 곡률; Notes: 그 계량을 복소로 — 각각 "다른 해는 없나?"·"복소 성분 둘을 어떻게 잇나?"에서 멈춤). 이제 **같은 점을 행렬로** 적는다. 실 3-벡터 $\vec n$ 을 파울리로 얹으면
$$
\vec n\cdot\vec\sigma=\begin{pmatrix}n_3&n_1-in_2\\ n_1+in_2&-n_3\end{pmatrix},\qquad P:=\tfrac12(I+\vec n\cdot\vec\sigma)\ (\operatorname{tr}=1).
$$
점을 행렬로 옮겨도 되려면 **계량까지 살아남아야** 한다. 행렬 곱을 직접 본다: $\sigma_a^2=I$, 그리고
$$
\sigma_1\sigma_2=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\!\left(\begin{smallmatrix}0&-i\\ i&0\end{smallmatrix}\right)=\left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right)=i\sigma_3\ (\text{순환; 순서 바꾸면 부호 반대})\ \Rightarrow\ \sigma_a\sigma_b=\delta_{ab}I+i\varepsilon_{abc}\sigma_c,
$$
대각합을 취하면 $\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}$. 그러므로 행렬화 $\iota:\vec x\mapsto\vec x\cdot\vec\sigma$ 의 행렬 내적 $\langle A,B\rangle=\operatorname{tr}(AB)$ 은
$$
\operatorname{tr}\big((\vec x\cdot\vec\sigma)(\vec y\cdot\vec\sigma)\big)=\sum_{a,b}x_a y_b\operatorname{tr}(\sigma_a\sigma_b)=2\,\vec x\cdot\vec y
\ \Longrightarrow\
\boxed{\ \vec x\cdot\vec y=\tfrac12\operatorname{tr}(\iota\vec x\,\iota\vec y)\ }.
$$
$\iota$ 는 등거리 — **손노트가 $\mathbb R^3$ 에서 잰 구면 계량이 행렬 쪽 $\tfrac12\operatorname{tr}$ 로 그대로 넘어온다.** 이것이 점을 행렬로 적어도 되는 이유이고, 아래 전개가 전부 여기서 흐른다.

**손계산 예시 1 — 실제 분해.** $H=\left(\begin{smallmatrix}3&\ 1-2i\\ 1+2i&\ -1\end{smallmatrix}\right)$ (에르미트). 대각합의 절반 $c_0=\tfrac12(3+(-1))=1$ 을 떼면
$$
H-c_0 I=\left(\begin{smallmatrix}2&\ 1-2i\\ 1+2i&\ -2\end{smallmatrix}\right)=\left(\begin{smallmatrix}x_3&\ x_1-ix_2\\ x_1+ix_2&\ -x_3\end{smallmatrix}\right)
\ \Rightarrow\ x_3=2,\ \ x_1-ix_2=1-2i\Rightarrow(x_1,x_2)=(1,2).
$$
$$
\therefore\quad H=1\cdot I+(1,2,2)\cdot\vec\sigma .
$$

**손계산 예시 2 — 등거리·인자 2 (다른 성격).** 위 $\vec x=(1,2,2)$, $|\vec x|^2=1+4+4=9$. $\vec x\cdot\vec\sigma=\left(\begin{smallmatrix}2&\ 1-2i\\ 1+2i&\ -2\end{smallmatrix}\right)$ 를 제곱한다:
$$
(1,1):\ 2^2+(1-2i)(1+2i)=4+5=9,\qquad (2,2):\ (1+2i)(1-2i)+(-2)^2=5+4=9,
$$
$$
(1,2):\ 2(1-2i)+(1-2i)(-2)=0\ (\text{대칭}),\qquad\text{곧}\quad (\vec x\cdot\vec\sigma)^2=9I.
$$
따라서 $\tfrac12\operatorname{tr}\big((\vec x\cdot\vec\sigma)^2\big)=\tfrac12\cdot18=9=|\vec x|^2$ — 등거리를 $\vec x=\vec y$ 에서 손으로 확인(인자 2가 실제로 상쇄).

---

## 2. Block 2 — 구면 점 $=$ 랭크1 사영자, 그 계량 $=\operatorname{tr}(dP\,dP)$

구면 점 $\vec n$ ($|\vec n|=1$) 을 $\operatorname{tr}=1$ 로 얹어 $P:=\tfrac12(I+\vec n\cdot\vec\sigma)$. 판별식:
$$
\det(I+\vec n\cdot\vec\sigma)=\det\left(\begin{smallmatrix}1+n_3&n_1-in_2\\ n_1+in_2&1-n_3\end{smallmatrix}\right)=(1+n_3)(1-n_3)-(n_1-in_2)(n_1+in_2)=1-n_3^2-(n_1^2+n_2^2)=1-|\vec n|^2.
$$
$|\vec n|=1$ 이니 $\det P=\tfrac14(1-|\vec n|^2)=0$, $\operatorname{tr}P=\tfrac12\cdot2=1$. 고윳값 합 $1$·곱 $0$ → $\{1,0\}$ → $P^2=P$ 인 **랭크1 사영자**.

계량은 Block 1의 등거리로 그대로 옮겨진다. $\vec n\cdot\vec\sigma=2P-I$ 이므로 $d(\vec n\cdot\vec\sigma)=2\,dP$, 이를 $|d\vec n|^2=\tfrac12\operatorname{tr}\big((d\vec n\cdot\vec\sigma)^2\big)$ 에 넣으면
$$
|d\vec n|^2=\tfrac12\operatorname{tr}\big((2\,dP)^2\big)=2\operatorname{tr}(dP\,dP)
\ \Longrightarrow\
\boxed{\ \operatorname{tr}(dP\,dP)=\tfrac12|d\vec n|^2\ }.
$$
인자 $\tfrac12$ 은 "$\tfrac12(I+\cdot)$ 얹기"에서 온 값(구면 $K=1$ vs 사영자 $K=2$ 의 뿌리).

### 드릴 — 밀도행렬로 (순수/혼합)

$P=\tfrac12(I+\vec n\cdot\vec\sigma)$ 는 큐빗 밀도행렬의 꼴이다. Bloch 벡터는 기댓값으로 되찾는다:
$$
\operatorname{tr}(P\sigma_a)=\tfrac12\operatorname{tr}\sigma_a+\tfrac12\sum_b n_b\operatorname{tr}(\sigma_b\sigma_a)=0+\tfrac12\,n_a\cdot2=n_a.
$$
순도(purity)와 고윳값도 손으로:
$$
\operatorname{tr}(P^2)=\tfrac14\operatorname{tr}\big((I+\vec n\cdot\vec\sigma)^2\big)=\tfrac14\big(2+0+2|\vec n|^2\big)=\tfrac12(1+|\vec n|^2),
$$
$$
\lambda^2-(\operatorname{tr}P)\lambda+\det P=\lambda^2-\lambda+\tfrac14(1-|\vec n|^2)=0\ \Rightarrow\ \lambda=\tfrac12(1\pm|\vec n|).
$$
그러니 Block 2의 조건 $\det P=1-|\vec n|^2=0$ 은 정확히 **$|\vec n|=1$ (구면) $\Leftrightarrow$ $\operatorname{tr}(P^2)=1$, 고윳값 $\{1,0\}$ $\Leftrightarrow$ 순수상태 $=$ 사영자**. $|\vec n|<1$ 은 Bloch 공 내부의 혼합상태($P^2\ne P$).

- **예시(순수)** $\vec n=(0,0,1)$: $P=\tfrac12(I+\sigma_3)=\operatorname{diag}(1,0)$, $\operatorname{tr}P^2=1$, 고윳값 $\{1,0\}$, $P^2=P$.
- **예시(혼합, 다른 성격)** $\vec n=(0,0,\tfrac12)$: $\rho=\tfrac12(I+\tfrac12\sigma_3)=\operatorname{diag}(\tfrac34,\tfrac14)$, $\operatorname{tr}\rho^2=\tfrac9{16}+\tfrac1{16}=\tfrac58=\tfrac12(1+\tfrac14)$, 고윳값 $\tfrac34,\tfrac14=\tfrac12(1\pm\tfrac12)$, $\rho^2\ne\rho$.

곧 $\mathbb{CP}^1$ = 순수상태 전체 = Bloch 공의 경계(구면). §3은 그 순수상태를 좌표 $z$ 로 적는다. *(sympy: $\operatorname{tr}(P\sigma_a)=n_a$, $\operatorname{tr}P^2=\tfrac12(1+|\vec n|^2)$, 고윳값 $\tfrac12(1\pm|\vec n|)$.)*

---

## 3. Block 3 — 역입체사영: 좌표와 복소구조

**남극 역입체사영.** 좌표 원점을 북극에 두려고 남극 $(0,0,-1)$ 에서 평면점 $(x,y,0)$ 로 쏜다. 직선 $(0,0,-1)+t(x,y,1)=(tx,\,ty,\,t-1)$ 이 구면 위에 있을 조건:
$$
t^2(x^2+y^2)+(t-1)^2=1\ \Rightarrow\ t^2 s+t^2-2t+1=1\ \Rightarrow\ t^2(s+1)=2t\ \Rightarrow\ t=\frac2S,
$$
$$
\vec n(z)=(tx,\,ty,\,t-1)=\Big(\tfrac{2x}S,\ \tfrac{2y}S,\ \tfrac{1-s}S\Big),\qquad z=x+iy\ \ (z=0\mapsto\text{북극}\,(0,0,1)).
$$
**사영자를 적으면 $vv^*/N$ 이 나온다.** $\vec n\cdot\vec\sigma=\dfrac1S\left(\begin{smallmatrix}1-s&2\bar z\\ 2z&-(1-s)\end{smallmatrix}\right)$ 이므로 $P=\tfrac12(I+\vec n\cdot\vec\sigma)$ 의 성분은
$$
P_{11}=\tfrac12\Big(1+\tfrac{1-s}S\Big)=\tfrac1S,\quad P_{22}=\tfrac12\Big(1-\tfrac{1-s}S\Big)=\tfrac sS=\tfrac{|z|^2}S,\quad P_{21}=\tfrac zS,\quad P_{12}=\tfrac{\bar z}S,
$$
$$
P=\frac1S\begin{pmatrix}1&\bar z\\ z&|z|^2\end{pmatrix}=\frac1S\binom1z\begin{pmatrix}1&\bar z\end{pmatrix}=\frac{vv^*}{\|v\|^2},\qquad v=\binom1z,\ N=S.
$$
**복소직선.** $Pv=\tfrac1S v(v^*v)=v$ ($v^*v=S$), 그리고 $v^\perp$ 는 $Pw=0$ — $P$ 의 $+1$ 고유선은 $\mathbb Cv\subset\mathbb C^2$. 실점 $\vec n\in S^2$ 이 사영자의 $+1$ 고유선(복소직선)으로 바뀐다: $S^2=\mathbb{CP}^1$, 좌표 $z=v_2/v_1$.
**컨벤션.** $z=0$ 에서 $P=\tfrac12(I+\sigma_3)=\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)=|0\rangle\langle0|$, 곧 북극 $=|0\rangle$. (북극에서 쐈으면 $n_3=\tfrac{s-1}S$ 라 $Pv\ne v$, 좌표가 $1/\bar z$ 로 뒤집힌다 — 남극이라야 맞음.)

---

## 4. Block 4 — 계량을 좌표 없이 당긴다: $\operatorname{tr}(dP\,dP)$ 닫힌형 (차원 무관)

$P=vv^*/N$ ($N=\|v\|^2$), $A:=dv\,v^*+v\,dv^*$, $dN=dv^*v+v^*dv$, $dP=\dfrac AN-\dfrac{vv^*}{N^2}dN$. 스칼라 $v^*v=N,\ v^*dv,\ dv^*v$ 는 trace 밖으로, $\operatorname{tr}(XY)=\operatorname{tr}(YX)$:
$$
\operatorname{tr}((vv^*)^2)=\operatorname{tr}(v(v^*v)v^*)=N\operatorname{tr}(vv^*)=N^2,
$$
$$
\operatorname{tr}(A\,vv^*)=\operatorname{tr}(dv\,v^*vv^*)+\operatorname{tr}(v\,dv^*vv^*)=N(v^*dv)+N(dv^*v)=N\,dN,
$$
$$
\operatorname{tr}(A^2)=\underbrace{(v^*dv)^2}_{dv\,v^*dv\,v^*}+\underbrace{N(dv^*dv)}_{dv\,v^*v\,dv^*}+\underbrace{N(dv^*dv)}_{v\,dv^*dv\,v^*}+\underbrace{(dv^*v)^2}_{v\,dv^*v\,dv^*}=(v^*dv)^2+2N(dv^*dv)+(dv^*v)^2.
$$
조립하면 $dN^2$ 항이 $-2+1$ 로 반만 남는다:
$$
\operatorname{tr}(dP\,dP)=\frac{\operatorname{tr}(A^2)}{N^2}-\frac{2\operatorname{tr}(A\,vv^*)}{N^3}dN+\frac{\operatorname{tr}((vv^*)^2)}{N^4}dN^2=\frac{\operatorname{tr}(A^2)-dN^2}{N^2}.
$$
$dN^2=(dv^*v)^2+2|v^*dv|^2+(v^*dv)^2$ 를 빼면 제곱항이 소거되어 $\operatorname{tr}(A^2)-dN^2=2N(dv^*dv)-2|v^*dv|^2$, 곧
$$
\boxed{\ \operatorname{tr}(dP\,dP)=\frac{2\big[\,\|v\|^2\langle dv,dv\rangle-|\langle v,dv\rangle|^2\,\big]}{\|v\|^4}\ }.
$$
차원 $n$ 을 한 번도 안 썼다 — CP¹·CPⁿ 공통 식.

---

## 5. Block 5 — CP¹ → FS·포텐셜, 그리고 CPⁿ

**CP¹.** $v=(1,z)$, $dv=(0,dz)$: $\|v\|^2=S$, $\langle dv,dv\rangle=|dz|^2$, $\langle v,dv\rangle=\bar z\,dz$, $|\langle v,dv\rangle|^2=|z|^2|dz|^2$. Block 4 식에:
$$
\operatorname{tr}(dP\,dP)=\frac{2(S-|z|^2)}{S^2}|dz|^2=\frac2{S^2}|dz|^2\qquad(S-|z|^2=1).
$$
Block 2와 대조: $\tfrac12|d\vec n|^2=\tfrac12\cdot\tfrac4{S^2}=\tfrac2{S^2}$ — 일치(둥근 계량의 절반).

### 드릴 — $|dz|^2$ 를 행렬로 보기 (원리)

위 닫힌형은 스칼라로 뛰어 행렬이 안 보인다. $P=\tfrac1S\left(\begin{smallmatrix}1&\bar z\\ z&|z|^2\end{smallmatrix}\right)$ 를 직접 미분해 $dP$ 를 **행렬로** 적는다 ($dS=\bar z\,dz+z\,d\bar z$, 각 성분에 몫미분):
$$
dP=\frac1{S^2}\begin{pmatrix}-(\bar z\,dz+z\,d\bar z) & d\bar z-\bar z^2\,dz\\[2pt] dz-z^2\,d\bar z & \bar z\,dz+z\,d\bar z\end{pmatrix}
$$
(대각 두 성분이 부호 반대 → $\operatorname{tr}dP=0$, 곧 $\operatorname{tr}P=1$ 을 반영). 원점 $z=0$ ($S=1$) 에서 보면 선명하다:
$$
dP\big|_0=\begin{pmatrix}0 & d\bar z\\ dz & 0\end{pmatrix},\qquad
(dP)^2\big|_0=\begin{pmatrix}d\bar z\,dz & 0\\ 0 & dz\,d\bar z\end{pmatrix}=|dz|^2\,I,\qquad
\operatorname{tr}(dP\,dP)\big|_0=2|dz|^2.
$$
**원리.** $dP$ 는 순수 off-diagonal 이다(Block 6의 $B+B^\dagger$): 오른쪽 위가 반정칙 $d\bar z$, 왼쪽 아래가 정칙 $dz$. 행렬 곱 $(dP)^2$ 에서 이 둘이 짝지어 $dz\cdot d\bar z=|dz|^2$ 로 대각에 올라온다. 곧 **$|dz|^2$ 는 "정칙 성분 $\times$ 반정칙 성분"이라는 행렬 곱**이다. 일반 $z$ 에서도 같은 짝지음으로
$$
\operatorname{tr}(dP\,dP)=\frac{2\,dz\,d\bar z}{S^2}=\frac2{S^2}|dz|^2.
$$
*(sympy: $dP$ 행렬 및 $\operatorname{tr}(dP\,dP)=2\,dz\,d\bar z/S^2$ 확인.)*

### 드릴 — 손노트의 복소화와 만나는 곳 ($\partial_z P$)

손노트(Notes)는 구면 점을 $z=x+iy$ 로 복소화해 $\partial_z=\tfrac12(\partial_x-i\partial_y)$ 로 미분하고, **정칙²은 null·혼합만 산다** — $\langle\partial_z\vec n,\partial_z\vec n\rangle=0$, $\langle\partial_z\vec n,\partial_{\bar z}\vec n\rangle=g_{z\bar z}$ — 를 얻었다. 그 *똑같은 $\partial_z$* 를 사영자 $P=\tfrac1S\left(\begin{smallmatrix}1&\bar z\\ z&|z|^2\end{smallmatrix}\right)$ 에 그대로 쓴다. $dP=\partial_z P\,dz+\partial_{\bar z}P\,d\bar z$, 성분미분($\partial_z S=\bar z$; $S-z\bar z=1$)으로
$$
\partial_z P=\frac1{S^2}\begin{pmatrix}-\bar z&-\bar z^2\\ 1&\bar z\end{pmatrix},\qquad
\partial_{\bar z}P=(\partial_z P)^\dagger=\frac1{S^2}\begin{pmatrix}-z&1\\ -z^2&z\end{pmatrix}.
$$
행렬 곱으로 손노트의 두 관찰이 그대로 재현된다:
$$
\operatorname{tr}\big((\partial_z P)^2\big)=0\ (\text{정칙 null}),\qquad
\operatorname{tr}(\partial_z P\,\partial_{\bar z}P)=\frac{S^2}{S^4}=\frac1{S^2}=g_{z\bar z},
$$
따라서 $\operatorname{tr}(dP\,dP)=2\,g_{z\bar z}\,|dz|^2=\dfrac2{S^2}|dz|^2$ (위 두 드릴과 같은 값).

**이곳이 두 손노트가 만나는 곳이다.** 손노트는 구면 점 $\vec n$ 에 $\partial_z$ 를 써 $\langle\partial_z\vec n,\partial_{\bar z}\vec n\rangle=\tfrac2{S^2}$ 를 얻었고, 여기서는 *그 점의 사영자* $P$ 에 **같은** $\partial_z$ 를 써 $\operatorname{tr}(\partial_z P,\partial_{\bar z}P)=\tfrac1{S^2}$ 를 얻는다 — 정확히 절반(Block 1·2의 등거리 $\tfrac12$). 복소화(손노트)와 사영자(이 문서)는 따로가 아니라 **하나의 $\partial_z$ 계산**, 대상만 $\vec n\leftrightarrow P$. *(sympy: $\partial_z P$ 행렬, $\operatorname{tr}((\partial_z P)^2)=0$, $\operatorname{tr}(\partial_z P\,\partial_{\bar z}P)=1/S^2$.)*

**포텐셜.** $\partial_{\bar z}\log(1+z\bar z)=\dfrac{z}{S}$, 다시 $\partial_z\dfrac zS=\dfrac{S-z\bar z}{S^2}=\dfrac1{S^2}$ 이므로
$$
g_{z\bar z}=\frac1{S^2}=\partial_z\partial_{\bar z}\log\|v\|^2,
$$
계량이 한 스칼라 $\Phi=\log\|v\|^2$(켈러 포텐셜)의 $\partial\bar\partial$. ($v\mapsto\mu v$ 에 $\Phi\mapsto\Phi+\log|\mu|^2$, $\partial\bar\partial\log|\mu|^2=0$ 이라 계량 불변.)

**CPⁿ.** $v=(1,z_1,\dots,z_n)$: $\langle dv,dv\rangle=\sum_i|dz_i|^2$, $\langle v,dv\rangle=\sum_i\bar z_i dz_i$. Block 4 식에 넣고 $ds^2=2g_{i\bar j}dz_i d\bar z_j$ 로 읽으면
$$
\operatorname{tr}(dP\,dP)=\frac{2}{S^2}\Big[S\sum_i|dz_i|^2-\sum_{i,j}\bar z_i z_j\,dz_i d\bar z_j\Big]
\ \Rightarrow\
\boxed{\ g_{i\bar j}=\frac{S\delta_{ij}-\bar z_i z_j}{S^2}=\partial_{z_i}\partial_{\bar z_j}\log\|v\|^2\ }.
$$
Block 4 닫힌형이 차원 무관이라 $\mathbb C^2\to\mathbb C^{n+1}$ 만으로 CPⁿ의 FS가 떨어진다.

---

## 6. Block 6 — 비퇴화

$P^2=P$ 를 미분하면 $dP\,P+P\,dP=dP$. 좌우에 $P$ 를 곱하고 $P^2=P$ 를 쓰면 $2P\,dP\,P=P\,dP\,P$, 곧 $P\,dP\,P=0$; $Q:=1-P$ ($Q^2=Q$, $PQ=QP=0$) 로 같은 계산이 $Q\,dP\,Q=0$. 그래서 $dP=(P{+}Q)dP(P{+}Q)=P\,dP\,Q+Q\,dP\,P=B+B^\dagger$ ($B:=P\,dP(1-P)$, $dP$ 에르미트라 둘째가 $B^\dagger$), 또 $B^2=P\,dP\,(QP)\,dP\,Q=0$. 따라서
$$
\operatorname{tr}(dP\,dP)=\operatorname{tr}\big((B+B^\dagger)^2\big)=2\operatorname{tr}(B^\dagger B)=2\|B\|^2\ge0\qquad(=0\iff dP=0),
$$
비퇴화·양정치. $B=P\,dP(1-P)$ 는 직선 $\mathbb Cv$ 에서 여공간 $v^\perp$ 로 가는 사상이라 $T_{[v]}\mathbb{CP}^n\cong\operatorname{Hom}(\mathbb Cv,v^\perp)$; 이 $B$ 가 문서 `3`이 두 번 미분할 제2기본형식이다.

---

## 부록 A — 줄별 손계산 (전부 직접 따라 적어 검산할 것)

**A0 (파울리 곱).** $\sigma_1\sigma_2=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right)=\left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right)=i\sigma_3$. 순환 동일. $\sigma_a^2=I$. $\operatorname{tr}(\sigma_a\sigma_b)$: $a=b$ 면 $\operatorname{tr}I=2$; $a\ne b$ 면 $\pm i\sigma_c$ 라 $\operatorname{tr}=0$. ✔(sympy: 표 $[[2,0,0],[0,2,0],[0,0,2]]$.)

**A1 (등거리).** $\operatorname{tr}((\vec x\cdot\vec\sigma)(\vec y\cdot\vec\sigma))=\sum_{a,b}x_ay_b\operatorname{tr}(\sigma_a\sigma_b)=\sum_a 2x_ay_a=2\vec x\cdot\vec y$. ✔

**A2 (사영자).** $\det(I+\vec n\cdot\vec\sigma)=(1+n_3)(1-n_3)-(n_1-in_2)(n_1+in_2)=1-n_3^2-(n_1^2+n_2^2)=1-|\vec n|^2$. $|\vec n|=1\Rightarrow\det P=\tfrac14\cdot0=0$, $\operatorname{tr}P=\tfrac12\cdot2=1$; 고윳값 합 1·곱 0 → $\{1,0\}$ → $P^2=P$. ✔

**A3 (역입체사영 $t$).** $t^2 s+(t-1)^2=1\Rightarrow t^2 s+t^2-2t+1=1\Rightarrow t^2(s+1)=2t\Rightarrow t=\tfrac2{s+1}=\tfrac2S$. $\vec n=(tx,ty,t-1)=(\tfrac{2x}S,\tfrac{2y}S,\tfrac{2-S}S)$, $2-S=1-s$. ✔

**A4 ($P$ 인수분해·고유벡터).** $\tfrac12(I+\vec n\cdot\vec\sigma)$ 의 $(1,1)=\tfrac12(1+\tfrac{1-s}S)=\tfrac12\cdot\tfrac{2}{S}=\tfrac1S$; $(2,1)=\tfrac12\cdot\tfrac{2z}S=\tfrac zS$; $(1,2)=\tfrac{\bar z}S$; $(2,2)=\tfrac12(1-\tfrac{1-s}S)=\tfrac sS=\tfrac{|z|^2}S$. 곧 $P=\tfrac1S\binom1z(1\ \bar z)$. $Pv=\tfrac1S v(v^*v)=v$ ($v^*v=S$). ✔(sympy: 남극 $Pv=v$; 북극 $n_3=\tfrac{s-1}S$ 면 $Pv\ne v$.)

**A5 (세 trace).** $(vv^*)^2=v(v^*v)v^*=Nvv^*\Rightarrow\operatorname{tr}=N^2$. $\operatorname{tr}(A\,vv^*)=\operatorname{tr}(dv\,v^*vv^*)+\operatorname{tr}(v\,dv^*vv^*)=N(v^*dv)+N(dv^*v)=N\,dN$. $\operatorname{tr}(A^2)$ 네 항 $=(v^*dv)^2+2N(dv^*dv)+(dv^*v)^2$. 조립: $\dfrac{\operatorname{tr}A^2-2dN^2+dN^2}{N^2}$, $dN^2$ 빼면 $\dfrac{2[N dv^*dv-|v^*dv|^2]}{N^2}$. ✔(sympy·수치: 임의 차원 일치.)

**A6 (CP¹ 대입).** $S-|z|^2=1\Rightarrow \operatorname{tr}(dP\,dP)=\tfrac{2\cdot1}{S^2}|dz|^2=\tfrac2{S^2}|dz|^2$. Bloch: $\tfrac12|d\vec n|^2=\tfrac2{S^2}|dz|^2$. ✔

**A7 (포텐셜).** $\partial_{\bar z}\log(1+z\bar z)=\tfrac{z}{1+z\bar z}$; $\partial_z\tfrac{z}{1+z\bar z}=\tfrac{(1+z\bar z)-z\bar z}{(1+z\bar z)^2}=\tfrac1{S^2}$. ✔(sympy.)

**A8 (CPⁿ).** $S\sum_i|dz_i|^2-(\sum_i\bar z_i dz_i)(\sum_j z_j d\bar z_j)=\sum_{i,j}(S\delta_{ij}-\bar z_i z_j)dz_i d\bar z_j\Rightarrow g_{i\bar j}=\tfrac{S\delta_{ij}-\bar z_iz_j}{S^2}$. ✔(sympy·수치.)

---

## 결과 요약

| Block | 한 일 (손으로) | 결과 |
|---|---|---|
| 1 | $\mathbb R^3\cong\mathrm{Herm}_0$ 등거리 | $\vec x\cdot\vec y=\tfrac12\operatorname{tr}$ |
| 2 | 구면 점 $\to$ 사영자, 계량 옮김 | $P=\tfrac12(I+\vec n\cdot\vec\sigma)$, $\operatorname{tr}(dP\,dP)=\tfrac12|d\vec n|^2$ |
| 3 | **남극 역입체사영** | $\vec n(z)$, $P=vv^*/S$, $v=(1,z)$, 복소직선=CP¹, 북극$=|0\rangle$ |
| 4 | 좌표 없이 당김 | $\operatorname{tr}(dP\,dP)=\tfrac{2[N dv^*dv-|v^*dv|^2]}{N^2}$ (차원 무관) |
| 5 | CP¹→FS·포텐셜, CPⁿ | $\tfrac2{S^2}|dz|^2=2\partial\bar\partial\log\|v\|^2$; $g_{i\bar j}=\tfrac{S\delta_{ij}-\bar z_iz_j}{S^2}$ |
| 6 | 비퇴화 | $\operatorname{tr}(dP\,dP)=2\|B\|^2\ge0$, $B=P\,dP(1-P)$ |

**한 문장.** 파울리로 $\mathbb R^3$ 이 곧 행렬공간임을 보고(§1), 구면 점을 사영자로 옮기고(§2), **남극 역입체사영**으로 좌표 $v=(1,z)$ 와 복소직선을 끄집어내고(§3), 평평한 $\operatorname{tr}$ 계량을 좌표 없이 당겨(§4) CP¹의 FS와 포텐셜, 나아가 $\mathbb C^2\to\mathbb C^{n+1}$ 만으로 CPⁿ의 FS를 복원한다(§5). 라플라시안·곡률은 이 길 어디에도 없다 — 그건 다 짓고 난 뒤(문서 `3`)의 일.

## 다음 후보
- 문서 `3`: 이 사영자 $P$ 를 두 번 미분(§6의 $B$ = 제2기본형식)해 곡률 $K$ — 모든 정칙방향 상수.
- 포텐셜 $\Phi=\log\|v\|^2$ 의 동차좌표 의미(왜 $\|v\|^2$)와 conic/Veronese pullback으로의 연결.
