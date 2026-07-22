# Reeb 벡터장 — $S^3$에서 $\Sigma^9$로, $\mathbb{CP}^1$에서 $\mathrm{Gr}(2,4)$로

> **이 글이 시작하는 자리.** [파트 IV 완전 상세](Reeb벡터장_완전계산.html)에서는 $S^3\to\mathbb{CP}^1$ 위에서 Reeb 벡터장을 실좌표로 계산했다. [걸음 6](걸음6_Gr24_플뤼커_완전판.html)은 $\Sigma^9\to\mathrm{Gr}(2,4)$에서도 “같은 계산”이라고 적었지만, 실제로 같은지 여섯 성분을 놓고 확인하지 않았다. [$(1,z)$에서 $(I,Z)$로](사전_1z에서_IZ로.html)의 §9 첫 번째 구멍이 바로 이것이었다.
>
> 여기서는 “Boothby–Wang”, “prequantization”을 출발점으로 삼지 않는다. 단위벡터의 위상속도를 읽는 1-형식을 먼저 만들고, $S^3$에서 계산한 뒤, 플뤼커 벡터가 사는 $\Sigma^9$에서 같은 식을 다시 계산한다. $U(2)$의 네 방향 가운데 어느 세 방향이 플뤼커 벡터를 아예 움직이지 않고, 어느 한 방향이 Reeb 방향으로 남는지도 행렬로 확인한다.
>
> **정규화.** 이 글의 $\alpha$는 기존 Reeb 문서와 같다. 따라서 아래층으로 내려간 $d\alpha$는 걸음 6의
> $$\omega=\frac{i}{2}\,\partial\bar\partial\log K$$
> 의 **두 배**다. 이 글에서는 이 둘을 같은 글자로 부르지 않는다:
> 아래 사영을 $\pi:\Sigma^9\to\mathrm{Gr}(2,4)$라 쓸 때
> $$\boxed{\ \pi^*\Omega=d\alpha,\qquad \omega:=\frac12\Omega=\frac{i}{2}\partial\bar\partial\log K\ }.$$

---

## §0. 왜 이 $\alpha$인가 — 위상속도를 숫자로 읽고 싶다

$\mathbb C^m$의 단위구면 위 점을

$$p=(p_1,\ldots,p_m),\qquad p^\dagger p=\sum_{j=1}^m|p_j|^2=1$$

이라 하자. $p$를 따라 움직이는 곡선 $p(t)$를 잡고 $p(0)=p$, $\dot p(0)=X$라 쓰자. 곡선이 단위구면 안에 있으므로

$$p(t)^\dagger p(t)=1$$

을 $t$로 미분하면

$$\frac d{dt}\Big|_0p(t)^\dagger p(t)=X^\dagger p+p^\dagger X=0.$$

두 항은 서로 켤레이므로

$$2\operatorname{Re}(p^\dagger X)=0,\qquad p^\dagger X\in i\mathbb R.$$

단위구면의 접벡터 $X$에 대해서는 $p^\dagger X$가 순허수다. 따라서

$$\boxed{\ \alpha_p(X):=-i\,p^\dagger X\ }$$

는 실수다. 이 식은 아직 이름이 아니라 요구에서 나왔다. 단위벡터가 움직일 때 그 움직임 중 $ip$ 방향의 양을 읽고 싶어서 만든 것이다.

실제로 위상만 바꾸는 곡선

$$p(t)=e^{it}p$$

의 속도는

$$X=\frac d{dt}\Big|_0e^{it}p=ip$$

이고,

$$\alpha_p(ip)=-i\,p^\dagger(ip)=-i\cdot i\,p^\dagger p=1.$$

반대로 $p^\dagger H=0$인 방향은

$$\alpha_p(H)=-i\,p^\dagger H=0$$

이다. 임의의 접벡터 $X$에서

$$\beta:=\alpha_p(X)=-i\,p^\dagger X\in\mathbb R$$

를 잡고

$$H:=X-\beta(ip)$$

라 두면

$$p^\dagger H=p^\dagger X-i\beta
=p^\dagger X-i(-i\,p^\dagger X)
=p^\dagger X-p^\dagger X=0.$$

따라서

$$\boxed{\ X=\underbrace{\alpha(X)\,ip}_{\text{위상만 바꾸는 부분}}+\underbrace{H}_{p^\dagger H=0}\ }.$$

$\alpha$가 “접속형식”이라는 말은 이 분해를 나중에 부르는 이름이다. 지금 계산으로 확인한 것은 더 구체적이다. $\alpha$는 접벡터가 가진 위상속도의 계수를 읽고, 그 계수만큼 $ip$를 빼면 $p$와 에르미트 직교하는 움직임이 남는다.

### 0.1 복소식에서 실좌표식이 나오는 자리

$p_j=x_j+iy_j$라고 쓰자. 접벡터 $X$에 값을 넣기 전의 1-형식으로는

$$\alpha=\frac{i}{2}\sum_{j=1}^m\bigl(p_j\,d\bar p_j-\bar p_j\,dp_j\bigr).$$

성분 하나를 전개하면

$$p\,d\bar p=(x+iy)(dx-i\,dy)
=x\,dx+y\,dy+i(y\,dx-x\,dy),$$

$$\bar p\,dp=(x-iy)(dx+i\,dy)
=x\,dx+y\,dy-i(y\,dx-x\,dy).$$

빼고 $i/2$를 곱하면

$$\frac i2(p\,d\bar p-\bar p\,dp)=x\,dy-y\,dx.$$

따라서

$$\boxed{\ \alpha=\sum_{j=1}^m(x_j\,dy_j-y_j\,dx_j)\ }.$$

이 식이 $-ip^\dagger dp$와 같은지도 단위구면 위에서 직접 확인할 수 있다. $N=p^\dagger p=1$을 미분하면

$$dp^\dagger p+p^\dagger dp=dN=0,$$

이므로

$$\frac i2\bigl(dp^\dagger p-p^\dagger dp\bigr)
=\frac i2\bigl(-p^\dagger dp-p^\dagger dp\bigr)
=-i\,p^\dagger dp.$$

왼쪽은 성분으로 쓴 $\alpha$다.

### 0.2 $d\alpha$에는 무엇이 남는가

성분 하나에서 외미분의 곱 규칙을 적용한다:

$$d(x_j\,dy_j)=dx_j\wedge dy_j+x_jd(dy_j)=dx_j\wedge dy_j,$$

$$d(-y_j\,dx_j)=-dy_j\wedge dx_j-y_jd(dx_j)=dx_j\wedge dy_j.$$

따라서

$$\boxed{\ d\alpha=2\sum_{j=1}^m dx_j\wedge dy_j\ }.$$

위상회전의 속도장을 실좌표로 쓰면

$$R=\sum_{j=1}^m\left(-y_j\frac\partial{\partial x_j}+x_j\frac\partial{\partial y_j}\right).$$

$dx_j(R)=-y_j$, $dy_j(R)=x_j$이므로

$$\alpha(R)=\sum_j\bigl(x_j^2+y_j^2\bigr)=N.$$

또한

$$\iota_R(dx_j\wedge dy_j)
=dx_j(R)\,dy_j-dy_j(R)\,dx_j
=-y_j\,dy_j-x_j\,dx_j,$$

따라서

$$\boxed{\ \iota_Rd\alpha=-2\sum_j(x_j\,dx_j+y_j\,dy_j)=-dN\ }.$$

주변 공간 $\mathbb C^m$에서는 $-dN$이 0이 아니다. 단위구면의 접벡터 $X$에 대해서만

$$dN(X)=\frac d{dt}\Big|_0N(p(t))=\frac d{dt}\Big|_0 1=0$$

이므로 $\iota_Rd\alpha=0$이 된다. 이 구분은 $m=2$에서도, $m=6$에서도 그대로 유지된다.

---

## §1. $S^3\to\mathbb{CP}^1$에서 계산을 닫아 본다

이제 $m=2$로 둔다. $\psi=(z_1,z_2)\in S^3\subset\mathbb C^2$이고

$$N=|z_1|^2+|z_2|^2=1.$$

위상곡선과 그 속도는

$$\gamma_\psi(\theta)=e^{i\theta}\psi,\qquad
\gamma_\psi'(0)=i\psi=R_\psi.$$

$z_r=x_r+iy_r$로 쓰면

$$R=-y_1\partial_{x_1}+x_1\partial_{y_1}
-y_2\partial_{x_2}+x_2\partial_{y_2}.$$

§0의 계산을 두 성분에 적용하면

$$\alpha(R)=|z_1|^2+|z_2|^2=1,$$

$$\iota_Rd\alpha=-d\bigl(|z_1|^2+|z_2|^2\bigr)=0
\qquad\text{on }S^3.$$

이 두 식 때문에 $R$을 $\alpha$의 Reeb 벡터장이라 부른다. 그러나 이름보다 먼저 보아야 할 것은 $R=i\psi$라는 값이다. $R$의 적분곡선은 정확히

$$\theta\longmapsto e^{i\theta}\psi,$$

즉 같은 $\mathbb{CP}^1$ 점을 나타내는 대표들이다.

### 1.1 한 점에서 네 실성분을 모두 넣는다

$$\psi=\frac1{\sqrt2}(1,i)$$

를 잡는다. 실좌표로는

$$x_1=\frac1{\sqrt2},\quad y_1=0,\quad x_2=0,\quad y_2=\frac1{\sqrt2}.$$

따라서

$$R_\psi=\frac1{\sqrt2}\partial_{y_1}-\frac1{\sqrt2}\partial_{x_2}.$$

이 점에서

$$\alpha
=\frac1{\sqrt2}dy_1-\frac1{\sqrt2}dx_2$$

이므로

$$\alpha(R_\psi)
=\frac1{\sqrt2}\cdot\frac1{\sqrt2}
-\frac1{\sqrt2}\cdot\left(-\frac1{\sqrt2}\right)=1.$$

위상곡선을 직접 미분해도

$$e^{i\theta}\psi
=\frac1{\sqrt2}\bigl(\cos\theta+i\sin\theta,\,-\sin\theta+i\cos\theta\bigr),$$

$$\frac d{d\theta}\Big|_0e^{i\theta}\psi
=\frac1{\sqrt2}(i,-1),$$

실좌표 속도는 $(0,1/\sqrt2,-1/\sqrt2,0)$이다. 방금 얻은 $R_\psi$와 성분까지 같다.

### 1.2 국소 절단을 고르면 $\alpha$가 아래층의 1-형식으로 보인다

$z_1\neq0$인 차트에서 $z=z_2/z_1=x+iy$라 하고, 위상을 하나 골라

$$s(z)=\frac{(1,z)}{\sqrt S},\qquad S=1+|z|^2=1+x^2+y^2$$

로 둔다. 이것은 $S^3\to\mathbb{CP}^1$의 각 원에서 첫 성분이 양의 실수가 되도록 대표 하나를 고른 것이다.

실좌표는

$$x_1=S^{-1/2},\quad y_1=0,\quad x_2=xS^{-1/2},\quad y_2=yS^{-1/2}.$$

$r=1$ 성분은 $x_1dy_1-y_1dx_1=0$이다. $r=2$ 성분은

$$dx_2=S^{-1/2}dx+x\,d(S^{-1/2}),$$

$$dy_2=S^{-1/2}dy+y\,d(S^{-1/2}).$$

따라서

$$\begin{aligned}
x_2dy_2-y_2dx_2
&=xS^{-1/2}\bigl(S^{-1/2}dy+y\,d(S^{-1/2})\bigr)\\
&\quad-yS^{-1/2}\bigl(S^{-1/2}dx+x\,d(S^{-1/2})\bigr).
\end{aligned}$$

$xyS^{-1/2}d(S^{-1/2})$가 두 번, 부호만 반대로 나타나므로 없어지고

$$\boxed{\ A:=s^*\alpha=\frac{x\,dy-y\,dx}{S}\ }.$$

이제 $dA$를 몫의 미분으로 계산한다. 먼저

$$d(x\,dy-y\,dx)=dx\wedge dy-dy\wedge dx=2dx\wedge dy,$$

$$d(S^{-1})=-S^{-2}dS=-\frac{2x\,dx+2y\,dy}{S^2}.$$

곱의 외미분을 쓰면

$$\begin{aligned}
dA
&=d(S^{-1})\wedge(x\,dy-y\,dx)+S^{-1}d(x\,dy-y\,dx)\\
&=-\frac{(2x\,dx+2y\,dy)\wedge(x\,dy-y\,dx)}{S^2}
+\frac{2dx\wedge dy}{S}.
\end{aligned}$$

첫 번째 분자의 쐐기곱을 네 항으로 펴면

$$2x^2dx\wedge dy-2xy\,dx\wedge dx
+2xy\,dy\wedge dy-2y^2dy\wedge dx$$

이고 가운데 두 항은 0, 마지막은 $dy\wedge dx=-dx\wedge dy$ 때문에 부호가 바뀐다. 따라서

$$dA=-\frac{2(x^2+y^2)}{S^2}dx\wedge dy+\frac{2S}{S^2}dx\wedge dy
=\boxed{\ \frac{2\\,dx\wedge dy}{(1+x^2+y^2)^2}\ }.$$

$dz\wedge d\bar z=-2i\,dx\wedge dy$이므로 같은 식은

$$\boxed{\ dA=\frac{i\\,dz\wedge d\bar z}{(1+|z|^2)^2}\ }.$$

걸음 6의 정규화는 이 형식의 절반이다:

$$\omega=\frac12dA
=\frac{i}{2}\frac{dz\wedge d\bar z}{(1+|z|^2)^2}.$$

따라서

$$\int_{\mathbb C}dA
=\int_0^{2\pi}\int_0^\infty\frac{2r}{(1+r^2)^2}\\,dr\,d\theta
=2\pi,$$

$$\int_{\mathbb C}\omega=\pi.$$

두 값은 서로 다른 계산 결과가 아니라 $d\alpha=2\omega$라는 한 개의 정규화 선택이다.

---

## §2. $\mathrm{Gr}(2,4)$ 위에 올라가기 전에 $\Sigma^9$를 실제로 만든다

$\mathbb C^4$의 2차원 평면에서 기저 두 개를 열로 세운다. $p_{12}\neq0$인 차트에서는 가우스 소거 후

$$V(a,b,c,d)
=\begin{pmatrix}
1&0\\
0&1\\
a&c\\
b&d
\end{pmatrix}
=\begin{pmatrix}I\\ Z\end{pmatrix},\qquad
Z=\begin{pmatrix}a&c\\ b&d\end{pmatrix}.$$

두 열을 $v,w$라 하자. $v\wedge w$의 여섯 성분은 두 행씩 고른 행렬식이다:

$$q_{12}=1,$$

$$q_{13}=\det\begin{pmatrix}1&0\\a&c\end{pmatrix}=c,\qquad
q_{14}=\det\begin{pmatrix}1&0\\b&d\end{pmatrix}=d,$$

$$q_{23}=\det\begin{pmatrix}0&1\\a&c\end{pmatrix}=-a,\qquad
q_{24}=\det\begin{pmatrix}0&1\\b&d\end{pmatrix}=-b,$$

$$q_{34}=\det\begin{pmatrix}a&c\\b&d\end{pmatrix}=ad-bc.$$

$\Delta:=ad-bc$라 줄이면

$$\boxed{\ q(Z)=(1,c,d,-a,-b,\Delta)\in\mathbb C^6\ }.$$

이 여섯 성분은

$$F(q):=q_{12}q_{34}-q_{13}q_{24}+q_{14}q_{23}$$

에 대해

$$F(q)=1\cdot(ad-bc)-c(-b)+d(-a)
=ad-bc+bc-ad=0$$

을 만족한다.

### 2.1 $F=0$은 실수 조건 몇 개인가

$F$는 복소수 값을 내므로 $F=0$은

$$\operatorname{Re}F=0,\qquad \operatorname{Im}F=0$$

이라는 실수 조건 두 개다. $\mathbb C^6$은 실 12차원이다. $F=0$인 원뿔이 원점 밖에서 실제로 실 10차원인지 미분으로 확인한다.

$$\left(
\frac{\partial F}{\partial q_{12}},
\frac{\partial F}{\partial q_{13}},
\frac{\partial F}{\partial q_{14}},
\frac{\partial F}{\partial q_{23}},
\frac{\partial F}{\partial q_{24}},
\frac{\partial F}{\partial q_{34}}
\right)
=(q_{34},-q_{24},q_{23},q_{14},-q_{13},q_{12}).$$

이 여섯 값이 전부 0이면 $q$의 여섯 성분도 전부 0이다. 따라서 $q\neq0$인 곳에서는 $dF\neq0$이고, 복소 방정식 하나가 실제로 실수 자유도 두 개를 없앤다.

이제

$$N(q)=\sum_{i<j}|q_{ij}|^2$$

를 1로 제한한다. $F$가 2차 동차식이므로 $F(q)=0$이면 $F(tq)=t^2F(q)=0$이다. 즉 실수 반지름 방향 $q\mapsto tq$는 $F=0$ 원뿔 안에 있다. 그 방향에서

$$\frac d{dt}\Big|_{t=1}N(tq)=\frac d{dt}\Big|_{t=1}t^2N(q)=2N(q)\neq0$$

이므로 $N=1$이 자유도 하나를 더 없앤다. 그래서

$$\boxed{\ \Sigma^9:=\{q\in\mathbb C^6:F(q)=0,\ N(q)=1\}\ }$$

의 실차원은

$$12-2-1=9$$

가 된다.

### 2.2 차트의 플뤼커 벡터를 단위로 만든다

$q(Z)$의 노름제곱은

$$\begin{aligned}
K(Z)&=\|q(Z)\|^2\\
&=1+|a|^2+|b|^2+|c|^2+|d|^2+|ad-bc|^2.
\end{aligned}$$

따라서

$$\boxed{\ s(Z):=\frac{q(Z)}{\sqrt{K(Z)}}\in\Sigma^9\ }.$$

$F(s)=K^{-1}F(q)=0$이고 $N(s)=K^{-1}\|q\|^2=1$이다. 이 $s$가 $\mathbb{CP}^1$에서 썼던

$$\frac{(1,z)}{\sqrt{1+|z|^2}}$$

와 같은 역할을 한다. 아직 “같다”고 선언한 것이 아니라, 제약식 두 개에 직접 넣어 확인했다.

### 2.3 숫자가 들어간 평면 하나

$$a=1,\qquad b=0,\qquad c=0,\qquad d=i$$

를 넣는다. 그러면 $\Delta=i$이고

$$q=(1,0,i,-1,0,i),\qquad K=1+1+1+1=4.$$

단위 플뤼커 벡터는

$$p=s(Z)=\frac12(1,0,i,-1,0,i).$$

클라인 식을 숫자로 확인하면

$$F(p)=\frac12\frac i2-0+\frac i2\left(-\frac12\right)
=\frac i4-\frac i4=0,$$

노름은

$$N(p)=\frac14+\frac14+\frac14+\frac14=1.$$

이 점은 $S^{11}$ 위에 있을 뿐 아니라 $F=0$도 만족하므로 $\Sigma^9$ 위에 있다.

### 2.4 왜 $\Sigma^9$에서 위상 하나를 지우면 $\mathrm{Gr}(2,4)$인가

$p\in\Sigma^9$이면 $N(p)=1$이므로 여섯 성분 중 적어도 하나는 0이 아니다. 먼저 $p_{12}\neq0$인 경우를 실제로 복원한다. 전체를 $p_{12}$로 나누어

$$\widehat p_{ij}:=\frac{p_{ij}}{p_{12}},\qquad \widehat p_{12}=1$$

로 두고

$$c=\widehat p_{13},\qquad d=\widehat p_{14},\qquad
a=-\widehat p_{23},\qquad b=-\widehat p_{24}$$

라고 읽는다. 클라인 관계를 $p_{12}^2$로 나누면

$$\widehat p_{34}-\widehat p_{13}\widehat p_{24}
+\widehat p_{14}\widehat p_{23}=0.$$

방금 정한 $a,b,c,d$를 넣으면

$$\widehat p_{34}-c(-b)+d(-a)=0,$$

따라서

$$\widehat p_{34}=ad-bc.$$

그러므로

$$\widehat p=(1,c,d,-a,-b,ad-bc)$$

이고, §2에서 쓴 두 열

$$v=(1,0,a,b)^{\mathsf T},\qquad
w=(0,1,c,d)^{\mathsf T}$$

의 $v\wedge w$와 정확히 같다. $p_{12}=0$이면 0이 아닌 다른 $p_{ij}$를 1로 만드는 같은 계산을 한다. 따라서 $F=0$, $p\neq0$인 플뤼커 벡터의 비율 $[p]$는 2-평면 하나를 정한다.

이제

$$\pi:\Sigma^9\longrightarrow\mathrm{Gr}(2,4),\qquad
\pi(p)=[p]$$

라 두자. $\pi(p')=\pi(p)$이면 어떤 $\lambda\in\mathbb C^*$가 있어서 $p'=\lambda p$다. 두 벡터가 모두 단위이므로

$$1=N(p')=N(\lambda p)=|\lambda|^2N(p)=|\lambda|^2,$$

따라서 $|\lambda|=1$이고 $\lambda=e^{i\theta}$다. 역으로 $p'=e^{i\theta}p$이면 당연히 $[p']=[p]$이다. 그러므로 $\pi$의 한 fiber는 정확히

$$\{e^{i\theta}p:0\le\theta<2\pi\}$$

이고,

$$\boxed{\ \Sigma^9/S^1=\mathrm{Gr}(2,4)\ }$$

가 플뤼커 좌표에서 확인된다.

---

## §3. 위상회전이 $\Sigma^9$를 떠나지 않는지 먼저 확인한다

$S^{11}$의 위상회전

$$\rho_\theta(p)=e^{i\theta}p$$

를 $\Sigma^9$에 제한하고 싶다. 노름을 보존하는 것만으로는 부족하다. 클라인 조건 $F=0$도 보존해야 한다.

노름은

$$N(e^{i\theta}p)=\sum_{i<j}|e^{i\theta}p_{ij}|^2
=|e^{i\theta}|^2\sum_{i<j}|p_{ij}|^2=N(p).$$

$F$는 각 항이 성분 두 개의 곱이므로

$$\begin{aligned}
F(e^{i\theta}p)
&=(e^{i\theta}p_{12})(e^{i\theta}p_{34})
-(e^{i\theta}p_{13})(e^{i\theta}p_{24})
+(e^{i\theta}p_{14})(e^{i\theta}p_{23})\\
&=e^{2i\theta}F(p).
\end{aligned}$$

$F(p)=0$이면 $F(e^{i\theta}p)=0$이다. 따라서 위상곡선은 $S^{11}$만이 아니라 $\Sigma^9$ 안에 머문다.

이 식을 $\theta=0$에서 미분하면

$$dF_p(ip)=\frac d{d\theta}\Big|_0F(e^{i\theta}p)=2iF(p)=0$$

이다. 즉 $ip$가 클라인 제약의 접방향이라는 사실도 미분으로 확인된다.

### 3.1 여섯 복소성분의 생성원

각 $p_{ij}=x_{ij}+iy_{ij}$에 대해

$$e^{i\theta}p_{ij}
=(x_{ij}\cos\theta-y_{ij}\sin\theta)
+i(x_{ij}\sin\theta+y_{ij}\cos\theta).$$

$\theta=0$에서 미분하면 실수부 속도는 $-y_{ij}$, 허수부 속도는 $x_{ij}$다. 따라서

$$\boxed{
R=\sum_{1\le i<j\le4}
\left(-y_{ij}\frac\partial{\partial x_{ij}}
+x_{ij}\frac\partial{\partial y_{ij}}\right)
}$$

이다. 이 벡터장은 $R_p=ip$이고, §3의 두 계산 때문에 $\Sigma^9$에 접한다.

$\mathbb C^6$의 표준 1-형식을

$$\alpha=\sum_{i<j}(x_{ij}\,dy_{ij}-y_{ij}\,dx_{ij})$$

로 두고 $\Sigma^9$에 제한한다. 그러면

$$\begin{aligned}
\alpha(R)
&=\sum_{i<j}\left[x_{ij}\\,dy_{ij}(R)-y_{ij}\\,dx_{ij}(R)\right]\\
&=\sum_{i<j}\left[x_{ij}^2+y_{ij}^2\right]\\
&=N=1\qquad\text{on }\Sigma^9.
\end{aligned}$$

또한

$$d\alpha=2\sum_{i<j}dx_{ij}\wedge dy_{ij}$$

이고

$$\begin{aligned}
\iota_Rd\alpha
&=2\sum_{i<j}\left[dx_{ij}(R)dy_{ij}-dy_{ij}(R)dx_{ij}\right]\\
&=-2\sum_{i<j}\left[y_{ij}dy_{ij}+x_{ij}dx_{ij}\right]\\
&=-dN.
\end{aligned}$$

$\Sigma^9$ 안의 곡선 $p(t)$에서는 $N(p(t))=1$이므로 모든 $X=p'(0)\in T_p\Sigma^9$에 대해

$$dN(X)=\frac d{dt}\Big|_0N(p(t))=0.$$

따라서

$$\boxed{\ \alpha(R)=1,\qquad \iota_Rd\alpha=0\quad\text{on }\Sigma^9\ }.$$

두 번째 식에서 클라인 조건은 식의 마지막 소거에 직접 등장하지 않는다. 그러나 $R$과 시험벡터 $X$가 실제로 $\Sigma^9$의 접벡터인지 보장하는 데 이미 사용되었다. $F=0$ 보존을 확인하지 않고 $S^{11}$의 계산만 복사하면 이 지점이 비게 된다.

$d\alpha$가 몫공간의 2-형식이 되려면 Reeb 방향을 0으로 먹는 것만으로는 부족하고, 같은 원을 따라가도 값이 바뀌지 않아야 한다. 이것도 복소식에서 바로 확인된다. $\theta$를 고정한 위상회전 $\rho_\theta(p)=e^{i\theta}p$에 대해

$$\begin{aligned}
\rho_\theta^*\alpha
&=-i(e^{i\theta}p)^\dagger d(e^{i\theta}p)\\
&=-i(e^{-i\theta}p^\dagger)(e^{i\theta}dp)\\
&=-ip^\dagger dp=\alpha.
\end{aligned}$$

$\theta$는 이 pullback에서 고정된 군 매개변수이므로 $d(e^{i\theta})=0$이다. 한 번 더 미분하면

$$\rho_\theta^*(d\alpha)=d(\rho_\theta^*\alpha)=d\alpha.$$

따라서 $d\alpha$는 fiber 방향을 먹으면 0이고 fiber를 따라 값도 변하지 않는다. 이 두 계산으로 $\mathrm{Gr}(2,4)$ 위에 2-형식 $\Omega$가 존재하여

$$\boxed{\ \pi^*\Omega=d\alpha\ }$$

가 된다.

### 3.2 §2.3의 숫자점에서 $R$을 쓴다

$$p=\frac12(1,0,i,-1,0,i)$$

에서 0이 아닌 실좌표는

$$x_{12}=\frac12,\qquad y_{14}=\frac12,\qquad
x_{23}=-\frac12,\qquad y_{34}=\frac12.$$

따라서

$$R_p
=\frac12\partial_{y_{12}}
-\frac12\partial_{x_{14}}
-\frac12\partial_{y_{23}}
-\frac12\partial_{x_{34}}.$$

같은 점에서

$$\alpha_p
=\frac12dy_{12}-\frac12dx_{14}-\frac12dy_{23}-\frac12dx_{34}$$

이므로

$$\alpha_p(R_p)=\frac14+\frac14+\frac14+\frac14=1.$$

클라인 식도 속도방향으로 직접 미분하면

$$dF_p(R_p)=2iF(p)=0.$$

노름은

$$dN_p(R_p)=2\sum_{i<j}(x_{ij}dx_{ij}(R_p)+y_{ij}dy_{ij}(R_p))$$

인데 각 성분에서 $x(-y)+y(x)=0$이므로 0이다. $R_p$가 두 제약식 모두에 접한다.

---

## §4. 두 조건을 만족하는 후보가 정말 유일한가 — $p_0=e_{12}$에서 접촉성을 계산한다

Reeb 벡터장은 $\alpha(R)=1$, $\iota_Rd\alpha=0$을 만족하는 벡터장이다. 이 두 조건이 벡터를 하나로 못 박으려면 $d\alpha$가 $\ker\alpha$ 위에서 퇴화하지 않아야 한다. 이 조건을 “$\alpha$가 접촉형식이다”라고 부르지만, 여기서는 $p_0$에서 행렬처럼 확인한다.

$$p_0=(1,0,0,0,0,0)=e_{12}\in\Sigma^9$$

를 잡는다. $F$의 미분은

$$dF_{p_0}=dp_{34}$$

이다. 따라서 $F=0$의 접벡터 $X$는

$$\delta p_{34}=0$$

을 만족한다. 이것은 복소조건이므로 $\delta x_{34}=\delta y_{34}=0$ 두 개다.

$N=1$의 접조건은

$$dN_{p_0}(X)=2\delta x_{12}=0,$$

즉 $\delta x_{12}=0$이다. $\delta y_{12}$는 남는다. 따라서 $T_{p_0}\Sigma^9$의 아홉 실방향은

$$\partial_{y_{12}},$$

$$\partial_{x_{13}},\partial_{y_{13}},
\partial_{x_{14}},\partial_{y_{14}},
\partial_{x_{23}},\partial_{y_{23}},
\partial_{x_{24}},\partial_{y_{24}}$$

로 잡을 수 있다.

$p_0$에서

$$\alpha_{p_0}=dy_{12},$$

그러므로

$$R_{p_0}=\partial_{y_{12}},\qquad
\ker\alpha_{p_0}
=\operatorname{span}\{\partial_{x_I},\partial_{y_I}:I=13,14,23,24\}.$$

$d\alpha$를 이 접공간에 제한하면 $12$ 성분에서는 $dx_{12}=0$이고 $34$ 성분은 두 미분이 모두 0이므로

$$d\alpha\big|_{T_{p_0}\Sigma^9}
=2\sum_{I=13,14,23,24}dx_I\wedge dy_I.$$

각 두 방향에서 행렬은

$$2dx_I\wedge dy_I
\quad\longleftrightarrow\quad
\begin{pmatrix}0&2\\-2&0\end{pmatrix},$$

판별식은 $4$다. 네 블록이 있으므로 $\ker\alpha_{p_0}$ 위의 $d\alpha$는 역행렬을 갖는다. 쐐기곱으로 한 번에 쓰면

$$\begin{aligned}
\alpha\wedge(d\alpha)^4\big|_{p_0}
&=dy_{12}\wedge
\left(2\sum_{I=13,14,23,24}dx_I\wedge dy_I\right)^4\\
&=2^4\,4!\;dy_{12}\wedge
dx_{13}\wedge dy_{13}\wedge
dx_{14}\wedge dy_{14}\\
&\qquad\wedge dx_{23}\wedge dy_{23}\wedge
dx_{24}\wedge dy_{24},
\end{aligned}$$

이고 계수 $2^4\cdot4!=384$는 0이 아니다.

다른 점에서도 같은지 보려면 평면의 정규직교 기저 $v,w$를 $\mathbb C^4$의 정규직교 기저로 연장한다. 그 기저변환을 주는 $U\in U(4)$는 $e_1\wedge e_2$를 $v\wedge w$로 보낸다. $\Lambda^2U$는 $\mathbb C^6$의 유니터리 변환이므로 $p^\dagger p$와

$$\alpha=-i\,p^\dagger dp$$

를 보존한다. 따라서 $p_0$에서 0이 아니었던 $\alpha\wedge(d\alpha)^4$는 모든 점에서도 0이 아니다.

이제 $R$과 $R'$가 Reeb의 두 조건을 모두 만족한다고 하자. $D=R-R'$라 두면

$$\alpha(D)=0,\qquad \iota_Dd\alpha=0.$$

$D\in\ker\alpha$이고 $d\alpha$가 그 공간에서 역행렬을 가지므로 $D=0$이다. §3에서 만든 위상생성원은 단순한 후보가 아니라 유일한 Reeb 벡터장이다.

---

## §5. $U(2)$의 네 방향 중 왜 한 방향만 Reeb로 보이는가

$\mathrm{Gr}(2,4)$의 평면에 정규직교 기저를 골라

$$Q=(v\;w)\in\mathbb C^{4\times2},\qquad Q^\dagger Q=I_2$$

라 쓰자. 같은 평면의 다른 정규직교 기저는

$$Q'=QG,\qquad G\in U(2)$$

이다.

$G=(g_{rs})$라 하면 새 열은

$$v'=g_{11}v+g_{21}w,\qquad
w'=g_{12}v+g_{22}w.$$

쐐기곱을 전개하면

$$\begin{aligned}
v'\wedge w'
&=(g_{11}v+g_{21}w)\wedge(g_{12}v+g_{22}w)\\
&=g_{11}g_{12}v\wedge v+g_{11}g_{22}v\wedge w
+g_{21}g_{12}w\wedge v+g_{21}g_{22}w\wedge w\\
&=(g_{11}g_{22}-g_{21}g_{12})v\wedge w\\
&=(\det G)\,v\wedge w.
\end{aligned}$$

$v\wedge v=w\wedge w=0$, $w\wedge v=-v\wedge w$만 사용했다.

$G\in SU(2)$이면 $\det G=1$이므로 $v\wedge w$가 아예 움직이지 않는다. $U(2)$의 실 4방향 가운데 $SU(2)$의 실 3방향은

$$Q\longmapsto p=v\wedge w$$

를 만드는 순간 이미 사라진다.

반면

$$G(\theta)=\begin{pmatrix}e^{i\theta}&0\\0&1\end{pmatrix}$$

이면 $\det G(\theta)=e^{i\theta}$이므로

$$v'\wedge w'=e^{i\theta}p.$$

이 한 방향이 $\Sigma^9$에서 Reeb 원으로 남는다.

### 5.1 공통위상을 쓰면 속도가 두 배가 되는 지뢰

두 프레임 벡터에 같은 위상을 곱하면

$$Q\longmapsto e^{i\phi}Q,$$

$$v\wedge w\longmapsto(e^{i\phi}v)\wedge(e^{i\phi}w)
=e^{2i\phi}(v\wedge w).$$

따라서 프레임의 공통위상 $\phi$와 플뤼커 벡터의 Reeb 매개변수 $\theta$는

$$\theta=2\phi$$

관계다. $p\mapsto e^{i\theta}p$를 단위속도로 올리는 프레임 곡선은

$$Q(\theta)=Qe^{i\theta I_2/2}$$

이고 그 속도는

$$\dot Q(0)=Q\frac{i}{2}I_2=\frac i2Q.$$

$Q\mapsto e^{i\theta}Q$를 그대로 쓰면 플뤼커 공간에서는 $p\mapsto e^{2i\theta}p$가 되어 $\alpha$가 속도를 2로 읽는다.

### 5.2 $\alpha$를 프레임까지 당겨서 네 방향을 숫자로 읽는다

$p=v\wedge w$이고 $v,w$가 정규직교라 하자. 먼저

$$\|p\|^2
=\|v\wedge w\|^2
=\|v\|^2\|w\|^2-|\langle v,w\rangle|^2
=1$$

이므로 $p\in\Sigma^9$다. 미분하면

$$dp=dv\wedge w+v\wedge dw.$$

쐐기곱의 내적

$$\langle a\wedge b,c\wedge d\rangle
=\langle a,c\rangle\langle b,d\rangle
-\langle a,d\rangle\langle b,c\rangle$$

을 각 항에 적용한다:

$$\begin{aligned}
\langle v\wedge w,dv\wedge w\rangle
&=\langle v,dv\rangle\langle w,w\rangle
-\langle v,w\rangle\langle w,dv\rangle\\
&=\langle v,dv\rangle,
\end{aligned}$$

$$\begin{aligned}
\langle v\wedge w,v\wedge dw\rangle
&=\langle v,v\rangle\langle w,dw\rangle
-\langle v,dw\rangle\langle w,v\rangle\\
&=\langle w,dw\rangle.
\end{aligned}$$

따라서

$$p^\dagger dp=v^\dagger dv+w^\dagger dw
=\operatorname{tr}(Q^\dagger dQ).$$

$\alpha=-ip^\dagger dp$였으므로 프레임 공간으로 당긴 식은

$$\boxed{\ \widetilde\alpha=-i\operatorname{tr}(Q^\dagger dQ)\ }.$$

$U(2)$ 수직방향은 $\dot Q=QA$, $A\in\mathfrak u(2)$ 꼴이다. 넣으면

$$\widetilde\alpha_Q(QA)
=-i\operatorname{tr}(Q^\dagger QA)
=-i\operatorname{tr}(A).$$

$A\in\mathfrak{su}(2)$이면 $\operatorname{tr}A=0$이므로 $\widetilde\alpha(QA)=0$이다. 실제 세 생성원을

$$A_1=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
A_2=\begin{pmatrix}0&i\\i&0\end{pmatrix},\qquad
A_3=\begin{pmatrix}i&0\\0&-i\end{pmatrix}$$

로 잡으면 모두 trace가 0이다.

Reeb를 단위속도로 올리는 중앙 생성원은

$$A_0=\frac i2I_2$$

이고

$$\widetilde\alpha_Q(QA_0)
=-i\operatorname{tr}\left(\frac i2I_2\right)
=-i\left(\frac i2+\frac i2\right)=1.$$

그러므로

$$12\xrightarrow{\;SU(2)\text{ 세 방향 제거}\;}9
\xrightarrow{\;\text{Reeb 한 방향 제거}\;}8$$

이라는 차원계산은 단순한 군 차원 암기가 아니다. 같은 $\widetilde\alpha=-i\operatorname{tr}(Q^\dagger dQ)$가 trace 없는 세 방향을 0으로 읽고, trace 방향 하나를 1로 읽는 계산이다.

---

## §6. 국소 절단 $s=q/\sqrt K$에서 $\alpha$를 직접 당긴다

§2의 차트로 돌아간다:

$$q=(1,c,d,-a,-b,\Delta),\qquad \Delta=ad-bc,$$

$$K=q^\dagger q=1+|a|^2+|b|^2+|c|^2+|d|^2+|\Delta|^2,$$

$$s=K^{-1/2}q.$$

$f:=K^{-1/2}$라 쓰면 $f$는 실수 함수이고

$$ds=f\,dq+q\,df,\qquad d\bar s=f\,d\bar q+\bar q\,df.$$

$\alpha$의 각 성분에 넣는다:

$$\begin{aligned}
s_jd\bar s_j-\bar s_jds_j
&=fq_j(f\,d\bar q_j+\bar q_jdf)
-f\bar q_j(f\,dq_j+q_jdf)\\
&=f^2(q_jd\bar q_j-\bar q_jdq_j)
+f|q_j|^2df-f|q_j|^2df\\
&=\frac1K(q_jd\bar q_j-\bar q_jdq_j).
\end{aligned}$$

$df$가 들어간 두 항은 성분마다 정확히 없어진다. 여섯 성분을 더하면

$$\boxed{
A:=s^*\alpha
=\frac{i}{2K}\sum_{i<j}
\left(q_{ij}d\bar q_{ij}-\bar q_{ij}dq_{ij}\right)
}.$$

$q_{12}=1$은 미분이 0이다. $q_{23}=-a$, $q_{24}=-b$의 마이너스는 두 번 나타나 서로 없어진다. 따라서

$$\begin{aligned}
A=\frac{i}{2K}\big[&a\,\mathrm d\bar a-\bar a\,\mathrm da
+b\,\mathrm d\bar b-\bar b\,\mathrm db\\
&+c\,\mathrm d\bar c-\bar c\,\mathrm dc
+d\,\mathrm d\bar d-\bar d\,\mathrm d d\\
&+\Delta\,\mathrm d\bar\Delta-\bar\Delta\,\mathrm d\Delta\big].
\end{aligned}$$

마지막 미분도 생략하지 않으면

$$\mathrm d\Delta=d\,\mathrm da+a\,\mathrm d d-c\,\mathrm db-b\,\mathrm dc,$$

$$\mathrm d\bar\Delta
=\bar d\,\mathrm d\bar a+\bar a\,\mathrm d\bar d
-\bar c\,\mathrm d\bar b-\bar b\,\mathrm d\bar c.$$

이 식이 $\mathrm{Gr}(2,4)$ 차트 위의 local connection form이다.

### 6.1 왜 이 식이 $\log K$의 미분으로 접히는가

$q_{ij}$는 $a,b,c,d$의 정칙다항식이다. 그러므로 $\partial$는 $q$만 미분하고 $\bar\partial$는 $\bar q$만 미분한다:

$$\partial K
=\partial\sum_{i<j}q_{ij}\bar q_{ij}
=\sum_{i<j}\bar q_{ij}\\,dq_{ij},$$

$$\bar\partial K
=\sum_{i<j}q_{ij}\\,d\bar q_{ij}.$$

따라서 방금 전개한 분자는

$$\sum(q_{ij}d\bar q_{ij}-\bar q_{ij}dq_{ij})
=\bar\partial K-\partial K$$

이고

$$\boxed{\ A=\frac i2\frac{\bar\partial K-\partial K}{K}
=\frac i2(\bar\partial-\partial)\log K\ }.$$

이제 $d=\partial+\bar\partial$를 적용한다:

$$\begin{aligned}
dA
&=\frac i2(\partial+\bar\partial)(\bar\partial-\partial)\log K\\
&=\frac i2\left(\partial\bar\partial
-\partial^2+\bar\partial^2-\bar\partial\partial\right)\log K.
\end{aligned}$$

$\partial^2=\bar\partial^2=0$이고 함수에 대해

$$\bar\partial\partial=-\partial\bar\partial$$

이므로

$$dA=\frac i2\left(\partial\bar\partial+\partial\bar\partial\right)\log K
=\boxed{\ i\,\partial\bar\partial\log K\ }.$$

한편 걸음 6의 플뤼커 당김 계산은

$$\omega=\frac i2\partial\bar\partial\log K$$

였다. 따라서 같은 차트에서

$$\boxed{\ dA=2\omega\ }.$$

위층에서는 $A=s^*\alpha$이므로 $dA=s^*(d\alpha)$. 결국 Reeb 계산으로 내려온 형식과 플뤼커 퍼텐셜을 두 번 미분한 형식 사이의 상수는

$$s^*(d\alpha)=i\partial\bar\partial\log K
=2\left(\frac i2\partial\bar\partial\log K\right)$$

에서 직접 2로 정해진다. 대칭성 때문에 “어떤 상수배”라고 끝낼 필요가 없다.

### 6.2 수평 lift를 이 식으로 직접 만든다

차트의 접벡터 $H$를 $s$로 미분해 $ds(H)\in T_s\Sigma^9$로 올리면 일반적으로 수평일 필요는 없다. 그 벡터의 위상성분은

$$\alpha(ds(H))=(s^*\alpha)(H)=A(H).$$

따라서

$$\widetilde H:=ds(H)-A(H)R$$

라 두면

$$\alpha(\widetilde H)
=A(H)-A(H)\alpha(R)
=A(H)-A(H)=0.$$

$\mathbb{CP}^1$에서 $V-\alpha(V)R$로 했던 수평화가 $\mathrm{Gr}(2,4)$에서도 문자 그대로 같은 뺄셈으로 작동한다. 달라진 것은 $s$가 두 성분이 아니라 여섯 성분이고, $A$의 분자에 $\Delta=ad-bc$ 항이 생긴 것뿐이다.

---

## §7. $\mathrm{Gr}(2,4)$ 안의 $\mathbb{CP}^1$에서 앞 계산이 그대로 돌아오는가

차트에서

$$a=z,\qquad b=c=d=0$$

로 제한한다. 그러면 $\Delta=0$이고

$$q(z)=(1,0,0,-z,0,0),\qquad K=1+|z|^2.$$

국소 절단은

$$s(z)=\frac{(1,0,0,-z,0,0)}{\sqrt{1+|z|^2}}.$$

$\alpha$를 당긴 식 §6에 넣으면

$$A=\frac i2\frac{z\,d\bar z-\bar z\,dz}{1+|z|^2}.$$

$-z$의 마이너스가 두 번 나타나므로 CP¹ 식과 부호까지 같다. 다시 미분하면

$$dA=\frac{i\,dz\wedge d\bar z}{(1+|z|^2)^2},$$

$$\omega=\frac12dA
=\frac{i}{2}\frac{dz\wedge d\bar z}{(1+|z|^2)^2}.$$

따라서 이 $\mathbb{CP}^1\subset\mathrm{Gr}(2,4)$ 위에서

$$\int dA=2\pi,\qquad \int\omega=\pi.$$

걸음 6에서 $[\omega]=\pi\sigma_1$의 상수를 정할 때 사용한 생성 $\mathbb{CP}^1$이 바로 이 한 변수 제한으로 보인다.

### 7.1 두 변수가 살아 있는 대각 절단

이번에는

$$a=z,\qquad d=w,\qquad b=c=0$$

로 둔다. 그러면 $\Delta=zw$이고

$$q(z,w)=(1,0,w,-z,0,zw).$$

노름제곱은

$$\begin{aligned}
K&=1+|z|^2+|w|^2+|zw|^2\\
&=1+|z|^2+|w|^2+|z|^2|w|^2\\
&=(1+|z|^2)(1+|w|^2).
\end{aligned}$$

$A$의 분자에서 $zw$ 항을 먼저 편다:

$$\begin{aligned}
zw\\,d(\bar z\bar w)-\bar z\bar w\\,d(zw)
&=zw(\bar w\,d\bar z+\bar z\,d\bar w)
-\bar z\bar w(w\,dz+z\,dw)\\
&=|w|^2(z\,d\bar z-\bar z\,dz)
+|z|^2(w\,d\bar w-\bar w\,dw).
\end{aligned}$$

독립 성분 $-z$와 $w$에서 나온 항까지 더하면

$$\begin{aligned}
&z\,d\bar z-\bar z\,dz+w\,d\bar w-\bar w\,dw\\
&\quad+zw\\,d(\bar z\bar w)-\bar z\bar w\,d(zw)\\
&=(1+|w|^2)(z\,d\bar z-\bar z\,dz)
+(1+|z|^2)(w\,d\bar w-\bar w\,dw).
\end{aligned}$$

$K=(1+|z|^2)(1+|w|^2)$로 나누면

$$\boxed{
A=\frac i2\frac{z\,d\bar z-\bar z\,dz}{1+|z|^2}
+\frac i2\frac{w\,d\bar w-\bar w\,dw}{1+|w|^2}
}.$$

따라서

$$\boxed{
dA=i\frac{dz\wedge d\bar z}{(1+|z|^2)^2}
+i\frac{dw\wedge d\bar w}{(1+|w|^2)^2}
}.$$

$\Delta=zw$ 항을 버렸다면 분자에 필요한 $|w|^2$, $|z|^2$가 생기지 않아 이 분리가 나오지 않는다. 플뤼커의 마지막 성분은 장식이 아니라 두 변수의 정규화를 정확히 보정한다.

§2.3의 숫자점은 이 절단의 $(z,w)=(1,i)$다. 그 점의 $K$는

$$K=(1+1)(1+1)=4$$

이고, 그래서 $q/\sqrt K=\frac12(1,0,i,-1,0,i)$가 나왔다.

---

## §8. $dA$의 16성분을 미적분식으로 읽는다

$u=(a,b,c,d)$라 하고

$$\Delta=ad-bc,\qquad
K=1+|a|^2+|b|^2+|c|^2+|d|^2+|\Delta|^2$$

를 다시 쓴다. $\Delta$의 네 편미분은

$$\Delta_a=d,\qquad \Delta_b=-c,\qquad
\Delta_c=-b,\qquad \Delta_d=a.$$

따라서 $K$의 1계 편미분은

$$K_a=\bar a+d\bar\Delta,$$

$$K_b=\bar b-c\bar\Delta,$$

$$K_c=\bar c-b\bar\Delta,$$

$$K_d=\bar d+a\bar\Delta.$$

켤레 방향은

$$K_{\bar a}=a+\bar d\Delta,\qquad
K_{\bar b}=b-\bar c\Delta,$$

$$K_{\bar c}=c-\bar b\Delta,\qquad
K_{\bar d}=d+\bar a\Delta.$$

$$r:=\begin{pmatrix}d\\-c\\-b\\a\end{pmatrix}$$

라 두면 $\Delta_u=r_u$이고

$$K_{u\bar v}=\delta_{uv}+r_u\bar r_v.$$

행렬을 전부 쓰면

$$
(K_{u\bar v})=
\begin{pmatrix}
1+|d|^2&-d\bar c&-d\bar b&d\bar a\\
-c\bar d&1+|c|^2&c\bar b&-c\bar a\\
-b\bar d&b\bar c&1+|b|^2&-b\bar a\\
a\bar d&-a\bar c&-a\bar b&1+|a|^2
\end{pmatrix}.
$$

로그를 두 번 미분하면 몫의 미분으로

$$\boxed{
g_{u\bar v}:=\partial_u\partial_{\bar v}\log K
=\frac{K K_{u\bar v}-K_uK_{\bar v}}{K^2}
}.$$

§6에서 얻은 곡률은 바로

$$\boxed{
dA=i\sum_{u,v\in\{a,b,c,d\}}
g_{u\bar v}\\,du\wedge d\bar v,\qquad
\omega=\frac i2\sum_{u,v}g_{u\bar v}\\,du\wedge d\bar v
}.$$

대각성분 하나를 실제로 쓰면

$$g_{a\bar a}
=\frac{K(1+|d|^2)
-(\bar a+d\bar\Delta)(a+\bar d\Delta)}{K^2}.$$

교차성분 하나는 $K_{a\bar b}=-d\bar c$이므로

$$g_{a\bar b}
=\frac{-K d\bar c
-(\bar a+d\bar\Delta)(b-\bar c\Delta)}{K^2}.$$

원점 $a=b=c=d=0$에서는

$$K=1,\qquad K_u=0,\qquad K_{u\bar v}=\delta_{uv},$$

따라서

$$g_{u\bar v}(0)=\delta_{uv}.$$

이 값을 $dA$에 넣으면

$$dA\big|_0
=i(da\wedge d\bar a+db\wedge d\bar b
+dc\wedge d\bar c+dd\wedge d\bar d).$$

$a=x_a+iy_a$ 등에 대해 $i\,da\wedge d\bar a=2dx_a\wedge dy_a$이므로

$$dA\big|_0
=2(dx_a\wedge dy_a+dx_b\wedge dy_b
+dx_c\wedge dy_c+dx_d\wedge dy_d).$$

§4에서 $p_0$의 수평공간에 제한해 얻은

$$2\sum_{I=13,14,23,24}dx_I\wedge dy_I$$

와 같은 네 개의 표준 넓이 블록이다. 차트 변수와 플뤼커 접성분의 대응은

$$\delta q=(0,\delta c,\delta d,-\delta a,-\delta b,0)$$

이므로 단지 순서와 두 개의 부호가 바뀔 뿐이고, $dx\wedge dy$에서는 두 부호가 함께 바뀌어 그대로 남는다.

---

## §9. 차트를 바꾸면 $A$는 달라지고 $dA$는 그대로인지 계산한다

$p_{12}\neq0$ 차트에서는 비동차 플뤼커 벡터를

$$q^{(12)}=\frac p{p_{12}}$$

로 잡았고, 그 노름제곱을 $K^{(12)}$라 했다. $p_{13}\neq0$ 차트에서는

$$q^{(13)}=\frac p{p_{13}}.$$

두 차트가 겹치는 곳에서

$$c=\frac{p_{13}}{p_{12}}\neq0$$

이므로

$$q^{(13)}=\frac1c q^{(12)},\qquad
K^{(13)}=\frac1{|c|^2}K^{(12)}.$$

각 차트의 단위 절단은

$$s_{12}=\frac{q^{(12)}}{\sqrt{K^{(12)}}},\qquad
s_{13}=\frac{q^{(13)}}{\sqrt{K^{(13)}}}.$$

대입하면

$$s_{13}
=\frac{q^{(12)}/c}{\sqrt{K^{(12)}/|c|^2}}
=\frac{|c|}{c}s_{12}.$$

$c=|c|e^{i\vartheta}$라 쓰면

$$\boxed{\ s_{13}=e^{-i\vartheta}s_{12}\ }.$$

두 절단은 같은 $\mathrm{Gr}(2,4)$ 점을 고르지만 $\Sigma^9$의 같은 점을 고르지는 않는다. Reeb 원 위에서 $-\vartheta$만큼 떨어져 있다.

일반적으로 $s'=e^{i\chi}s$이면

$$d(e^{i\chi}s)=e^{i\chi}(i\,s\,d\chi+ds),$$

$$\begin{aligned}
(s')^\dagger ds'
&=e^{-i\chi}s^\dagger e^{i\chi}(i\,s\,d\chi+ds)\\
&=i(s^\dagger s)d\chi+s^\dagger ds\\
&=i\,d\chi+s^\dagger ds.
\end{aligned}$$

$A=-is^\dagger ds$이므로

$$A'=A+d\chi.$$

여기서는 $\chi=-\vartheta$이므로

$$\boxed{\ A_{13}=A_{12}-d\vartheta\ }.$$

한 번 더 미분하면

$$dA_{13}=dA_{12}-d(d\vartheta)=dA_{12}.$$

$A$가 차트마다 달라지는 양은 Reeb 원 위에서 절단을 얼마나 돌려 골랐는지를 기록한다. $dA$가 그 차이를 잊기 때문에 아래층 $\mathrm{Gr}(2,4)$의 전역 2-형식이 된다. 이 계산을 이름으로 부르면 $S^1\hookrightarrow\Sigma^9\to\mathrm{Gr}(2,4)$의 접속과 곡률이고, 이 특별한 원다발을 Boothby–Wang 다발이라고 한다.
