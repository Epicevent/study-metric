# 3 — 곡률: 사영자를 두 번 미분한다 (정칙방향은 모두 $K=2$)

> **흐름.** 문서 `2`는 공 위 점을 사영자 $P=vv^*/N$ 로, 계량을 $\operatorname{tr}(dP\,dP)$ 로 짓고, $dP$ 의 정칙 성분 $B=P\,dP(1{-}P)=\partial_z P\,dz$ 를 남겼다. 곡률은 그 $P$ 를 **한 번 더** 미분해 나온다 — 문서 `0`이 구면에서 법선 $\vec n$ 을 미분(shape operator)해 곡률을 잰 그 짓을, 평평한 $\mathrm{Herm}$ 속 사영자에 그대로.
>
> **퀄리티 기준 = 손노트.** 관찰 먼저, 실제 행렬·손계산 예시, 모든 줄 검산(부록). 내적 $\langle A,B\rangle=\operatorname{tr}(AB)$, $S=1+\sum|z_i|^2$, $E_{ab}$ = $(a,b)$ 성분만 1인 행렬.

---

## 1. 곡률은 어디서 나오나 — 사영자를 두 번 미분 (Part1의 근본개념)

Part1은 곡률을 공식에서 꺼내지 않았다. 구면 점을 **단위법선 $\vec n$ 으로 보고 그 법선을 미분**(shape operator $-d\vec n$)해 제2기본형식으로 $K$ 를 얻고, *거기서* 내재 공식 $K=-\tfrac1{2\lambda}\Delta\log\lambda$ 를 유도했다(가우스의 위대한 정리). 곡률의 근본은 **임베딩을 두 번 미분한 제2기본형식**이지 내재 공식이 아니다. 여기서도 같은 손으로 간다 — 공 위 점의 사영자 $P$ 가 평평한 $\mathrm{Herm}$ 에 박힌 대상이고, 곡률은 $P$ 를 두 번 미분(문서 `2`의 $B=\partial_z P$ 를 한 번 더)한 제2기본형식에서 나온다. (그 근본 도구인 Gauss 방정식은 §2.1에서 Part1의 일반판으로 유도.)

### 1.1 CP¹: 제1·제2기본형식을 직접 계산 → $K=2$ (Part1과 같은 손)

사영자 임베딩 $P(x,y)$ ($z=x+iy$) 는 3차원 $\mathrm{Herm}_0=\operatorname{span}\{\sigma_1,\sigma_2,\sigma_3\}$ 속 곡면(여차원 1)이라 Part1의 곡면 공식이 그대로다. $z=0$ 에서 직접 미분한다 ($\partial_x=\partial_z+\partial_{\bar z}$, $\partial_y=i(\partial_z-\partial_{\bar z})$; §2.3의 $\partial_z P|_0=E_{10}$, $\partial_z\partial_{\bar z}P|_0=E_{11}-E_{00}$).

**1계 — 접벡터.**
$$
P_x|_0=E_{10}+E_{01}=\sigma_1,\qquad P_y|_0=i(E_{10}-E_{01})=\sigma_2.
$$
**제1기본형식** ($\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}$):
$$
E=\langle P_x,P_x\rangle=\operatorname{tr}(\sigma_1^2)=2,\quad F=\langle P_x,P_y\rangle=\operatorname{tr}(\sigma_1\sigma_2)=0,\quad G=\langle P_y,P_y\rangle=\operatorname{tr}(\sigma_2^2)=2.
$$
(일반 $z$ 면 $E=G=2/S^2$, $F=0$ — 문서 `2`의 사영자 계량 $\operatorname{tr}(dP\,dP)$.)

**2계 + 단위법선.**
$$
P_{xx}|_0=(\partial_z+\partial_{\bar z})^2P|_0=2\,\partial_z\partial_{\bar z}P|_0=2(E_{11}-E_{00})=-2\sigma_3,\quad P_{yy}|_0=-2\sigma_3,\quad P_{xy}|_0=i(\partial_z^2-\partial_{\bar z}^2)P|_0=0.
$$
접평면은 $\{\sigma_1,\sigma_2\}$, 거기 수직인 곡면의 **단위법선** $\xi=\dfrac{\sigma_3}{\sqrt2}$ ($\operatorname{tr}\xi^2=1$, $\langle\xi,\sigma_1\rangle=\langle\xi,\sigma_2\rangle=0$).
**제2기본형식** ($L=\langle P_{xx},\xi\rangle$ 등):
$$
L=\operatorname{tr}\!\Big(-2\sigma_3\cdot\tfrac{\sigma_3}{\sqrt2}\Big)=-\tfrac2{\sqrt2}\operatorname{tr}(\sigma_3^2)=-2\sqrt2,\qquad M=0,\qquad N=-2\sqrt2.
$$
**곡률** (Part1의 $K=\dfrac{LN-M^2}{EG-F^2}$):
$$
K=\frac{(-2\sqrt2)(-2\sqrt2)-0}{2\cdot2-0}=\frac84=\boxed{2}.
$$
곡률이 **제1·제2기본형식 직접 계산**에서 나왔다 — Part1이 구면 법선으로 한 그 손 그대로. (SU(2) 등질성 §2.2로 모든 점에서 $K=2$; sympy: $P_x{=}\sigma_1,P_y{=}\sigma_2$, $E{=}G{=}2,F{=}0$, $P_{xx}{=}P_{yy}{=}-2\sigma_3$, $L{=}N{=}-2\sqrt2,M{=}0$, $K{=}2$.)

### 1.2 확인: 내재 공식으로도 (Part1이 유도한 공식 = 문서 `0·1` 다리)
그 근본에서 Part1이 뽑은 내재 공식 $K=-\tfrac1{2\lambda}\Delta\log\lambda$ 에 사영자 계량 $\lambda=2/S^2$ 를 넣어 교차확인한다. $\log\lambda=\log2-2\log S$, 문서 `2` §3.4의 $\Delta\log S=4/S^2$:
$$
\Delta\log\lambda=-\frac8{S^2},\qquad K=-\frac{S^2}4\Big(-\frac8{S^2}\Big)=2.
$$
§1.1의 근본 계산과 같은 값(둥근 $\lambda=4/S^2$ 면 $K=1$). 이 내재 공식이 문서 `0·1` 로 잇는 다리 — *시작이 아니라 확인.*

---

## 2. CPⁿ ($n\ge2$): Gauss 방정식 (평평한 공간 속 부분다양체)

$n\ge2$ 는 곡면이 아니라 실 $2n$-차원이라 문서 `0`의 곡면 공식이 그대로는 안 통한다. 대신 **평평한 $\mathrm{Herm}$ 속 부분다양체의 단면곡률**을 제2기본형식으로 잰다 — 도구를 먼저 유도한다.

### 2.1 Gauss 방정식 — 항별로 유도 (문서 `0` shape operator의 일반판)
주변 $\mathrm{Herm}$ 이 평평 → 방향미분 $D$ 의 곡률 $0$: 임의 장에 $D_XD_YZ-D_YD_XZ-D_{[X,Y]}Z=0$. 접벡터장 $X,Y$ 에 $D_XY$ 를 접·법으로 가른다(이게 곡면 접속 $\nabla$ 와 제2기본형식 $\mathrm{II}$ 의 정의):
$$
D_XY=\nabla_XY+\mathrm{II}(X,Y),\qquad \nabla_XY\ (\text{접}),\ \mathrm{II}(X,Y)\ (\text{법}).
$$
**보조(Weingarten).** 법 $\xi$·접 $Z$ 는 $\langle\xi,Z\rangle=0$; $X$ 로 미분하면 $\langle D_X\xi,Z\rangle+\langle\xi,D_XZ\rangle=0$, 그런데 $\langle\xi,D_XZ\rangle=\langle\xi,\mathrm{II}(X,Z)\rangle$ ($D_XZ$ 의 법선부만 $\xi$ 와 짝) 이므로
$$
\langle(D_X\xi)^{\text{접}},Z\rangle=-\langle\xi,\mathrm{II}(X,Z)\rangle.\tag{W}
$$
이제 평평함 식을 $Z=Y$, $\langle\cdot,X\rangle$ 로 항별로. $D_YY=\nabla_YY+\mathrm{II}(Y,Y)$ 를 다시 $D_X$:
$$
D_X(D_YY)=\underbrace{\nabla_X\nabla_YY+\mathrm{II}(X,\nabla_YY)}_{D_X(\nabla_YY)}+\ D_X\big(\mathrm{II}(Y,Y)\big).
$$
$\langle\cdot,X\rangle$ 을 잡으면 — $\mathrm{II}(X,\nabla_YY)$ 는 법선이라 접 $X$ 와 직교($0$); $\mathrm{II}(Y,Y)$ 는 법선 $\xi$ 라 (W)로 $\langle D_X\mathrm{II}(Y,Y),X\rangle=-\langle\mathrm{II}(Y,Y),\mathrm{II}(X,X)\rangle$:
$$
\langle D_XD_YY,X\rangle=\langle\nabla_X\nabla_YY,X\rangle-\langle\mathrm{II}(X,X),\mathrm{II}(Y,Y)\rangle.
$$
똑같이 ($\xi=\mathrm{II}(X,Y)$), 그리고 $D_{[X,Y]}Y$ 의 법선부는 $X$ 와 직교:
$$
\langle D_YD_XY,X\rangle=\langle\nabla_Y\nabla_XY,X\rangle-\langle\mathrm{II}(X,Y),\mathrm{II}(X,Y)\rangle,\qquad
\langle D_{[X,Y]}Y,X\rangle=\langle\nabla_{[X,Y]}Y,X\rangle.
$$
셋을 평평함 $\langle D_XD_YY-D_YD_XY-D_{[X,Y]}Y,X\rangle=0$ 에 넣으면 $\nabla$-항이 곡률 정의 $\langle R(X,Y)Y,X\rangle=\langle\nabla_X\nabla_YY-\nabla_Y\nabla_XY-\nabla_{[X,Y]}Y,X\rangle$ 로 모여
$$
\boxed{\ \langle R(X,Y)Y,X\rangle=\langle\mathrm{II}(X,X),\mathrm{II}(Y,Y)\rangle-\langle\mathrm{II}(X,Y),\mathrm{II}(X,Y)\rangle\ }.
$$
정규직교 $X,Y$ 면 좌변 = 그 2-평면 **단면곡률 $K$**. (여차원 1이면 $\mathrm{II}$ 가 스칼라 $L,M,N$ → $LN-M^2$, 문서 `0`.)

### 2.2 한 점이면 충분 (등질성)
$U\in SU(n{+}1)$ 는 $P\mapsto UPU^{-1}$, $\operatorname{tr}((U\,dP\,U^{-1})^2)=\operatorname{tr}(dP^2)$ 라 **등거리**. 추이적($[v]\to[e_0]$)이라 **한 점 $z=0$ ($P_0=E_{00}$) 에서 재면 끝** — 그것도 한 방향이 아니라 임의 방향을 한 번에.

### 2.3 제2기본형식 at $z=0$ — 실제로 미분해서
$P_{IJ}=v_I\bar v_J/N$ ($v_0=1,\ v_k=z_k$, $N=1+\sum z_k\bar z_k$, $\tfrac1N=1-\sum z_k\bar z_k+\cdots$). $z=0$ 에서 곱미분($N|_0=1$, $\partial(1/N)|_0=0$):
- **1계.** $\partial_{z_a}v_I|_0=\delta_{Ia}$ 라 분자에서 $\partial_{z_a}(v_I\bar v_J)|_0=\delta_{Ia}\delta_{J0}$ 만 살아 $\partial_{z_a}P|_0=E_{a0}$ (마찬가지 $\partial_{\bar z_b}P|_0=E_{0b}$). — 문서 `2`의 $B=\partial_z P$.
- **2계 혼합.** 분자 $\partial_{z_a}\partial_{\bar z_b}(v_I\bar v_J)|_0=\delta_{Ia}\delta_{Jb}$ → $E_{ab}$; 그리고 $\partial_{z_a}\partial_{\bar z_b}(1/N)|_0=-\delta_{ab}$ → $(0,0)$ 에 $-\delta_{ab}$ (교차항은 $\partial(1/N)|_0=0$ 이라 죽음):
$$
\partial_{z_a}\partial_{\bar z_b}P|_0=E_{ab}-\delta_{ab}E_{00}.
$$
- **2계 정칙–정칙.** $\partial_{z_a}\partial_{z_b}P|_0=0$ (분자에 $\bar v$ 미분이 없고 $1/N$ 도 $z$ 만으론 0); 반정칙도 $0$ — **혼합만 산다**(문서 `2` §3.3의 정칙 null과 같은 구조).

확인($n=1$): $P_{11}=z\bar z/N$, $\partial_z\partial_{\bar z}(z\bar z)=1$; $P_{00}=1/N$, $\partial_z\partial_{\bar z}(1/N)|_0=-1$ → $\partial_z\partial_{\bar z}P|_0=E_{11}-E_{00}$. ✓

임의 정칙방향 $u\in\mathbb C^n$ 의 실접벡터와 그 길이:
$$
X_u:=\sum_a(u_a E_{a0}+\bar u_a E_{0a}),\qquad \langle X_u,X_u\rangle=\operatorname{tr}(X_u^2)=2|u|^2.
$$
제2기본형식(2계 미분의 법선부, 혼합항만 살아):
$$
\mathrm{II}(X_u,X_u)=2\big(U-|u|^2E_{00}\big),\quad U_{ij}:=\bar u_i u_j\ (\text{랭크 1});\qquad \mathrm{II}(X_u,X_{iu})=0.
$$
($\mathrm{II}(X_u,X_{iu})=0$ 은 $+i$·$-i$ 항이 정확히 상쇄 — 임베딩이 정칙이라는 정체. 이 $\mathrm{II}$ 가 문서 `2` $B=\partial_z P$ 를 한 번 더 미분한 것.)

### 2.4 임의 정칙방향의 곡률 $=2$ (예시로)
$U^2=|u|^2U$ 이므로 $|\mathrm{II}(X_u,X_u)|^2=\operatorname{tr}[4(U-|u|^2E_{00})^2]=4(|u|^4+|u|^4)=8|u|^4$. Gauss($X=X_u$, $Y=X_{iu}$, $\langle X_u,X_u\rangle=\langle X_{iu},X_{iu}\rangle=2|u|^2$, $\langle X_u,X_{iu}\rangle=0$):
$$
K=\frac{\langle\mathrm{II}(X_u,X_u),\mathrm{II}(X_{iu},X_{iu})\rangle-|\mathrm{II}(X_u,X_{iu})|^2}{|X_u|^2|X_{iu}|^2}=\frac{8|u|^4-0}{(2|u|^2)^2}=\boxed{2}.
$$
- **예시** $u=(1,0)$: $U=E_{11}$, $\mathrm{II}(X_u,X_u)=2(E_{11}-E_{00})=\operatorname{diag}(-2,2,0)$, $|\mathrm{II}|^2=\operatorname{tr}\operatorname{diag}(4,4,0)=8$, $K=8/4=2$.
- **예시(다른 방향)** $u=\tfrac1{\sqrt2}(1,1)$: $|u|^2=1$, $U=\tfrac12\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$ (하부블록), $|\mathrm{II}|^2=8$, $K=2$ — **방향 무관.** *(sympy·수치 Gauss: 정칙평면 $K=2$.)*

---

## 3. 드릴 — "전방향 상수"의 정체 (정칙은 $2$, 실평면은 $[\tfrac12,2]$)

"곡률이 어느 방향이든 일정"이 얼마나 센 조건인지 끝까지 판다. **정칙평면**(위)은 모두 $2$. **임의의 실 2-평면**은?

**완전실평면.** $u=(1,0)$, $w=(0,1)$ ($w\ne Ju$, 둘 다 "실방향"). 실제 행렬:
$$
\mathrm{II}(X_u,X_u)=\operatorname{diag}(-2,2,0),\quad \mathrm{II}(X_w,X_w)=\operatorname{diag}(-2,0,2),\quad \mathrm{II}(X_u,X_w)=E_{12}+E_{21}.
$$
Gauss: $\langle\mathrm{II}(X_u,X_u),\mathrm{II}(X_w,X_w)\rangle=\operatorname{tr}\operatorname{diag}(4,0,0)=4$, $|\mathrm{II}(X_u,X_w)|^2=\operatorname{tr}(E_{12}{+}E_{21})^2=2$, 분모 $2\cdot2-0=4$:
$$
K=\frac{4-2}{4}=\frac12.
$$
**보간.** $X_u$ 고정, $W_t=\cos t\,X_w+\sin t\,X_{iu}$ ($Ju$ 와 실⟂ 사이 회전)면
$$
\boxed{\ K(t)=2-\tfrac32\cos^2 t\ \in\ \big[\tfrac12,\ 2\big]\ }
$$
$\cos t=0$(정칙평면)에서 최대 $2$, $\cos t=\pm1$(완전실)에서 최소 $\tfrac12$. *(sympy·수치 Gauss at $z=0$: 정칙 $K{=}2$, 실 $K{=}\tfrac12$.)*

> **드릴 결론.** 실 단면곡률은 상수가 *아니다* — $[\tfrac12,2]$ 로 변한다. **오직 정칙평면에서만** 모두 $2$. 그러니 "전방향 곡률 일정"의 정확한 정체는 **상수 정칙단면곡률** $H\equiv2$ — 실곡률을 상수로 강요하면 $\tfrac12=2$ 모순(평탄뿐)이라, CPⁿ은 그 사이에서 정칙방향만 못 박는다. (CP¹은 실 2차원이라 모든 평면이 정칙평면 = 한 수로 겹쳐 $K=2$.)

---

## 4. 왜 Fubini–Study

문서 `1`에서 CP¹의 "상수 곡률"이 둥근 계량을 등거리 빼고 유일하게 못 박았다(CP¹의 FS). $n\ge2$ 에서 실단면은 갈라지지만(§3), **살아남아 계량을 못 박는 쪽**이 상수 정칙단면곡률 $H\equiv2$ — §2.4에서 모든 정칙방향에 대해 직접 확인한 그것. 구성한 계량이 정확히 이걸 가지므로 FS다. 트레이스로 $\operatorname{Ric}=(n{+}1)g$(켈러–아인슈타인): $R_{i\bar j}=-\partial_i\partial_{\bar j}\log\det g=(n{+}1)g_{i\bar j}$.

---

## 5. (덧) conic 거울 — 한 줄
$\rho_{\mathbb{CP}^1}=-\partial\bar\partial\log\det g=2\,\partial\bar\partial\log S$, conic $\nu_2(z)=[1:\sqrt2 z:z^2]$ 는 $\|\nu_2\|^2=(1+|z|^2)^2=S^2$ 라 $\nu_2^*\omega_{\mathbb{CP}^2}=2\,\partial\bar\partial\log S$ — 같은 form: $\rho_{\mathbb{CP}^1}=\nu_2^*\omega_{\mathbb{CP}^2}$.

---

## 부록 A — 검산

**A1 (곡률 공식).** $\lambda=2/S^2$: $\log\lambda=\log2-2\log S$; $\Delta\log S=4\partial_z\partial_{\bar z}\log S=4/S^2$ (문서 `2` §3.4); $\Delta\log\lambda=-8/S^2$; $K=-\tfrac{S^2}4(-\tfrac8{S^2})=2$. ✔

**A2 (2계 미분 at 0).** $P_{ba}=z_b\bar z_a/N\Rightarrow\partial_{z_a}\partial_{\bar z_b}$ 가 $(b,a)$ 에 $1$; $P_{00}=1-\sum z\bar z\Rightarrow(0,0)$ 에 $-\delta_{ab}$. 곧 $\partial_{z_a}\partial_{\bar z_b}P|_0=E_{ba}-\delta_{ab}E_{00}$. ✔

**A3 (정칙 $K=2$).** $U^2=|u|^2U$; $|\mathrm{II}(X_u,X_u)|^2=4\operatorname{tr}(U^2-2|u|^2UE_{00}+|u|^4E_{00})=4(|u|^4-0+|u|^4)=8|u|^4$; $K=8|u|^4/(2|u|^2)^2=2$. 수치 Gauss(CP², $z=0$): $g=2I$, 정칙평면 $K=2$. ✔

**A4 (실평면 $K=\tfrac12$, 보간).** $\mathrm{II}(X_u,X_u)=\operatorname{diag}(-2,2,0)$, $\mathrm{II}(X_w,X_w)=\operatorname{diag}(-2,0,2)$, $\mathrm{II}(X_u,X_w)=E_{12}{+}E_{21}$; $K=(4-2)/4=\tfrac12$. $K(t)=2-\tfrac32\cos^2t$. 수치 Gauss: 실평면 $K=0.5$. ✔

---

## 결과 요약

| | 계산 | 결과 |
|---|---|---|
| §1.1 | $\lambda=2/S^2$ → 곡률 공식 | $K=2$ (둥근 $4/S^2$ 면 $1$) |
| §1.2 | 사영자 두 번 미분 (CP¹) | $\partial_z\partial_{\bar z}P|_0=E_{11}-E_{00}$ → $K=2$ |
| §2 | Gauss 방정식 + $\mathrm{II}$ (CPⁿ) | 임의 정칙방향 $K=2$ |
| §3 | 드릴 | 실평면 $K(t)=2-\tfrac32\cos^2t\in[\tfrac12,2]$ |
| §4 | 왜 FS | 상수 정칙단면곡률 $H\equiv2$, $\operatorname{Ric}=(n{+}1)g$ |

**한 문장.** 공 위 사영자 $P$ 를 문서 `2`가 한 번 미분해 계량을 지었고($B=\partial_z P$), 여기서 **한 번 더** 미분(제2기본형식)해 Gauss 방정식으로 곡률을 잰다 — 정칙방향은 모두 $K=2$(구면의 극단적 대칭이 CPⁿ으로 이어진 것), 실평면은 $[\tfrac12,2]$. 그 상수 정칙단면곡률이 FS를 못 박는다.

## 다음
- 문서 `4`: 이 곡률을 적분 → 넓이·Gauss–Bonnet ($\int K\,dA=2\pi\chi$).
