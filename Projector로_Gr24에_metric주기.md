# Projector들의 모임에 metric 주기 — CP¹ 손노트에서 Gr(2,4)로

> **질문 하나.** $4\times2$ 행렬 $X$가 나타내는 평면을 $P=XX^*$로 기억하기로 했다. 그렇다면 이런 rank-$2$ projector들의 모임에 길이는 어떻게 주는가?
>
> **이 노트의 범위.** 차트 $Z$, Plücker 좌표, $\mathbb CP^5$, Reeb 벡터장은 아직 쓰지 않는다. 실제 행렬곡선 두 개를 미분하고, 손노트의 CP¹ 계산이 고른 계수를 그대로 옮겨 $g_P^{\mathrm{QFI}}(A,C)=2\operatorname{tr}(AC)$와 $g_P^{\mathrm{FS}}(A,C)=\frac12\operatorname{tr}(AC)$까지만 얻는다. 두 식은 서로 다른 metric이 아니라 $g^{\mathrm{QFI}}=4g^{\mathrm{FS}}$라는 **정규화 차이**다.
>
> **검산.** `verify_projector_gr24_metric.py` — 본문의 행렬곱·미분·trace·계수 **20/20 통과**.

---

## §0. 먼저 두 곡선을 눈으로 구별한다

출발점은

$$
X_0=
\begin{pmatrix}
1&0\\
0&1\\
0&0\\
0&0
\end{pmatrix},
\qquad
P_0=X_0X_0^*=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}
$$

이다. $X_0$의 두 열은 $e_1,e_2$이고, $P_0$는 벡터 $(a,b,c,d)^{\mathsf T}$에서 앞의 두 성분만 남긴다:

$$
P_0
\begin{pmatrix}a\\b\\c\\d\end{pmatrix}
=
\begin{pmatrix}a\\b\\0\\0\end{pmatrix}.
$$

### 0.1 행렬만 움직이고 평면은 안 움직이는 곡선

두 열을 같은 평면 안에서 돌린다:

$$
R(t)=
\begin{pmatrix}
\cos t&-\sin t\\
\sin t&\cos t
\end{pmatrix},
\qquad
X_{\mathrm{same}}(t)=X_0R(t).
$$

$X_{\mathrm{same}}(t)$는 움직인다. 실제로

$$
\dot X_{\mathrm{same}}(0)=
\begin{pmatrix}
0&-1\\
1&0\\
0&0\\
0&0
\end{pmatrix}\ne0.
$$

그러나 projector는

$$
\begin{aligned}
P_{\mathrm{same}}(t)
&=X_{\mathrm{same}}(t)X_{\mathrm{same}}(t)^*\\
&=X_0R(t)R(t)^*X_0^*\\
&=X_0I_2X_0^*\\
&=P_0
\end{aligned}
$$

로 아예 일정하다. 따라서

$$
\dot P_{\mathrm{same}}(t)=0.
$$

이 곡선에는 길이를 주지 않아야 한다. 우리가 재려는 것은 **기저행렬 $X$의 움직임**이 아니라 **평면, 즉 $P$의 움직임**이기 때문이다.

### 0.2 평면이 실제로 움직이는 곡선

이번에는 첫 번째 열 $e_1$은 고정하고, 두 번째 열을 $e_2$에서 $e_3$ 쪽으로 돌린다:

$$
X(t)=
\begin{pmatrix}
1&0\\
0&\cos t\\
0&\sin t\\
0&0
\end{pmatrix}.
$$

두 열은 계속 정규직교한다:

$$
X(t)^*X(t)=
\begin{pmatrix}
1&0\\
0&\cos^2t+\sin^2t
\end{pmatrix}
=I_2.
$$

이제 이 절의 두 행렬에서만

$$
c=\cos t,
\qquad
s=\sin t
$$

로 짧게 쓰자. 이번 projector는

$$
P(t)=X(t)X(t)^*
=
\begin{pmatrix}
1&0&0&0\\
0&c^2&cs&0\\
0&cs&s^2&0\\
0&0&0&0
\end{pmatrix}.
$$

$t$가 변하면 이 행렬도 변한다. 미분하면

$$
\dot P(t)=
\begin{pmatrix}
0&0&0&0\\
0&-2cs&c^2-s^2&0\\
0&c^2-s^2&2cs&0\\
0&0&0&0
\end{pmatrix}.
$$

특히 $t=0$에서

$$
A:=\dot P(0)=
\begin{pmatrix}
0&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&0
\end{pmatrix}\ne0.
$$

두 곡선의 차이는 이제 $P$에서 보인다:

| 올린 행렬의 움직임 | projector에서 | 평면에서 |
|---|---:|---|
| $X_0R(t)$ | $\dot P=0$ | 안 움직임 |
| $[e_1,\cos t\,e_2+\sin t\,e_3]$ | $\dot P\ne0$ | 움직임 |

이제 $\dot P$의 크기만 정하면 된다.

---

## §1. CP¹ 손노트가 계수 $2$를 이미 골랐다

우선 방금 얻은 $A=\dot P(0)$를 제곱한다:

$$
A^2=
\begin{pmatrix}
0&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&0
\end{pmatrix},
\qquad
\operatorname{tr}(A^2)=2.
$$

따라서 $\operatorname{tr}(\dot P^2)$는 실제 평면운동에 양의 수를 준다. 남은 질문은 앞에 붙일 상수다:

$$
ds^2=c\,\operatorname{tr}(dP^2).
$$

그 $c$는 새로 정할 필요가 없다. CP¹ 손노트에서 이미 정했다.

rank-$1$ projector를 Pauli 행렬로 쓰면

$$
P=vv^*=\frac12\bigl(I+n_1\sigma_1+n_2\sigma_2+n_3\sigma_3\bigr),
\qquad |n|=1.
$$

미분하면

$$
dP=\frac12\sum_{i=1}^3dn_i\,\sigma_i.
$$

여기서

$$
\operatorname{tr}(\sigma_i\sigma_j)=2\delta_{ij}
$$

이므로

$$
\begin{aligned}
\operatorname{tr}(dP^2)
&=\frac14\sum_{i,j}dn_i\,dn_j\,
  \operatorname{tr}(\sigma_i\sigma_j)\\
&=\frac12\sum_i dn_i^2\\
&=\frac12|dn|^2.
\end{aligned}
$$

손노트는 Bloch 구면을 반지름 $1$인 구면으로 두고

$$
ds^2_{\mathrm{hand}}=|dn|^2
$$

를 사용했다. 위 trace 계산에 넣으면

$$
\boxed{\ ds^2_{\mathrm{hand}}
=2\operatorname{tr}(dP^2).\ }
$$

이것이 QFIM 정규화다. 이름보다 중요한 것은 계수의 출처다. **$2$는 rank가 $2$가 되어서 생긴 수가 아니라, CP¹ 손노트에서 단위 Bloch 구면을 선택했기 때문에 이미 생긴 수다.**

위의 $\dot P(t)$를 직접 제곱하면 모든 $t$에서

$$
\operatorname{tr}\bigl(\dot P(t)^2\bigr)=2.
$$

따라서 이 곡선에서는

$$
ds^2_{\mathrm{QFI}}
=2\operatorname{tr}\bigl(\dot P(t)^2\bigr)dt^2
=4dt^2.
$$

속력은 $2$이고, $0\le t\le\theta$ 동안의 길이는

$$
L_{\mathrm{QFI}}(P|_{[0,\theta]})
=\int_0^\theta
\sqrt{2\operatorname{tr}(\dot P(t)^2)}\,dt
=\int_0^\theta2\,dt
=2\theta.
$$

---

## §2. 이제서야 projector들의 모임을 적는다

우리가 방금 움직인 행렬들이 사는 집합은

$$
\mathcal P_2
=\left\{
P\in M_4(\mathbb C):
P^*=P,\quad P^2=P,\quad \operatorname{tr}P=2
\right\}
$$

이다.

$X^*X=I_2$인 $4\times2$ 행렬에서 $P=XX^*$를 만들면 실제로

$$
P^*=(XX^*)^*=XX^*=P,
$$

$$
P^2=XX^*XX^*=X(X^*X)X^*=XX^*=P,
$$

$$
\operatorname{tr}P
=\operatorname{tr}(XX^*)
=\operatorname{tr}(X^*X)
=\operatorname{tr}I_2
=2.
$$

반대로 $P^*=P$, $P^2=P$이면 $P$의 고윳값은 $0$ 또는 $1$이다. $\operatorname{tr}P=2$이므로 고윳값 $1$이 정확히 두 개이고, $P$의 상은 $2$차원 부분공간이다. 따라서

$$
\boxed{\ \mathcal P_2\cong\mathrm{Gr}(2,4).\ }
$$

이것은 새로운 추상적 모형이 아니다. $2$차원 부분공간을 **그 부분공간으로의 직교투영이라는 $4\times4$ 행렬 하나로 기록한 것**이다.

---

## §3. 아무 Hermitian 행렬이나 속도가 되는 것은 아니다

$P(t)$가 $\mathcal P_2$ 안의 곡선이고

$$
P(0)=P,
\qquad
A=\dot P(0)
$$

라고 하자.

먼저 $P(t)^*=P(t)$를 미분하면

$$
A^*=A.
$$

다음으로 $P(t)^2=P(t)$를 미분한다. 곱의 미분 한 번이다:

$$
\frac d{dt}P(t)^2
=\dot P(t)P(t)+P(t)\dot P(t).
$$

$t=0$을 넣으면

$$
\boxed{\ AP+PA=A.\ }
$$

마지막으로 $\operatorname{tr}P(t)=2$를 미분하면

$$
\operatorname{tr}A=0.
$$

이 조건들이 실제로 무엇을 금지하는지 $P_0$에서 보자. $4\times4$ 행렬 $A$를 $2\times2$ 블록으로

$$
A=
\begin{pmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{pmatrix},
\qquad
P_0=
\begin{pmatrix}
I_2&0\\
0&0
\end{pmatrix}
$$

라고 쓴다. 그러면

$$
AP_0+P_0A
=
\begin{pmatrix}
2A_{11}&A_{12}\\
A_{21}&0
\end{pmatrix}.
$$

이것이 $A$ 자체와 같아야 하므로

$$
A_{11}=0,
\qquad
A_{22}=0.
$$

또한 $A^*=A$이므로 $A_{12}=A_{21}^*$. 따라서 모든 허용된 속도는

$$
\boxed{
A=
\begin{pmatrix}
0&B^*\\
B&0
\end{pmatrix},
\qquad B\in M_2(\mathbb C).
}
$$

의 꼴이다.

§0.2의 실제 속도도 이 꼴이다. 그때는

$$
B=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$

즉 대각 블록은 같은 평면 안과 그 직교여공간 안에서 도는 움직임이고 projector의 속도에서는 사라진다. 남는 것은 두 공간 사이를 오가는 비대각 블록 $B$다.

---

## §4. 이 속도들에 내적을 준다

CP¹ 손노트의 정규화를 그대로 사용하여, $P\in\mathcal P_2$에서 두 허용된 속도 $A,C$에

$$
\boxed{
g_P^{\mathrm{QFI}}(A,C)
=2\operatorname{tr}(AC)
}
$$

라고 둔다. $A,C$는 Hermitian 행렬이고 접공간은 실벡터공간이므로 이것은 실쌍선형식이다. 실제로

$$
\overline{\operatorname{tr}(AC)}
=\operatorname{tr}((AC)^*)
=\operatorname{tr}(CA)
=\operatorname{tr}(AC).
$$

대칭성은 trace의 순환성에서 바로 나온다:

$$
g_P^{\mathrm{QFI}}(C,A)
=2\operatorname{tr}(CA)
=2\operatorname{tr}(AC)
=g_P^{\mathrm{QFI}}(A,C).
$$

길이의 제곱이 양수인지도 위 블록형에 직접 넣어 확인할 수 있다:

$$
A^2=
\begin{pmatrix}
B^*B&0\\
0&BB^*
\end{pmatrix}.
$$

따라서

$$
\begin{aligned}
g_{P_0}^{\mathrm{QFI}}(A,A)
&=2\operatorname{tr}(A^2)\\
&=2\operatorname{tr}(B^*B)+2\operatorname{tr}(BB^*)\\
&=4\operatorname{tr}(B^*B)\\
&=4\sum_{i,j}|B_{ij}|^2.
\end{aligned}
$$

$A\ne0$이면 $B\ne0$이므로 이 값은 엄밀히 양수다. 그래서 이 내적은 실제 Riemannian metric이다.

### 좌표나 기저를 바꾸어도 값이 같은가

$U\in U(4)$로 주변공간의 정규직교 기저를 바꾸면

$$
P\longmapsto UPU^*,
\qquad
A\longmapsto UAU^*,
\qquad
C\longmapsto UCU^*.
$$

이때

$$
\begin{aligned}
g_{UPU^*}^{\mathrm{QFI}}(UAU^*,UCU^*)
&=2\operatorname{tr}(UAU^*UCU^*)\\
&=2\operatorname{tr}(UACU^*)\\
&=2\operatorname{tr}(AC)\\
&=g_P^{\mathrm{QFI}}(A,C).
\end{aligned}
$$

따라서 이 metric은 $P_0$의 특별한 좌표에 묶여 있지 않다.

---

## §5. metric과 두 점 사이의 거리는 같은 단어가 아니다

§4의 내적은 한 점 $P$에서 **순간속도**의 길이를 정한다. 곡선 $P(t)$ 전체의 길이는

$$
L_{\mathrm{QFI}}[P]
=\int_a^b
\sqrt{2\operatorname{tr}\bigl(\dot P(t)^2\bigr)}\,dt.
$$

두 projector $P,Q$ 사이의 Riemannian 거리는 그 둘을 잇는 모든 projector 곡선 가운데 가장 짧은 길이다:

$$
d_{\mathrm{QFI}}(P,Q)
=\inf_{\substack{P(a)=P\\P(b)=Q}}
L_{\mathrm{QFI}}[P].
$$

이 정의에서 §0.1의 기저회전은 projector 곡선이 상수이므로 길이가 $0$이다. 반면 §0.2의 평면회전은 §1에서 길이가 $2\theta$였다.

주변 행렬공간에서 두 projector를 곧장 빼서 얻는 값과 혼동하면 안 된다. §0.2의 $P(t)$에 대해 직접 계산하면

$$
\operatorname{tr}\bigl((P(\theta)-P_0)^2\bigr)
=2\sin^2\theta.
$$

따라서 같은 계수 $2$를 붙인 주변공간의 직선거리, 즉 현의 길이는

$$
d_{\mathrm{chord}}(P_0,P(\theta))
=\sqrt{2\operatorname{tr}\bigl((P(\theta)-P_0)^2\bigr)}
=2|\sin\theta|.
$$

projector들의 공간 안에서 §0.2의 곡선을 따라간 길이는 $2|\theta|$이고, 주변공간에서 곧장 잰 현은 $2|\sin\theta|$다. 구면의 호와 현이 다른 것과 같다. 다만

$$
2\sin\theta=2\theta+O(\theta^3)
$$

이므로 아주 가까이에서는 같은 일차 길이를 준다. Riemannian metric은 바로 그 일차 길이를 모든 점에서 이어 붙이는 장치다.

---

## §6. 어느 metric을 목표로 하는가 — 계수만 마지막에 갈라진다

지금까지 손노트의 단위 Bloch 구면, 곧 QFIM 정규화를 따랐다:

$$
\boxed{
g_P^{\mathrm{QFI}}(A,C)=2\operatorname{tr}(AC).
}
$$

$\mathbb CP^1$을 반지름 $\tfrac12$인 구면으로 보는 표준 Fubini–Study 정규화는 이것의 $\tfrac14$이다. 따라서 $\mathbb CP^5$의 FS metric과 비교할 때 사용할 projector metric은

$$
\boxed{
g_P^{\mathrm{FS}}(A,C)
=\frac14g_P^{\mathrm{QFI}}(A,C)
=\frac12\operatorname{tr}(AC).
}
$$

우리의 실제 곡선에서는

$$
g^{\mathrm{QFI}}(\dot P,\dot P)=4,
\qquad
g^{\mathrm{FS}}(\dot P,\dot P)=1.
$$

이 노트가 한 일은 $\mathbb CP^5$에서 metric을 빌려오는 것이 아니다. rank-$2$ projector들의 모임을 Hermitian 행렬공간 안에 놓고, CP¹ 손노트와 같은 trace 계산으로 metric을 **직접** 준 것이다. 이후 Plücker 임베딩으로 당긴 FS metric과 비교할 때는 위 FS projector 식을 목표로 놓고 양쪽을 따로 계산하면 된다.
