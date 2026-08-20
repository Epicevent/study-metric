# 라플라시안으로 바꾸고 싶다

## Gaussian 2-form에서 방사방향을 만들고, 뒤늦게 Hodge star를 발견하여 구면까지

출발은 개념이 아니다.

다음 적분을 Green 정리나 발산정리로 풀어 보고 싶다.

\[
\iint_{\mathbf R^2}e^{-x^2-y^2}\,dx\,dy.
\]

라플라시안으로 바꿀 수 있다면 좋겠다.

\[
e^{-x^2-y^2}=-\Delta\phi
\]

인 함수 \(\phi\)를 찾으면

\[
\iint_D e^{-x^2-y^2}\,dx\,dy
=-\iint_D\Delta\phi\,dx\,dy
\]

가 되고, 오른쪽은 경계의 flux로 바뀐다.

그런데 \(\phi\)를 어떻게 찾는가?

바로 PDE를 풀기 전에, 일단 한 번 적분해서 원주방향 1-form을 찾는다. 그 원주방향을 방사방향으로 돌리면 gradient가 보일지도 모른다.

이 계산을 하고 난 뒤에야 그 90도 회전에 **Hodge star**라는 이름을 붙일 것이다.

---

# 1. 일단 \(d\omega=\Omega\)를 풀어 본다

다음 2-form을 잡는다.

\[
\boxed{
\Omega=e^{-x^2-y^2}\,dx\wedge dy.
}
\]

계산에 필요한 규칙은 하나다. 1-form

\[
\omega=P\,dx+Q\,dy
\]

에 대해

\[
\boxed{
d\omega=(Q_x-P_y)\,dx\wedge dy.}
\]

그리고 Stokes–Green 공식은

\[
\int_Dd\omega=\int_{\partial D}\omega
\]

이다.

## 1.1 회전대칭이 있으니 \(d\theta\)를 써 본다

\[
r^2=x^2+y^2,
\qquad
x=r\cos\theta,
\qquad
y=r\sin\theta.
\]

직접 미분하면

\[
\boxed{dx\wedge dy=r\,dr\wedge d\theta.}
\]

따라서

\[
\Omega=e^{-r^2}r\,dr\wedge d\theta.
\]

원점 주위로 회전대칭인 1-form을

\[
\omega=A(r)d\theta
\]

꼴로 찾아보자.

\[
d\omega=A'(r)dr\wedge d\theta.
\]

그러므로

\[
A'(r)=re^{-r^2}.
\]

적분하면

\[
\boxed{A(r)=C-\frac12e^{-r^2}.}
\]

즉 \(d\omega=\Omega\)를 만족하는 1-form은 여러 개다.

\[
\omega_C=\left(C-\frac12e^{-r^2}\right)d\theta.
\]

## 1.2 적분상수는 장식이 아니다

가장 간단히 \(C=0\)을 택하면

\[
\omega_\infty=-\frac12e^{-r^2}d\theta.
\]

무한대에서는 잘 사라진다. 하지만 \(d\theta\)는 원점에서 singular하므로, 이 1-form은 원점을 포함한 disk 전체에 smooth하지 않다.

원점에서 smooth하게 만들고 싶으면 \(C=1/2\)를 택한다.

\[
\boxed{
\omega_0=rac{1-e^{-r^2}}2d\theta.
}
\]

왜 smooth한지 보자.

\[
\boxed{
d\theta=\frac{-y\,dx+x\,dy}{r^2}.}
\]

또

\[
1-e^{-r^2}=r^2+O(r^4).
\]

따라서

\[
\omega_0
=
\frac{1-e^{-r^2}}{2r^2}
(-y\,dx+x\,dy)
\]

에서 coefficient는 원점까지 유한하게 연장된다.

두 선택의 차이는

\[
\boxed{
\omega_0-\omega_\infty=\frac12d\theta.
}
\]

두 1-form은 서로 다르지만

\[
d\omega_0=d\omega_\infty=\Omega
\]

이다. 나중에 구면의 두 chart에서도 정확히 같은 일이 생긴다.

## 1.3 이 primitive만으로 Gaussian 적분이 끝난다

반지름 \(R\)인 disk를 \(D_R\)라 하자.

\[
\int_{D_R}\Omega
=
\int_{\partial D_R}\omega_0.
\]

경계에서는 \(r=R\)이므로

\[
\omega_0
=
\frac{1-e^{-R^2}}2d\theta.
\]

따라서

\[
\begin{aligned}
\int_{D_R}e^{-x^2-y^2}\,dx\,dy
&=
\frac{1-e^{-R^2}}2
\int_0^{2\pi}d\theta\\
&=
\pi(1-e^{-R^2}).
\end{aligned}
\]

\(R\to\infty\)로 보내면

\[
\boxed{
\iint_{\mathbf R^2}e^{-x^2-y^2}\,dx\,dy=\pi.
}
\]

아직 Hodge star도, Laplacian도 쓰지 않았다.

---

# 2. 그런데 나는 라플라시안으로 바꾸고 싶다

지금 얻은 것은

\[
\Omega=d\omega_0
\]

이다. 하지만 원래 바라던 것은

\[
\Omega=-\Delta\phi\,dx\wedge dy
\]

였다.

그러면 \(\omega_0\)에서 gradient \(\nabla\phi\)를 찾아야 한다.

## 2.1 \(\omega_0\)의 coefficient는 원주방향이다

다시

\[
\omega_0
=
\frac{1-e^{-r^2}}{2r^2}
(-y\,dx+x\,dy)
\]

라고 쓴다.

1-form의 coefficient pair만 뽑으면

\[
F
=
\frac{1-e^{-r^2}}{2r^2}(-y,x).
\]

벡터 \((-y,x)\)는 원 \(r=\text{constant}\)에 접한다. 즉 \(F\)는 **원주방향**이다.

반면 회전대칭인 함수 \(\phi(r)\)의 gradient는

\[
\nabla\phi
=
\phi'(r)\left(\frac xr,\frac yr\right)
\]

처럼 **방사방향**이다.

그래서 바로 gradient를 찾을 수 없다.

## 2.2 원주방향을 90도 돌려 방사방향으로 만든다

다음 회전행렬을 적용한다.

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

\[
J(-y,x)=(-x,-y).
\]

따라서

\[
JF
=
-\frac{1-e^{-r^2}}{2r^2}(x,y).
\]

이제 정확히 방사방향이다.

그러면 \(JF=\nabla\phi\)라고 놓아 볼 수 있다.

\[
\phi'(r)\left(\frac xr,\frac yr\right)
=
-\frac{1-e^{-r^2}}{2r^2}(x,y).
\]

따라서

\[
\boxed{
\phi'(r)
=-\frac{1-e^{-r^2}}{2r}.
}
\]

\(\phi\)의 닫힌꼴을 구할 필요는 없다. 이 미분식만으로 라플라시안을 계산할 수 있다.

## 2.3 방사형 라플라시안을 계산한다

2차원에서 radial function의 라플라시안은

\[
\Delta\phi
=
\phi''(r)+\frac1r\phi'(r)
=
\frac1r\frac{d}{dr}\bigl(r\phi'(r)\bigr).
\]

그런데

\[
r\phi'(r)
=-\frac{1-e^{-r^2}}2.
\]

따라서

\[
\begin{aligned}
\Delta\phi
&=
\frac1r\frac{d}{dr}
\left(-\frac{1-e^{-r^2}}2\right)\\
&=
\frac1r(-re^{-r^2})\\
&=-e^{-r^2}.
\end{aligned}
\]

즉

\[
\boxed{
\Omega
=e^{-r^2}dx\wedge dy
=-\Delta\phi\,dx\wedge dy.
}
\]

원주방향 1-form을 방사방향으로 돌렸더니, 원하던 라플라시안 potential이 나왔다.

> **이 계산의 원천적인 순서**
>
> \[
> \boxed{
> \text{2-form}
> \to
> \text{원주방향 primitive}
> \to
> 90^\circ\text{ 회전}
> \to
> \text{방사방향 gradient}
> \to
> \text{Laplacian}.
> }
> \]

---

# 3. 방금 한 90도 회전에 Hodge star라는 이름을 붙인다

이제서야 이름을 붙인다.

1-form

\[
\alpha=P\,dx+Q\,dy
\]

의 coefficient pair \((P,Q)\)에 \(J\)를 적용하면

\[
(-Q,P)
\]

가 된다.

이를 1-form으로 다시 쓰는 연산을 \(*\)라고 부르자.

\[
\boxed{
*(P\,dx+Q\,dy)
=-Q\,dx+P\,dy.
}
\]

즉

\[
*dx=dy,
\qquad
*dy=-dx.
\]

Hodge star는 이 계산에서는 **원주방향과 방사방향을 서로 바꾸는 90도 회전의 이름**일 뿐이다.

## 3.1 Gaussian 계산을 한 줄로 다시 쓴다

우리가 만든 \(\phi\)는

\[
*d\phi=\omega_0
\]

가 아니라 부호를 확인하면

\[
\boxed{
*d\phi=\omega_0,
\qquad
\omega_0=-*d\phi
}
\]

중 어느 쪽인가?

직접 확인하자.

\[
d\phi
=
\phi'(r)dr
=
-\frac{1-e^{-r^2}}{2r}dr.
\]

또

\[
*dr=r\,d\theta.
\]

따라서

\[
*d\phi
=
-\frac{1-e^{-r^2}}2d\theta
=-\omega_0.
\]

그러므로 정확한 식은

\[
\boxed{
\omega_0=-*d\phi.
}
\]

이제 \(d\)를 취한다.

\[
\Omega=d\omega_0=-d(*d\phi).
\]

한편

\[
d\phi=\phi_xdx+\phi_ydy
\]

이므로

\[
*d\phi=-\phi_y dx+\phi_xdy.
\]

따라서

\[
\begin{aligned}
d(*d\phi)
&=
(\phi_{xx}+\phi_{yy})dx\wedge dy\\
&=
\Delta\phi\,dx\wedge dy.
\end{aligned}
\]

결국

\[
\boxed{
\Omega
=-d(*d\phi)
=-\Delta\phi\,dx\wedge dy.
}
\]

이 식은 새로운 원리가 아니다. 앞에서 원주방향을 방사방향으로 돌린 계산을 압축한 표기다.

## 3.2 Stokes가 발산정리로 바뀐다

\[
\omega_0=-*d\phi
\]

이므로

\[
\int_D\Omega
=
\int_{\partial D}\omega_0
=
-\int_{\partial D}*d\phi.
\]

경계를 반시계방향으로 돌 때, \(-*d\phi\)의 접선방향 성분은 \(-\nabla\phi\)의 바깥 법선방향 성분과 같다. 따라서

\[
\boxed{
\int_D-\Delta\phi\,dx\,dy
=
-\int_{\partial D}\frac{\partial\phi}{\partial n}\,ds.
}
\]

즉 처음 하고 싶었던 “라플라시안으로 바꾸어 발산정리를 쓴다”가 실제로 복원되었다.

---

# 4. 가장 단순한 방사형 potential은 \(\log r\)다

Gaussian에서는 \(\phi'(r)\)가 조금 복잡했다. 이제 가장 단순한 radial function을 본다.

\[
\phi(r)=\log r.
\]

\[
d\log r=\frac{dr}{r}.
\]

앞에서 \(*dr=r\,d\theta\)였으므로

\[
\boxed{
*d\log r=d\theta.
}
\]

이 식은 지금까지의 계산을 가장 작게 압축한다.

- \(d\log r\): 원점에서 바깥쪽으로 얼마나 빠르게 변하는가.
- \(d\theta\): 원점을 한 바퀴 돌 때 얼마나 회전하는가.
- Hodge star: 방사방향을 원주방향으로 90도 돌린다.

## 4.1 punctured plane에서는 라플라시안이 0이다

\[
\Delta\log r
=
\frac1r\frac{d}{dr}
\left(r\frac1r\right)
=0
\qquad(r>0).
\]

그런데 원을 한 바퀴 돌면

\[
\int_{|z|=\varepsilon}d\theta=2\pi.
\]

따라서

\[
\boxed{
\frac1{2\pi}
\int_{|z|=\varepsilon}
*d\log|z|
=1.
}
\]

원점을 뺀 곳에서는 라플라시안이 0인데, 원점을 둘러싼 경계적분은 \(1\)을 기억한다.

이 정수가 함수 \(z\)의 zero order다.

---

# 5. \(\mathbf P^1\)의 두 chart에서 \(z\)의 zero와 pole을 본다

동차좌표를 \([Z_0:Z_1]\)라 하고

\[
U_z=\{Z_0\neq0\},
\qquad
z=\frac{Z_1}{Z_0},
\]

\[
U_w=\{Z_1\neq0\},
\qquad
w=\frac{Z_0}{Z_1}
\]

로 둔다.

overlap에서는

\[
\boxed{w=z^{-1}.}
\]

## 5.1 세 ring

\[
\boxed{
\mathbf C[z],
\qquad
\mathbf C[w]=\mathbf C[z^{-1}],
\qquad
\mathbf C[z,z^{-1}].
}
\]

함수 \(z\)는 \(U_z\)에서는 regular하다. 무한대 chart에서는

\[
z=w^{-1}
\]

이므로 pole을 가진다.

## 5.2 zero와 pole의 차수

원점에서는

\[
z=z^1\cdot1
\]

이므로

\[
\operatorname{ord}_0(z)=1.
\]

무한대에서는

\[
z=w^{-1}
\]

이므로

\[
\operatorname{ord}_\infty(z)=-1.
\]

따라서

\[
\boxed{
\operatorname{div}(z)=[0]-[\infty].
}
\]

이것은 앞의 경계적분과 같은 숫자다.

- \(z=0\) 근방: \((2\pi)^{-1}\int d\theta=+1\).
- \(w=0\) 근방: \(\log|z|=-\log|w|\)이므로 \(-1\).

나중에 current의 언어를 배우면 이 계산을

\[
\frac1{2\pi}d(*d\log|z|)
=
\delta_0-\delta_\infty
\]

라고 압축한다. 지금 필요한 것은 작은 원의 적분뿐이다.

---

# 6. \(dz=-w^{-2}dw\): winding이 두 배가 된다

이제 함수 \(z\)가 아니라 좌표 frame의 변화를 본다.

\[
z=\frac1w
\]

를 미분하면

\[
\boxed{dz=-w^{-2}dw.}
\]

이는 cotangent frame의 변화다.

반대로 tangent frame

\[
e_z=\frac{\partial}{\partial z},
\qquad
e_w=\frac{\partial}{\partial w}
\]

은

\[
\begin{aligned}
e_w
&=\frac{dz}{dw}e_z\\
&=-w^{-2}e_z\\
&=-z^2e_z.
\end{aligned}
\]

따라서 tangent bundle의 transition function은

\[
\boxed{g(z)=-z^2.}
\]

적도 \(|z|=1\)에서 \(z=e^{i\theta}\)이면

\[
g(z)=-e^{2i\theta}.
\]

\(z\)가 한 바퀴 도는 동안 \(g\)는 두 바퀴 돈다.

\[
\boxed{
\frac1{2\pi i}
\oint g^{-1}dg=2.
}
\]

또

\[
g^{-1}dg=2\frac{dz}{z}.
\]

\[
\frac{dz}{z}=d\log r+i\,d\theta
\]

이므로

\[
\boxed{
g^{-1}dg
=2d\log|z|+2i\,d\theta.}
\]

함수 \(z\)에서 보았던 radial growth와 angular winding이 transition \(-z^2\)에서는 정확히 두 배가 된다.

---

# 7. 실제 목표: round sphere의 곡률을 같은 방식으로 계산한다

구면의 round metric을 \(z\)-chart에서

\[
\boxed{
ds^2
=
\frac{4|dz|^2}{(1+|z|^2)^2}
}
\]

로 쓴다.

\[
ds^2=e^{2\phi_z}|dz|^2
\]

이므로

\[
\boxed{
\phi_z
=\log2-\log(1+|z|^2).
}
\]

## 7.1 \(w\)-chart와 비교한다

\[
dz=-w^{-2}dw
\]

이므로

\[
|dz|^2=|w|^{-4}|dw|^2.
\]

계량을 다시 쓰면

\[
\phi_w(w)
=
\log2-\log(1+|w|^2).
\]

같은 overlap에서 비교하면

\[
\begin{aligned}
\phi_w(1/z)-\phi_z(z)
&=2\log|z|.
\end{aligned}
\]

즉

\[
\boxed{
\phi_w-\phi_z=2\log|z|.
}
\]

좌표변환의 modulus가 conformal potential에 \(2\log|z|\)를 보탠다.

## 7.2 곡률을 라플라시안으로 바꾸고 싶다

Gaussian에서 이미 다음 계산을 얻었다.

\[
-d(*d\phi)
=-\Delta\phi\,dx\wedge dy.
\]

따라서 구면의 local curvature 2-form을

\[
\boxed{
\Omega=-d(*d\phi)
}
\]

로 계산해 보자.

local primitive를

\[
\boxed{
\omega=-*d\phi
}
\]

라고 둔다. 이 \(\omega\)를 나중에 **connection 1-form**이라고 부른다.

즉 connection은 여기서 갑자기 정의된 개념이 아니다.

> 곡률을 라플라시안으로 쓰고 싶어서 \(-\Delta\phi\)를 만들었고,  
> 그 전에 한 번 적분한 local primitive가 \(\omega=-*d\phi\)다.

## 7.3 \(z\)-chart에서 계산한다

\[
\phi_z(r)=\log2-\log(1+r^2).
\]

\[
(\phi_z)_r=-\frac{2r}{1+r^2}.
\]

따라서

\[
\begin{aligned}
\omega_z
&=-*d\phi_z\\
&=-*(\phi_z)_rdr\\
&=\frac{2r}{1+r^2}*dr\\
&=\frac{2r^2}{1+r^2}d\theta.
\end{aligned}
\]

즉

\[
\boxed{
\omega_z
=
\frac{2r^2}{1+r^2}d\theta.
}
\]

한 번 더 \(d\)를 취하면

\[
\begin{aligned}
d\omega_z
&=
d\left(\frac{2r^2}{1+r^2}\right)\wedge d\theta\\
&=
\frac{4r}{(1+r^2)^2}dr\wedge d\theta\\
&=
\frac4{(1+r^2)^2}dx\wedge dy.
\end{aligned}
\]

한편 metric의 area form은

\[
\boxed{
dA
=
\frac4{(1+r^2)^2}dx\wedge dy.}
\]

따라서

\[
\boxed{d\omega_z=dA.}
\]

2차원에서는 curvature 2-form을 \(K\,dA\)라고 쓰므로

\[
K\,dA=dA
\]

이고

\[
\boxed{K=1.}
\]

## 7.4 두 connection의 차이

\(w=se^{i\varphi}\)에서 같은 계산을 하면

\[
\omega_w
=
\frac{2s^2}{1+s^2}d\varphi.
\]

overlap에서

\[
s=r^{-1},
\qquad
\varphi=-\theta.
\]

따라서

\[
\omega_w
=-\frac{2}{1+r^2}d\theta.
\]

그러므로

\[
\boxed{
\omega_w-\omega_z=-2d\theta.
}
\]

이 식은 앞의 potential 차이에서 바로 나온다.

\[
\begin{aligned}
\omega_w-\omega_z
&=-*d(\phi_w-\phi_z)\\
&=-2*d\log|z|\\
&=-2d\theta.
\end{aligned}
\]

\(d\theta\)는 overlap에서 closed이므로

\[
d\omega_w=d\omega_z.
\]

local primitive는 다르지만 curvature는 global하게 붙는다.

---

# 8. 함수의 zero·pole과 tangent bundle의 zero를 한 점에서 비교한다

함수 \(z\)는

\[
\operatorname{div}(z)=[0]-[\infty]
\]

였다. total degree는 \(0\)이다.

이제 tangent vector field

\[
\boxed{
s=z\frac{\partial}{\partial z}}
\]

를 본다.

\(z\)-chart에서는 coefficient가 \(z\)이므로 \(z=0\)에서 한 번 사라진다.

\(w\)-chart에서는

\[
\frac{\partial}{\partial z}
=-w^2\frac{\partial}{\partial w}
\]

이므로

\[
\begin{aligned}
s
&=z\frac{\partial}{\partial z}\\
&=\frac1w
\left(-w^2\frac{\partial}{\partial w}\right)\\
&=-w\frac{\partial}{\partial w}.
\end{aligned}
\]

따라서 무한대 \(w=0\)에서도 한 번 사라진다.

\[
\boxed{
\text{zeros of }s=[0]+[\infty].
}
\]

zero 총수는 \(2\)다.

이제 같은 정수 \(2\)가 세 군데서 나온다.

\[
\boxed{
\begin{aligned}
&z\partial_z\text{의 zero 총수}=2,\\
&-z^2\text{의 winding}=2,\\
&\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2.
\end{aligned}}
\]

---

# 9. 적도의 winding form을 구면 전체로 올린다

Gaussian 계산에서 두 primitive

\[
\omega_0,
\qquad
\omega_\infty
\]

가 같은 \(d\omega=\Omega\)를 만들면서

\[
\omega_0-\omega_\infty=\frac12d\theta
\]

만큼 달랐다.

구면에서도 같은 현상이 생긴다.

\[
\omega_w-\omega_z=-2d\theta.
\]

한 chart에서 smooth한 primitive를 고르면 다른 pole에서 문제가 생긴다. 그래서 두 chart에 각각 하나씩 두고 overlap의 차이를 기록한다.

## 9.1 normalized overlap form

\[
\boxed{
\alpha=\frac1\pi d\theta.
}
\]

그러면

\[
\int_{S^1}\alpha=2.
\]

## 9.2 두 weight로 나누어 놓는다

smooth functions \(\chi_z,\chi_w\)를

\[
\chi_z+\chi_w=1
\]

이 되게 잡는다.

- \(\chi_w=0\) near \(z=0\).
- \(\chi_z=0\) near \(w=0\).

이제

\[
A_z=\chi_w\alpha,
\qquad
A_w=-\chi_z\alpha
\]

로 둔다.

overlap에서

\[
A_w-A_z=-\alpha.
\]

또 \(d\alpha=0\)이므로

\[
\begin{aligned}
dA_z
&=d\chi_w\wedge\alpha,\\
dA_w
&=-d\chi_z\wedge\alpha
=d\chi_w\wedge\alpha.
\end{aligned}
\]

따라서

\[
\boxed{dA_z=dA_w.}
\]

두 local 2-form이 하나의 global 2-form으로 붙는다.

이 계산에 붙는 이름이 **Mayer–Vietoris connecting calculation**이다.

## 9.3 적분하면 overlap의 winding이 그대로 나온다

annulus에서 \(\chi_w=\chi(r)\)라고 하고, 안쪽에서 \(0\), 바깥쪽에서 \(1\)이 되게 잡자.

\[
d\chi_w=\chi'(r)dr.
\]

따라서

\[
F_{\mathrm{MV}}
=
dA_z
=
\frac{\chi'(r)}\pi dr\wedge d\theta.
\]

적분하면

\[
\begin{aligned}
\int_{\mathbf P^1}F_{\mathrm{MV}}
&=
\frac1\pi
\int_0^{2\pi}d\theta
\int\chi'(r)dr\\
&=
2.
\end{aligned}
\]

즉

\[
\boxed{
\int_{\mathbf P^1}F_{\mathrm{MV}}=2.
}
\]

round metric의 normalized curvature도

\[
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2
\]

이므로 같은 winding을 본다.

---

# 10. 이 계산에서 이름들이 실제로 가리킨 것

계산을 끝낸 뒤에만 이름을 정리한다.

- **Hodge star**  
  원주방향과 방사방향을 바꾸는 90도 회전.

- **connection 1-form**  
  곡률을 \(d\omega\)로 만들기 위해 chart마다 잡은 local primitive
  \[
  \omega=-*d\phi.
  \]

- **curvature 2-form**  
  connection을 한 번 더 미분한 것
  \[
  d\omega=K\,dA.
  \]

- **winding**  
  overlap transition의 phase가 원을 몇 번 도는지 세는 정수.

- **Mayer–Vietoris 계산**  
  overlap의 closed 1-form을 두 chart에 나누어 놓고 \(d\)를 취해 global 2-form을 만드는 계산.

하지만 실제 순서는 이름의 순서가 아니다.

\[
\boxed{
\begin{aligned}
\text{적분을 라플라시안으로 바꾸고 싶다}
&\longrightarrow
\text{원주방향 primitive를 찾는다}\\
&\longrightarrow
\text{방사방향으로 90도 돌린다}\\
&\longrightarrow
\text{gradient와 Laplacian이 나온다}\\
&\longrightarrow
\text{그 회전에 Hodge star라고 이름 붙인다}\\
&\longrightarrow
\text{구면의 두 chart에서 같은 계산을 반복한다}.
\end{aligned}}
\]

---

# 11. 직접 다시 할 계산

1. \(dx\wedge dy=r\,dr\wedge d\theta\)를 계산한다.
2. \(d(A(r)d\theta)=e^{-r^2}r\,dr\wedge d\theta\)에서 \(A(r)\)를 구한다.
3. \(C=0\)과 \(C=1/2\)가 각각 어디에서 smooth한지 확인한다.
4. \(\omega_0\)의 coefficient pair가 \((-y,x)\) 방향인지 확인한다.
5. 이를 90도 돌려 \((x,y)\) 방향으로 만든다.
6. \(\phi'(r)=-(1-e^{-r^2})/(2r)\)에서 \(\Delta\phi=-e^{-r^2}\)를 계산한다.
7. 그 회전을 \(*\)로 쓰면 \(\omega_0=-*d\phi\)인지 부호까지 확인한다.
8. \(*d\log r=d\theta\)를 \(x,y\) 성분으로 계산한다.
9. \(\operatorname{div}(z)=[0]-[\infty]\)를 두 chart에서 확인한다.
10. \(dz=-w^{-2}dw\)에서 tangent transition \(-z^2\)를 구한다.
11. \(\phi_w-\phi_z=2\log|z|\)에서 \(\omega_w-\omega_z=-2d\theta\)를 얻는다.
12. \(d\omega_z=K\,dA\)와 \(K=1\)을 계산한다.
13. \(z\partial_z=-w\partial_w\)의 zero가 두 개인지 확인한다.
14. partition of unity로 만든 global 2-form의 적분이 \(2\)인지 계산한다.
