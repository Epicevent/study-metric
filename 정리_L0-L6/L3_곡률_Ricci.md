# L3 — 곡률: 등뼈에 $-\partial\bar\partial\log\det$ 한 번 더 $\big(\det g=S^{-2},\ \rho=2g,\ K=1\Leftrightarrow\mathrm{Ric}=g\big)$

> **이 층의 역할.** L2의 등뼈 $g_{z\bar z}=S^{-2}$에 곡률 자(L0의 $K=\rho/g$ 형태)를 갖다 댄다. 곡면이라 $\det g$가 성분 하나뿐이어서 모든 것이 한 줄로 떨어진다. 그리고 이 층이 골격의 **유일한 함정** — "$K=1$인데 왜 $\mathrm{Ric}=2g$?" — 이 사는 곳이다. 세 원본노트(Part3 §2, Lifting §7, projector §5)가 입을 모아 경고하는 그 함정을, 어느 $g$로 재느냐로 완전히 해소한다.

학습용이라 작은 계단으로 쪼개고, 검산은 부록에. **모든 상수는 독립 계산으로 검증되었다.**

---

## 0. 표기와 규약

- $S=1+s$. 포텐셜 계수 $h:=g_{z\bar z}=\partial\bar\partial\log S=1/S^2$ (L2 등뼈).
- Ricci 형식 계수 $\rho_{z\bar z}:=-\partial_z\partial_{\bar z}\log\det g$. Kähler 형식 $\omega\leftrightarrow g$, Ricci 형식 $\rho\leftrightarrow\rho_{z\bar z}$.
- 곡면 항등식: $\mathrm{Ric}=K\,g$, $\rho=K\,\omega$ (실 2차원은 곡률 성분 하나).

---

## 1. Block 1 — $\det g$ (1차원이라 성분 하나)

- **(a)** CP¹은 복소 1차원 ⟹ 계량행렬 $g_{i\bar j}$가 $1\times1$ ⟹
$$
\boxed{\ \det g=g_{z\bar z}=h=\frac{1}{S^2}=S^{-2}\ }.
$$
- **(b)** 이 "성분 하나"가 Part1에서 세 곡률(단면·Gauss·정칙단면)이 겹쳐 보인 이유이자, 일반화에서 $\det$이 등장하는 자리다(L4). *(Part3 §2.1)*

---

## 2. Block 2 — Ricci 형식: $\rho=2g$

### 연습 2.1 — $-\partial\bar\partial\log\det g$

- **(a)** $\det g=S^{-2}$를 넣으면
$$
\rho_{z\bar z}=-\partial_z\partial_{\bar z}\log\det g=-\partial\bar\partial\log S^{-2}=2\,\partial\bar\partial\log S.
$$
- **(b)** L2의 $\partial\bar\partial\log S=1/S^2=h$ 이므로
$$
\boxed{\ \rho_{z\bar z}=\frac{2}{S^2}=2h=2\,g_{z\bar z}^{\text{(pot)}}\ }.
$$
- **(c)** 즉 **Ricci 형식이 계량(Kähler 형식)에 상수배로 비례** — Kähler–Einstein. *(Part3 §2.2)*

### 연습 2.2 — 좌표독립 정체: $\mathrm{Ric}=K\,g$

- **(a)** 실 2차원 Riemann 텐서는 성분 하나: $R_{ijkl}=K(g_{ik}g_{jl}-g_{il}g_{jk})$. 축약 → $\mathrm{Ric}=K\,g$, $\rho=K\,\omega$.
- **(b)** 그러므로 "$\rho_{z\bar z}=(\text{상수})\cdot g_{z\bar z}$"는 곧 **상수 Gauss 곡률**이고, Part1의 $K=1$과 동치:
$$
\boxed{\ K=1\ \Longleftrightarrow\ \mathrm{Ric}=1\cdot g\ \Longleftrightarrow\ \rho=\omega\ },\qquad K\,dA=dA.
$$
*(Part3 §2.3)*

### 연습 2.3 — Liouville과 같은 식 (L1·L2와 닫힘)

- **(a)** KE 텐서식 $\rho_{z\bar z}=c\,g_{z\bar z}$를 사용자 좌표($g_{z\bar z}=\lambda/2$)로: $\rho_{z\bar z}=-\partial\bar\partial\log(\lambda/2)=-\tfrac14\Delta\log\lambda$.
- **(b)** $=c\cdot\lambda/2$로 두면 $\Delta\log\lambda=-2c\lambda$. Part2의 Liouville $\Delta\log\lambda=-2\lambda$와 비교 → $c=1$, $K=c=1$. **KE 방정식이 $n=1$에서 정확히 Liouville.** *(Part3 §2.4)*

---

## 3. ⚠ 주의 박스 — "$2$냐 $1$냐" (이 층의, 그리고 골격 전체의 유일한 함정)

같은 계산에서 $2$와 $1$이 둘 다 나오는데 모순이 아니다. **무엇을 무엇으로 재느냐**의 문제다.

- **Ricci 형식 계수는 척도 불변.** $\rho_{z\bar z}=-\partial\bar\partial\log g_{z\bar z}=\dfrac{2}{S^2}$는 어떤 정규화든 **같은 수**다(상수배 $g\mapsto c_0 g$는 $\partial\bar\partial\log$에서 소멸).
- **"$\mathrm{Ric}=c\,g$"의 $c$는 어느 $g$로 재느냐에 의존:**
  - 포텐셜 계수 $h=1/S^2$로 재면 $c=\rho_{z\bar z}/h=2=(n{+}1)$.
  - 사용자 Hermitian $g_{z\bar z}=\lambda/2=2h$로 재면 $c=\rho_{z\bar z}/(2h)=1=K$.
- **불변량은 $K=\rho/\omega$**(Gauss 곡률). 숫자 "$n+1=2$"는 *Ricci 형식 대 포텐셜 계량의 비율*이지 Gauss 곡률이 아니다.
- **함정:** "$\mathrm{Ric}=2g$"와 "$K=1$"을 **어느 $g$인지 안 밝히고** 나란히 쓰는 것. 늘 $K=\rho/\omega$(불변)와 $c$(척도 의존)를 구분하라.

| 무엇을 재나 | 분모 $g$ | $c=\rho_{z\bar z}/g$ | 의미 |
|---|---|---|---|
| 포텐셜 | $h=1/S^2$ | $2=n+1$ | Ricci/포텐셜 비율 (L4로 올라가는 수) |
| 사용자 Hermitian | $2h=2/S^2$ | $1=K$ | Gauss 곡률 (둥근 정규화) |

---

## 4. Block 4 — 곡률 2-형식과 적분 예고 (L5로)

- **(a)** $\rho=K\omega$, $K\,dA=dA$ (위 §2.2). 그래서 곡률 적분이 면적 적분이 된다(둥근 정규화): $\int K\,dA=\int dA=4\pi$.
- **(b)** 코호몰로지 진술 $[\tfrac{i}{2\pi}\rho]=c_1$로 올리면 "$\mathrm{Ric}=(n+1)\omega$"는 $c_1(\mathbb{CP}^n)=(n+1)H$의 그림자(L5·L6). 숫자 $n+1$은 정규화 무관(차수라서). *(projector §6)*

---

## 부록 A. 한 줄 한 줄 (검산용)

**A1** $\det g=g_{z\bar z}$ (1×1) $=1/S^2$. ✔

**A2.1** $\rho_{z\bar z}=-\partial\bar\partial\log S^{-2}=+2\partial\bar\partial\log S=2/S^2=2h$. ✔

**A2.3** $g_{z\bar z}=\lambda/2$, $\rho_{z\bar z}=-\tfrac14\Delta\log\lambda$; $=c\lambda/2\Rightarrow\Delta\log\lambda=-2c\lambda$; Part2 $c=1$, $K=1$. ✔

**A3 (두 정규화의 $K$ — 손으로).** L1 부록 B1에서 $\lambda=c/(1+s)^2$면 $K=4/c$ (한 줄: $\Delta\log\lambda=-8/(1+s)^2$, $K=-\tfrac1{2\lambda}\Delta\log\lambda=4/c$). 따라서
$$
\lambda=2g_{z\bar z}=\frac{2}{S^2}\ (c=2)\Rightarrow K=2;\qquad
\lambda=\frac{4}{S^2}\ (c=4)\Rightarrow K=1.
$$
**$\rho_{z\bar z}$의 척도불변 (손으로).** 계량을 $g\mapsto c_0 g$ 하면 $\log\det(c_0 g)=\log c_0^{\,1}+\log\det g$ (1성분), 상수 $\log c_0$는 $\partial\bar\partial$에서 소멸 ⟹ $\rho_{z\bar z}=-\partial\bar\partial\log\det g=\dfrac{2}{S^2}$는 $c_0$에 무관. 그래서 같은 $\rho_{z\bar z}$를 분모 $h=1/S^2$로 재면 $c=2$, $2h$로 재면 $c=1$ — §3 함정의 손계산판. ✔

**A4 (코드 교차검증, `verify3.py`)**
```
Backbone Kahler metric lambda = 2*g_zz = 2/(1+s)^2 ; K = 2
K(sphere 4/(1+s)^2) = 1
```
손(A3)과 일치. ✔

---

## 결과 요약

| 블록 | 한 일 | 결과 |
|---|---|---|
| B1 | $\det g$ (1성분) | $\det g=S^{-2}$ |
| B2 | $-\partial\bar\partial\log\det g$ | $\rho=2g^{\text{(pot)}}$; $K=1\Leftrightarrow\mathrm{Ric}=g\Leftrightarrow\rho=\omega$ |
| B3 (함정) | 어느 $g$로 재나 | 포텐셜 기준 $c=2=n{+}1$, Hermitian 기준 $c=1=K$ |
| B4 | 곡률 2-형식 | $K\,dA=dA$, $[\tfrac{i}{2\pi}\rho]=c_1$ → L5 |

**한 문장.** 등뼈 $\det g=S^{-2}$에 $-\partial\bar\partial\log$을 한 번 더 돌리면 $\rho=2\partial\bar\partial\log S=2g$가 떨어지고, 이는 곡면 항등식 $\mathrm{Ric}=K g$로 읽으면 "$K=1\Leftrightarrow\mathrm{Ric}=g$"다 — "$2$냐 $1$이냐"는 척도불변인 $\rho_{z\bar z}=2/S^2$를 포텐셜($c{=}2$)로 재느냐 Hermitian($c{=}1$)으로 재느냐의 차이일 뿐, 불변량은 $K=\rho/\omega$다.

*출처: cp1_constant_ricci_kahler_einstein_observation_part3_note.md(§2), cp1_laplacian_curvature_lifting_note.md(§7), fs_via_projector_conic_pullback_path_note.md(§5–6).*
