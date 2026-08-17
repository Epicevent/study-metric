# 다항식 관계를 모르는 상태에서

## $S^2\simeq\mathbf{CP}^1$와 $\mathrm{Gr}(2,4)$, 두 토이모델

> **출발 질문.** 한 국소 차트에는 holomorphic function이 무한히 많다. $\mathrm{Gr}(2,4)$에서 Gaussian elimination을 하고 남는 $a,b,c,d$도, 외부 매개변수의 함수로 당겨 보면 $e^t,\sin t$ 같은 임의의 holomorphic function일 수 있다. 그렇다면 아직 아무 다항식 관계도 모르는 상태에서 무엇을 유한하게 골라 보고, 어떤 계산으로 관계를 발견하는가?
>
> **이 노트의 답.** line bundle 하나가 임의의 국소 함수를 다항식으로 바꾸는 것은 아니다. 실제 입력은
> $$
> (L,\;V),\qquad V\subset H^0(X,L)\text{ finite-dimensional}
> $$
> 이다. 한 section이 사라지지 않는 chart에서 $V$의 section들을 그 section으로 나누면 유한한 국소 함수족이 생긴다. 그 함수족이 정의하는 polynomial-ring map의 kernel을 계산하여 관계를 **처음부터 발견**한다. 관계를 homogenize하고 다른 chart로 확장하는 것은 그 다음 단계다.

이 노트는 두 개의 토이모델을 끝까지 나란히 민다.

- $S^2\simeq\mathbf{CP}^1$: winding, 두 chart의 gluing, $\mathcal O(k)$의 global section, $\mathcal O(2)$의 Veronese relation.
- $\mathrm{Gr}(2,4)$: Gaussian elimination, determinant line bundle, 여섯 maximal-minor section, local kernel, Plücker relation.

마지막에는 같은 기계가 relative Grassmannian과 Reineke tower에서 fiberwise 반복되는 지점까지 간다.

---

# 0. 무엇을 가정하고 무엇을 만들 것인가

이 노트는 다음만 가정한다.

1. 복소수와 $2\times2$ determinant.
2. 한 변수 holomorphic function의 Taylor 전개.
3. 행렬의 Gaussian elimination.
4. $1$-form, exterior derivative $d$, Stokes theorem.
5. 필요할 때 열린 덮개에 맞춘 partition of unity를 만들 수 있다는 사실.

Mayer–Vietoris, Chern class, section ring이라는 이름은 계산을 한 뒤 붙인다.

## 0.1 표기와 gluing convention

$\mathbf{CP}^1$의 표준 두 chart를

$$
U_0=\{X\neq0\},\qquad z=\frac{Y}{X},
$$

$$
U_\infty=\{Y\neq0\},\qquad w=\frac{X}{Y}=\frac1z
$$

로 잡는다. 이 노트에서 $\mathcal O(k)$의 local frame $e_0,e_\infty$는

$$
e_\infty=z^k e_0
$$

로 붙인다. 따라서 section

$$
s=f_0e_0=f_\infty e_\infty
$$

의 coefficient는

$$
f_\infty(w)=z^{-k}f_0(z)=w^k f_0(1/w)
$$

를 만족한다.

## 0.2 핵심 구분

이 노트 전체에서 다음 네 대상을 섞지 않는다.

1. 열린집합 위의 **임의의 holomorphic function**.
2. universal affine chart의 **좌표함수**.
3. line bundle의 **모든 local section**.
4. global section 가운데 선택한 **유한차원 section system**.

다항식 관계를 찾는 입력은 4번이다.

---

# I. 무한히 많은 함수에서 유한한 함수족으로

## 1. 임의의 local holomorphic function은 무한히 많다

열린집합 $U$ 위의

$$
\mathcal O(U)
$$

는 보통 무한차원이다. 임의의 네 함수

$$
a,b,c,d\in\mathcal O(U)
$$

사이에 비자명한 polynomial relation이 있을 이유는 없다.

예를 들어 $U=\mathbf C$에서

$$
a(t)=e^t,\qquad b(t)=\sin t,\qquad c(t)=t,\qquad d(t)=e^{t^2}
$$

를 잡을 수 있다. 이 함수들은 $t$에 대한 rational function일 필요가 없다.

따라서 다음 방식은 출발부터 잘못이다.

> local chart에서 임의의 holomorphic function 몇 개를 고르고, 그들 사이에 다항식 관계가 있으리라 기대한다.

## 2. universal chart의 좌표함수는 다른 말이다

$$
\mathbf A^4=\operatorname{Spec}\mathbf C[a,b,c,d]
$$

라고 쓸 때 $a,b,c,d$는 **추상적인 독립 좌표**다. 이것은 $a,b,c,d$가 어떤 외부 변수 $t$의 polynomial이라는 뜻이 아니다.

holomorphic family

$$
\phi:Y\longrightarrow\mathbf A^4
$$

를 잡으면 universal coordinate는

$$
a\mapsto a\circ\phi,\quad
b\mapsto b\circ\phi,\quad
c\mapsto c\circ\phi,\quad
d\mapsto d\circ\phi
$$

로 당겨진다. 당긴 함수들은 얼마든지 초월적일 수 있다.

따라서 두 문장은 동시에 참이다.

$$
\boxed{
\begin{aligned}
a,b,c,d&:\text{ universal chart에서는 독립 algebraic coordinates},\\
a\circ\phi,b\circ\phi,c\circ\phi,d\circ\phi
&:\text{ 한 analytic family에서는 임의의 holomorphic functions}.
\end{aligned}}
$$

## 3. line bundle의 모든 local section도 여전히 무한차원이다

$L\to X$가 line bundle이고 $e$가 $U\subset X$ 위의 nowhere-zero local frame이면

$$
\Gamma(U,L)=\mathcal O(U)e.
$$

즉 모든 local section은

$$
s=f e,\qquad f\in\mathcal O(U)
$$

로 쓸 수 있다. 따라서 line bundle을 도입했다고 local function의 무한한 자유도가 사라지는 것은 아니다.

$$
\boxed{
\text{line bundle 자체는 local holomorphic functions를 polynomial이나 rational function으로 만들지 않는다.}
}
$$

## 4. 유한한 section system이 좌표 후보를 고른다

실제로 사영좌표를 만드는 것은 line bundle $L$과 함께 고른 유한차원 공간

$$
V=\operatorname{span}\{s_0,\dots,s_N\}\subset H^0(X,L)
$$

이다.

$s_0\neq0$인 open set

$$
U_0=\{x\in X:s_0(x)\neq0\}
$$

에서는 $s_0$ 자체를 local frame으로 쓸 수 있다. 그러면

$$
s_i=y_i s_0,
\qquad
y_i=\frac{s_i}{s_0}\in\mathcal O(U_0).
$$

이제 무한히 많은 $\mathcal O(U_0)$ 전체가 아니라

$$
y_1,\dots,y_N
$$

이라는 유한 함수족이 생긴다.

이 함수들이 local map을 만든다.

$$
\varphi_0:U_0\longrightarrow\mathbf A^N,
\qquad
x\longmapsto(y_1(x),\dots,y_N(x)).
$$

아직 관계는 모른다. 관계는 다음 사상의 kernel로 **정의하고 계산한다**.

$$
\boxed{
\Phi_0:
\mathbf C[Y_1,\dots,Y_N]
\longrightarrow
\mathcal O(U_0),
\qquad
Y_i\longmapsto y_i.
}
$$

$$
\boxed{
I_0=\ker\Phi_0
=
\{\text{선택된 local ratio 함수들이 만족하는 polynomial relations}\}.
}
$$

두 토이모델에서는 target이 각각 $\mathbf C[z]$와 $\mathbf C[a,b,c,d]$이므로 kernel을 손으로 완전히 계산할 수 있다.

---

# II. 첫 번째 토이모델: $S^2\simeq\mathbf{CP}^1$

## 5. 두 chart를 붙여 line bundle을 만든다

$U_0\cap U_\infty\simeq\mathbf C^*$ 위의 nowhere-zero holomorphic function

$$
g(z):\mathbf C^*\longrightarrow\mathbf C^*
$$

를 잡고

$$
e_\infty=g(z)e_0
$$

로 두 trivial line bundle을 붙인다.

$\mathcal O(k)$에서는

$$
g(z)=z^k.
$$

적도 $|z|=1$에서 $z=e^{i\theta}$이므로

$$
g(e^{i\theta})=e^{ik\theta}.
$$

그 winding은

$$
\frac1{2\pi i}
\oint_{|z|=1}\frac{dg}{g}
=
\frac1{2\pi i}
\oint_{|z|=1}k\frac{dz}{z}
=k.
$$

아직 이 정수를 분류정리로 사용하지 않는다. 실제 gluing data에서 계산된 정수 하나로 기록한다.

## 6. global holomorphic section을 직접 전수조사한다

section을

$$
s=f_0(z)e_0=f_\infty(w)e_\infty
$$

로 쓰면

$$
f_\infty(w)=w^k f_0(1/w).
$$

$f_0$는 $\mathbf C$ 전체에서 holomorphic이므로 Taylor 전개가 있다.

$$
f_0(z)=\sum_{n=0}^{\infty}a_nz^n.
$$

따라서

$$
f_\infty(w)
=
w^k f_0(1/w)
=
\sum_{n=0}^{\infty}a_n w^{k-n}.
$$

### 6.1 $k\ge0$

$w=0$에서 holomorphic이려면 음의 지수가 없어야 한다. 즉

$$
a_n=0\qquad(n>k).
$$

그러므로

$$
f_0(z)=a_0+a_1z+\cdots+a_kz^k.
$$

따라서

$$
H^0(\mathbf{CP}^1,\mathcal O(k))
=
\operatorname{span}\{1,z,\dots,z^k\},
$$

$$
\dim H^0(\mathbf{CP}^1,\mathcal O(k))=k+1.
$$

homogeneous notation에서는 basis를

$$
X^k,X^{k-1}Y,\dots,Y^k
$$

로 쓸 수 있다.

### 6.2 $k<0$

모든 $n\ge0$에 대해 $k-n<0$이므로 $w=0$에서 holomorphic이 되려면 모든 $a_n$이 0이어야 한다.

$$
H^0(\mathbf{CP}^1,\mathcal O(k))=0.
$$

여기서 첫 번째 핵심 현상이 보인다.

$$
\boxed{
\text{각 chart의 holomorphic function은 무한히 많지만,
transition을 통과해 global section이 되는 함수는 유한차원이다.}
}
$$

---

# III. winding form이 $S^2$의 curvature가 되는 계산

이 절은 relation을 직접 찾는 데 논리적으로 필수는 아니다. 하지만 교수님이 강조한

$$
\text{winding}\longrightarrow\text{partition of unity}\longrightarrow\text{curvature}\longrightarrow c_1
$$

을 $S^2$에서 계산해 두면, 왜 같은 line bundle이 section과 curvature를 동시에 조직하는지가 보인다.

## 7. overlap의 closed winding form

$S^2$를 북쪽과 남쪽 open set으로 덮는다.

$$
S^2=U_N\cup U_S.
$$

overlap은 적도 주위의 band이고 deformation retract하면 $S^1$이다.

transition $g=e^{ik\theta}$에 대해 normalized winding form을

$$
\alpha_k
=
\frac1{2\pi i}g^{-1}dg
=
\frac{k}{2\pi}d\theta
$$

로 둔다. 그러면

$$
d\alpha_k=0,
\qquad
\int_{S^1}\alpha_k=k.
$$

## 8. partition of unity로 전역 $2$-form을 만든다

$$
\rho_N+\rho_S=1
$$

인 partition of unity를 잡는다. $\rho_N$은 북쪽에서 $1$, 남쪽에서 $0$이 되게 한다.

각 chart에서 normalized connection form을

$$
A_N=-\rho_S\alpha_k,
\qquad
A_S=\rho_N\alpha_k
$$

로 둔다.

overlap에서

$$
A_S-A_N
=(\rho_N+\rho_S)\alpha_k
=\alpha_k.
$$

이제 미분한다.

$$
\begin{aligned}
dA_N
&=-d\rho_S\wedge\alpha_k-\rho_Sd\alpha_k\\
&=d\rho_N\wedge\alpha_k,
\end{aligned}
$$

$$
dA_S=d\rho_N\wedge\alpha_k.
$$

따라서 두 식은 하나의 전역 $2$-form $F_k$로 붙는다.

$$
\boxed{
F_k|_{U_N}=dA_N,
\qquad
F_k|_{U_S}=dA_S.
}
$$

chosen orientation에서 band의 남쪽에서 북쪽으로 $\rho_N$이 $0$에서 $1$로 변하도록 잡으면

$$
\begin{aligned}
\int_{S^2}F_k
&=\int_{\text{band}}d\rho_N\wedge\alpha_k\\
&=\left(\int d\rho_N\right)
  \left(\int_{S^1}\alpha_k\right)\\
&=k.
\end{aligned}
$$

즉 같은 정수가 세 번 나온다.

$$
\boxed{
\operatorname{wind}(g)
=
\int_{S^1}\alpha_k
=
\int_{S^2}F_k
=k.
}
$$

이 계산을 cohomology 언어로 부르면 overlap의 $H^1$ class를 전역 $H^2$ class로 보내는 Mayer–Vietoris connecting map이다. 그러나 손계산 자체는 partition of unity와 Stokes theorem뿐이다.

## 9. connection과 first Chern class

local frame이 $e_S=ge_N$로 바뀔 때 connection form은

$$
A_S-A_N=\frac1{2\pi i}g^{-1}dg
$$

만큼 바뀐다. 반면 curvature

$$
F=dA
$$

는 전역으로 붙는다.

이 normalized convention에서는

$$
c_1(L)=[F]
$$

로 쓰며

$$
\langle c_1(\mathcal O(k)),[S^2]\rangle=k.
$$

다른 책에서 $i/(2\pi)$가 따로 붙는 것은 connection과 curvature를 $i\mathbf R$-값으로 잡기 때문이다. 본질은

$$
\boxed{
\text{transition의 winding}=\text{curvature의 적분}
}
$$

이다.

### 9.1 $T\mathbf{CP}^1$과 Gaussian curvature

좌표변환 $w=1/z$에서

$$
\frac{\partial}{\partial w}
=
\frac{dz}{dw}\frac{\partial}{\partial z}
=
-z^2\frac{\partial}{\partial z}.
$$

따라서 tangent bundle의 transition은 winding $2$를 갖는다.

$$
T\mathbf{CP}^1\simeq\mathcal O(2).
$$

이 특별한 bundle의 Levi–Civita/Chern curvature는 Gaussian curvature $2$-form $K\,dA$로 읽힌다. 일반 line bundle의 curvature를 항상 Gaussian curvature라고 부르는 것은 아니다.

---

# IV. 관계를 모른 채 찾는 첫 예: $\mathcal O(2)$

## 10. 세 section이 만드는 map

$$
H^0(\mathbf{CP}^1,\mathcal O(2))
=
\operatorname{span}\{X^2,XY,Y^2\}.
$$

세 section을 동시에 평가하면

$$
\nu_2:\mathbf{CP}^1\longrightarrow\mathbf P^2,
\qquad
[X:Y]\longmapsto[X^2:XY:Y^2]
$$

를 얻는다.

여기서는 image의 방정식을 모른다고 가정한다.

## 11. 한 chart에서 유한한 함수족을 내린다

$X\neq0$인 chart에서 $X^2$를 local frame으로 쓰면

$$
\frac{X^2}{X^2}=1,
\qquad
\frac{XY}{X^2}=z,
\qquad
\frac{Y^2}{X^2}=z^2.
$$

따라서 affine map은

$$
\phi_0:\mathbf A^1\longrightarrow\mathbf A^2,
\qquad
z\longmapsto(u,v)=(z,z^2)
$$

이다.

## 12. degree를 올려가며 relation을 검색한다

### 12.1 linear relation

$$
A+Bu+Cv=0
$$

에 $u=z,v=z^2$를 넣으면

$$
A+Bz+Cz^2=0.
$$

모든 $z$에서 0이려면

$$
A=B=C=0.
$$

linear relation은 없다.

### 12.2 quadratic relation

homogeneous quadratic을 전부 적는다.

$$
P(Z_0,Z_1,Z_2)
=
A Z_0^2+B Z_0Z_1+C Z_0Z_2
+D Z_1^2+E Z_1Z_2+F Z_2^2.
$$

$$
(Z_0,Z_1,Z_2)=(1,z,z^2)
$$

를 넣으면

$$
P(1,z,z^2)
=
A+Bz+(C+D)z^2+Ez^3+Fz^4.
$$

모든 $z$에서 0이려면

$$
A=B=E=F=0,
\qquad
C+D=0.
$$

따라서 quadratic relation 공간은 한 차원이고

$$
\boxed{
Z_0Z_2-Z_1^2=0.
}
$$

관계를 미리 주어 놓고 검산한 것이 아니다. 가능한 quadratic의 coefficient를 모두 놓고 kernel을 계산했다.

## 13. affine kernel 전체를 계산한다

ring map을

$$
\Psi_0:\mathbf C[U,V]\longrightarrow\mathbf C[z],
\qquad
U\mapsto z,
\quad
V\mapsto z^2
$$

로 둔다.

임의의 polynomial $P(U,V)$를 $V-U^2$로 나누면

$$
P(U,V)=Q(U,V)(V-U^2)+R(U)
$$

로 쓸 수 있다. $P(z,z^2)=0$이면

$$
R(z)=0
$$

이므로 $R=0$. 따라서

$$
\boxed{
\ker\Psi_0=(V-U^2).
}
$$

## 14. 그 다음에 homogenize하고 다른 chart를 본다

$$
U=\frac{Z_1}{Z_0},
\qquad
V=\frac{Z_2}{Z_0}
$$

를 넣고 $Z_0^2$를 곱하면

$$
Z_0Z_2-Z_1^2=0.
$$

$Y\neq0$ chart에서는 $w=X/Y$이고 $Y^2$를 frame으로 쓰므로 section ratio는

$$
w^2,w,1.
$$

같은 식은

$$
w^2\cdot1-w^2=0
$$

이 된다. local하게 발견한 homogeneous relation이 다른 chart에서도 같은 식으로 살아남는다.

---

# V. 두 번째 토이모델: $\mathrm{Gr}(2,4)$

## 15. 행렬과 Gaussian elimination

$\mathrm{Gr}(2,4)$의 점은 $\mathbf C^4$ 안의 $2$-평면이다. 기저를 두 행으로 놓으면 full-rank matrix

$$
A\in M_{2\times4}(\mathbf C)
$$

를 얻는다. 행 기저를 바꾸면

$$
A\longmapsto gA,
\qquad
g\in GL(2,\mathbf C)
$$

가 된다.

첫 두 열의 minor가 0이 아닌 chart에서는 Gaussian elimination으로

$$
A\sim
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

로 유일하게 만들 수 있다. 따라서

$$
U_{12}\simeq\mathbf A^4
$$

이고

$$
a,b,c,d
$$

는 독립 좌표다.

$$
\boxed{
\text{$a,b,c,d$ 사이에는 비자명한 polynomial relation이 없다.}
}
$$

## 16. 왜 이 좌표는 “rational이면서 rational이 아닐 수 있는가”

Grassmannian 전체의 Plücker coordinate를 쓰면 $U_{12}$에서

$$
a=-\frac{p_{23}}{p_{12}},
\qquad
b=-\frac{p_{24}}{p_{12}},
\qquad
c=\frac{p_{13}}{p_{12}},
\qquad
d=\frac{p_{14}}{p_{12}}.
$$

따라서 $a,b,c,d$는 **Grassmannian 위에서는** rational functions이고, $p_{12}\neq0$인 chart에서는 regular functions다.

하지만 holomorphic family

$$
\phi:Y\longrightarrow U_{12}
$$

를 잡으면

$$
a\circ\phi,b\circ\phi,c\circ\phi,d\circ\phi
$$

는 $Y$ 위의 임의의 holomorphic functions일 수 있다. 예를 들어

$$
a(t)=e^t,
\qquad
b(t)=\sin t,
\qquad
c(t)=t,
\qquad
d(t)=e^{-t}
$$

도 허용된다.

그러므로 다음 추론은 틀렸다.

> Gaussian elimination 뒤의 네 함수가 외부 변수에 대한 rational functions이기 때문에 relation이 생긴다.

관계는 네 자유함수 사이에서 찾는 것이 아니다.

---

# VI. determinant line bundle이 유한한 section system을 고른다

## 17. tautological bundle

$$
\mathcal S\longrightarrow\mathrm{Gr}(2,4)
$$

를

$$
\mathcal S_W=W
$$

로 정의한다. fiber가 $2$-차원이므로 rank $2$ bundle이다.

그 determinant의 dual을

$$
L_{\mathrm{Pl}}
=
\det\mathcal S^*
=
\bigwedge^2\mathcal S^*
$$

로 둔다.

## 18. 여섯 canonical global sections

표준 dual basis $e_1^*,\dots,e_4^*$에서

$$
e_i^*\wedge e_j^*
\in
\bigwedge^2(\mathbf C^4)^*
$$

를 잡는다. 이를 각 평면 $W$에 제한하면

$$
s_{ij}(W)
=(e_i^*\wedge e_j^*)|_{\wedge^2W}
\in
(\det\mathcal S^*)_W
$$

가 된다.

따라서 여섯 global section

$$
s_{12},s_{13},s_{14},s_{23},s_{24},s_{34}
$$

이 생긴다. 이 노트에서는 이들이 모든 global section을 소진한다는 정리까지 필요하지 않다. 여섯 section이 만드는 유한차원 공간

$$
V_{\mathrm{Pl}}
=\operatorname{span}\{s_{ij}\}
\subset H^0(\mathrm{Gr}(2,4),L_{\mathrm{Pl}})
$$

만 사용한다.

평면의 기저를 행으로 놓은 $A$에서 이 section을 평가하면 maximal minor가 나온다.

$$
p_{ij}(A)=\det A_{\{i,j\}}.
$$

여기서 determinant의 역할은 relation을 미리 알려주는 것이 아니다.

$$
\boxed{
\text{determinant는 무한히 많은 local sections 가운데 볼 만한 여섯 canonical global sections를 고른다.}
}
$$

---

# VII. 한 chart에서 Plücker relation을 처음부터 발견한다

## 19. $p_{12}$를 local frame으로 쓴다

$U_{12}=\{p_{12}\neq0\}$에서는 $s_{12}$가 사라지지 않으므로 local frame으로 쓸 수 있다.

Gaussian elimination된 matrix

$$
A=
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

의 모든 $2\times2$ minor를 계산한다.

$$
p_{12}=1,
$$

$$
p_{13}=c,
\qquad
p_{14}=d,
$$

$$
p_{23}=-a,
\qquad
p_{24}=-b,
$$

$$
p_{34}=ad-bc.
$$

따라서 section ratio는

$$
x_{13}=\frac{p_{13}}{p_{12}}=c,
\quad
x_{14}=d,
\quad
x_{23}=-a,
\quad
x_{24}=-b,
\quad
x_{34}=ad-bc.
$$

유한한 affine map이 생긴다.

$$
\Phi:\mathbf A^4\longrightarrow\mathbf A^5,
$$

$$
(a,b,c,d)
\longmapsto
(c,d,-a,-b,ad-bc).
$$

## 20. 네 자유좌표를 먼저 회수한다

출력의 처음 네 좌표로 입력을 복원할 수 있다.

$$
a=-x_{23},
\qquad
b=-x_{24},
\qquad
c=x_{13},
\qquad
d=x_{14}.
$$

따라서 다섯 번째 출력은

$$
\begin{aligned}
x_{34}
&=ad-bc\\
&=(-x_{23})x_{14}-(-x_{24})x_{13}\\
&=x_{13}x_{24}-x_{14}x_{23}.
\end{aligned}
$$

그러므로 image는 $\mathbf A^5$ 안의 graph

$$
\boxed{
x_{34}-x_{13}x_{24}+x_{14}x_{23}=0
}
$$

위에 놓인다.

이 식은 $a,b,c,d$를 제약하지 않는다. 네 개의 자유입력으로부터 생긴 **다섯 번째 ambient coordinate**를 결정한다.

## 21. 이 식이 local ideal 전체임을 증명한다

ring map을

$$
\Psi:
\mathbf C[X_{13},X_{14},X_{23},X_{24},X_{34}]
\longrightarrow
\mathbf C[a,b,c,d]
$$

로 두고

$$
X_{13}\mapsto c,
\quad
X_{14}\mapsto d,
\quad
X_{23}\mapsto-a,
\quad
X_{24}\mapsto-b,
\quad
X_{34}\mapsto ad-bc
$$

로 보낸다.

임의의 polynomial $P$를 $X_{34}$에 대한 polynomial로 보고

$$
G=X_{34}-X_{13}X_{24}+X_{14}X_{23}
$$

로 나누면

$$
P=QG+R(X_{13},X_{14},X_{23},X_{24})
$$

로 쓸 수 있다.

$\Psi(P)=0$이면 $\Psi(G)=0$이므로

$$
R(c,d,-a,-b)=0.
$$

그런데 $a,b,c,d$는 독립 좌표다. 따라서

$$
R=0.
$$

그러므로

$$
\boxed{
\ker\Psi
=
\bigl(
X_{34}-X_{13}X_{24}+X_{14}X_{23}
\bigr).
}
$$

relation을 알고 시작한 것이 아니다. graph map의 kernel을 직접 계산했다.

## 22. 그 다음에 homogenize한다

$$
x_{ij}=\frac{p_{ij}}{p_{12}}
$$

를 넣고

$$
x_{34}-x_{13}x_{24}+x_{14}x_{23}=0
$$

에 $p_{12}^2$를 곱하면

$$
\boxed{
p_{12}p_{34}
-p_{13}p_{24}
+p_{14}p_{23}
=0.
}
$$

각 항은 degree $2$이고, row basis change $A\mapsto gA$ 아래 모든 $p_{ij}$가 $\det g$만큼 함께 변한다. 따라서 식 전체는 $(\det g)^2$만큼 변하며 “0이다”라는 명제는 basis와 chart에 무관하다.

계산 순서는 분명하다.

$$
\boxed{
\text{local section ratio}
\to
\text{affine map}
\to
\text{kernel}
\to
\text{homogenization}
\to
\text{global relation}.
}
$$

---

# VIII. 초월적인 holomorphic family와 universal relation

## 23. 초월함수를 대입해도 relation은 유지된다

universal chart에서는

$$
x_{34}-x_{13}x_{24}+x_{14}x_{23}=0
$$

가 coordinate-ring identity다.

이제 $Y$ 위의 arbitrary holomorphic family를 대입한다.

$$
a=a(y),\quad b=b(y),\quad c=c(y),\quad d=d(y).
$$

그러면

$$
\begin{aligned}
&x_{34}(y)-x_{13}(y)x_{24}(y)+x_{14}(y)x_{23}(y)\\
&=(a(y)d(y)-b(y)c(y))
-c(y)(-b(y))
+d(y)(-a(y))\\
&=0.
\end{aligned}
$$

$a(y),b(y),c(y),d(y)$가 rational인지 아닌지는 무관하다. universal polynomial identity는 임의의 function substitution 아래에서도 유지된다.

## 24. 한 family만 보면 extra relation이 생길 수 있다

예를 들어

$$
a(t)=t,
\qquad
b(t)=0,
\qquad
c(t)=0,
\qquad
d(t)=t
$$

인 한 곡선만 보면

$$
x_{13}=0,
\qquad
x_{24}=0,
\qquad
x_{14}+x_{23}=0
$$

같은 추가 relation도 생긴다.

이것은 $\mathrm{Gr}(2,4)$ 전체의 relation이 아니라 그 한 곡선이 더 작은 subvariety에 놓인 결과다.

따라서 universal relation을 찾으려면 한 parameterized family가 아니라

$$
U_{12}\simeq\mathbf A^4
$$

전체에서 계산해야 한다.

---

# IX. line bundle의 역할을 정확히 고정한다

## 25. line bundle이 하지 않는 일

line bundle은

- arbitrary local holomorphic function을 rational function으로 만들지 않는다.
- $a,b,c,d$ 사이에 relation을 강제로 만들지 않는다.
- Plücker relation을 자동으로 알려주지 않는다.

## 26. line bundle과 section system이 실제로 하는 일

쌍

$$
(L,V),
\qquad
V\subset H^0(X,L)
$$

는

1. 서로 다른 chart에서 같은 geometric data를 표현하는 section들을 묶고,
2. 한 section이 사라지지 않는 곳에서 유한한 ratio 함수들을 만들며,
3. 같은 degree의 homogeneous relation이 frame change 아래에서도 의미 있게 남도록 한다.

frame을

$$
e'=ge
$$

로 바꾸면 section coefficient는

$$
f_i'=g^{-1}f_i
$$

로 함께 변한다. degree $d$ homogeneous polynomial $P$는

$$
P(f_0',\dots,f_N')
=g^{-d}P(f_0,\dots,f_N)
$$

로 변한다. 따라서

$$
P(f_0,\dots,f_N)=0
$$

이라는 명제는 frame에 무관하다.

관계를 실제로 만드는 원인은 각 예에서 다르다.

- $\mathcal O(2)$: $1,z,z^2$의 multiplication.
- $\mathrm{Gr}(2,4)$: maximal minors와 $2\times2$ determinant.
- 일반 Grassmannian: decomposable wedge가 만족하는 quadratic identities.

---

# X. section ring: 관계를 찾는 일반 기계

## 27. degree별 multiplication map

$$
V\subset H^0(X,L)
$$

를 잡는다. degree $d$ homogeneous polynomial은 section들의 곱으로

$$
\mu_d:
\operatorname{Sym}^d V
\longrightarrow
H^0(X,L^d)
$$

를 만든다.

$$
\boxed{
\ker\mu_d
=
\text{degree $d$ homogeneous relations among the chosen sections}.
}
$$

relation을 모를 때는

$$
d=1,2,3,\dots
$$

순서로 kernel을 조사한다.

## 28. $\mathcal O(2)$에서 dimension count를 실제로 본다

$$
V=H^0(\mathbf{CP}^1,\mathcal O(2))
$$

는 dimension $3$이므로

$$
\dim\operatorname{Sym}^2V=6.
$$

반면

$$
H^0(\mathbf{CP}^1,\mathcal O(4))
$$

의 dimension은 $5$다. multiplication map

$$
\mu_2:\operatorname{Sym}^2H^0(\mathcal O(2))
\longrightarrow H^0(\mathcal O(4))
$$

에는 적어도 한 차원의 kernel이 있어야 한다.

실제로

$$
(X^2)(Y^2)-(XY)^2=0
$$

가 그 kernel을 생성한다.

## 29. section ring

모든 degree를 합치면

$$
R(X,L)
=
\bigoplus_{d\ge0}H^0(X,L^d)
$$

을 얻는다.

선택한 $V$가 만드는 polynomial ring에서 section ring으로 가는 map

$$
\operatorname{Sym}^{\bullet}V
\longrightarrow
R(X,L)
$$

의 kernel이 projective image의 homogeneous ideal이다.

$$
\boxed{
I(X\hookrightarrow\mathbf P(V^*))
=
\ker\bigl(
\operatorname{Sym}^{\bullet}V
\to
R(X,L)
\bigr).
}
$$

이 식은 relation을 이미 안다는 뜻이 아니다. **무엇의 kernel을 계산해야 하는지**를 정확히 고정한다는 뜻이다.

---

# XI. 같은 line bundle에서 metric과 curvature가 나온다

## 30. $\mathbf{CP}^1$의 $\mathcal O(1)$

$U_0$에서 Fubini–Study Hermitian metric을

$$
h_0(z)=\frac1{1+|z|^2}
$$

로 잡는다.

Chern curvature convention을

$$
F=-\partial\bar\partial\log h
$$

로 잡으면

$$
F_{\mathcal O(1)}
=
\partial\bar\partial\log(1+|z|^2).
$$

$\mathcal O(k)$에서는 tensor power에 의해

$$
h_k=h_0^k,
$$

$$
F_{\mathcal O(k)}=kF_{\mathcal O(1)}.
$$

normalized integral은 앞의 winding $k$와 같은 정수를 준다.

## 31. $\mathrm{Gr}(2,4)$의 Plücker line bundle

chart matrix를

$$
A=(I_2\;Z),
\qquad
Z=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
$$

로 쓴다.

두 row vector $v_1,v_2$의 Gram matrix는

$$
G=AA^*=I_2+ZZ^*.
$$

wedge의 norm은 Gram determinant다.

$$
\|v_1\wedge v_2\|^2
=
\det G.
$$

따라서 dual determinant line bundle의 local frame metric은

$$
h_{\mathrm{Pl}}
=
\frac1{\det(I_2+ZZ^*)}.
$$

그 curvature는

$$
\boxed{
F_{\mathrm{Pl}}
=
\partial\bar\partial
\log\det(I_2+ZZ^*).
}
$$

한편 $2\times4$ Cauchy–Binet identity에 의해

$$
\det(AA^*)
=
\sum_{i<j}|p_{ij}|^2.
$$

따라서

$$
F_{\mathrm{Pl}}
=
\partial\bar\partial
\log\sum_{i<j}|p_{ij}|^2.
$$

오른쪽은 Plücker embedding으로 당긴 Fubini–Study curvature다.

$$
\boxed{
F_{\mathrm{Pl}}
=
\iota_{\mathrm{Pl}}^*F_{\mathrm{FS}}.
}
$$

$S^2$에서 transition의 winding을 curvature로 올린 기계와, Grassmannian에서 determinant section의 norm으로 curvature를 만든 기계가 여기서 만난다.

---

# XII. 두 토이모델은 왜 정확히 같은 역할을 하는가

| 항목 | $S^2\simeq\mathbf{CP}^1$ | $\mathrm{Gr}(2,4)$ |
|---|---|---|
| 자유 chart 좌표 | $z$ | $a,b,c,d$ |
| 자연한 line bundle | $\mathcal O(2)$ | $\det\mathcal S^*$ |
| 선택된 section 수 | $3$ | $6$ |
| nonzero section으로 나눈 함수 | $1,z,z^2$ | $1,c,d,-a,-b,ad-bc$ |
| affine ambient dimension | $2$ | $5$ |
| source dimension | $1$ | $4$ |
| 처음 발견하는 local 식 | $v-u^2=0$ | $x_{34}-x_{13}x_{24}+x_{14}x_{23}=0$ |
| homogeneous 식 | $Z_0Z_2-Z_1^2=0$ | $p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0$ |
| curvature의 원천 | transition winding | Gram determinant / Plücker norm |
| 다음 일반화 | $\mathcal O(k)$, Veronese | relative Plücker, Reineke tower |

두 경우 모두 source보다 ambient projective space의 dimension이 하나 크다.

$$
\dim\mathbf{CP}^1=1,
\qquad
\dim\mathbf P^2=2,
$$

$$
\dim\mathrm{Gr}(2,4)=4,
\qquad
\dim\mathbf P^5=5.
$$

따라서 둘 다 hypersurface 하나로 닫히는 특별히 깨끗한 toy model이다. 일반 projective variety에서는 codimension만큼의 equation으로 끝나지 않을 수 있고, ideal이 higher-degree generator와 syzygy를 가질 수 있다.

---

# XIII. Relative Grassmannian과 Reineke tower로 올라가기

## 32. vector space를 vector bundle로 바꾼다

$E\to X$가 rank $N$ vector bundle이면

$$
\operatorname{Gr}_X(k,E)
=
\{(x,U):U\subset E_x,\ \dim U=k\}
$$

를 만든다.

각 fiber는 ordinary Grassmannian이다.

$$
\pi^{-1}(x)\simeq\operatorname{Gr}(k,E_x).
$$

relative tautological bundle을 $\mathcal S$라 하면

$$
L_{\mathrm{rel}}
=
\det\mathcal S^*
$$

가 relative Plücker line bundle이다.

$E$를 한 open set에서 trivialize하면

$$
\operatorname{Gr}_X(k,E)|_U
\simeq
U\times\operatorname{Gr}(k,N).
$$

따라서 ordinary Grassmannian에서 한 계산이 fiber마다 그대로 작동한다.

- Gaussian elimination.
- maximal-minor sections.
- local polynomial kernel.
- determinant metric과 curvature.

그 다음 base chart change가 이 fiberwise 계산을 전역으로 붙인다.

## 33. Reineke tower

acyclic quiver에서는 이전 단계의 tautological bundles로 다음 ambient bundle $E_r$를 만들고

$$
X_r
=
\operatorname{Gr}_{X_{r-1}}(d_r,E_r)
$$

를 반복한다.

그러므로 tower의 각 단계는

$$
\boxed{
\text{$S^2$에서 익힌 line-bundle gluing}
+
\text{$\mathrm{Gr}(2,4)$에서 익힌 fiberwise Plücker model}
}
$$

의 반복이다.

각 단계의 Plücker determinant line bundle curvature를 조합하면 twisted tower Kähler metric으로 넘어간다.

---

# XIV. relation을 모를 때 사용하는 실제 절차

## 34. 계산 절차

1. 대상 $X$를 local coordinates로 parameterize한다.
2. arbitrary local functions 전체를 보지 않는다.
3. natural line bundle $L$를 찾는다.
4. finite-dimensional section system
   $$
   V\subset H^0(X,L)
   $$
   을 고른다.
5. $s_0\neq0$인 chart에서
   $$
   y_i=s_i/s_0
   $$
   를 계산한다.
6. affine map
   $$
   U_0\to\mathbf A^N
   $$
   을 적는다.
7. polynomial-ring map의 kernel을 degree $1,2,3,\dots$ 순서로 계산한다.
8. local relation이 ideal 전체를 생성하는지 증명한다.
9. homogenize한다.
10. frame change와 다른 chart에서 같은 homogeneous relation인지 확인한다.
11. Hermitian metric과 curvature를 계산한다.
12. vector bundle base 위에서는 이 과정을 fiberwise 반복한다.

## 35. 실패 검문

다음 중 하나를 하면 핀트가 어긋난다.

- $a,b,c,d$ 자체의 relation을 찾으려 한다.
- 외부 parameter $t$에 대한 rationality를 요구한다.
- 모든 local section과 선택된 finite global section system을 섞는다.
- 알려진 Plücker relation을 먼저 쓰고 뒤에서 정당화한다.
- local relation 발견과 global extension을 한 문장으로 합친다.
- 한 holomorphic family에서 생긴 우연한 extra relation을 universal ideal로 착각한다.
- determinant가 relation을 자동으로 준다고 말한다. determinant는 먼저 canonical sections를 준다.

---

# XV. 손계산 문제

## 문제 1 — $\mathcal O(3)$의 section

두 chart 접합식으로

$$
H^0(\mathbf{CP}^1,\mathcal O(3))
$$

의 basis를 직접 구하여라.

<details>
<summary>답</summary>

$$
1,z,z^2,z^3.
$$

homogeneous notation에서는

$$
X^3,X^2Y,XY^2,Y^3.
$$
</details>

## 문제 2 — $\mathcal O(-2)$

같은 계산으로 nonzero global holomorphic section이 없음을 보여라.

<details>
<summary>답</summary>

$$
f_\infty(w)=w^{-2}f_0(1/w)
$$

가 $w=0$에서 holomorphic이려면 $f_0$의 모든 Taylor coefficient가 0이어야 한다.
</details>

## 문제 3 — POU curvature

$$
A_N=-\rho_S\alpha_k,
\qquad
A_S=\rho_N\alpha_k
$$

에서

$$
dA_N=dA_S
$$

를 한 줄씩 확인하여라.

## 문제 4 — Veronese linear relation

$$
1,z,z^2
$$

사이에 nonzero linear relation이 없음을 coefficient comparison으로 보여라.

## 문제 5 — Veronese quadratic relation

일반 homogeneous quadratic을 대입하여 relation 공간이 한 차원임을 다시 계산하여라.

## 문제 6 — Grassmannian의 여섯 minor

$$
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

의 모든 $2\times2$ minor를 부호까지 계산하여라.

## 문제 7 — graph ideal

$$
\mathbf C[X_1,\dots,X_5]
\to
\mathbf C[u_1,\dots,u_4],
$$

$$
X_i\mapsto u_i\;(i\le4),
\qquad
X_5\mapsto f(u_1,\dots,u_4)
$$

의 kernel이

$$
(X_5-f(X_1,\dots,X_4))
$$

임을 polynomial division으로 증명하여라.

## 문제 8 — transcendental family 대입

$$
a=e^t,
\quad
b=\sin t,
\quad
c=t,
\quad
d=e^{-t}
$$

를 Plücker coordinate에 넣고 relation이 항등적으로 0인지 확인하여라.

## 문제 9 — 우연한 extra relation

$$
a=t,
\quad
b=0,
\quad
c=0,
\quad
d=t
$$

인 family에서 universal Plücker relation 외에 어떤 linear relations가 추가되는지 찾아라.

## 문제 10 — Gram determinant

두 row vector $v_1,v_2$에 대해

$$
\|v_1\wedge v_2\|^2
=
\det(\langle v_i,v_j\rangle)
$$

를 성분 전개로 증명하여라.

## 문제 11 — Cauchy–Binet

$$
A=(I_2\;Z)
$$

에 대해

$$
\det(AA^*)=\sum_{i<j}|p_{ij}|^2
$$

를 $2\times4$ 행렬에서 직접 전개하여라.

## 문제 12 — section multiplication

$\mathcal O(2)$의 세 basis section의 degree $2$ monomial 여섯 개를 적고, $\mathcal O(4)$의 basis 다섯 개에 보내지는 multiplication map의 kernel dimension을 계산하여라.

<details>
<summary>답</summary>

$$
\dim\operatorname{Sym}^2H^0(\mathcal O(2))=6,
\qquad
\dim H^0(\mathcal O(4))=5.
$$

kernel은 한 차원이고 generator는

$$
(X^2)(Y^2)-(XY)^2.
$$
</details>

## 문제 13 — 다른 Plücker chart

$p_{13}\neq0$인 chart에서 pivot columns를 $1,3$으로 잡아 echelon form을 만들고, 나머지 Plücker ratio를 네 자유좌표로 표현하여라. 마지막에 같은 homogeneous quadratic이 나타나는지 확인하여라.

## 문제 14 — 한 family와 universal space

holomorphic map

$$
\phi:\mathbf C\to U_{12}\simeq\mathbf A^4
$$

의 image가 Zariski dense일 수도 있고 아닐 수도 있다. 다음 두 예의 Zariski closure를 비교하여라.

$$
\phi_1(t)=(t,t^2,t^3,t^4),
$$

$$
\phi_2(t)=(e^t,e^{\sqrt2t},e^{\sqrt3t},e^{\sqrt5t}).
$$

첫 예에는 명백한 polynomial relations가 있다. 둘째 예에서는 어떤 종류의 독립성 문제가 등장하는지 서술하여라.

---

# XVI. 마지막 압축

처음부터 relation을 알고 있지 않다.

$S^2\simeq\mathbf{CP}^1$에서는

1. transition의 winding이 $\mathcal O(k)$를 고른다.
2. gluing condition이 무한한 local holomorphic functions를 유한한 global section space로 줄인다.
3. $\mathcal O(2)$의 세 section을 한 chart에 내린다.
4. polynomial-ring map의 kernel을 계산하여 conic relation을 찾는다.

$\mathrm{Gr}(2,4)$에서는

1. Gaussian elimination 뒤의 $a,b,c,d$는 자유좌표다.
2. determinant line bundle이 여섯 canonical sections를 고른다.
3. $p_{12}\neq0$ chart에서 section ratios를 계산한다.
4. $\mathbf A^4\to\mathbf A^5$ graph map의 kernel을 계산한다.
5. 마지막에 homogenize하여 Plücker relation을 얻는다.

따라서 두 toy model을 관통하는 문장은 다음이다.

$$
\boxed{
\text{무한한 local function 전체에서 relation을 찾는 것이 아니다.}
}
$$

$$
\boxed{
\text{line bundle의 유한한 section system을 local functions로 내린 뒤,
그 map의 kernel을 계산한다.}
}
$$

그리고 이 기계가 relative Grassmannian의 fiber마다 반복되면서 Reineke tower로 올라간다.

---

## 준거 자료와 이 노트의 역할

기존 자료는 Gaussian elimination으로 affine chart를 만들고, maximal minors를 Plücker coordinates로 기록한 뒤, $\mathrm{Gr}(2,4)$에서 구체적인 quadratic relation을 제시하고 relative Grassmannian과 Reineke tower로 올라간다. 이 노트는 그 계산을 대체하지 않는다. 같은 계산을 두고 질문의 방향을 바꾼다.

> relation을 이미 아는 상태에서 확인하는 대신, relation을 모르는 상태에서 왜 유한한 함수족을 선택하고 어떻게 kernel로 발견하는가?

이 역방향 질문을 $S^2\simeq\mathbf{CP}^1$와 $\mathrm{Gr}(2,4)$ 두 토이모델에서 자립적으로 닫는 것이 이 노트의 목적이다.
