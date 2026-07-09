# 4 — Gauss–Bonnet: 먼저 "같은 집합"임을 못 박고, 그 위에서 적분한다

> **흐름.** 문서 `3`의 두 계량(라운드 $K=1$, 사영자 $K=2$)이 *둘 다* $\int K\,dA=2\pi\chi$ 라 하려면, **먼저 둘이 같은 집합 위에 있어야** 한다. 라운드는 $\mathbb R^3$ 단위구 $S^2$, 사영자는 $\mathrm{Herm}$ 의 $\mathbb{CP}^1$ — a priori **다른 집합**이다. 이 둘이 같은 집합임을 전단사로 못 박은 뒤(§2), 그 한 집합 $M$ 위에서 정직히 적분(§3)하고 Gauss–Bonnet(§4)으로 닫는다. (같은 집합이라 *가정*하고 넘어가면 그게 마법이다.)
>
> **퀄리티 = 손노트.** 전단사 증명, 적분 실제로, 검산.

---

## 1. 세팅과 질문

두 계량이 사는 곳이 다르다:
- **라운드** (문서 `0·1`): $\mathbb R^3$ 단위구 $S^2=\{\vec n\in\mathbb R^3:|\vec n|=1\}$ 위, $ds^2=|d\vec n|^2$.
- **사영자** (문서 `2`): $\mathrm{Herm}(2)$ 속 $\mathbb{CP}^1=\{$랭크1 사영자 $P:P^2=P=P^*,\operatorname{tr}P=1\}$ 위, $ds^2=\operatorname{tr}(dP\,dP)$.

$\int K\,dA$ 를 둘에 대해 같은 위상량이라 하기 전에, **$S^2$ 와 $\mathbb{CP}^1$ 이 같은 집합인가**를 먼저 답해야 한다.

---

## 2. 라운드 $=$ 사영자 $=$ 한 집합 $M$ (Bloch 전단사, 증명)

$S^2$ 와 $\mathbb{CP}^1$ 사이에 서로 역인 두 사상을 세운다.

**$\Phi:S^2\to\mathbb{CP}^1$**, $\vec n\mapsto P:=\tfrac12(I+\vec n\cdot\vec\sigma)$. 잘 정의됨:
$$
\operatorname{tr}P=\tfrac12(2+0)=1,\qquad \det P=\tfrac14\det(I+\vec n\cdot\vec\sigma)=\tfrac14(1-|\vec n|^2)\overset{|\vec n|=1}{=}0,
$$
$\operatorname{tr}=1,\det=0$ → 고윳값 $\{1,0\}$ → $P^2=P$, 랭크1 사영자. ($P^2-P=\tfrac14(|\vec n|^2-1)I=0$ 도 직접.)

**$\Psi:\mathbb{CP}^1\to S^2$**, $P\mapsto\vec n:=(\operatorname{tr}(P\sigma_1),\operatorname{tr}(P\sigma_2),\operatorname{tr}(P\sigma_3))$. 잘 정의됨: 랭크1 사영자는 $\operatorname{tr}(P^2)=1$ 인데, $\operatorname{tr}(P^2)=\tfrac12(1+|\vec n|^2)$ (문서 `2` 밀도행렬) $\Rightarrow|\vec n|=1$, $\vec n\in S^2$.

**서로 역:** $\Psi\Phi=\mathrm{id}$ — $\operatorname{tr}\big(\tfrac12(I+\vec n\cdot\vec\sigma)\sigma_a\big)=\tfrac12\operatorname{tr}\sigma_a+\tfrac12\sum_b n_b\operatorname{tr}(\sigma_b\sigma_a)=n_a$. $\Phi\Psi=\mathrm{id}$ — $2\times2$ 에르미트는 $\tfrac12(\operatorname{tr}(\cdot)I+\sum_a\operatorname{tr}(\cdot\,\sigma_a)\sigma_a)$ 로 유일하게 복원되고 $\operatorname{tr}P=1$ 이라 $P=\tfrac12(I+\vec n\cdot\vec\sigma)$. 둘 다 매끄러움.

$$
\boxed{\ S^2\ \cong\ \mathbb{CP}^1\ (\text{미분동형})\ =:\ M\ }
$$

**그러니 라운드와 사영자는 다른 두 집합이 아니라, 한 집합 $M$ 위의 두 계량**이다. 같은 점에서 값만 다르다:
$$
\text{라운드}\ |d\vec n|^2,\qquad \text{사영자}\ \operatorname{tr}(dP\,dP)=\tfrac12|d\vec n|^2\ (\text{문서 `2`, } dP=\tfrac12 d\vec n\cdot\vec\sigma).
$$
*(sympy: $\operatorname{tr}P=1$, $\det P=\tfrac14(1-|\vec n|^2)$, $P^2=P\Leftrightarrow|\vec n|=1$, $\operatorname{tr}(P\sigma_a)=n_a$.)*

---

## 3. 그 한 집합 $M$ 위에서 정직히 적분

$M=\mathbb{CP}^1$ 을 아핀 차트로 편다: $[v]=[1:z]$, $z\in\mathbb C$ (남은 한 점 $[0:1]$ 은 $z=\infty$; §2의 $\vec n$ 으로는 남극). 계량은 $\lambda|dz|^2$, $\lambda=c/S^2$ ($S=1+|z|^2$; 라운드 $c=4$, 사영자 $c=2$ — 문서 `2·3`). 넓이는 한 번만 정직히(치환 $u=1+r^2$):
$$
\operatorname{Area}=\int_0^{2\pi}\!\!\int_0^\infty\frac{c}{(1+r^2)^2}\,r\,dr\,d\phi=2\pi\cdot c\cdot\tfrac12=c\pi\quad(\text{라운드 }4\pi,\ \text{사영자 }2\pi).
$$
$K$ 는 상수(문서 `3`: 라운드 $1$, 사영자 $2$)라
$$
\int_M K\,dA=K\cdot\operatorname{Area}:\qquad \text{라운드}\ 1\cdot4\pi=4\pi,\quad \text{사영자}\ 2\cdot2\pi=4\pi.
$$
같은 집합 $M$ 위의 두 계량이 — $K$ 는 $1$ vs $2$, 넓이는 $4\pi$ vs $2\pi$ 로 달라도 — 둘 다 $\int_M K\,dA=4\pi$.

---

## 4. $\int_M K\,dA$ 는 계량에 무관하다 — 등각 변화로 증명

§3은 두 계량이 $4\pi$ 로 *같음*을 봤다. 왜 같은가 — 우연이 아니라 $\int_M K\,dA$ 가 $M$ 위 계량에 **무관**하기 때문임을 증명한다(이게 Gauss–Bonnet의 심장).

$M$ 위 두 계량이 등각 관계 $\tilde g=e^{2u}g$ (라운드·사영자는 $e^{2u}=\tfrac12$, $u$ 상수; 일반 $u(z)$ 도). 등온좌표 $g=\lambda|dz|^2$, $\tilde g=\tilde\lambda|dz|^2$ ($\tilde\lambda=e^{2u}\lambda$). 문서 `0`의 $K=-\tfrac1{2\lambda}\Delta_0\log\lambda$ ($\Delta_0$ 평면 라플라시안)에 넣으면
$$
\tilde K=-\frac1{2\tilde\lambda}\Delta_0\log\tilde\lambda
=e^{-2u}\Big(-\frac1{2\lambda}\Delta_0\log\lambda-\frac1\lambda\Delta_0 u\Big)
=e^{-2u}\big(K-\Delta_g u\big),\qquad \Delta_g u:=\tfrac1\lambda\Delta_0 u.
$$
넓이 $d\tilde A=\tilde\lambda\,dx\,dy=e^{2u}dA_g$ 이므로 곡률 2-form이
$$
\tilde K\,d\tilde A=(K-\Delta_g u)\,dA_g.
$$
그런데 **닫힌 $M$ 에는 경계가 없어** $\displaystyle\int_M\Delta_g u\,dA_g=0$ (발산정리, 경계항 없음; 좌표로도 $\int_{\mathbb C}\Delta_0 u\,dx\,dy=0$: $u$ 가 $M$ 위 매끄러워 빠진 점에서도 유량 0). 따라서
$$
\boxed{\ \int_M\tilde K\,d\tilde A=\int_M K\,dA-\underbrace{\int_M\Delta_g u\,dA_g}_{0}=\int_M K\,dA\ }.
$$
**$\int_M K\,dA$ 는 등각 변화에 불변** — 계량이 달라도 같다. 라운드↔사영자는 $u$ 상수라 $\Delta u=0$, 아예 $\tilde K\,d\tilde A=K\,dA$ 같은 2-form(그래서 둘 다 $4\pi$); 일반 등각 계량도 위 논증으로 같다. *(sympy: $\tilde K\,d\tilde A=(K-\Delta_g u)dA_g$ 확인.)*

$S^2$ 위 모든 매끄러운 계량은 등각류 하나(균일화)라, $\int_M K\,dA$ 는 $M$ 만의 수 = $2\pi\chi(M)$:
$$
\int_M K\,dA=4\pi=2\pi\chi(M)\quad(\chi(S^2)=2;\ \text{손계산은 문서 `5`}).
$$

---

## 부록 A — 검산

**A1 (전단사).** $\det(I+\vec n\cdot\vec\sigma)=1-|\vec n|^2$; $P=\tfrac12(I+\vec n\cdot\vec\sigma)$ 는 $|\vec n|=1$ 에서 $P^2=P$, $\operatorname{tr}P=1$; $\operatorname{tr}(P\sigma_a)=n_a$ (왕복). → $S^2\cong\mathbb{CP}^1$. ✔(sympy)

**A2 (계량 관계).** $dP=\tfrac12 d\vec n\cdot\vec\sigma$, $\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}$ → $\operatorname{tr}(dP\,dP)=\tfrac12|d\vec n|^2$. ✔

**A3 (넓이).** $\int_0^\infty\frac{r\,dr}{(1+r^2)^2}=\tfrac12$ → $\operatorname{Area}=c\pi$; 라운드 $4\pi$, 사영자 $2\pi$. ✔(sympy)

**A4 ($\int K\,dA$).** $K$ 상수라 $K\cdot\operatorname{Area}$: $1\cdot4\pi=2\cdot2\pi=4\pi$. ✔

---

## 결과 요약

| 단계 | 한 일 | 결과 |
|---|---|---|
| §2 | $S^2\cong\mathbb{CP}^1$ (Bloch 전단사, 증명) | 한 집합 $M$, 두 계량 |
| §3 | $M$ 위 넓이·$\int K\,dA$ | 라운드 $(1,4\pi,4\pi)$, 사영자 $(2,2\pi,4\pi)$ |
| §4 | Gauss–Bonnet | $\int_M K\,dA=2\pi\chi(M)=4\pi$ |

**한 문장.** 라운드($\mathbb R^3$ 구)와 사영자($\mathrm{Herm}$ CP¹)는 a priori 다른 집합이지만 Bloch 전단사 $\vec n\leftrightarrow P=\tfrac12(I+\vec n\cdot\vec\sigma)$ 로 **한 곡면 $M$**(증명, §2)이고, 그 위의 두 계량은 $K$·넓이가 달라도 $\int_M K\,dA$ 가 $M$ 의 위상 불변량 $2\pi\chi=4\pi$ 라 둘 다 같다 — "같은 집합"을 먼저 못 박았기에 마법이 아니다.
