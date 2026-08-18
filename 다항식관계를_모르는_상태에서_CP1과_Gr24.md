# 다항식 관계를 모르는 상태에서

## 왜 RREF·projector·Plücker 중 하나를 고르는가

> **출발 질문.** $\mathbf{CP}^1$에서는 $q\sim\lambda q$, Grassmannian에서는 frame $A\sim gA$라는 중복이 있다. 그런데 이 중복은 normalization이나 projection matrix로 이미 정확히 제거할 수 있다. 그렇다면 왜 다시 line bundle, section, maximal minor, Plücker coordinate를 생각하는가? 왜 하필 그 관측량들을 고르며, 그 뒤에 polynomial ring과 kernel을 만드는가?
>
> **답의 골자.** Plücker를 고르는 이유는 중복을 제거하지 못해서도, projector보다 정보를 더 많이 담아서도 아니다. RREF, projector, Plücker는 모두 원래 점을 복원한다. 다만 각각이 다른 종류의 계산을 가능하게 한다.
>
> $$
> \boxed{
> \begin{array}{ccl}
> \text{RREF} &:& \text{국소 holomorphic·algebraic 좌표},\\
> \text{projector} &:& \text{전역 Hermitian·metric·QFIM 계산},\\
> \text{Plücker} &:& \text{전역 holomorphic·polynomial·projective 계산}.
> \end{array}}
> $$
>
> polynomial ring과 kernel은 **마지막 단계**다. 먼저 어떤 범주에서 무엇을 관찰하려는지 정하고, 그 목적에 맞는 완전한 관측량을 고른 뒤에야 그 관측량 사이의 관계를 kernel로 모은다.

이 노트는 다음 빈틈을 닫는다.

1. 같은 공간을 표현하는 세 방식이 실제로 같은 정보를 담는지 확인한다.
2. projector가 이미 $\lambda$와 $G$의 중복을 제거하는데도 Plücker가 필요한 이유를 계산한다.
3. determinant line bundle과 maximal minor가 임의의 선택이 아니라 어떻게 나오는지 보인다.
4. 그 뒤에야 relation을 모르는 상태에서 polynomial kernel을 계산한다.
5. 마지막으로 relative Grassmannian과 Reineke tower에서 왜 Plücker가 구조적 본선인지 설명한다.

---

# 0. 자료에서 주어진 것과 이 노트가 추가하는 것

기존 Grassmannian 자료의 순서는 다음이다.

$$
\text{행렬 quotient}
\longrightarrow
\text{Gaussian elimination과 affine chart}
\longrightarrow
\text{maximal minor}
\longrightarrow
\text{Plücker embedding}
\longrightarrow
\text{relative Grassmannian과 Reineke tower}.
$$

그 자료는 이 흐름 자체를 제공한다. 이 노트가 추가하는 질문은 하나다.

> Gaussian elimination도, normalized projector도 이미 같은 평면을 완전히 기록한다. 그럼에도 왜 projective algebraic geometry에서는 wedge와 Plücker를 골라야 하는가?

projector와 Plücker의 비교, 그리고 “관측량을 고르는 법”은 기존 자료의 문장을 반복하는 것이 아니라 그 사이의 논리적 빈틈을 메우기 위한 추가 설명이다.

---

# 1. 무엇을 가정하는가

이 노트는 다음만 가정한다.

- 복소수, 행렬곱, determinant, Gaussian elimination.
- Hermitian inner product와 adjoint $A^\dagger$.
- holomorphic function에 $\bar z$가 나타나면 일반적으로 holomorphic하지 않다는 사실.
- exterior product $v\wedge w$의 bilinearity와 alternating 성질.
- $1$-form, exterior derivative $d$, Stokes theorem.

Mayer–Vietoris, Chern class, section ring, projective morphism이라는 이름은 계산 뒤에 붙인다.

## 1.1 row convention과 column convention

Grassmannian의 행렬표현은 두 convention이 모두 쓰인다.

- **row frame:** full-rank $2\times4$ matrix의 row space를 본다.
- **column frame:** full-rank $4\times2$ matrix의 column space를 본다.

둘은 transpose로 바뀐다. Gaussian elimination과 minor 계산에서는 row frame

$$
A=
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

을 쓰고, orthogonal projector에서는 column frame $M=A^T$를 쓴다.

---

# I. 먼저 “좋은 관측량”이 무엇인지 고정한다

## 2. 중복을 제거하는 것만으로는 선택이 끝나지 않는다

어떤 공간이 quotient

$$
\mathcal M=U/G
$$

로 주어졌다고 하자. $u\in U$는 실제 점이 아니라 대표이고, $gu$는 같은 점을 나타낸다.

대표의 중복을 없애는 방법은 하나가 아닐 수 있다. 따라서 관측량

$$
\mathcal O:U\longrightarrow Y
$$

를 고를 때는 최소한 다음을 검사해야 한다.

### 조건 A — 대표에 무관한가

$$
\mathcal O(gu)=\mathcal O(u)
$$

이거나, projective target이라면 모든 성분이 같은 nonzero scalar만큼 변해야 한다.

### 조건 B — quotient의 점을 잃지 않는가

$$
\mathcal O(u_1)=\mathcal O(u_2)
\quad\Longrightarrow\quad
u_1,u_2\text{가 같은 }G\text{-orbit}
$$

이어야 한다. 즉 원래 점을 복원할 수 있어야 한다.

### 조건 C — 원하는 범주의 사상인가

우리가 원하는 것이 무엇인지 먼저 정해야 한다.

- local holomorphic coordinates인가?
- global smooth/Hermitian coordinates인가?
- global holomorphic polynomial coordinates인가?
- metric과 curvature 계산인가?
- projective algebraic family의 구성인가?

같은 정보를 담아도 범주가 다르면 후속 계산이 달라진다.

### 조건 D — 어떤 추가 선택에 의존하는가

projector는 Hermitian metric을 사용한다. Plücker는 metric 없이 complex linear structure만 사용한다. 이 차이는 정보량의 차이가 아니라 **추가 구조의 차이**다.

### 조건 E — 어떤 대칭과 호환되는가

- projector는 unitary symmetry와 자연스럽다.
- Plücker는 $GL(n,\mathbf C)$의 complex-linear action과 자연스럽다.

이 다섯 조건을 확인한 뒤에야 “왜 이것을 골랐는가”라는 질문이 닫힌다.

---

# II. 첫 토이모델: 같은 $\mathbf{CP}^1$을 세 번 본다

## 3. 실제 점과 대표

$$
\mathbf{CP}^1
=
(\mathbf C^2\setminus\{0\})/\mathbf C^\times.
$$

즉

$$
q=\begin{pmatrix}X\\Y\end{pmatrix}
\sim
\lambda q,
\qquad
\lambda\in\mathbf C^\times.
$$

우리는 같은 projective point를 세 방식으로 관찰한다.

---

## 4. 첫 번째 관찰: local normalization

$X\neq0$인 곳에서는

$$
q\sim \frac1Xq
=
\begin{pmatrix}1\\z\end{pmatrix},
\qquad
z=\frac YX.
$$

이 한 수 $z$가 그 chart의 projective point를 완전히 결정한다.

### 장점

- holomorphic이다.
- 계산이 가장 단순하다.
- 이 chart는 $\mathbf C$와 같다.

### 한계

$X=0$에서는 사용할 수 없다. 다른 chart

$$
w=\frac XY=\frac1z
$$

로 갈아타야 한다.

따라서 local normalization은

$$
\boxed{\text{국소 holomorphic chart}}
$$

를 주지만 하나의 global coordinate는 주지 않는다.

---

## 5. 두 번째 관찰: normalized projector

대표 $q$에서 rank-one orthogonal projector를 만든다.

$$
P_q
=
\frac{qq^\dagger}{q^\dagger q}.
$$

### 5.1 scaling을 정확히 제거한다

$$
P_{\lambda q}
=
\frac{\lambda q(\lambda q)^\dagger}
{(\lambda q)^\dagger(\lambda q)}
=
P_q.
$$

즉 projector는 $q\sim\lambda q$를 완전히 카운터 친다.

### 5.2 원래 projective point도 복원한다

$$
\operatorname{Im}P_q=\mathbf Cq.
$$

따라서 $P_q$를 알면 원래 projective line을 정확히 안다.

### 5.3 chart에서 실제 식

$q=(1,z)^T$라면

$$
P(z)
=
\frac1{1+|z|^2}
\begin{pmatrix}
1&\bar z\\
z&|z|^2
\end{pmatrix}.
$$

projector는 다음 식을 만족한다.

$$
P^2=P,
\qquad
P^\dagger=P,
\qquad
\operatorname{tr}P=1.
$$

### 5.4 왜 complex-holomorphic coordinate가 아닌가

$P(z)$에는

$$
\bar z,\qquad |z|^2
$$

가 들어간다. 따라서

$$
\frac{\partial P}{\partial\bar z}\neq0.
$$

즉 projector는 global하고 완전하지만 holomorphic하지 않다.

### 5.5 projector가 잘하는 계산

projector는 Hermitian metric과 직접 맞는다.

$$
\boxed{
\frac12\operatorname{Tr}(dP\,dP)
=
\frac{|dz|^2}{(1+|z|^2)^2}
}
$$

이라는 Fubini–Study metric을 준다. normalization convention에 따라 전체 상수만 달라질 수 있다.

그러므로 projector는

$$
\boxed{\text{global Hermitian·metric 관찰}}
$$

에 매우 적합하다.

---

## 6. 세 번째 관찰: projective section coordinates

사실 $\mathbf{CP}^1$ 자체는 이미

$$
[X:Y]
$$

라는 global projective coordinate를 갖는다. 이는 $\mathcal O(1)$의 두 section

$$
X,\qquad Y
$$

가 만드는 identity map이다.

그렇다면 왜

$$
X^2,\ XY,\ Y^2
$$

를 보는가?

## 7. 왜 $\mathcal O(2)$인가

이 선택은 quotient redundancy만으로 강제되지 않는다. 두 가지 목적이 겹친다.

### 목적 A — relation이 처음 나타나는 최소 toy model

$\mathcal O(1)$의 map은

$$
\mathbf{CP}^1\longrightarrow\mathbf P^1
$$

인 identity라 새 polynomial relation이 없다.

$\mathcal O(2)$에서는

$$
\dim H^0(\mathbf{CP}^1,\mathcal O(2))=3
$$

이므로

$$
\mathbf{CP}^1\longrightarrow\mathbf P^2
$$

가 되고, 처음으로 ambient dimension이 하나 더 커져 비자명한 equation을 기대할 수 있다.

### 목적 B — tangent bundle과 curvature toy model

좌표변환 $w=1/z$에서

$$
\frac{\partial}{\partial w}
=-z^2\frac{\partial}{\partial z}.
$$

따라서

$$
T\mathbf{CP}^1\simeq\mathcal O(2).
$$

즉 $\mathcal O(2)$는 가장 작은 relation toy model이면서 Gaussian curvature와 first Chern class를 담는 tangent line bundle이기도 하다.

---

## 8. 왜 세 section을 전부 고르는가

스케일링 $q\mapsto\lambda q$ 아래 degree-two homogeneous polynomial은 모두

$$
F(\lambda X,\lambda Y)=\lambda^2F(X,Y)
$$

로 같은 weight를 갖는다.

그 전체 공간은

$$
\operatorname{Sym}^2(\mathbf C^2)^*
=
\operatorname{span}\{X^2,XY,Y^2\}.
$$

이 세 개는 임의로 고른 함수가 아니라 **degree two의 모든 관측량의 basis**다.

두 개만 고르면 정보가 빠질 수 있다. 예를 들어

$$
[X:Y]\longmapsto[X^2:Y^2]
$$

만 보면

$$
[X:Y]
\quad\text{와}\quad
[X:-Y]
$$

를 구별하지 못한다. $XY$가 그 부호 정보를 복원한다.

반면 complete system은 점을 분리한다. $X\neq0$이면

$$
\frac{XY}{X^2}=\frac YX=z
$$

로 원래 chart coordinate를 회수한다. $X=0$인 점은 유일하게 $[0:0:1]$로 간다.

따라서 complete degree-two system

$$
X^2,XY,Y^2
$$

을 쓰면 point separation이 회복된다.

---

## 9. 그 다음에 relation을 찾는다

map은

$$
\nu_2:[X:Y]\longmapsto[X^2:XY:Y^2].
$$

$X\neq0$ chart에서 $z=Y/X$를 쓰면

$$
[1:z:z^2].
$$

아직 relation을 모른다고 하자.

### 9.1 linear relation 검색

$$
A+Bz+Cz^2=0
$$

이 모든 $z$에서 성립하려면

$$
A=B=C=0.
$$

linear relation은 없다.

### 9.2 quadratic relation 검색

일반 homogeneous quadratic

$$
\begin{aligned}
Q={}&A Z_0^2+B Z_0Z_1+C Z_0Z_2\\
&+D Z_1^2+E Z_1Z_2+F Z_2^2
\end{aligned}
$$

에 $(Z_0,Z_1,Z_2)=(1,z,z^2)$를 넣으면

$$
Q(1,z,z^2)
=A+Bz+(C+D)z^2+Ez^3+Fz^4.
$$

따라서

$$
A=B=E=F=0,
\qquad C+D=0.
$$

relation space는 한 차원이고

$$
\boxed{Z_0Z_2-Z_1^2=0.}
$$

이제야 polynomial ring을 도입해

$$
\mathbf C[Z_0,Z_1,Z_2]
\longrightarrow
\mathbf C[X,Y]
$$

의 kernel이 이 식으로 생성된다고 말한다.

---

# III. winding과 POU는 같은 line bundle의 다른 관찰이다

## 10. 두 chart의 gluing

$\mathcal O(k)$의 local frame을

$$
e_\infty=z^k e_0
$$

로 붙인다.

section

$$
s=f_0e_0=f_\infty e_\infty
$$

은

$$
f_\infty(w)=w^k f_0(1/w)
$$

를 만족한다.

$f_0(z)=\sum_{n\ge0}a_nz^n$를 넣으면 $k\ge0$에서

$$
f_0(z)=a_0+a_1z+\cdots+a_kz^k.
$$

즉 local holomorphic functions는 무한히 많지만 global section은 $k+1$차원으로 줄어든다.

## 11. winding form에서 curvature로

적도에서 transition $g=e^{ik\theta}$를 잡고

$$
\alpha_k
=
\frac1{2\pi i}g^{-1}dg
=
\frac{k}{2\pi}d\theta
$$

를 둔다.

partition of unity

$$
\rho_N+\rho_S=1
$$

로

$$
A_N=-\rho_S\alpha_k,
\qquad
A_S=\rho_N\alpha_k
$$

를 만들면

$$
A_S-A_N=\alpha_k
$$

이고

$$
dA_N=dA_S.
$$

따라서 전역 curvature form $F_k$가 생기고

$$
\boxed{
\int_{S^2}F_k
=
\int_{S^1}\alpha_k
=k.
}
$$

같은 line bundle을

- section으로 보면 finite coordinate system이 나오고,
- connection과 curvature로 보면 Chern number가 나온다.

이 둘은 경쟁하는 설명이 아니라 같은 gluing data의 서로 다른 관찰이다.

---

# IV. 둘째 토이모델: 같은 $\mathrm{Gr}(2,4)$를 세 번 본다

## 12. 실제 점과 frame의 중복

$W\in\mathrm{Gr}(2,4)$의 basis를 두 row로 놓으면 full-rank matrix

$$
A\in M_{2\times4}(\mathbf C)
$$

를 얻는다.

basis를 바꾸면

$$
A\sim gA,
\qquad
g\in GL(2,\mathbf C).
$$

한 점은 frame 하나가 아니라 이 orbit 전체다.

---

## 13. 첫 번째 관찰: Gaussian elimination과 RREF

$p_{12}=\det A_{12}\neq0$인 곳에서는 row operation으로

$$
A\sim
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}.
$$

이 chart에서는

$$
(a,b,c,d)\in\mathbf C^4
$$

가 평면을 완전히 결정한다.

### 장점

- holomorphic이고 algebraic이다.
- 네 자유좌표가 정말 독립이다.
- local computation에 가장 좋다.

### 한계

$p_{12}=0$인 평면에서는 이 gauge를 쓸 수 없다. 다른 nonzero minor를 pivot으로 잡아야 한다.

따라서 RREF는

$$
\boxed{\text{국소 holomorphic·algebraic 관찰}}
$$

이다.

---

## 14. 두 번째 관찰: orthogonal projector

column frame $M=A^T$를 쓰고

$$
P_M
=
M(M^\dagger M)^{-1}M^\dagger
$$

를 만든다.

row convention으로는 같은 식을

$$
P_A
=
A^\dagger(AA^\dagger)^{-1}A
$$

로 쓴다.

### 14.1 $GL(2)$ basis change를 정확히 제거한다

column frame에서 basis change는 $M\mapsto Mg$다. 그러면

$$
\begin{aligned}
P_{Mg}
&=Mg(g^\dagger M^\dagger Mg)^{-1}g^\dagger M^\dagger\\
&=Mg\bigl(g^{-1}(M^\dagger M)^{-1}(g^\dagger)^{-1}\bigr)g^\dagger M^\dagger\\
&=P_M.
\end{aligned}
$$

따라서 projector는 $A\sim gA$를 이미 완전히 카운터 친다.

### 14.2 원래 평면도 복원한다

$$
\operatorname{Im}P_M=W.
$$

즉 projector와 Grassmannian point는 같은 정보를 가진다.

### 14.3 RREF chart에서 실제 식

$$
M=
\begin{pmatrix}
I_2\\ Z
\end{pmatrix},
\qquad
Z=
\begin{pmatrix}
a&c\\ b&d
\end{pmatrix}
$$

라 하면

$$
P(Z)
=
\begin{pmatrix}I_2\\Z\end{pmatrix}
(I_2+Z^\dagger Z)^{-1}
\begin{pmatrix}I_2&Z^\dagger\end{pmatrix}.
$$

여기에는 $Z^\dagger$, 즉 복소켤레가 들어간다. 따라서 $P(Z)$는 $Z$의 holomorphic polynomial coordinate가 아니다.

---

## 15. projector를 complex polynomial equations만으로 보면 더 큰 공간이 나온다

orthogonal projector는

$$
P^2=P,
\qquad
\operatorname{tr}P=2,
\qquad
P^\dagger=P
$$

를 만족한다.

마지막 Hermitian 조건을 버리고

$$
P^2=P,
\qquad
\operatorname{tr}P=2
$$

만 complex polynomial equations로 남기면 무엇이 생기는가?

complex idempotent $P$는

$$
W=\operatorname{Im}P,
\qquad
K=\ker P,
\qquad
\mathbf C^4=W\oplus K
$$

를 함께 기억한다. 즉 평면 하나가 아니라 **평면과 complement의 쌍**을 기억한다.

가장 작은 예로

$$
P_t=
\begin{pmatrix}
1&t\\0&0
\end{pmatrix}
$$

를 보면

$$
P_t^2=P_t
$$

이고 모든 $t$에서 image는 $\mathbf Ce_1$로 같지만

$$
\ker P_t=\mathbf C(-t,1)
$$

는 달라진다.

Hermitian 조건은 standard inner product를 이용해

$$
K=W^\perp
$$

를 선택한다. 따라서 projector model은

$$
\boxed{\text{평면 자체}+\text{Hermitian metric이 고른 orthogonal complement}}
$$

의 모델이다.

그 결과 projector는 global smooth/Hermitian model로는 정확하지만, metric-free complex algebraic model과는 다르다.

---

## 16. symmetry도 다르다

ambient unitary $U\in U(4)$에 대해서는

$$
P_{UW}=UP_WU^\dagger.
$$

그러나 일반 $h\in GL(4,\mathbf C)$는 standard orthogonality를 보존하지 않는다. $hW$의 orthogonal complement는 일반적으로 $h(W^\perp)$가 아니다.

즉 projector는

$$
\boxed{U(4)\text{-자연적}}
$$

이고, complex algebraic geometry에서 원하는 것은 보통

$$
\boxed{GL(4,\mathbf C)\text{-자연적}}
$$

인 표현이다.

---

# V. 세 번째 관찰: Plücker가 왜 나오는가

## 17. 두 basis vector를 metric 없이 하나로 묶는다

$W$의 ordered basis를

$$
r_1,r_2\in\mathbf C^4
$$

라고 하자.

두 벡터를 metric 없이 하나의 line-valued object로 묶는 가장 직접적인 연산은 exterior product다.

$$
\omega_W=r_1\wedge r_2\in\bigwedge^2\mathbf C^4.
$$

basis를

$$
\begin{pmatrix}r_1'\\r_2'\end{pmatrix}
=
g
\begin{pmatrix}r_1\\r_2\end{pmatrix}
$$

로 바꾸면 bilinearity와 alternating 성질로

$$
\boxed{
r_1'\wedge r_2'
=
\det(g)\,r_1\wedge r_2.
}
$$

projective class에서는 공통 scalar가 사라진다.

$$
W\longmapsto[\omega_W]
\in\mathbf P(\bigwedge^2\mathbf C^4).
$$

이것이 Plücker map이다.

## 18. projector처럼 완전한 정보인가

그렇다. nonzero decomposable $2$-vector

$$
\omega=r_1\wedge r_2
$$

에서

$$
\boxed{
W
=
\{v\in\mathbf C^4:v\wedge\omega=0\}
}
$$

로 원래 평면을 복원한다.

실제로 $r_1,r_2$를 basis $r_1,r_2,r_3,r_4$로 연장하고

$$
v=c_1r_1+c_2r_2+c_3r_3+c_4r_4
$$

라 쓰면

$$
v\wedge r_1\wedge r_2
=c_3r_3\wedge r_1\wedge r_2+c_4r_4\wedge r_1\wedge r_2.
$$

두 항은 독립이므로 이것이 0일 필요충분조건은 $c_3=c_4=0$, 즉 $v\in W$인 것이다.

따라서

$$
\boxed{
P_W\quad\text{와}\quad[\wedge^2W]
}
$$

는 point-set 수준에서 같은 정보를 가진다.

Plücker를 고르는 이유는 정보량이 더 많아서가 아니다.

---

## 19. 왜 maximal minors인가

표준 basis $e_1,\dots,e_4$에서

$$
\omega_W
=
\sum_{1\le i<j\le4}
p_{ij}\,e_i\wedge e_j
$$

로 전개한다.

row frame $A=(a_{ij})$의 두 row가 $r_1,r_2$일 때 coefficient를 직접 전개하면

$$
p_{ij}=a_{1i}a_{2j}-a_{1j}a_{2i}=\det A_{ij}.
$$

즉 maximal minor는 편의상 골라낸 함수가 아니다.

$$
\boxed{
\text{maximal minors}=\text{전체 wedge vector의 basis coordinates}.
}
$$

여섯 개를 전부 쓰는 이유도 여기에 있다. $\bigwedge^2\mathbf C^4$의 한 벡터를 완전히 기록하려면 basis coordinate 여섯 개가 필요하다.

특정 chart에서는 일부가 나머지로 결정될 수 있다. 예를 들어 $p_{12}\neq0$이면 $p_{34}$가 다른 ratio로 결정된다. 그러나 이것은 **local redundancy**다. 전체 여섯 coordinate는

- chart를 고르지 않고,
- $GL(4,\mathbf C)$ 아래 닫혀 있고,
- wedge vector 전체를 기록한다.

minimal subset을 찾는 문제와 canonical full system을 쓰는 문제는 다르다.

---

## 20. determinant line bundle은 어디서 생기는가

Grassmannian 위 tautological bundle을

$$
\mathcal S_W=W
$$

로 정의한다.

각 fiber의 top exterior power

$$
\det\mathcal S_W
=
\bigwedge^2W
$$

는 한 차원이다.

Plücker point $[\bigwedge^2W]$는 바로 이 한 차원 line을 ambient $\bigwedge^2\mathbf C^4$ 안에서 보는 것이다.

그 dual

$$
L_{\mathrm{Pl}}=\det\mathcal S^*
$$

위의 global sections는 ambient linear functional

$$
e_i^*\wedge e_j^*
$$

을 $\bigwedge^2W$에 제한하여 얻는다. 그 값이 $p_{ij}$다.

따라서 논리 순서는 다음이다.

$$
\boxed{
W
\longrightarrow
\bigwedge^2W\text{라는 canonical line}
\longrightarrow
\det\mathcal S^*
\longrightarrow
\text{maximal-minor sections}.
}
$$

line bundle을 먼저 임의로 고르고 minor를 찾은 것이 아니다. 부분공간의 top wedge가 먼저 line을 만들고, 그 dual의 coordinate sections가 minor로 나타난다.

---

# VI. 이제서야 Plücker relation을 찾는다

## 21. image의 본질적 조건은 decomposability다

ambient projective space

$$
\mathbf P(\bigwedge^2\mathbf C^4)\simeq\mathbf P^5
$$

에는 모든 $2$-vector가 들어 있다.

하지만 평면에서 온 것은

$$
\omega=r_1\wedge r_2
$$

꼴의 decomposable vector뿐이다.

평면에서 온 벡터라면 자동으로

$$
\omega\wedge\omega
=(r_1\wedge r_2)\wedge(r_1\wedge r_2)=0
$$

이다. 같은 벡터가 두 번 나타나기 때문이다.

## 22. 식을 직접 전개한다

$$
\begin{aligned}
\omega={}&p_{12}e_{12}+p_{13}e_{13}+p_{14}e_{14}\\
&+p_{23}e_{23}+p_{24}e_{24}+p_{34}e_{34}
\end{aligned}
$$

라 쓰면, 서로 보완되는 index pair만 $e_{1234}$를 만든다.

$$
\boxed{
\omega\wedge\omega
=
2\bigl(
 p_{12}p_{34}
-p_{13}p_{24}
+p_{14}p_{23}
\bigr)e_{1234}.
}
$$

따라서 image는

$$
\boxed{
p_{12}p_{34}
-p_{13}p_{24}
+p_{14}p_{23}=0
}
$$

을 만족한다.

이 relation은 kernel 계산 전에 이미 **decomposable wedge라는 intrinsic image condition**에서 나왔다.

## 23. 이 식을 만족하면 정말 평면에서 오는가

nonzero coordinate 중 하나를 고른다. 예를 들어 $p_{12}\neq0$라고 하자. projective scaling으로 $p_{12}=1$로 만들고

$$
a=-p_{23},
\qquad
b=-p_{24},
\qquad
c=p_{13},
\qquad
d=p_{14}
$$

라고 둔다.

relation은

$$
p_{34}=p_{13}p_{24}-p_{14}p_{23}=ad-bc
$$

를 준다. 따라서 모든 좌표는

$$
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

의 maximal minors와 정확히 일치한다.

다른 $p_{ij}\neq0$인 경우에도 해당 열을 pivot으로 같은 reconstruction을 한다. 그러므로 $\mathrm{Gr}(2,4)$에서는 이 한 quadratic이 decomposable locus 전체를 정의한다.

---

## 24. RREF chart와 같은 식을 대조한다

$$
A=
\begin{pmatrix}
1&0&a&b\\
0&1&c&d
\end{pmatrix}
$$

이면

$$
p_{12}=1,
\quad
p_{13}=c,
\quad
p_{14}=d,
\quad
p_{23}=-a,
\quad
p_{24}=-b,
\quad
p_{34}=ad-bc.
$$

따라서

$$
(a,b,c,d)
\longmapsto
(c,d,-a,-b,ad-bc)
$$

라는 $\mathbf A^4\to\mathbf A^5$ graph map이 생긴다.

그 local ideal은

$$
\boxed{
x_{34}-x_{13}x_{24}+x_{14}x_{23}=0.}
$$

이를 homogenize하면 위의 Plücker quadratic이 된다.

즉 relation 발견에는 두 길이 있고 서로 일치한다.

$$
\boxed{
\begin{array}{ccl}
\text{exterior algebra} &:& \omega\wedge\omega=0,\\
\text{local coordinates} &:& \ker(\mathbf C[x_{ij}]\to\mathbf C[a,b,c,d]).
\end{array}}
$$

---

# VII. RREF·projector·Plücker 비교표

| 항목 | RREF / Gaussian elimination | orthogonal projector | Plücker |
|---|---|---|---|
| 출력 | $Z$ 또는 $a,b,c,d$ | Hermitian idempotent $P_W$ | projective wedge $[\bigwedge^2W]$ |
| 범위 | 한 affine chart | 전역 | 전역 |
| 대표중복 제거 | pivot gauge | 정확히 제거 | projectivization으로 제거 |
| 점 복원 | 가능 | $W=\operatorname{Im}P$ | $W=\{v:v\wedge\omega=0\}$ |
| holomorphic | 예, chart 안에서 | 아니오, $\bar Z$ 포함 | 예 |
| polynomial | 예, chart 안에서 | Hermitian 조건은 conjugation 포함 | 예 |
| 추가 선택 | pivot minor | Hermitian metric | 없음: complex linear structure만 |
| 자연한 대칭 | chart subgroup | $U(4)$ | $GL(4,\mathbf C)$ |
| 주용도 | local 계산 | metric·QFIM·symplectic 계산 | projective equations·line bundle·family |

핵심은 다음이다.

$$
\boxed{
\text{셋은 정보량 경쟁을 하는 것이 아니라 계산 범주를 나눈다.}
}
$$

---

# VIII. 왜 ring은 맨 마지막에 등장하는가

## 25. 관측량을 고르기 전에는 kernel도 의미가 없다

임의의 local holomorphic functions

$$
f_1,\dots,f_N
$$

을 고르면 relation이 없을 수도 있고, 특정 family에만 우연한 relation이 생길 수도 있다.

먼저 다음을 끝내야 한다.

1. 어떤 quotient point를 관찰하는가?
2. 어떤 범주에서 계산하려는가?
3. 관측량이 대표에 무관한가?
4. 관측량이 점을 분리하는가?
5. 추가 metric이나 gauge 선택이 숨어 있는가?
6. 원하는 symmetry와 호환되는가?

그 뒤에만 polynomial ring을 만든다.

## 26. $\mathbf{CP}^1$의 kernel

$$
\Phi:
\mathbf C[Z_0,Z_1,Z_2]
\longrightarrow
\mathbf C[X,Y]
$$

을

$$
Z_0\mapsto X^2,
\qquad
Z_1\mapsto XY,
\qquad
Z_2\mapsto Y^2
$$

로 정의하면

$$
\ker\Phi=(Z_0Z_2-Z_1^2).
$$

## 27. $\mathrm{Gr}(2,4)$의 kernel

$$
\Psi:
\mathbf C[p_{12},p_{13},p_{14},p_{23},p_{24},p_{34}]
\longrightarrow
\text{polynomial functions on full-rank frames}
$$

에서 $p_{ij}$를 maximal minor로 보내면

$$
\ker\Psi
=
(p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}).
$$

여기서 ring을 생각한 이유는

$$
\boxed{
\text{이미 정당화된 polynomial 관측량들의 모든 곱과 relation을
하나의 ideal로 모으기 위해서다.}
}
$$

projector entry들로도 다른 algebra를 만들 수 있다. 다만 그것은 conjugation과 Hermitian metric이 들어간 real/Hermitian model을 기록한다. 현재 원하는 complex projective model과는 다른 대수화다.

---

# IX. projector와 Plücker는 metric에서 다시 만난다

## 28. $\mathbf{CP}^1$

projector에서는

$$
\frac12\operatorname{Tr}(dP\,dP)
$$

가 Fubini–Study metric을 준다.

line bundle 쪽에서는

$$
\omega_{\mathrm{FS}}
=i\partial\bar\partial\log(1+|z|^2)
$$

가 같은 metric의 Kähler form을 준다.

$\mathcal O(2)$의 Veronese map을 metric과 정확히 맞출 때는 unitary-normalized basis

$$
[1:\sqrt2z:z^2]
$$

를 사용하면 pullback potential이

$$
\log(1+2|z|^2+|z|^4)
=2\log(1+|z|^2)
$$

가 되어 pullback Kähler form은 $2\omega_{\mathrm{FS}}$다.

## 29. $\mathrm{Gr}(2,4)$

$$
M=\begin{pmatrix}I_2\\Z\end{pmatrix}
$$

에서 projector는

$$
P(Z)=M(M^\dagger M)^{-1}M^\dagger.
$$

Plücker determinant line bundle의 local Hermitian metric은

$$
h_{\mathrm{Pl}}
=
\det(M^\dagger M)^{-1}
=
\det(I_2+Z^\dagger Z)^{-1}.
$$

그 curvature는

$$
\omega_{\mathrm{Gr}}
=i\partial\bar\partial
\log\det(I_2+Z^\dagger Z).
$$

한편 projector에서 얻는 metric은

$$
\boxed{
g_{\mathrm{Gr}}=\frac12\operatorname{Tr}(dP\,dP).}
$$

직접 미분하면 둘은 같은 canonical Grassmannian metric을 준다. 원점 $Z=0$에서는 특히

$$
\frac12\operatorname{Tr}(dP^2)
=
\operatorname{Tr}(dZ^\dagger dZ),
$$

$$
\partial\bar\partial
\log\det(I+Z^\dagger Z)|_{Z=0}
=
\operatorname{Tr}(dZ^\dagger dZ).
$$

따라서 projector와 Plücker는 서로를 대체하지 않는다.

- projector는 metric을 바로 계산한다.
- Plücker line bundle은 그 metric의 Kähler potential과 curvature class를 전역 holomorphic language로 기록한다.

---

# X. Relative Grassmannian과 Reineke tower에서 선택이 갈린다

## 30. relative Grassmannian

$E\to X$가 rank $N$ vector bundle이면

$$
\operatorname{Gr}_X(k,E)
=
\{(x,W):W\subset E_x,\ \dim W=k\}
$$

를 만든다.

각 open set에서 $E$를 trivialize하면 ordinary Grassmannian 계산이 fiber마다 반복된다.

### RREF의 역할

nonzero minor를 고르면 local chart

$$
U\times\mathbf A^{k(N-k)}
$$

를 얻는다. local holomorphic 계산에 적합하다.

### projector의 역할

$E$에 Hermitian metric을 추가하면 각 fiber의 orthogonal projector를 만들 수 있다. 이는 fiberwise metric과 horizontal/vertical differential geometry에 유용하다.

그러나 projector construction은 그 Hermitian metric에 의존하며, relative Grassmannian을 metric-free algebraic subvariety로 정의하는 장치는 아니다.

### relative Plücker의 역할

각 fiber의 line

$$
\bigwedge^kW\subset\bigwedge^kE_x
$$

를 기록하면

$$
\operatorname{Gr}_X(k,E)
\hookrightarrow
\mathbf P_X(\bigwedge^kE)
$$

를 얻는다.

각 fiber의 decomposability relations가 homogeneous polynomial equations이므로 relative Grassmannian은 projective bundle 안의 closed algebraic subvariety가 된다.

따라서 projection

$$
\operatorname{Gr}_X(k,E)\to X
$$

가 projective morphism이라는 결론은 Plücker model에서 바로 나온다.

## 31. Reineke tower

acyclic quiver의 순서에 따라

$$
X_r
=
\operatorname{Gr}_{X_{r-1}}(d_r,E_r)
$$

를 반복하면 Reineke tower가 된다.

여기서 세 모델의 역할은 분리된다.

$$
\boxed{
\begin{array}{ccl}
\text{RREF} &:& \text{각 단계의 local chart},\\
\text{relative Plücker} &:& \text{algebraicity와 projectivity},\\
\text{projector/Hermitian metric} &:& \text{Kähler metric과 curvature 계산}.
\end{array}}
$$

Ricci-positive tower라는 큰 그림에서는 바로 이 세 층이 모두 필요하다.

1. Plücker determinant line bundle이 algebraic class와 projective structure를 준다.
2. 그 line bundle에 Hermitian metric을 주어 curvature form을 만든다.
3. 여러 단계의 curvature form을 twisting하여 tower metric을 만든다.
4. horizontal–vertical block 또는 projector 계산으로 metric positivity를 검사한다.

---

# XI. 관측량을 고르는 실제 프로토콜

## 32. 1단계 — 같은 점으로 보는 중복을 적는다

$$
u\sim gu.
$$

## 33. 2단계 — 무엇을 계산하려는지 먼저 적는다

- local coordinates?
- global metric?
- holomorphic embedding?
- polynomial equations?
- projective family?

목표가 없으면 “가장 좋은 표현”도 없다.

## 34. 3단계 — 후보 관측량이 quotient에 내려가는지 확인한다

- RREF: gauge fixing이 가능한 chart인가?
- projector: $P_{gu}=P_u$인가?
- projective section: 모든 coordinate가 같은 scalar로 변하는가?

## 35. 4단계 — 점을 분리하는지 확인한다

- projector에서 $W=\operatorname{Im}P$인가?
- Plücker에서 $W=\{v:v\wedge\omega=0\}$인가?
- section 일부만 골랐을 때 서로 다른 점이 합쳐지지 않는가?

## 36. 5단계 — 숨은 추가 구조를 확인한다

- projector는 Hermitian metric을 사용한다.
- RREF는 pivot choice를 사용한다.
- Plücker는 complex linear structure와 top wedge만 사용한다.

## 37. 6단계 — symmetry와 범주를 확인한다

- unitary-equivariant인가?
- $GL(n,\mathbf C)$-equivariant인가?
- holomorphic인가?
- polynomial인가?

## 38. 7단계 — image condition을 찾는다

- symmetric rank-one tensor인가?
- decomposable wedge인가?
- idempotent/Hermitian matrix인가?

## 39. 8단계 — 마지막에 kernel ideal을 계산한다

이 단계에 와서야

$$
\mathbf C[\text{formal coordinates}]
\longrightarrow
\text{actual functions or sections}
$$

의 kernel이 공간의 equation을 기록한다.

---

# XII. 손계산 문제

## 문제 1 — projector가 projective point를 분리하는가

$P_q=P_{q'}$이면 $[q]=[q']$임을 image를 이용해 증명하여라.

## 문제 2 — projector의 antiholomorphic dependence

$$
P(z)=\frac1{1+|z|^2}
\begin{pmatrix}1&\bar z\\z&|z|^2\end{pmatrix}
$$

에서 $\partial P/\partial\bar z\neq0$인 성분을 하나 계산하여라.

## 문제 3 — section 일부를 버리면 생기는 식별

$$
[X:Y]\mapsto[X^2:Y^2]
$$

가 $[X:Y]$와 $[X:-Y]$를 식별함을 확인하여라.

## 문제 4 — $\mathcal O(2)$의 relation을 모른 채 찾기

일반 homogeneous quadratic의 coefficient를 놓고

$$
[1:z:z^2]
$$

를 대입하여 kernel이 한 차원임을 계산하여라.

## 문제 5 — complex idempotent의 complement

$$
P_t=\begin{pmatrix}1&t\\0&0\end{pmatrix}
$$

에 대해 $P_t^2=P_t$, $\operatorname{Im}P_t=\mathbf Ce_1$, $\ker P_t=\mathbf C(-t,1)$을 확인하여라.

## 문제 6 — Grassmann projector의 basis invariance

$$
P_A=A^\dagger(AA^\dagger)^{-1}A
$$

에 $A\mapsto gA$를 대입하여 $P_{gA}=P_A$를 한 줄씩 계산하여라.

## 문제 7 — 여섯 maximal minor

$$
A=\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}
$$

의 모든 maximal minor를 부호까지 계산하여라.

## 문제 8 — semi-invariance

$p_{ij}(gA)=\det(g)p_{ij}(A)$를 determinant multiplicativity로 증명하여라.

## 문제 9 — wedge에서 평면 복원

$\omega=r_1\wedge r_2\neq0$일 때

$$
W=\operatorname{span}(r_1,r_2)
=
\{v:v\wedge\omega=0\}
$$

임을 증명하여라.

## 문제 10 — decomposability relation

일반 $2$-vector $\omega=\sum p_{ij}e_i\wedge e_j$에 대해 $\omega\wedge\omega$를 직접 전개하여 Plücker quadratic을 얻어라.

## 문제 11 — projector metric과 Plücker metric

$Z=0$에서

$$
\frac12\operatorname{Tr}(dP^2)
=
\operatorname{Tr}(dZ^\dagger dZ)
$$

를 block matrix multiplication으로 확인하여라.

## 문제 12 — 세 표현의 선택

다음 목표마다 RREF, projector, Plücker 중 무엇을 먼저 사용할지 이유를 한 문장으로 적어라.

1. 한 점 근방에서 tangent vector를 행렬 $D$로 계산한다.
2. QFIM을 계산한다.
3. relative Grassmannian이 projective morphism임을 보인다.
4. Plücker line bundle의 curvature를 계산한다.

---

# XIII. 마지막 압축

처음 질문은

> projection matrix가 이미 $\lambda$와 $G$의 중복을 완전히 제거하는데 왜 Plücker를 생각하는가?

였다.

정답은 다음이다.

$$
\boxed{
\text{Plücker는 중복 제거 장치가 아니라
complex-projective 범주에 맞춘 완전 관측량이다.}
}
$$

- RREF는 local holomorphic coordinates를 준다.
- projector는 global Hermitian point와 metric을 준다.
- Plücker는 global holomorphic polynomial coordinates와 line bundle을 준다.

세 방식은 모두 원래 평면을 복원한다. 차이는 정보량이 아니라 **정보의 조직 방식과 후속 연산**이다.

maximal minor를 고른 이유도 이제 정확하다.

$$
\boxed{
\text{두 basis vector의 top wedge가 basis change 아래 determinant만큼 변하고,
그 wedge 전체의 coordinates가 maximal minors이기 때문이다.}
}
$$

line bundle은 이 공통 scalar ambiguity를 metric으로 normalize하지 않고 한 차원 fiber로 보존한다.

그 뒤에야 ring을 만든다.

$$
\boxed{
\text{이미 정당화된 polynomial 관측량들의 곱과 relation을
kernel ideal 하나로 모으기 위해 ring을 쓴다.}
}
$$

그리고 relative Grassmannian과 Reineke tower에서는

$$
\boxed{
\text{Plücker가 algebraicity·projectivity를,
projector와 Hermitian metric이 curvature 계산을 담당한다.}
}
$$

이것이 같은 공간을 세 번 보는 이유다.
