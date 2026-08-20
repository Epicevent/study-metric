# 함수 \(z\) 하나에서 구면의 곡률까지

## Gaussian 2-form에서 Hodge star를 복원하고 zero·pole, winding, connection, Mayer–Vietoris로 올라가기

이 노트는 Hodge star를 먼저 정의하고 사용하는 방식으로 시작하지 않는다.

먼저 아주 구체적인 미적분 문제를 푼다.

\[
\Omega=e^{-x^2-y^2}\,dx\wedge dy
\]

가 주어졌을 때

\[
d\omega=\Omega
\]

를 만족하는 1-form \(\omega\)를 직접 찾는다. 그 과정에서

1. 원주방향과 방사방향이 90도 회전으로 연결되고,
2. 그 회전을 1-form에 적용한 것이 Hodge star이며,
3. \(d(*d\psi)\)가 라플라시안을 만든다는 사실

을 계산으로 복원한다.

그다음 같은 장치를 함수

\[
f(z)=z
\]

에 적용하여

\[
\boxed{
\text{zero·pole의 차수}
\longleftrightarrow
\text{원주 적분과 winding}
\longleftrightarrow
\text{tangent transition }-z^2
\longleftrightarrow
\text{connection의 차이}
\longleftrightarrow
\text{곡률의 적분}
}
\]

을 한 계산선으로 연결한다.

가정하는 것은 다음뿐이다.

- 한 변수와 여러 변수 미적분
- 복소수 \(z=x+iy\)
- \(2\times2\) 행렬과 선형변환
- Green 정리와 Stokes 정리
- 편미분과 라플라시안

---

# I. Hodge star가 나오기 전의 최소 언어

# 1. 1-form은 벡터의 성분을 읽는 선형함수다

평면의 접벡터를

\[
v=a\frac{\partial}{\partial x}
+b\frac{\partial}{\partial y}
\]

라고 쓰자.

\(dx,dy\)는 벡터의 두 성분을 읽는다.

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

를 주는 선형함수다. 이런 것을 1-form이라고 부른다.

함수 \(h(x,y)\)의 미분은

\[
\boxed{
dh=h_x\,dx+h_y\,dy.
}
\]

Euclidean inner product를 쓰면 1-form \(Pdx+Qdy\)와 coefficient vector

\[
F_\alpha=(P,Q)
\]

를 서로 대응시킬 수 있다.

곡선 \(\gamma(t)=(x(t),y(t))\) 위에서

\[
\int_\gamma\alpha
=
\int
\left(
P\frac{dx}{dt}
+Q\frac{dy}{dt}
\right)dt.
\]

즉 1-form의 적분은 coefficient vector의 접선방향 성분을 더하는 선적분이다.

---

# 2. wedge product는 \(2\times2\) 행렬식이다

두 1-form을

\[
\alpha=P\,dx+Q\,dy,
\qquad
\beta=R\,dx+S\,dy
\]

라고 하자.

그 wedge product를

\[
\boxed{
\alpha\wedge\beta
=(PS-QR)\,dx\wedge dy
}
\]

로 정의한다.

오른쪽 coefficient는 행렬식

\[
\det
\begin{pmatrix}
P&Q\\
R&S
\end{pmatrix}
=PS-QR
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

---

# 3. exterior derivative는 Green 정리의 integrand다

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

Green 정리는 바로

\[
\boxed{
\int_Dd\alpha
=
\int_{\partial D}\alpha
}
\]

라고 쓸 수 있다.

함수 \(h\)에 대해

\[
d(dh)=0
\]

이다. 실제로

\[
\begin{aligned}
d(dh)
&=d(h_xdx+h_ydy)\\
&=(h_{yx}-h_{xy})dx\wedge dy\\
&=0.
\end{aligned}
\]

- \(d\alpha=0\)이면 \(\alpha\)를 closed라고 한다.
- \(\alpha=dh\)이면 \(\alpha\)를 exact라고 한다.

모든 exact 1-form은 closed다. 반대는 영역의 모양에 따라 실패할 수 있다. 뒤에서 \(d\theta\)가 그 예가 된다.

---

# 4. polar coordinate의 세 기본식

\[
x=r\cos\theta,
\qquad
y=r\sin\theta.
\]

미분하면

\[
dx=\cos\theta\,dr-r\sin\theta\,d\theta,
\]

\[
dy=\sin\theta\,dr+r\cos\theta\,d\theta.
\]

wedge를 취하면

\[
\boxed{
dx\wedge dy=r\,dr\wedge d\theta.
}
\]

또

\[
r^2=x^2+y^2
\]

를 미분하면

\[
\boxed{
dr=\frac{x\,dx+y\,dy}{r}.
}
\]

각도방향 1-form은

\[
\boxed{
d\theta
=
\frac{-y\,dx+x\,dy}{r^2}.
}
\]

\(\theta\) 자체는 원점을 한 바퀴 돌면 \(2\pi\)만큼 바뀌므로 전역적인 한 값 함수가 아니다. 그러나 위 식으로 적은 \(d\theta\)는 \(\mathbf R^2\setminus\{0\}\)에서 single-valued한 1-form이다.

---

# II. Gaussian 2-form으로 Hodge star를 발견한다

# 5. 문제: \(d\omega=e^{-r^2}dx\wedge dy\)를 풀어라

다음 2-form을 잡는다.

\[
\boxed{
\Omega=e^{-r^2}dx\wedge dy.
}
\]

polar coordinate에서는

\[
\Omega=e^{-r^2}r\,dr\wedge d\theta.
\]

원점에 대한 회전대칭이 있으므로 1-form도

\[
\omega=A(r)d\theta
\]

꼴로 찾아보는 것이 자연스럽다.

그러면

\[
d\omega=A'(r)dr\wedge d\theta.
\]

따라서 \(d\omega=\Omega\)가 되려면

\[
A'(r)=re^{-r^2}
\]

이어야 한다.

적분하면

\[
\boxed{
A(r)=C-\frac12e^{-r^2}.
}
\]

같은 2-form \(\Omega\)를 만드는 1-form이 상수 \(C\)만큼 여러 개 나온다.

---

# 6. 어느 primitive를 고를 것인가: 원점의 smoothness가 상수를 정한다

## 6.1 원점에서 smooth한 선택

\(d\theta\)는 원점에서 singular하므로 \(A(r)d\theta\)가 smooth하려면 \(A(r)\)가 최소한 \(r^2\)처럼 사라져야 한다.

\[
e^{-r^2}=1-r^2+O(r^4)
\]

이므로 \(C=1/2\)를 택하면

\[
A_0(r)=\frac{1-e^{-r^2}}2
=\frac{r^2}{2}+O(r^4).
\]

따라서

\[
\boxed{
\omega_0
=
\frac{1-e^{-r^2}}2d\theta
}
\]

는 원점까지 smooth하게 연장된다.

Cartesian coordinate로 쓰면

\[
\boxed{
\omega_0
=
\frac{1-e^{-r^2}}{2r^2}
(-y\,dx+x\,dy).
}
\]

\((1-e^{-r^2})/r^2\to1\)이므로 원점에서 singularity가 실제로 소거된다.

## 6.2 무한대에서 사라지는 선택

\(C=0\)을 택하면

\[
\omega_\infty
=-\frac12e^{-r^2}d\theta.
\]

이 form은 \(r\to\infty\)에서 사라지지만, 원점에서는 \(-\frac12d\theta\)처럼 singular하다.

두 primitive의 차이는

\[
\boxed{
\omega_0-\omega_\infty
=
\frac12d\theta.
}
\]

\(d\theta\)는 punctured plane에서 closed다.

\[
d(d\theta)=0
\qquad(r>0).
\]

그러나 원을 한 바퀴 돌면

\[
\int_{|z|=R}d\theta=2\pi
\]

이므로 전역 single-valued 함수의 미분일 수 없다.

이 계산이 뒤에서 사용할 winding form의 첫 출현이다.

---

# 7. Gaussian integral을 Stokes로 복원한다

반지름 \(R\)인 disk를 \(D_R\)라 하자.

\[
\int_{D_R}\Omega
=
\int_{\partial D_R}\omega_0.
\]

원 \(r=R\)에서

\[
\omega_0
=
\frac{1-e^{-R^2}}2d\theta.
\]

따라서

\[
\begin{aligned}
\int_{D_R}e^{-r^2}dxdy
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
\int_{\mathbf R^2}e^{-x^2-y^2}dxdy=\pi.
}
\]

이 계산에서 \(d\theta\)는 장식이 아니다. radial 2-form의 적분을 원주 적분으로 바꾸는 실제 계산도구다.

---

# 8. 원주방향 벡터를 90도 돌리면 방사방향 벡터가 된다

1-form

\[
\alpha=Pdx+Qdy
\]

의 coefficient vector를

\[
F=(P,Q)
\]

라고 하자.

다음 행렬을 잡는다.

\[
\boxed{
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
}
\]

\(J\)는 vector를 반시계방향으로 90도 회전시킨다.

\[
J(P,Q)=(-Q,P).
\]

Gaussian primitive \(\omega_0=A_0(r)d\theta\)의 coefficient vector는

\[
F_{\omega_0}
=
\frac{A_0(r)}{r^2}(-y,x).
\]

이것은 원에 접하는 방향이다.

\(-J\)로 한 번 돌리면

\[
-JF_{\omega_0}
=
\frac{A_0(r)}{r^2}(x,y),
\]

즉 바깥쪽 방사방향 vector가 된다.

원주방향과 방사방향의 관계가 여기서 실제로 나타났다.

---

# 9. 이 90도 회전을 1-form에 적용한 것이 Hodge star다

이제 Hodge star를 다음처럼 **발견된 회전의 이름**으로 정의한다.

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
*(Pdx+Qdy)
=-Qdx+Pdy.
}
\]

coefficient vector에 정확히 \(J\)를 적용한 것이다.

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

두 번 적용하면

\[
\boxed{**\alpha=-\alpha}
\]

이다. 90도 회전을 두 번 하면 180도 회전이 되는 것과 같다.

또

\[
\begin{aligned}
\alpha\wedge*\alpha
&=(Pdx+Qdy)\wedge(-Qdx+Pdy)\\
&=(P^2+Q^2)dx\wedge dy.
\end{aligned}
\]

즉

\[
\boxed{
\alpha\wedge*\alpha
=|\alpha|^2dx\wedge dy.
}
\]

Hodge star는 metric으로 길이를 재고 orientation으로 90도 방향을 선택하는 연산이다.

---

# 10. Hodge star는 circulation을 flux로 바꾼다

영역 \(D\)의 경계를 반시계방향으로 돈다고 하자.

단위접선 vector를

\[
T=(T_x,T_y)
\]

라고 하면 바깥쪽 단위법선은

\[
n=(T_y,-T_x).
\]

1-form \(\alpha=Pdx+Qdy\)의 선적분 integrand는

\[
F\cdot T
=PT_x+QT_y.
\]

한편 \(-*\alpha\)의 coefficient vector는

\[
(Q,-P).
\]

이를 \(G\)라 하면

\[
\begin{aligned}
G\cdot n
&=(Q,-P)\cdot(T_y,-T_x)\\
&=QT_y+PT_x\\
&=F\cdot T.
\end{aligned}
\]

따라서

\[
\boxed{
\text{\(\alpha\)의 circulation}
=
\text{\(-*\alpha\)에 대응하는 vector field의 outward flux}.
}
\]

또

\[
\operatorname{div}(Q,-P)=Q_x-P_y.
\]

따라서

\[
\boxed{
d\alpha
=
\operatorname{div}(-*\alpha)\,dx\wedge dy.
}
\]

Green의 circulation theorem과 divergence theorem이 Hodge star의 90도 회전으로 같은 정리가 된다.

---

# 11. 라플라시안은 \(d(*d\psi)\)에서 복원된다

함수 \(\psi\)에 대해

\[
d\psi=\psi_xdx+\psi_ydy.
\]

Hodge star를 적용하면

\[
*d\psi=-\psi_y dx+\psi_xdy.
\]

한 번 더 \(d\)를 취하면

\[
\begin{aligned}
d(*d\psi)
&=d(-\psi_y dx+\psi_xdy)\\
&=(\psi_{xx}+\psi_{yy})dx\wedge dy.
\end{aligned}
\]

따라서

\[
\boxed{
d(*d\psi)=\Delta\psi\,dx\wedge dy.}
\]

이 식은 Hodge star와 라플라시안의 연결을 완전히 기본계산으로 복원한다.

## 11.1 Gaussian 계산으로 다시 확인

앞에서

\[
\omega_0=A_0(r)d\theta,
\qquad
A_0(r)=\frac{1-e^{-r^2}}2
\]

를 얻었다.

polar coordinate에서

\[
*dr=r\,d\theta,
\qquad
*d\theta=-\frac{dr}{r}.
\]

따라서

\[
-*\omega_0
=
\frac{A_0(r)}rdr.
\]

다음 함수는 적분으로 정의할 수 있다.

\[
\psi(r)
=
\int_0^r\frac{A_0(s)}sds.
\]

그러면

\[
d\psi=\frac{A_0(r)}rdr=-*\omega_0.
\]

즉

\[
\omega_0=*d\psi.
\]

radial Laplacian을 계산하면

\[
\begin{aligned}
\Delta\psi
&=
\frac1r\frac{d}{dr}
\left(r\frac{d\psi}{dr}\right)\\
&=
\frac1rA_0'(r)\\
&=e^{-r^2}.
\end{aligned}
\]

따라서

\[
\boxed{
\omega_0=*d\psi,
\qquad
\Delta\psi=e^{-r^2},
\qquad
d\omega_0=e^{-r^2}dx\wedge dy.
}
\]

특수함수의 이름을 몰라도 된다. 미적분의 기본정리와 radial Laplacian만으로 충분하다.

---

# III. 함수 \(z\)의 zero·pole와 winding

# 12. \(\mathbf P^1\)의 두 chart와 세 ring

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
\boxed{w=z^{-1}.}
\]

각 chart의 algebraic regular-function ring은

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

즉

\[
\mathbf C[X],
\qquad
\mathbf C[1/X],
\qquad
\mathbf C[X,1/X]
\]

가 정확히 나온다.

---

# 13. overlap ring의 unit과 winding number

\[
\boxed{
\mathbf C[z,z^{-1}]^\times
=
\{cz^n:c\in\mathbf C^\times,\ n\in\mathbf Z\}.
}
\]

Laurent polynomial

\[
f(z)=\sum_{j=m}^{M}a_jz^j,
\qquad
a_ma_M\neq0
\]

가 Laurent polynomial inverse를 가진다고 하자. 곱 \(fh=1\)에서 가장 낮은 지수와 가장 높은 지수가 모두 \(0\)이어야 한다. 그러려면 \(m=M\)이어야 하므로 \(f=cz^n\)이다.

적도 \(|z|=1\)에서 \(z=e^{i\theta}\)라 하면

\[
cz^n=ce^{in\theta}
\]

이므로 원점을 \(n\)번 돈다.

\[
\boxed{
\frac1{2\pi i}
\oint_{|z|=1}f^{-1}df=n.
}
\]

Laurent exponent와 winding number가 같은 정수다.

---

# 14. 대수적으로 \(z\)의 zero와 pole을 센다

점 \(P\) 근방의 local coordinate를 \(t\)라 하자.

\[
f=t^m u,
\qquad
u(P)\neq0
\]

로 쓰이면 정수 \(m\)을 \(f\)의 order라고 한다.

- \(m>0\): \(m\)차 zero.
- \(m<0\): \(-m\)차 pole.

## 14.1 원점

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

## 14.2 무한대

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

## 14.3 divisor

\[
\boxed{
\operatorname{div}(z)=[0]-[\infty].
}
\]

함수 \(z\)의 zero와 pole은 total degree

\[
1+(-1)=0
\]

으로 상쇄된다.

---

# 15. 같은 정수를 \(d\log|z|\)와 \(d\theta\)로 읽는다

앞에서 이미

\[
\boxed{*d\log|z|=d\theta}
\]

를 성분계산으로 얻었다.

작은 원을 한 바퀴 돌면

\[
\boxed{
\frac1{2\pi}
\int_{|z|=\varepsilon}
*d\log|z|
=1.
}
\]

이는

\[
\operatorname{ord}_0(z)=1
\]

과 같은 정수다.

무한대에서는

\[
\log|z|=-\log|w|
\]

이므로 작은 \(w\)-원에서 같은 적분은 \(-1\)이 된다.

따라서

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

나중에 distribution 또는 current를 배우면 이 경계적분을

\[
\frac1{2\pi}d*d\log|z|
=
\delta_0-\delta_\infty
\]

라고 압축한다. 현재 필요한 실질은 작은 원의 경계적분뿐이다.

---

# IV. \(dz=-w^{-2}dw\)에서 tangent bundle의 winding \(2\)로

# 16. cotangent frame의 변화

\[
z=\frac1w
\]

를 미분하면

\[
\boxed{dz=-w^{-2}dw.}
\]

반대로

\[
\boxed{dw=-z^{-2}dz.}
\]

\(dz,dw\)는 cotangent space의 local bases다. exponent \(-2\)가 보인다.

---

# 17. tangent frame의 변화

\[
e_z=\frac{\partial}{\partial z},
\qquad
e_w=\frac{\partial}{\partial w}
\]

라고 하자.

chain rule에 의해

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

이는 overlap ring의 invertible element다.

\[
g\in\mathbf C[z,z^{-1}]^\times.
\]

적도에서

\[
z=e^{i\theta}
\]

이므로

\[
g(z)=-e^{2i\theta}.
\]

\(\theta\)가 한 바퀴 도는 동안 \(2\theta\)는 두 바퀴 돈다.

\[
\boxed{
\frac1{2\pi i}
\oint_{|z|=1}g^{-1}dg=2.
}
\]

---

# 18. 한 logarithmic derivative 안에 radial part와 angular part가 함께 있다

\[
g=-z^2
\]

이므로

\[
\boxed{g^{-1}dg=2\frac{dz}{z}.}
\]

또

\[
\frac{dz}{z}
=d\log r+i\,d\theta.
\]

따라서

\[
\boxed{
g^{-1}dg
=2d\log|z|+2i\,d\theta.}
\]

- 실수부 \(2d\log|z|\): transition의 크기 변화.
- 허수부 \(2d\theta\): transition의 회전 변화.

그리고 Hodge star가

\[
*d\log|z|=d\theta
\]

로 둘을 90도 회전 관계로 연결한다.

---

# V. conformal metric에서 connection과 curvature를 복원한다

# 19. 2차원 conformal metric

다음 계량을 생각한다.

\[
\boxed{
ds^2=e^{2\phi}(dx^2+dy^2).
}
\]

길이 \(1\)인 orthogonal coframe은

\[
\theta^1=e^\phi dx,
\qquad
\theta^2=e^\phi dy
\]

이다.

2차원 conformal metric에서도 1-form의 Hodge star는

\[
*dx=dy,
\qquad
*dy=-dx
\]

그대로다. 실제로

\[
*\theta^1=\theta^2
\]

에서 공통 factor \(e^\phi\)가 소거된다.

---

# 20. connection을 orthonormal frame의 회전량으로 정의한다

점이 움직이면 orthonormal pair \((\theta^1,\theta^2)\)도 회전한다. 그 infinitesimal rotation을 1-form

\[
\omega=A\,dx+B\,dy
\]

로 기록한다.

2차원에서 회전만 있고 길이변화가 없다는 조건을 다음 구조방정식으로 적는다.

\[
\boxed{
d\theta^1=-\omega\wedge\theta^2,}
\]

\[
\boxed{
d\theta^2=\omega\wedge\theta^1.}
\]

이 노트에서는 이 두 식을 connection 1-form의 정의로 사용한다.

먼저

\[
\begin{aligned}
d\theta^1
&=d(e^\phi dx)\\
&=e^\phi d\phi\wedge dx\\
&=-e^\phi\phi_y dx\wedge dy.
\end{aligned}
\]

또

\[
\begin{aligned}
d\theta^2
&=d(e^\phi dy)\\
&=e^\phi d\phi\wedge dy\\
&=e^\phi\phi_x dx\wedge dy.
\end{aligned}
\]

\(\omega=A dx+Bdy\)를 구조방정식에 넣으면

\[
A=\phi_y,
\qquad
B=-\phi_x.
\]

따라서

\[
\boxed{
\omega
=\phi_y dx-\phi_xdy.
}
\]

그런데

\[
*d\phi
=\phi_xdy-\phi_ydx
\]

이므로

\[
\boxed{
\omega=-*d\phi.
}
\]

이제 Hodge star가 connection에 등장하는 이유가 계산으로 보인다.

- \(d\phi\)는 conformal factor의 방사적 변화다.
- Hodge star가 이를 90도 돌린다.
- 그 결과 \(-*d\phi\)가 orthonormal frame의 회전량이 된다.

---

# 21. curvature는 connection을 한 번 더 미분한 것이다

\[
\Omega=d\omega
\]

라고 두자.

\[
\begin{aligned}
d\omega
&=d(\phi_y dx-\phi_xdy)\\
&=-(\phi_{xx}+\phi_{yy})dx\wedge dy.
\end{aligned}
\]

따라서

\[
\boxed{
\Omega=-\Delta\phi\,dx\wedge dy.
}
\]

2차원에서 면적형식은

\[
dA=e^{2\phi}dx\wedge dy.
\]

모든 2-form은 면적형식의 scalar multiple이므로

\[
\Omega=K\,dA
\]

라고 놓고 그 scalar \(K\)를 Gaussian curvature라고 부른다.

그러면

\[
K e^{2\phi}=-\Delta\phi
\]

이고

\[
\boxed{K=-e^{-2\phi}\Delta\phi,}
\]

\[
\boxed{K\,dA=-\Delta\phi\,dx\wedge dy.}
\]

앞의 기본항등식

\[
d(*d\psi)=\Delta\psi\,dx\wedge dy
\]

와 비교하면 curvature 공식은 단순히

\[
\omega=-*d\phi
\]

에 \(d\)를 취한 것이다.

---

# VI. round sphere의 두 chart 계산

# 22. round metric과 conformal factor

반지름 \(1\)인 round sphere의 stereographic metric은

\[
\boxed{
ds^2
=\frac{4|dz|^2}{(1+|z|^2)^2}.
}
\]

따라서

\[
\boxed{
\phi_z(z)
=\log2-\log(1+|z|^2).
}
\]

\(w=1/z\)와

\[
dz=-w^{-2}dw
\]

를 대입하면

\[
|dz|^2=|w|^{-4}|dw|^2
\]

이고

\[
1+|z|^2
=\frac{1+|w|^2}{|w|^2}.
\]

따라서

\[
ds^2
=
\frac{4|dw|^2}{(1+|w|^2)^2}
\]

이고

\[
\boxed{
\phi_w(w)
=\log2-\log(1+|w|^2).
}
\]

같은 overlap에서 비교하면

\[
\boxed{
\phi_w(1/z)-\phi_z(z)
=2\log|z|.
}
\]

이 항은 정확히

\[
\log\left|\frac{dz}{dw}\right|
\]

에서 왔다.

---

# 23. 라플라시안으로 곡률을 계산한다

\[
\phi_z(r)
=\log2-\log(1+r^2).
\]

radial Laplacian

\[
\Delta h=h_{rr}+\frac1r h_r
\]

을 사용한다.

\[
(\phi_z)_r=-\frac{2r}{1+r^2},
\]

\[
(\phi_z)_{rr}
=-\frac{2(1-r^2)}{(1+r^2)^2}.
\]

따라서

\[
\begin{aligned}
\Delta\phi_z
&=(\phi_z)_{rr}+\frac1r(\phi_z)_r\\
&=-\frac4{(1+r^2)^2}.
\end{aligned}
\]

그러므로

\[
\boxed{
K\,dA
=\frac4{(1+r^2)^2}dx\wedge dy.
}
\]

그런데

\[
dA=e^{2\phi_z}dx\wedge dy
=\frac4{(1+r^2)^2}dx\wedge dy.
\]

따라서

\[
\boxed{K=1.}
\]

---

# 24. 두 chart의 connection 차이

\[
\omega_z=-*d\phi_z.
\]

직접 계산하면

\[
\boxed{
\omega_z
=\frac{2r^2}{1+r^2}d\theta.
}
\]

\(w=se^{i\varphi}\) chart에서는

\[
\omega_w
=\frac{2s^2}{1+s^2}d\varphi.
\]

overlap에서

\[
s=r^{-1},
\qquad
\varphi=-\theta
\]

이므로

\[
\boxed{
\omega_w
=-\frac{2}{1+r^2}d\theta.
}
\]

따라서

\[
\boxed{
\omega_w-\omega_z=-2d\theta.
}
\]

같은 식은 Hodge star로 더 짧게 나온다.

\[
\begin{aligned}
\omega_w-\omega_z
&=-*d(\phi_w-\phi_z)\\
&=-2*d\log|z|\\
&=-2d\theta.
\end{aligned}
\]

이것이 Hodge star의 핵심 역할이다.

\[
\boxed{
\text{radial change }d\log|z|
\stackrel{*}{\longmapsto}
\text{angular change }d\theta.
}
\]

overlap에서 \(d(d\theta)=0\)이므로

\[
d\omega_w=d\omega_z.
\]

local connection은 다르지만 curvature는 global하게 붙는다.

---

# 25. 함수 \(z\)와 tangent section \(z\partial_z\)를 구분한다

함수 \(z\)는

\[
\operatorname{div}(z)=[0]-[\infty]
\]

를 갖는다. total degree는 \(0\)이다.

이제 tangent vector field

\[
s=z\frac{\partial}{\partial z}
\]

를 보자.

\(z\)-chart에서는 coefficient가 \(z\)이므로 원점에서 한 번 사라진다.

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

따라서 무한대에서도 한 번 사라진다.

\[
\boxed{
\text{zero divisor of }s
=[0]+[\infty].
}
\]

zero 총수는 \(2\)다.

이제 같은 정수 \(2\)가 세 번 나타난다.

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

# VII. Mayer–Vietoris를 partition of unity로 직접 계산한다

# 26. 적도 overlap의 winding form

\[
U_z\cap U_w\simeq\mathbf C^\times
\]

는 원과 같은 핵심 모양을 갖는다.

transition \(g=-z^2\)의 phase는 적도에서 두 번 돈다. 이를 기록하는 real 1-form을

\[
\boxed{
\alpha=\frac1\pi d\theta
}
\]

라고 두자.

\[
d\alpha=0,
\qquad
\int_{S^1}\alpha=2.
\]

---

# 27. partition of unity

\(\chi_z,\chi_w\)를 다음 조건을 만족하는 smooth functions라고 하자.

\[
0\le\chi_z,\chi_w\le1,
\qquad
\chi_z+\chi_w=1.
\]

또

- \(\chi_w=0\) near \(z=0\),
- \(\chi_z=0\) near \(w=0\)

가 되게 잡는다.

즉 두 chart의 기여도를 부드럽게 나누는 weight들이다.

local 1-form을

\[
A_z=\chi_w\alpha,
\qquad
A_w=-\chi_z\alpha
\]

로 둔다.

overlap에서

\[
\begin{aligned}
A_w-A_z
&=-(\chi_z+\chi_w)\alpha\\
&=-\alpha.
\end{aligned}
\]

이것은 round connection의 normalized gluing equation

\[
\frac{\omega_w}{2\pi}
-
\frac{\omega_z}{2\pi}
=-\frac1\pi d\theta
=-\alpha
\]

와 같다.

---

# 28. \(d\)를 취하면 global 2-form이 된다

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
\boxed{dA_z=dA_w.}
\]

두 local 2-form은 하나의 global 2-form으로 붙는다.

\[
\boxed{
F_{\mathrm{MV}}
=dA_z=dA_w.
}
\]

이것이 Mayer–Vietoris connecting calculation의 실물이다.

- overlap의 closed 1-form이 있고,
- partition of unity로 두 local 1-form을 만들고,
- \(d\)를 취해 global 2-form을 만든다.

---

# 29. 적분하면 winding \(2\)가 그대로 나온다

overlap annulus에서 \(\chi_w=\chi(r)\)라고 하자.

inner boundary 근방에서는 \(\chi=0\), outer boundary 근방에서는 \(\chi=1\)이 되게 잡는다.

그러면

\[
d\chi_w=\chi'(r)dr
\]

이고

\[
F_{\mathrm{MV}}
=\frac{\chi'(r)}\pi dr\wedge d\theta.
\]

따라서

\[
\begin{aligned}
\int_{\mathbf P^1}F_{\mathrm{MV}}
&=\int_0^{2\pi}\int
\frac{\chi'(r)}\pi dr\,d\theta\\
&=\frac{2\pi}{\pi}
\left(\chi(\text{outer})-\chi(\text{inner})\right)\\
&=2.
\end{aligned}
\]

즉

\[
\boxed{
\int_{\mathbf P^1}F_{\mathrm{MV}}=2.
}
\]

---

# 30. POU curvature와 round curvature의 비교

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

POU connection과 round connection의 차이를 각 chart에서 빼면 overlap에서 두 차이가 일치한다. 따라서 하나의 global 1-form \(B\)로 붙는다.

그 결과 두 curvature의 차이는

\[
\frac{K\,dA}{2\pi}-F_{\mathrm{MV}}=dB.
\]

구면에는 boundary가 없으므로 Stokes 정리에 의해

\[
\int_{\mathbf P^1}dB=0.
\]

따라서

\[
\boxed{
\int_{\mathbf P^1}\frac{K\,dA}{2\pi}
=
\int_{\mathbf P^1}F_{\mathrm{MV}}
=2.
}
\]

“같은 cohomology class”라는 말은 여기서는 다음 뜻이다.

> 두 closed 2-form의 차이가 global 1-form의 \(d\)이고, 따라서 닫힌 구면에서 적분값이 같다.

---

# VIII. 전체 계산을 한 표에 놓는다

| 관찰 대상 | local calculation | 정수 |
|---|---|---:|
| Gaussian 2-form | \(d\omega_0=e^{-r^2}dx\wedge dy\) |  |
| smooth primitive | \(\omega_0=(1-e^{-r^2})d\theta/2\) |  |
| Gaussian integral | \(\int_{\mathbf R^2}e^{-r^2}dxdy\) | \(\pi\) |
| Hodge star | coefficient vector의 90도 회전 |  |
| Laplacian | \(d(*d\psi)=\Delta\psi\,dx\wedge dy\) |  |
| 함수 \(z\) at \(0\) | \(z=z^1\) | \(+1\) |
| 함수 \(z\) at \(\infty\) | \(z=w^{-1}\) | \(-1\) |
| divisor of \(z\) | \([0]-[\infty]\) | total \(0\) |
| radial-to-angular | \(*d\log|z|=d\theta\) |  |
| 작은 원 적분 | \((2\pi)^{-1}\int d\theta\) | \(1\) |
| tangent transition | \(e_w=-z^2e_z\) | winding \(2\) |
| tangent section | \(z\partial_z=-w\partial_w\) | zeros \(1+1\) |
| connection difference | \(\omega_w-\omega_z=-2d\theta\) | period \(2\) |
| curvature | \(d\omega=K\,dA\) | \(\int KdA/(2\pi)=2\) |
| POU/MV | \(F_{\mathrm{MV}}=dA_z=dA_w\) | \(\int F_{\mathrm{MV}}=2\) |

---

# IX. 스터디에서 직접 할 최소 계산

## 계산 1

polar coordinate에서

\[
dx\wedge dy=rdr\wedge d\theta
\]

를 계산한다.

## 계산 2

\[
d\omega=e^{-r^2}dx\wedge dy
\]

를 만족하는

\[
\omega=A(r)d\theta
\]

를 찾고

\[
A(r)=C-\frac12e^{-r^2}
\]

를 얻는다.

## 계산 3

원점에서 smooth하다는 조건으로

\[
\omega_0=\frac{1-e^{-r^2}}2d\theta
\]

를 고른다.

## 계산 4

Stokes 정리로

\[
\int_{\mathbf R^2}e^{-x^2-y^2}dxdy=\pi
\]

를 계산한다.

## 계산 5

90도 회전 행렬

\[
J=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]

에서

\[
*dx=dy,
\qquad
*dy=-dx
\]

를 정의한다.

## 계산 6

\[
*d\log r=d\theta
\]

를 \(x,y\) 성분으로 확인한다.

## 계산 7

\[
d(*d\psi)=\Delta\psi\,dx\wedge dy
\]

를 직접 미분한다.

## 계산 8

세 ring

\[
\mathbf C[z],
\qquad
\mathbf C[z^{-1}],
\qquad
\mathbf C[z,z^{-1}]
\]

을 적는다.

## 계산 9

\[
\operatorname{ord}_0(z)=1,
\qquad
\operatorname{ord}_\infty(z)=-1
\]

을 확인한다.

## 계산 10

\[
dz=-w^{-2}dw,
\qquad
e_w=-z^2e_z
\]

를 계산한다.

## 계산 11

\[
\phi_w(1/z)-\phi_z(z)=2\log|z|
\]

과

\[
\omega_w-\omega_z=-2d\theta
\]

를 계산한다.

## 계산 12

POU로

\[
F_{\mathrm{MV}}=dA_z=dA_w
\]

를 만들고 적분이 \(2\)인지 확인한다.

---

# X. 마지막 압축

Hodge star는 처음부터 주어진 추상기호가 아니다.

Gaussian 2-form의 primitive를 찾으면 원주방향 1-form이 나오고, 그 coefficient vector를 90도 돌리면 방사방향 gradient가 나온다.

그 회전을 이름 붙인 것이

\[
\boxed{
*=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
}
\]

이다.

그래서

\[
\boxed{
*d\log|z|=d\theta
}
\]

이고

\[
\boxed{
d(*d\psi)=\Delta\psi\,dx\wedge dy.}
\]

conformal metric에서는 orthonormal frame의 회전량이

\[
\boxed{
\omega=-*d\phi
}
\]

이고, 한 번 더 미분하면

\[
\boxed{
d\omega=K\,dA.}
\]

따라서 전체 계산선은

\[
\boxed{
\begin{aligned}
e^{-r^2}dx\wedge dy
&\longrightarrow
\omega_0=\frac{1-e^{-r^2}}2d\theta\\
&\longrightarrow
\text{90도 회전 }*\\
&\longrightarrow
*d\log|z|=d\theta\\
&\longrightarrow
\operatorname{div}(z)=[0]-[\infty]\\
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
