# IG1 — Bregman divergence에서 Hessian 계량까지

> 강의노트 *Dually Flat Geometry v2* **§3.1 "Second derivative: Hessian metric"** 의 완전 유도.
> 원문은 네 줄이다. 이 문서는 그 네 줄을 한 줄도 건너뛰지 않고 펴고, 원문이 말하지 않는 세 가지 — **부호는 왜 마이너스인가**, **미분 순서를 바꾸면 왜 다른 상쇄가 일어나는가**, **§1의 $\tfrac12$ 규약과 어떻게 맞물리는가** — 를 채운다.
> 대상 원문은 외부 강의노트라 저장소에 포함하지 않는다 (인용한 정의·주장은 전부 아래에 옮겨 적었다).
> 검산: `verify_ig1_bregman.py` (25/25)

---

## §0. 이 계산이 우리 트랙에서 서는 자리

걸음 0–6에서 우리가 반복한 동작은 하나였다: **퍼텐셜 하나를 두 번 미분하면 계량이 나온다.**

$$\text{켈러 트랙:}\quad g_{j\bar k}=\partial_j\bar\partial_k\log K \qquad\text{(퍼텐셜의 \emph{복소} Hessian)}$$

정보기하는 같은 동작의 **실수판**이다:

$$\text{정보기하 트랙:}\quad g_{ij}=F_{ij} \qquad\text{(볼록 퍼텐셜의 \emph{실} Hessian)}$$

그런데 출발점이 다르다. 켈러 쪽은 퍼텐셜 $K$를 **손에 쥐고 시작**했다. 정보기하 쪽은 **divergence $D[P:Q]$를 쥐고 시작해서** 계량을 *유도*한다. §3.1이 하는 일이 정확히 그 유도이고, 결과가 "그 divergence를 만든 볼록함수의 Hessian"이라는 것이다.

한 가지 더 — 걸음 5에서 잰 QFIM의 고전판인 **Fisher 정보계량**이 이 유도의 특수경우로 나온다(§6). 두 트랙이 만나는 지점이다.

---

## §1. 셋업 — 기호를 못 박는다

볼록영역의 좌표를 $x=(x^1,\dots,x^n)$이라 하고, 볼록함수 $F$의 **Bregman divergence**를

$$\boxed{\;D(x,y)\;=\;B_F[x:y]\;=\;F(x)-F(y)-F_a(y)\,(x^a-y^a)\;}$$

로 둔다. 표기 약속:

| 기호 | 뜻 |
|---|---|
| $F_a$ | $\partial F/\partial x^a$ |
| $F_{ij}$ | $\partial^2F/\partial x^i\partial x^j$ |
| $F_a(y)(x^a-y^a)$ | $a$에 대한 **합** (아인슈타인 규약) |
| $\partial_i$ | **첫** 슬롯($x$)의 미분 |
| $\partial'_j$ | **둘째** 슬롯($y$)의 미분 |

기하적으로 $D(x,y)$는 "$y$에서 그은 접평면과 실제 $F$ 사이의 세로 간격"이다. $F$가 볼록이면 접평면이 항상 아래에 있으므로 $D\ge0$이고, $D=0$은 $x=y$에서만 (강볼록일 때).

> **유일하게 조심할 것.** $F_a(y)$는 **$y$만의 함수**다. $\partial_i$(첫 슬롯)에는 상수처럼 행동하고, 거꾸로 $x^a$는 $\partial'_j$(둘째 슬롯)에 상수처럼 행동한다. 아래 모든 계산이 이 한 문장에서 갈린다.

---

## §2. ① 첫 슬롯 1계 — $\partial_iD=F_i(x)-F_i(y)$

$x^i$로 미분한다. 세 항을 따로:

$$\partial_i\,F(x)=F_i(x)$$

$$\partial_i\big[-F(y)\big]=0 \qquad (y\text{만의 함수})$$

$$\partial_i\big[-F_a(y)(x^a-y^a)\big] \;=\; -F_a(y)\cdot\frac{\partial(x^a-y^a)}{\partial x^i} \;=\; -F_a(y)\,\delta^a_i \;=\; -F_i(y)$$

셋째 줄이 이 절의 전부다. **$F_a(y)$가 $x$에 무관하므로 곱의 미분에서 한 항만 살아남고**, 크로네커 델타가 합 $\sum_a$를 $a=i$ 하나로 접는다. 합치면

$$\boxed{\;\partial_iD=F_i(x)-F_i(y)\;}$$

**읽는 법.** 이것은 "$x$에서의 기울기와 $y$에서의 기울기의 차"다. $x=y$에서 0이 되는 것이 눈에 보인다 — 대각이 $D$의 최소점이라는 사실의 1계 표현. (검산 [01][04])

---

## §3. ② 혼합 2계 — $\partial_i\partial'_jD=-F_{ij}(y)$

### 3.1 $\partial_i$ 먼저

②에 $\partial'_j$를 건다. $F_i(x)$는 $y$에 무관해 죽고,

$$\partial'_j\big[F_i(x)-F_i(y)\big]=-F_{ij}(y)$$

$$\boxed{\;\partial_i\partial'_jD=-F_{ij}(y)\;}$$

### 3.2 $\partial'_j$ 먼저 — 다른 상쇄, 같은 답

**여기가 원문에 없는 교차검증이다.** 순서를 바꾸면 계산이 전혀 다르게 흘러간다. $y^j$로 먼저 미분하면 이번엔 곱의 미분에서 **두 항이 다 살아난다**:

$$\partial'_j\,F(x)=0$$
$$\partial'_j\big[-F(y)\big]=-F_j(y)$$
$$\partial'_j\big[-F_a(y)(x^a-y^a)\big] =\underbrace{-F_{aj}(y)(x^a-y^a)}_{F_a(y)\text{를 미분}} \;\underbrace{-\,F_a(y)\cdot(-\delta^a_j)}_{(x^a-y^a)\text{를 미분}} =-F_{aj}(y)(x^a-y^a)+F_j(y)$$

합치면 $-F_j(y)$와 $+F_j(y)$가 **정확히 상쇄**되어

$$\boxed{\;\partial'_jD=-F_{aj}(y)\,(x^a-y^a)\;}$$

이제 여기에 $\partial_i$를 걸면 $-F_{aj}(y)\delta^a_i=-F_{ij}(y)$ — **같은 답** ✓

두 경로가 구조적으로 다르다는 점이 핵심이다:

| 경로 | 곱의 미분에서 | 상쇄 | 결과 |
|---|---|---|---|
| $\partial_i$ 먼저 | 한 항만 생존 | 없음 | $F_i(x)-F_i(y)\;\to\;-F_{ij}(y)$ |
| $\partial'_j$ 먼저 | 두 항 생존 | $\mp F_j(y)$ 상쇄 | $-F_{aj}(x^a-y^a)\;\to\;-F_{ij}(y)$ |

(검산 [02][07][08] — 두 순서 모두 9성분 전부)

### 3.3 덤으로 얻는 것

$\partial'_jD=-F_{aj}(y)(x^a-y^a)$에서 $(x^a-y^a)$ 인자가 그대로 보이므로

$$D\big|_\Delta=0,\qquad \partial_iD\big|_\Delta=0,\qquad \partial'_jD\big|_\Delta=0$$

이 즉시 나온다 — 대각이 값·기울기 양쪽에서 임계점. (검산 [03][04][05])

---

## §4. ③ 대각 제한 — Hessian 계량

$y\to x$로 보내면 $-F_{ij}(y)\to-F_{ij}(x)$이므로

$$g_{ij}\;=\;-\,\partial_i\partial'_jD\,\Big|_{\Delta}\;=\;F_{ij}(x)$$

$$\boxed{\;\textbf{Bregman 기하의 계량 = }F\textbf{의 Hessian}\;}$$

대칭성 $g_{ij}=g_{ji}$는 $F_{ij}=F_{ji}$(2계 편미분의 교환)에서 자동, 양정치성은 $F$의 **강볼록**에서 나온다. (검산 [09][10])

---

## §5. 부호는 왜 마이너스인가 — 원문이 안 짚는 곳

원문은 $g_{ij}=-\partial_i\partial'_jD|_\Delta$의 마이너스를 그냥 쓴다. 이유는 이렇다.

$F$가 볼록이고 $D\ge0$이며 $x=y$가 최소점이므로, **첫 슬롯만으로 두 번** 미분하면 양반정치가 나온다:

$$\partial_i\partial_jD=F_{ij}(x)\;\succeq\;0$$

그런데 **슬롯을 하나씩 나눠** 미분하면 부호가 뒤집힌다:

$$\partial_i\partial'_jD=-F_{ij}(y)\;\preceq\;0$$

직관: $x$를 $y$에서 멀리 밀면 $D$가 커지지만, $y$를 $x$ 쪽으로 당기면 $D$가 **작아진다.** 두 슬롯이 서로 반대로 작용하므로 혼합 2계에 마이너스가 붙는다. 그래서 계량을 얻으려면 부호를 되돌려야 한다.

**가장 단순한 예로 확인.** $F=\tfrac12\|x\|^2$이면

$$D=\tfrac12\|x-y\|^2,\qquad \partial_i\partial'_jD=-\delta_{ij},\qquad -\partial_i\partial'_jD=\delta_{ij},\qquad \partial_i\partial_jD=+\delta_{ij}$$

유클리드 거리제곱의 절반이 나오고 계량은 $I$ ✓ (검산 [11][12][13][14])

> **왜 굳이 혼합 2계를 쓰나 — $\partial_i\partial_jD$로 하면 안 되나?**
> 계량만 원한다면 그래도 된다(둘 다 $F_{ij}$를 준다). 그러나 **§3.2의 connection들**은 3계 혼합 도함수 $\partial_i\partial_j\partial'_k D$와 $\partial'_i\partial'_j\partial_k D$로 정의되고, 이 둘이 **서로 다른** 두 접속을 준다. 두 슬롯을 처음부터 구분해 두어야 그 구조가 보인다. 계량 단계에서 슬롯을 구분하는 것은 그 준비다.

---

## §6. §3.1이 이미 §3.2를 준비해 두었다

§2에서 얻은 $\partial_i\partial_jD=F_{ij}(x)$를 다시 보자. **$y$가 전혀 들어 있지 않다.** 그러므로

$$\Gamma_{ij,k}=-\,\partial_i\partial_j\partial'_kD\,\Big|_\Delta=-\,\partial'_k\big[F_{ij}(x)\big]\Big|_\Delta=0$$

$$\boxed{\;x\text{-좌표에서 한쪽 connection이 사라진다}\;}$$

즉 **$x$는 $\nabla$에 대한 아핀좌표**다. 반면 $\partial_kD=F_k(x)-F_k(y)$에는 $y$가 남아 있어 $\Gamma^*\neq0$ — 이것이 원문 §3.2 제목 *"한 connection만 x-coordinates에서 사라진다"*의 내용이고, **§3.1의 계산이 이미 그 근거를 만들어 두었다.** (검산 [08])

이것이 노트 §1의 질문 *"확률분포에는 왜 두 종류의 직선이 필요한가"* 에 대한 첫 답이다: 한 좌표계에서 한쪽 직선만 곧게 펴지고, 다른 쪽 직선은 굽어 보인다.

---

## §7. §1의 $\tfrac12$ 규약과 맞물리는가 — factor 검산

노트 §1은 divergence의 2차 전개를

$$D[P_\xi:P_{\xi+d\xi}]=\tfrac12\,g_{ij}(\xi)\,d\xi^id\xi^j+O(\|d\xi\|^3)$$

로 쓴다. **여기의 $g$와 §3.1의 $g=-\partial\partial'D|_\Delta$가 같은 $g$인가?** 이 저장소의 규약상 factor는 반드시 확인한다.

$x=y+\Delta$를 넣고 테일러 전개하면

$$B_F[y+\Delta:y]=F(y+\Delta)-F(y)-F_a(y)\Delta^a =\tfrac12F_{ab}(y)\Delta^a\Delta^b+\tfrac16F_{abc}(y)\Delta^a\Delta^b\Delta^c+O(\Delta^4)$$

1계 항이 정의상 이미 빠져 있으므로 **2차항이 곧바로 $\tfrac12F_{ab}\Delta^a\Delta^b$**. 즉 $\tfrac12$ 규약의 $g_{ij}$가 정확히 $F_{ij}$이고, §3.1의 $g$와 **같다** ✓ (검산 [15][16])

$$\boxed{\;\text{factor 일치: 두 정의가 같은 }g\text{를 준다 (지뢰 없음)}\;}$$

### 덤 — §6.1의 예고가 여기서 보인다

방향을 뒤집어 $B_F[y:y+\Delta]$를 전개하면

$$B_F[y:y+\Delta]=\tfrac12F_{ab}\Delta^a\Delta^b+\tfrac13F_{abc}\Delta^a\Delta^b\Delta^c+O(\Delta^4)$$

**2차항은 같고 3차항이 다르다** ($\tfrac16$ vs $\tfrac13$, 차이 $\tfrac16F_{abc}\Delta^3$). 이것이 원문 §6.1 *"왜 second order는 divergence의 방향성을 잊는가?"* 의 답이다:

> **계량(2차)은 $D$의 비대칭성을 보지 못한다. 비대칭성은 3차에서 처음 나타나고, 그것이 두 connection이 갈라지는 자리다.**

$D[P:Q]\neq D[Q:P]$인데도 계량이 하나뿐인 이유, 그리고 굳이 3계 도함수까지 가야 하는 이유가 이 한 줄에 있다. (검산 [17][18])

---

## §8. 노트 자신의 예 — $g$가 Fisher 계량이다

§2.2의 음의 엔트로피

$$\varphi(\eta)=\sum_{a=0}^n p_a\log p_a,\qquad p_i=\eta_i,\quad p_0=1-\sum_{i=1}^n\eta_i$$

를 $F$ 자리에 넣는다.

### 8.1 기울기 — log-ratio 좌표가 나온다

$\partial p_0/\partial\eta_i=-1$에 주의하며 두 덩어리를 미분:

$$\frac{\partial}{\partial\eta_i}\big[p_0\log p_0\big]=(\log p_0+1)\cdot(-1)=-\log p_0-1$$
$$\frac{\partial}{\partial\eta_i}\big[\eta_i\log\eta_i\big]=\log\eta_i+1$$

더하면 $\pm1$이 상쇄되어

$$\boxed{\;\varphi_i=\log\frac{p_i}{p_0}\;}$$

**dual log-ratio 좌표가 저절로 나왔다** — 노트가 §1에서 예고한 그 좌표다. (검산 [20])

### 8.2 Hessian — Fisher 계량

한 번 더 미분한다. $\varphi_i=\log\eta_i-\log p_0$이므로

$$g_{ij}=\varphi_{ij}=\frac{\partial}{\partial\eta_j}\Big[\log\eta_i-\log p_0\Big] =\frac{\delta_{ij}}{\eta_i}-\frac{1}{p_0}\cdot(-1) =\frac{\delta_{ij}}{p_i}+\frac{1}{p_0}$$

이것이 정말 Fisher 계량인지 **정의로 완전히 독립 계산**해서 맞춘다:

$$g^{\text{Fisher}}_{ij}=\mathbb{E}\big[\partial_i\log p\,\partial_j\log p\big] =\sum_{a=0}^n\frac{1}{p_a}\frac{\partial p_a}{\partial\eta_i}\frac{\partial p_a}{\partial\eta_j} =\underbrace{\frac{\delta_{ij}}{p_i}}_{a=i\ \text{항}}+\underbrace{\frac{(-1)(-1)}{p_0}}_{a=0\ \text{항}} =\frac{\delta_{ij}}{p_i}+\frac{1}{p_0}\quad\checkmark$$

$a=0$ 항에서 마이너스가 **제곱되어** $+1/p_0$이 되는 것이 요점이다. (검산 [21][22])

### 8.3 구조와 양정치성

$$g=\operatorname{diag}\!\Big(\frac{1}{p_1},\dots,\frac{1}{p_n}\Big)+\frac{1}{p_0}\,\mathbf{1}\mathbf{1}^{\mathsf T}$$

**양정치 대각 + rank-1 양반정치** ⟹ 양정치. 한 점 $(p_1,p_2,p_3)=(\tfrac15,\tfrac14,\tfrac1{10})$에서 실베스터 판정으로 선행 주소행렬식 $[\tfrac{65}{9},\,40,\,\tfrac{4000}{9}]$ 전부 양수 ✓ (검산 [23][24])

그리고 §2.2의 주장 $B_\varphi[\eta(p):\eta(q)]=D_{\mathrm{KL}}[p:q]$도 한 점에서 확인했다 (검산 [25]).

---

## §9. 요약 — 네 줄이 실제로 담고 있던 것

| 원문 한 줄 | 실제 내용 |
|---|---|
| $\partial_iD=F_i(x)-F_i(y)$ | $F_a(y)$가 $x$에 상수 ⟹ 곱의 미분에서 한 항, $\delta^a_i$가 합을 접음 (§2) |
| $\partial_i\partial'_jD=-F_{ij}(y)$ | 순서를 바꾸면 $\mp F_j(y)$ 상쇄를 거쳐 같은 답 (§3) |
| $g_{ij}=-\partial_i\partial'_jD\|_\Delta=F_{ij}$ | 마이너스는 두 슬롯이 반대로 작용하기 때문 (§5) |
| *(원문에 없음)* | $\partial_i\partial_jD$가 $y$에 무관 ⟹ §3.2의 $\Gamma=0$ (§6) |
| *(원문에 없음)* | §1의 $\tfrac12$ 규약과 factor 일치; 비대칭은 3차에서 (§7) |

### 다음

- **IG2**: §3.2 — 두 connection $\Gamma_{ij,k}$, $\Gamma^*_{ij,k}$과 "한쪽만 사라진다"
- **IG3**: §4 — Gaussian에서 moments ↔ log-density 계수
- 걸음 5(QFIM)와의 접속: 고전 Fisher와 양자 Fisher의 factor 관계 (기존 지뢰 "FS vs QFIM 4배"와 이어짐)

### 검산

```
pip install sympy
python 정보기하/verify_ig1_bregman.py     # 25/25
```

임의의 매끄러운 $F$(미정의 함수)로 ①②③을 기호 검산하고, 3차까지의 주장은 **계수가 임의 기호인 일반 3차 다항식**으로 검산한다(임의의 매끄러운 $F$는 3차까지 자기 테일러 다항식과 일치하므로 일반성을 잃지 않는다).
