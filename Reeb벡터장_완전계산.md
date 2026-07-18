# Reeb 벡터장 완전 계산 — 합성함수 미분 수준까지

> **목적.** 발표(Hopf → FS → $\int\omega_{FS}=2\pi$) 전에 Reeb 벡터장 계산을 손으로 완전히 재현하기 위한 연습 대본. A1 워크시트의 G2·G3·G4를 중심으로, 그 앞뒤(G1, G5, 그리고 Reeb 둘째 조건 $\iota_{R}d\alpha=0$)까지 **정의 확인 → 대입 → 라이프니츠/합성함수 미분 → 정리**의 모든 줄을 생략 없이 적는다.
> **최종 목표 두 줄.** $R_\alpha=\sum_r(-y_r\partial_{x_r}+x_r\partial_{y_r})$ 에 대해
> $$\alpha(R_\alpha)=1 \quad\text{그리고}\quad \iota_{R_\alpha}d\alpha=0 \qquad (\text{on } S^3)$$
> 이 두 조건이 Reeb 벡터장의 정의다.

---

## 0. 등장인물과 표기

- 좌표: $\mathbb{C}^2=\mathbb{R}^4$, $z_r=x_r+iy_r$ ($r=1,2$). 켤레는 $\overline{z}_r=x_r-iy_r$.
- 구면: $S^3=\{x_1^2+y_1^2+x_2^2+y_2^2=1\}\subset\mathbb{R}^4$.
- 1-형식:
$$\alpha=\frac{i}{2}\sum_{r=1}^{2}\left(z_r\,d\overline{z}_r-\overline{z}_r\,dz_r\right).$$
- 후보 벡터장:
$$R_\alpha=\sum_{r=1}^{2}\left(-y_r\,\partial_{x_r}+x_r\,\partial_{y_r}\right).$$

이 문서에서 확인할 것: **(§2)** $R_\alpha$가 원 작용 $(z_1,z_2)\mapsto(e^{i\theta}z_1,e^{i\theta}z_2)$의 무한소 생성원이라는 것, **(§4)** $\alpha(R_\alpha)=1$, **(§6)** $\iota_{R_\alpha}d\alpha=0$, **(§7)** fiber 곡선으로 당기면(pullback) $\alpha=d\theta$.

---

## 1. 준비 운동 두 개 — 벡터장·1-형식이 하는 일, 그리고 $\alpha$의 실좌표꼴

### 1a. $\partial_{x_r}$와 $dx_r$의 쌍대 규칙 — 이것 하나로 §3·§4가 끝난다

벡터장은 좌표벡터장의 결합으로 적는다:
$$V=\sum_{s=1}^{2}\left(a_s\,\partial_{x_s}+b_s\,\partial_{y_s}\right).$$

1-형식 $dx_r$이 $V$에게 하는 일의 **정의**는 "좌표함수 $x_r$을 $V$ 방향으로 미분한 값"이다:
$$dx_r(V)=V(x_r)=\sum_{s}\left(a_s\,\frac{\partial x_r}{\partial x_s}+b_s\,\frac{\partial x_r}{\partial y_s}\right).$$

편미분을 하나하나 계산하면: $x_1, y_1, x_2, y_2$는 서로 **독립 좌표**이므로

$$\frac{\partial x_r}{\partial x_s}=\delta_{rs}\ (\text{같은 것끼리만 }1),\qquad \frac{\partial x_r}{\partial y_s}=0\ (\text{전부}).$$

따라서 살아남는 항은 $s=r$의 $a_r\cdot1$ 하나뿐:
$$\boxed{\ dx_r(V)=a_r,\qquad dy_r(V)=b_r\ }$$
($dy_r$ 쪽도 같은 계산: $\partial y_r/\partial y_s=\delta_{rs}$, $\partial y_r/\partial x_s=0$.)

**한 문장 요약.** $dx_r$는 벡터장에서 "$\partial_{x_r}$ 앞의 계수"를 읽어내는 기계다.

### 1b. $\alpha$를 실좌표로 (G1 전체 전개)

성분 하나 $z=x+iy$에 대해 $\frac{i}{2}(z\,d\overline z-\overline z\,dz)$를 전개한다. 먼저 재료:
$$dz=dx+i\,dy,\qquad d\overline z=dx-i\,dy.$$

곱 하나씩 (분배법칙, $i^2=-1$):
$$z\,d\overline z=(x+iy)(dx-i\,dy)=x\,dx-ix\,dy+iy\,dx-i^2y\,dy=\underbrace{x\,dx+y\,dy}_{\text{실수부}}+i\,(y\,dx-x\,dy),$$
$$\overline z\,dz=(x-iy)(dx+i\,dy)=x\,dx+ix\,dy-iy\,dx-i^2y\,dy=\underbrace{x\,dx+y\,dy}_{\text{실수부}}-i\,(y\,dx-x\,dy).$$

빼면 실수부는 소거되고 허수부만 두 배:
$$z\,d\overline z-\overline z\,dz=2i\,(y\,dx-x\,dy).$$

$\frac{i}{2}$를 곱하면 ($\frac{i}{2}\cdot 2i=i^2=-1$):
$$\frac{i}{2}\left(z\,d\overline z-\overline z\,dz\right)=-(y\,dx-x\,dy)=x\,dy-y\,dx.$$

$r=1,2$를 더해서:
$$\boxed{\ \alpha=\sum_{r=1}^{2}\left(x_r\,dy_r-y_r\,dx_r\right)\ }$$

---

## 2. 원 작용의 무한소 생성원 (G3) — 곡선을 그리고, $\theta$로 미분한다

"무한소 생성원"의 뜻: 점 $(z_1,z_2)$를 원 작용으로 흘려보낸 곡선
$$\gamma(\theta)=\left(e^{i\theta}z_1,\ e^{i\theta}z_2\right)$$
의 $\theta=0$에서의 **속도벡터**가 그 점에서의 벡터장 값이라는 것. 그러니 할 일은 (i) $\gamma$를 실좌표로 적고 (ii) $\theta$로 미분하고 (iii) $\theta=0$을 대입하는 것, 세 동작뿐이다.

### 2a. 실좌표로 적기 — 오일러 공식 + 분배법칙

$e^{i\theta}=\cos\theta+i\sin\theta$ 이므로, 성분 하나:
$$e^{i\theta}z_r=(\cos\theta+i\sin\theta)(x_r+iy_r)
=\underbrace{\left(x_r\cos\theta-y_r\sin\theta\right)}_{=:X_r(\theta)}
+i\,\underbrace{\left(x_r\sin\theta+y_r\cos\theta\right)}_{=:Y_r(\theta)}.$$

(전개 확인: $\cos\theta\cdot x_r + \cos\theta\cdot iy_r + i\sin\theta\cdot x_r + i^2\sin\theta\cdot y_r$, 여기서 $i^2y_r\sin\theta=-y_r\sin\theta$가 실수부로, 나머지 $i$ 붙은 두 항이 허수부로 간다.)

### 2b. $\theta$로 미분 — 항마다 한 줄씩

$x_r, y_r$는 $\theta$와 무관한 상수 취급이므로, 각 항은 $\frac{d}{d\theta}\cos\theta=-\sin\theta$, $\frac{d}{d\theta}\sin\theta=\cos\theta$만 쓰면 된다:
$$X_r'(\theta)=x_r\cdot(-\sin\theta)-y_r\cdot\cos\theta=-x_r\sin\theta-y_r\cos\theta,$$
$$Y_r'(\theta)=x_r\cdot\cos\theta+y_r\cdot(-\sin\theta)=x_r\cos\theta-y_r\sin\theta.$$

### 2c. $\theta=0$ 대입

$\sin0=0$, $\cos0=1$:
$$X_r'(0)=-y_r,\qquad Y_r'(0)=x_r.$$

속도벡터를 좌표벡터장으로 적으면
$$\gamma'(0)=\sum_{r=1}^{2}\left(-y_r\,\partial_{x_r}+x_r\,\partial_{y_r}\right)=R_\alpha. \qquad\blacksquare$$

### 2d. 같은 답, 복소 지름길

$\frac{d}{d\theta}e^{i\theta}z_r\big|_{\theta=0}=iz_r$ (지수함수 미분). 그리고
$$iz_r=i(x_r+iy_r)=-y_r+ix_r$$
— 실수부 $-y_r$이 $x_r$ 방향 속도, 허수부 $x_r$이 $y_r$ 방향 속도. 2c와 동일. **"$i$를 곱한다 = 각 $\mathbb{C}$ 평면에서 90° 회전"**이 $R_\alpha$의 정체다.

### 2e. 검산 — 곡선이 $S^3$를 떠나지 않는다

$$X_r^2+Y_r^2=(x_r\cos\theta-y_r\sin\theta)^2+(x_r\sin\theta+y_r\cos\theta)^2.$$
전개하면 교차항이 소거된다:
$$=x_r^2\cos^2\theta-2x_ry_r\cos\theta\sin\theta+y_r^2\sin^2\theta
+x_r^2\sin^2\theta+2x_ry_r\sin\theta\cos\theta+y_r^2\cos^2\theta
=x_r^2+y_r^2.$$
따라서 $\sum_r(X_r^2+Y_r^2)=\sum_r(x_r^2+y_r^2)=1$ — 시작점이 $S^3$이면 곡선 전체가 $S^3$ 위. 특히 **속도벡터 $R_\alpha$는 $S^3$의 접벡터다** (§6에서 이 사실이 결정적으로 쓰인다).

---

## 3. 쌍대짝 네 개 (G4의 준비) — $dx_r(R_\alpha)$, $dy_r(R_\alpha)$

$R_\alpha$의 계수를 §1a의 표기로 읽으면 $a_r=-y_r$, $b_r=x_r$. §1a의 규칙을 그대로 적용하되, 처음 한 번은 **네 항 전부** 적어 보자. $dx_1(R_\alpha)=R_\alpha(x_1)$:

$$R_\alpha(x_1)=(-y_1)\underbrace{\frac{\partial x_1}{\partial x_1}}_{=1}+x_1\underbrace{\frac{\partial x_1}{\partial y_1}}_{=0}+(-y_2)\underbrace{\frac{\partial x_1}{\partial x_2}}_{=0}+x_2\underbrace{\frac{\partial x_1}{\partial y_2}}_{=0}=-y_1.$$

같은 방식으로 나머지 셋 (살아남는 항만 표시):
$$dy_1(R_\alpha)=x_1\cdot\frac{\partial y_1}{\partial y_1}=x_1,\qquad
dx_2(R_\alpha)=-y_2,\qquad
dy_2(R_\alpha)=x_2.$$

$$\boxed{\ dx_r(R_\alpha)=-y_r,\qquad dy_r(R_\alpha)=x_r\ }$$

---

## 4. 첫째 조건: $\alpha(R_\alpha)=1$ (G4)

§1b의 $\alpha$에 §3의 짝을 **자리마다** 대입한다. 1-형식은 벡터장에 대해 선형이므로 항별로 계산하면 된다:

$$\alpha(R_\alpha)=\sum_{r=1}^{2}\Big(x_r\,\underbrace{dy_r(R_\alpha)}_{=x_r}-y_r\,\underbrace{dx_r(R_\alpha)}_{=-y_r}\Big)
=\sum_{r=1}^{2}\left(x_r^2+y_r^2\right).$$

$\mathbb{R}^4$ 전체에서 이 값은 함수 $N:=x_1^2+y_1^2+x_2^2+y_2^2=\|v\|^2$이고, $S^3$ **위에서는** $N=1$:
$$\boxed{\ \alpha(R_\alpha)=\|v\|^2=1 \quad\text{on } S^3\ }$$

**"on $S^3$"의 뜻을 분명히.** $\alpha(R_\alpha)$는 $\mathbb{R}^4$의 함수로는 $N$이다 — 상수가 아니다. "$S^3$ 위에서 1"이라는 말은 포함사상 $\iota:S^3\hookrightarrow\mathbb{R}^4$로 **당긴(제한한)** 함수 $N\circ\iota$가 상수함수 1이라는 뜻이다. §6에서 이 구분이 실제로 일을 한다.

**숫자 한 점 검산.** $(x_1,y_1,x_2,y_2)=(\tfrac12,\tfrac12,\tfrac12,\tfrac12)$ (norm$^2=\tfrac14\cdot4=1$, $S^3$ 위). 이 점에서 $R_\alpha=(-\tfrac12,\tfrac12,-\tfrac12,\tfrac12)$이고
$$\alpha(R_\alpha)=x_1b_1-y_1a_1+x_2b_2-y_2a_2
=\tfrac12\cdot\tfrac12-\tfrac12\cdot(-\tfrac12)+\tfrac12\cdot\tfrac12-\tfrac12\cdot(-\tfrac12)
=\tfrac14+\tfrac14+\tfrac14+\tfrac14=1.\ \checkmark$$

---

## 5. $d\alpha$ — 라이프니츠 한 줄씩 (G5)

외미분의 라이프니츠 규칙: $d(f\,\beta)=df\wedge\beta+f\,d\beta$ ($f$ 함수, $\beta$ 1-형식). 그리고 $d(dy_r)=0$ ($d^2=0$).

항 하나: $f=x_r$, $\beta=dy_r$.
$$d(x_r\,dy_r)=\underbrace{dx_r}_{=df}\wedge\,dy_r+x_r\,\underbrace{d(dy_r)}_{=0}=dx_r\wedge dy_r.$$

다음 항: $f=-y_r$, $\beta=dx_r$.
$$d(-y_r\,dx_r)=-dy_r\wedge dx_r+(-y_r)\cdot0=-\,dy_r\wedge dx_r.$$

쐐기곱의 반대칭 $\beta\wedge\gamma=-\gamma\wedge\beta$로 방향을 통일하면 $-\,dy_r\wedge dx_r=+\,dx_r\wedge dy_r$. 두 항이 같은 것을 하나씩 내놓으므로:
$$\boxed{\ d\alpha=2\sum_{r=1}^{2}dx_r\wedge dy_r\ }$$

---

## 6. 둘째 조건: $\iota_{R_\alpha}d\alpha=0$ — 이 문서의 본론

### 6a. 내부곱(interior product)의 계산 규칙

2-형식 $\omega$에 벡터장 $R$을 "첫째 칸에 꽂는" 것이 내부곱이다: $(\iota_R\omega)(V):=\omega(R,V)$. 쐐기곱의 정의
$$(\beta\wedge\gamma)(R,V)=\beta(R)\gamma(V)-\beta(V)\gamma(R)$$
에서 $V$ 자리를 비워 두고 읽으면, 1-형식 $\beta,\gamma$에 대해
$$\iota_R(\beta\wedge\gamma)=\beta(R)\,\gamma-\gamma(R)\,\beta.$$

### 6b. 항 하나에 적용

$\beta=dx_r$, $\gamma=dy_r$, 그리고 §3의 짝:
$$\iota_{R_\alpha}(dx_r\wedge dy_r)=\underbrace{dx_r(R_\alpha)}_{=-y_r}\,dy_r-\underbrace{dy_r(R_\alpha)}_{=x_r}\,dx_r
=-y_r\,dy_r-x_r\,dx_r.$$

### 6c. 합산

$$\iota_{R_\alpha}d\alpha=2\sum_{r=1}^{2}\left(-x_r\,dx_r-y_r\,dy_r\right)
=-2\sum_{r=1}^{2}\left(x_r\,dx_r+y_r\,dy_r\right).$$

### 6d. 이 1-형식의 정체 — $N$의 전미분

합성함수 미분 $d(x^2)=2x\,dx$ (바깥 $u^2$ 미분 $2u$, 안쪽 그대로)를 좌표마다 쓰면:
$$dN=d\left(x_1^2+y_1^2+x_2^2+y_2^2\right)=2x_1\,dx_1+2y_1\,dy_1+2x_2\,dx_2+2y_2\,dy_2.$$

6c와 비교하면 정확히
$$\boxed{\ \iota_{R_\alpha}d\alpha=-dN\ }$$

**주의: $\mathbb{R}^4$에서는 0이 아니다.** $dN$은 멀쩡히 살아 있는 1-형식이다. 0이 되는 것은 $S^3$에 **제한했을 때**다.

### 6e. $S^3$로 당기면 죽는다 — pullback 한 단계씩

포함사상 $\iota:S^3\hookrightarrow\mathbb{R}^4$의 pullback이 하는 일:

- **함수에 대해**: $\iota^*N=N\circ\iota$ — "함수를 $S^3$ 위에서만 읽어라". 그런데 $S^3$의 정의가 바로 $N=1$이므로 $N\circ\iota\equiv1$, **상수함수**.
- **외미분과 교환**: $\iota^*(dN)=d(\iota^*N)$. (pullback의 기본 성질 — 좌표로 쓰면 합성함수 미분 그 자체다.)

두 줄을 이으면:
$$\iota^*(dN)=d(N\circ\iota)=d(1)=0$$
— 상수함수의 미분은 0. 따라서
$$\iota^*\left(\iota_{R_\alpha}d\alpha\right)=-\iota^*(dN)=0.
\qquad\boxed{\ \iota_{R_\alpha}d\alpha=0 \quad\text{on } S^3\ }$$

### 6f. 같은 결론, 기하의 말로

$dN(V)=0$ ⟺ $V$가 등위면 $\{N=1\}=S^3$의 **접벡터**. §2e에서 $R_\alpha$가 $S^3$의 접벡터임을 이미 확인했다. 그러므로 $S^3$의 임의의 접벡터 $V$에 대해
$$(\iota_{R_\alpha}d\alpha)(V)=d\alpha(R_\alpha,V)=-dN(V)=0$$
— "$d\alpha$에 $R_\alpha$를 꽂으면, 접방향에서는 아무것도 재지 못한다".

**숫자 한 점 검산.** §4의 점 $(\tfrac12,\tfrac12,\tfrac12,\tfrac12)$에서 $\iota_{R_\alpha}d\alpha=-2\left(\tfrac12dx_1+\tfrac12dy_1+\tfrac12dx_2+\tfrac12dy_2\right)=-(dx_1+dy_1+dx_2+dy_2)$. 접벡터 하나, 예컨대 $V=\partial_{x_1}-\partial_{y_1}$ ($dN(V)=2\cdot\tfrac12-2\cdot\tfrac12=0$이므로 접벡터)에 먹이면 $-(1-1+0+0)=0$. $\checkmark$

---

## 7. fiber 곡선으로 당겨서 재확인 (G2) — pullback의 모든 동작

fiber 하나를 곡선으로 적는다: $c(\theta)=(e^{i\theta},0)$, 즉
$$x_1\circ c=\cos\theta,\quad y_1\circ c=\sin\theta,\quad x_2\circ c=0,\quad y_2\circ c=0.$$

**pullback의 정의 두 줄:**

- 함수: $c^*f=f\circ c$ (곡선 위에서 읽기).
- 1-형식: $c^*(df)=d(f\circ c)$ — 좌표로는 **합성함수 미분**이다.

재료 네 개를 하나씩:
$$c^*(dx_1)=d(\cos\theta)=-\sin\theta\,d\theta,\qquad
c^*(dy_1)=d(\sin\theta)=\cos\theta\,d\theta,$$
$$c^*(dx_2)=d(0)=0,\qquad c^*(dy_2)=d(0)=0.$$

pullback은 곱과 합을 보존하므로 ($c^*(f\beta)=(c^*f)(c^*\beta)$), $\alpha$에 항별로 적용:
$$c^*\alpha=\underbrace{(x_1\circ c)}_{\cos\theta}\underbrace{c^*(dy_1)}_{\cos\theta\,d\theta}
-\underbrace{(y_1\circ c)}_{\sin\theta}\underbrace{c^*(dx_1)}_{-\sin\theta\,d\theta}
+\underbrace{0\cdot0-0\cdot0}_{r=2\ \text{항}}$$
$$=\cos^2\theta\,d\theta+\sin^2\theta\,d\theta=\boxed{\ d\theta\ }$$

**§2·§3·§4와 한 그림으로.** 곡선의 속도는 $c'(\theta)=(-\sin\theta,\cos\theta,0,0)$인데, $c(\theta)$ 점에서의 $R_\alpha$ 값은 $(-y_1,x_1,-y_2,x_2)\big|_{c(\theta)}=(-\sin\theta,\cos\theta,0,0)$ — **정확히 같다.** fiber는 $R_\alpha$의 적분곡선이고, $c^*\alpha=d\theta$는 "$\alpha$가 그 흐름의 속도를 1로 잰다"($\alpha(R_\alpha)=1$)를 곡선 위에서 다시 말한 것이다.

---

## 8. 요약 — 세 줄로 남에게 설명하기

| 조건 | 계산의 뼈대 | 결과 |
|---|---|---|
| 생성원 | $\frac{d}{d\theta}e^{i\theta}z_r\big|_0=iz_r$, $iz_r=-y_r+ix_r$ | $R_\alpha=\sum(-y_r\partial_{x_r}+x_r\partial_{y_r})$ |
| $\alpha(R_\alpha)$ | 쌍대짝 $dx_r(R)=-y_r$, $dy_r(R)=x_r$ 대입 | $\sum(x_r^2+y_r^2)=\|v\|^2=1$ on $S^3$ |
| $\iota_{R_\alpha}d\alpha$ | $\iota_R(dx\wedge dy)=dx(R)dy-dy(R)dx$ → $-dN$ | $\iota^*(dN)=d(1)=0$ on $S^3$ |

1. $R_\alpha$는 "$i$ 곱하기"(위상 회전)의 속도장이다.
2. $\alpha$는 그 회전 속도를 정확히 1로 읽는다 — 값이 $\|v\|^2$라서 $S^3$ 위에서 1.
3. $d\alpha$에 $R_\alpha$를 꽂으면 $-d\|v\|^2$가 나오는데, $S^3$에서는 $\|v\|^2$가 상수 1이므로 미분이 0.

*모든 좌표 계산의 재료는 다섯 개뿐: 쌍대 규칙 $dx_r(\partial_{x_s})=\delta_{rs}$ · 오일러 공식 · 라이프니츠 $d(f\beta)=df\wedge\beta$ · 반대칭 $\beta\wedge\gamma=-\gamma\wedge\beta$ · 합성함수 미분 $c^*(df)=d(f\circ c)$.*
