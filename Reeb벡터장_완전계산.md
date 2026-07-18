# 파트 IV 완전 상세 — 접속형식 $\alpha$와 Reeb 벡터장, 정의부터 모든 줄

> **목적.** [발표계산_완전판](발표계산_완전판.html)의 Part IV(슬라이드 7–9: $\alpha$ 실좌표 → Reeb → $d\alpha$ → $\iota_R d\alpha=0$ → fiber)를 **약점 보강용으로 최대 해상도**로 다시 쓴 문서. 벡터장·1-형식·쌍대짝·외미분·내부곱·pullback — 등장하는 모든 연산을 정의부터 세우고, 모든 계산을 규칙 적용 한 줄 단위로 적는다. 앞단(구면·Hopf·FS)은 완전판의 Part I–III.
> **최종 목표.** $R_\alpha=\sum_r(-y_r\partial_{x_r}+x_r\partial_{y_r})$에 대해
> $$\alpha(R_\alpha)=1,\qquad \iota_{R_\alpha}d\alpha=0\qquad(\text{on }S^3)$$
> — Reeb 벡터장의 정의 두 조건 — 그리고 이 $R_\alpha$가 **FS가 사영으로 제거하는 바로 그 방향**($i\psi$)이라는 것까지.

표기: $\mathbb{C}^2=\mathbb{R}^4$, $z_r=x_r+iy_r$ ($r=1,2$), $S^3=\{N=1\}$, $N=x_1^2+y_1^2+x_2^2+y_2^2=\|v\|^2$.

---

## §1. 기초 — 벡터장과 1-형식이 실제로 하는 일

### 1a. $\partial_{x_r}$의 뜻: 방향미분 기계

$\partial_{x_r}$는 "함수를 받아 $x_r$ 방향 변화율을 내놓는 기계"다: $\partial_{x_r}(f)=\frac{\partial f}{\partial x_r}$. 일반 벡터장은 좌표벡터장의 (점마다 달라도 되는) 결합:
$$V=\sum_{s=1}^{2}\bigl(a_s\,\partial_{x_s}+b_s\,\partial_{y_s}\bigr),\qquad
V(f)=\sum_s\Bigl(a_s\frac{\partial f}{\partial x_s}+b_s\frac{\partial f}{\partial y_s}\Bigr).$$

### 1b. $dx_r$의 뜻과 쌍대 규칙 — 편미분 네 개를 전부 쓴다

1-형식 $dx_r$의 **정의**: 좌표함수 $x_r$을 벡터장 방향으로 미분한 값, $dx_r(V):=V(x_r)$. 위 식에 $f=x_1$을 넣고 네 편미분을 하나씩:
$$V(x_1)=a_1\underbrace{\frac{\partial x_1}{\partial x_1}}_{=1}
+b_1\underbrace{\frac{\partial x_1}{\partial y_1}}_{=0}
+a_2\underbrace{\frac{\partial x_1}{\partial x_2}}_{=0}
+b_2\underbrace{\frac{\partial x_1}{\partial y_2}}_{=0}=a_1.$$
($x_1,y_1,x_2,y_2$는 서로 독립 좌표라 "자기 자신으로 미분한 것"만 1.) 일반적으로
$$\boxed{\ dx_r(V)=a_r,\qquad dy_r(V)=b_r\ }$$
— **$dx_r$는 "$\partial_{x_r}$ 앞의 계수"를 읽어내는 기계.** 일반 1-형식 $\beta=\sum_r(p_r\,dx_r+q_r\,dy_r)$은 선형으로 작동한다: $\beta(V)=\sum_r(p_ra_r+q_rb_r)$.

### 1c. $df$와 곡선 — 이 문서에서 쓸 유일한 "미분기하" 사실

함수 $f$의 전미분 $df$가 속도벡터에게 하는 일은 **합성함수 미분** 그 자체다: 곡선 $c(t)$에 대해
$$df\bigl(c'(t)\bigr)=\frac{d}{dt}\,f\bigl(c(t)\bigr).$$
(§7에서 이 한 줄이 $\iota_Rd\alpha=0$을 끝낸다.)

---

## §2. $\alpha$를 실좌표로 (슬라이드 7, G1) — 그리고 $\alpha$가 실(real)인 이유

$$\alpha=\frac{i}{2}\sum_{r=1}^{2}\bigl(z_r\,d\bar z_r-\bar z_r\,dz_r\bigr),\qquad
dz_r=dx_r+i\,dy_r,\quad d\bar z_r=dx_r-i\,dy_r.$$

### 2a. 전개 — 분배법칙 여덟 항

성분 하나($z=x+iy$)에서 곱 두 개를 각각 네 항으로:
$$z\,d\bar z=(x+iy)(dx-i\,dy)
=x\,dx\ \underbrace{-\,ix\,dy}_{}\ \underbrace{+\,iy\,dx}_{}\ \underbrace{-\,i^2y\,dy}_{=+y\,dy}
=\underbrace{x\,dx+y\,dy}_{\text{대칭부}}+i\,(y\,dx-x\,dy),$$
$$\bar z\,dz=(x-iy)(dx+i\,dy)
=x\,dx+ix\,dy-iy\,dx-i^2y\,dy
=\underbrace{x\,dx+y\,dy}_{\text{대칭부}}-i\,(y\,dx-x\,dy).$$

빼면 대칭부는 소거되고 허수부만 두 배:
$$z\,d\bar z-\bar z\,dz=2i\,(y\,dx-x\,dy).$$
$\tfrac i2$를 곱하면 ($\tfrac i2\cdot2i=i^2=-1$):
$$\frac i2\bigl(z\,d\bar z-\bar z\,dz\bigr)=-(y\,dx-x\,dy)=x\,dy-y\,dx.$$
$$\boxed{\ \alpha=\sum_{r=1}^{2}\bigl(x_r\,dy_r-y_r\,dx_r\bigr)\ }$$

### 2b. 왜 앞에 $\frac i2$가 붙어 있나 — 실형식이 되도록

괄호 $z\,d\bar z-\bar z\,dz$는 **순허수** 조합이다: 켤레를 취하면
$$\overline{z\,d\bar z-\bar z\,dz}=\bar z\,dz-z\,d\bar z=-(z\,d\bar z-\bar z\,dz).$$
순허수에 $i$를 곱하면 실수가 된다 — $\tfrac i2$의 $i$는 실형식으로 만드는 역할($\bar\alpha=\alpha$), $\tfrac12$은 2a에서 두 배로 불어난 것의 정규화다. 실제로 결과 $x\,dy-y\,dx$는 실계수뿐이다.

---

## §3. Reeb 후보 = 원 작용의 무한소 생성원 (슬라이드 8, G3)

"무한소 생성원"의 뜻: 점 $v=(z_1,z_2)$를 원 작용으로 흘린 곡선
$$\gamma(\theta)=\bigl(e^{i\theta}z_1,\ e^{i\theta}z_2\bigr)$$
의 $\theta=0$ 속도벡터가 그 점에서의 벡터장 값. 할 일 세 동작: 실좌표로 적기 → $\theta$ 미분 → $\theta=0$ 대입.

### 3a. 실좌표로 적기 — 오일러 공식 + 분배법칙

$e^{i\theta}=\cos\theta+i\sin\theta$이므로
$$e^{i\theta}z_r=(\cos\theta+i\sin\theta)(x_r+iy_r)
=\underbrace{x_r\cos\theta-y_r\sin\theta}_{=:X_r(\theta)}
+\ i\,\underbrace{(x_r\sin\theta+y_r\cos\theta)}_{=:Y_r(\theta)}.$$
(네 항 추적: $x_r\cos\theta$ 실 · $iy_r\cos\theta$ 허 · $ix_r\sin\theta$ 허 · $i^2y_r\sin\theta=-y_r\sin\theta$ 실.)

### 3b. $\theta$로 미분 — 항마다 한 줄

$x_r,y_r$는 $\theta$와 무관(출발점 고정)이므로 $(\cos\theta)'=-\sin\theta$, $(\sin\theta)'=\cos\theta$만 쓴다:
$$X_r'(\theta)=-x_r\sin\theta-y_r\cos\theta,\qquad
Y_r'(\theta)=x_r\cos\theta-y_r\sin\theta.$$

### 3c. $\theta=0$ 대입

$\sin0=0,\ \cos0=1$:
$$X_r'(0)=-y_r,\qquad Y_r'(0)=x_r
\qquad\Longrightarrow\qquad
\boxed{\ R_\alpha=\sum_{r=1}^2\bigl(-y_r\,\partial_{x_r}+x_r\,\partial_{y_r}\bigr)\ }$$

### 3d. 복소 지름길 — 같은 답

$\frac{d}{d\theta}e^{i\theta}z_r\big|_{0}=iz_r$ (지수함수 미분), 그리고
$$iz_r=i(x_r+iy_r)=-y_r+ix_r$$
— 실수부 $-y_r$이 $x_r$ 방향, 허수부 $x_r$이 $y_r$ 방향. 3c와 동일. **$R_\alpha$의 정체 = "$i$ 곱하기" = 각 $\mathbb{C}$ 평면의 90° 회전.**

### 3e. 궤도가 $S^3$를 떠나지 않는다 — 교차항 소거 전부

$$X_r^2+Y_r^2=(x_r\cos\theta-y_r\sin\theta)^2+(x_r\sin\theta+y_r\cos\theta)^2$$
$$=x_r^2\cos^2\theta-2x_ry_r\cos\theta\sin\theta+y_r^2\sin^2\theta
+x_r^2\sin^2\theta+2x_ry_r\sin\theta\cos\theta+y_r^2\cos^2\theta$$
교차항 $\mp2x_ry_r\cos\theta\sin\theta$가 소거되고 $\cos^2+\sin^2=1$로 묶이면 $=x_r^2+y_r^2$. 합하면 $N$이 보존된다: 출발점이 $S^3$이면 궤도 전체가 $S^3$, 따라서 **속도벡터 $R_\alpha$는 $S^3$의 접벡터다.** (§7에서 결정적으로 쓴다.)

### 3f. $R_\alpha$의 길이

$$|R_\alpha|^2=\sum_r\bigl((-y_r)^2+x_r^2\bigr)=N\ \overset{S^3}{=}\ 1$$
— $S^3$ 위에서 **단위 벡터장**이다. 특히 어느 점에서도 0이 아니다.

---

## §4. 쌍대짝 네 개 (슬라이드 8, G4의 준비)

$R_\alpha$의 계수는 $a_r=-y_r$, $b_r=x_r$. 처음 한 번은 §1b처럼 네 항 전부:
$$dx_1(R_\alpha)=R_\alpha(x_1)
=(-y_1)\cdot\underbrace{\tfrac{\partial x_1}{\partial x_1}}_{1}
+x_1\cdot\underbrace{\tfrac{\partial x_1}{\partial y_1}}_{0}
+(-y_2)\cdot\underbrace{\tfrac{\partial x_1}{\partial x_2}}_{0}
+x_2\cdot\underbrace{\tfrac{\partial x_1}{\partial y_2}}_{0}
=-y_1.$$
나머지 셋은 살아남는 항만:
$$dy_1(R_\alpha)=x_1\cdot\tfrac{\partial y_1}{\partial y_1}=x_1,\qquad
dx_2(R_\alpha)=-y_2,\qquad dy_2(R_\alpha)=x_2.$$
$$\boxed{\ dx_r(R_\alpha)=-y_r,\qquad dy_r(R_\alpha)=x_r\ }$$

---

## §5. 첫째 조건 $\alpha(R_\alpha)=1$ (슬라이드 8, G4)

### 5a. 자리마다 대입

$$\alpha(R_\alpha)=\sum_{r}\Bigl(x_r\,\underbrace{dy_r(R_\alpha)}_{=x_r}-y_r\,\underbrace{dx_r(R_\alpha)}_{=-y_r}\Bigr)
=\sum_r\bigl(x_r^2+y_r^2\bigr)=N.$$
$$\boxed{\ \alpha(R_\alpha)=\|v\|^2\ \overset{S^3}{=}\ 1\ }$$

### 5b. "on $S^3$"의 뜻

$\alpha(R_\alpha)$는 $\mathbb{R}^4$의 함수로는 $N$ — 상수가 아니다. "$S^3$ 위에서 1"은 포함사상 $\iota:S^3\hookrightarrow\mathbb{R}^4$로 제한한 함수 $N\circ\iota\equiv1$이라는 뜻. (§7에서 이 구분이 실제로 일한다.)

### 5c. 숫자 한 점

$p=(x_1,y_1,x_2,y_2)=(\tfrac12,\tfrac12,\tfrac12,\tfrac12)$ ($N=4\cdot\tfrac14=1$ ✓). $R_\alpha|_p=(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12)$이고
$$\alpha(R_\alpha)\big|_p=\tfrac12\cdot\tfrac12-\tfrac12\cdot(-\tfrac12)+\tfrac12\cdot\tfrac12-\tfrac12\cdot(-\tfrac12)=\tfrac14\cdot4=1.\ \checkmark$$

---

## §6. $\alpha$가 "접속"인 이유 — 수직/수평 분해를 계산으로

여기가 파트 IV의 **의미의 중심**이다. $S^3$의 접벡터 $V$를 두 조각으로 나눈다:
$$V=\underbrace{\alpha(V)\,R_\alpha}_{\text{수직(vertical) = fiber 방향}}
+\underbrace{\bigl(V-\alpha(V)\,R_\alpha\bigr)}_{=:H,\ \text{수평(horizontal)}}.$$

### 6a. 수평 조각은 정말 $\alpha$를 0으로 만드는가

$\alpha$는 선형이므로
$$\alpha(H)=\alpha(V)-\alpha(V)\,\alpha(R_\alpha)=\alpha(V)\,\bigl(1-N\bigr)\ \overset{S^3}{=}\ 0.$$
— §5의 $\alpha(R_\alpha)=N$이 정확히 여기서 필요했다. $S^3$ 위에서 분해는 완벽하다:
$$T_pS^3=\underbrace{\mathrm{span}\{R_\alpha\}}_{1\text{차원 (§3f: }R_\alpha\neq0)}\ \oplus\ \underbrace{\ker\alpha\cap T_pS^3}_{2\text{차원}}
\qquad(3=1+2).$$
수평 2차원이 $\mathbb{CP}^1$ 접공간의 "대표"다 — **$\alpha$는 fiber 성분을 계량하고, 그것을 빼는 규칙이 접속이다.**

### 6b. 숫자로 한 번 끝까지

$p=(\tfrac12,\tfrac12,\tfrac12,\tfrac12)$, $V=\partial_{x_1}-\partial_{y_1}$ (접벡터인지는 §7g에서 확인). 먼저
$$\alpha(V)=x_1\cdot\underbrace{dy_1(V)}_{-1}-y_1\cdot\underbrace{dx_1(V)}_{1}+0=\tfrac12(-1)-\tfrac12(1)=-1.$$
수평 조각:
$$H=V-(-1)R_\alpha=V+R_\alpha
=(1,-1,0,0)+(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12)=(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12).$$
검산 둘: $\alpha(H)=\tfrac12(-\tfrac12)-\tfrac12(\tfrac12)+\tfrac12(\tfrac12)-\tfrac12(-\tfrac12)=-\tfrac14-\tfrac14+\tfrac14+\tfrac14=0$ ✓ (수평);
$dN(H)=2\bigl[\tfrac12\cdot\tfrac12+\tfrac12(-\tfrac12)+\tfrac12(-\tfrac12)+\tfrac12\cdot\tfrac12\bigr]=0$ ✓ (여전히 접벡터).

### 6c. FS와의 다리 — $(1-P)$가 죽이는 방향이 정확히 $R_\alpha$다

완전판 Part III의 사영 $(1-P)$, $P=\psi\psi^*$를 fiber 방향 $i\psi$에 걸어 본다 ($Pu=\psi\langle\psi,u\rangle$):
$$\langle\psi,i\psi\rangle=i\,\langle\psi,\psi\rangle=i
\quad\Longrightarrow\quad
P(i\psi)=\psi\cdot i=i\psi
\quad\Longrightarrow\quad
\boxed{\ (1-P)(i\psi)=0\ }$$
그런데 §3d에서 $i\psi$의 실좌표 아바타가 곧 $R_\alpha$였다. 즉:
**FS 계량이 사영으로 제거하는 방향($i\psi$) = $\alpha$가 1로 재는 방향($R_\alpha$).** 같은 분해를 Part III는 복소·행렬 언어로, Part IV는 실좌표·미분형식 언어로 말하고 있다.

---

## §7. $d\alpha$와 둘째 조건 $\iota_{R_\alpha}d\alpha=0$

### 7a. $d\alpha$ — 라이프니츠 한 줄씩 (슬라이드 9, G5)

규칙: $d(f\,\beta)=df\wedge\beta+f\,d\beta$, $d(dg)=0$, $\beta\wedge\gamma=-\gamma\wedge\beta$.

$$d(x_r\,dy_r)=dx_r\wedge dy_r+x_r\,\underbrace{d(dy_r)}_{=0}=dx_r\wedge dy_r,$$
$$d(-y_r\,dx_r)=-dy_r\wedge dx_r+(-y_r)\cdot\underbrace{d(dx_r)}_{=0}=-\,dy_r\wedge dx_r=+\,dx_r\wedge dy_r.$$
두 항 모두 $dx_r\wedge dy_r$을 주므로
$$\boxed{\ d\alpha=2\sum_{r=1}^2 dx_r\wedge dy_r\ }$$

### 7b. 2-형식이 벡터 두 개를 먹는 규칙 — 부호의 출처

쐐기곱의 **정의**(1-형식 $\beta,\gamma$):
$$(\beta\wedge\gamma)(U,V)=\beta(U)\gamma(V)-\beta(V)\gamma(U)
=\det\begin{pmatrix}\beta(U)&\beta(V)\\ \gamma(U)&\gamma(V)\end{pmatrix}.$$
검사: $(dx\wedge dy)(\partial_x,\partial_y)=1\cdot1-0\cdot0=1$, 순서를 바꾸면 $-1$ — 반대칭은 행렬식의 반대칭이다.

### 7c. 내부곱 — 첫째 칸에 $R$을 꽂는다

정의: $(\iota_R\omega)(V):=\omega(R,V)$. 7b에서 $U=R$을 넣고 $V$ 자리를 비워 읽으면
$$\boxed{\ \iota_R(\beta\wedge\gamma)=\beta(R)\,\gamma-\gamma(R)\,\beta\ }$$
— "1-형식 두 장 중 한 장이 $R$을 먹고, 남은 한 장이 결과 1-형식이 된다. 순서 바꾼 쪽은 마이너스."

### 7d. 항 하나에 적용, 그리고 합산

$\beta=dx_r,\ \gamma=dy_r$과 §4의 쌍대짝:
$$\iota_{R_\alpha}(dx_r\wedge dy_r)=\underbrace{dx_r(R_\alpha)}_{-y_r}\,dy_r-\underbrace{dy_r(R_\alpha)}_{x_r}\,dx_r
=-y_r\,dy_r-x_r\,dx_r.$$
합산($d\alpha$의 계수 2 포함):
$$\iota_{R_\alpha}d\alpha=2\sum_r\bigl(-x_r\,dx_r-y_r\,dy_r\bigr)
=-\sum_r\bigl(2x_r\,dx_r+2y_r\,dy_r\bigr).$$

### 7e. 이 1-형식의 정체 — $N$의 전미분

합성함수 미분 $d(x^2)=2x\,dx$를 네 좌표 각각에:
$$dN=d\bigl(x_1^2+y_1^2+x_2^2+y_2^2\bigr)=2x_1dx_1+2y_1dy_1+2x_2dx_2+2y_2dy_2.$$
7d와 자리마다 비교하면
$$\boxed{\ \iota_{R_\alpha}d\alpha=-\,dN\ }$$
**주의: $\mathbb{R}^4$에서는 0이 아니다.** $dN$은 멀쩡한 1-형식이다. 0이 되는 것은 $S^3$에 제한할 때다.

### 7f. $S^3$에서 죽는 이유 — 곡선 한 줄로

$S^3$의 접벡터 $V$를 잡자. 정의상 $V=c'(0)$인 곡선 $c$가 $S^3$ **안에** 있다. §1c의 규칙:
$$dN(V)=\frac{d}{dt}\Big|_{0}\,N\bigl(c(t)\bigr)=\frac{d}{dt}\Big|_{0}\,1=0$$
— $c$가 $S^3$ 안에 머무는 한 $N\circ c\equiv1$, **상수의 미분은 0.** 따라서 모든 접벡터 $V$에 대해
$$(\iota_{R_\alpha}d\alpha)(V)=-dN(V)=0
\qquad\Longrightarrow\qquad
\boxed{\ \iota_{R_\alpha}d\alpha=0\ \text{ on } S^3\ }$$
(pullback의 말로 같은 내용: $\iota^*(dN)=d(N\circ\iota)=d(1)=0$ — "$d$와 pullback의 교환"이 좌표로는 방금 그 합성함수 미분이다.)

### 7g. 숫자 한 점 검산

$p=(\tfrac12,\tfrac12,\tfrac12,\tfrac12)$에서
$$\iota_{R_\alpha}d\alpha\big|_p=-(dx_1+dy_1+dx_2+dy_2).$$
$V=\partial_{x_1}-\partial_{y_1}$: 먼저 접벡터인지 — $dN(V)=2x_1\cdot1+2y_1\cdot(-1)=1-1=0$ ✓. 먹이면
$$-(1-1+0+0)=0.\ \checkmark$$
이중 검산 — 정의 7b로 직접: $d\alpha(R_\alpha,V)=2\sum_r\bigl[dx_r(R)\,dy_r(V)-dx_r(V)\,dy_r(R)\bigr]$, $r=1$ 항 $=(-\tfrac12)(-1)-(1)(\tfrac12)=0$, $r=2$ 항 $=0$. 합 0 ✓.

---

## §8. fiber 위에서 $\alpha=d\theta$ (슬라이드 8, G2) — pullback의 모든 동작

### 8a. pullback의 정의 두 줄

- 함수: $c^*f=f\circ c$ ("곡선 위에서 읽어라").
- 1-형식: $c^*(df)=d(f\circ c)$ — 좌표로는 합성함수 미분. 그리고 $c^*$는 곱·합을 보존: $c^*(f\beta)=(c^*f)(c^*\beta)$.

### 8b. 재료 네 개

fiber 곡선 $c(\theta)=(e^{i\theta},0)$: $x_1\circ c=\cos\theta,\ y_1\circ c=\sin\theta,\ x_2\circ c=y_2\circ c=0$.
$$c^*(dx_1)=d(\cos\theta)=-\sin\theta\,d\theta,\qquad c^*(dy_1)=d(\sin\theta)=\cos\theta\,d\theta,$$
$$c^*(dx_2)=d(0)=0,\qquad c^*(dy_2)=0.$$

### 8c. 항별 대입

$$c^*\alpha=\underbrace{(x_1\circ c)}_{\cos\theta}\underbrace{c^*(dy_1)}_{\cos\theta\,d\theta}
-\underbrace{(y_1\circ c)}_{\sin\theta}\underbrace{c^*(dx_1)}_{-\sin\theta\,d\theta}
+\underbrace{0-0}_{r=2}
=(\cos^2\theta+\sin^2\theta)\,d\theta=\boxed{\ d\theta\ }$$

### 8d. 한 그림으로 — fiber는 $R_\alpha$의 적분곡선

$$c'(\theta)=(-\sin\theta,\ \cos\theta,\ 0,\ 0),\qquad
R_\alpha\big|_{c(\theta)}=(-y_1,\ x_1,\ -y_2,\ x_2)\big|_{c(\theta)}=(-\sin\theta,\ \cos\theta,\ 0,\ 0)$$
— **성분까지 같다.** $c^*\alpha=d\theta$는 "$\alpha$가 이 흐름의 속도를 1로 잰다"($\alpha(R_\alpha)=1$)를 곡선 위에서 다시 말한 것.

---

## §9. 요약 — 남에게 설명하는 순서

| 단계 | 계산의 뼈대 | 결과 | 절 |
|---|---|---|---|
| $\alpha$ 실좌표 | 분배법칙 8항, 대칭부 소거 | $\sum(x\,dy-y\,dx)$, 실형식 | §2 |
| 생성원 | 오일러 전개 → $\theta$ 미분 → $0$ 대입 ($=iz$) | $R_\alpha=\sum(-y\partial_x+x\partial_y)$ | §3 |
| 쌍대짝 | $dx_r(V)=a_r$ 규칙 | $dx_r(R)=-y_r$, $dy_r(R)=x_r$ | §4 |
| 조건 1 | 자리마다 대입 | $\alpha(R)=N\overset{S^3}{=}1$ | §5 |
| 분해 | $\alpha(V-\alpha(V)R)=\alpha(V)(1-N)$ | 수직$\oplus$수평, $(1-P)(i\psi)=0$ | §6 |
| $d\alpha$ | 라이프니츠, $d^2=0$ | $2\sum dx\wedge dy$ | §7a |
| 조건 2 | $\iota_R(\beta\wedge\gamma)=\beta(R)\gamma-\gamma(R)\beta$ | $\iota_Rd\alpha=-dN\overset{S^3}{=}0$ | §7d–f |
| fiber | $c^*(df)=d(f\circ c)$ | $c^*\alpha=d\theta$, $c'=R_\alpha$ | §8 |

세 줄 버전:
1. $R_\alpha$는 "$i$ 곱하기"(위상 회전)의 속도장이고, $S^3$ 위 단위 벡터장이다.
2. $\alpha$는 그 방향을 정확히 1로 읽으며($\alpha(R)=N=1$), 그래서 접벡터를 수직($R$ 방향)$\oplus$수평($\ker\alpha$)으로 가른다 — FS의 $(1-P)$와 같은 분해.
3. $d\alpha$에 $R$을 꽂으면 $-dN$인데, $S^3$ 안에 머무는 곡선을 따라 $N\equiv1$이므로 접방향에서 0이다.

*좌표 계산의 재료는 여섯: 쌍대 규칙 $dx_r(\partial_{x_s})=\delta_{rs}$ · 오일러 공식 · 라이프니츠 $d(f\beta)=df\wedge\beta$ · 반대칭(행렬식) · 합성함수 미분 $df(c'(t))=\frac{d}{dt}f(c(t))$ · 사영 $Pu=\psi\langle\psi,u\rangle$. 검산: `python verify_reeb.py`.*
