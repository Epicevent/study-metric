# 0 — (Part 1 손노트 옮김) 구면에서 곡률공식까지

> 손글씨 Part 1(`원본노트/Part1.pdf`, 11쪽)을 한 줄도 건너뛰지 않고 옮긴 것. 흐름: 입체사영으로 둥근 계량을 짓고 → 제2기본형식·shape operator로 $K=\dfrac{LN-M^2}{EG-F^2}$ → **제1기본형식만으로** 다시 쓰고(Theorema Egregium, 3×3 결정자 항등식) → 등온좌표에서 $K=-\dfrac1{2\lambda}\Delta\log\lambda$ → 구면에 넣어 Liouville과 닫는 물음까지. 이 문서의 마지막 식이 문서 `1`의 출발점이다.

---

## 1. 입체사영

북극 $N=(0,0,1)$, 평면점 $X=(x,y,0)$. 직선
$$
P=N+t(X-N)=(1-t)N+tX=(tx,\ ty,\ 1-t).
$$
$P$ 가 단위구 $S^2$ 위에 있으려면 $(tx)^2+(ty)^2+(1-t)^2=1$:
$$
t^2(x^2+y^2)+1-2t+t^2=1\ \Rightarrow\ t^2(x^2+y^2+1)-2t=0\ \Rightarrow\ t\big[(x^2+y^2+1)t-2\big]=0.
$$
$t\ne0$ 이므로 $t=\dfrac{2}{x^2+y^2+1}$. 따라서 ($D:=x^2+y^2+1$)
$$
P=\Big(\frac{2x}{D},\ \frac{2y}{D},\ 1-\frac{2}{D}\Big),\qquad 1-\frac2D=\frac{x^2+y^2-1}{D}.
$$

---

## 2. 제1기본형식 — $E=G=\dfrac{4}{(1+s)^2}$, $F=0$

몫의 미분으로 ($s:=x^2+y^2$, $D=1+s$):
$$
P_x=\frac{1}{D^2}\big(2(1+y^2-x^2),\ -4xy,\ 4x\big),\qquad
P_y=\frac{1}{D^2}\big(-4xy,\ 2(1+x^2-y^2),\ 4y\big).
$$

**$E=\langle P_x,P_x\rangle$.** 분자(=$D^4\,E$)를 전개한다:
$$
4(1+y^2-x^2)^2+16x^2y^2+16x^2.
$$
$(1+y^2-x^2)^2=1+y^4+x^4+2y^2-2x^2-2x^2y^2$ 이므로 $4(\cdots)=4+4y^4+4x^4+8y^2-8x^2-8x^2y^2$. 나머지 둘을 더하면
$$
4+4y^4+4x^4+8y^2-8x^2-8x^2y^2+16x^2y^2+16x^2
=4\big(1+x^4+y^4+2x^2+2y^2+2x^2y^2\big)=4(1+x^2+y^2)^2=4D^2.
$$
따라서 $E=\dfrac{4D^2}{D^4}=\dfrac{4}{D^2}=\dfrac{4}{(1+s)^2}$.

**$F=\langle P_x,P_y\rangle$.** 분자(=$D^4F$):
$$
2(1+y^2-x^2)(-4xy)+(-4xy)\,2(1+x^2-y^2)+4x\cdot4y
=-8xy\big[(1+y^2-x^2)+(1+x^2-y^2)\big]+16xy.
$$
대괄호 $=2$ 이므로 $=-16xy+16xy=0$. $\boxed{F=0}$.

**$G=\langle P_y,P_y\rangle=\dfrac{4}{(1+s)^2}$** (대칭). 그러므로
$$
\boxed{\ ds^2=E\,dx^2+2F\,dx\,dy+G\,dy^2=\frac{4}{(1+x^2+y^2)^2}(dx^2+dy^2)\ }.
$$

**첫 관찰.** $P$ 는 단위구의 **단위 법벡터**($n=P$)다. 따라서 Gauss 사상이 항등사상, shape operator $S=-dn=-\mathrm{Id}$, $\det S=(-1)(-1)=1=K$. 아래 §4–5에서 이 $K=1$ 을 *계량만으로* 다시 유도한다.

---

## 3. 일반 곡면의 곡률 $K=\dfrac{LN-M^2}{EG-F^2}$

곡면 $P(x,y)$, 법벡터 $n=\dfrac{P_x\times P_y}{\|P_x\times P_y\|}$. 제1기본형식 $E,F,G$ 위와 같고, 제2기본형식
$$
L=\langle P_{xx},n\rangle,\quad M=\langle P_{xy},n\rangle,\quad N=\langle P_{yy},n\rangle.
$$
shape operator는 Gauss 사상의 미분 $W=-dn$ (곧 $W(P_x)=-n_x$, $W(P_y)=-n_y$). **Weingarten 관계** — $\langle n,P_x\rangle=0$, $\langle n,P_y\rangle=0$ 을 미분하면 ($\langle n_x,P_x\rangle+\langle n,P_{xx}\rangle=0$ 등)
$$
\langle W(P_x),P_x\rangle=\langle-n_x,P_x\rangle=\langle n,P_{xx}\rangle=L,\quad
\langle W(P_x),P_y\rangle=\langle n,P_{xy}\rangle=M,\quad
\langle W(P_y),P_y\rangle=N.
$$
$W(P_x)=aP_x+cP_y,\ W(P_y)=bP_x+dP_y$ 로 두면 위가 $\langle W(P_x),P_x\rangle=aE+cF=L$, $\langle W(P_x),P_y\rangle=aF+cG=M$, 마찬가지로 $bE+dF=M$, $bF+dG=N$:
$$
\begin{pmatrix}E&F\\F&G\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}L&M\\M&N\end{pmatrix}
\ \Rightarrow\
\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}E&F\\F&G\end{pmatrix}^{-1}\begin{pmatrix}L&M\\M&N\end{pmatrix}.
$$
Gauss 곡률은 정의상 주곡률(=$W$ 의 두 고유값)의 곱, 곧 $K=\det W$. 행렬식의 곱셈성으로
$$
K=\det W=\frac{\det\begin{pmatrix}L&M\\M&N\end{pmatrix}}{\det\begin{pmatrix}E&F\\F&G\end{pmatrix}}:
$$
$$
\boxed{\ K=\frac{LN-M^2}{EG-F^2}\ }.
$$

---

## 4. 제1기본형식만으로 (Theorema Egregium)

목표: $K$ 가 $E,F,G$ 와 그 도함수로만 적힘을 보인다(법선·embedding 없이). $L,M,N$ 을 결정자로 우회한다.

### 4.1 세 결정자

세 벡터를 열로 갖는 $3\times3$ 행렬의 결정자는 **스칼라 삼중곱**과 같다 — 첫 열 여인수 전개의 계수가 정확히 $b\times c$ 의 성분이라 $\det(a,b,c)=a\cdot(b\times c)$:
$$
D_1:=\det(P_{xx},P_x,P_y)=P_{xx}\cdot(P_x\times P_y),\quad
D_2:=\det(P_{xy},P_x,P_y),\quad
D_3:=\det(P_{yy},P_x,P_y).
$$
$n=\dfrac{P_x\times P_y}{\|P_x\times P_y\|}$ 이므로 $P_{xx}\cdot(P_x\times P_y)=\|P_x\times P_y\|\,\langle P_{xx},n\rangle=\|P_x\times P_y\|\,L$. 같은 식으로
$$
D_1=\|P_x\times P_y\|\,L,\quad D_2=\|P_x\times P_y\|\,M,\quad D_3=\|P_x\times P_y\|\,N.
$$
Lagrange 항등식 ($\|a\times b\|^2=\|a\|^2\|b\|^2\sin^2\theta=\|a\|^2\|b\|^2-\|a\|^2\|b\|^2\cos^2\theta=\|a\|^2\|b\|^2-\langle a,b\rangle^2$): $\|P_x\times P_y\|^2=\|P_x\|^2\|P_y\|^2-\langle P_x,P_y\rangle^2=EG-F^2$. 따라서
$$
LN-M^2=\frac{D_1D_3-D_2^2}{\|P_x\times P_y\|^2}=\frac{D_1D_3-D_2^2}{EG-F^2},
\qquad
\boxed{\ K=\frac{D_1D_3-D_2^2}{(EG-F^2)^2}\ }.
$$

### 4.2 결정자 곱을 내적의 결정자로

$\det A\,\det B=\det(A^{\mathsf T}B)$ (곱셈성 $\det A\,\det B=\det(AB)$ 와 $\det A^{\mathsf T}=\det A$), 그리고 $A^{\mathsf T}B$ 의 성분은 $A,B$ 열들의 내적이다. $A=(P_{xx},P_x,P_y)$, $B=(P_{yy},P_x,P_y)$:
$$
D_1D_3=\det\!\begin{pmatrix}
\langle P_{xx},P_{yy}\rangle & \langle P_{xx},P_x\rangle & \langle P_{xx},P_y\rangle\\
\langle P_x,P_{yy}\rangle & E & F\\
\langle P_y,P_{yy}\rangle & F & G
\end{pmatrix},
\quad
D_2^2=\det\!\begin{pmatrix}
\langle P_{xy},P_{xy}\rangle & \langle P_{xy},P_x\rangle & \langle P_{xy},P_y\rangle\\
\langle P_x,P_{xy}\rangle & E & F\\
\langle P_y,P_{xy}\rangle & F & G
\end{pmatrix}.
$$

### 4.3 첫 행 여인수 전개

행렬 $\begin{pmatrix}\alpha&\beta&\gamma\\ p&E&F\\ q&F&G\end{pmatrix}$ 의 결정자는 $\alpha(EG-F^2)-\beta(pG-Fq)+\gamma(pF-Eq)$. 적용:
$$
D_1D_3=\langle P_{xx},P_{yy}\rangle(EG-F^2)-\langle P_{xx},P_x\rangle(pG-Fq)+\langle P_{xx},P_y\rangle(pF-Eq),
$$
$$
D_2^2=\langle P_{xy},P_{xy}\rangle(EG-F^2)-\langle P_{xy},P_x\rangle(p'G-Fq')+\langle P_{xy},P_y\rangle(p'F-Eq'),
$$
여기서 $p=\langle P_x,P_{yy}\rangle,\ q=\langle P_y,P_{yy}\rangle,\ p'=\langle P_x,P_{xy}\rangle,\ q'=\langle P_y,P_{xy}\rangle$. 모든 $\beta,\gamma,p,q,\dots$ 는 $\langle\text{2계},\text{1계}\rangle$ 형이라 제1기본형식의 도함수로 환원된다(§4.4). 단 하나 $\langle P_{xx},P_{yy}\rangle-\langle P_{xy},P_{xy}\rangle$ 만 $\langle\text{2계},\text{2계}\rangle$ 인데, 이것도 환원된다 — 그것이 Egregium의 핵심.

### 4.4 내적들을 $E,F,G$ 의 도함수로

$\langle P_x,P_x\rangle=E$ 등을 미분한다:
$$
\partial_x\langle P_x,P_x\rangle=2\langle P_{xx},P_x\rangle=E_x,\quad
\partial_y\langle P_x,P_x\rangle=2\langle P_{xy},P_x\rangle=E_y,
$$
$$
\partial_y\langle P_y,P_y\rangle=2\langle P_{yy},P_y\rangle=G_y,\quad
\partial_x\langle P_y,P_y\rangle=2\langle P_{xy},P_y\rangle=G_x,
$$
$$
\partial_x\langle P_x,P_y\rangle=\langle P_{xx},P_y\rangle+\langle P_x,P_{xy}\rangle=F_x,\quad
\partial_y\langle P_x,P_y\rangle=\langle P_{xy},P_y\rangle+\langle P_x,P_{yy}\rangle=F_y.
$$
이것으로 모든 1차 항을 적을 수 있다.

---

## 5. 등온좌표에서 마무리 ($F=0,\ E=G=\lambda$)

§2의 구면이 정확히 이 경우다($F=0$, $E=G=\lambda$). 위 항등식이 깔끔해진다:
$$
\langle P_{xx},P_x\rangle=\tfrac12\lambda_x,\quad
\langle P_{xy},P_x\rangle=\tfrac12\lambda_y,\quad
\langle P_{yy},P_y\rangle=\tfrac12\lambda_y,\quad
\langle P_{xy},P_y\rangle=\tfrac12\lambda_x,
$$
그리고 $F=0$ 의 미분 $\langle P_{xx},P_y\rangle+\langle P_x,P_{xy}\rangle=0$, $\langle P_{xy},P_y\rangle+\langle P_x,P_{yy}\rangle=0$ 에서
$$
\langle P_{xx},P_y\rangle=-\langle P_x,P_{xy}\rangle=-\tfrac12\lambda_y,\qquad
\langle P_x,P_{yy}\rangle=-\langle P_{xy},P_y\rangle=-\tfrac12\lambda_x.
$$

### 5.1 핵심 2계–2계 항

$\langle P_{xx},P_y\rangle=-\tfrac12\lambda_y$ 를 $y$ 로, $\langle P_{xy},P_y\rangle=\tfrac12\lambda_x$ 를 $x$ 로 미분:
$$
\langle P_{xxy},P_y\rangle+\langle P_{xx},P_{yy}\rangle=-\tfrac12\lambda_{yy},\qquad
\langle P_{xxy},P_y\rangle+\langle P_{xy},P_{xy}\rangle=\tfrac12\lambda_{xx}.
$$
둘을 빼면 $\langle P_{xxy},P_y\rangle$ 가 소거되어
$$
\boxed{\ \langle P_{xx},P_{yy}\rangle-\langle P_{xy},P_{xy}\rangle=-\tfrac12(\lambda_{xx}+\lambda_{yy})=-\tfrac12\Delta\lambda\ }.
$$

### 5.2 두 결정자 ($F=0,E=G=\lambda$)

§4.3에 대입. $\langle P_{xx},P_x\rangle=\tfrac12\lambda_x$, $\langle P_x,P_{yy}\rangle=-\tfrac12\lambda_x$, $\langle P_{xx},P_y\rangle=-\tfrac12\lambda_y$, $\langle P_y,P_{yy}\rangle=\tfrac12\lambda_y$:
$$
D_1D_3=\langle P_{xx},P_{yy}\rangle\lambda^2-\big(\tfrac12\lambda_x\big)\big(-\tfrac12\lambda_x\big)\lambda+\big(-\tfrac12\lambda_y\big)\big(-\tfrac12\lambda_y\big)\lambda
=\langle P_{xx},P_{yy}\rangle\lambda^2+\tfrac14(\lambda_x^2+\lambda_y^2)\lambda.
$$
(둘째 항 $-\beta(pG-Fq)=-(\tfrac12\lambda_x)(-\tfrac12\lambda_x\cdot\lambda)=+\tfrac14\lambda_x^2\lambda$; 셋째 항 $+\gamma(pF-Eq)=(-\tfrac12\lambda_y)(-\lambda\cdot\tfrac12\lambda_y)=+\tfrac14\lambda_y^2\lambda$.)

$\langle P_{xy},P_x\rangle=\langle P_x,P_{xy}\rangle=\tfrac12\lambda_y$, $\langle P_{xy},P_y\rangle=\langle P_y,P_{xy}\rangle=\tfrac12\lambda_x$:
$$
D_2^2=\langle P_{xy},P_{xy}\rangle\lambda^2-\big(\tfrac12\lambda_y\big)\big(\tfrac12\lambda_y\big)\lambda-\big(\tfrac12\lambda_x\big)\big(\tfrac12\lambda_x\big)\lambda
=\langle P_{xy},P_{xy}\rangle\lambda^2-\tfrac14(\lambda_x^2+\lambda_y^2)\lambda.
$$
빼면
$$
D_1D_3-D_2^2=\big(\langle P_{xx},P_{yy}\rangle-\langle P_{xy},P_{xy}\rangle\big)\lambda^2+\tfrac12(\lambda_x^2+\lambda_y^2)\lambda
=-\tfrac12\Delta\lambda\,\lambda^2+\tfrac12(\lambda_x^2+\lambda_y^2)\lambda.
$$

### 5.3 곡률

$(EG-F^2)^2=\lambda^4$ 로 나눈다:
$$
K=\frac{D_1D_3-D_2^2}{\lambda^4}
=\frac{-\tfrac12\Delta\lambda\,\lambda^2+\tfrac12(\lambda_x^2+\lambda_y^2)\lambda}{\lambda^4}
=-\frac{\Delta\lambda}{2\lambda^2}+\frac{\lambda_x^2+\lambda_y^2}{2\lambda^3}.
$$
$\Delta\log\lambda=\partial_x\!\big(\tfrac{\lambda_x}{\lambda}\big)+\partial_y\!\big(\tfrac{\lambda_y}{\lambda}\big)=\dfrac{\Delta\lambda}{\lambda}-\dfrac{\lambda_x^2+\lambda_y^2}{\lambda^2}$ 이므로
$$
\boxed{\ K=-\frac{1}{2\lambda}\Big(\frac{\Delta\lambda}{\lambda}-\frac{\lambda_x^2+\lambda_y^2}{\lambda^2}\Big)=-\frac{1}{2\lambda}\,\Delta\log\lambda=-\frac{1}{2e^{\sigma}}\Delta\sigma,\quad \sigma=\log\lambda\ }.
$$
*(검산: $E=G$, $F=0$, $\|P_x\times P_y\|^2=EG-F^2$, $K=1$, 그리고 §5의 모든 내적 항등식과 $\langle P_{xx},P_{yy}\rangle-\langle P_{xy},P_{xy}\rangle=-\tfrac12\Delta\lambda$ 를 sympy로 확인.)*

---

## 6. 구면에 넣으면 — Liouville, 그리고 닫는 물음

§2의 구면 $\lambda=\dfrac{4}{(1+x^2+y^2)^2}$ 에 $K=1$ 을 부과:
$$
1=-\frac{1}{2e^{\sigma}}\Delta\sigma\ \Longleftrightarrow\ \Delta\sigma=-2e^{\sigma}.
$$
실제 해임을 확인 — $\sigma=\log4-2\log(1+x^2+y^2)$, $\sigma_x=-\dfrac{4x}{1+x^2+y^2}$:
$$
-\Delta\sigma=\partial_x\!\Big(\frac{4x}{1+x^2+y^2}\Big)+\partial_y\!\Big(\frac{4y}{1+x^2+y^2}\Big)
=\frac{4(1+x^2+y^2)-8x^2+4(1+x^2+y^2)-8y^2}{(1+x^2+y^2)^2}=\frac{8}{(1+s)^2},
$$
$$
2e^{\sigma}=2\cdot\frac{4}{(1+s)^2}=\frac{8}{(1+s)^2}\ \Rightarrow\ \Delta\sigma=-2e^\sigma.\quad\checkmark
$$

> **닫는 물음 (Part 1의 마지막 줄).** *다른 해는 없는가?* — 여기서 문서 `1`이 시작한다(구를 모르는 척하고 $\Delta\sigma=-2e^\sigma$ 를 직접 적분).
