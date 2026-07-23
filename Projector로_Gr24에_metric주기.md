# Projector들의 모임에 metric 주기 — CP¹ 손노트에서 Gr(2,4)로

> **질문 하나.** $4\times2$ 행렬 $X$가 나타내는 평면을 $P=XX^*$로 기억하기로 했다. 그렇다면 이런 rank-$2$ projector들의 모임에 길이는 어떻게 주는가?
>
> **이 노트의 범위.** 먼저 실제 행렬곡선 두 개로 rank-$2$ projector의 접벡터와 trace metric을 만든다. 그러나 trace 공식을 결론으로 놓지 않는다. CP¹ 손노트처럼 복소수 한 칸 $z$가 움직이는 평면족을 끝까지 계산한 뒤, 임의의 $2\times2$ 차트 $Z$로 넓혀 projector trace, $\partial\bar\partial\log\det(I+Z^*Z)$, Plücker 임베딩으로 당긴 $\mathbb CP^5$의 FS metric, Reeb 계산에서 내려온 $dA/2$가 같은 물건의 서로 다른 계산임을 확인한다. $4\times4$ 성분표, Ricci, 부피, 측지거리는 다루지 않는다.
>
> **검산.** `verify_projector_gr24_metric.py` — 본문의 행렬곱·미분·trace·계수 **32/32 통과**.
>
> **이 노트 안에서 바로가기.** metric만 따라가려면 [두 곡선](#projector-two-curves) → [한 칸짜리 $\mathbb{CP}^1$](#projector-cp1-slice) → [임의의 $Z$](#projector-general-chart)까지만 읽으면 된다. “그런데 왜 Plücker와 $\mathbb{CP}^5$가 필요한가”는 [§7.2](#projector-why-plucker)에서 별도의 질문으로 시작한다.

---

<a id="projector-two-curves"></a>

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

<a id="projector-cp1-slice"></a>

## §5. trace를 예전 CP¹ 계산에 다시 꽂는다

CP¹ 손노트는 $\operatorname{tr}(dP\,dP)$라고 적고 멈추지 않았다. 그 식을 실제 좌표 $z=x+iy$에 넣어 역입체사영에서 얻었던

$$
\frac{dx^2+dy^2}{(1+x^2+y^2)^2}
$$

와 만나는지 확인했다. $Gr(2,4)$에서도 같은 검사를 해야 한다.

네 복소좌표를 한꺼번에 움직이지 말고, §0.2에서 움직였던 자리 하나만 복소수로 만든다:

$$
V(z)=
\begin{pmatrix}
1&0\\
0&1\\
0&z\\
0&0
\end{pmatrix}.
$$

두 열은 $e_1$과 $e_2+ze_3$이다. $z$가 바뀌면 두 번째 직선이 바뀌므로 평면도 실제로 바뀐다.

여기서는 열의 길이가 $1$이 아니므로 $VV^*$라고 쓰면 projector가 아니다. 열들의 Gram 행렬을 먼저 계산한다:

$$
G:=V^*V
=
\begin{pmatrix}
1&0\\
0&1+|z|^2
\end{pmatrix}.
$$

$S:=1+|z|^2$라고 쓰면

$$
G^{-1}=
\begin{pmatrix}
1&0\\
0&S^{-1}
\end{pmatrix},
$$

따라서 이 평면 위로의 직교 projector는

$$
\begin{aligned}
P(z)
&=V(V^*V)^{-1}V^*\\
&=
\begin{pmatrix}
1&0&0&0\\
0&S^{-1}&\bar zS^{-1}&0\\
0&zS^{-1}&|z|^2S^{-1}&0\\
0&0&0&0
\end{pmatrix}.
\end{aligned}
$$

이 행렬에서 첫 번째 좌표는 늘 $1$, 네 번째 좌표는 늘 $0$이다. 실제로 움직이는 가운데 $2\times2$ 블록만 떼면

$$
\frac1S
\begin{pmatrix}
1&\bar z\\
z&|z|^2
\end{pmatrix}.
$$

이것은 CP¹ 손노트의 rank-$1$ projector와 문자 그대로 같다. $Gr(2,4)$ 안에서 CP¹ 하나를 찾아낸 것이다.

### 그 블록을 다시 미분한다

$$
dS=\bar z\,dz+z\,d\bar z
$$

이므로 성분별 몫미분은

$$
dP
=\frac1{S^2}
\begin{pmatrix}
0&0&0&0\\
0&-dS&d\bar z-\bar z^2dz&0\\
0&dz-z^2d\bar z&dS&0\\
0&0&0&0
\end{pmatrix}.
$$

여기서 $dz\,d\bar z$는 쐐기곱이 아니라 metric을 계산할 때의 대칭곱이다. 실제 실접벡터 하나에 두 번 넣으면 $|\dot z|^2$가 된다.

움직이는 $2\times2$ 블록의 세 성분을

$$
a:=-dS,
\qquad
b:=d\bar z-\bar z^2dz,
\qquad
c:=dz-z^2d\bar z
$$

라고 쓰면 그 블록은 $S^{-2}\bigl(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\bigr)$이고

$$
\begin{pmatrix}a&b\\c&-a\end{pmatrix}^{\!2}
=(a^2+bc)I_2.
$$

이제 분자만 편다:

$$
\begin{aligned}
a^2
&=(\bar z\,dz+z\,d\bar z)^2\\
&=\bar z^2dz^2+2|z|^2dz\,d\bar z+z^2d\bar z^2,
\end{aligned}
$$

$$
\begin{aligned}
bc
&=(d\bar z-\bar z^2dz)(dz-z^2d\bar z)\\
&=dz\,d\bar z-z^2d\bar z^2-\bar z^2dz^2+|z|^4dz\,d\bar z.
\end{aligned}
$$

$dz^2$와 $d\bar z^2$ 항이 지워지고

$$
a^2+bc
=(1+2|z|^2+|z|^4)dz\,d\bar z
=S^2dz\,d\bar z.
$$

따라서

$$
\boxed{
\operatorname{tr}(dP\,dP)
=\frac{2\,dz\,d\bar z}{S^2}.
}
$$

FS 정규화와 QFIM 정규화는 이제 숫자까지 분리된다:

$$
\boxed{
ds^2_{\mathrm{FS}}
=\frac12\operatorname{tr}(dP\,dP)
=\frac{dz\,d\bar z}{(1+|z|^2)^2},
}
$$

$$
\boxed{
ds^2_{\mathrm{QFI}}
=2\operatorname{tr}(dP\,dP)
=\frac{4\,dz\,d\bar z}{(1+|z|^2)^2}.
}
$$

§0.2의 실곡선은 이 복소직선에서 $z=\tan t$로 놓은 것이다. 실제로

$$
S=1+\tan^2t=\sec^2t,
\qquad
\dot z=\sec^2t,
$$

이므로

$$
g_{\mathrm{FS}}(\dot P,\dot P)
=\frac{|\dot z|^2}{S^2}=1,
\qquad
g_{\mathrm{QFI}}(\dot P,\dot P)=4.
$$

§1에서 행렬을 직접 미분해 얻었던 두 숫자가 좌표 $z$ 계산에서도 그대로 돌아왔다.

---

<a id="projector-general-chart"></a>

## §6. 한 칸에서 본 계산을 임의의 $Z$로 넓힌다

이제야 네 복소좌표를 한꺼번에 둔다:

$$
V(Z)=
\begin{pmatrix}
I_2\\
Z
\end{pmatrix},
\qquad
G:=V^*V=I_2+Z^*Z,
\qquad
P:=VG^{-1}V^*.
$$

$Z(t)$가 움직이는 실곡선을 하나 잡고

$$
D:=\dot Z,
\qquad
\dot V=
\begin{pmatrix}
0\\D
\end{pmatrix}
$$

라고 하자. 목표는 $\frac12\operatorname{tr}(\dot P^2)$를 $D$만으로 적는 것이다.

먼저 $P=VG^{-1}V^*$를 보통 곱미분한다:

$$
\dot P
=\dot V G^{-1}V^*
+V\dot{(G^{-1})}V^*
+VG^{-1}\dot V^*.
$$

역행렬 미분은 $G^{-1}G=I_2$를 미분해서 얻는다:

$$
\dot{(G^{-1})}
=-G^{-1}\dot G G^{-1},
\qquad
\dot G=\dot V^*V+V^*\dot V.
$$

두 식을 대입하고 $P=VG^{-1}V^*$를 다시 묶으면

$$
\boxed{
\dot P
=(I_4-P)\dot V G^{-1}V^*
+VG^{-1}\dot V^*(I_4-P).
}
$$

첫 항을

$$
K:=(I_4-P)\dot V G^{-1}V^*
$$

라고 쓰면 둘째 항은 $K^*$다. 또한 $V^*(I_4-P)=0$이므로

$$
K^2=0,
\qquad
(K^*)^2=0.
$$

따라서

$$
\begin{aligned}
\frac12\operatorname{tr}(\dot P^2)
&=\frac12\operatorname{tr}\bigl((K+K^*)^2\bigr)\\
&=\frac12\operatorname{tr}(KK^*+K^*K)\\
&=\operatorname{tr}(K^*K).
\end{aligned}
$$

$K^*K$를 넣고 trace를 순환시키면

$$
\begin{aligned}
\operatorname{tr}(K^*K)
&=\operatorname{tr}\!\left(
VG^{-1}\dot V^*(I_4-P)\dot V G^{-1}V^*
\right)\\
&=\operatorname{tr}\!\left(
G^{-1}\dot V^*(I_4-P)\dot V G^{-1}V^*V
\right)\\
&=\operatorname{tr}\!\left(
G^{-1}\dot V^*(I_4-P)\dot V
\right).
\end{aligned}
$$

마지막 줄에서 $V^*V=G$가 오른쪽의 $G^{-1}$ 하나를 지웠다.

$\dot V$는 아래 블록에만 $D$를 가지므로 $I_4-P$의 오른쪽 아래 블록만 필요하다. $P=VG^{-1}V^*$를 블록으로 쓰면 그 블록은

$$
I_2-ZG^{-1}Z^*.
$$

$H:=I_2+ZZ^*$라고 두자. 이 행렬이 $H^{-1}$임은 이름을 빌리지 않고 곱해서 확인할 수 있다:

$$
\begin{aligned}
&(I_2-ZG^{-1}Z^*)(I_2+ZZ^*)\\
&=I_2+ZZ^*-ZG^{-1}Z^*-ZG^{-1}(Z^*Z)Z^*\\
&=I_2+Z\bigl[I_2-G^{-1}-G^{-1}(Z^*Z)\bigr]Z^*\\
&=I_2+Z\bigl[I_2-G^{-1}(I_2+Z^*Z)\bigr]Z^*\\
&=I_2.
\end{aligned}
$$

그러므로

$$
\dot V^*(I_4-P)\dot V
=D^*H^{-1}D.
$$

전부 조립하면 projector에서 직접 얻은 FS 길이는

$$
\boxed{
g^{\mathrm{FS}}_Z(D,D)
=\frac12\operatorname{tr}(\dot P^2)
=\operatorname{tr}\!\left[
(I_2+Z^*Z)^{-1}D^*
(I_2+ZZ^*)^{-1}D
\right].
}
$$

$Z$가 §5의 한 칸짜리 행렬이면 이 식의 오른쪽은 정확히 $|\dot z|^2/(1+|z|^2)^2$로 줄어든다.

---

## §7. 같은 식이 차트·Plücker·Reeb 계산에서 다시 나온다

이제 projector 계산과 다른 계산을 독립적으로 진행한 뒤 마지막에만 만난다.

### 7.1 $\log\det(I_2+Z^*Z)$를 두 번 미분한다

$$
\Phi(Z):=\log\det G,
\qquad
G=I_2+Z^*Z
$$

라고 하자. 복소방향 $E$로 $Z$만 미분하면

$$
\partial_E\Phi
=\operatorname{tr}(G^{-1}Z^*E).
$$

이제 독립된 방향 $D$로 $Z^*$ 쪽을 미분한다. 이때

$$
\bar\partial_DG=D^*Z,
\qquad
\bar\partial_D(G^{-1})=-G^{-1}D^*ZG^{-1},
\qquad
\bar\partial_DZ^*=D^*.
$$

곱미분하면

$$
\begin{aligned}
\bar\partial_D\partial_E\Phi
&=\operatorname{tr}\!\left[
-G^{-1}D^*ZG^{-1}Z^*E+G^{-1}D^*E
\right]\\
&=\operatorname{tr}\!\left[
G^{-1}D^*(I_2-ZG^{-1}Z^*)E
\right]\\
&=\operatorname{tr}\!\left[
G^{-1}D^*H^{-1}E
\right].
\end{aligned}
$$

특히 $E=D$로 두면 §6의 projector 계산과 정확히 같다:

$$
\boxed{
\frac12\operatorname{tr}(\dot P^2)
=\bar\partial_D\partial_D\log\det(I_2+Z^*Z).
}
$$

projector trace와 켈러 퍼텐셜은 서로 다른 metric을 우연히 정의한 것이 아니다. 같은 길이제곱을 두 경로로 계산한 것이다.

<a id="projector-why-plucker"></a>

### 7.2 metric은 이미 얻었는데 왜 Plücker와 $\mathbb CP^5$로 가는가

먼저 경계를 분명히 하자. **목표가 $Gr(2,4)$의 metric 하나라면 §6에서 계산은 끝났다.**

$$
P(V)=V(V^*V)^{-1}V^*
$$

는 $V\mapsto VG$라는 기저 중복을 완전히 지우며, $\frac12\operatorname{tr}(dP^2)$로 길이도 직접 준다. Plücker는 metric을 얻기 위해 반드시 거쳐야 하는 장치가 아니다.

다만 $P(V)$에는 $V^*$와 $(V^*V)^{-1}$이 들어간다. 이것은 직교사영자를 만들기에는 정확한 식이지만, $V$의 성분에 대한 **정칙 다항식 기록**은 아니다. 이제 다음 요구를 추가한다고 하자.

> 같은 평면을 기저 선택과 무관하게 기록하되, 그 기록이 $V$의 성분에 대해 정칙 다항식이고, 한 차트를 고르지 않아도 전역적으로 이어지게 하라.

이 추가 요구가 생기는 순간 projector와 다른 기록이 필요해진다.

$V$의 두 열을 $v,w\in\mathbb C^4$라 하고 기저를

$$
G=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\in GL(2,\mathbb C)
$$

로 바꾸자. $V'=VG$의 두 열은

$$
v'=av+cw,
\qquad
w'=bv+dw
$$

이다. 두 열을 교대곱에 넣어 한 줄씩 펴면

$$
\begin{aligned}
v'\wedge w'
&=(av+cw)\wedge(bv+dw)\\
&=ab\,v\wedge v+ad\,v\wedge w
  +cb\,w\wedge v+cd\,w\wedge w\\
&=ad\,v\wedge w-cb\,v\wedge w\\
&=(ad-bc)v\wedge w\\
&=(\det G)(v\wedge w).
\end{aligned}
$$

행렬 전체였던 기저 중복 $G\in GL(2)$가 복소수 하나 $\det G$의 배수 중복으로 줄었다. 복소사영공간은 이 영이 아닌 복소수배를 같은 점으로 보므로

$$
W=\operatorname{span}(v,w)
\longmapsto
[v\wedge w]
\in\mathbb P(\Lambda^2\mathbb C^4)
=\mathbb CP^5
$$

가 기저 선택과 무관하게 정의된다. **이 현상을 확인한 뒤에 붙이는 이름이 Plücker 임베딩이다.**

$v\wedge w$의 여섯 성분은 $V$의 $2\times2$ 소행렬식들이다. 가우스 소거는 이 발상을 만들어 낸 원인이 아니라, 그 여섯 사영좌표에서 원래 평면을 다시 복원하는 계산이다.

> **계산 우회로 — 기존 걸음 6의 정확한 네 절.** 이 문서는 열 프레임 $V$를 쓰고, 걸음 6a는 행 프레임 $A=V^{\mathsf T}$를 쓴다. 전치만 다르고 기저변환과 소행렬식 계산은 같다. [① 가우스 소거로 차트 대표 고르기](걸음6_Gr24_플뤼커_완전판.html#plucker-gaussian-chart) → [② 소행렬식이 모두 $\det G$배 되는 계산](걸음6_Gr24_플뤼커_완전판.html#plucker-minors-scale) → [③ 그 소행렬식이 $v\wedge w$의 성분임을 확인](걸음6_Gr24_플뤼커_완전판.html#plucker-wedge-coordinates) → [④ 사영좌표에서 평면을 역복원](걸음6_Gr24_플뤼커_완전판.html#plucker-reconstruction). 네 계산 뒤에는 [Cauchy--Binet 합류점](걸음6_Gr24_플뤼커_완전판.html#plucker-cauchy-binet)으로 간다.

이제 Plücker 벡터를

$$
q(Z)=v\wedge w\in\Lambda^2\mathbb C^4\cong\mathbb C^6
$$

라고 쓰자. Cauchy--Binet 공식을 이 $4\times2$ 행렬에 적용하면

$$
\boxed{
\|q(Z)\|^2
=\sum_{i<j}|p_{ij}(Z)|^2
=\det(V^*V)
=\det(I_2+Z^*Z).
}
$$

$\mathbb CP^5$의 FS 퍼텐셜은 동차좌표 $q$에서 $\log\|q\|^2$다. Plücker 좌표를 대입하면

$$
\log\|q(Z)\|^2
=\log\det(I_2+Z^*Z)
=\Phi(Z).
$$

따라서

$$
\boxed{
g^{\mathrm{FS}}_{\mathrm{projector}}
=\text{Plücker 임베딩으로 당긴 }g^{\mathrm{FS}}_{\mathbb CP^5}.
}
$$

여기서 $\mathbb CP^5$가 metric을 새로 만들어 준 것이 아니다. projector에서 먼저 계산한 metric의 차트식이 $\log\det(I_2+Z^*Z)$였고, Cauchy--Binet가 그 같은 스칼라를 $\|q\|^2$라고 다시 읽어 준 것이다.

> **우회로에서 돌아온 자리.** [걸음 6b의 Cauchy--Binet 계산](걸음6_Gr24_플뤼커_완전판.html#plucker-cauchy-binet)을 마쳤다면 바로 위의 박스가 복귀점이다. 더 아래의 Ricci·부피·쌍대성은 지금 metric 비교에는 필요하지 않다.

§5의 한 칸 예시에서는 이 연결이 눈에 바로 보인다. 그때

$$
q(z)=(1,z,0,0,0,0),
\qquad
\|q(z)\|^2=1+|z|^2.
$$

즉 $Gr(2,4)$ 안의 그 CP¹은 Plücker 임베딩 뒤에서도 $[1:z:0:\cdots:0]$이라는 평범한 projective line이다.

### 7.3 metric의 옆에 있던 2-form은 어디서 다시 만나는가

방금 얻은 복소값 쌍선형식을

$$
h_Z(D,E)
:=\operatorname{tr}\!\left[
G^{-1}D^*H^{-1}E
\right]
$$

라고 쓰자. 실접벡터 $D,E$에 대해

$$
g_{\mathrm{FS}}(D,E)=\operatorname{Re}h_Z(D,E),
\qquad
\omega(D,E)=\operatorname{Im}h_Z(D,E).
$$

한 칸 예시에서는

$$
h=\frac{d\bar z\otimes dz}{S^2}.
$$

$z=x+iy$를 넣고 서로 다른 두 방향을 실제로 대입하면

$$
h(\partial_x,\partial_x)=\frac1{S^2},
\qquad
h(\partial_y,\partial_y)=\frac1{S^2},
\qquad
h(\partial_x,\partial_y)=\frac{i}{S^2}.
$$

따라서

$$
g_{\mathrm{FS}}
=\frac{dx^2+dy^2}{S^2},
\qquad
\omega
=\frac{dx\wedge dy}{S^2}
=\frac{i}{2}\frac{dz\wedge d\bar z}{S^2}.
$$

Reeb 계산은 별도의 경로에서, 단위 Plücker 벡터 $s=q/\sqrt{\|q\|^2}$와 $\alpha=-is^*ds$를 사용했다. 이 한 칸에서 국소 1-form은

$$
A=s^*\alpha
=\frac{i}{2}\frac{z\,d\bar z-\bar z\,dz}{S}.
$$

외미분하면

$$
dA
=i\frac{dz\wedge d\bar z}{S^2}
=2\frac{dx\wedge dy}{S^2}.
$$

그러므로 두 독립 계산이 마지막에

$$
\boxed{
\frac12dA=\omega=\operatorname{Im}h,
\qquad
g_{\mathrm{FS}}=\operatorname{Re}h
}
$$

로 만난다. 외미분 $d$가 metric을 만든 것도 아니고, 허수부가 trace 계산 중 사라진 것도 아니다. projector trace는 $h$의 실수부를 길이로 읽었고, Reeb 쪽의 $dA/2$는 같은 $h$의 허수부를 넓이로 읽었다.

---

## §8. trace 식은 출발점이었다

이제 다음 네 줄은 따로 놓인 사실이 아니다:

$$
\boxed{
\begin{aligned}
g_P^{\mathrm{FS}}(A,C)
&=\frac12\operatorname{tr}(AC),\\
g_Z^{\mathrm{FS}}(D,E)
&=\operatorname{Re}\operatorname{tr}\!\left[
(I_2+Z^*Z)^{-1}D^*(I_2+ZZ^*)^{-1}E
\right],\\
g_{u\bar v}^{\mathrm{FS}}
&=\partial_u\partial_{\bar v}log\det(I_2+Z^*Z),\\
g^{\mathrm{FS}}_{Gr(2,4)}
&=\text{Plücker로 당긴 }g^{\mathrm{FS}}_{\mathbb CP^5}.
\end{aligned}
}
$$

첫 줄은 projector들의 모임을 Hermitian 행렬공간 안에서 본 계산이고, 둘째 줄은 같은 계산을 $(I_2,Z)$ 차트로 쓴 것이며, 셋째 줄은 그 계수를 한 스칼라 퍼텐셜로 접은 것이고, 넷째 줄은 Cauchy--Binet로 그 스칼라가 Plücker 노름임을 알아본 것이다.

QFIM 정규화가 필요하면 이 전체 metric에 마지막으로 $4$를 곱한다:

$$
\boxed{
g^{\mathrm{QFI}}=4g^{\mathrm{FS}},
\qquad
g_P^{\mathrm{QFI}}(A,C)=2\operatorname{tr}(AC).
}
$$

계수 $4$는 rank가 $2$라서 생긴 것이 아니라, CP¹ 손노트에서 단위 Bloch 구면을 택했던 정규화를 그대로 유지한 결과다.
