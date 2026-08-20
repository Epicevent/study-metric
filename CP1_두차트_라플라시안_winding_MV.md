# 함수 $z$ 하나에서 구면의 곡률까지

## $\mathbf P^1=S^2$의 chart ring, zero·pole, $\log|z|$, winding, connection, Mayer–Vietoris

이 노트는 함수 하나만 끝까지 민다.

$$
f(z)=z.
$$

이 함수의 zero와 pole을 먼저 계산하고, 같은 정수를

- Laurent exponent,
- 원주 적분과 winding,
- $\log|z|$의 라플라시안 질량,
- tangent bundle의 transition $-z^2$,
- round metric의 connection 차이,
- 곡률 적분

에서 다시 찾는다.

비교할 두 식은 다음이다.

$$
\boxed{
\operatorname{div}(z)=[0]-[\infty]
}
$$

과

$$
\boxed{
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2.
}
$$

첫 번째는 **함수** $z$의 zero와 pole을 센다. 두 번째는 **tangent bundle**의 degree를 센다. 둘을 바로 같다고 놓으면 안 된다. 둘 사이를 연결하는 실제 물건은

$$
\boxed{
\frac{dz}{z}=d\log|z|+i\,d\theta
}
$$

와

$$
\boxed{
g(z)=-z^2}
$$

이다.

---

# 0. 계산 convention

첨부 노트와 같은 반지름 $1$의 round metric을 사용한다.

$$
\boxed{
 ds^2=\frac{4|dz|^2}{(1+|z|^2)^2}
}
$$

실좌표 $z=x+iy$에서

$$
ds^2=e^{2\phi}(dx^2+dy^2)
$$

로 쓰면

$$
\boxed{
\phi=\log2-\log(1+x^2+y^2).
}
$$

가우스곡률 공식은

$$
\boxed{
K=-e^{-2\phi}\Delta\phi
}
$$

이고, 실제 적분되는 곡률 $2$-form은

$$
\boxed{
K\,dA=-\Delta\phi\,dx\wedge dy.
}
$$

orientation과 Hodge star는

$$
dx\wedge dy>0,
$$

$$
*dx=dy,
\qquad
*dy=-dx
$$

로 고정한다. 이 convention에서 Levi-Civita connection $1$-form은

$$
\boxed{
\omega=\phi_y\,dx-\phi_x\,dy=-*d\phi
}
$$

이고

$$
\boxed{
d\omega=K\,dA}
$$

이다.

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

로 둔다. overlap에서는

$$
\boxed{w=z^{-1}.}
$$

## 1.1 세 coordinate ring

$$
\mathcal O_{\mathrm{alg}}(U_z)=\mathbf C[z],
$$

$$
\mathcal O_{\mathrm{alg}}(U_w)=\mathbf C[w]
=\mathbf C[z^{-1}],
$$

$$
\boxed{
\mathcal O_{\mathrm{alg}}(U_z\cap U_w)
=\mathbf C[z,z^{-1}].
}
$$

따라서 예상한

$$
\mathbf C[X],
\qquad
\mathbf C[1/X],
\qquad
\mathbf C[X,1/X]
$$

가 맞다.

- $\mathbf C[1/X]$는 $X^{-1}$의 nonnegative powers만 허용한다.
- $\mathbf C[X,1/X]$는 양수와 음수 지수를 모두 허용하는 Laurent polynomial ring이다.

## 1.2 overlap ring의 unit

$$
\boxed{
\mathbf C[z,z^{-1}]^\times
=
\{cz^n:c\in\mathbf C^\times,\ n\in\mathbf Z\}.
}
$$

Laurent polynomial

$$
h(z)=\sum_{j=m}^{M}a_jz^j,
\qquad a_ma_M\neq0
$$

가 Laurent polynomial inverse를 가진다고 하자. 곱이 $1$이면 가장 낮은 지수와 가장 높은 지수가 모두 $0$이어야 한다. 그러려면 $m=M$이어야 하므로 $h=cz^n$이다.

이 정수 $n$은 원 $|z|=1$ 위의 winding number와 같다.

$$
\boxed{
\frac{1}{2\pi i}
\oint_{|z|=1}h^{-1}dh=n.
}
$$

## 1.3 세 함수 층위를 섞지 않는다

$$
\mathbf C[z]
\subset
\mathcal O_{\mathrm{hol}}(U_z)
\subset
C^\infty(U_z).
$$

- $z$와 $z^{-1}$은 algebraic 또는 holomorphic data다.
- $\log|z|$와 $\phi$는 smooth real-valued data다.
- 둘을 연결하는 것은 logarithmic derivative $dz/z$다.

---

# 2. 대수적으로 $z$의 zero와 pole을 계산한다

함수 $z$는 $U_z$에서는 regular하지만 $\mathbf P^1$ 전체에서는 rational function이다.

## 2.1 $z=0$에서

점 $0$의 local parameter는 그대로 $z$다.

$$
z=z^1\cdot1.
$$

뒤의 $1$은 local ring의 unit이므로

$$
\boxed{
\operatorname{ord}_0(z)=1.
}
$$

즉 $z$는 $0$에서 simple zero를 가진다.

## 2.2 무한대에서

무한대의 local coordinate는

$$
w=\frac1z.
$$

따라서

$$
z=w^{-1}.
$$

즉

$$
\boxed{
\operatorname{ord}_\infty(z)=-1.
}
$$

$z$는 무한대에서 simple pole을 가진다.

## 2.3 divisor

따라서

$$
\boxed{
\operatorname{div}(z)=[0]-[\infty].
}
$$

- local parameter의 양의 지수는 zero order다.
- 음의 지수는 pole order다.
- nonzero unit은 order에 기여하지 않는다.

zero order와 pole order의 합은

$$
1+(-1)=0.
$$

이것이 rational function의 principal divisor가 degree $0$인 가장 작은 예다.

---

# 3. 같은 zero와 pole을 $\log|z|$, winding, 라플라시안으로 본다

## 3.1 punctured plane에서는 harmonic이다

polar coordinate를

$$
z=re^{i\theta}
$$

로 둔다.

$$
\log|z|=\log r.
$$

$r>0$에서는

$$
\begin{aligned}
\Delta\log r
&=\frac1r\frac{\partial}{\partial r}
\left(r\frac{\partial}{\partial r}\log r\right)\\
&=\frac1r\frac{\partial}{\partial r}(1)\\
&=0.
\end{aligned}
$$

따라서

$$
\boxed{
\Delta\log|z|=0
\qquad(z\neq0).
}
$$

## 3.2 Hodge star는 winding form을 만든다

$$
d\log r=\frac{dr}{r}.
$$

평면에서

$$
*dr=r\,d\theta
$$

이므로

$$
\boxed{
*d\log|z|=d\theta.
}
$$

작은 원을 한 바퀴 돌면

$$
\boxed{
\frac1{2\pi}
\int_{|z|=\varepsilon}*d\log|z|
=1.
}
$$

이 정수는

$$
\operatorname{ord}_0(z)=1
$$

과 같다.

## 3.3 원점의 라플라시안 질량

punctured disk에서는 $d*d\log|z|=0$이다. 그러나 원점을 포함한 disk에서 Stokes를 쓰면

$$
\begin{aligned}
\int_{|z|\le R}d*d\log|z|
&=\int_{|z|=R}*d\log|z|\\
&=2\pi.
\end{aligned}
$$

따라서 distribution 또는 current의 의미에서

$$
\boxed{
d*d\log|z|=2\pi\,\delta_0.}
$$

simple zero 하나가 라플라시안에 질량 $2\pi$로 나타난다.

## 3.4 무한대의 pole

$w=1/z$이므로

$$
\log|z|=-\log|w|.
$$

따라서 $w=0$, 즉 무한대에서는

$$
\boxed{
d*d\log|z|=-2\pi\,\delta_\infty.}
$$

두 chart를 합치면

$$
\boxed{
\frac1{2\pi}d*d\log|z|
=
\delta_0-\delta_\infty.
}
$$

이는

$$
\operatorname{div}(z)=[0]-[\infty]
$$

의 라플라시안 표현이다.

현재 직접 확인한 일반형은 다음과 같다. $f=t^m\cdot u$이고 $u$가 local unit이면

$$
\log|f|=m\log|t|+\log|u|,
$$

따라서

$$
\boxed{
\operatorname{ord}_P(f)
=
\frac1{2\pi}\int_{\partial D_P}d\arg f
=
\frac1{2\pi}\int_{D_P}d*d\log|f|.
}
$$

---

# 4. $dz=-w^{-2}dw$: 함수 $z$에서 tangent bundle로

## 4.1 cotangent frame

$$
z=\frac1w
$$

를 미분하면

$$
\boxed{
dz=-w^{-2}dw.}
$$

반대 방향으로는

$$
\boxed{dw=-z^{-2}dz.}
$$

따라서 cotangent frame의 exponent는 $-2$다.

## 4.2 tangent frame

$$
e_z=\frac{\partial}{\partial z},
\qquad
e_w=\frac{\partial}{\partial w}
$$

라고 하자. chain rule에 의해

$$
\begin{aligned}
e_w
&=\frac{dz}{dw}e_z\\
&=-w^{-2}e_z\\
&=-z^2e_z.
\end{aligned}
$$

따라서 tangent bundle의 transition function은

$$
\boxed{g(z)=-z^2.}
$$

이는 overlap ring의 unit이다.

$$
g\in\mathbf C[z,z^{-1}]^\times.
$$

## 4.3 logarithmic derivative의 실수부와 허수부

$g=-z^2$이므로

$$
\boxed{
g^{-1}dg=2\frac{dz}{z}.}
$$

또

$$
\frac{dz}{z}=d\log r+i\,d\theta.
$$

따라서

$$
\boxed{
g^{-1}dg
=2d\log|z|+2i\,d\theta.}
$$

- real part $2d\log|z|$는 conformal factor의 변화를 기록한다.
- imaginary part $2d\theta$는 frame의 회전과 winding을 기록한다.

원 $|z|=1$에서는 $d\log r=0$이므로

$$
\frac{1}{2\pi i}g^{-1}dg
=
\frac1\pi d\theta.
$$

따라서

$$
\boxed{
\frac{1}{2\pi i}
\oint_{|z|=1}g^{-1}dg=2.
}
$$

이것이

$$
T\mathbf P^1\simeq\mathcal O(2)
$$

의 winding number다.

---

# 5. $dz=-w^{-2}dw$가 round metric의 conformal factor에 기여하는 항

## 5.1 $z$-chart

$$
ds^2=\frac{4|dz|^2}{(1+|z|^2)^2}
=e^{2\phi_z}|dz|^2
$$

이므로

$$
\boxed{
\phi_z(z)=\log2-\log(1+|z|^2).
}
$$

## 5.2 $w$-chart

$$
|dz|^2=|w|^{-4}|dw|^2
$$

이고

$$
1+|z|^2
=1+|w|^{-2}
=\frac{1+|w|^2}{|w|^2}.
$$

따라서

$$
\begin{aligned}
ds^2
&=\frac{4|w|^{-4}|dw|^2}
{\left((1+|w|^2)/|w|^2\right)^2}\\
&=\frac{4|dw|^2}{(1+|w|^2)^2}.
\end{aligned}
$$

즉

$$
\boxed{
\phi_w(w)=\log2-\log(1+|w|^2).
}
$$

## 5.3 두 local potential의 차이

$w=1/z$를 대입하면

$$
\begin{aligned}
\phi_w(1/z)
&=\log2-\log(1+|z|^{-2})\\
&=\log2-\log(1+|z|^2)+2\log|z|.
\end{aligned}
$$

따라서 overlap에서

$$
\boxed{
\phi_w(1/z)-\phi_z(z)=2\log|z|.
}
$$

이 항은

$$
\log\left|\frac{dz}{dw}\right|
$$

에서 왔다. overlap에서는

$$
\Delta\log|z|=0
$$

이므로 local potential은 서로 다르지만 같은 curvature $2$-form을 만든다.

---

# 6. 두 chart에서 라플라시안으로 곡률을 계산한다

## 6.1 $z$-chart

$r=|z|$라 하면

$$
\phi_z(r)=\log2-\log(1+r^2).
$$

먼저

$$
(\phi_z)_r=-\frac{2r}{1+r^2}.
$$

다시 미분하면

$$
(\phi_z)_{rr}
=-\frac{2(1-r^2)}{(1+r^2)^2}.
$$

따라서

$$
\begin{aligned}
\Delta\phi_z
&=(\phi_z)_{rr}+\frac1r(\phi_z)_r\\
&=-\frac{2(1-r^2)}{(1+r^2)^2}
-\frac2{1+r^2}\\
&=-\frac4{(1+r^2)^2}.
\end{aligned}
$$

그러므로

$$
\boxed{
K\,dA
=-\Delta\phi_z\,dx\wedge dy
=\frac4{(1+r^2)^2}dx\wedge dy.
}
$$

그런데

$$
dA=e^{2\phi_z}dx\wedge dy
=\frac4{(1+r^2)^2}dx\wedge dy.
$$

따라서

$$
\boxed{K=1.}
$$

## 6.2 $w$-chart

$s=|w|$라 하면 같은 계산으로

$$
\boxed{
K\,dA
=\frac4{(1+s^2)^2}d\xi\wedge d\eta
}
$$

를 얻는다. 여기서 $w=\xi+i\eta$다.

$w=1/z$ 아래

$$
d\xi\wedge d\eta
=\left|\frac{dw}{dz}\right|^2dx\wedge dy
=r^{-4}dx\wedge dy
$$

이고

$$
\frac4{(1+r^{-2})^2}r^{-4}
=
\frac4{(1+r^2)^2}.
$$

따라서 두 chart의 곡률 $2$-form은 실제로 같은 form이다.

---

# 7. connection 차이에서 winding $2$를 읽는다

## 7.1 $z$-chart connection

$$
(\phi_z)_x=-\frac{2x}{1+r^2},
\qquad
(\phi_z)_y=-\frac{2y}{1+r^2}.
$$

따라서

$$
\begin{aligned}
\omega_z
&=(\phi_z)_y\,dx-(\phi_z)_x\,dy\\
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

$d$를 취하면

$$
\begin{aligned}
d\omega_z
&=d\left(\frac{2r^2}{1+r^2}\right)\wedge d\theta\\
&=\frac{4r}{(1+r^2)^2}dr\wedge d\theta\\
&=\frac4{(1+r^2)^2}dx\wedge dy.
\end{aligned}
$$

따라서

$$
\boxed{d\omega_z=K\,dA.}
$$

## 7.2 $w$-chart connection

$w=se^{i\varphi}$라 하면

$$
\omega_w=\frac{2s^2}{1+s^2}d\varphi.
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

그러므로

$$
\boxed{
\omega_w-\omega_z=-2d\theta.
}
$$

$d(d\theta)=0$ on overlap이므로

$$
d\omega_w=d\omega_z.
$$

local connection은 다르지만 curvature는 global하게 붙는다.

---

# 8. 함수의 divisor와 tangent section의 zero를 구분한다

## 8.1 함수 $z$

함수 $z$는 trivial line bundle의 meromorphic section이다.

$$
\boxed{
\operatorname{div}(z)=[0]-[\infty].
}
$$

zero와 pole이 하나씩 있어 총 degree는 $0$이다.

## 8.2 tangent section $s=z\partial_z$

vector field

$$
\boxed{
s=z\frac{\partial}{\partial z}}
$$

를 보자.

$z$-chart에서는 coefficient가 $z$이므로 $z=0$에서 simple zero를 가진다.

$w$-chart에서는

$$
\frac{\partial}{\partial z}
=\frac{dw}{dz}\frac{\partial}{\partial w}
=-w^2\frac{\partial}{\partial w}.
$$

따라서

$$
\begin{aligned}
s
&=z\frac{\partial}{\partial z}\\
&=\frac1w\left(-w^2\frac{\partial}{\partial w}\right)\\
&=-w\frac{\partial}{\partial w}.
\end{aligned}
$$

즉 $w=0$, 곧 무한대에서도 simple zero를 가진다.

따라서

$$
\boxed{
\operatorname{div}(s)=[0]+[\infty].
}
$$

총 zero multiplicity는

$$
1+1=2.
$$

그리고 round metric의 curvature도

$$
\boxed{
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2
}
$$

를 준다.

이제 같은 정수 $2$가 세 번 나타난다.

- tangent section의 zero 총수,
- transition $-z^2$의 winding,
- curvature 적분.

---

# 9. Mayer–Vietoris: 적도의 winding form을 구면의 curvature class로 올린다

## 9.1 overlap의 real closed $1$-form

$U_z\cap U_w\simeq\mathbf C^*$는 $S^1$로 deformation retract한다.

transition $g=-z^2$의 phase에서 real closed form을 잡는다.

$$
\boxed{
\alpha_{\mathbb R}
=\frac1{2\pi}d\arg g
=\frac1\pi d\theta.
}
$$

따라서

$$
\boxed{
\int_{S^1}\alpha_{\mathbb R}=2.
}
$$

주의할 점은 $g^{-1}dg/(2\pi i)$ 전체가 overlap에서 complex-valued라는 것이다. Mayer–Vietoris의 real de Rham 계산에는 그 phase part인 $\alpha_{\mathbb R}$를 사용한다.

## 9.2 partition of unity

$U_z,U_w$에 subordinate한 partition of unity를

$$
\chi_z+\chi_w=1
$$

로 잡는다.

local $1$-form을

$$
A_z=\chi_w\alpha_{\mathbb R},
\qquad
A_w=-\chi_z\alpha_{\mathbb R}
$$

로 둔다.

overlap에서

$$
A_w-A_z=-\alpha_{\mathbb R}.
$$

또 $d\alpha_{\mathbb R}=0$이므로

$$
\begin{aligned}
dA_z
&=d\chi_w\wedge\alpha_{\mathbb R},\\
dA_w
&=-d\chi_z\wedge\alpha_{\mathbb R}\\
&=d\chi_w\wedge\alpha_{\mathbb R}.
\end{aligned}
$$

따라서 두 local $2$-form은 하나의 global $2$-form으로 붙는다.

$$
\boxed{
F_{\mathrm{MV}}=dA_z=dA_w.
}
$$

## 9.3 적분

cutoff가 band를 가로질러 $0$에서 $1$로 증가하도록 orientation을 잡으면

$$
\begin{aligned}
\int_{\mathbf P^1}F_{\mathrm{MV}}
&=\int_{\mathrm{band}}d\chi_w\wedge\alpha_{\mathbb R}\\
&=\left(\int d\chi_w\right)
\left(\int_{S^1}\alpha_{\mathbb R}\right)\\
&=1\cdot2\\
&=2.
\end{aligned}
$$

따라서

$$
\boxed{
\int_{\mathbf P^1}F_{\mathrm{MV}}=2.
}
$$

cutoff 선택에 따라 $F_{\mathrm{MV}}$의 pointwise 모양은 달라질 수 있다. 그러나 cohomology class는 winding만으로 정해진다.

## 9.4 round connection과 비교

round metric의 normalized connection을

$$
\mathcal A_z=\frac{\omega_z}{2\pi},
\qquad
\mathcal A_w=\frac{\omega_w}{2\pi}
$$

로 두면

$$
\mathcal A_w-\mathcal A_z
=-\frac1\pi d\theta
=-\alpha_{\mathbb R}.
$$

그리고

$$
\boxed{
 d\mathcal A_z=d\mathcal A_w
 =\frac{K\,dA}{2\pi}.
}
$$

따라서

$$
\boxed{
[F_{\mathrm{MV}}]
=
\left[\frac{K\,dA}{2\pi}\right].
}
$$

Mayer–Vietoris의 partition-of-unity 계산과 round metric의 Levi-Civita connection은 같은 overlap winding class를 서로 다른 방식으로 확장한다.

---

# 10. 한 표로 정리

| 관찰 대상 | local expression | 검출되는 정수 |
|---|---|---:|
| rational function $z$ | $z$ at $0$, $w^{-1}$ at $\infty$ | $+1,-1$ |
| divisor of $z$ | $[0]-[\infty]$ | total $0$ |
| $\log|z|$ | $*d\log|z|=d\theta$ | winding $1$ |
| tangent transition | $g=-z^2$ | winding $2$ |
| tangent section | $z\partial_z=-w\partial_w$ | zeros $1+1=2$ |
| round connection | $\omega_w-\omega_z=-2d\theta$ | period $2$ |
| curvature | $d\omega=K\,dA$ | $\int KdA/(2\pi)=2$ |

가장 중요한 구분은 다음이다.

$$
\boxed{
\text{함수 }z:\ [0]-[\infty]
\qquad\neq\qquad
\text{tangent section }z\partial_z:\ [0]+[\infty].
}
$$

함수는 trivial line bundle의 meromorphic section이어서 zero와 pole이 상쇄된다. tangent section은 nontrivial bundle의 holomorphic section이어서 zero 총수가 curvature degree $2$와 맞는다.

---

# 11. 스터디 진행 순서

1. 세 ring을 적는다.
   $$
   \mathbf C[z],\qquad
   \mathbf C[z^{-1}],\qquad
   \mathbf C[z,z^{-1}].
   $$
2. $\operatorname{ord}_0(z)=1$, $\operatorname{ord}_\infty(z)=-1$을 local coordinate로 확인한다.
3. $*d\log|z|=d\theta$와 $(2\pi)^{-1}\int d\theta=1$을 계산한다.
4. $(2\pi)^{-1}d*d\log|z|=\delta_0-\delta_\infty$가 divisor와 같은 정보를 담는지 본다.
5. $dz=-w^{-2}dw$와 $e_w=-z^2e_z$를 계산한다.
6. $g^{-1}dg=2d\log|z|+2i\,d\theta$에서 modulus와 phase를 분리한다.
7. $\phi_w(1/z)-\phi_z(z)=2\log|z|$를 계산한다.
8. $\omega_w-\omega_z=-2d\theta$를 계산한다.
9. $d\omega=K\,dA$와 $\int KdA/(2\pi)=2$를 확인한다.
10. $s=z\partial_z=-w\partial_w$가 $0$과 $\infty$에서 각각 한 번 사라지는지 확인한다.
11. POU로 $\alpha_{\mathbb R}=d\theta/\pi$를 global $2$-form으로 올리고 적분이 $2$인지 확인한다.

---

# 12. 검문 문제

1. $\mathbf C[z,z^{-1}]^\times=\{cz^n\}$을 증명하라.
2. $\operatorname{div}(z)=[0]-[\infty]$를 두 local coordinate로 계산하라.
3. $*d\log|z|=d\theta$를 $x,y$ 좌표에서 직접 확인하라.
4. 작은 원의 경계적분으로 $d*d\log|z|=2\pi\delta_0$를 설명하라.
5. $g=-z^2$에 대해 $(2\pi i)^{-1}\oint g^{-1}dg=2$를 계산하라.
6. $\phi_w(1/z)-\phi_z(z)=2\log|z|$를 metric 변환으로 얻어라.
7. $\phi_z=\log2-\log(1+r^2)$에서 $\Delta\phi_z=-4/(1+r^2)^2$를 계산하라.
8. $\omega_z=2r^2(1+r^2)^{-1}d\theta$를 $\omega=-*d\phi$에서 유도하라.
9. $s=z\partial_z=-w\partial_w$를 확인하고 zero 총수를 계산하라.
10. 함수 $z$의 divisor degree는 $0$인데 tangent section의 zero degree는 $2$인 이유를 설명하라.
11. POU로 만든 $F_{\mathrm{MV}}$와 $K\,dA/(2\pi)$가 pointwise로 같을 필요는 없지만 같은 cohomology class인 이유를 설명하라.

---

# 13. 마지막 압축

함수 $z$ 하나에서 세 언어가 만난다.

## 대수

$$
\boxed{
 z\in\mathbf C[z],
 \qquad
 z=w^{-1}\in\mathbf C[w,w^{-1}],
 \qquad
 \operatorname{div}(z)=[0]-[\infty].
}
$$

## 해석

$$
\boxed{
\frac{dz}{z}=d\log|z|+i\,d\theta,
\qquad
\frac1{2\pi}d*d\log|z|
=\delta_0-\delta_\infty.
}
$$

## 곡률

$$
\boxed{
g=-z^2,
\qquad
\omega_w-\omega_z=-2d\theta,
\qquad
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2.
}
$$

그리고 가장 구체적인 bundle section은

$$
\boxed{
z\partial_z=-w\partial_w}
$$

이다. 이 tangent section은 $0$과 $\infty$에서 각각 한 번 사라진다.

따라서 이 토이모델에서 직접 보이는 계산선은 다음이다.

$$
\boxed{
\text{Laurent exponent}
\longleftrightarrow
\text{zero·pole order}
\longleftrightarrow
\text{winding}
\longleftrightarrow
\text{connection 차이}
\longleftrightarrow
\text{curvature degree}.
}
$$
