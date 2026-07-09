# L1 — CP¹의 등온인자 $\lambda$: 세 계산이 한 $\lambda$로

> **이 층의 역할.** L0의 자를 처음으로 갖다 대기 전에, **잴 대상인 $\lambda$를 짓는다.** 세 가지 독립적인 길 — (1) 구면 stereographic, (2) Liouville ODE, (3) 사영자 $\operatorname{tr}(dP\,dP)$ — 이 모두 같은 함수꼴 $\dfrac{c}{(1+s)^2}$을 내놓고, 상수 $c$만 규약(Bloch 인자 2)으로 갈린다. 이 일치가 **검증 우선순위 2순위**이며, 본 문서 끝에서 실제 계산으로 못 박는다.

학습용이라 작은 계단으로 쪼개고, 검산은 부록에. **모든 상수는 독립 계산으로 검증되었다.**

---

## 0. 표기와 규약

- $z=x+iy$, $s=|z|^2=r^2$, $S=1+s$. 등온좌표 $ds^2=\lambda|dz|^2=\lambda(dx^2+dy^2)$.
- $\sigma=\log\lambda$, 곡률 자 $K=-\tfrac{1}{2\lambda}\Delta\log\lambda$ (L0).
- 목표 함수꼴: $\lambda=\dfrac{c}{(1+s)^2}$. 아래 세 계산이 각각 $c=4$ 또는 $c=2$를 준다.

> **결론 먼저(2순위 검증의 요지).** 구면 stereographic과 Liouville은 $c=4$ ($K=1$), 사영자 $\operatorname{tr}(dP\,dP)$는 $c=2$ ($K=2$)를 준다. 셋은 **상수배 2**만 다른 같은 구면이다. $c$는 곡률 정규화 선택일 뿐 기하의 본질이 아니다(불변량은 $\int K\,dA=4\pi$, L5).

---

## 1. Block 1 — 구면 stereographic: $\lambda=\dfrac{4}{(1+s)^2}$ *(Part1 PDF)*

단위구 $S^2\subset\mathbb R^3$를 북극에서 평면으로 입체사영한다.

### 연습 1.1 — 사영과 위치벡터

- **(a)** 북극 $(0,0,1)$ 기준 사영의 역사상(평면 $z=x+iy\mapsto$ 구면점):
$$
P(x,y)=\frac{1}{1+s}\big(2x,\ 2y,\ s-1\big)\in S^2,\qquad s=x^2+y^2 .
$$
$\|P\|=1$ 임을 확인: $4x^2+4y^2+(s-1)^2=4s+s^2-2s+1=(s+1)^2$, 나누면 $1$. ✔
- **(b)** $P$는 그 점에서의 **단위 법벡터**이기도 하다(구면이라 위치=법선). 이 사실이 §3(곡률)에서 shape operator로 직결된다.

### 연습 1.2 — 당긴 계량

- **(a)** $dP$를 계산해 $ds^2=dP\cdot dP$를 잡으면(부록 A1) 모든 교차항이 약분되고
$$
\boxed{\ ds^2=\frac{4}{(1+s)^2}\,(dx^2+dy^2)=\frac{4}{(1+s)^2}|dz|^2\ }\ \Rightarrow\ \lambda_{\text{sph}}=\frac{4}{(1+s)^2}.
$$
- **(b)** L0 자로 곡률: $\Delta\log\lambda_{\text{sph}}=-8/(1+s)^2$(L0 부록 B), $K=-\tfrac1{2\lambda}\Delta\log\lambda=1$. **단위구라 $K=1$.** *(Part1: "the gauss curvature =1, $P(x,y)$ is the unit normal vector of the unit sphere".)*

---

## 2. Block 2 — Liouville ODE: $\lambda_a=\dfrac{4a}{(1+ar^2)^2}$ *(Part2)*

이번엔 **구를 주지 않고** "$K\equiv1$"만 부과해 같은 $\lambda$를 *역으로* 얻는다.

### 연습 2.1 — PDE와 ODE 환원

- **(a)** $K=1$을 자에 넣으면 $1=-\tfrac1{2\lambda}\Delta\log\lambda$, 즉 **Liouville 방정식**
$$
\Delta\sigma=-2e^{\sigma}\qquad(\sigma=\log\lambda).
$$
- **(b)** 회전대칭 $\sigma=\sigma(r)$ 가정, $\Delta g=\tfrac1r(rg')'$:
$$
\frac1r(r\sigma')'=-2e^{\sigma}.
$$

### 연습 2.2 — 자율형 + 에너지 적분 (적분상수까지)

- **(a)** $t=\log r$ ($r\tfrac{d}{dr}=\tfrac{d}{dt}$, 점$=d/dt$)로 두면 $\tfrac1r(r\sigma')'=e^{-2t}\ddot\sigma$, 식은 $\ddot\sigma=-2e^{\sigma+2t}$.
- **(b)** $\psi:=\sigma+2t=\log(\lambda r^2)$로 합치면 $\ddot\psi=-2e^{\psi}$ ($t$ 소거된 자율방정식).
- **(c)** $\dot\psi$를 곱해 적분: $\tfrac12\dot\psi^2=-2e^{\psi}+C$. **원점 정칙성**($r\to0$에서 $\lambda\to\lambda(0)$ 유한 ⟹ $\dot\psi\to2$, $e^\psi\to0$)으로 $C=2$. 따라서 $\dot\psi^2=4(1-e^{\psi})$.

### 연습 2.3 — 변수분리·복원

- **(a)** $w=\sqrt{1-e^{\psi}}$ 치환으로 $\displaystyle\int\frac{-2\,dw}{1-w^2}=2t+\text{c}$ → $w=\tanh(t-t_0)$.
- **(b)** $e^{\psi}=1-w^2=\operatorname{sech}^2(t-t_0)$. $\operatorname{sech}^2x=\dfrac{4e^{2x}}{(1+e^{2x})^2}$, $e^{2(t-t_0)}=ar^2$ ($a:=e^{-2t_0}$):
$$
e^{\psi}=\frac{4ar^2}{(1+ar^2)^2}\ \Rightarrow\ \boxed{\ \lambda_a=\frac{e^{\psi}}{r^2}=\frac{4a}{(1+ar^2)^2}\ }\quad(a>0).
$$
- **(c)** $a=1$이 Block 1의 $\lambda_{\text{sph}}=4/(1+r^2)^2$. 남은 자유도 $a$는 딜레이션 $z\mapsto\sqrt a\,z$ 대칭. *(Part2 §2)*

> **유일성(맥락).** Liouville 일반해는 $\lambda=\dfrac{4|f'(z)|^2}{(1+|f(z)|^2)^2}$ ($f$ 국소단사 정칙). CP¹ 전체로 완비·매끄럽게 확장되려면 $f\in PSL(2,\mathbb C)$(Möbius), 모두 서로 등거리. 따라서 $K\equiv1$ 완비계량은 **등거리 차이로 유일** = FS. *(Part2 §4, $S^2$ uniformization)*

---

## 3. Block 3 — 사영자 $\operatorname{tr}(dP\,dP)$: $\lambda=\dfrac{2}{(1+s)^2}$ *(projector note)*

평평한 행렬공간에서 conic 사상으로 당겨 짓는 길. 라플라시안을 한 번도 안 쓴다.

### 연습 3.1 — 차원 무관 닫힌형

- **(a)** $v\in\mathbb C^{n+1}$, $N=\|v\|^2$, 사영자 $P=vv^*/N$ ($P^2=P$, $\operatorname{tr}P=1$). 미분 $dP=\dfrac{dv\,v^*+v\,dv^*}{N}-\dfrac{vv^*}{N^2}dN$.
- **(b)** trace를 전개하면(부록 A3, cyclic + 스칼라 추출) 제곱항이 거짓말처럼 소거되어
$$
\boxed{\ ds^2=\operatorname{tr}(dP\,dP)=\frac{2\big[N\,(dv^*dv)-|v^*dv|^2\big]}{N^2}\ }\qquad(\text{차원 무관}).
$$

### 연습 3.2 — CP¹ 대입

- **(a)** $v=(1,z)$: $dv^*dv=|dz|^2$, $v^*dv=\bar z\,dz$, $|v^*dv|^2=|z|^2|dz|^2$, $N=S$.
- **(b)** 닫힌형에 넣고 $S-|z|^2=1$:
$$
ds^2=\frac{2(S-|z|^2)}{S^2}|dz|^2=\frac{2}{(1+s)^2}|dz|^2\ \Rightarrow\ \lambda_{\text{proj}}=\frac{2}{(1+s)^2}.
$$
- **(c)** L0 자로 곡률: $\Delta\log\lambda_{\text{proj}}=-8/(1+s)^2$(상수 $2$는 $\log$에서 $\lambda_{\text{sph}}$와 같은 미분), 그런데 분모 $\lambda$가 절반이라 $K=-\tfrac1{2\lambda_{\text{proj}}}\Delta\log\lambda_{\text{proj}}=2$. **사영자 계량은 $K=2$**(반지름 $1/\sqrt2$ 구).

### 연습 3.3 — Bloch 인자 2 (왜 절반인가)

- **(a)** $P=\tfrac12(I+\vec n\cdot\vec\sigma)$ (Bloch), $|\vec n|=1$. 그러면 $dP=\tfrac12 d\vec n\cdot\vec\sigma$, $\operatorname{tr}(dP\,dP)=\tfrac12|d\vec n|^2$.
- **(b)** 즉 단위 Bloch 구의 계량 $|d\vec n|^2=2\operatorname{tr}(dP\,dP)=\dfrac{4}{S^2}|dz|^2=\lambda_{\text{sph}}$. **사영자 계량은 단위구의 정확히 절반.** *(projector §3.2)*

---

## 4. ⚠ 주의 박스 — "$c=2$냐 $c=4$냐"는 규약, 기하 아님

- $\lambda_{\text{sph}}=4/S^2$ (단위구, $K=1$, 넓이 $4\pi$) 와 $\lambda_{\text{proj}}=2/S^2$ (사영자, $K=2$, 넓이 $2\pi$)는 **상수배 2**만 다르다.
- 상수배 $g\mapsto c_0 g$는 $K\mapsto K/c_0$, 넓이 $\mapsto c_0\cdot$넓이로 바꾸지만 **곱 $\int K\,dA$는 불변**(둘 다 $4\pi=2\pi\chi$, L5).
- FS 계량은 본래 스케일을 빼고 정의된다. 본 골격의 규약 $ds^2=2g_{z\bar z}|dz|^2$, $g_{z\bar z}=\partial\bar\partial\log S=1/S^2$는 $\lambda=2/S^2$ = **사영자 열**을 쓴다. 스펙의 "$K=1$" 진술은 $\lambda=4/S^2$ = **구면 열**. 다리는 $\lambda_{\text{sph}}=2\lambda_{\text{proj}}=4h$ ($h=1/S^2$).

---

## 부록 A. 한 줄 한 줄 (검산용)

**A1 (stereographic 계량)** $P=\tfrac{1}{1+s}(2x,2y,s-1)$. 각 성분 미분 후 $dP\cdot dP$를 모으면 분자 $4(dx^2+dy^2)$, 분모 $(1+s)^2$ — 표준 결과 $ds^2=\tfrac{4}{(1+s)^2}(dx^2+dy^2)$. (또는 $\partial\bar\partial$ 길: §L2.) ✔

**A2 (Liouville 검산, Part1 해 대입)** $\sigma=\log4-2\log(1+r^2)$: $\sigma'=\tfrac{-4r}{1+r^2}$, $r\sigma'=\tfrac{-4r^2}{1+r^2}$, $(r\sigma')'=\tfrac{-8r}{(1+r^2)^2}$, $\tfrac1r(r\sigma')'=\tfrac{-8}{(1+r^2)^2}=-2\cdot\tfrac{4}{(1+r^2)^2}=-2e^\sigma$. ✔

**A3 (tr(dP dP) 닫힌형)** $\operatorname{tr}((vv^*)^2)=N^2$, $\operatorname{tr}(A\,vv^*)=N\,dN$ ($A=dv\,v^*+v\,dv^*$), $\operatorname{tr}(A^2)=(v^*dv)^2+2N(dv^*dv)+(dv^*v)^2$. 조립: $\operatorname{tr}(dP\,dP)=\tfrac{\operatorname{tr}(A^2)-(dN)^2}{N^2}$. $(dN)^2$ 빼면 제곱항 소거 → $\tfrac{2[N\,dv^*dv-|v^*dv|^2]}{N^2}$. ✔

## 부록 B. 2순위 검증 — 손으로 완전 전개

코드 없이 따라갈 수 있게 한 칸씩. 재료는 **단 하나**: L0 부록 B의 $\Delta\log(1+ar^2)=\dfrac{4a}{(1+ar^2)^2}$ (아래 B0에서 재유도).

### B0 — 보조 라플라시안 (모든 줄이 재사용)
극좌표 $\Delta g=\tfrac1r(rg')'$. $f=\log(1+ar^2)$:
$$
f'=\frac{2ar}{1+ar^2},\quad rf'=\frac{2ar^2}{1+ar^2},\quad
(rf')'=\frac{4ar(1+ar^2)-2ar^2\cdot2ar}{(1+ar^2)^2}=\frac{4ar}{(1+ar^2)^2},
$$
$$
\Delta f=\frac1r(rf')'=\frac{4a}{(1+ar^2)^2}.
$$
($a=1$이면 $\Delta\log(1+s)=\dfrac{4}{(1+s)^2}$.)

### B1 — 일반 $\lambda=\dfrac{c}{(1+s)^2}$ 의 곡률은 $K=\dfrac{4}{c}$
$\sigma=\log\lambda=\log c-2\log(1+s)$. B0($a=1$)으로 $\Delta\sigma=-2\cdot\dfrac{4}{(1+s)^2}=-\dfrac{8}{(1+s)^2}$. 자에 대입:
$$
K=-\frac{1}{2\lambda}\Delta\sigma
=-\frac12\cdot\frac{(1+s)^2}{c}\cdot\Big(-\frac{8}{(1+s)^2}\Big)
=\frac{4}{c}.
$$
- $c=4$ (구면·Liouville): $K=1$.
- $c=2$ (사영자): $K=2$.
- **비율** $\dfrac{\lambda_{\text{sph}}}{\lambda_{\text{proj}}}=\dfrac{4}{2}=2$ = Bloch 인자. (곡률은 역으로 $K_{\text{sph}}/K_{\text{proj}}=1/2$.)

### B2 — Liouville $\lambda_a=\dfrac{4a}{(1+ar^2)^2}$ 가 $K\equiv1$ (모든 $a$)
$\sigma_a=\log(4a)-2\log(1+ar^2)$. B0으로 $\Delta\sigma_a=-2\cdot\dfrac{4a}{(1+ar^2)^2}=-\dfrac{8a}{(1+ar^2)^2}$. 그런데 우변은 정확히 $-2\lambda_a$:
$$
\Delta\sigma_a=-2\lambda_a\quad\Longrightarrow\quad \boxed{\Delta\log\lambda_a+2\lambda_a=0}\ (\text{Liouville}),
$$
$$
K=-\frac{1}{2\lambda_a}\Delta\sigma_a=-\frac{1}{2\lambda_a}(-2\lambda_a)=1\quad(\forall a).
$$
적분상수 $a$가 곡률에 안 들어옴 — 딜레이션 대칭이 $K=1$을 보존.

### B3 — 코드 교차검증 (`verify3.py`)
위 손계산을 기계로 재현:
```
K(sphere 4/(1+s)^2) = 1     # B1, c=4
K(proj   2/(1+s)^2) = 2     # B1, c=2
ratio sphere/proj   = 2     # Bloch 인자
K(Liouville lam_a)  = 1     # B2, a 무관
Delta log lam_a + 2*lam_a = 0   # B2
```
**결론:** 세 $\lambda$는 모두 $c/(1+s)^2$ 꼴이고 $K=4/c$. 구면·Liouville($c{=}4$)은 $K{=}1$, 사영자($c{=}2$)는 그 절반 스케일 $K{=}2$ — **같은 둥근 구면**, Bloch 인자 2 차이. 손과 기계 일치. ✔

---

## 결과 요약

| 길 | $\lambda$ | $K$ | 출처 | 특징 |
|---|---|---|---|---|
| 구면 stereographic | $4/(1+s)^2$ | $1$ | Part1 | 단위구, $P=$단위법선 |
| Liouville ODE | $4a/(1+ar^2)^2$ | $1$ | Part2 | $K\equiv1$만으로 역유도, $a$=딜레이션 |
| 사영자 $\operatorname{tr}(dP\,dP)$ | $2/(1+s)^2$ | $2$ | projector | 평탄→conic 당김, 라플라시안 0회 |

**한 문장.** CP¹의 등온인자는 세 독립적 길(구면 사영 / $K\equiv1$ Liouville / 평탄공간 사영자 당김)에서 같은 $c/(1+s)^2$ 꼴로 떨어지며, 구면·Liouville의 $c=4$($K{=}1$)와 사영자의 $c=2$($K{=}2$)는 Bloch 인자 2의 규약 차이일 뿐 — sympy로 비율 2와 $\int K\,dA$ 불변을 확인했다(2순위 검증 완료).

*출처: 원본노트/Part1.pdf, fubini_study_from_constant_curvature_part2_note.md, fs_via_projector_conic_pullback_path_note.md.*
