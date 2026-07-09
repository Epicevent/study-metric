# $S^2\subset\mathbb R^3$ 에서 가우스–보넷까지 — 한 벌 완결 노트

구면에서 출발해서, 복소수를 만들고, 점을 행렬로 옮기고, 행렬 집합 위에서 $\displaystyle\int K\,dA=4\pi$ 까지 간다. **읽는 데 필요한 것은 전부 이 안에서 만든다.** 밖에서 받아들이는 정리는 하나 — Part1에서 임베딩으로 유도해 둔 곡률 공식

$$ds^2=\lambda\,(dx^2+dy^2)\ \text{일 때}\quad K=-\frac1{2\lambda}\Delta\log\lambda$$

— 뿐이다.

---

## 0. 무대: $S^2\subset\mathbb R^3$ 와 입체사영

단위구면 $S^2=\{n_1^2+n_2^2+n_3^2=1\}\subset\mathbb R^3$. 좌표 원점을 북극에 두고 싶으니 **남극** $(0,0,-1)$ 에서 평면점 $(x,y,0)$ 으로 직선을 쏜다:

$$(0,0,-1)+t\,(x,y,1)=(tx,\ ty,\ t-1).$$

이 점이 구면 위에 있을 조건 ($s:=x^2+y^2$ 로 적는다):

$$t^2x^2+t^2y^2+(t-1)^2=1
\ \Longrightarrow\ t^2s+t^2-2t+1=1
\ \Longrightarrow\ t^2(s+1)=2t
\ \Longrightarrow\ t=\frac2{s+1}.$$

$S:=1+s$ 로 쓰면 $t=\tfrac2S$ 이고, 교점은

$$\vec n(x,y)=\Big(\frac{2x}S,\ \frac{2y}S,\ \frac2S-1\Big)=\Big(\frac{2x}S,\ \frac{2y}S,\ \frac{1-s}S\Big)
\qquad\big((x,y)=(0,0)\mapsto(0,0,1)\ \text{북극}\big).$$

검산 — 구면 위인가:

$$\lvert\vec n\rvert^2=\frac{4x^2+4y^2+(1-s)^2}{S^2}=\frac{4s+1-2s+s^2}{S^2}=\frac{(1+s)^2}{S^2}=1\ \checkmark$$

평면 $(x,y)$ 전체가 구면에서 남극 한 점만 빼고 전부를 덮는다.

---

## 1. $\mathbb R^3$ 에서 계량 재기 — 제1기본형식

곡면 위 길이는 $\mathbb R^3$ 유클리드 내적으로 잰다: $ds^2=\lvert d\vec n\rvert^2=\langle\vec n_x,\vec n_x\rangle dx^2+2\langle\vec n_x,\vec n_y\rangle dx\,dy+\langle\vec n_y,\vec n_y\rangle dy^2$. 성분부터 몫미분한다. $S_x=2x$, $S_y=2y$ 이고

$$\partial_x\frac{2x}S=\frac{2S-2x\cdot2x}{S^2}=\frac{2S-4x^2}{S^2},\qquad
\partial_x\frac{2y}S=\frac{0-2y\cdot2x}{S^2}=\frac{-4xy}{S^2},$$

$$\partial_x\frac{1-s}S=\frac{(-2x)S-(1-s)(2x)}{S^2}=\frac{-2x\,[S+1-s]}{S^2}=\frac{-4x}{S^2}
\qquad(S+1-s=1+s+1-s=2),$$

$$\vec n_x=\frac1{S^2}\big(2S-4x^2,\ -4xy,\ -4x\big),\qquad
\vec n_y=\frac1{S^2}\big(-4xy,\ 2S-4y^2,\ -4y\big)\ (x\leftrightarrow y\ \text{대칭}).$$

**$E=\langle\vec n_x,\vec n_x\rangle$ — 전부 전개한다** (분모 $S^4$ 잠시 생략):

$$(2S-4x^2)^2+(-4xy)^2+(-4x)^2
=4S^2-16x^2S+16x^4+16x^2y^2+16x^2$$

$$=4S^2-16x^2S+16x^2\underbrace{(x^2+y^2+1)}_{=S}
=4S^2-16x^2S+16x^2S=4S^2
\qquad\Longrightarrow\qquad E=\frac{4S^2}{S^4}=\frac4{S^2}.$$

$G$ 는 대칭으로 같다. **$F=\langle\vec n_x,\vec n_y\rangle$:**

$$(2S-4x^2)(-4xy)+(-4xy)(2S-4y^2)+(-4x)(-4y)
=-8xyS+16x^3y-8xyS+16xy^3+16xy$$

$$=8xy\,\big[-2S+2x^2+2y^2+2\big]=8xy\,\big[-2S+2s+2\big]=8xy\cdot0=0.$$

$$\therefore\qquad \boxed{\ ds^2=\frac4{S^2}\,(dx^2+dy^2)\ }\qquad
\lambda_{\text{라운드}}=\frac4{S^2}.$$

등온($E=G$, $F=0$)이다 — 왜 하필 등온인지는 §3에서 복소 계산이 답해준다.

---

## 2. 복소수 도구 만들기

$z:=x+iy$, $\bar z=x-iy$ 라 두면 $z\bar z=x^2+y^2=s$, 곧 $S=1+z\bar z$. 그리고

$$dz=dx+i\,dy,\qquad d\bar z=dx-i\,dy
\qquad\Longrightarrow\qquad
dx=\frac{dz+d\bar z}2,\qquad dy=\frac{dz-d\bar z}{2i}.$$

함수 $f=u(x,y)+iv(x,y)$ 의 전미분에 대입한다:

$$df=f_x\,dx+f_y\,dy
=f_x\,\frac{dz+d\bar z}2+f_y\,\frac{dz-d\bar z}{2i}
=\underbrace{\tfrac12\big(f_x-if_y\big)}_{=:\ \partial_zf}\,dz
+\underbrace{\tfrac12\big(f_x+if_y\big)}_{=:\ \partial_{\bar z}f}\,d\bar z.$$

계수가 나온 뒤에야 이름을 붙였다. 바로 확인:

$$\partial_zz=\tfrac12(1-i\cdot i)=1,\qquad \partial_z\bar z=\tfrac12(1+i\cdot i)=0
\quad(\text{켤레는 반대}),$$

$$\partial_zS=\partial_z(1+z\bar z)=\bar z,\qquad \partial_{\bar z}S=z,\qquad S-z\bar z=1,$$

$$\lvert dz\rvert^2=dz\,d\bar z=(dx+idy)(dx-idy)=dx^2+dy^2.$$

라플라시안도 옮겨 둔다. $\partial_z+\partial_{\bar z}=\partial_x$, $i(\partial_z-\partial_{\bar z})=\partial_y$ 에서

$$\Delta=\partial_x^2+\partial_y^2
=(\partial_z+\partial_{\bar z})^2+i^2(\partial_z-\partial_{\bar z})^2
=\big[\partial_z^2+2\partial_z\partial_{\bar z}+\partial_{\bar z}^2\big]-\big[\partial_z^2-2\partial_z\partial_{\bar z}+\partial_{\bar z}^2\big]
=4\,\partial_z\partial_{\bar z}.$$

이 절의 밑재료 세 줄 — $\partial_zS=\bar z$, $\partial_{\bar z}S=z$, $S-s=1$ — 이 이후 모든 몫미분에 쓰인다.

---

## 3. 같은 계량을 복소로 — $\mathbb C\times\mathbb R$ 묶음

§0의 $\vec n$ 을 $(\nu,\,n_3)=\big(\tfrac{2z}S,\ \tfrac{1-s}S\big)\in\mathbb C\times\mathbb R$ 로 묶고 **묶은 채로** 미분한다 ($\nu=n_1+in_2=\tfrac{2x+2iy}S=\tfrac{2z}S$). 몫미분 네 번:

$$\partial_z\nu=\frac{2\cdot S-2z\cdot\partial_zS}{S^2}=\frac{2S-2z\bar z}{S^2}=\frac{2(S-s)}{S^2}=\frac2{S^2},\qquad
\partial_{\bar z}\nu=\frac{0-2z\cdot\partial_{\bar z}S}{S^2}=-\frac{2z^2}{S^2},$$

$$\partial_zn_3=\frac{(-\bar z)S-(1-s)\bar z}{S^2}=\frac{-\bar z[S+1-s]}{S^2}=-\frac{2\bar z}{S^2},\qquad
\partial_{\bar z}n_3=\overline{\partial_zn_3}=-\frac{2z}{S^2}\ (n_3\ \text{실}).$$

전미분을 조립한다:

$$d\nu=\frac2{S^2}\,dz-\frac{2z^2}{S^2}\,d\bar z,\qquad
dn_3=-\frac{2\bar z}{S^2}\,dz-\frac{2z}{S^2}\,d\bar z.$$

$\mathbb C\times\mathbb R$ 의 제곱길이는 $ds^2=\lvert d\nu\rvert^2+dn_3^2$ ($dn_1^2+dn_2^2=\lvert d\nu\rvert^2$ 은 $\nu=n_1+in_2$ 의 절댓값 전개 그대로). 먼저 $\lvert d\nu\rvert^2=d\nu\cdot\overline{d\nu}$, $\overline{d\nu}=\tfrac2{S^2}d\bar z-\tfrac{2\bar z^2}{S^2}dz$:

$$\lvert d\nu\rvert^2
=-\frac{4\bar z^2}{S^4}\,dz^2+\frac{4+4s^2}{S^4}\,dz\,d\bar z-\frac{4z^2}{S^4}\,d\bar z^2
\qquad(z^2\bar z^2=s^2).$$

다음 $dn_3^2$ (실 1-형식의 제곱):

$$dn_3^2=\frac{4\bar z^2}{S^4}\,dz^2+\frac{8s}{S^4}\,dz\,d\bar z+\frac{4z^2}{S^4}\,d\bar z^2.$$

더하면 $dz^2$ 계수 $-\tfrac{4\bar z^2}{S^4}+\tfrac{4\bar z^2}{S^4}=0$, $d\bar z^2$ 계수도 켤레라 $0$, 혼합 계수는

$$\frac{4+4s^2+8s}{S^4}=\frac{4(1+s)^2}{S^4}=\frac4{S^2}
\qquad\Longrightarrow\qquad
\lvert d\vec n\rvert^2=\frac4{S^2}\,\lvert dz\rvert^2\ \checkmark$$

— §1의 실좌표 계산과 같은 값. 그리고 §1의 의문이 풀린다: $dz^2,d\bar z^2$ 항이 $\lvert d\nu\rvert^2$ 와 $dn_3^2$ 사이에서 **상쇄**되는 것 — 이것이 "$E=G$, $F=0$(등온)"의 정체다.

---

## 4. 점을 행렬로

### (4a) 파울리 행렬 — 도구

$$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

직접 곱한다: $\sigma_a^2=I$ (각각 대입), $\sigma_1\sigma_2=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\left(\begin{smallmatrix}0&-i\\ i&0\end{smallmatrix}\right)=\left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right)$ (순환 동일, 순서 바꾸면 부호 반대). 대각합: $\operatorname{tr}I=2$, $\operatorname{tr}\left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right)=0$, 곧

$$\operatorname{tr}(\sigma_a\sigma_b)=2\delta_{ab}
\qquad\Longrightarrow\qquad
\operatorname{tr}\big[(\vec a\cdot\vec\sigma)(\vec b\cdot\vec\sigma)\big]=\sum_{a,b}a_ab_b\operatorname{tr}(\sigma_a\sigma_b)=2\,\vec a\cdot\vec b$$

— $\mathbb R^3$ 내적이 $\tfrac12\operatorname{tr}$ 로 행렬 세계에 그대로 복사된다. 표기: $\vec a\cdot\vec\sigma=\left(\begin{smallmatrix}a_3&a_1-ia_2\\ a_1+ia_2&-a_3\end{smallmatrix}\right)$.

### (4b) 사영자 — 점의 행렬화

$[z_1:z_2]$ 에 (비율만 의미 있는 두 복소수 쌍) 행렬을 대응시킨다: 대표 $v=(z_1,z_2)$ 를 잡아

$$P=\frac{vv^*}{\lVert v\rVert^2}.$$

$v\mapsto\mu v$ 에 분자 $\lvert\mu\rvert^2vv^*$, 분모 $\lvert\mu\rvert^2\lVert v\rVert^2$ — $P$ 불변. 차트 $v=(1,z)$ 에서 $\lVert v\rVert^2=1+z\bar z=S$ 이고

$$vv^*=\binom1z\begin{pmatrix}1&\bar z\end{pmatrix}=\begin{pmatrix}1&\bar z\\ z&s\end{pmatrix}
\qquad\Longrightarrow\qquad
P(z)=\frac1S\begin{pmatrix}1&\bar z\\ z&s\end{pmatrix}.$$

자격 확인 셋:

$$\operatorname{tr}P=\frac{1+s}S=1,\qquad
P^2=\frac{v\,(v^*v)\,v^*}{S^2}=\frac{v\cdot S\cdot v^*}{S^2}=P,\qquad
Pv=\frac{v(v^*v)}S=v.$$

파울리로 분해한다. $\tfrac12\operatorname{tr}P=\tfrac12$ 을 떼면 성분마다

$$\tfrac1S-\tfrac12=\frac{2-S}{2S}=\frac{1-s}{2S},\qquad \tfrac sS-\tfrac12=\frac{s-1}{2S},$$

$$P-\tfrac12I=\frac1{2S}\begin{pmatrix}1-s&2\bar z\\ 2z&s-1\end{pmatrix}=\tfrac12\,\vec n\cdot\vec\sigma,
\qquad
\vec n=\Big(\frac{2x}S,\ \frac{2y}S,\ \frac{1-s}S\Big)$$

— **§0의 입체사영 그 점이다.** 점의 세 얼굴이 묶였다:

$$[1:z]\ \longleftrightarrow\ \vec n(z)\in S^2\ \longleftrightarrow\ P(z)=\tfrac12\big(I+\vec n\cdot\vec\sigma\big).$$

### (4c) 행렬을 미분한다

$P$ 의 네 성분을 §2 규칙으로 각각 몫미분:

$$\partial_z\frac1S=-\frac{\bar z}{S^2},\qquad
\partial_z\frac{\bar z}S=-\frac{\bar z^2}{S^2},\qquad
\partial_z\frac zS=\frac{S-z\bar z}{S^2}=\frac1{S^2},\qquad
\partial_z\frac sS=\partial_z\Big(1-\frac1S\Big)=+\frac{\bar z}{S^2},$$

$$\partial_zP=\frac1{S^2}\begin{pmatrix}-\bar z&-\bar z^2\\ 1&\bar z\end{pmatrix},\qquad
\partial_{\bar z}P=\partial_{\bar z}(P^\dagger)=(\partial_zP)^\dagger=\frac1{S^2}\begin{pmatrix}-z&1\\ -z^2&z\end{pmatrix}\ (P\ \text{에르미트}).$$

곱을 **네 성분 전부** 적는다 (분모 $S^4$ 잠시 생략). $(\partial_zP)^2$:

$$\begin{pmatrix}-\bar z&-\bar z^2\\ 1&\bar z\end{pmatrix}\begin{pmatrix}-\bar z&-\bar z^2\\ 1&\bar z\end{pmatrix}
=\begin{pmatrix}\bar z^2-\bar z^2&\bar z^3-\bar z^3\\ -\bar z+\bar z&-\bar z^2+\bar z^2\end{pmatrix}
=\begin{pmatrix}0&0\\0&0\end{pmatrix}$$

— **행렬째 $0$** (멱영). §3의 "$dz^2$ 계수 소거"가 행렬에서는 이렇게 가장 강한 꼴로 성립한다. $(\partial_zP)(\partial_{\bar z}P)$:

$$\begin{pmatrix}-\bar z&-\bar z^2\\ 1&\bar z\end{pmatrix}\begin{pmatrix}-z&1\\ -z^2&z\end{pmatrix}
=\begin{pmatrix}\bar zz+\bar z^2z^2&-\bar z-\bar z^2z\\ -z-\bar zz^2&1+\bar zz\end{pmatrix}
=\begin{pmatrix}s+s^2&-\bar z(1+s)\\ -z(1+s)&1+s\end{pmatrix}=S\begin{pmatrix}s&-\bar z\\ -z&1\end{pmatrix},$$

$$\partial_zP\,\partial_{\bar z}P=\frac1{S^3}\begin{pmatrix}s&-\bar z\\ -z&1\end{pmatrix},\qquad
\boxed{\ t:=\operatorname{tr}\big(\partial_zP\,\partial_{\bar z}P\big)=\frac{s+1}{S^3}=\frac1{S^2}\ }$$

### (4d) 세 눈금이 한 양으로

§4b의 $P=\tfrac12(I+\vec n\cdot\vec\sigma)$ 에서 상수 $\tfrac12I$ 는 미분에서 죽는다: $dP=\tfrac12\,d\vec n\cdot\vec\sigma$. §4a의 $\tfrac12\operatorname{tr}$ 복사로

$$\operatorname{tr}(dP\,dP)=\tfrac14\cdot2\,\lvert d\vec n\rvert^2=\tfrac12\,\lvert d\vec n\rvert^2=\tfrac12\cdot\frac4{S^2}\lvert dz\rvert^2=\frac2{S^2}\lvert dz\rvert^2$$

— §1·§3의 구면 계산과 §4c의 행렬 계산이 서로를 검산한다. 실좌표 그람행렬도 (4c)의 두 곱만으로: $P_x=\partial_zP+\partial_{\bar z}P$, $P_y=i(\partial_zP-\partial_{\bar z}P)$ 를 전개하고 trace (cyclic: $\operatorname{tr}(\partial_{\bar z}P\,\partial_zP)=t$):

$$E=\operatorname{tr}(P_xP_x)=\underbrace{0}_{(\partial_zP)^2}+t+t+\underbrace{0}_{(\partial_{\bar z}P)^2}=2t,\qquad
F=i\,[\,0-t+t-0\,]=0,\qquad
G=i^2[\,0-t-t+0\,]=2t.$$

계량 눈금 정리 — 전부 한 양 $t=\tfrac1{S^2}$ 의 상수배:

$$\lambda_{\text{라운드}}=4t\ (\S1\cdot\S3),\qquad
\lambda_{\operatorname{tr}}=2t\ (=E=G),\qquad
g_{z\bar z}=t.$$

---

## 5. 행렬 집합 위의 적분이 왜 2변수 적분인가

$\int$ 을 적으려면 원리가 필요하다. 곡면은 **행렬들의 집합** $M=\{P(z)\}\cup\{P(\infty)\}\subset\mathrm{Herm}(2)$ 이기 때문이다.

**넓이의 원리는 그람행렬식이다.** 내적 공간에서 두 벡터 $a,b$ 가 치는 평행사변형 넓이는 $\lvert a\rvert\lvert b\rvert\sin\theta$:

$$\text{넓이}^2=\lvert a\rvert^2\lvert b\rvert^2(1-\cos^2\theta)=\lvert a\rvert^2\lvert b\rvert^2-(a\cdot b)^2
=\det\begin{pmatrix}a\cdot a&a\cdot b\\ a\cdot b&b\cdot b\end{pmatrix}$$

— 내적만 있으면 되는 명제. 우리 접벡터는 행렬 $P_x,P_y$, 내적은 $\operatorname{tr}$, 그람행렬은 (4d)에서 쟀다: $E=G=2t$, $F=0$. 그러므로

$$dA_M=\sqrt{EG-F^2}\ dx\,dy=2t\ dx\,dy,
\qquad
\int_Mf\,dA_M:=\iint f\big(P(z)\big)\,2t\ dx\,dy.$$

**2변수 적분은 선언이 아니라, 행렬 접벡터들의 그람무게가 $(x,y)$ 마다 내려준 것이다.** (라운드 눈금이면 무게 $4t$ — 상수배.)

집합의 적분이 되려면 둘을 더 확인한다.

*빠진 점.* 차트 $v=(1,z)$ 는 $P(\infty)=\left(\begin{smallmatrix}0&0\\0&1\end{smallmatrix}\right)$ 을 못 덮는다. 반대 차트 $v=(w,1)$ 로 덮자. 이 차트의 $t_w$ 는 따로 계산할 필요가 없다: 기저를 맞바꾸는 상수 유니터리 $X=\sigma_1$ 에 대해 $X\binom w1=\binom1w$ 이므로 $P_{(w,1)}=X\,P_{(1,w)}\,X$; 상수 켤레는 미분과 교환하고 $\operatorname{tr}(XAX\,XBX)=\operatorname{tr}(AB)$ ($X^2=I$, cyclic) 이라 (4c)와 **글자만 바꾼 같은 계산**이 적용되어

$$t_w=\frac1{(1+\lvert w\rvert^2)^2}.$$

빠진 점은 이 차트의 $w=0$ — 무게 유한한 한 점, 넓이 $0$.

*차트 무관.* 겹침에서 $w=1/z$:

$$1+\lvert w\rvert^2=1+\frac1s=\frac Ss,\qquad
\frac{dw}{dz}=-\frac1{z^2}\ \Rightarrow\ \Big\lvert\frac{dw}{dz}\Big\rvert^2=\frac1{s^2},
\qquad
2t_w\cdot\Big\lvert\frac{dw}{dz}\Big\rvert^2=2\cdot\frac{s^2}{S^2}\cdot\frac1{s^2}=\frac2{S^2}=2t$$

— 두 차트의 넓이요소가 겹침에서 일치(치환적분). $\int_M$ 은 차트 선택과 무관하다.

---

## 6. 곡률 — 받아들인 공식을 여기서 쓴다

받아들인 공식 $K=-\tfrac1{2\lambda}\Delta\log\lambda$ 에 §2의 $\Delta=4\partial_z\partial_{\bar z}$ 를 쓴다. §4d의 결론이 $\lambda=(\text{상수})\cdot t$ 였다 — $\log\lambda=\log(\text{상수})+\log t$ 에서 **상수는 미분에서 죽으므로**

$$K\,dA=-\tfrac12\,\Delta\log\lambda\ dx\,dy=-\tfrac12\,\Delta\log t\ dx\,dy$$

— 가우스–보넷의 적분요소가 눈금과 무관하게 사영자 산출물 $t$ **하나의 로그**다. 계산하자. $\log t=-2\log S$:

$$\partial_{\bar z}\log t=-2\,\frac{\partial_{\bar z}S}S=-\frac{2z}S,\qquad
\partial_z\Big(-\frac{2z}S\Big)=-\frac{2\cdot S-2z\cdot\bar z}{S^2}=-\frac{2(S-s)}{S^2}=-\frac2{S^2},$$

$$\Delta\log t=4\cdot\Big(-\frac2{S^2}\Big)=-\frac8{S^2}.$$

눈금 $\lambda_c=c\,t$ 의 곡률:

$$K_c=-\frac1{2c\,t}\cdot\Big(-\frac8{S^2}\Big)=\frac{S^2}{2c}\cdot\frac8{S^2}=\frac4c.$$

$c=4$(라운드): $K=1$ — 단위구가 맞다. $c=2$($\operatorname{tr}$): $K=2$. $c=1$($g$): $K=4$. 눈금 절반이면 곡률 두 배 — 반지름 $1,\tfrac1{\sqrt2},\tfrac12$ 구의 $K=1/r^2$ 그대로.

---

## 7. 넓이

$$A_c=\iint c\,t\ dx\,dy\ \overset{\text{극좌표}}{=}\ c\cdot2\pi\int_0^\infty\frac{r\,dr}{(1+r^2)^2}
\qquad(r^2=s).$$

치환 $u=1+r^2$, $du=2r\,dr$:

$$\int_0^\infty\frac{r\,dr}{(1+r^2)^2}=\frac12\int_1^\infty\frac{du}{u^2}=\frac12\Big[-\frac1u\Big]_1^\infty=\frac12,
\qquad
A_c=c\cdot2\pi\cdot\frac12=c\,\pi.$$

$c=4$: $4\pi$ — 단위구 넓이, 맞다. $c=2$: $2\pi$, $c=1$: $\pi$. 적분의 수렴이 §5 "빠진 점 넓이 $0$"의 실물이다.

---

## 8. $\displaystyle\int_MK\,dA=4\pi$ — 같은 적분을 세 결로

**첫째, 그냥 곱한다.** $K_c$ 상수이므로

$$\int_MK\,dA=K_c\,A_c=\frac4c\cdot c\,\pi=4\pi$$

— $c$ 소거, 눈금 무관.

**둘째, 상수인 걸 모른 척하고, 사영자 언어 그대로.** §6의 적분요소로

$$\int_MK\,dA=-\frac12\iint\Delta\log\operatorname{tr}\big(\partial_zP\,\partial_{\bar z}P\big)\,dx\,dy
=-\frac12\iint\Big(-\frac8{S^2}\Big)dx\,dy=4\iint\frac{dx\,dy}{S^2}=4\pi$$

(마지막 적분은 §7에서 이미 했다). 가우스–보넷 적분의 정체는 행렬 양 $t$ 의 로그에 라플라시안을 건 것 — 눈금 $c$ 는 이 줄에 등장하지 못한다.

**셋째, 라플라시안의 적분이라면 반경함수로 끝까지.** $\log t=f(r)=-2\log(1+r^2)$ 은 $r$ 만의 함수다. 반경함수의 $\Delta$ 부터 손으로 만든다. $r^2=x^2+y^2$ 을 $x$ 로 미분하면 $2r\,\partial_xr=2x$, 곧 $\partial_xr=\tfrac xr$. 그러면

$$\partial_xf=f'\,\frac xr,\qquad
\partial_x^2f=f''\cdot\frac xr\cdot\frac xr+f'\cdot\Big(\frac1r-\frac{x}{r^2}\cdot\frac xr\Big)
=f''\,\frac{x^2}{r^2}+f'\Big(\frac1r-\frac{x^2}{r^3}\Big),$$

$y$ 쪽도 똑같이 하고 더하면 ($x^2+y^2=r^2$)

$$\Delta f=f''\,\frac{r^2}{r^2}+f'\Big(\frac2r-\frac{r^2}{r^3}\Big)=f''+\frac{f'}r=\frac1r\big(r\,f'\big)'.$$

원판 $r\le R$ 위의 적분이 완전미분이라 그냥 계산된다. $f'=-2\cdot\tfrac{2r}{1+r^2}=-\tfrac{4r}{1+r^2}$, 경계항 $r=0$ 에서 $rf'=-\tfrac{4r^2}{1+r^2}\to0$:

$$\iint_{r\le R}\Delta f\ dx\,dy=2\pi\int_0^R\frac1r\big(rf'\big)'\cdot r\,dr=2\pi\Big[r\,f'\Big]_0^R=2\pi R\,f'(R)=-\frac{8\pi R^2}{1+R^2},$$

$$\int_{r\le R}K\,dA=-\tfrac12\cdot\Big(-\frac{8\pi R^2}{1+R^2}\Big)=\frac{4\pi R^2}{1+R^2}.$$

이 유한형을 정직하게 재검산하자 — 라운드($c=4$, $K=1$)에서는 이 값이 그냥 캡의 넓이다. 직접 적분 ($u=1+r^2$):

$$\int_0^R\frac4{(1+r^2)^2}\cdot2\pi r\,dr=4\pi\int_1^{1+R^2}\frac{du}{u^2}=4\pi\Big[1-\frac1{1+R^2}\Big]=\frac{4\pi R^2}{1+R^2}\ \checkmark$$

$R=1$(적도까지): $2\pi$ — 전체의 절반, 반구. $R\to\infty$: $4\pi$ — 첫째·둘째와 재회.

---

## 9. 그런데 $4\pi$ 는 어디에 저장되어 있었나

셋째 계산이 말해준 것: 원판 적분 전체가 경계값 하나 $2\pi R\,f'(R)$ 로 응축된다. $R\to\infty$ 에서 남는 것은?

$$\log t=-2\log(1+r^2)\ \sim\ -4\log r,\qquad
r\,f'=-\frac{4r^2}{1+r^2}=-\frac4{1+1/r^2}\ \longrightarrow\ -4,$$

$$\int_MK\,dA=-\tfrac12\cdot2\pi\cdot(-4)=4\pi.$$

**전부가 빠진 한 점 $P(\infty)$ 주변에서 $t$ 가 갖는 로그계수 $-4$ ($t\sim r^{-4}$) 에 저장되어 있었다.** 상수 $c$ 는 $\log r$ 의 계수에 낄 수 없으니 눈금을 아무리 바꿔도 이 계수는 안 변한다 — $\int K\,dA$ 의 눈금 무관성이 이 그림이다.

이 $4\pi$ 가 임의 계량에서 불변($=2\pi\chi$, $\chi=2$)이라는 해석은 이 노트 밖의 일이다 — 계량 무관성(등각 변화)은 문서 `4`가 증명했고, $\chi=2$ 를 손으로 세는 것은 문서 `5`의 몫. 여기서 확립한 것은 수 $4\pi$, 세 눈금 공통, 무한원점 로그계수로의 응축까지다.

---

## 10. 정리, 그리고 다음 질문

등정로 전체가 이 노트 안에 있다:

$$S^2\subset\mathbb R^3\ \overset{\S0}{\to}\ \vec n(x,y)\ \overset{\S1}{\to}\ \lambda_{\text{라운드}}=\tfrac4{S^2}
\ \overset{\S2\text{–}3}{\to}\ \partial_z,\ \text{복소 재유도}
\ \overset{\S4}{\to}\ P,\ t=\operatorname{tr}(\partial_zP\,\partial_{\bar z}P)=\tfrac1{S^2}
\ \overset{\S5}{\to}\ dA=\sqrt{EG-F^2}\,dxdy
\ \overset{\S6\text{–}8}{\to}\ \int K\,dA=4\pi
\ \overset{\S9}{\to}\ t\sim r^{-4}.$$

| $\lambda$ | 어디서 온 눈금 | $K$ | $A$ | $\int K\,dA$ |
|---|---|---|---|---|
| $4t$ | 라운드 — §1(실좌표)·§3(복소) 두 번 유도 | $1$ | $4\pi$ | $4\pi$ |
| $2t$ | $\operatorname{tr}(dP\,dP)$ — §4 그람무게 | $2$ | $2\pi$ | $4\pi$ |
| $t$ | $g_{z\bar z}$ (FS/겹침) | $4$ | $\pi$ | $4\pi$ |

수입품은 곡률 공식 하나, 이 안에서 만든 도구는 $\partial_z$(§2)와 반경 라플라시안(§8). 덤으로 얻은 관찰 둘 — $(\partial_zP)^2$ 은 행렬째 $0$(멱영), $\partial_zP\,\partial_{\bar z}P=\tfrac1{S^3}\left(\begin{smallmatrix}s&-\bar z\\-z&1\end{smallmatrix}\right)$.

다음 질문 셋. 캡의 유한형이 $2\pi$ 에서 모자라는 몫 $2\pi\tfrac{1-R^2}{1+R^2}$ 을 경계 위도원의 **측지곡률**로 읽을 수 있을까 — 그러려면 $k_g$ 를 먼저 정의하고 계산해야 한다(아직 안 했다). $\chi=2$ 를 손으로 셀 수 있을까(문서 `5`). 그람무게 원리는 차원을 안 가리니, 접행렬 $2n$ 개로 같은 노트를 $\mathbb{CP}^n$ 에서 다시 쓸 수 있을까(문서 `2` §4의 닫힌형이 입구다).
