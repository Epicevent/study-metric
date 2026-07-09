# L4 — CPⁿ로의 확장 $\big(g_{i\bar j}=\tfrac{S\delta_{ij}-\bar z_i z_j}{S^2},\ \det g=S^{-(n+1)},\ \mathrm{Ric}=(n+1)g\big)$ — **검증 1순위**

> **이 층의 역할.** 등뼈는 차원에 무관하다 — 같은 동작($\partial\bar\partial\log S$ → $\det$ → $-\partial\bar\partial\log\det$)을 $v=(1,z_1,\dots,z_n)$에 반복하면 CPⁿ의 FS 계량·Ricci가 글자 하나 안 바꾸고 올라간다. **그리고 여기가 골격의 가장 약한 고리**다: L2의 두 등뼈(직접 $\partial\bar\partial\log S$ vs 사영자 $\operatorname{tr}(dP\,dP)$)가 CPⁿ에서도 정말 같은 $g_{i\bar j}$로 합류하는가? 일치하면 골격이 서고, 불일치면 표 전체가 틀린 것이다. 본 문서 §4에서 **sympy로 두 경로를 독립 계산**해 일치를 못 박는다(1순위 검증).

학습용이라 작은 계단으로 쪼개고, 검산은 부록에. **모든 상수는 독립 계산으로 검증되었다.**

---

## 0. 표기와 규약

- $z=(z_1,\dots,z_n)\in\mathbb C^n$, $s=\sum_k|z_k|^2$, $S=1+s$. 올림 $v=(1,z_1,\dots,z_n)$, $\|v\|^2=S$.
- 포텐셜 $\Phi=\log S$, 계량 $g_{i\bar j}=\partial_{z_i}\partial_{\bar z_j}\Phi$ (등뼈, L2를 행렬로).
- 인덱스: $i$는 정칙($z_i$), $\bar j$는 반정칙($\bar z_j$). $n=1$로 내리면 L2·L3와 일치해야 한다(내적 검산).

---

## 1. Block 1 — 계량 $g_{i\bar j}$ (L2의 $\partial\bar\partial\log S$를 행렬로)

### 연습 1.1 — 첫 미분

- **(a)** $\partial_{\bar z_j}S=\partial_{\bar z_j}\big(1+\sum_k z_k\bar z_k\big)=z_j$. 따라서
$$
\partial_{\bar z_j}\log S=\frac{z_j}{S}.
$$

### 연습 1.2 — 둘째 미분 (몫의 미분, 행렬판)

- **(a)** $\partial_{z_i}S=\bar z_i$. 몫의 미분:
$$
\partial_{z_i}\frac{z_j}{S}=\frac{\delta_{ij}\,S-z_j\,\partial_{z_i}S}{S^2}=\frac{\delta_{ij}S-\bar z_i z_j}{S^2}.
$$
- **(b)** 즉
$$
\boxed{\ g_{i\bar j}=\partial_{z_i}\partial_{\bar z_j}\log S=\frac{S\,\delta_{ij}-\bar z_i z_j}{S^2}\ },\qquad
g=\frac{1}{S^2}\underbrace{(S\,I-\bar z\,z^{\mathsf T})}_{=:M}.
$$
- **(c)** $n=1$ 검산: $\dfrac{S-\bar z z}{S^2}=\dfrac{S-s}{S^2}=\dfrac{1}{S^2}$ — L2 등뼈와 정확히 일치. ✔ **분자 대각항에 $S$를 남길 것**(지우면 $\det$이 틀림).

---

## 2. Block 2 — $\det g=S^{-(n+1)}$ (두 방법)

### 연습 2.1 — 고유값 한 줄

- **(a)** $\bar z\,z^{\mathsf T}$는 **랭크 1**, 0 아닌 고유값은 trace $=\sum_k z_k\bar z_k=s$(고유벡터 $\bar z$ 방향).
- **(b)** $M=S\,I-\bar z z^{\mathsf T}$의 고유값: $\bar z$ 방향에서 $S-s=1$(한 개), 직교여공간에서 $S$($n-1$개). 따라서
$$
\det M=(S-s)\,S^{n-1}=1\cdot S^{n-1}=S^{n-1}.
$$
- **(c)** $g=M/S^2$, $n\times n$ ⟹
$$
\boxed{\ \det g=\frac{\det M}{(S^2)^n}=\frac{S^{n-1}}{S^{2n}}=S^{-(n+1)}\ }\quad(\text{CP}^1:S^{-2},\ \text{CP}^2:S^{-3}).
$$

### 연습 2.2 — 직접 전개로 교차검산 ($n=2$)

- **(a)** $g=\dfrac1{S^2}\begin{pmatrix}S-|z_1|^2 & -\bar z_1 z_2\\ -\bar z_2 z_1 & S-|z_2|^2\end{pmatrix}$.
- **(b)** $\det(S^2 g)=(S-|z_1|^2)(S-|z_2|^2)-|z_1|^2|z_2|^2=S^2-S(|z_1|^2+|z_2|^2)=S^2-Ss=S(S-s)=S$.
- **(c)** $\det g=S/S^4=S^{-3}$. 고유값 방법과 일치. ✔ *(Lifting A4.2)*

---

## 3. Block 3 — Ricci: $\mathrm{Ric}=(n+1)g$

### 연습 3.1 — $-\partial\bar\partial\log\det g$ (치환 박스에 그대로)

- **(a)** $\det g=S^{-(n+1)}=e^{-(n+1)\Phi}$ 이므로 $\log\det g=-(n+1)\Phi$:
$$
\rho_{i\bar j}=-\partial_{z_i}\partial_{\bar z_j}\log\det g=(n+1)\,\partial_{z_i}\partial_{\bar z_j}\log S=(n+1)\,g_{i\bar j}.
$$
- **(b)** 즉
$$
\boxed{\ \mathrm{Ric}=(n+1)\,g\ }\qquad(\text{CP}^1:2g,\ \text{CP}^2:3g).
$$

### 연습 3.2 — 왜 이렇게 깔끔한가 (확장의 엔진)

- **(a)** $\det g$ **자체가 포텐셜의 거듭제곱** $e^{-(n+1)\Phi}$다. 계량을 만든 $\Phi$가 $\det g$ 안에 다시 들어앉아 있어, $\partial\bar\partial$ 한 방에 $g$가 비례로 튀어나온다. 상수 $n+1$은 지수에서 떨어진 숫자. *(Lifting §5)*
- **(b)** ⚠ 함정(L3 §3 재확인): "$K=1$인데 왜 $c=n+1$?" — 불변량 $K=\rho/\omega=1$(둥근), $c=n+1$은 Ricci/포텐셜 비율. 포텐셜 $h$로 재면 $n+1$, Hermitian $2h$로 재면... 더 정확히는 CPⁿ에서 $\mathrm{Ric}=(n+1)g$가 표준(정칙단면곡률 일정). 어느 $g$인지 늘 밝힐 것.

---

## 4. ★ Block 4 — 검증 1순위: 두 등뼈가 정말 합류하는가 (sympy 독립 계산)

L2에서 두 경로 — (i) $\partial_{z_i}\partial_{\bar z_j}\log S$, (ii) $\operatorname{tr}(dP\,dP)$ — 가 CP¹에서 합류했다. **CPⁿ($n=2$)에서 독립적으로 계산해 일치를 확인**한다. 일치하면 L2의 합류가 모든 차원에서 서고, 불일치면 골격이 틀린 것. **손계산 전체 전개는 부록 A4**(한 칸씩), 아래는 그 기계 교차검증이다.

### 4.1 경로 (i): 포텐셜 $\partial_{z_i}\partial_{\bar z_j}\log S$

`verify2.py`에서 $\log S=\log(1+z_1\bar z_1+z_2\bar z_2)$를 직접 두 번 미분해 닫힌형 $(S\delta_{ij}-\bar z_i z_j)/S^2$와 **성분별 비교**:
```
Path(i) == closed form: True
det g = ...(전개식)... ; S^-(n+1)=S^-3: True
```

### 4.2 경로 (ii): 사영자 $\operatorname{tr}(dP\,dP)$, $v=(1,z_1,z_2)$

$P=vv^*/\|v\|^2$ ($3\times3$), $dP=\sum_{\text{var}}\partial P\,d(\text{var})$를 형식적 1-형식으로 전개, $\operatorname{tr}(dP\,dP)$의 $dz_i\,d\bar z_j$ 계수를 추출해 $2g_{i\bar j}$와 비교:
```
coeff dz1 dzb1 - 2g = 0   match=True
coeff dz1 dzb2 - 2g = 0   match=True
coeff dz2 dzb1 - 2g = 0   match=True
coeff dz2 dzb2 - 2g = 0   match=True
all pure dz-dz / dzb-dzb coeffs zero: True
PRIORITY 1: tr(dP dP)=2 g_ij dz dzb : True
```
순수 $dz_i dz_j$·$d\bar z_i d\bar z_j$ 계수가 **모두 0**(Kähler성: 포텐셜이 실수라 $(2,0)$·$(0,2)$ 성분 없음).

> **1순위 검증 결론.**
> $$
> \boxed{\ \operatorname{tr}(dP\,dP)\ \overset{n=2}{=}\ 2\,\big(\partial_{z_i}\partial_{\bar z_j}\log S\big)\,dz_i\,d\bar z_j\ }
> $$
> 두 경로가 **성분까지 완전일치**, $\det g=S^{-3}=S^{-(n+1)}$ 확인. ⟹ **L2의 두 등뼈 합류가 CPⁿ에서 선다. 골격 유효.** (만약 불일치였다면 이 표의 골격이 틀린 것이었다 — 그렇지 않았다.)

*(주의: 초기 계산에서 `simplify`를 `coeff` 전에 호출해 0이 나온 버그가 있었음 → `expand` 후 곧바로 `coeff`로 수정해 위 결과 확정. 검산의 검산.)*

---

## 5. Block 5 — $n\ge2$에서 무엇이 죽고 사는가 (확장의 정직한 단서)

- **정칙단면곡률은 모든 $n$에서 상수**(살아남음) — 이것이 FS를 못 박는 가장 강한 조건.
- **Riemann 단면곡률은 $n\ge2$에서 비상수**: 정칙단면곡률 $c>0$이면 실 단면곡률은 $[c/4,c]$에서 변동. 상수 단면곡률을 강요하면 $c/4=c\Rightarrow c=0$(평탄) — CPⁿ이 죽는다.
- **그래서 올릴 수 있는 형태는** 상수 단면곡률이 아니라 $-\partial\bar\partial\log\det g=c\,g$(상수 Ricci/KE)였다. L0의 곡면 자를 직접 못 올린 이유도 이것. *(Part3 §3)*

---

## 부록 A. 한 줄 한 줄 (검산용)

**A1** $\partial_{\bar z_j}\log S=z_j/S$; $\partial_{z_i}(z_j/S)=\dfrac{\delta_{ij}S-\bar z_i z_j}{S^2}$. ✔

**A2 (고유값)** $M=SI-\bar z z^{\mathsf T}$, 고유값 $\{S-s=1,\ \underbrace{S,\dots,S}_{n-1}\}$, $\det M=S^{n-1}$, $\det g=S^{n-1}/S^{2n}=S^{-(n+1)}$. ✔
**A2′ ($n=2$ 직접)** $\det(S^2 g)=(S-|z_1|^2)(S-|z_2|^2)-|z_1z_2|^2=S^2-Ss=S\Rightarrow\det g=S^{-3}$. ✔

**A3** $-\partial_i\partial_{\bar j}\log S^{-(n+1)}=(n+1)\partial_i\partial_{\bar j}\log S=(n+1)g_{i\bar j}$. ✔

**A4 (1순위) — 손으로 완전 전개 ($n=2$).** 코드 없이 따라갈 수 있도록 한 칸씩 깐다. 출발은 L1 §3.1에서 **손으로** 얻은 차원 무관 닫힌형
$$
\operatorname{tr}(dP\,dP)=\frac{2\big[N\,(dv^*dv)-|v^*dv|^2\big]}{N^2},\qquad N=\|v\|^2 .
$$

**(1) 세 조각을 $v=(1,z_1,z_2)$, $dv=(0,dz_1,dz_2)$, $N=S$로 손계산.**
$dv^*=(0,d\bar z_1,d\bar z_2)$, $v^*=(1,\bar z_1,\bar z_2)$ 이므로

$$
dv^*dv=d\bar z_1dz_1+d\bar z_2dz_2=\sum_{i}dz_i\,d\bar z_i,
$$
$$
v^*dv=\bar z_1dz_1+\bar z_2dz_2=\sum_i \bar z_i\,dz_i,\qquad
dv^*v=\overline{v^*dv}=\sum_j z_j\,d\bar z_j,
$$
$$
|v^*dv|^2=(v^*dv)(dv^*v)=\Big(\sum_i\bar z_i dz_i\Big)\Big(\sum_j z_j d\bar z_j\Big)=\sum_{i,j}\bar z_i z_j\,dz_i\,d\bar z_j .
$$

**(2) 조립 — 분자가 통째로 $g$로 묶인다.**
$$
N\,(dv^*dv)-|v^*dv|^2
=S\sum_i dz_i d\bar z_i-\sum_{i,j}\bar z_i z_j\,dz_i d\bar z_j
=\sum_{i,j}\big(S\,\delta_{ij}-\bar z_i z_j\big)\,dz_i\,d\bar z_j .
$$
따라서
$$
\operatorname{tr}(dP\,dP)=\frac{2}{S^2}\sum_{i,j}\big(S\delta_{ij}-\bar z_i z_j\big)dz_i d\bar z_j
=2\sum_{i,j}g_{i\bar j}\,dz_i d\bar z_j,\quad g_{i\bar j}=\frac{S\delta_{ij}-\bar z_i z_j}{S^2}.
$$
이것이 경로 (ii). **경로 (i)** 는 §1.2에서 손으로 $\partial_{z_i}\partial_{\bar z_j}\log S=\dfrac{S\delta_{ij}-\bar z_i z_j}{S^2}$ — **같은 $g_{i\bar j}$.** 두 등뼈가 손으로 합류. ✔

**(3) 성분으로 풀어 쓰기 (sympy 출력과 글자까지 대조).** $S=1+|z_1|^2+|z_2|^2$:
$$
2g_{1\bar 1}=\frac{2(S-|z_1|^2)}{S^2}=\frac{2(1+|z_2|^2)}{S^2},\quad
2g_{2\bar 2}=\frac{2(1+|z_1|^2)}{S^2},
$$
$$
2g_{1\bar 2}=\frac{-2\bar z_1 z_2}{S^2},\quad
2g_{2\bar 1}=\frac{-2\bar z_2 z_1}{S^2}.
$$
(sympy가 찍은 `2*(z2*zb2+1)/S²`, `-2*z2*zb1/S²` 등과 정확히 일치 — `zb`$=\bar z$.)

**(4) 순수 $(2,0)$·$(0,2)$ 항이 0인 구조적 이유 (손으로 보는 핵심).** 닫힌형의 두 항 $dv^*dv$와 $(v^*dv)(dv^*v)$는 **각각 "정칙 미분 1개 × 반정칙 미분 1개"** 의 곱이라, $dz_i\,d\bar z_j$ 꼴만 만든다. $dz_i\,dz_j$나 $d\bar z_i\,d\bar z_j$는 애초에 나올 자리가 없다. 그래서 Kähler성($(2,0)=(0,2)=0$)이 **닫힌형에서 자명** — 이것이 sympy가 "순수항 0"을 준 이유다. (계산이 아니라 꼴에서 보인다.)

**A4′ (코드 교차검증, `verify2.py`)** 위 손계산을 그대로 기계로 재현: `Path(i)==closed form: True`; `coeff(dz_i dzb_j)-2g_ij=0` ∀i,j; 순수항 0; `det g=S^-3`; `PRIORITY 1 ... : True`. 손과 기계 일치. ✔

---

## 결과 요약

| 블록 | 한 일 | 결과 |
|---|---|---|
| B1 | $\partial\bar\partial\log S$ 행렬화 | $g_{i\bar j}=\dfrac{S\delta_{ij}-\bar z_i z_j}{S^2}$ ($n{=}1$→$1/S^2$) |
| B2 | $\det$ (고유값 + 직접) | $\det g=S^{-(n+1)}$ |
| B3 | $-\partial\bar\partial\log\det g$ | $\mathrm{Ric}=(n+1)g$; 엔진 $\det g=e^{-(n+1)\Phi}$ |
| **B4** | **1순위 검증** | **$\operatorname{tr}(dP\,dP)=2\partial\bar\partial\log S$ 성분일치($n{=}2$) ⟹ 골격 유효** |
| B5 | $n\ge2$ 분기 | 상수 단면곡률 죽음, 상수 Ricci/정칙단면 생존 |

**한 문장.** $v=(1,z_1,\dots,z_n)$로 같은 동작을 반복하면 $g_{i\bar j}=\tfrac{S\delta_{ij}-\bar z_i z_j}{S^2}$, $\det g=S^{-(n+1)}$, $\mathrm{Ric}=(n+1)g$가 글자 하나 안 바꾸고 올라가고 — 직접 $\partial\bar\partial\log S$와 사영자 $\operatorname{tr}(dP\,dP)$가 $n=2$에서 성분까지 일치함을 sympy로 확인했으므로, L2의 두 등뼈 합류는 모든 차원에서 서고 골격은 유효하다(1순위 검증 완료).

*출처: cp1_laplacian_curvature_lifting_note.md(§4–5), cp1_constant_ricci_kahler_einstein_observation_part3_note.md(§3–4), fs_via_projector_conic_pullback_path_note.md(§4); 검증 verify2.py.*
