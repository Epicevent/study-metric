# 함수 \(z\) 하나에서 구면의 곡률까지

## 미적분과 선형대수만으로 보는 zero·pole, winding, Hodge star, connection, Mayer–Vietoris

이 노트는 다음 한 함수만 끝까지 본다.

\[
f(z)=z.
\]

목표는 서로 낯설어 보이는 다섯 계산이 실제로 같은 정수를 보고 있다는 것을 확인하는 것이다.

\[
\boxed{
\text{zero·pole의 차수}
\longleftrightarrow
\text{원주 적분}
\longleftrightarrow
\text{좌표변환의 winding}
\longleftrightarrow
\text{connection의 차이}
\longleftrightarrow
\text{곡률의 적분}
}
\]

가정하는 것은 다음뿐이다.

- 한 변수와 여러 변수 미적분
- 복소수 \(z=x+iy\)
- \(2\times2\) 행렬과 선형변환
- Green–Stokes 공식
- 편미분과 라플라시안

`1-form`, `wedge`, `Hodge star`, `connection`이라는 말은 계산 전에 먼저 정의한다.

---

# 0. 계산에 필요한 최소 언어

## 0.1 벡터와 1-form

평면의 한 점에서 접벡터를

\[
v=a\frac{\partial}{\partial x}
+b\frac{\partial}{\partial y}
\]

라고 쓰자.

\(dx,dy\)는 벡터의 \(x,y\) 성분을 읽는 선형함수다.

\[
dx(v)=a,
\qquad
dy(v)=b.
\]

따라서

\[
\alpha=P\,dx+Q\,dy
\]

는 벡터 \(v\)에 대해

\[
\alpha(v)=Pa+Qb
\]

를 주는 선형함수다. 이런 것을 **1-form**이라고 부른다.

함수 \(h(x,y)\)의 미분은

\[
dh=h_x\,dx+h_y\,dy.
\]

이것은 익숙한 gradient \((h_x,h_y)\)를 1-form으로 적은 것이다.

## 0.2 wedge product는 행렬식이다

두 1-form

\[
\alpha=P\,dx+Q\,dy,
\qquad
\beta=R\,dx+S\,dy
\]

의 wedge product를

\[
\boxed{
\alpha\wedge\beta
=(PS-QR)\,dx\wedge dy
}
\]

로 정의한다.

오른쪽의 \(PS-QR\)는 행렬식

\[
\det
\begin{pmatrix}
P&Q\\
R&S
\end{pmatrix}
\]

이다.

따라서

\[
dx\wedge dx=0,
\qquad
dy\wedge dy=0,
\qquad
dy\wedge dx=-dx\wedge dy.
\]

\(dx\wedge dy\)는 oriented area를 나타내는 기본 2-form이다.

## 0.3 1-form의 exterior derivative

\[
\alpha=P\,dx+Q\,dy
\]

에 대해

\[
\boxed{
d\alpha=(Q_x-P_y)\,dx\wedge dy
}
\]

로 정의한다.

이 식은 Green 정리의 integrand와 같다.

\[
\int_D d\alpha
=
\int_{\partial D}\alpha.
\]

또 함수 \(h\)에 대해

\[
d(dh)=0
\]

이다. 실제로

\[
d(h_xdx+h_ydy)
=(h_{yx}-h_{xy})dx\wedge dy=0.
\]

## 0.4 Hodge star는 90도 회전 행렬이다

이 노트에서 Hodge star는 1-form의 coefficient vector를 90도 회전시키는 연산이다.

\[
\boxed{
*dx=dy,
\qquad
*dy=-dx.
}
\]

따라서

\[
\boxed{
*(P\,dx+Q\,dy)
=-Q\,dx+P\,dy.
}
\]

선형대수의 행렬로 쓰면

\[
\begin{pmatrix}
P\\Q
\end{pmatrix}
\longmapsto
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\begin{pmatrix}
P\\Q
\end{pmatrix}.
\]

왜 이 회전이 자연스러운지 확인하자.

\[
\begin{aligned}
\alpha\wedge *\alpha
&=(Pdx+Qdy)\wedge(-Qdx+Pdy)\\
&=(P^2+Q^2)\,dx\wedge dy.
\end{aligned}
\]

즉 \(*\alpha\)는 \(\alpha\)에 직교하고 길이는 같으며, \(\alpha\wedge*\alpha\)는 길이제곱 곱하기 면적형식이다.

> **핵심.** 이 노트에서 Hodge star는 새로운 마법이 아니다.  
> coefficient vector \((P,Q)\)를 \((-Q,P)\)로 돌리는 \(2\times2\) 행렬이다.

## 0.5 conformal metric에서도 1-form의 star는 같다

구면의 chart에서는 평면계량의 배수

\[
ds^2=e^{2\phi}(dx^2+dy^2)
\]

를 사용한다.

이 계량에서 길이 \(1\)인 coframe은

\[
\theta^1=e^\phi dx,
\qquad
\theta^2=e^\phi dy
\]

이다.

직교정규 coframe을 90도 회전시키면

\[
*\theta^1=\theta^2,
\qquad
*\theta^2=-\theta^1.
\]

양변에서 \(e^\phi\)가 소거되므로 여전히

\[
*dx=dy,
\qquad
*dy=-dx.
\]

2차원에서는 conformal factor가 1-form의 Hodge star에서 사라진다.

---

# 1. \(d\log r\)를 90도 돌리면 \(d\theta\)가 된다

이 계산이 zero·pole과 winding을 잇는 핵심이다.

\[
z=x+iy=re^{i\theta},
\qquad
r=\sqrt{x^2+y^2}.
\]

## 1.1 \(dr\)와 \(d\theta\)

\[
r^2=x^2+y^2
\]

를 미분하면

\[
2r\,dr=2x\,dx+2y\,dy.
\]

따라서

\[
\boxed{
dr=\frac{x\,dx+y\,dy}{r}.
}
\]

한편 \(\theta\)의 미분은

\[
\boxed{
d\theta=\frac{-y\,dx+x\,dy}{r^2}.
}
\]

이 식은 직접 확인할 수 있다. 원 \(x=r\cos\theta,\ y=r\sin\theta\) 위에서는

\[
dx=-r\sin\theta\,d\theta,
\qquad
dy=r\cos\theta\,d\theta
\]

이므로

\[
\frac{-y\,dx+x\,dy}{r^2}=d\theta.
\]

## 1.2 \(d\log r\)

\[
d\log r=\frac{dr}{r}
=\frac{x\,dx+y\,dy}{r^2}.
\]

Hodge star를 적용하면

\[
\begin{aligned}
*d\log r
&=
*\left(
\frac{x}{r^2}dx+\frac{y}{r^2}dy
\right)\\
&=
-\frac{y}{r^2}dx+\frac{x}{r^2}dy\\
&=d\theta.
\end{aligned}
\]

따라서

\[
\boxed{
*d\log|z|=d\theta.
}
\]

이 식의 뜻은 간단하다.

- \(d\log|z|\)는 원점에서 바깥쪽으로 향하는 **방사방향 변화**다.
- Hodge star는 그 방향을 90도 돌린다.
- 그 결과가 원점을 도는 **각방향 변화** \(d\theta\)다.

이것이 “Hodge star로 zero·pole과 winding을 연결한다”의 전부다.

## 1.3 원을 한 바퀴 적분한다

반지름 \(\varepsilon\)인 원에서 \(\theta\)는 \(0\)부터 \(2\pi\)까지 증가한다.

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

오른쪽의 정수 \(1\)은 \(z\)가 원점에서 한 번 사라진다는 정수와 같다.

---

# 2. \(\mathbf P^1\)의 두 chart와 세 ring

동차좌표를 \([Z_0:Z_1]\)라 하자.

\[
U_z=\{Z_0\neq0\},
\qquad
z=\frac{Z_1}{Z_0},
\]

\[
U_w=\{Z_1\neq0\},
\qquad
w=\frac{Z_0}{Z_1}.
\]

overlap에서는

\[
\boxed{
w=\frac1z.
}
\]

## 2.1 각 chart의 regular-function ring

\[
\mathcal O_{\mathrm{alg}}(U_z)=\mathbf C[z],
\]

\[
\mathcal O_{\mathrm{alg}}(U_w)=\mathbf C[w]
=\mathbf C[z^{-1}],
\]

\[
\boxed{
\mathcal O_{\mathrm{alg}}(U_z\cap U_w)
=\mathbf C[z,z^{-1}].
}
\]

따라서 질문에서 예상한

\[
\mathbf C[X],
\qquad
\mathbf C[1/X],
\qquad
\mathbf C[X,1/X]
\]

가 정확히 나온다.

- \(\mathbf C[z]\): \(z\)의 nonnegative powers.
- \(\mathbf C[z^{-1}]\): \(z^{-1}\)의 nonnegative powers.
- \(\mathbf C[z,z^{-1}]\): 양수와 음수 지수를 모두 허용.

## 2.2 overlap ring의 invertible elements

\[
\boxed{
\mathbf C[z,z^{-1}]^\times
=
\{cz^n:c\in\mathbf C^\times,\ n\in\mathbf Z\}.
}
\]

짧게 증명하자.

\[
f(z)=\sum_{j=m}^{M}a_jz^j,
\qquad
a_ma_M\neq0
\]

가 Laurent polynomial inverse를 가진다고 하자. \(fh=1\)에서 가장 낮은 지수와 가장 높은 지수가 모두 \(0\)이어야 한다. 그러려면 \(m=M\)이어야 하므로 \(f=cz^n\)이다.

이 지수 \(n\)은 원 위의 winding number다.

\[
\frac1{2\pi i}
\oint_{|z|=1}f^{-1}df=n.
\]

---

# 3. 대수적으로 \(z\)의 zero와 pole을 센다

## 3.1 zero와 pole의 차수 정의

점 \(P\) 근방의 local coordinate를 \(t\)라 하자.

함수 \(f\)가

\[
f=t^m u
\]

로 쓰이고 \(u(P)\neq0\)이면, \(u\)는 그 점에서 사라지지 않는 factor다.

정수 \(m\)을 \(f\)의 order라고 부른다.

\[
\operatorname{ord}_P(f)=m.
\]

- \(m>0\): \(m\)차 zero.
- \(m=0\): zero도 pole도 아님.
- \(m<0\): \(-m\)차 pole.

## 3.2 원점

원점의 local coordinate는 \(z\)다.

\[
z=z^1\cdot1.
\]

따라서

\[
\boxed{
\operatorname{ord}_0(z)=1.
}
\]

## 3.3 무한대

무한대의 local coordinate는

\[
w=\frac1z.
\]

따라서

\[
z=w^{-1}.
\]

그러므로

\[
\boxed{
\operatorname{ord}_\infty(z)=-1.
}
\]

## 3.4 divisor는 zero와 pole을 한 줄에 적은 기록이다

함수의 모든 zero와 pole을 multiplicity와 함께 적은 formal sum을 divisor라고 부른다.

\[
\boxed{
\operatorname{div}(z)=[0]-[\infty].
}
\]

총합은

\[
1+(-1)=0.
\]

함수 \(z\)의 zero와 pole은 서로 상쇄된다.

---

# 4. 같은 zero와 pole을 라플라시안과 원주 적분으로 본다

## 4.1 punctured plane에서는 \(\log r\)가 harmonic이다

평면 라플라시안은

\[
\Delta h=h_{xx}+h_{yy}.
\]

radial function \(h(r)\)에 대해서는

\[
\Delta h=h_{rr}+\frac1r h_r.
\]

\(h(r)=\log r\)이면

\[
h_r=\frac1r,
\qquad
h_{rr}=-\frac1{r^2}.
\]

따라서 \(r>0\)에서

\[
\boxed{
\Delta\log r=0.
}
\]

원점을 뺀 곳에서는 아무 일도 일어나지 않는다.

## 4.2 그런데 작은 원의 적분은 사라지지 않는다

앞에서

\[
*d\log r=d\theta
\]

를 계산했다.

따라서

\[
\int_{|z|=\varepsilon}*d\log r=2\pi.
\]

punctured disk

\[
A_{\varepsilon,R}
=
\{\varepsilon\le r\le R\}
\]

에서 Stokes를 쓰면

\[
0
=
\int_{A_{\varepsilon,R}}d*d\log r
=
\int_{r=R}d\theta
-
\int_{r=\varepsilon}d\theta.
\]

두 경계적분은 모두 \(2\pi\)다.

\(\varepsilon\to0\)으로 보내도 안쪽 경계적분은 사라지지 않는다. 원점에 남은 이 \(2\pi\)가 zero order \(1\)을 기록한다.

나중에 distribution 또는 current의 기호를 배우면 이 사실을

\[
d*d\log|z|
=
2\pi\delta_0
\]

라고 압축한다. 하지만 현재 필요한 계산은 경계적분

\[
\frac1{2\pi}\int d\theta=1
\]

뿐이다.

## 4.3 무한대에서는 부호가 반대다

\[
w=\frac1z
\]

이므로

\[
\log|z|=-\log|w|.
\]

따라서 무한대의 작은 \(w\)-원에서는

\[
\frac1{2\pi}
\int *d\log|z|
=
-1.
\]

즉

\[
\boxed{
\text{원점의 }+1
\quad\text{과}\quad
\text{무한대의 }-1
}
\]

이 바로

\[
\operatorname{div}(z)=[0]-[\infty]
\]

다.

> **현재까지의 결론**
>
> \[
> \boxed{
> \operatorname{ord}_P(f)
> =
> \frac1{2\pi}
> \int_{\partial D_P}d\arg f
> }
> \]
>
> 를 \(f=z\)에 대해 직접 계산했다.

---

# 5. \(dz=-w^{-2}dw\): 함수에서 tangent bundle로

## 5.1 cotangent frame

\[
z=\frac1w
\]

를 미분하면

\[
\boxed{
dz=-w^{-2}dw.
}
\]

반대로

\[
\boxed{
dw=-z^{-2}dz.
}
\]

\(dz,dw\)는 cotangent vector의 local bases다. exponent가 \(-2\)라는 사실이 보인다.

## 5.2 tangent frame

\[
e_z=\frac{\partial}{\partial z},
\qquad
e_w=\frac{\partial}{\partial w}
\]

라고 하자.

chain rule로

\[
\begin{aligned}
e_w
&=
\frac{dz}{dw}e_z\\
&=
-w^{-2}e_z\\
&=
-z^2e_z.
\end{aligned}
\]

따라서 tangent bundle의 transition function은

\[
\boxed{
g(z)=-z^2.
}
\]

이것은 overlap ring의 invertible element다.

\[
g\in\mathbf C[z,z^{-1}]^\times.
\]

## 5.3 winding이 왜 \(2\)인가

적도에서

\[
z=e^{i\theta}.
\]

그러면

\[
g(z)=-e^{2i\theta}.
\]

\(\theta\)가 \(0\)에서 \(2\pi\)까지 한 번 증가하는 동안 \(2\theta\)는 \(0\)에서 \(4\pi\)까지 증가한다. 따라서 \(g\)는 원점을 두 번 돈다.

미분으로 쓰면

\[
g^{-1}dg
=
2\frac{dz}{z}.
\]

적도에서는

\[
\frac{dz}{z}=i\,d\theta.
\]

따라서

\[
\boxed{
\frac1{2\pi i}
\oint_{|z|=1}g^{-1}dg
=
\frac1{2\pi}
\int_0^{2\pi}2\,d\theta
=2.
}
\]

## 5.4 modulus와 phase를 한 식에서 분리한다

\[
z=re^{i\theta}
\]

이면

\[
\frac{dz}{z}
=
d\log r+i\,d\theta.
\]

따라서

\[
\boxed{
g^{-1}dg
=
2d\log|z|+2i\,d\theta.
}
\]

- 실수부 \(2d\log|z|\): 크기 변화.
- 허수부 \(2d\theta\): 회전 변화.

Hodge star는 이 둘을

\[
*d\log|z|=d\theta
\]

로 연결한다.

---

# 6. round metric의 두 local potential

첨부 노트와 같은 round metric을 사용한다.

\[
\boxed{
ds^2
=
\frac{4|dz|^2}{(1+|z|^2)^2}.
}
\]

## 6.1 \(z\)-chart

\[
ds^2=e^{2\phi_z}|dz|^2
\]

로 쓰면

\[
\boxed{
\phi_z(z)
=
\log2-\log(1+|z|^2).
}
\]

## 6.2 \(w\)-chart

\[
z=\frac1w,
\qquad
dz=-w^{-2}dw.
\]

따라서

\[
|dz|^2=|w|^{-4}|dw|^2.
\]

또

\[
1+|z|^2
=
1+|w|^{-2}
=
\frac{1+|w|^2}{|w|^2}.
\]

그러므로

\[
\begin{aligned}
ds^2
&=
\frac{4|w|^{-4}|dw|^2}
{\left((1+|w|^2)/|w|^2\right)^2}\\
&=
\frac{4|dw|^2}{(1+|w|^2)^2}.
\end{aligned}
\]

즉

\[
\boxed{
\phi_w(w)
=
\log2-\log(1+|w|^2).
}
\]

## 6.3 같은 overlap에서 비교한다

\(w=1/z\)를 넣으면

\[
\begin{aligned}
\phi_w(1/z)
&=
\log2-\log(1+|z|^{-2})\\
&=
\log2-\log(1+|z|^2)+2\log|z|.
\end{aligned}
\]

따라서

\[
\boxed{
\phi_w(1/z)-\phi_z(z)
=
2\log|z|.
}
\]

이 \(2\log|z|\)는 정확히

\[
\log\left|\frac{dz}{dw}\right|
\]

에서 왔다.

overlap \(z\neq0\)에서는

\[
\Delta\log|z|=0.
\]

따라서 두 potential은 서로 달라도 같은 curvature를 만든다.

---

# 7. connection을 미적분로 직접 만든다

`connection`이라는 말을 먼저 쓰지 말고 계산부터 하자.

## 7.1 orthonormal coframe

conformal metric

\[
ds^2=e^{2\phi}(dx^2+dy^2)
\]

에서

\[
\theta^1=e^\phi dx,
\qquad
\theta^2=e^\phi dy
\]

는 길이 \(1\)인 두 직교 1-form이다.

점이 움직이면 이 orthonormal pair가 회전한다. 그 infinitesimal rotation을

\[
\omega=A\,dx+B\,dy
\]

라는 1-form으로 기록하려 한다.

2차원에서 회전만 있고 늘어남은 없다는 조건을 다음 두 식으로 적는다.

\[
d\theta^1=-\omega\wedge\theta^2,
\]

\[
d\theta^2=\omega\wedge\theta^1.
\]

이 노트에서는 이 두 식을 \(\omega\)의 정의로 사용한다.

## 7.2 \(\omega\)를 푼다

먼저

\[
\begin{aligned}
d\theta^1
&=
d(e^\phi dx)\\
&=
e^\phi d\phi\wedge dx\\
&=
-e^\phi\phi_y\,dx\wedge dy.
\end{aligned}
\]

또

\[
\begin{aligned}
d\theta^2
&=
d(e^\phi dy)\\
&=
e^\phi d\phi\wedge dy\\
&=
e^\phi\phi_x\,dx\wedge dy.
\end{aligned}
\]

\(\omega=A\,dx+B\,dy\)를 첫 식에 넣으면

\[
-\omega\wedge\theta^2
=
-e^\phi A\,dx\wedge dy.
\]

따라서

\[
A=\phi_y.
\]

둘째 식에 넣으면

\[
\omega\wedge\theta^1
=
-e^\phi B\,dx\wedge dy.
\]

따라서

\[
B=-\phi_x.
\]

결국

\[
\boxed{
\omega
=
\phi_y\,dx-\phi_x\,dy.
}
\]

Hodge star 표기로는

\[
*d\phi
=
\phi_xdy-\phi_ydx
\]

이므로

\[
\boxed{
\omega=-*d\phi.
}
\]

이제 “Hodge star가 connection과 연결된다”는 말이 구체적으로 보인다.

- \(d\phi\): conformal factor가 가장 빨리 변하는 방향.
- \(-*d\phi\): 그 방향을 90도 돌린 1-form.
- 이 1-form이 orthonormal frame의 회전을 측정한다.

## 7.3 curvature는 connection을 한 번 더 미분한 것

\[
\Omega=d\omega
\]

라고 두자.

\[
\begin{aligned}
d\omega
&=
d(\phi_y\,dx-\phi_x\,dy)\\
&=
-\phi_{yy}\,dx\wedge dy
-\phi_{xx}\,dx\wedge dy\\
&=
-(\phi_{xx}+\phi_{yy})dx\wedge dy.
\end{aligned}
\]

따라서

\[
\boxed{
\Omega
=
-\Delta\phi\,dx\wedge dy.
}
\]

2차원에서는 모든 2-form이 area form의 scalar multiple다.

\[
dA=e^{2\phi}dx\wedge dy.
\]

그 scalar를 Gaussian curvature \(K\)라고 부른다.

\[
\Omega=K\,dA.
\]

그러므로

\[
K e^{2\phi}
=
-\Delta\phi
\]

이고

\[
\boxed{
K=-e^{-2\phi}\Delta\phi.
}
\]

또

\[
\boxed{
K\,dA
=
-\Delta\phi\,dx\wedge dy.
}
\]

---

# 8. round sphere에서 곡률을 계산한다

\[
\phi_z(r)
=
\log2-\log(1+r^2).
\]

radial Laplacian을 사용한다.

\[
\Delta h=h_{rr}+\frac1r h_r.
\]

먼저

\[
(\phi_z)_r
=
-\frac{2r}{1+r^2}.
\]

다시 미분하면

\[
(\phi_z)_{rr}
=
-\frac{2(1-r^2)}{(1+r^2)^2}.
\]

따라서

\[
\begin{aligned}
\Delta\phi_z
&=
-\frac{2(1-r^2)}{(1+r^2)^2}
-\frac2{1+r^2}\\
&=
-\frac4{(1+r^2)^2}.
\end{aligned}
\]

그러므로

\[
\boxed{
K\,dA
=
\frac4{(1+r^2)^2}dx\wedge dy.
}
\]

그런데

\[
dA
=
e^{2\phi_z}dx\wedge dy
=
\frac4{(1+r^2)^2}dx\wedge dy.
\]

따라서

\[
\boxed{
K=1.
}
\]

이 normalization은 첨부 노트와 같다. 첨부 노트도 scalar \(K\)보다 \(K\,dA\)를 실제 적분 대상으로 강조한다.

---

# 9. 두 chart의 connection 차이가 \(-2d\theta\)다

## 9.1 \(z\)-chart

\[
(\phi_z)_x
=
-\frac{2x}{1+r^2},
\qquad
(\phi_z)_y
=
-\frac{2y}{1+r^2}.
\]

따라서

\[
\begin{aligned}
\omega_z
&=
(\phi_z)_y\,dx-(\phi_z)_x\,dy\\
&=
\frac{2(-y\,dx+x\,dy)}{1+r^2}.
\end{aligned}
\]

그런데

\[
-y\,dx+x\,dy=r^2d\theta.
\]

따라서

\[
\boxed{
\omega_z
=
\frac{2r^2}{1+r^2}d\theta.
}
\]

## 9.2 \(w\)-chart

\(w=se^{i\varphi}\)라 하면 같은 계산으로

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
\boxed{
\omega_w
=
-\frac{2}{1+r^2}d\theta.
}
\]

두 식을 빼면

\[
\boxed{
\omega_w-\omega_z
=
-2d\theta.
}
\]

이 식은 앞의 Hodge star 계산에서도 바로 나온다.

\[
\phi_w(1/z)-\phi_z(z)
=
2\log|z|.
\]

따라서

\[
\begin{aligned}
\omega_w-\omega_z
&=
-*d(\phi_w-\phi_z)\\
&=
-2*d\log|z|\\
&=
-2d\theta.
\end{aligned}
\]

즉 Hodge star의 역할은 정확히 하나다.

\[
\boxed{
\text{radial change }d\log|z|
\quad\stackrel{*}{\longmapsto}\quad
\text{angular change }d\theta.
}
\]

## 9.3 \(d\)를 취하면 차이가 사라진다

overlap에서

\[
d(d\theta)=0.
\]

따라서

\[
d\omega_w=d\omega_z.
\]

즉 local connection은 다르지만 curvature는 하나의 global 2-form으로 붙는다.

직접 계산하면

\[
\begin{aligned}
d\omega_z
&=
d\left(
\frac{2r^2}{1+r^2}
\right)\wedge d\theta\\
&=
\frac{4r}{(1+r^2)^2}dr\wedge d\theta\\
&=
\frac4{(1+r^2)^2}dx\wedge dy\\
&=
K\,dA.
\end{aligned}
\]

---

# 10. 함수 \(z\)와 tangent section \(z\partial_z\)는 다르다

이 구분이 zero·pole과 curvature를 잇는 마지막 다리다.

## 10.1 함수 \(z\)

\[
\operatorname{div}(z)
=
[0]-[\infty].
\]

zero 하나와 pole 하나가 상쇄되어 total degree는 \(0\)이다.

## 10.2 tangent vector field

각 점에 tangent vector를 하나씩 고른 것을 vector field 또는 tangent-bundle section이라고 부른다.

다음 vector field를 보자.

\[
s
=
z\frac{\partial}{\partial z}.
\]

\(z\)-chart에서는 coefficient가 \(z\)이므로 \(z=0\)에서 한 번 사라진다.

\(w\)-chart에서는

\[
\frac{\partial}{\partial z}
=
\frac{dw}{dz}
\frac{\partial}{\partial w}
=
-w^2\frac{\partial}{\partial w}.
\]

따라서

\[
\begin{aligned}
s
&=
z\frac{\partial}{\partial z}\\
&=
\frac1w
\left(
-w^2\frac{\partial}{\partial w}
\right)\\
&=
-w\frac{\partial}{\partial w}.
\end{aligned}
\]

즉 \(w=0\), 곧 무한대에서도 한 번 사라진다.

따라서

\[
\boxed{
\text{zero of }s
=
[0]+[\infty].
}
\]

zero 총수는

\[
1+1=2.
\]

함수 \(z\)에서는 무한대가 pole이었지만, tangent frame 자체가

\[
\frac{\partial}{\partial z}
=
-w^2\frac{\partial}{\partial w}
\]

로 변하면서 \(w^2\)가 pole을 상쇄하고 오히려 zero를 하나 더 만든다.

이제 같은 정수 \(2\)가 세 군데서 나온다.

\[
\boxed{
\begin{aligned}
&\text{tangent section의 zero 총수}=2,\\
&\text{transition }-z^2\text{의 winding}=2,\\
&\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2.
\end{aligned}
}
\]

---

# 11. Mayer–Vietoris를 partition of unity로 직접 계산한다

이름보다 계산이 먼저다.

## 11.1 적도 overlap의 closed 1-form

\[
U_z\cap U_w\simeq\mathbf C^\times
\]

는 원과 같은 핵심 모양을 갖는다.

transition \(g=-z^2\)의 phase는 적도에서 두 번 돈다. 그 winding을 기록하는 real 1-form을

\[
\boxed{
\alpha
=
\frac1\pi d\theta
}
\]

라고 두자.

\[
\int_{S^1}\alpha=2.
\]

또

\[
d\alpha=0
\]

이다.

## 11.2 partition of unity란 무엇인가

\(\chi_z,\chi_w\)를 다음 조건을 만족하는 smooth functions라고 하자.

\[
0\le\chi_z,\chi_w\le1,
\]

\[
\chi_z+\chi_w=1,
\]

- \(\chi_w=0\) near \(z=0\),
- \(\chi_z=0\) near \(w=0\).

즉 두 chart의 기여도를 부드럽게 나누는 weight들이다.

## 11.3 overlap form을 두 local forms로 나눈다

\[
A_z=\chi_w\alpha,
\qquad
A_w=-\chi_z\alpha
\]

로 둔다.

- \(A_z\)는 \(z=0\) 근방에서 \(\chi_w=0\)이므로 smooth하게 연장된다.
- \(A_w\)는 \(w=0\) 근방에서 \(\chi_z=0\)이므로 smooth하게 연장된다.

overlap에서

\[
\begin{aligned}
A_w-A_z
&=
-(\chi_z+\chi_w)\alpha\\
&=
-\alpha.
\end{aligned}
\]

이것은 round connection의 차이

\[
\frac{\omega_w}{2\pi}
-
\frac{\omega_z}{2\pi}
=
-\frac1\pi d\theta
=
-\alpha
\]

와 같은 gluing equation이다.

## 11.4 \(d\)를 취하면 global 2-form이 된다

\[
d\alpha=0
\]

이므로

\[
dA_z=d\chi_w\wedge\alpha,
\]

\[
dA_w=-d\chi_z\wedge\alpha.
\]

그런데

\[
d\chi_z+d\chi_w=0.
\]

따라서

\[
\boxed{
dA_z=dA_w.
}
\]

두 local 2-form이 하나의 global 2-form \(F_{\mathrm{MV}}\)로 붙는다.

\[
\boxed{
F_{\mathrm{MV}}
=
dA_z
=
dA_w.
}
\]

## 11.5 적분하면 winding \(2\)가 그대로 나온다

overlap annulus에서 \(\chi_w=\chi(r)\)라고 하자.

\[
\chi(r)=0
\]

near the inner boundary,

\[
\chi(r)=1
\]

near the outer boundary.

그러면

\[
d\chi_w=\chi'(r)\,dr.
\]

따라서

\[
F_{\mathrm{MV}}
=
\frac{\chi'(r)}{\pi}
dr\wedge d\theta.
\]

적분하면

\[
\begin{aligned}
\int_{\mathbf P^1}F_{\mathrm{MV}}
&=
\int_0^{2\pi}\int
\frac{\chi'(r)}{\pi}
dr\,d\theta\\
&=
\frac{2\pi}{\pi}
\left(
\chi(\text{outer})-\chi(\text{inner})
\right)\\
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

이것이 Mayer–Vietoris connecting calculation의 실물이다.

- overlap의 closed 1-form이 있고,
- partition of unity로 두 local 1-form을 만들고,
- \(d\)를 취해 global 2-form을 만든다.

## 11.6 round curvature와 왜 같은 class인가

round metric의 normalized local connections를

\[
\mathcal A_z=\frac{\omega_z}{2\pi},
\qquad
\mathcal A_w=\frac{\omega_w}{2\pi}
\]

라고 두자.

이들도

\[
\mathcal A_w-\mathcal A_z=-\alpha
\]

를 만족한다.

POU connection과 round connection의 차이를 각 chart에서 빼면 overlap에서 차이가 \(0\)이므로 하나의 global 1-form \(B\)로 붙는다.

따라서 두 curvature의 차이는

\[
\frac{K\,dA}{2\pi}
-
F_{\mathrm{MV}}
=
dB.
\]

구면에는 boundary가 없으므로 Stokes에 의해

\[
\int_{\mathbf P^1}dB=0.
\]

따라서 두 form의 적분은 같다.

\[
\boxed{
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}
=
\int_{\mathbf P^1}F_{\mathrm{MV}}
=
2.
}
\]

“같은 cohomology class”라는 말은 여기서는 단지 다음 뜻이다.

> 두 closed 2-form의 차이가 global 1-form의 \(d\)이고,  
> 따라서 닫힌 구면에서 모든 적분 결과가 같다.

---

# 12. 전체 계산을 한 표에 놓는다

| 대상 | local calculation | 정수 |
|---|---|---:|
| 함수 \(z\) at \(0\) | \(z=z^1\) | \(+1\) |
| 함수 \(z\) at \(\infty\) | \(z=w^{-1}\) | \(-1\) |
| divisor of \(z\) | \([0]-[\infty]\) | total \(0\) |
| radial change | \(d\log|z|\) |  |
| 90도 회전 | \(*d\log|z|=d\theta\) |  |
| 작은 원 적분 | \((2\pi)^{-1}\int d\theta\) | \(1\) |
| tangent transition | \(e_w=-z^2e_z\) | winding \(2\) |
| tangent section | \(z\partial_z=-w\partial_w\) | zeros \(1+1\) |
| connection difference | \(\omega_w-\omega_z=-2d\theta\) | period \(2\) |
| curvature | \(d\omega=K\,dA\) | \(\int KdA/(2\pi)=2\) |
| POU/MV | \(F_{\mathrm{MV}}=dA_z=dA_w\) | \(\int F_{\mathrm{MV}}=2\) |

---

# 13. 스터디에서 직접 할 최소 계산

## 계산 1

다음을 적는다.

\[
\mathbf C[z],
\qquad
\mathbf C[z^{-1}],
\qquad
\mathbf C[z,z^{-1}].
\]

## 계산 2

\[
\operatorname{ord}_0(z)=1,
\qquad
\operatorname{ord}_\infty(z)=-1
\]

을 확인한다.

## 계산 3

\[
d\log r=\frac{x\,dx+y\,dy}{r^2},
\]

\[
d\theta=\frac{-y\,dx+x\,dy}{r^2}
\]

를 계산한다.

## 계산 4

Hodge star 행렬

\[
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]

으로

\[
*d\log r=d\theta
\]

를 확인한다.

## 계산 5

\[
\frac1{2\pi}\int_{|z|=\varepsilon}d\theta=1
\]

을 계산한다.

## 계산 6

\[
dz=-w^{-2}dw,
\qquad
e_w=-z^2e_z
\]

를 계산한다.

## 계산 7

\[
g^{-1}dg
=
2d\log|z|+2i\,d\theta
\]

를 확인한다.

## 계산 8

\[
\phi_w(1/z)-\phi_z(z)
=
2\log|z|
\]

를 계산한다.

## 계산 9

구조방정식에서

\[
\omega=-*d\phi
\]

를 유도한다.

## 계산 10

\[
\omega_w-\omega_z=-2d\theta
\]

와

\[
d\omega=K\,dA
\]

를 확인한다.

## 계산 11

\[
z\partial_z=-w\partial_w
\]

가 \(0,\infty\)에서 각각 한 번 사라지는지 확인한다.

## 계산 12

POU로

\[
F_{\mathrm{MV}}=dA_z=dA_w
\]

를 만들고 적분이 \(2\)인지 계산한다.

---

# 14. 마지막 압축

Hodge star는 추상적인 연결 장치가 아니다.

\[
\boxed{
*
=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
}
\]

라는 90도 회전이다.

그래서

\[
\boxed{
d\log|z|
\stackrel{*}{\longmapsto}
d\theta.
}
\]

- \(d\log|z|\)는 zero와 pole 근방의 radial growth를 본다.
- \(d\theta\)는 그 점을 도는 winding을 본다.
- \(dz=-w^{-2}dw\)의 exponent \(2\)는 tangent frame이 두 번 도는 것을 뜻한다.
- connection은 conformal factor의 gradient를 90도 돌린
  \[
  \omega=-*d\phi
  \]
  이다.
- connection에 \(d\)를 한 번 더 취하면
  \[
  d\omega=K\,dA
  \]
  가 된다.
- partition of unity는 overlap의 \(d\theta\)를 두 chart에 나누어 놓고, \(d\)를 취해 global curvature form을 만든다.

따라서 함수 \(z\) 하나에서 실제로 보이는 계산선은

\[
\boxed{
\begin{aligned}
z=w^{-1}
&\longrightarrow
\operatorname{div}(z)=[0]-[\infty]\\
&\longrightarrow
*d\log|z|=d\theta\\
&\longrightarrow
e_w=-z^2e_z\\
&\longrightarrow
\omega_w-\omega_z=-2d\theta\\
&\longrightarrow
d\omega=K\,dA\\
&\longrightarrow
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}=2.
\end{aligned}
}
\]
