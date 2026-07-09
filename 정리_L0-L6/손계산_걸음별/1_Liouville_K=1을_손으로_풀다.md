# 1 — $K\equiv1$ 을 손으로 풀다: Liouville에서 구면까지

설정: $ds^2=\lambda|dz|^2$, $\sigma=\log\lambda$, 등온좌표 곡률 $K=-\dfrac{1}{2\lambda}\Delta\sigma$ (문서 `0` §5). $z=x+iy$, $s=r^2$, 회전대칭이면 $\Delta=\dfrac{d^2}{dr^2}+\dfrac1r\dfrac{d}{dr}=\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{d}{dr}\Big)$.

---

## 1. $K\equiv1$ 은 곧 $\Delta\sigma=-2e^\sigma$

곡률식에 $K=1$ 을 부과: $1=-\dfrac1{2\lambda}\Delta\sigma$, 양변에 $-2\lambda=-2e^\sigma$ 곱하면 $\boxed{\Delta\sigma=-2e^\sigma}$ (Liouville).

**구면으로 확인.** $\lambda=\dfrac{4}{(1+r^2)^2}$, $\sigma=\log4-2\log(1+r^2)$. 한 칸씩:
$$
\sigma'=-2\cdot\frac{2r}{1+r^2}=-\frac{4r}{1+r^2},\qquad r\sigma'=-\frac{4r^2}{1+r^2},
$$
$$
(r\sigma')'=-\frac{(8r)(1+r^2)-(4r^2)(2r)}{(1+r^2)^2}=-\frac{8r+8r^3-8r^3}{(1+r^2)^2}=-\frac{8r}{(1+r^2)^2},
$$
$$
\Delta\sigma=\frac1r(r\sigma')'=-\frac{8}{(1+r^2)^2}=-2\cdot\frac{4}{(1+r^2)^2}=-2e^\sigma.\quad\checkmark
$$
되넣으면 $K=-\dfrac1{2\lambda}\Delta\sigma=-\dfrac{(1+r^2)^2}{8}\cdot\Big(-\dfrac{8}{(1+r^2)^2}\Big)=1$. $(1+r^2)^2$ 이 통째로 약분 — 법벡터·embedding 없이 안에서 본 $K=1$.

---

## 2. 자율형으로 ($t=\log r$)

회전대칭 해 $\sigma=\sigma(r)$ 를 찾는다: $\dfrac1r(r\sigma')'=-2e^\sigma$. 비선형이라 직접 적분이 안 된다. 스케일 대칭 $r\mapsto cr$ 을 좌표로 삼아 자율형으로 바꾼다.

### 2.1 좌표 바꾸기
$t=\log r$, 곧 $r=e^t$, $\dfrac{dt}{dr}=\dfrac1r$, 따라서 $\dfrac{d}{dr}=\dfrac1r\dfrac{d}{dt}$ (점$\,\dot{}=d/dt$).
$$
\sigma'=\frac{d\sigma}{dr}=\frac1r\dot\sigma\ \Rightarrow\ r\sigma'=\dot\sigma,
$$
$$
(r\sigma')'=\frac{d}{dr}\dot\sigma=\frac1r\frac{d}{dt}\dot\sigma=\frac1r\ddot\sigma,\qquad
\frac1r(r\sigma')'=\frac1{r^2}\ddot\sigma=e^{-2t}\ddot\sigma.
$$
방정식 $e^{-2t}\ddot\sigma=-2e^\sigma$ 의 양변에 $r^2=e^{2t}$:
$$
\ddot\sigma=-2e^{\sigma+2t}.
$$

### 2.2 $t$ 를 변수에 흡수
$\psi:=\sigma+2t=\log\lambda+2\log r=\log(\lambda r^2)$. 미분:
$$
\dot\psi=\dot\sigma+2,\qquad \ddot\psi=\ddot\sigma\quad(2t\ \text{는 1차, 2계도함수 }0).
$$
$\sigma+2t=\psi$ 이므로 $e^{\sigma+2t}=e^\psi$. §2.1에 넣으면
$$
\boxed{\ \ddot\psi=-2e^{\psi}\ }\qquad(t\ \text{소거된 자율방정식}).
$$

---

## 3. 에너지 첫적분, 원점이 상수를 고정

### 3.1 첫적분
$\ddot\psi=-2e^\psi$ 의 양변에 $\dot\psi$ 를 곱한다. 좌·우변이 완전미분임을 알아챈다:
$$
\dot\psi\,\ddot\psi=\frac{d}{dt}\Big(\tfrac12\dot\psi^2\Big),\qquad -2e^\psi\dot\psi=\frac{d}{dt}\big(-2e^\psi\big).
$$
$t$ 로 적분(상수 $C$):
$$
\tfrac12\dot\psi^2=-2e^\psi+C\ \Rightarrow\ \dot\psi^2=2C-4e^\psi.
$$

### 3.2 원점 정칙성으로 $C=2$
원점에서 계량 $ds^2=\lambda(dx^2+dy^2)$ 가 매끄럽고 비퇴화면 $\lambda$ 는 매끄럽고 $\lambda(0)>0$, 곧 $\lambda=\lambda(0)+O(r^2)$. 그러면 $e^\psi=\lambda r^2=\lambda(0)r^2+O(r^4)\to0$, 그리고
$$
\psi=\log(\lambda r^2)=2\log r+\log\lambda(0)+O(r^2)=2t+\log\lambda(0)+O(e^{2t}),
$$
$t$ 로 미분하면 $\dot\psi=2+O(e^{2t})\xrightarrow{\ t\to-\infty\ }2$ ($r^2=e^{2t}\to0$).
$\dot\psi^2=2C-4e^\psi$ 에 $t\to-\infty$ 극한을 넣으면 $2^2=2C-0$, 곧 $C=2$:
$$
\boxed{\ \dot\psi^2=4(1-e^\psi)\ }.
$$

---

## 4. 변수분리로 적분

### 4.1 분리
원점 근처 $\dot\psi\to+2>0$ 이라 양의 가지 $\dot\psi=2\sqrt{1-e^\psi}$:
$$
\frac{d\psi}{\sqrt{1-e^\psi}}=2\,dt.
$$

### 4.2 좌변을 적분 가능하게 — 치환 $w=\sqrt{1-e^\psi}$
$$
w^2=1-e^\psi\ \Rightarrow\ e^\psi=1-w^2,\qquad e^\psi\,d\psi=-2w\,dw\ \Rightarrow\ d\psi=\frac{-2w}{1-w^2}\,dw,
$$
$$
\frac{d\psi}{\sqrt{1-e^\psi}}=\frac{1}{w}\cdot\frac{-2w}{1-w^2}\,dw=\frac{-2}{1-w^2}\,dw.
$$

### 4.3 부분분수로 적분
$\dfrac{1}{1-w^2}=\dfrac{1}{(1-w)(1+w)}=\dfrac12\Big(\dfrac{1}{1-w}+\dfrac{1}{1+w}\Big)$ 이므로
$$
\int\frac{-2\,dw}{1-w^2}=-\Big(\!\int\frac{dw}{1-w}+\int\frac{dw}{1+w}\Big)=-\big(-\log(1-w)+\log(1+w)\big)=-\log\frac{1+w}{1-w}.
$$
$\operatorname{artanh}w=\tfrac12\log\dfrac{1+w}{1-w}$ 이므로 좌변 $=-2\operatorname{artanh}w$. 우변은 $2t+\text{c}$:
$$
-2\operatorname{artanh}w=2t+\text{c}\ \Rightarrow\ \operatorname{artanh}w=t_0-t\ \Rightarrow\ w=\tanh(t_0-t),\quad w^2=\tanh^2(t-t_0).
$$

### 4.4 복원
$$
e^\psi=1-w^2=1-\tanh^2(t-t_0)=\operatorname{sech}^2(t-t_0)\qquad(1-\tanh^2=\operatorname{sech}^2).
$$
**$\operatorname{sech}^2$ 를 지수로 — 손으로:** $\operatorname{sech}x=\dfrac{1}{\cosh x}=\dfrac{2}{e^x+e^{-x}}=\dfrac{2e^x}{e^{2x}+1}$, 제곱하면 $\operatorname{sech}^2x=\dfrac{4e^{2x}}{(e^{2x}+1)^2}$. $x=t-t_0$, $e^{2(t-t_0)}=e^{2t}e^{-2t_0}=a r^2$ ($a:=e^{-2t_0}>0$):
$$
e^\psi=\frac{4ar^2}{(1+ar^2)^2}\ \Rightarrow\ \lambda=\frac{e^\psi}{r^2}=\boxed{\ \frac{4a}{(1+ar^2)^2}\ }\quad(a>0).
$$
$a=1$ 이 §1의 구면. 상수 둘 중 $C$ 는 정칙성으로, $a$ 는 딜레이션 $z\mapsto\sqrt a\,z$ 로.

---

## 5. 회전대칭을 떼면 — 정칙 $f$ 하나마다 해 하나

임의 국소단사 정칙 $f$ 에 대해 $\lambda=\dfrac{4|f'|^2}{(1+|f|^2)^2}$ 도 해다. 두 보조정리를 손으로.

### 5.1 정칙 사상의 라플라시안 공변성
$\Delta_z(g\circ f)=|f'|^2(\Delta_w g)\circ f$. $\Delta=4\partial_z\partial_{\bar z}$, $f$ 정칙이라 $\partial_{\bar z}f=0$, $\partial_z\bar f=0$. 체인룰:
$$
\partial_z(g\circ f)=g_w\,\partial_z f+g_{\bar w}\,\partial_z\bar f=g_w\,f'\quad(\partial_z\bar f=0),
$$
$$
\partial_{\bar z}\partial_z(g\circ f)=\partial_{\bar z}(g_w\,f')=f'\,\partial_{\bar z}(g_w)=f'\,g_{w\bar w}\,\partial_{\bar z}\bar f=f'\,g_{w\bar w}\,\overline{f'}=|f'|^2\,g_{w\bar w}.
$$
($f'$ 는 정칙이라 $\partial_{\bar z}f'=0$.) $\times4$: $\ \Delta_z(g\circ f)=|f'|^2(\Delta_w g)\circ f$. ∎

### 5.2 $\log|f'|^2$ 은 조화
$f$ 국소단사 ⟹ $f'\ne0$ ⟹ $\log f'$ 정칙. $\log|f'|^2=\log(f'\overline{f'})=\log f'+\log\overline{f'}=2\,\mathrm{Re}(\log f')$. 정칙함수 실수부는 조화 ⟹ $\Delta_z\log|f'|^2=0$.

### 5.3 확인
$\Lambda(w)=\dfrac4{(1+|w|^2)^2}$ 에 §1의 계산을 $w$ 로 그대로 — $\log\Lambda=\log4-2\log(1+|w|^2)$, $\Delta_w\log(1+|w|^2)=4/(1+|w|^2)^2$ 이므로 $\Delta_w\log\Lambda=-8/(1+|w|^2)^2=-2\Lambda$. $\sigma=\log\lambda=(\log\Lambda)\circ f+\log|f'|^2$ 이고 $\Delta$ 가 선형:
$$
\Delta_z\sigma=\underbrace{|f'|^2(\Delta_w\log\Lambda)\circ f}_{\text{5.1}}+\underbrace{\Delta_z\log|f'|^2}_{=0\ (\text{5.2})}
=|f'|^2(-2\Lambda\circ f)=-2\,\Lambda(f)|f'|^2=-2\lambda.\quad\checkmark
$$
임의 정칙 $f$ 가 $K\equiv1$ 해를 준다. (기계 검산: $f=z^2$, Möbius 모두 $\Delta\sigma+2\lambda=0$; $\operatorname{sech}^2$·artanh 항등식 수치 확인.)

> 문서 `2`: 이 $\lambda=4/(1+|z|^2)^2$ 를 $\partial\bar\partial$ 한 포텐셜 $\Phi=\log S$ 로 다시 적고 CPⁿ으로 올린다.
