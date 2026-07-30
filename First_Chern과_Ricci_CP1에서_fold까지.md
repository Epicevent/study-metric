# First Chern class와 Ricci curvature를 실제로 맞붙이는 계산노트

## $\mathbb{CP}^1$의 두 곡률을 손으로 계산하고, $T^2\to S^2$의 fold에서 무엇이 살아남는지 본다

먼저 이름을 붙이지 말고 두 번 미분한다. $z=x+iy$와

$$
S=1+|z|^2=1+z\bar z
$$

를 놓자. $\mathbb{CP}^1$의 Fubini--Study 계량을 이 노트의 정규화로 쓰면

$$
g_{z\bar z}=\frac1{S^2},
\qquad
ds^2=\frac{2}{S^2}(dx^2+dy^2),
$$

$$
\omega_{\mathrm{FS}}
=i g_{z\bar z}\,dz\wedge d\bar z
=\frac{i\,dz\wedge d\bar z}{S^2}.
$$

그런데 이 계량의 계수 $g_{z\bar z}$ 자체를 로그 미분하면

$$
\begin{aligned}
\rho
&=-i\,\partial\bar\partial\log g_{z\bar z}\\
&=-i\,\partial\bar\partial\log S^{-2}\\
&=2i\,\partial\bar\partial\log S\\
&=\frac{2i\,dz\wedge d\bar z}{S^2}\\
&=\boxed{2\omega_{\mathrm{FS}}}.
\end{aligned}
\tag{0.1}
$$

한 형식은 두 배다. 실제 적분도

$$
\int_{\mathbb{CP}^1}\omega_{\mathrm{FS}}=2\pi,
\qquad
\int_{\mathbb{CP}^1}\rho=4\pi
\tag{0.2}
$$

로 두 배다. 이 $1$과 $2$가 오늘 구별할 두 정수다.

$$
\frac1{2\pi}\int\omega_{\mathrm{FS}}=1,
\qquad
\frac1{2\pi}\int\rho=2.
\tag{0.3}
$$

첫 번째는 양의 생성자 $\mathcal O(1)$의 First Chern number이고, 두 번째는
$T\mathbb{CP}^1$의 First Chern number다. 둘 다 ``곡률 적분''이지만 **서로 다른
선다발의 곡률**이다. 지도교수님의 피드백을 이 노트에서 계산으로 붙잡을 지점이 바로 여기다.

---

## 이 노트의 목표와 사실 표기

이 노트가 답할 질문은 네 개다.

1. 왜 $\omega_{\mathrm{FS}}$는 Chern 수 $1$을, Ricci 형식 $\rho$는 Chern 수 $2$를 주는가?
2. $f:T^2\to\mathbb{CP}^1$가 이 두 형식을 어떻게 $T^2$로 옮기는가?
3. fold에서 pullback metric은 망가지는데 $f^*\rho$는 왜 망가지지 않는가?
4. $g+\varepsilon h$로 metric을 살린 뒤 $\varepsilon\to0$으로 보내면 같은 signed curvature가 나오는가?

표기는 다음처럼 구별한다.

- **[직접 계산]** 이 노트에서 미분하거나 적분해 얻은 식.
- **[논문]** Huang, *A Gauss-Bonnet Theorem for Quantum States*의 정의 또는 주장.
- **[표준 사실]** Chern--Weil, Gauss--Bonnet처럼 입력으로 쓰는 정리.
- **[검문]** 논문의 주장과 별도로 확인해야 하는 논리적 경계.

논문: [arXiv 2510.15760](https://arxiv.org/abs/2510.15760) ·
[HTML 원문](https://arxiv.org/html/2510.15760v1)

독립 검산은 다음 명령으로 한다.

$$
\texttt{python verify\_chern\_ricci\_fold.py}
$$

---

# 1. 워밍업 I — $dz\wedge d\bar z$에서 실제 면적을 꺼낸다

$z=x+iy$이므로

$$
dz=dx+i\,dy,
\qquad
d\bar z=dx-i\,dy.
$$

쐐기곱을 한 항씩 전개하면

$$
\begin{aligned}
dz\wedge d\bar z
&=(dx+i\,dy)\wedge(dx-i\,dy)\\
&=dx\wedge dx-i\,dx\wedge dy
  +i\,dy\wedge dx-i^2dy\wedge dy\\
&=-i\,dx\wedge dy+i(-dx\wedge dy)\\
&=-2i\,dx\wedge dy.
\end{aligned}
$$

따라서

$$
\boxed{i\,dz\wedge d\bar z=2\,dx\wedge dy}.
\tag{1.1}
$$

여기서 허수부가 갑자기 사라진 것이 아니다. $dz\wedge d\bar z$ 자체가 순허수이고,
앞의 $i$와 곱해져 실수 면적형식이 된 것이다. 그러므로

$$
\omega_{\mathrm{FS}}
=\frac{2}{(1+x^2+y^2)^2}\,dx\wedge dy.
\tag{1.2}
$$

## 1.1 반지름 적분으로 $2\pi$를 직접 얻는다

$x=r\cos\theta$, $y=r\sin\theta$이면 $dx\wedge dy=r\,dr\wedge d\theta$다.
그래서

$$
\begin{aligned}
\int_{\mathbb{CP}^1}\omega_{\mathrm{FS}}
&=\int_0^{2\pi}\int_0^\infty
\frac{2r}{(1+r^2)^2}\,dr\,d\theta\\
&=2\pi\int_0^\infty\frac{2r}{(1+r^2)^2}\,dr.
\end{aligned}
$$

$u=1+r^2$, $du=2r\,dr$를 넣으면

$$
\int_0^\infty\frac{2r}{(1+r^2)^2}\,dr
=\int_1^\infty u^{-2}\,du
=1.
$$

따라서

$$
\boxed{\int_{\mathbb{CP}^1}\omega_{\mathrm{FS}}=2\pi}.
\tag{1.3}
$$

---

# 2. 워밍업 II — $\partial\bar\partial\log S$를 한 줄도 생략하지 않는다

$z$와 $\bar z$를 독립변수처럼 미분한다. 먼저

$$
\bar\partial\log S
=\frac{1}{S}\bar\partial(1+z\bar z)
=\frac{z}{S}\,d\bar z.
$$

이제 $z/S$를 $z$로 미분한다.

$$
\begin{aligned}
\partial\left(\frac zS\right)
&=\frac{S\,\partial z-z\,\partial S}{S^2}\\
&=\frac{S-z\bar z}{S^2}\,dz\\
&=\frac1{S^2}\,dz.
\end{aligned}
$$

그러므로

$$
\boxed{
\partial\bar\partial\log S
=\frac{dz\wedge d\bar z}{S^2}}.
\tag{2.1}
$$

여기에 $i$를 곱한 것이 $\omega_{\mathrm{FS}}$다.

$$
\boxed{\omega_{\mathrm{FS}}=i\partial\bar\partial\log S}.
\tag{2.2}
$$

이 식은 퍼텐셜을 두 번 미분해서 metric과 면적형식을 얻었던 기존 CP¹ 손계산과
같은 식이다. 이제 **같은 미분기계에 어느 선다발의 metric을 넣는가**만 바꾼다.

---

# 3. 첫 번째 선다발 — 왜 $\mathcal O(1)$의 Chern 수가 $1$인가

양의 hyperplane line bundle $H=\mathcal O(1)$의 이 차트 국소 frame을 $e$라 하고,
그 Hermitian norm을

$$
h_H(z)=\|e(z)\|^2=\frac1S
\tag{3.1}
$$

로 둔다. 선다발의 Chern curvature convention을

$$
F_H=-\partial\bar\partial\log h_H
\tag{3.2}
$$

로 잠근다. 그러면

$$
\begin{aligned}
F_H
&=-\partial\bar\partial\log(S^{-1})\\
&=\partial\bar\partial\log S\\
&=\frac{dz\wedge d\bar z}{S^2}.
\end{aligned}
$$

따라서 그 First Chern form은

$$
c_1(H,h_H)
=\frac{i}{2\pi}F_H
=\frac{\omega_{\mathrm{FS}}}{2\pi}.
\tag{3.3}
$$

§1의 적분을 그대로 쓰면

$$
\boxed{\int_{\mathbb{CP}^1}c_1(H)=1}.
\tag{3.4}
$$

## 3.1 정규화된 상태로 같은 2-form을 다시 만든다

CP¹의 국소 단위상태를

$$
s(z)=\frac{(1,z)}{\sqrt S}
$$

로 잡는다. 곱미분을 하면

$$
s^\dagger ds
=\frac{\bar z\,dz-z\,d\bar z}{2S}.
\tag{3.5}
$$

실수 Berry potential을 이 노트에서는

$$
A=-i\,s^\dagger ds
=-\frac{i}{2S}(\bar z\,dz-z\,d\bar z)
$$

로 둔다. $z=x+iy$를 넣으면

$$
A=\frac{x\,dy-y\,dx}{1+x^2+y^2}.
\tag{3.6}
$$

이제 평범하게 외미분한다.

$$
\begin{aligned}
dA
&=d\left(\frac{x\,dy-y\,dx}{S}\right)\\
&=\frac{2\,dx\wedge dy}{S}
-\frac{2(x\,dx+y\,dy)\wedge(x\,dy-y\,dx)}{S^2}\\
&=\frac{2S-2(x^2+y^2)}{S^2}\,dx\wedge dy\\
&=\frac{2}{S^2}\,dx\wedge dy\\
&=\boxed{\omega_{\mathrm{FS}}}.
\end{aligned}
\tag{3.7}
$$

즉 이전 Reeb/Hopf 손계산의 $A\mapsto dA$와 지금의 Chern curvature는 같은
2-form에 도착한다.

> **부호 검문.** $s$가 span하는 tautological line은 $\mathcal O(-1)$이고
> $H=\mathcal O(1)$은 그 쌍대다. 수학의 $c_1(\mathcal O(-1))$와 물리의
> Berry-curvature convention 사이에는 흔히 마이너스가 들어간다. 이 노트는 논문의
> $C=(2\pi)^{-1}\int\Omega$가 양의 생성자를 세도록 $\Omega=dA=\omega_{\mathrm{FS}}$
> 로 잠갔다. 다른 convention을 쓰면 $C$의 부호만 함께 바꾸면 된다.

---

# 4. 두 번째 선다발 — Ricci curvature는 왜 정확히 두 배인가

이번에 미분할 metric은 $H$의 $h_H=S^{-1}$이 아니라 접다발의 metric이다.
국소 holomorphic frame $\partial_z$의 norm은 상수배를 무시하면

$$
h_T(z)=\|\partial_z\|^2=g_{z\bar z}=S^{-2}.
\tag{4.1}
$$

그래서 접다발의 Chern curvature는

$$
\begin{aligned}
F_T
&=-\partial\bar\partial\log h_T\\
&=-\partial\bar\partial\log(S^{-2})\\
&=2\partial\bar\partial\log S\\
&=2F_H.
\end{aligned}
\tag{4.2}
$$

그 실수형식 $iF_T$가 Ricci form이다.

$$
\boxed{\rho=iF_T=2\omega_{\mathrm{FS}}}.
\tag{4.3}
$$

따라서

$$
\boxed{
c_1(T\mathbb{CP}^1)
=\left[\frac{\rho}{2\pi}\right]
=2\left[\frac{\omega_{\mathrm{FS}}}{2\pi}\right]
=2c_1(H)}.
\tag{4.4}
$$

## 4.1 왜 접다발이 $\mathcal O(2)$인지 winding으로 재확인한다

무한대 차트 $w=1/z$에서 연쇄법칙을 쓰면

$$
\frac{\partial}{\partial w}
=\frac{dz}{dw}\frac{\partial}{\partial z}
=-\frac1{w^2}\frac{\partial}{\partial z}
=-z^2\frac{\partial}{\partial z}.
\tag{4.5}
$$

겹침의 전이함수에서 상수 $-1$은 감김수 $0$, $z^2$는 감김수 $2$다. 따라서

$$
\boxed{T\mathbb{CP}^1\simeq\mathcal O(2)}.
\tag{4.6}
$$

§4의 로그 미분이 준 계수 $2$와 전이함수 $z^2$의 winding $2$가 일치한다.
이것이 ``Ricci form이 First Chern class를 대표한다''는 말을 CP¹에서 손으로
확인한 내용이다.

## 4.2 같은 숫자들을 엔티티별로 분리한다

| 적분하는 2-form | 어느 선다발의 곡률인가 | 정규화 적분 |
|---|---|---:|
| $\omega_{\mathrm{FS}}$ | $H=\mathcal O(1)$ | $1$ |
| $-\omega_{\mathrm{FS}}$ | tautological $\mathcal O(-1)$ | $-1$ |
| $\rho=2\omega_{\mathrm{FS}}$ | $T\mathbb{CP}^1\simeq\mathcal O(2)$ | $2$ |

이 표에서 $1$과 $2$를 같은 ``Chern number''라고 뭉개면 이후의 $2\pi$와
$4\pi$가 전부 헷갈린다.

---

# 5. 이제 $f:T^2\to\mathbb{CP}^1$가 구면의 곡률을 토러스로 옮긴다

## 5.1 먼저 방향을 정확히 말한다

점은

$$
f:T^2\longrightarrow\mathbb{CP}^1
$$

방향으로 간다. 2-form은 그 반대 방향으로 pullback된다.

$$
\omega_{\mathrm{FS}}
\quad\longmapsto\quad
f^*\omega_{\mathrm{FS}},
\qquad
\rho
\quad\longmapsto\quad
f^*\rho.
$$

그러나 ``반대로 옮긴다''는 말은 값의 방향을 뒤집는다는 뜻이 아니다. source의 두
벡터 $X,Y\in T_kT^2$를 먼저 $df_kX,df_kY$로 target에 보낸 뒤 target form이
그 둘을 읽는다는 뜻이다.

$$
(f^*\rho)_k(X,Y)
=\rho_{f(k)}(df_kX,df_kY).
\tag{5.1}
$$

## 5.2 projector에서 metric과 signed area를 동시에 계산한다

논문의 lower-band projector를

$$
P(k)=\frac12(I+n(k)\cdot\sigma),
\qquad |n(k)|=1
\tag{5.2}
$$

로 쓴다. 논문의 $n$은 $n=-\hat d$다. Pauli 행렬의 곱

$$
(a\cdot\sigma)(b\cdot\sigma)
=(a\cdot b)I+i(a\times b)\cdot\sigma,
\qquad
\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}
\tag{5.3}
$$

만 쓴다.

$P_\mu=\frac12n_\mu\cdot\sigma$이므로 논문의 trace metric은

$$
\begin{aligned}
g_{\mu\nu}
&=\operatorname{tr}(P_\mu P_\nu)\\
&=\frac14\operatorname{tr}ig((n_\mu\cdot\sigma)(n_\nu\cdot\sigma)\big)\\
&=\boxed{\frac12n_\mu\cdot n_\nu}.
\end{aligned}
\tag{5.4}
$$

한편 commutator는

$$
[P_x,P_y]
=\frac14[n_x\cdot\sigma,n_y\cdot\sigma]
=\frac{i}{2}(n_x\times n_y)\cdot\sigma.
$$

따라서

$$
\begin{aligned}
\bar\lambda
&=-i\operatorname{tr}\big(P[P_x,P_y]\big)\\
&=-i\operatorname{tr}\left[
\frac{I+n\cdot\sigma}{2}\,
\frac{i}{2}(n_x\times n_y)\cdot\sigma
\right]\\
&=\boxed{\frac12n\cdot(n_x\times n_y)}.
\end{aligned}
\tag{5.5}
$$

$|n|^2=1$을 미분하면 $n\cdot n_x=n\cdot n_y=0$이다. 즉 $n_x,n_y$는
구면의 접평면에 있고, $n_x\times n_y$는 $n$과 평행하다. 그러므로

$$
\begin{aligned}
\det g
&=\frac14\left(|n_x|^2|n_y|^2-(n_x\cdot n_y)^2\right)\\
&=\frac14|n_x\times n_y|^2\\
&=\bar\lambda^2.
\end{aligned}
$$

즉

$$
\boxed{\sqrt{\det g}=|\bar\lambda|}.
\tag{5.6}
$$

metric은 제곱 때문에 부호를 잊고, 2-form은 부호를 보존한다.

$$
dA=|\bar\lambda|\,dk_x\wedge dk_y,
\qquad
d\bar A=\bar\lambda\,dk_x\wedge dk_y.
\tag{5.7}
$$

그리고 (5.5)는 문자 그대로 구면 면적형식의 pullback이다.

$$
\boxed{d\bar A=f^*\omega_{\mathrm{FS}}}.
\tag{5.8}
$$

> **정규화 검문.** (5.4)는 단위구면 계량의 $1/2$배다. 따라서 projector
> 구면의 반지름은 $1/\sqrt2$, Gauss curvature는 $2$, 총면적은 $2\pi$다.
> 논문 본문의 ``radius $1/2$''라는 문장은 같은 줄의 $K_G=2$ 및 trace metric과
> 양립하지 않는다. 반지름 $1/2$라면 곡률은 $4$여야 한다.

---

# 6. 논문의 실제 two-band map에서 부호가 뒤집히는 두 점을 본다

논문의 $m_0=1$ model은

$$
d(k_x,k_y)
=\big(\sin k_x,\sin k_y,1-\cos k_x-\cos k_y\big),
$$

$$
n=-\frac d{|d|},
\qquad
r=|d|.
\tag{6.1}
$$

먼저

$$
d_x=(\cos k_x,0,\sin k_x),
\qquad
d_y=(0,\cos k_y,\sin k_y).
$$

외적은

$$
d_x\times d_y
=(-\sin k_x\cos k_y,-\cos k_x\sin k_y,\cos k_x\cos k_y).
$$

내적을 한 항씩 모으면

$$
\begin{aligned}
d\cdot(d_x\times d_y)
&=-\sin^2k_x\cos k_y-\cos k_x\sin^2k_y\\
&\quad +(1-\cos k_x-\cos k_y)\cos k_x\cos k_y\\
&=\cos k_x\cos k_y-\cos k_x-\cos k_y.
\end{aligned}
\tag{6.2}
$$

정규화 사상의 표준 미분식과 $n=-\hat d$의 마이너스를 쓰면

$$
n\cdot(n_x\times n_y)
=-\frac{d\cdot(d_x\times d_y)}{r^3}.
$$

따라서

$$
\boxed{
\bar\lambda(k_x,k_y)
=\frac{\cos k_x+\cos k_y-\cos k_x\cos k_y}{2r^3}}
\tag{6.3}
$$

이고

$$
r^2=3-2\cos k_x-2\cos k_y+2\cos k_x\cos k_y.
\tag{6.4}
$$

## 6.1 양의 점: $(0,0)$

$$
d=(0,0,-1),\qquad n=(0,0,1),
$$

$$
n_x=(-1,0,0),\qquad n_y=(0,-1,0).
$$

그러므로

$$
g(0,0)=
\begin{pmatrix}
1/2&0\\0&1/2
\end{pmatrix},
\qquad
\bar\lambda(0,0)=\frac12.
\tag{6.5}
$$

## 6.2 음의 점: $(\pi,\pi)$

$$
d=(0,0,3),\qquad n=(0,0,-1),
$$

$$
n_x=(1/3,0,0),\qquad n_y=(0,1/3,0).
$$

따라서

$$
g(\pi,\pi)=
\begin{pmatrix}
1/18&0\\0&1/18
\end{pmatrix},
\qquad
\bar\lambda(\pi,\pi)=-\frac1{18}.
\tag{6.6}
$$

같은 양의 frame $(\partial_{k_x},\partial_{k_y})$를 target으로 보냈는데, 첫 점에서는
오른손 frame이고 둘째 점에서는 왼손 frame이다. 연속함수 $\bar\lambda$가
$1/2$에서 $-1/18$로 바뀌었으므로 그 사이 어딘가에서 반드시 $0$을 지난다.
실제 singular set은

$$
\boxed{\cos k_x+\cos k_y-\cos k_x\cos k_y=0}.
\tag{6.7}
$$

이것이 이 예시에서의 ``중간값정리 같은 직관''을 완전히 적은 식이다.

---

# 7. 구면의 Ricci curvature가 토러스에서 무엇이 되는가

CP¹에서 이미

$$
\rho=2\omega_{\mathrm{FS}}
$$

를 계산했다. 이제 pullback의 선형성만 쓴다.

$$
\begin{aligned}
f^*\rho
&=f^*(2\omega_{\mathrm{FS}})\\
&=2f^*\omega_{\mathrm{FS}}\\
&=2\bar\lambda\,dk_x\wedge dk_y.
\end{aligned}
\tag{7.1}
$$

regular point에서는 $df$가 가역이고, pullback metric $g=f^*g_{\mathrm{FS}}$의
Gauss curvature는 target과 같은 $K_G=2$다. 이것은 별도의 신탁이 아니다.
정의상

$$
g_k(X,Y)=g_{\mathrm{FS},f(k)}(df_kX,df_kY),
\tag{7.2}
$$

이고 $df_k$가 가역인 작은 이웃에서는 이 등식 자체가 $f$를 local isometry로
만든다. 따라서 그 작은 이웃의 곡률도 $2$다.

그러므로 regular locus에서

$$
\boxed{
K_G\,d\bar A
=2\bar\lambda\,dk_x\wedge dk_y
=f^*\rho}.
\tag{7.3}
$$

이 식이 논문의 signed Gauss-curvature integral을 First Chern class와 연결한다.

$$
\begin{aligned}
\frac1{4\pi}\int_{T^2}K_G\,d\bar A
&=\frac1{4\pi}\int_{T^2}f^*\rho\\
&=\frac1{4\pi}\int_{T^2}2f^*\omega_{\mathrm{FS}}\\
&=\frac1{2\pi}\int_{T^2}f^*\omega_{\mathrm{FS}}\\
&=\deg f.
\end{aligned}
\tag{7.4}
$$

논문의 convention에서는 이 degree가 Chern number $C$다. 이 model에서는

$$
\boxed{deg f=C=1}.
\tag{7.5}
$$

따라서

$$
\int_{T^2}f^*\omega_{\mathrm{FS}}=2\pi,
\qquad
\int_{T^2}f^*\rho=4\pi.
\tag{7.6}
$$

여기까지는 fold의 singular curvature를 전혀 쓰지 않았다. target에서 이미 성립한
$\rho=2\omega_{\mathrm{FS}}$를 pullback하고 degree 공식을 썼을 뿐이다.

---

# 8. ``전체가 양수거나 전체가 음수여야 하지 않나?''의 정확한 엔티티

그 엔티티는 $K_G$가 아니다. regular locus에서 $K_G=2$는 실제로 계속 양수다.
부호를 가진 것은

$$
\boxed{\bar\lambda
=\text{$f^*\omega_{\mathrm{FS}}$의 $dk_x\wedge dk_y$ 계수}}
\tag{8.1}
$$

이고, 같은 부호를 가진 Ricci-curvature coefficient는 $2\bar\lambda$다.

만약 $df$가 모든 점에서 가역이라면 $\bar\lambda$는 연속이고 한 번도 $0$이 아니다.
$T^2$는 연결되어 있으므로 중간값정리에 의해

$$
\bar\lambda>0\text{ everywhere}
\qquad\text{또는}\qquad
\bar\lambda<0\text{ everywhere}.
\tag{8.2}
$$

그러면 $g=f^*g_{\mathrm{FS}}$는 $T^2$ 전체의 매끄러운 Riemannian metric이고
$K_g=2$다. 따라서

$$
\int_{T^2}K_g\,dA_g
=2\operatorname{Area}_g(T^2)>0.
\tag{8.3}
$$

하지만 ordinary Gauss--Bonnet은

$$
\int_{T^2}K_g\,dA_g
=2\pi\chi(T^2)=0
\tag{8.4}
$$

을 요구한다. 모순이다. 따라서

$$
\boxed{df\text{는 어딘가에서 rank를 잃어야 하고 }\bar\lambda=0\text{인 점이 존재한다}.}
\tag{8.5}
$$

이 논리는 ``구면의 양의 곡률을 토러스 전체에 local isometry로 복사할 수 없다''는
관찰을 미적분학의 부호 연속성과 Gauss--Bonnet으로 적은 것이다.

## 8.1 서로 다른 네 정수를 섞지 않는다

| 정수 | 어느 다발/공간을 재는가 | 이 예시의 값 |
|---|---|---:|
| $\chi(T^2)$ | source의 접다발 $TT^2$ | $0$ |
| $\chi(S^2)=c_1(TS^2)[S^2]$ | target의 접다발 | $2$ |
| $C=\deg f$ | pullback eigenline의 Berry convention | $1$ |
| $c_1(f^*T\mathbb{CP}^1)[T^2]$ | target 접다발을 pullback한 다발 | $2C=2$ |

$f^*T\mathbb{CP}^1$와 $TT^2$는 같은 다발이 아니다. $df$가 모든 점에서
동형이었다면 둘이 동형이 되었겠지만, 바로 그 가능성이 (8.3)--(8.5)에서 막혔다.
그래서

$$
\int_{T^2}f^*\rho=4\pi
$$

와

$$
\int_{T^2}K_{TT^2}\,dA=0
$$

는 전혀 모순이 아니다. 서로 다른 다발의 Chern form을 적분한 것이다.

---

# 9. $g+\varepsilon h$ 공격 — 정말 signed curvature를 복구하는가

먼저 $g+\varepsilon I$라고만 쓰면 좌표를 바꿀 때 $I$가 무엇인지 정해지지 않는다.
전역적으로 하려면 $T^2$에 미리 고른 background metric $h$가 필요하다.

$$
g_\varepsilon=f^*g_{\mathrm{FS}}+\varepsilon h,
\qquad \varepsilon>0.
\tag{9.1}
$$

그러면 $g_\varepsilon$은 양의 정부호이므로 역행렬과 ordinary curvature를 계산할 수
있다. 문제는 그 극한이 **무엇을 기억하느냐**다.

## 9.1 fold normal form 하나에 직접 넣는다

target의 한 stereographic patch를 $(X,Y)$로 쓰고

$$
g_{\mathrm{FS}}
=\Lambda(X,Y)(dX^2+dY^2),
\qquad
\omega_{\mathrm{FS}}=\Lambda(X,Y)dX\wedge dY,
$$

$$
\Lambda(X,Y)=\frac{2}{(1+X^2+Y^2)^2}
\tag{9.2}
$$

로 둔다. ordinary fold의 local model은

$$
f(u,v)=(u,v^2).
\tag{9.3}
$$

미분하면

$$
dX=du,
\qquad
dY=2v\,dv.
$$

따라서 pullback metric은

$$
g
=\Lambda(u,v^2)(du^2+4v^2dv^2),
\tag{9.4}
$$

signed area는

$$
d\bar A
=f^*\omega_{\mathrm{FS}}
=2v\Lambda(u,v^2)\,du\wedge dv,
\tag{9.5}
$$

ordinary area는

$$
dA
=2|v|\Lambda(u,v^2)\,du\wedge dv.
\tag{9.6}
$$

$v>0$과 $v<0$은 같은 target 쪽을 덮지만 orientation은 반대다. metric의 determinant는
$v^2$만 보므로 그 차이를 잊는다.

## 9.2 regularization의 극한을 fold 양쪽에서 비교한다

$h=du^2+dv^2$를 택하면

$$
g_\varepsilon
=(\Lambda+\varepsilon)du^2+(4v^2\Lambda+\varepsilon)dv^2.
\tag{9.7}
$$

고정된 $v\ne0$에서는 $\varepsilon\to0$일 때 $g_\varepsilon\to g$가 매끄럽다.
따라서

$$
K_{g_\varepsilon}\longrightarrow 2,
\qquad
dA_{g_\varepsilon}\longrightarrow2|v|\Lambda\,du\wedge dv.
$$

그러므로

$$
K_{g_\varepsilon}dA_{g_\varepsilon}
\longrightarrow
4|v|\Lambda\,du\wedge dv.
\tag{9.8}
$$

하지만 우리가 보존하려던 Ricci pullback은

$$
f^*\rho
=2f^*\omega_{\mathrm{FS}}
=4v\Lambda\,du\wedge dv.
\tag{9.9}
$$

$v<0$에서 (9.8)과 (9.9)는 부호가 반대다. 따라서

$$
\boxed{
g+\varepsilon h\text{의 ordinary curvature measure는 }
f^*\rho\text{를 그대로 복구하지 않는다}.}
\tag{9.10}
$$

이유는 단순하다. $g_\varepsilon$은 끝까지 Riemannian metric이므로 orientation-reversing
sheet도 양의 면적으로 센다. signed 2-form이 가진 방향 정보는 metric만으로 복구되지 않는다.

## 9.3 전역 검문은 더 강하다

$g_\varepsilon$이 $T^2$의 매끄러운 metric이면 모든 $\varepsilon>0$에 대해

$$
\int_{T^2}K_{g_\varepsilon}\,dA_{g_\varepsilon}
=2\pi\chi(T^2)=0.
\tag{9.11}
$$

반면 degree $1$인 Bloch map은

$$
\int_{T^2}f^*\rho=4\pi.
\tag{9.12}
$$

따라서 두 measure의 전역 극한이 아무 보정 없이 같을 수 없다. $g_\varepsilon$의 curvature는
fold 근처에서 concentration을 만들 수 있지만, 그 전체 질량은 (9.11)을 지켜야 한다.
이 concentration을 분석하는 것은 흥미로운 별도 문제지만, 그것을 곧바로 논문의
$d\bar A$나 $\kappa_s$와 동일시하면 안 된다.

---

# 10. 논문의 ``limiting curvature''는 무엇의 극한인가

논문의 singular curvature $\kappa_s$는

$$
g_\varepsilon=g+\varepsilon h
$$

의 Gauss curvature 극한으로 정의되지 않는다. 논문은 singular curve에 맞춘 좌표 $(u,v)$에서
$v=0$으로 다가가며 **regular sheet의 geodesic curvature**를 본다.

논문의 식 (29)--(31)의 구조는

$$
\Gamma^v_{uu}
=\frac{2EF_u-FE_u-EE_v}{2(EG-F^2)}
$$

에서 분모 $EG-F^2=\det g=\bar\lambda^2$가 $0$이 되는 문제를

$$
\kappa_g
=\frac{\Gamma^v_{uu}\,\bar\lambda}{E^{3/2}}
$$

와 함께 묶어 한 개의 $\bar\lambda$를 상쇄하고, 남은 $0/0$에 L'Hôpital을 적용하는 것이다.
즉 극한 대상은

$$
\boxed{
\text{regularized metric의 Gauss curvature가 아니라,
regular side에서 singular curve로 가는 geodesic curvature}}
\tag{10.1}
$$

다.

그리고 논문의 두 Gauss--Bonnet 식에서 역할도 다르다.

- unsigned $\int K_GdA$를 Euler characteristic과 맞출 때는 singular boundary term
  $2\int\kappa_sds$가 필요하다.
- signed $\int K_Gd\bar A$를 Chern number와 맞출 때는 (7.3)의
  $f^*\rho=2f^*\omega_{\mathrm{FS}}$가 중심이고 singular-curvature 항은 소거된다.

따라서 ``limiting curvature가 Chern number를 만든다''고 읽으면 층위가 섞인다.
Chern 수를 직접 운반하는 것은 signed pullback 2-form이다.

---

# 11. 이 계산으로 논문을 어디까지 읽었고, 무엇은 아직 검증하지 않았는가

## 11.1 이 노트에서 직접 확인된 것

1. CP¹에서 $\rho=2\omega_{\mathrm{FS}}$.
2. $c_1(T\mathbb{CP}^1)=2c_1(\mathcal O(1))$.
3. two-band projector에서 $d\bar A=f^*\omega_{\mathrm{FS}}$.
4. regular locus에서 $K_Gd\bar A=f^*\rho$.
5. 따라서 signed curvature integral은 degree/Chern number다.
6. $g+\varepsilon h$는 orientation sign을 잃으므로 이 signed form의 단순 대체물이 아니다.

## 11.2 논문의 도구가 실제로 일을 하는 지점

$\rho=2\omega_{\mathrm{FS}}$와 degree 공식만으로 signed integral은 이미 계산된다.
따라서 이 부분 자체가 front 이론의 성과는 아니다. front/singular-curvature 장치가 실제로
일하는 곳은 **unsigned quantum volume의 초과분과 fold 경계항을 ordinary
Gauss--Bonnet 방식으로 정리하는 부분**이다.

## 11.3 별도로 검증해야 하는 것

- 논문이 택한 normal과 $(f,N)$이 strict front 정의에서 실제 immersion인지.
- cusp를 포함한 singular set이 generalized Gauss--Bonnet 정리의 가정을 만족하는지.
- 수치 singular-curvature 적분과 cusp 처리의 수렴이 충분한지.
- multi-band에서 $\rho$와 Berry/Chern 형식의 관계가 어떤 다발 사상으로 남는지.

이 항목들은 (7.3)이 맞다는 사실만으로 자동 해결되지 않는다.

---

# 12. 하루 손계산 순서 — 답을 가리고 직접 할 일

## A. 워밍업: form이 실제 면적이 되는 데까지

1. $dz\wedge d\bar z=-2i\,dx\wedge dy$를 전개한다.
2. $\partial\bar\partial\log(1+z\bar z)$를 몫미분으로 계산한다.
3. $\int_{\mathbb C}i\,dz\wedge d\bar z/S^2=2\pi$를 극좌표로 계산한다.
4. $A=(xdy-ydx)/S$를 외미분하여 $dA=\omega_{\mathrm{FS}}$를 얻는다.

## B. First Chern class 두 개를 분리한다

5. $h_H=S^{-1}$를 $-\partial\bar\partial\log h_H$에 넣는다.
6. $h_T=S^{-2}$를 같은 식에 넣고 정확히 어디서 계수 $2$가 생기는지 표시한다.
7. $w=1/z$에서 $\partial_w=-z^2\partial_z$를 유도하고 작은 원에서 $z^2$의 winding을 센다.

## C. two-band map으로 옮긴다

8. Pauli 곱셈식만으로 (5.4)와 (5.5)를 다시 유도한다.
9. $d\cdot(d_x\times d_y)$를 전개하여 (6.2)를 얻는다.
10. $(0,0)$과 $(\pi,\pi)$에서 $n_x,n_y,g,\bar\lambda$를 모두 계산한다.
11. $\bar\lambda=0$의 방정식을 얻고 대각선 $k_x=k_y$에서 실제 근을 구한다.
12. 수치적분으로 $\int_{T^2}\bar\lambda\,dk_xdk_y=2\pi$를 확인한다.

## D. metric regularization을 공격한다

13. $f(u,v)=(u,v^2)$에서 $d\bar A$와 $dA$를 따로 계산한다.
14. $v=1$과 $v=-1$에서 $K,d\bar A$의 부호가 반대이고 $K,dA$는 같은 부호임을 확인한다.
15. $g_\varepsilon=g+\varepsilon(du^2+dv^2)$의 determinant를 계산하고,
    $v\ne0$에서 $dA_{g_\varepsilon}\to dA_g$를 확인한다.
16. Gauss--Bonnet으로 $\int K_{g_\varepsilon}dA_{g_\varepsilon}=0$과
    $\int f^*\rho=4\pi$를 대조하여, 필요한 singular concentration의 총질량을 생각한다.

---

# 13. 검산용 답

1. $-2i\,dx\wedge dy$.
2. $dz\wedge d\bar z/S^2$.
3. $2\pi$.
4. $2dx\wedge dy/S^2$.
5. $F_H=\partial\bar\partial\log S$.
6. $F_T=2\partial\bar\partial\log S$; $\log S^{-2}=-2\log S$에서 $2$가 나온다.
7. winding $2$, 따라서 $T\mathbb{CP}^1\simeq\mathcal O(2)$.
8. $g_{\mu\nu}=\frac12n_\mu\cdot n_\nu$,
   $\bar\lambda=\frac12n\cdot(n_x\times n_y)$.
9. $\cos k_x\cos k_y-\cos k_x-\cos k_y$.
10. $(0,0)$에서는 $g=\frac12I$, $\bar\lambda=1/2$;
    $(\pi,\pi)$에서는 $g=\frac1{18}I$, $\bar\lambda=-1/18$.
11. 대각선에서 $2c-c^2=0$이므로 허용되는 근은 $c=0$, 즉
    $k_x=k_y=\pm\pi/2$; 이 점들은 cusp 후보라 ordinary fold 계산과 따로 다뤄야 한다.
12. $2\pi$.
13. $d\bar A=2v\Lambda\,du\wedge dv$, $dA=2|v|\Lambda\,du\wedge dv$.
14. signed coefficient는 $4v\Lambda$, unsigned coefficient는 $4|v|\Lambda$.
15. $\det g_\varepsilon=(\Lambda+\varepsilon)(4v^2\Lambda+\varepsilon)$.
16. regularization curvature measure는 fold 부근의 추가 singular measure 없이는
    signed Ricci pullback으로 갈 수 없다.

---

## 마지막에 남겨 둘 한 문장

$$
\boxed{
\text{fold에서 죽는 것은 }(f^*g_{\mathrm{FS}})^{-1}\text{이고,}
\quad
\text{살아남는 것은 }f^*\rho=2f^*\omega_{\mathrm{FS}}\text{이다}.}
$$

metric은 orientation을 제곱해 잊지만, Chern--Ricci 2-form은 그 부호를 보존한다.
논문의 signed curvature 공식을 읽을 기준은 이 차이다.
