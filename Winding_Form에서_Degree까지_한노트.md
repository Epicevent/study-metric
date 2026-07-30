# 원을 세던 적분이 구면의 degree가 되기까지

## winding form 하나로 $T^2\to S^2$의 $1\leftrightarrow3$ fold를 끝까지 계산한다

이 노트의 출발점은 정의가 아니다. 논문의 실제 two-band map에서 target 점 하나를 찍는다.

$$
q(20^\circ)
=
(\sin20^\circ,0,-\cos20^\circ).
$$

이 점으로 오는 source 점은 세 개다. 각 점 주위의 작은 원을 map으로 보내고

$$
\vartheta
=
\frac{-Y\,dX+X\,dY}{X^2+Y^2}
$$

를 적분하면

$$
2\pi,\qquad 2\pi,\qquad -2\pi
$$

가 나온다. 합은 $2\pi$다. fold를 건넌 뒤에는 원상이 하나만 남고 그 원 하나에서
$2\pi$가 나온다.

$$
2\pi+2\pi-2\pi=2\pi.
$$

원상 수 $3$과 $1$은 다르지만 이 적분의 합은 같다. 이 변하지 않는 정수

$$
\frac1{2\pi}\sum\oint\vartheta
$$

가 이 노트에서 실제로 계산할 **degree**다.

---

## 이 노트에서 사실을 읽는 법

- **[논문]** Huang, *A Gauss-Bonnet Theorem for Quantum States*의 식 또는 주장.
- **[유도]** 논문의 map을 넣어 이 노트에서 전개한 계산.
- **[수치]** 독립 검산 스크립트가 계산한 값.
- **[대조]** 같은 winding form을 다른 map에 적용한 결과.

논문: [arXiv 2510.15760](https://arxiv.org/abs/2510.15760) ·
[HTML 원문](https://arxiv.org/html/2510.15760v1)

독립 검산:

$$
\texttt{python verify\_winding\_degree\_note.py}
$$

---

# 0. 규약을 한 번만 잠근다

## 0.1 세 공간

domain은

$$
T^2
=
\mathbb R^2/(2\pi\mathbb Z)^2,
\qquad
(k_x,k_y)\sim(k_x+2\pi m,k_y+2\pi n)
$$

이고 orientation은

$$
dk_x\wedge dk_y>0
$$

로 잡는다.

target은 outward orientation을 가진 단위구면 $S^2$다. 그러나 projector metric의
면적은 단위구면 면적의 절반으로 정규화한다. stereographic coordinate

$$
w=X+iY
$$

에서는

$$
\omega_{\mathrm{FS}}
=
\frac{2}{(1+X^2+Y^2)^2}\,dX\wedge dY,
\qquad
\int_{S^2}\omega_{\mathrm{FS}}=2\pi.
\tag{0.1}
$$

이 정규화에서 구면의 Gauss curvature는

$$
K_{S^2}=2.
\tag{0.2}
$$

## 0.2 논문의 실제 map

**[논문]** Hamiltonian의 $d$-vector와 lower-band Bloch map은

$$
d(k_x,k_y)
=
(\sin k_x,\sin k_y,1-\cos k_x-\cos k_y),
\tag{0.3}
$$

$$
F:T^2\longrightarrow S^2,
\qquad
F(k)=-\frac{d(k)}{|d(k)|}.
\tag{0.4}
$$

로 둔다. 이후 $F(k)=n(k)$라고도 쓴다.

## 0.3 오늘 적분할 1-form

평면의 원점을 뺀 곳에서

$$
\boxed{
\vartheta
=
\frac{-Y\,dX+X\,dY}{X^2+Y^2}
=d\arg(X+iY).
}
\tag{0.5}
$$

$\vartheta$는 target의 작은 원을 몇 번 도는지 읽는다. 이 form 하나가

$$
\text{작은 원의 winding}
\longrightarrow
\text{local degree}
\longrightarrow
\text{global degree}
\longrightarrow
\int_{T^2}F^*\omega_{\mathrm{FS}}
$$

로 변한다.

---

# 1. 먼저 원과 ellipse를 실제로 적분한다

## 1.1 $m$번 도는 원

$$
\gamma_m(t)
=
(R\cos mt,R\sin mt),
\qquad
0\le t\le2\pi.
$$

한 줄씩 대입하면

$$
X=R\cos mt,
\qquad
Y=R\sin mt,
$$

$$
dX=-Rm\sin mt\,dt,
\qquad
dY=Rm\cos mt\,dt.
$$

따라서

$$
\begin{aligned}
-Y\,dX+X\,dY
&=
-R\sin mt(-Rm\sin mt\,dt)\\
&\quad
+R\cos mt(Rm\cos mt\,dt)\\
&=
R^2m\,dt,
\end{aligned}
$$

$$
X^2+Y^2=R^2.
$$

그러므로

$$
\gamma_m^*\vartheta=m\,dt
$$

이고

$$
\boxed{
\oint_{\gamma_m}\vartheta
=
\int_0^{2\pi}m\,dt
=2\pi m.
}
\tag{1.1}
$$

반지름 $R$은 사라지고 감긴 횟수와 방향만 남는다.

## 1.2 작은 원이 ellipse가 되면

source의 작은 원

$$
h(t)=\varepsilon(\cos t,\sin t)
$$

에 real linear map

$$
L=
\begin{pmatrix}
a&0\\
0&b
\end{pmatrix}
$$

을 적용하면

$$
X=a\varepsilon\cos t,
\qquad
Y=b\varepsilon\sin t.
$$

이제 같은 form을 적분한다.

$$
dX=-a\varepsilon\sin t\,dt,
\qquad
dY=b\varepsilon\cos t\,dt,
$$

$$
\begin{aligned}
-Y\,dX+X\,dY
&=
ab\varepsilon^2
(\sin^2t+\cos^2t)\,dt\\
&=
ab\varepsilon^2\,dt,
\end{aligned}
$$

$$
X^2+Y^2
=
\varepsilon^2
(a^2\cos^2t+b^2\sin^2t).
$$

따라서

$$
\oint_{L\circ h}\vartheta
=
\int_0^{2\pi}
\frac{ab}
{a^2\cos^2t+b^2\sin^2t}\,dt.
\tag{1.2}
$$

각 사분면에서 $s=\tan t$를 넣으면

$$
\boxed{
\oint_{L\circ h}\vartheta
=
2\pi\,\operatorname{sgn}(ab)
=
2\pi\,\operatorname{sgn}\det L.
}
\tag{1.3}
$$

ellipse가 얼마나 길거나 납작한지는 사라진다. orientation을 보존했는지 뒤집었는지만
남는다.

---

# 2. 논문의 실제 target 점에서 세 winding을 계산한다

## 2.1 target 경로를 고른다

$$
q(\theta)
=
(\sin\theta,0,-\cos\theta),
\qquad
0<\theta<40^\circ.
\tag{2.1}
$$

$q(\theta)$에서 target tangent frame을

$$
t_1=(\cos\theta,0,\sin\theta),
\qquad
t_2=(0,-1,0)
\tag{2.2}
$$

로 잡는다. 실제로

$$
t_1\times t_2
=
(\sin\theta,0,-\cos\theta)
=q(\theta),
$$

이므로 $(t_1,t_2)$는 target orientation을 보존한다.

target 국소좌표는

$$
X=t_1\cdot(n-q),
\qquad
Y=t_2\cdot(n-q)
\tag{2.3}
$$

로 둔다.

## 2.2 원상 세 개를 근 공식으로 구한다

$q_y=0$이므로 원상은 $k_y=0$ 또는 $k_y=\pi$ 위에서 찾을 수 있다.

### Sheet $A$: $k_y=0$

$$
d(k_x,0)
=
(\sin k_x,0,-\cos k_x).
$$

따라서

$$
F(k_x,0)
=
(-\sin k_x,0,\cos k_x).
$$

$$
F(-\pi+\theta,0)
=
(\sin\theta,0,-\cos\theta)
=q(\theta).
$$

그러므로

$$
\boxed{
A(\theta)=(-\pi+\theta,0).
}
\tag{2.4}
$$

### Sheets $B,C$: $k_y=\pi$

$u=-k_x\in(0,\pi)$라 두면

$$
d(-u,\pi)
=
(-\sin u,0,2-\cos u).
$$

따라서 $F(-u,\pi)=q(\theta)$가 되려면 성분비가

$$
\frac{\sin u}{2-\cos u}
=
\tan\theta
\tag{2.5}
$$

를 만족해야 한다.

$$
t=\tan\frac u2
$$

를 넣으면

$$
\sin u=\frac{2t}{1+t^2},
\qquad
\cos u=\frac{1-t^2}{1+t^2}.
$$

그러므로

$$
\frac{\sin u}{2-\cos u}
=
\frac{2t}{1+3t^2}.
$$

$a=\tan\theta$라 두면

$$
3at^2-2t+a=0.
\tag{2.6}
$$

근은

$$
\boxed{
t_\pm
=
\frac{1\pm\sqrt{1-3a^2}}{3a},
\qquad
u_\pm=2\arctan t_\pm.
}
\tag{2.7}
$$

판별식

$$
1-3\tan^2\theta
$$

가 양수일 때 $B,C$ 두 sheet가 존재하고, $\theta=30^\circ$에서 둘이 붙으며,
$\theta>30^\circ$에서는 사라진다.

## 2.3 $\theta=20^\circ$에서 실제 숫자

**[수치]**

$$
q(20^\circ)
\approx
(0.342020,0,-0.939693).
$$

세 원상은

$$
\begin{aligned}
A&=(-2.79252680,0),\\
B&=(-0.40422136,\pi),\\
C&=(-2.03923959,\pi).
\end{aligned}
\tag{2.8}
$$

미분은 정규화된 벡터의 미분

$$
\boxed{
\partial_\mu n
=
-\frac{\partial_\mu d}{|d|}
+\frac{d(d\cdot\partial_\mu d)}{|d|^3}
}
\tag{2.9}
$$

로 계산한다. 여기서

$$
\partial_xd=(\cos k_x,0,\sin k_x),
\qquad
\partial_yd=(0,\cos k_y,\sin k_y).
$$

$(t_1,t_2)$ 성분으로 투영한 $2\times2$ Jacobian은

$$
J_i
=
\begin{pmatrix}
t_1\cdot\partial_xn&t_1\cdot\partial_yn\\
t_2\cdot\partial_xn&t_2\cdot\partial_yn
\end{pmatrix}_{k=k_i}.
\tag{2.10}
$$

실제 대입 결과는

$$
J_A=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\qquad
\det J_A=1,
\tag{2.11}
$$

$$
J_B\approx
\begin{pmatrix}
-0.634332&0\\
0&-0.869610
\end{pmatrix},
\qquad
\det J_B\approx0.551621,
\tag{2.12}
$$

$$
J_C\approx
\begin{pmatrix}
0.279606&0\\
0&-0.383314
\end{pmatrix},
\qquad
\det J_C\approx-0.107177.
\tag{2.13}
$$

각 source 원을

$$
k_i+\varepsilon(\cos t,\sin t)
$$

로 잡으면 target에서는 첫째 근사로 $J_i\varepsilon(\cos t,\sin t)$라는 ellipse가
된다. (1.3)을 그대로 적용하면

$$
\oint_{C_A}(\zeta\circ F)^*\vartheta=2\pi,
$$

$$
\oint_{C_B}(\zeta\circ F)^*\vartheta=2\pi,
$$

$$
\oint_{C_C}(\zeta\circ F)^*\vartheta=-2\pi.
$$

따라서

$$
\boxed{
\frac1{2\pi}
\sum_{i=A,B,C}
\oint_{C_i}(\zeta\circ F)^*\vartheta
=
\frac{2\pi+2\pi-2\pi}{2\pi}
=1.
}
\tag{2.14}
$$

여기서 처음으로 관찰을 말로 읽는다.

> 세 source sheet가 target의 같은 작은 원판을 덮지만, 하나는 반대 방향이다.
> 방향을 붙여 상쇄하면 target 원판 한 장만 남는다.

---

# 3. fold를 건너도 winding의 합은 왜 남는가

## 3.1 가장 작은 fold

$$
G(p,q)=(p,q^2)
\tag{3.1}
$$

를 잡고 target 점

$$
y=\left(2,\frac14\right)
$$

을 고른다. 원상은

$$
p_+=\left(2,\frac12\right),
\qquad
p_-=\left(2,-\frac12\right).
$$

target 중심좌표를

$$
X=p-2,
\qquad
Y=q^2-\frac14
$$

로 잡는다.

### $p_+$ 주위

$$
p=2+\varepsilon\cos t,
\qquad
q=\frac12+\varepsilon\sin t.
$$

그러면

$$
X=\varepsilon\cos t,
$$

$$
\begin{aligned}
Y
&=
\left(\frac12+\varepsilon\sin t\right)^2-\frac14\\
&=
\varepsilon\sin t+\varepsilon^2\sin^2t.
\end{aligned}
$$

$\varepsilon$이 작을 때 이 곡선은 반시계로 한 번 돈다.

$$
\frac1{2\pi}\oint_{C_+}G^*\vartheta=+1.
\tag{3.2}
$$

### $p_-$ 주위

$$
p=2+\varepsilon\cos t,
\qquad
q=-\frac12+\varepsilon\sin t.
$$

이번에는

$$
X=\varepsilon\cos t,
$$

$$
\begin{aligned}
Y
&=
\left(-\frac12+\varepsilon\sin t\right)^2-\frac14\\
&=
-\varepsilon\sin t+\varepsilon^2\sin^2t.
\end{aligned}
$$

시계 방향으로 한 번 돈다.

$$
\frac1{2\pi}\oint_{C_-}G^*\vartheta=-1.
\tag{3.3}
$$

둘의 합은

$$
(+1)+(-1)=0.
\tag{3.4}
$$

target의 $Y<0$ 쪽에는 원상이 없다. 따라서 fold를 건널 때

$$
0
\longleftrightarrow
(+1)+(-1)
$$

이 되고 signed winding의 합은 변하지 않는다.

## 3.2 논문의 $1\leftrightarrow3$

논문의 map에는 fold와 무관하게 계속 남아 있는 $A$ sheet가 있다.
fold를 건너면 $B,C$라는 $+/-$ 한 쌍이 더해지거나 사라진다.

$$
\underbrace{(+1)}_{A}
\longleftrightarrow
\underbrace{(+1)}_{A}
+\underbrace{(+1)+(-1)}_{B,C}.
\tag{3.5}
$$

그래서 원상 수는

$$
1\longleftrightarrow3
$$

으로 변하지만 winding의 합은

$$
1\longleftrightarrow1
$$

이다.

$\theta=35^\circ$에서는 원상이

$$
A(35^\circ)=(-2.53072742,0)
$$

하나뿐이고

$$
J_A=I_2.
$$

따라서

$$
\frac1{2\pi}\oint_{C_A}(\zeta\circ F)^*\vartheta=1.
\tag{3.6}
$$

(2.14)와 (3.6)은 같은 정수를 준다.

---

# 4. 이제 degree라는 이름을 붙인다

## 4.1 정체

닫힌 oriented surface 사이의 smooth map

$$
F:M\longrightarrow N
$$

에서 $M$ 전체의 orientation을 $F$로 밀어 보냈을 때 $N$의 orientation이 순수하게
$d$장 남는다면

$$
F_*[M]=d[N]
\tag{4.1}
$$

라고 쓴다. 이 정수 $d$가

$$
\boxed{\deg F}
$$

다.

이것이 degree의 정체다. regular target 하나의 원상을 세는 공식은 이 정수를 재는
방법이다.

## 4.2 winding form으로 재는 공식

regular target $y\in N$를 잡고 orientation-preserving target 좌표

$$
\zeta=X+iY,
\qquad
\zeta(y)=0
$$

를 잡는다. 원상들을

$$
F^{-1}(y)=\{p_1,\dots,p_r\}
$$

라 하고 각 $p_i$ 주위의 작은 반시계 원을 $C_i$라 하면

$$
\boxed{
\deg F
=
\frac1{2\pi}
\sum_{i=1}^r
\oint_{C_i}
(\zeta\circ F)^*\vartheta.
}
\tag{4.2}
$$

regular point에서는 작은 원이 ellipse로 가므로 (1.3)에 의해

$$
\frac1{2\pi}
\oint_{C_i}(\zeta\circ F)^*\vartheta
=
\operatorname{sgn}\det dF_{p_i}.
$$

따라서 익숙한 계산법

$$
\deg F
=
\sum_{p_i\in F^{-1}(y)}
\operatorname{sgn}\det dF_{p_i}
\tag{4.3}
$$

이 나온다.

(4.3)은 정의가 아니라 (4.2)의 ellipse 계산 결과다.

---

# 5. 구면 면적 적분이 winding 합으로 변하는 Stokes 계산

## 5.1 구면에서 원 하나를 준비한다

$$
r^2=X^2+Y^2
$$

라 두고

$$
\alpha
=
\frac{-Y\,dX+X\,dY}{1+r^2}
=
\frac{r^2}{1+r^2}\vartheta
\tag{5.1}
$$

를 잡는다.

polar coordinate에서

$$
-Y\,dX+X\,dY=r^2d\theta
$$

이므로

$$
\alpha=\frac{r^2}{1+r^2}d\theta.
$$

미분하면

$$
\begin{aligned}
d\alpha
&=
d\left(\frac{r^2}{1+r^2}\right)\wedge d\theta\\
&=
\frac{2r}{(1+r^2)^2}\,dr\wedge d\theta\\
&=
\frac{2}{(1+r^2)^2}\,dX\wedge dY\\
&=
\omega_{\mathrm{FS}}.
\end{aligned}
\tag{5.2}
$$

면적도 직접 확인한다.

$$
\begin{aligned}
\int_{S^2}\omega_{\mathrm{FS}}
&=
\int_0^{2\pi}\int_0^\infty
\frac{2r}{(1+r^2)^2}\,dr\,d\theta\\
&=
2\pi.
\end{aligned}
\tag{5.3}
$$

## 5.2 무한대 좌표에서 $\alpha$가 winding form이 된다

앞에서 고른 regular target $y$를 orientation-preserving 구면 회전으로 $\infty$에
보내도 winding과 degree는 변하지 않는다. 이제 빠진 target 점을 $\infty$라 하고 그
주위 좌표를

$$
\zeta=\frac1w=\rho e^{i\phi}
$$

로 둔다. 그러면

$$
r=\frac1\rho,
\qquad
\theta=-\phi.
$$

따라서

$$
\alpha
=
\frac{r^2}{1+r^2}d\theta
=
-\frac1{1+\rho^2}d\phi
\longrightarrow
-d\phi
=-\vartheta_\zeta.
\tag{5.4}
$$

## 5.3 source에 Stokes 정리를 적용한다

$\infty$의 원상 $p_i$ 주위에서 작은 원판 $D_i(\varepsilon)$를 빼고

$$
M_\varepsilon
=
M\setminus\bigcup_iD_i(\varepsilon)
$$

라 둔다. $C_i=\partial D_i$는 원판의 반시계 방향으로 잡는다. 그러면
구멍 난 $M_\varepsilon$의 boundary orientation은

$$
\partial M_\varepsilon=-\sum_iC_i
$$

다.

이제

$$
\begin{aligned}
\int_MF^*\omega_{\mathrm{FS}}
&=
\lim_{\varepsilon\to0}
\int_{M_\varepsilon}F^*(d\alpha)\\
&=
\lim_{\varepsilon\to0}
\int_{\partial M_\varepsilon}F^*\alpha\\
&=
-\lim_{\varepsilon\to0}
\sum_i\oint_{C_i}F^*\alpha.
\end{aligned}
$$

(5.4)를 넣으면

$$
\boxed{
\int_MF^*\omega_{\mathrm{FS}}
=
\sum_i
\oint_{C_i}
(\zeta\circ F)^*\vartheta.
}
\tag{5.5}
$$

두 개의 마이너스가 상쇄되었다.

- 첫 마이너스: 구멍의 boundary는 시계 방향이다.
- 둘째 마이너스: $\alpha\to-\vartheta_\zeta$다.

(4.2)와 합치면

$$
\boxed{
\int_MF^*\omega_{\mathrm{FS}}
=
2\pi\deg F.
}
\tag{5.6}
$$

따라서 winding 합, signed preimage 합, pullback area 적분은 세 계산이 아니라 같은
정수를 세 방식으로 읽은 것이다.

---

# 6. 논문의 two-band map에서 degree를 세 방식으로 맞춘다

## 6.1 원상 winding

(2.14)에서

$$
\deg F
=
\frac{2\pi+2\pi-2\pi}{2\pi}
=1.
\tag{6.1}
$$

## 6.2 signed density

**[유도]** 이 map에서

$$
N(k_x,k_y)
=
\cos k_x+\cos k_y-\cos k_x\cos k_y
\tag{6.2}
$$

라 두면

$$
\boxed{
\bar\lambda
=
\frac{N}
{2(3-2N)^{3/2}}.
}
\tag{6.3}
$$

그리고

$$
F^*\omega_{\mathrm{FS}}
=
\bar\lambda\,dk_x\wedge dk_y.
\tag{6.4}
$$

$\theta=20^\circ$의 세 원상에서

$$
N_A=1,
\qquad
N_B\approx0.838818,
\qquad
N_C\approx-1.902996.
$$

분모는 양수이므로

$$
\operatorname{sgn}\bar\lambda_A=+,
\qquad
\operatorname{sgn}\bar\lambda_B=+,
\qquad
\operatorname{sgn}\bar\lambda_C=-.
$$

이것은 세 winding의 $+,+,-$와 같다.

## 6.3 전체 적분

**[수치]**

$$
\int_{T^2}\bar\lambda\,dk_xdk_y
=
6.283185307179587
=2\pi.
\tag{6.5}
$$

따라서

$$
\frac1{2\pi}
\int_{T^2}F^*\omega_{\mathrm{FS}}
=1.
\tag{6.6}
$$

세 경로가 만난다.

$$
\boxed{
\underbrace{\frac1{2\pi}\sum_i\oint_{C_i}F^*\vartheta}_{\text{local winding}}
=
\underbrace{\sum_i\operatorname{sgn}\det dF_{p_i}}_{\text{signed preimages}}
=
\underbrace{\frac1{2\pi}\int_{T^2}F^*\omega_{\mathrm{FS}}}_{\text{signed area}}
=
\deg F
=1.
}
\tag{6.7}
$$

---

# 7. degree/Chern 계산과 singular-curvature 계산을 섞지 않는다

이 구별이 논문을 읽을 때 가장 중요하다.

## 7.1 signed 계산: degree가 이미 끝낸다

**[논문]** two-band map에서는 Berry curvature와 signed area density가

$$
\Omega=\bar\lambda
\tag{7.1}
$$

로 일치한다. 따라서 Chern number는

$$
C
=
\frac1{2\pi}
\int_{T^2}\Omega\,dk_xdk_y
=
\frac1{2\pi}
\int_{T^2}F^*\omega_{\mathrm{FS}}
=
\deg F.
\tag{7.2}
$$

regular locus에서 $K_G=2$이므로 논문의 식 (37)은

$$
\begin{aligned}
\frac1{4\pi}\int K_G\,d\bar A
&=
\frac1{4\pi}\int 2F^*\omega_{\mathrm{FS}}\\
&=
\frac1{2\pi}\int F^*\omega_{\mathrm{FS}}\\
&=
\deg F\\
&=
1.
\end{aligned}
\tag{7.3}
$$

이 식의 정수성은 지금 계산한 degree/winding에서 이미 나온다.

## 7.2 unsigned 계산: 여기서부터 논문의 새 도구가 필요하다

Riemannian area는 signed form이 아니라

$$
dA
=
|\bar\lambda|\,dk_xdk_y
\tag{7.4}
$$

다. 따라서 뒤집힌 $C$ sheet도 음수로 상쇄되지 않고 양의 면적으로 더해진다.

**[수치]**

$$
\int_{T^2}dA
=
1.1889492578\times2\pi,
$$

$$
\int_{T^2}K_G\,dA
=
2.3778985157\times2\pi.
\tag{7.5}
$$

이 값은 signed 적분 $4\pi$보다 크다. fold가 만든 $+/-$ 두 sheet가 signed 계산에서는
상쇄되지만 unsigned 면적에서는 두 장 모두 남기 때문이다.

논문의 singular curvature

$$
\kappa_s
$$

와 그 line integral은 바로 이 unsigned Gauss--Bonnet 장부를 맞추기 위해 등장한다.

$$
\boxed{
\begin{array}{c|c|c}
&\text{무엇을 센다}&\text{필요한 도구}\\ \hline
\int K_G\,d\bar A
&\text{방향을 가진 순수 겹수}
&\text{winding/degree}\\
\int K_G\,dA
&\text{접힌 모든 sheet의 실제 면적}
&\text{fold의 }\kappa_s\text{와 cusp}
\end{array}}
\tag{7.6}
$$

degree는 논문의 singular-curvature 계산을 대체하지 않는다. 둘은 서로 다른 질문에
답한다.

---

# 8. cusp에서도 degree가 보는 것과 보지 않는 것

논문의 cusp 근처에서 target 경로를 움직이면 원상이

$$
1\leftrightarrow3\leftrightarrow1
$$

로 바뀐다.

**[수치]** cusp tangent coordinate에서 $A=0.04$를 고정하고 $B$를 움직인 결과:

$$
\begin{array}{c|c|c}
B&\text{원상 수}&\text{orientation signs}\\ \hline
-0.006&1&+\\
-0.005&3&+,-,+\\
0&3&+,-,+\\
+0.005&3&+,-,+\\
+0.006&1&+
\end{array}
\tag{8.1}
$$

모든 줄에서 signed sum은

$$
1
$$

이다. 따라서 degree는 cusp를 지나도 변하지 않는다.

하지만 degree는 다음을 기록하지 않는다.

- 어느 두 root가 fold에서 함께 태어났는가.
- 세 root의 sheet ID가 cusp 주변에서 어떻게 이어지는가.
- unsigned area가 얼마나 중복되었는가.
- singular curvature가 cusp에 접근하며 어떻게 발산하는가.

그래서 논문의 fold/cusp 계산에는 root count가 아니라 root continuation과 sheet
provenance가 추가로 필요하다. degree는 그 trace가 보존해야 할 가장 거친 전역 정수다.

---

# 9. Weierstrass는 마지막 대조군이다

이 절은 논문의 fold를 설명하기 위한 주 예시가 아니다. 같은 $T^2\to S^2$라도
singularity 종류가 다르면 winding이 어떻게 보이는지 확인하는 대조군이다.

정사각 격자 $\Lambda$에 대해

$$
F_\wp:\mathbb C/\Lambda\longrightarrow\mathbb{CP}^1,
\qquad
F_\wp([z])=[\wp(z):1]
\tag{9.1}
$$

를 잡는다. target의 $\infty$ 근처 좌표를

$$
\zeta=\frac1w
$$

로 잡으면 source의 $z=0$ 근처에서

$$
\zeta\circ F_\wp(z)
=
\frac1{\wp(z)}
=
z^2+O(z^6).
\tag{9.2}
$$

source의 작은 원

$$
z(t)=\varepsilon e^{it}
$$

을 넣으면

$$
\zeta\circ F_\wp(z(t))
=
\varepsilon^2e^{2it}+O(\varepsilon^6).
$$

따라서

$$
\begin{aligned}
\oint(\zeta\circ F_\wp)^*\vartheta
&=
\int_0^{2\pi}d\arg(e^{2it})\\
&=
\int_0^{2\pi}2\,dt\\
&=
4\pi.
\end{aligned}
\tag{9.3}
$$

그러므로

$$
\boxed{
\deg F_\wp
=
\frac{4\pi}{2\pi}
=2.
}
\tag{9.4}
$$

논문의 fold에서는 두 원상이 $+/-$ 한 쌍으로 태어난다. Weierstrass branch에서는
한 source 점 주위의 원이 target을 두 번 같은 방향으로 돈다.

$$
\boxed{
\begin{array}{c|c|c}
&\text{local model}&\text{winding}\\ \hline
\text{fold}
&(p,q)\mapsto(p,q^2)
&(+1)+(-1)=0\\
\text{branch}
&z\mapsto z^2
&+2
\end{array}}
\tag{9.5}
$$

이 차이 때문에 fold singular set은 곡선이고, holomorphic branch set은 고립점이다.

---

# 10. 곡률 계산은 degree 위에 어떻게 얹히는가

구면 metric을

$$
g_{S^2}
=
e^{2v(w)}|dw|^2,
\qquad
e^{2v(w)}
=
\frac{2}{(1+|w|^2)^2}
$$

라고 쓰면

$$
-e^{-2v}\Delta_wv=2.
$$

holomorphic regular point에서 $w=F_\wp(z)$를 넣으면

$$
g=F_\wp^*g_{S^2}=e^{2u(z)}|dz|^2,
\qquad
u=v(\wp(z))+\log|\wp'(z)|.
$$

$\wp'\ne0$인 곳에서는

$$
\Delta\log|\wp'|=0
$$

이고 chain rule은

$$
\Delta_z(v\circ\wp)
=
|\wp'|^2(\Delta_wv)\circ\wp
$$

를 준다. 따라서

$$
\boxed{
K_g=-e^{-2u}\Delta_zu=2
}
\tag{10.1}
$$

다.

branch point에서는 $u=\log r+s$이고 작은 원의 geodesic-curvature 적분이

$$
\kappa_g\,ds
=
(1+ru_r)d\theta
$$

인데

$$
ru_r=1+O(r^2)
$$

이므로

$$
\begin{aligned}
\oint\kappa_g\,ds
&=
\int_0^{2\pi}(1+ru_r)d\theta\\
&\longrightarrow
\int_0^{2\pi}2\,d\theta\\
&=
4\pi
\end{aligned}
$$

로 간다. 평범한 점의 $2\pi$보다 $2\pi$ 많으므로 point defect는

$$
2\pi-4\pi=-2\pi
$$

다. 이것은 fold 곡선의 $\kappa_s$가 아니라 branch point의 atomic correction이다.

따라서 두 층을 분리한다.

$$
\boxed{
\begin{array}{c|c}
\text{degree/winding}
&\text{map이 target을 순수하게 몇 번 덮는가}\\
\text{singular curvature}
&\text{퇴화 metric의 Gauss--Bonnet 장부를 어떻게 닫는가}
\end{array}}
\tag{10.2}
$$

---

# 11. 하루 손계산 순서

아래 문제는 앞의 풀이를 덮고 다시 계산한다.

## 문제

1. $\gamma_{-2}(t)=(3\cos2t,-3\sin2t)$에 $\vartheta$를 넣어
   $-4\pi$를 얻어라.
2. ellipse $X=2\cos t$, $Y=-3\sin t$에 $\vartheta$를 적분해
   $-2\pi$를 얻어라.
3. $\alpha=(-YdX+XdY)/(1+X^2+Y^2)$를 직접 미분하여
   $d\alpha=\omega_{\mathrm{FS}}$를 얻어라.
4. $\theta=20^\circ$에서 (2.7)의 두 근을 계산하여 $B,C$의 $k_x$를 재현하라.
5. (2.9)를 사용하여 $J_A=I_2$를 직접 확인하라.
6. $J_B,J_C$의 대각성분을 계산하고 (1.2)에 넣어 각각 $+2\pi,-2\pi$를 얻어라.
7. $\theta=35^\circ$에서 판별식이 음수임을 확인하고 $A$ winding 하나만 남음을 보여라.
8. toy fold의 두 원상에서 $Y$의 1차항 부호가 반대임을 다시 계산하라.
9. (5.1)--(5.5)의 두 마이너스가 어디서 생기고 어디서 상쇄되는지 한 줄씩 적어라.
10. $\zeta\circ F_\wp(z)=z^2+O(z^6)$에 $z=\varepsilon e^{it}$를 넣어
    winding $2$를 재현하라.

## 숫자 검산표

$$
\begin{array}{c|c}
\text{항목}&\text{답}\\ \hline
\tan20^\circ&0.3639702343\\
\sqrt{1-3\tan^220^\circ}&0.7767300462\\
k_{x,B}&-0.40422135795\\
k_{x,C}&-2.03923959484\\
\det J_A&1\\
\det J_B&0.55162122557\\
\det J_C&-0.10717678113\\
\int_{T^2}F^*\omega_{\mathrm{FS}}&2\pi\\
\deg F&1\\
\deg F_\wp&2
\end{array}
$$

---

# 12. 마지막 연결

이 노트에서 새로 등장한 적분은 없다.

$$
\oint\vartheta
$$

를

$$
\text{한 원의 감김}
$$

으로 읽고,

$$
\sum_i\oint F^*\vartheta
$$

를

$$
\text{모든 source sheet의 signed 감김}
$$

으로 읽고,

$$
\int_{T^2}F^*\omega_{\mathrm{FS}}
$$

를 Stokes 정리로 같은 boundary winding 합으로 바꾸었다.

따라서

$$
\boxed{
\text{winding form}
\Longrightarrow
\text{local orientation}
\Longrightarrow
\text{degree}
\Longrightarrow
\text{signed area}
\Longrightarrow
\text{Chern number}.
}
$$

논문의 $1\leftrightarrow3$ fold는 이 사슬을 깨지 않는다. fold가 추가하는 두 sheet의
winding이 $+1$과 $-1$이어서 서로 지워지기 때문이다. 논문의 singular curvature는
이 signed 사슬이 아니라, 지워지지 않고 실제 면적으로 남는 두 sheet의 **unsigned**
Gauss--Bonnet 장부를 다룬다.
