# 두 차트의 한 전이함수에서 곡률까지

## $\mathbf P^1=S^2$의 chart ring, $dz=-w^{-2}dw$, winding, connection, Mayer–Vietoris

이 노트의 목표는 하나의 계산선을 끝까지 보는 것이다.

$$
\boxed{
\text{두 affine chart의 overlap ring}
\longrightarrow
\text{좌표변환의 미분 }dz=-w^{-2}dw
\longrightarrow
\text{conformal factor의 변화}
\longrightarrow
\text{connection 차이와 winding}
\longrightarrow
\text{partition of unity}
\longrightarrow
K\,dA.
}
$$

계량은 첨부 노트와 같은 반지름 $1$의 round metric을 사용한다.

$$
ds^2=\frac{4|dz|^2}{(1+|z|^2)^2}.
$$

이 convention에서

$$
ds^2=e^{2u}(dx^2+dy^2)
$$

이면

$$
\boxed{K=-e^{-2u}\Delta u},
$$

따라서 실제로 적분되는 곡률 $2$-form은

$$
\boxed{K\,dA=-\Delta u\,dx\wedge dy}.
$$

---

# 1. 두 pole-deleted chart와 세 ring

동차좌표를 $[Z_0:Z_1]$라 쓰고

$$
U_z=\{Z_0\neq0\},
\qquad
z=\frac{Z_1}{Z_0},
$$

$$
U_w=\{Z_1\neq0\},
\qquad
w=\frac{Z_0}{Z_1}
$$

로 둔다. 그러면 overlap에서

$$
w=\frac1z,
\qquad
z=\frac1w.
$$

기하적으로 $U_z,U_w$는 각각 한 pole을 제거한 구면이다. 어느 쪽을 북극·남극 제거 chart라고 부르는지는 stereographic projection convention에 달려 있으므로, 여기서는 $z$-chart와 $w$-chart라고 부른다.

## 1.1 algebraic regular-function ring

$$
\mathcal O_{\mathrm{alg}}(U_z)=\mathbf C[z],
$$

$$
\mathcal O_{\mathrm{alg}}(U_w)=\mathbf C[w]
=\mathbf C[z^{-1}],
$$

$$
\mathcal O_{\mathrm{alg}}(U_z\cap U_w)
=\mathbf C[z,z^{-1}].
$$

따라서 질문에서 예상한

$$
\mathbf C[X],\qquad
\mathbf C[1/X],\qquad
\mathbf C[X,1/X]
$$

가 맞다. 다만 $\mathbf C[1/X]$는 $X^{-1}$을 하나의 변수로 갖는 polynomial ring이고,

$$
\mathbf C[X,1/X]
$$

는 양수와 음수 지수를 모두 허용하는 Laurent polynomial ring이다.

## 1.2 세 종류의 함수환을 섞지 않는다

이번 계산에는 세 층이 함께 등장한다.

$$
\mathbf C[z]
\subset
\mathcal O_{\mathrm{hol}}(U_z)
\subset
C^\infty(U_z).
$$

- $\mathbf C[z]$: algebraic regular functions.
- $\mathcal O_{\mathrm{hol}}(U_z)$: 모든 entire holomorphic functions.
- $C^\infty(U_z)$: 모든 smooth functions.

아래의 conformal factor

$$
u_z=\log 2-\log(1+|z|^2)
$$

는 $\bar z$에 의존하므로 $\mathbf C[z]$나 holomorphic ring의 원소가 아니다. 그것은 smooth real-valued function이다.

반면 좌표변환

$$
w=z^{-1}
$$

과 그 미분에서 나오는

$$
-z^2,
\qquad
-z^{-2}
$$

는 overlap ring $\mathbf C[z,z^{-1}]$의 unit이다. 이 unit이 algebraic gluing과 differential-geometric gluing을 연결한다.

## 1.3 overlap ring의 unit과 정수

$$
\mathbf C[z,z^{-1}]^\times
=
\{c z^n:c\in\mathbf C^\times,\ n\in\mathbf Z\}.
$$

이것을 짧게 확인하자. Laurent polynomial

$$
f(z)=\sum_{j=m}^{M}a_jz^j,
\qquad
a_m a_M\neq0
$$

가 Laurent polynomial inverse를 가진다고 하자. 곱 $fg=1$에서 가장 낮은 지수와 가장 높은 지수가 둘 다 $0$이어야 한다. 그러려면 $m=M$여야 하므로 $f$는 단항식 $cz^n$이다.

이 정수 $n$은 원 $|z|=1$ 위에서 winding number가 된다.

$$
\frac{1}{2\pi i}
\oint_{|z|=1}f^{-1}df
=n.
$$

---

# 2. $dz=-w^{-2}dw$가 metric에 실제로 기여하는 방식

## 2.1 $z$-chart의 conformal factor

$$
ds^2=\frac{4|dz|^2}{(1+|z|^2)^2}
=e^{2u_z}|dz|^2
$$

이므로

$$
\boxed{u_z(z)=\log 2-\log(1+|z|^2)}
$$

## 2.2 $w$-chart로 바꾼다

$$
z=\frac1w
$$

이므로

$$
\boxed{dz=-w^{-2}dw}.
$$

따라서

$$
|dz|^2=|w|^{-4}|dw|^2.
$$

또

$$
1+|z|^2
=1+|w|^{-2}
=\frac{1+|w|^2}{|w|^2}.
$$

그러므로

$$
\begin{aligned}
ds^2
&=
\frac{4|w|^{-4}|dw|^2}
{\left((1+|w|^2)/|w|^2\right)^2}\\
&=
\frac{4|dw|^2}{(1+|w|^2)^2}.
\end{aligned}
$$

즉 $w$-chart에서도

$$
\boxed{u_w(w)=\log 2-\log(1+|w|^2)}
$$

## 2.3 두 local potential의 차이

$w=1/z$를 대입하면

$$
\begin{aligned}
u_w(1/z)
&=\log 2-\log(1+|z|^{-2})\\
&=\log 2-\log(1+|z|^2)+2\log|z|.
\end{aligned}
$$

따라서 overlap에서

$$
\boxed{u_w(1/z)-u_z(z)=2\log|z|}
$$

이 $2\log|z|$가 바로 $|dz/dw|=|w|^{-2}$가 conformal factor에 기여한 부분이다.

## 2.4 왜 curvature는 두 chart에서 일치하는가

polar coordinate $z=re^{i\theta}$에서

$$
\Delta\log r
=
\frac1r\frac{\partial}{\partial r}
\left(r\frac{\partial}{\partial r}\log r\right)
=
\frac1r\frac{\partial}{\partial r}(1)
=0
$$

이다. 이 계산은 $r>0$, 즉 overlap $\mathbf C^*$에서만 하는 계산이다.

따라서

$$
\Delta\bigl(u_w(1/z)-u_z(z)\bigr)=0
$$

이고, 두 local potential은 같은 curvature $2$-form을 만든다.

$$
\boxed{
-\Delta u_z\,dx\wedge dy
=
-\Delta u_w\,d\xi\wedge d\eta.
}
$$

여기서 $w=\xi+i\eta$다.

---

# 3. 각 chart에서 라플라시안으로 곡률 계산

## 3.1 $z$-chart

$r^2=x^2+y^2$라 하면

$$
u_z=\log 2-\log(1+r^2).
$$

radial Laplacian을 사용하면

$$
\Delta u_z
=
u_{rr}+\frac1r u_r.
$$

먼저

$$
u_r=-\frac{2r}{1+r^2}.
$$

다시 미분하면

$$
u_{rr}
=-\frac{2(1-r^2)}{(1+r^2)^2}.
$$

따라서

$$
\begin{aligned}
\Delta u_z
&=-\frac{2(1-r^2)}{(1+r^2)^2}
-\frac{2}{1+r^2}\\
&=-\frac4{(1+r^2)^2}.
\end{aligned}
$$

그러므로

$$
\boxed{
K\,dA
=-\Delta u_z\,dx\wedge dy
=\frac4{(1+r^2)^2}dx\wedge dy.
}
$$

또

$$
dA=e^{2u_z}dx\wedge dy
=\frac4{(1+r^2)^2}dx\wedge dy
$$

이므로

$$
\boxed{K=1}.
$$

## 3.2 $w$-chart

$s=|w|$라 하면 같은 계산으로

$$
\Delta_w u_w
=-\frac4{(1+s^2)^2}
$$

이고

$$
\boxed{
K\,dA
=\frac4{(1+s^2)^2}d\xi\wedge d\eta.
}
$$

$w=1/z$ 아래

$$
d\xi\wedge d\eta
=\left|\frac{dw}{dz}\right|^2 dx\wedge dy
=r^{-4}dx\wedge dy
$$

이고

$$
\frac4{(1+s^2)^2}r^{-4}
=
\frac4{(1+r^2)^2}.
$$

따라서 두 chart의 곡률 $2$-form은 실제로 같은 form이다.

---

# 4. connection $1$-form에서 같은 계산 보기

첨부 노트와 같은 convention으로

$$
\theta^1=e^u dx,
\qquad
\theta^2=e^u dy
$$

를 orthonormal coframe이라 하자. Levi-Civita connection $1$-form은

$$
\boxed{
\omega=u_y dx-u_xdy=-*du
}
$$

이고

$$
\boxed{
d\omega=K\,dA}.
$$

## 4.1 $z$-chart connection

$$
u_x=-\frac{2x}{1+r^2},
\qquad
u_y=-\frac{2y}{1+r^2}.
$$

따라서

$$
\begin{aligned}
\omega_z
&=\frac{-2y}{1+r^2}dx
+\frac{2x}{1+r^2}dy\\
&=\frac{2(-y\,dx+x\,dy)}{1+r^2}.
\end{aligned}
$$

polar coordinate에서

$$
-y\,dx+x\,dy=r^2d\theta
$$

이므로

$$
\boxed{
\omega_z=\frac{2r^2}{1+r^2}d\theta.
}
$$

이제 $d$를 취한다.

$$
\begin{aligned}
d\omega_z
&=d\left(\frac{2r^2}{1+r^2}\right)\wedge d\theta\\
&=\frac{4r}{(1+r^2)^2}dr\wedge d\theta\\
&=\frac4{(1+r^2)^2}dx\wedge dy.
\end{aligned}
$$

즉

$$
\boxed{d\omega_z=K\,dA}.
$$

## 4.2 $w$-chart connection

$w=se^{i\varphi}$라 하면

$$
\boxed{
\omega_w=\frac{2s^2}{1+s^2}d\varphi.
}
$$

on overlap에서

$$
s=r^{-1},
\qquad
\varphi=-\theta.
$$

따라서 $z$ 변수로 다시 쓰면

$$
\boxed{
\omega_w=-\frac{2}{1+r^2}d\theta.
}
$$

두 connection form의 차이는

$$
\begin{aligned}
\omega_w-\omega_z
&=-\frac{2}{1+r^2}d\theta
-\frac{2r^2}{1+r^2}d\theta\\
&=-2d\theta.
\end{aligned}
$$

즉

$$
\boxed{
\omega_w-\omega_z=-2d\theta.
}
$$

그리고 $d(d\theta)=0$이므로

$$
d\omega_w=d\omega_z.
$$

이것이 connection level에서 본 local curvature의 gluing이다.

---

# 5. $dz=-w^{-2}dw$에서 winding number $2$가 나오는 지점

## 5.1 tangent frame의 transition

좌표 vector field를

$$
e_z=\frac{\partial}{\partial z},
\qquad
e_w=\frac{\partial}{\partial w}
$$

라고 하자.

chain rule로

$$
e_w
=\frac{dz}{dw}e_z
=-w^{-2}e_z
=-z^2e_z.
$$

따라서 tangent bundle의 transition function은

$$
\boxed{g(z)=-z^2}.
$$

이것은 overlap ring의 unit이다.

$$
g\in\mathbf C[z,z^{-1}]^\times.
$$

## 5.2 winding form

normalized winding form을

$$
\alpha
=
\frac{1}{2\pi i}g^{-1}dg
$$

라고 두자.

$g=-z^2$이므로

$$
g^{-1}dg=2\frac{dz}{z}.
$$

$|z|=1$, $z=e^{i\theta}$에서

$$
\frac{dz}{z}=i\,d\theta.
$$

따라서

$$
\boxed{
\alpha=\frac1\pi d\theta.
}
$$

그리고

$$
\boxed{
\int_{S^1}\alpha
=\frac1\pi\int_0^{2\pi}d\theta
=2.
}
$$

이 정수 $2$는

$$
T\mathbf P^1\simeq\mathcal O(2)
$$

의 degree다.

## 5.3 cotangent에서는 부호가 반대다

질문에서 직접 적은 식

$$
dz=-w^{-2}dw
$$

은 cotangent frame의 관계다. 반대 방향으로 쓰면

$$
dw=-z^{-2}dz.
$$

따라서 cotangent bundle의 transition exponent는 $-2$이고

$$
K_{\mathbf P^1}=T^*\mathbf P^1\simeq\mathcal O(-2).
$$

정리하면

- tangent frame: winding $+2$.
- cotangent frame: winding $-2$.
- $|dz/dw|$의 modulus: conformal potential에 $2\log|z|$를 추가.
- $dz/dw$의 phase: connection form에 $2d\theta$를 추가.

---

# 6. Mayer–Vietoris: 적도의 winding form에 $d$를 취해 구면의 $2$-form 만들기

## 6.1 overlap은 적도 band이고 $S^1$로 줄어든다

$U_z\cap U_w\simeq\mathbf C^*$이고

$$
\mathbf C^*\simeq S^1
$$

로 deformation retract한다. 따라서 overlap의 핵심 closed $1$-form은

$$
\frac{d\theta}{2\pi}
$$

이다.

우리 tangent transition은 winding $2$이므로

$$
\alpha=2\frac{d\theta}{2\pi}
=\frac1\pi d\theta.
$$

## 6.2 진짜 partition of unity를 사용한 연결사상

$U_z,U_w$에 subordinate한 smooth partition of unity를

$$
\chi_z+\chi_w=1
$$

로 잡는다. $\chi_z$는 $w$-pole 근방에서 $0$, $\chi_w$는 $z$-pole 근방에서 $0$이 되게 한다.

local $1$-form을

$$
A_z=\chi_w\alpha,
\qquad
A_w=-\chi_z\alpha
$$

로 둔다. overlap에서

$$
A_w-A_z
=-(\chi_z+\chi_w)\alpha
=-\alpha.
$$

또 $d\alpha=0$이므로

$$
\begin{aligned}
dA_z
&=d\chi_w\wedge\alpha,\\
dA_w
&=-d\chi_z\wedge\alpha
=d\chi_w\wedge\alpha.
\end{aligned}
$$

따라서 두 local $2$-form은 하나의 global $2$-form으로 붙는다.

$$
\boxed{
F_{\mathrm{MV}}=dA_z=dA_w.
}
$$

이것이 Mayer–Vietoris connecting map의 실제 계산이다.

## 6.3 적분은 winding number를 그대로 회수한다

$\chi_w$가 남쪽에서 $0$, 북쪽에서 $1$로 변하도록 band coordinate를 잡으면

$$
\begin{aligned}
\int_{S^2}F_{\mathrm{MV}}
&=\int_{\mathrm{band}}d\chi_w\wedge\alpha\\
&=\left(\int d\chi_w\right)
\left(\int_{S^1}\alpha\right)\\
&=1\cdot2\\
&=2.
\end{aligned}
$$

따라서

$$
\boxed{
\int_{S^2}F_{\mathrm{MV}}=2.
}
$$

이 $F_{\mathrm{MV}}$는 normalized Euler/Chern curvature representative다.

$$
[F_{\mathrm{MV}}]
=
\left[\frac{K\,dA}{2\pi}\right].
$$

일반적인 cutoff를 쓰면 두 form은 pointwise로 같을 필요는 없다. 하지만 둘 다 적분이 $2$이고 $H^2(S^2)$가 $1$차원이므로 같은 cohomology class를 나타낸다.

## 6.4 이것이 Mayer–Vietoris connecting map이다

두 pole-deleted chart는 각각 contractible하므로

$$
H^1(U_z)=H^1(U_w)=0.
$$

반면 overlap은 $\mathbf C^*\simeq S^1$이므로

$$
H^1(U_z\cap U_w)\simeq\mathbf R[d\theta].
$$

de Rham Mayer–Vietoris sequence의 해당 부분은

$$
0
\longrightarrow
H^1(U_z\cap U_w)
\xrightarrow{\delta_{\mathrm{MV}}}
H^2(S^2)
\longrightarrow
0
$$

가 된다. 위 partition-of-unity 계산은 이 추상 화살표를 실제 식으로 만든 것이다.

$$
\boxed{
\delta_{\mathrm{MV}}[\alpha]
=[F_{\mathrm{MV}}].
}
$$

우리의 $\alpha$는 적도에서 적분이 $2$이므로

$$
\delta_{\mathrm{MV}}[\alpha]
=
\left[\frac{K\,dA}{2\pi}\right]
$$

이고, 이 class의 전체 적분은 $2$다.

---

# 7. round metric의 connection은 winding form을 정확히 어떻게 확장하는가

앞에서 계산한 실제 Levi-Civita connection을 $2\pi$로 나눈다.

$$
\mathcal A_z
=\frac{\omega_z}{2\pi}
=\frac{r^2}{1+r^2}\frac{d\theta}{\pi},
$$

$$
\mathcal A_w
=\frac{\omega_w}{2\pi}
=-\frac{1}{1+r^2}\frac{d\theta}{\pi}.
$$

따라서

$$
\mathcal A_w-\mathcal A_z
=-\frac1\pi d\theta
=-\alpha.
$$

즉 실제 round metric의 local connection forms가 overlap의 winding form을 정확히 받아서 붙는다.

이제 $d$를 취하면

$$
\begin{aligned}
d\mathcal A_z
&=\frac{1}{2\pi}d\omega_z\\
&=\frac{K\,dA}{2\pi}.
\end{aligned}
$$

구체적으로

$$
\begin{aligned}
d\mathcal A_z
&=d\left(
\frac{r^2}{1+r^2}\frac{d\theta}{\pi}
\right)\\
&=\frac{2r}{\pi(1+r^2)^2}dr\wedge d\theta\\
&=\frac{2}{\pi(1+r^2)^2}dx\wedge dy.
\end{aligned}
$$

한편

$$
\frac{K\,dA}{2\pi}
=
\frac1{2\pi}
\frac4{(1+r^2)^2}dx\wedge dy
=
\frac{2}{\pi(1+r^2)^2}dx\wedge dy.
$$

따라서

$$
\boxed{
d\mathcal A_z=d\mathcal A_w=\frac{K\,dA}{2\pi}}.
$$

이 식이 교수님이 말한 계산선의 가장 구체적인 형태다.

$$
\boxed{
\text{overlap의 winding form}
\longrightarrow
\text{두 chart의 connection forms}
\xrightarrow{d}
\frac{K\,dA}{2\pi}.
}
$$

---

# 8. ring gluing과 Mayer–Vietoris gluing을 한 표에 놓기

| 대상 | $U_z$ | $U_w$ | overlap 조건 |
|---|---|---|---|
| regular function | $f_z\in\mathbf C[z]$ | $f_w\in\mathbf C[w]$ | $f_z(z)=f_w(1/z)$ |
| tangent frame | $e_z=\partial_z$ | $e_w=\partial_w$ | $e_w=-z^2e_z$ |
| conformal potential | $u_z$ | $u_w$ | $u_w(1/z)-u_z(z)=2\log|z|$ |
| connection | $\omega_z$ | $\omega_w$ | $\omega_w-\omega_z=-2d\theta$ |
| curvature | $d\omega_z$ | $d\omega_w$ | 둘이 같아서 global $K\,dA$로 붙음 |

## 8.1 global regular function을 실제로 계산한다

$$
f_z(z)\in\mathbf C[z],
\qquad
f_w(w)\in\mathbf C[w]
$$

가 같은 global regular function을 나타내려면

$$
f_z(z)=f_w(1/z)
$$

이어야 한다.

왼쪽은 $z$의 nonnegative powers만 갖고, 오른쪽은 nonpositive powers만 갖는다. 둘이 Laurent polynomial로 같으려면 상수항밖에 남을 수 없다.

$$
\Gamma(\mathbf P^1,\mathcal O)=\mathbf C.
$$

## 8.2 tangent bundle은 function이 아니라 transition unit으로 붙는다

평범한 function은 overlap에서 값이 같아야 한다. 반면 tangent frame은

$$
e_w=-z^2e_z
$$

처럼 unit을 곱해 붙는다.

그 unit의 Laurent exponent $2$가 winding number이고, connection 차이 $-2d\theta$가 그 smooth differential-geometric 그림이다.

---

# 9. 수요일 스터디용 최소 진행 순서

## 계산 1 — ring 세 개를 적는다

$$
\mathbf C[z],
\qquad
\mathbf C[w]=\mathbf C[z^{-1}],
\qquad
\mathbf C[z,z^{-1}].
$$

그리고 overlap ring의 unit이 $cz^n$뿐임을 확인한다.

## 계산 2 — $dz=-w^{-2}dw$를 metric에 대입한다

$$
\frac{4|dz|^2}{(1+|z|^2)^2}
=
\frac{4|dw|^2}{(1+|w|^2)^2}.
$$

## 계산 3 — 두 conformal potential의 차이를 구한다

$$
u_w(1/z)-u_z(z)=2\log|z|.
$$

## 계산 4 — overlap에서 라플라시안이 사라짐을 본다

$$
\Delta\log|z|=0
\qquad(z\neq0).
$$

## 계산 5 — connection을 직접 적는다

$$
\omega_z=\frac{2r^2}{1+r^2}d\theta,
$$

$$
\omega_w=-\frac{2}{1+r^2}d\theta.
$$

## 계산 6 — 차이에서 winding을 읽는다

$$
\omega_w-\omega_z=-2d\theta,
$$

$$
\frac1{2\pi}\int_{S^1}2d\theta=2.
$$

## 계산 7 — $d$를 취해 곡률을 얻는다

$$
d\omega_z=d\omega_w=K\,dA.
$$

정규화하면

$$
\boxed{
\frac1{2\pi}d\omega
=
\frac{K\,dA}{2\pi},
\qquad
\int_{S^2}\frac{K\,dA}{2\pi}=2.
}
$$

---

# 10. 스스로 확인할 기본 문제

1. $\mathbf C[z,z^{-1}]^\times=\{cz^n\}$을 증명하라.
2. $dz=-w^{-2}dw$에서 $u_w(1/z)-u_z(z)=2\log|z|$를 얻어라.
3. $\Delta\log r=0$을 polar Laplacian으로 계산하라.
4. $u_z=\log 2-\log(1+r^2)$에서 $\Delta u_z=-4/(1+r^2)^2$를 계산하라.
5. $\omega=-*du$에서 $\omega_z=2r^2(1+r^2)^{-1}d\theta$를 얻어라.
6. $w=1/z$를 사용하여 $\omega_w=-2(1+r^2)^{-1}d\theta$를 얻어라.
7. $g=-z^2$에 대해 $(2\pi i)^{-1}\oint g^{-1}dg=2$를 계산하라.
8. $d\omega_z=4(1+r^2)^{-2}dx\wedge dy$를 확인하라.
9. 진짜 partition of unity로 만든 $F_{\mathrm{MV}}$와 $K\,dA/(2\pi)$가 왜 pointwise로 같을 필요는 없지만 같은 cohomology class인지 설명하라.
10. cotangent transition $dw=-z^{-2}dz$가 degree $-2$를 준다는 것을 설명하라.

---

# 11. 마지막 압축

이번 계산에서 $dz=-w^{-2}dw$는 두 가지 방식으로 기여한다.

첫째, 절댓값은 conformal potential을 바꾼다.

$$
\left|\frac{dz}{dw}\right|=|w|^{-2}
\quad\Longrightarrow\quad
u_w(1/z)-u_z(z)=2\log|z|.
$$

둘째, 위상은 orthonormal frame을 회전시킨다.

$$
\arg\left(-w^{-2}\right)
\quad\Longrightarrow\quad
\omega_w-\omega_z=-2d\theta.
$$

이 closed $1$-form의 period가 winding number $2$다. Mayer–Vietoris의 partition-of-unity 계산은 이 overlap $1$-form을 두 chart의 connection으로 나누어 놓고, $d$를 취해 global curvature $2$-form을 만든다.

$$
\boxed{
-z^2\in\mathbf C[z,z^{-1}]^\times
\longleftrightarrow
2\log|z|
\longleftrightarrow
2d\theta
\longleftrightarrow
\frac{K\,dA}{2\pi}.
}
$$

하나의 transition unit이 algebraic ring, conformal metric, winding number, connection, curvature를 동시에 묶는다.
