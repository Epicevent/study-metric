# 라플라시안으로 바꾸고 싶다

## \(\pi e^{-R^2}\)밖에 안 나온 자리에서 적도의 winding과 구면의 곡률까지

처음 궁금했던 것은 이것이다.

\[
\iint_{\mathbf R^2}e^{-x^2-y^2}\,dx\,dy
\]

를 극좌표로 바로 풀지 않고, 라플라시안과 발산정리로 풀 수 없을까?

가우스곡률도

\[
K=-e^{-2\phi}\Delta\phi
\]

꼴로 나오니, Gaussian 적분에서도

\[
e^{-x^2-y^2}=-\Delta\phi
\]

를 만들면 비슷한 계산이 될 것 같다.

그런데 \(\phi\)를 바로 찾으려 하니 막힌다.

그래서 손노트에서는 먼저

\[
\Omega=e^{-x^2-y^2}\,dx\wedge dy
\]

를 한 번 적분해

\[
d\omega=\Omega
\]

인 \(\omega\)를 찾고, 그 \(\omega\)의 원주방향을 방사방향으로 돌려 gradient를 만들려고 했다.

그 계산을 그대로 끝까지 밀어 본다.

중간에 실제로 생겼던 실패도 지우지 않는다.

> 외곽 경계만 계산하면 \(\pi e^{-R^2}\) 비슷한 항만 나오고, \(R\to\infty\)에서 오히려 \(0\)이 된다.  
> 빠진 \(\pi\)는 어디에 있는가?

그 빠진 항을 찾다 보면

\[
d\theta,
\qquad
\log r,
\qquad
\text{zero와 pole},
\qquad
\text{winding},
\qquad
\text{두 chart의 connection 차이}
\]

가 한 계산으로 묶인다.

---

# 1. 먼저 \(d\omega=\Omega\)를 푼다

\[
\boxed{
\Omega=e^{-r^2}\,dx\wedge dy,
\qquad
r^2=x^2+y^2.
}
\]

극좌표에서

\[
x=r\cos\theta,
\qquad
y=r\sin\theta
\]

이므로

\[
\boxed{
dx\wedge dy=r\,dr\wedge d\theta.}
\]

따라서

\[
\Omega=e^{-r^2}r\,dr\wedge d\theta.
\]

회전대칭을 그대로 따라

\[
\omega=A(r)d\theta
\]

라고 놓는다.

그러면

\[
d\omega=A'(r)dr\wedge d\theta.
\]

따라서

\[
A'(r)=re^{-r^2}.
\]

적분하면

\[
\boxed{
A(r)=C-\frac12e^{-r^2}.
}
\]

즉

\[
\omega_C=\left(C-\frac12e^{-r^2}\right)d\theta
\]

는 모두 같은 \(\Omega\)를 만든다.

\[
d\omega_C=\Omega.
\]

여기서 손노트가 먼저 집은 것은

\[
\boxed{
\omega_\infty=-\frac12e^{-r^2}d\theta.
}
\]

이 선택은 \(r\to\infty\)에서 사라진다.

일단 이걸 그대로 따라간다.

---

# 2. \(\omega_\infty\)는 원주방향이다

\[
\boxed{
d\theta=\frac{-y\,dx+x\,dy}{r^2}.}
\]

따라서

\[
\begin{aligned}
\omega_\infty
&=-\frac12e^{-r^2}d\theta\\
&=
\frac{e^{-r^2}}{2r^2}
\left(y\,dx-x\,dy\right).
\end{aligned}
\]

1-form의 coefficient pair만 보면

\[
\boxed{
F_\infty
=
\frac{e^{-r^2}}{2r^2}(y,-x).
}
\]

벡터 \((y,-x)\)는 원에 접한다.

즉 \(F_\infty\)는 원주방향이다.

그런데 회전대칭 함수 \(\phi(r)\)의 gradient는

\[
\nabla\phi
=
\phi'(r)\left(\frac xr,\frac yr\right)
\]

처럼 방사방향이어야 한다.

그래서 손노트에서 원주방향을 \(90^\circ\) 돌렸다.

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

\[
J(y,-x)=(x,y).
\]

따라서

\[
\boxed{
G_\infty
=JF_\infty
=
\frac{e^{-r^2}}{2r^2}(x,y).
}
\]

이제 방사방향이 되었다.

---

# 3. 방사방향이 되었으니 gradient라고 놓아 본다

\[
\nabla\phi_\infty=G_\infty
\]

라고 놓는다.

방사형 함수의 gradient와 비교하면

\[
\phi_\infty'(r)rac{(x,y)}r
=
\frac{e^{-r^2}}{2r^2}(x,y).
\]

따라서

\[
\boxed{
\phi_\infty'(r)=\frac{e^{-r^2}}{2r}.
}
\]

적분하면 exponential integral이 나온다.

\[
\boxed{
\phi_\infty(r)
=
\frac14\operatorname{Ei}(-r^2)+C.
}
\]

하지만 닫힌꼴은 중요하지 않다.

라플라시안에는 \(\phi_\infty'\)만 있으면 된다.

2차원 radial Laplacian은

\[
\Delta\phi
=
\frac1r\frac{d}{dr}\left(r\phi'(r)\right).
\]

여기서는

\[
r\phi_\infty'(r)=\frac12e^{-r^2}.
\]

따라서

\[
\begin{aligned}
\Delta\phi_\infty
&=
\frac1r\frac{d}{dr}\left(\frac12e^{-r^2}\right)\\
&=
\frac1r\left(-re^{-r^2}\right)\\
&=-e^{-r^2}.
\end{aligned}
\]

즉 원하던 식이 나왔다.

\[
\boxed{
-\Delta\phi_\infty=e^{-r^2}
\qquad(r>0).
}
\]

여기까지는 손노트의 의도대로 잘 된다.

이제 발산정리를 쓰면 끝날 것 같다.

---

# 4. 외곽 경계만 계산하면 답이 사라진다

\[
G_\infty=\nabla\phi_\infty
=
\frac{e^{-r^2}}{2r^2}(x,y).
\]

반지름 \(R\)인 원에서 바깥쪽 단위법선은

\[
n=\frac{(x,y)}R.
\]

따라서

\[
G_\infty\cdot n
=
\frac{e^{-R^2}}{2R}.
\]

또

\[
ds=R\,d\theta.
\]

외곽 경계의 flux 크기는

\[
\boxed{
\int_{|z|=R}G_\infty\cdot n\,ds
=
\pi e^{-R^2}.
}
\]

손노트 마지막 페이지에서 나온 항이 이것이다.

그런데 \(R\to\infty\)이면 이 값은 \(0\)으로 간다.

Gaussian 적분은 \(\pi\)여야 한다.

무언가가 빠졌다.

부호 convention을 어떻게 잡든 핵심 문제는 같다.

> 외곽 경계 하나만 보면 \(e^{-R^2}\) 항만 남고, 상수 \(\pi\)가 없다.

---

# 5. 빠진 것은 원점의 안쪽 경계다

\(G_\infty\)를 원점 근방에서 본다.

\[
G_\infty
\sim
\frac1{2r^2}(x,y)
=
\frac1{2r}e_r.
\]

원점에서 singular하다.

그러므로 발산정리를 disk 전체에 바로 쓸 수 없다.

실제로 계산할 영역은

\[
A_{\varepsilon,R}
=
\{\varepsilon\le r\le R\}
\]

인 annulus다.

annulus의 boundary는 두 개다.

- 바깥 원 \(r=R\)의 outward normal은 \(+e_r\).
- 안쪽 원 \(r=\varepsilon\)의 outward normal은 annulus 바깥쪽을 향하므로 \(-e_r\).

따라서 바깥 flux는

\[
\pi e^{-R^2}
\]

이고, 안쪽 flux는

\[
-\pi e^{-\varepsilon^2}
\]

이다.

전체 flux는

\[
\pi e^{-R^2}-\pi e^{-\varepsilon^2}.
\]

한편

\[
-\operatorname{div}G_\infty=e^{-r^2}.
\]

따라서

\[
\begin{aligned}
\int_{A_{\varepsilon,R}}e^{-r^2}\,dx\,dy
&=
-\int_{\partial A_{\varepsilon,R}}G_\infty\cdot n\,ds\\
&=
\pi e^{-\varepsilon^2}-\pi e^{-R^2}.
\end{aligned}
\]

\(\varepsilon\to0\)으로 보내면

\[
\boxed{
\int_{|z|\le R}e^{-r^2}\,dx\,dy
=
\pi(1-e^{-R^2}).
}
\]

그리고 \(R\to\infty\)이면

\[
\boxed{
\int_{\mathbf R^2}e^{-r^2}\,dx\,dy=\pi.
}
\]

빠진 \(\pi\)는 원점의 안쪽 경계에 있었다.

이것이 손노트 계산에서 실제로 더 가야 할 첫 지점이다.

---

# 6. 원점의 안쪽 경계를 없애는 다른 방법

아까 일반해는

\[
\omega_C
=
\left(C-\frac12e^{-r^2}\right)d\theta
\]

였다.

\(C=0\)인 \(\omega_\infty\)는 무한대에서 편하지만 원점에서 singular했다.

이번에는

\[
C=\frac12
\]

를 택한다.

\[
\boxed{
\omega_0
=
\frac{1-e^{-r^2}}2d\theta.
}
\]

원점 근방에서

\[
1-e^{-r^2}=r^2+O(r^4)
\]

이므로

\[
\omega_0
=
\frac{1-e^{-r^2}}{2r^2}
(-y\,dx+x\,dy)
\]

는 원점까지 smooth하게 연장된다.

이제 disk 전체에 Stokes를 바로 쓸 수 있다.

\[
\int_{D_R}\Omega
=
\int_{\partial D_R}\omega_0.
\]

경계에서

\[
\omega_0
=
\frac{1-e^{-R^2}}2d\theta.
\]

따라서

\[
\boxed{
\int_{D_R}e^{-r^2}\,dx\,dy
=
\pi(1-e^{-R^2}).
}
\]

같은 답이 inner boundary 없이 나온다.

두 primitive의 차이는

\[
\boxed{
\omega_0-\omega_\infty
=
\frac12d\theta.
}
\]

그리고

\[
d(d\theta)=0
\qquad(r>0).
\]

즉 둘은 punctured plane에서 같은 \(d\omega\)를 만든다.

하지만

\[
\int_{|z|=1}\frac12d\theta=\pi
\]

이므로 \(\frac12d\theta\)는 아무 전역 single-valued 함수의 미분이 아니다.

이 closed 1-form이 바로 빠진 안쪽 경계 \(\pi\)를 들고 있다.

---

# 7. potential에서도 같은 보정이 보인다

\(\omega_\infty\)에 대응하는 potential은

\[
\phi_\infty(r)
=
\frac14\operatorname{Ei}(-r^2).
\]

원점 근방에서

\[
\operatorname{Ei}(-r^2)
=
2\log r+\text{smooth term}
\]

이므로

\[
\phi_\infty(r)
=
\frac12\log r+\text{smooth term}.
\]

원점의 singularity가 정확히 \(\frac12\log r\)다.

그러므로

\[
\boxed{
\phi_0
=
\phi_\infty-\frac12\log r
}
\]

라고 놓으면 원점의 log singularity가 사라진다.

그리고

\[
\omega_0
=
\omega_\infty+rac12d\theta.
\]

두 보정이 같은 것인지 확인한다.

방사방향 \(d\log r\)를 원주방향으로 \(90^\circ\) 돌리면

\[
\boxed{
*d\log r=d\theta.
}
\]

따라서

\[
- *d\phi_0
=
-*d\phi_\infty+rac12*d\log r
=
\omega_\infty+rac12d\theta
=
\omega_0.
\]

즉

- potential에서는 \(\frac12\log r\)를 빼고,
- primitive에서는 \(\frac12d\theta\)를 더한다.

같은 보정이다.

---

# 8. 이제서야 이 회전에 Hodge star라는 이름을 붙인다

지금까지 실제로 한 일은 coefficient vector를 \(90^\circ\) 돌린 것이다.

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

1-form

\[
\alpha=P\,dx+Q\,dy
\]

의 coefficient pair \((P,Q)\)를

\[
(-Q,P)
\]

로 돌리는 연산을

\[
\boxed{
*(P\,dx+Q\,dy)
=-Q\,dx+P\,dy
}
\]

라고 쓰자.

그러면

\[
*dx=dy,
\qquad
*dy=-dx.
\]

이 노트에서 Hodge star는 처음부터 주어진 개념이 아니다.

> 원주방향 primitive를 방사방향 gradient로 바꾸기 위해 실제로 사용한 회전행렬의 이름이다.

함수 \(\phi\)에 대해

\[
d\phi=\phi_xdx+\phi_ydy
\]

이므로

\[
*d\phi=-\phi_y dx+\phi_xdy.
\]

다시 \(d\)를 취하면

\[
\begin{aligned}
d(*d\phi)
&=
(\phi_{xx}+\phi_{yy})dx\wedge dy\\
&=
\Delta\phi\,dx\wedge dy.
\end{aligned}
\]

따라서 앞의 Gaussian 계산은

\[
\boxed{
\omega=-*d\phi,
\qquad
d\omega=-\Delta\phi\,dx\wedge dy
}
\]

로 압축된다.

이 표기는 계산 뒤에 붙인 이름일 뿐이다.

---

# 9. 가장 작은 모델은 \(\log r\)다

Gaussian potential의 singular part가 \(\frac12\log r\)였으므로, 이제 \(\log r\) 자체를 본다.

\[
d\log r=\frac{dr}{r}.
\]

\[
*dr=r\,d\theta
\]

이므로

\[
\boxed{
*d\log r=d\theta.
}
\]

원점을 뺀 곳에서는

\[
\Delta\log r=0.
\]

그런데 작은 원에서는

\[
\int_{|z|=\varepsilon}d\theta=2\pi.
\]

따라서

\[
\boxed{
\frac1{2\pi}
\int_{|z|=\varepsilon}*d\log|z|
=1.
}
\]

원점을 뺀 곳에서는 라플라시안이 \(0\)인데, 원점을 둘러싼 경계는 정수 \(1\)을 기억한다.

Gaussian 계산에서 빠진 inner boundary와 완전히 같은 모양이다.

---

# 10. \(\mathbf P^1\)에서 함수 \(z\)의 zero와 pole

두 chart를 잡는다.

\[
U_z:\ z=\frac{Z_1}{Z_0},
\qquad
U_w:\ w=\frac{Z_0}{Z_1}.
\]

\[
\boxed{w=z^{-1}.}
\]

각 chart와 overlap의 ring은

\[
\boxed{
\mathbf C[z],
\qquad
\mathbf C[w]=\mathbf C[z^{-1}],
\qquad
\mathbf C[z,z^{-1}].
}
\]

원점에서는

\[
z=z^1
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

작은 원 적분으로 읽으면

- \(z=0\)에서 \((2\pi)^{-1}\int d\theta=+1\),
- \(w=0\)에서 \(\log|z|=-\log|w|\)이므로 \(-1\)

이다.

zero와 pole은 Gaussian 계산의 inner boundary 부호와 같은 방식으로 나타난다.

---

# 11. \(dz=-w^{-2}dw\): 같은 계산이 두 배가 된다

\[
z=\frac1w
\]

를 미분하면

\[
\boxed{
dz=-w^{-2}dw.}
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

따라서 transition은

\[
\boxed{g(z)=-z^2.}
\]

적도 \(|z|=1\)에서 \(z=e^{i\theta}\)이면

\[
g(z)=-e^{2i\theta}.
\]

따라서 \(g\)는 두 번 돈다.

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
\frac{dz}{z}
=d\log r+i\,d\theta
\]

이므로

\[
\boxed{
g^{-1}dg
=2d\log|z|+2i\,d\theta.}
\]

Gaussian에서 보았던

\[
\log r
\quad\longleftrightarrow\quad
d\theta
\]

가 transition에서는 정확히 두 배로 나타난다.

---

# 12. round sphere에서도 먼저 local primitive를 찾는다

round metric을

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
=
\log2-\log(1+|z|^2).
}
\]

Gaussian 계산에서 이미

\[
-\Delta\phi\,dx\wedge dy
=d(-*d\phi)
\]

를 얻었다.

그래서 구면에서도

\[
\boxed{
\omega_z=-*d\phi_z
}
\]

를 local primitive로 잡는다.

나중에 이 \(\omega_z\)를 connection 1-form이라고 부른다.

## 12.1 \(z\)-chart에서 계산

\[
\phi_z(r)=\log2-\log(1+r^2).
\]

\[
\phi_z'(r)=-\frac{2r}{1+r^2}.
\]

따라서

\[
\begin{aligned}
\omega_z
&=-*d\phi_z\\
&=-\phi_z'(r)*dr\\
&=\frac{2r^2}{1+r^2}d\theta.
\end{aligned}
\]

\[
\boxed{
\omega_z
=
\frac{2r^2}{1+r^2}d\theta.
}
\]

이 식은 \(r=0\)에서 \(r^2d\theta\)처럼 되어 smooth하다.

한 번 더 \(d\)를 취하면

\[
\begin{aligned}
d\omega_z
&=
\frac{4r}{(1+r^2)^2}dr\wedge d\theta\\
&=
\frac4{(1+r^2)^2}dx\wedge dy.
\end{aligned}
\]

metric의 area form도

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

2차원에서 곡률 2-form을 \(K\,dA\)라고 쓰므로

\[
\boxed{K=1.}
\]

---

# 13. 다른 chart에서는 다른 primitive가 나온다

\(w=1/z\)이고

\[
\phi_w(w)=\log2-\log(1+|w|^2).
\]

같은 overlap에서 비교하면

\[
\boxed{
\phi_w(1/z)-\phi_z(z)=2\log|z|.
}
\]

따라서

\[
\begin{aligned}
\omega_w-\omega_z
&=-*d(\phi_w-\phi_z)\\
&=-2*d\log|z|\\
&=-2d\theta.
\end{aligned}
\]

즉

\[
\boxed{
\omega_w-\omega_z=-2d\theta.
}
\]

직접 계산해도

\[
\omega_w
=-\frac{2}{1+r^2}d\theta
\]

가 나온다.

\(\omega_z\)는 \(z=0\) pole에서 smooth하고,
\(\omega_w\)는 \(w=0\) pole에서 smooth하다.

둘은 overlap에서 \(-2d\theta\)만큼 다르다.

그리고

\[
d(d\theta)=0
\]

이므로

\[
\boxed{d\omega_z=d\omega_w.}
\]

local primitive는 다르지만 curvature는 하나로 붙는다.

---

# 14. Gaussian 계산과 구면 계산은 같은 모양이다

| Gaussian plane | round sphere |
|---|---|
| \(\omega_\infty=-\frac12e^{-r^2}d\theta\) | \(\omega_z=\frac{2r^2}{1+r^2}d\theta\) |
| 무한대에서 편하지만 원점에서 singular | 한 pole에서 smooth |
| \(\omega_0=\frac{1-e^{-r^2}}2d\theta\) | \(\omega_w=-\frac2{1+r^2}d\theta\) |
| 원점에서 smooth | 다른 pole에서 smooth |
| 차이 \(\frac12d\theta\) | 차이 \(-2d\theta\) |
| 빠진 inner boundary가 \(\pi\) | 적도 winding이 \(2\) |
| 둘 다 같은 \(d\omega=\Omega\) | 둘 다 같은 \(d\omega=K\,dA\) |

두 경우 모두 다음 일이 일어난다.

1. 한쪽에서 편한 primitive는 다른 특이점에서 문제가 생긴다.
2. 두 primitive의 차이는 \(d\theta\)의 상수배다.
3. 그 차이는 punctured overlap에서 closed다.
4. 그러나 원주 적분이 0이 아니어서 전역 exact가 아니다.
5. \(d\)를 취하면 차이는 사라지고 같은 2-form이 나온다.

Gaussian 손노트에서 빠진 안쪽 경계가, 구면에서는 적도 overlap의 winding으로 다시 나타난다.

---

# 15. 적도의 winding form을 두 chart에 나누어 놓는다

transition \(-z^2\)의 winding을 기록하는 real 1-form을

\[
\boxed{
\alpha=\frac1\pi d\theta
}
\]

라고 두자.

\[
\int_{S^1}\alpha=2.
\]

두 smooth weight \(\chi_z,\chi_w\)를

\[
\chi_z+\chi_w=1
\]

이 되게 잡는다.

- \(\chi_w=0\) near \(z=0\),
- \(\chi_z=0\) near \(w=0\).

그리고

\[
A_z=\chi_w\alpha,
\qquad
A_w=-\chi_z\alpha
\]

라고 둔다.

그러면 overlap에서

\[
A_w-A_z=-\alpha.
\]

또 \(d\alpha=0\)이므로

\[
\begin{aligned}
dA_z
&=d\chi_w\wedge\alpha,\\
dA_w
&=-d\chi_z\wedge\alpha\\
&=d\chi_w\wedge\alpha.
\end{aligned}
\]

따라서

\[
\boxed{dA_z=dA_w.}
\]

두 local 2-form이 하나의 global 2-form으로 붙는다.

이 계산에 붙는 이름이 Mayer–Vietoris connecting calculation이다.

annulus에서 \(\chi_w=\chi(r)\)라고 놓으면

\[
F_{\mathrm{MV}}
=
\frac{\chi'(r)}\pi dr\wedge d\theta.
\]

따라서

\[
\begin{aligned}
\int_{\mathbf P^1}F_{\mathrm{MV}}
&=
\frac1\pi
\int_0^{2\pi}d\theta
\int\chi'(r)dr\\
&=2.
\end{aligned}
\]

즉

\[
\boxed{
\int_{\mathbf P^1}F_{\mathrm{MV}}=2.
}
\]

Gaussian annulus에서 안쪽 경계가 빠진 적분을 복구했던 것과 같은 계산이다.

---

# 16. 함수 \(z\)와 tangent section을 구분한다

함수 \(z\)는

\[
\operatorname{div}(z)=[0]-[\infty]
\]

였다.

zero와 pole이 상쇄되어 total degree는 \(0\)이다.

이번에는 tangent vector field

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

따라서 무한대에서도 한 번 사라진다.

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

# 17. 이번 계산에서 실제로 얻은 것

처음에는 Gaussian 적분을 라플라시안으로 바꾸고 싶었다.

그런데 바로 potential을 찾지 못해

\[
d\omega=\Omega
\]

부터 풀었다.

그 primitive가 원주방향이어서 \(90^\circ\) 돌려 방사 gradient를 만들었다.

그 결과

\[
-\Delta\phi=e^{-r^2}
\]

를 얻었다.

하지만 potential과 vector field가 원점에서 singular해서 외곽 경계만 계산하면 답이 빠졌다.

annulus의 안쪽 경계를 넣거나,

\[
\omega_0-\omega_\infty=\frac12d\theta
\]

라는 closed winding form으로 primitive를 보정해야 했다.

그 보정은 potential에서는

\[
\phi_0-\phi_\infty=-\frac12\log r
\]

였다.

그래서

\[
*d\log r=d\theta
\]

가 자연스럽게 나타났다.

이제 구면에서는 좌표변환이

\[
dz=-w^{-2}dw
\]

이므로 같은 현상이 두 배로 나타났다.

\[
\phi_w-\phi_z=2\log|z|,
\qquad
\omega_w-\omega_z=-2d\theta.
\]

그리고 적도의 \(2d\theta\)를 두 chart에 나누어 놓고 \(d\)를 취하면 구면 전체의 curvature 2-form이 나왔다.

최종 계산선은 다음이다.

\[
\boxed{
\begin{aligned}
\iint e^{-r^2}
&\longrightarrow
\omega_\infty=-\frac12e^{-r^2}d\theta\\
&\longrightarrow
\nabla\phi_\infty
\longrightarrow
-\Delta\phi_\infty=e^{-r^2}\\
&\longrightarrow
\text{빠진 inner boundary }\pi\\
&\longrightarrow
\omega_0-\omega_\infty=\frac12d\theta\\
&\longrightarrow
*d\log r=d\theta\\
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
\end{aligned}}
\]

Hodge star, connection, Mayer–Vietoris는 이 계산을 한 뒤 붙인 이름들이다.

---

# 18. 직접 다시 할 계산

1. \(dx\wedge dy=r\,dr\wedge d\theta\)를 계산한다.
2. \(d(A(r)d\theta)=e^{-r^2}r\,dr\wedge d\theta\)에서 \(A(r)\)를 구한다.
3. \(\omega_\infty=-\frac12e^{-r^2}d\theta\)의 coefficient vector를 적는다.
4. 그 vector를 \(90^\circ\) 돌려 방사 vector \(G_\infty\)를 얻는다.
5. \(\nabla\phi_\infty=G_\infty\)에서 \(\phi_\infty'(r)=e^{-r^2}/(2r)\)를 얻는다.
6. \(-\Delta\phi_\infty=e^{-r^2}\)를 계산한다.
7. 외곽 경계 flux가 \(\pi e^{-R^2}\) 크기밖에 안 나오는 것을 확인한다.
8. annulus의 안쪽 경계를 넣어 \(\pi(1-e^{-R^2})\)를 복원한다.
9. \(\omega_0=\omega_\infty+\frac12d\theta\)가 원점에서 smooth함을 확인한다.
10. \(\phi_0=\phi_\infty-\frac12\log r\)에서 log singularity가 소거되는지 확인한다.
11. \(*d\log r=d\theta\)를 성분으로 확인한다.
12. \(\operatorname{div}(z)=[0]-[\infty]\)를 두 chart에서 계산한다.
13. \(dz=-w^{-2}dw\)에서 tangent transition \(-z^2\)를 얻는다.
14. \(\phi_w-\phi_z=2\log|z|\)와 \(\omega_w-\omega_z=-2d\theta\)를 계산한다.
15. \(d\omega_z=K\,dA=dA\)를 계산한다.
16. partition of unity로 만든 global 2-form의 적분이 \(2\)인지 계산한다.
17. \(z\partial_z=-w\partial_w\)의 zero가 두 개인지 확인한다.
