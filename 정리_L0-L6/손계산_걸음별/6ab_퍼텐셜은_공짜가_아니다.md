# 6ab — 퍼텐셜은 공짜가 아니다

> **읽는 자리: `6a`와 `6b` 사이.** `6b` §1은 "$K=\sum|p_{ij}|^2$을 대입하면 켈러 퍼텐셜, 켈러성은 공짜"라고 넘어갔다. 그 문장은 **틀렸다** — 정확히 말하면 *공짜인 부분과 절대 공짜가 아닌 부분을 뭉갰다.*
> 이 문서는 뭉갠 것을 갈라 세운다. 결론부터: **$K$는 $\mathrm{Gr}(2,4)$ 위의 함수가 아니다.** 함수일 수 **없다** — 그리고 그 사실의 증명은 이미 우리가 계산해 둔 값 하나에서 나온다.
> 검산: `verify6_plucker.py` PART 4b

---

## §0. 공짜일 수 없다는 증명 — 우리가 이미 잰 값으로

$K$가 만약 $\mathrm{Gr}(2,4)$ 위에 잘 정의된 매끄러운 함수라고 하자. 그러면 $u:=\log K$도 전역 함수다. 이때 $\omega=\frac{i}{2}\partial\bar\partial u$는 **완전형식(exact)**이 된다. 실제로 $d=\partial+\bar\partial$이고 $\partial^2=\bar\partial^2=0$이므로

$$d\Big[\tfrac{i}{4}\big(\bar\partial u-\partial u\big)\Big] =\tfrac{i}{4}\big(\partial\bar\partial u-\bar\partial\partial u\big) =\tfrac{i}{4}\cdot 2\,\partial\bar\partial u =\tfrac{i}{2}\partial\bar\partial u=\omega.$$

*(중간 줄: $\bar\partial\partial u=-\partial\bar\partial u$.)* 그런데 $\mathrm{Gr}(2,4)$ 안의 생성 $\mathbb{CP}^1$은 **경계 없는 콤팩트 곡면**이므로 스토크스에 의해

$$\int_{\mathbb{CP}^1}\omega=\int_{\mathbb{CP}^1}d(\cdots)=0.$$

그런데 6c §1.1에서 우리는 **직접 적분해서** $\int_{\mathbb{CP}^1}\omega=\pi\neq0$을 얻었다.

$$\boxed{\;\text{모순. 따라서 }K\text{는 }\mathrm{Gr}(2,4)\text{ 위의 함수일 수 없다.}\;}$$

이것이 사용자의 지적이 옳은 이유의 전부다. **퍼텐셜이 공짜로 주어질 수 있었다면 그 다양체 위의 켈러류는 항상 0이었을 것이고, 6c의 부피 계산(=차수 2)도 통째로 무너진다.** $\int\omega=\pi$라는 0 아닌 값이 곧 "퍼텐셜은 전역적으로 존재하지 않는다"의 증서다.

> **뒤집어 읽기.** 콤팩트 켈러 다양체에서 켈러 형식은 **절대로** 전역 퍼텐셜을 갖지 않는다($[\omega]\neq0$이므로). 퍼텐셜은 언제나 **국소적**이다. 우리가 $\mathbb{CP}^1$에서 $K=1+|z|^2$을 아무 죄책감 없이 써 온 것도 사실은 **차트 하나에서만** 쓴 것이었다 — 걸음 2에서 그냥 지나간 지점이다.

---

## §1. 무슨 일이 실제로 일어났나 — $K$는 게이지에 걸린다

6a §2.2의 관찰을 다시 보자. 평면 $W$의 대표 $A$를 $gA$로 바꾸면

$$p_{ij}\longmapsto (\det g)\,p_{ij} \qquad\Longrightarrow\qquad K=\sum|p_{ij}|^2\longmapsto |\det g|^2\,K.$$

**$K$는 평면의 함수가 아니라 대표 $A$의 함수다.** 6a에서 소행렬식의 *비율*만이 평면의 함수라고 했던 그 이야기가, 퍼텐셜 층위에서 되돌아온 것이다. $|p_{ij}|^2$의 합은 비율이 아니므로 살아남지 못한다.

그렇다면 6b에서 우리가 쓴 $K=1+|a|^2+\cdots+|ad-bc|^2$은 무엇이었나? **차트 $(I\mid Z)$로 게이지를 고정한 뒤의 값**이다. 즉 $p_{12}=1$로 정규화한 대표에서 잰 값이고, 차트를 바꾸면 값이 바뀐다.

$$K^{(12)}(Z)=\sum_{i<j}\left|\frac{p_{ij}}{p_{12}}\right|^2 \qquad\text{— 이것이 6b의 } K.$$

**정직한 문장.** $K$는 *퍼텐셜*이지 *함수*가 아니다. 이 구분을 빼면 6c의 위상 논증($[\omega]=\pi\sigma_1$, 부피=차수, Fano 지수)이 전부 근거를 잃는다.

---

## §2. 그런데도 $\omega$는 살아남는다 — 유일한 이유

퍼텐셜이 차트마다 다른데 왜 $\omega=\frac{i}{2}\partial\bar\partial\log K$는 잘 정의되나? 차이가 **정확히 $\log|\text{정칙}|^2$ 꼴**이고, 그 꼴은 $\partial\bar\partial$가 죽이기 때문이다.

**보조정리.** $f$가 정칙이고 영점이 없으면 $\partial\bar\partial\log|f|^2=0$.

*증명.* 국소적으로 $\log|f|^2=\log f+\log\bar f$. $f$가 정칙이므로 $\bar\partial\log f=0$, 따라서 $\partial\bar\partial\log f=0$. $\bar f$가 반정칙이므로 $\partial\log\bar f=0$, 따라서 $\partial\bar\partial \log\bar f = \partial(\bar\partial\log\bar f)$인데 $\bar\partial\log\bar f = \overline{\partial \log f}$는 반정칙이므로 $\partial$가 죽인다. 합해서 0. $\blacksquare$

*(가지(branch) 선택이 걸리면: $\partial\bar\partial\log|f|^2 = \partial\bar\partial\log(f\bar f)$를 $\bar\partial(\partial f/f)=0$로 직접 봐도 된다. 어차피 $\partial\bar\partial$는 가지에 무관.)*

$$\boxed{\;K'=|f|^2K\;(f\text{ 정칙, 무영점}) \quad\Longrightarrow\quad \tfrac{i}{2}\partial\bar\partial\log K'=\tfrac{i}{2}\partial\bar\partial\log K\;}$$

**이 한 줄이 이 문서의 심장이다.** 아래 §3(차트 갈아타기)과 §6(대칭군 작용) 두 곳에서 *같은* 메커니즘이 쓰인다.

---

## §3. 두 차트에서 명시적으로

$p_{12}\neq0$ 차트와 $p_{13}\neq0$ 차트가 겹치는 곳($c=p_{13}\neq0$)에서 실제로 확인하자.

$A=(I\mid Z)=\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}$의 **1,3열** 블록은 $M=\begin{pmatrix}1&a\\0&c\end{pmatrix}$, $\det M=c=p_{13}$. 이 블록을 단위로 만드는 대표는 $A'=M^{-1}A$이고, 6a §2.2에 의해

$$p_{ij}(A')=\frac{p_{ij}(A)}{\det M}=\frac{p_{ij}}{c} \qquad\Longrightarrow\qquad K^{(13)}=\frac{K^{(12)}}{|c|^2}.$$

$$\boxed{\;K^{(12)}=|c|^2\,K^{(13)},\qquad c=p_{13}/p_{12}\ \text{정칙·무영점}\;}$$

§2의 보조정리로 두 차트의 $\omega$가 일치한다. (`verify6_plucker.py`: $K^{(13)}=K/|p_{13}|^2$과 $\partial\bar\partial\log|c|^2=0$ 둘 다 성분으로 확인)

**여기서 6a의 "차트 6장"이 값을 한다.** 6장 각각이 자기 퍼텐셜 $K^{(ij)}$를 갖고, 겹치는 곳에서 $|{\cdot}|^2$배로 이어 붙는다. $\omega$ 하나가 그 6장 위에서 한 덩어리로 정의된다.

---

## §4. 이 구조의 이름 — 선다발 위의 계량, $\omega$는 그 곡률

$\{K^{(\alpha)}\}$가 겹침에서 $K^{(\alpha)}=|g_{\alpha\beta}|^2K^{(\beta)}$ ($g_{\alpha\beta}$ 정칙 무영점)로 이어지는 것 — 이것이 **정칙 선다발 위의 에르미트 계량**의 정의 그 자체다. 우리 경우 그 선다발은 플뤼커로 당겨온 $\mathcal{O}(1)$(초평면 다발)이고, $\sum|p_{ij}|^2$은 $\Lambda^2\mathbb{C}^4$의 표준 에르미트 내적이 유도한 계량이다.

그리고 $\omega=\frac{i}{2}\partial\bar\partial\log K$는 그 계량의 **곡률**(의 상수배)이며, 그 코호몰로지류가 제1 천류다:

$$\Big[\frac{\omega}{\pi}\Big]=c_1\big(\varphi^*\mathcal{O}(1)\big)=\sigma_1\in H^2\big(\mathrm{Gr}(2,4);\mathbb{Z}\big).$$

**6c에서 공짜로 쓴 것들이 전부 여기 있었다.**

| 6c에서 쓴 문장 | 실제 근거 |
|---|---|
| "$\omega$는 닫힌 형식" | $\partial^2=\bar\partial^2=0$ (§0에서 확인) — 이건 진짜 공짜 |
| "$[\omega]$는 $h$의 상수배" | $\omega/\pi$가 정수류 $\sigma_1$을 대표 (위 식) + $H^2(\mathrm{Gr})=\mathbb{Z}\sigma_1$ |
| "상수는 $\int_{\mathbb{CP}^1}\omega=\pi$로 고정" | $\sigma_1$이 생성 직선과 1로 짝지음 |
| "$\mathrm{Ric}=4g$의 4 = Fano 지수" | $\det g=K^{-4}$ ⟹ 반표준다발 계량이 $K^{-4}$ ⟹ $c_1(\mathrm{Gr})=4\sigma_1$ |

**정직한 표시.** $H^2(\mathrm{Gr}(2,4);\mathbb{Z})=\mathbb{Z}\sigma_1$은 이 문서가 **유도하지 않고 가져다 쓰는 입력**이다 (슈베르트 세포 분해에서 나온다: 2차원 세포가 $\sigma_1$ 하나뿐). 6c §1.4의 "부피=차수" 논증은 이 입력 위에 서 있다.

---

## §5. 양정치성도 공짜가 아니다

6b §1은 "복소 부분다양체의 접공간은 $J$-불변이라 제한해도 계량"이라고 했다. 이건 **$\omega_{FS}$가 이미 양정치라는 것을 전제**한 문장이다. 우리 손으로 확인하는 편이 낫고, 실제로 6b §6.3의 자취 형태가 **한 줄 증명**을 준다.

$$ds^2=\mathrm{tr}\big(F^{-1}\,dZ^\dagger\,G^{-1}\,dZ\big),\qquad F=I+Z^\dagger Z,\quad G=I+ZZ^\dagger.$$

$F,G$는 에르미트 양정치다 ($I$에 $M^\dagger M$꼴을 더한 것). 그러므로 양의 제곱근 $F^{1/2},G^{1/2}$과 그 역이 존재한다. 이제

$$X:=G^{-1/2}\,dZ\,F^{-1/2}$$

로 두면, 자취의 순환성으로

$$\mathrm{tr}\big(X^\dagger X\big) =\mathrm{tr}\big(F^{-1/2}dZ^\dagger G^{-1/2}\cdot G^{-1/2}dZ F^{-1/2}\big) =\mathrm{tr}\big(F^{-1}dZ^\dagger G^{-1}dZ\big)=ds^2.$$

그런데 $\mathrm{tr}(X^\dagger X)=\sum_{i,j}|X_{ij}|^2$이므로

$$\boxed{\;ds^2=\sum_{i,j}|X_{ij}|^2\;\ge\;0,\qquad =0\iff X=0\iff dZ=0.\;}$$

**양정치 증명 끝.** 계산이 아니라 구조에서 나왔고, 차원에 무관하므로 모든 $\mathrm{Gr}(k,n)$에서 그대로 성립한다. (`verify6_plucker.py`: 무작위 200점에서 $g$의 최소 고유값 $>0$, 그리고 위 자취 항등식을 무작위 50점에서 확인)

---

## §6. 제일 중요한 질문 — **왜 하필 이 $K$인가**

여기까지 와도 남는 의문이 있다. $\Lambda^2\mathbb{C}^4$ 위의 에르미트 내적으로 $\sum|p_{ij}|^2$을 **고른 것은 선택**이다. 다른 내적을 골랐다면 다른 계량이 나온다. 왜 이것인가? 노트도, 6b도 이 질문을 건드리지 않았다.

**답: 대칭이 고른다.**

### 6.1 $U(4)$가 차트에 어떻게 작용하나

$\mathbb{C}^4$의 유니터리 변환 $u$는 2-평면을 2-평면으로 보내므로 $\mathrm{Gr}(2,4)$에 작용한다. 대표로는 $A\mapsto Au^{\mathsf T}$. $u^{\mathsf T}$를 2×2 블록으로 쪼개 $\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$라 하면

$$(I\mid Z)\,u^{\mathsf T}=\big(\alpha+Z\gamma\;\big|\;\beta+Z\delta\big) =(\alpha+Z\gamma)\big(I\mid Z'\big), \qquad \boxed{\;Z'=(\alpha+Z\gamma)^{-1}(\beta+Z\delta)\;}$$

— **분수선형 작용**. ($\mathbb{CP}^1$에서 $z\mapsto\frac{\beta+z\delta}{\alpha+z\gamma}$였던 뫼비우스 변환의 행렬판. 걸음 2의 그 작용이 2×2로 올라온 것.)

### 6.2 그러면 $K$는 어떻게 변하나 — §2와 **똑같은** 메커니즘

$u$가 유니터리면 $\Lambda^2u^{\mathsf T}$도 $\Lambda^2\mathbb{C}^4$에서 유니터리이므로, **정규화하지 않은** 대표에서는 $\sum|p_{ij}|^2$이 보존된다. 그런데 위 식이 보여주듯 $(I\mid Z)u^{\mathsf T}$는 $(I\mid Z')$의 $(\alpha+Z\gamma)$배다. 6a §2.2로

$$p\big((I\mid Z)u^{\mathsf T}\big)=\det(\alpha+Z\gamma)\cdot p\big((I\mid Z')\big)$$

이고, 노름을 취하면

$$\boxed{\;K(Z)=\big|\det(\alpha+Z\gamma)\big|^2\;K(Z')\;}$$

$\det(\alpha+Z\gamma)$는 $Z$의 **정칙** 함수다. 따라서 §2의 보조정리로

$$\omega(Z)=\tfrac{i}{2}\partial\bar\partial\log K(Z) =\tfrac{i}{2}\partial\bar\partial\log K(Z')=\omega(Z').$$

$$\boxed{\;\omega\text{는 }U(4)\text{-불변이다.}\;}$$

(`verify6_plucker.py`: $u$를 좌표 1,3의 회전 $(3/5,4/5)$로 잡아 분수선형 작용과 위 항등식을 기호로 확인)

**한 메커니즘, 두 용도.** $\log|\text{정칙}|^2$이 죽는다는 사실이 (i) 차트 무관성(§3)과 (ii) 대칭 불변성(§6.2)을 동시에 준다. 노트가 "복소 부분다양체는 공짜로 켈러"라는 한 문장으로 덮어버린 자리에 실제로 있던 구조가 이것이다.

### 6.3 유일성 — 그래서 이 $K$가 "그" $K$다

$\mathrm{Gr}(2,4)$는 $U(4)$의 등질공간이고, 한 점(예: $Z=0$)의 등방부분군은 $U(2)\times U(2)$다. 그 점의 접공간은

$$T\cong \mathrm{Hom}(\mathbb{C}^2,\mathbb{C}^2)=(\mathbb{C}^2)^*\otimes\mathbb{C}^2$$

이고, $U(2)\times U(2)$의 표현으로서 **기약**이다(두 기약표현의 외부텐서곱). 게다가 중심의 원 $(e^{i\theta}I,\,I)$이 $T$ 위에서 복소 스칼라배로 작용하므로, 불변 리만계량은 자동으로 에르미트형식의 실부이고, 슈어 보조정리로 **양의 상수배를 빼면 유일**하다.

$$\boxed{\;U(4)\text{-불변 켈러 계량은 상수배를 빼면 유일하다.}\;}$$

이 한 줄이 세 가지를 한꺼번에 해결한다.

1. **선택의 자의성 해소.** $\sum|p_{ij}|^2$을 고른 것이 자의적으로 보였지만, 그것이 $U(4)$-등변인 이상 **결과는 유일한 불변계량**일 수밖에 없다. 다른 $U(4)$-등변 구성을 해도 상수배만 다르다.
2. **노트 §6 ③의 근거.** 노트는 길 1(Reeb)로 내려온 형식이 "§3의 $g$와 상수배로 일치해야 하고, 상수는 생성 $\mathbb{CP}^1$ 위 적분값 $\pi$ 하나로 고정한다"고 썼는데 **왜 상수배인지는 말하지 않았다.** 이유가 이 유일성이다: 두 길 모두 $U(4)$-등변이므로 같은 불변계량을 상수배 차이로 만든다. 그래서 숫자 하나($\int_{\mathbb{CP}^1}=\pi$)면 맞춤이 끝난다.
3. **$\mathrm{Ric}=4g$의 재해석.** 아인슈타인 조건 $\mathrm{Ric}=\lambda g$는 사실 **강제**다 — $\mathrm{Ric}$도 $U(4)$-불변 대칭 2-텐서이므로 유일성에 의해 $g$의 상수배일 수밖에 없다. 6b §7의 계산이 한 일은 "아인슈타인이다"가 아니라 **그 상수가 4임을 정하는 것**이었다.

> **주의(정직).** 위 유일성 논증은 "불변 계량"의 유일성이지, "$\omega$가 켈러(닫힘+양정치)"까지 공짜로 준다는 뜻은 아니다. 닫힘은 §0, 양정치는 §5에서 각각 따로 확보했다.

---

## §7. 그래서 무엇이 공짜였고 무엇이 아니었나

| 주장 | 공짜? | 근거 |
|---|---|---|
| $\omega$가 닫힌 형식 | **공짜** | $\partial^2=\bar\partial^2=0$ (§0) |
| $\omega$가 (1,1)형식 | **공짜** | $\partial\bar\partial$의 형태 |
| $K$가 전역 함수 | **거짓** | §0 스토크스 모순 |
| $\omega$가 잘 정의됨 | 아님 | $\partial\bar\partial\log|f|^2=0$ 필요 (§2–3) |
| $\omega$가 양정치 | 아님 | 자취 형태 $\sum|X_{ij}|^2$ (§5) |
| 하필 이 $K$인 이유 | 아님 | $U(4)$-등변 + 불변계량 유일성 (§6) |
| $[\omega]=\pi\sigma_1$ | 아님 | 선다발 계량의 곡률 + $H^2=\mathbb{Z}\sigma_1$(외부 입력) (§4) |
| 길 1 = 길 2 (상수배) | 아님 | 불변계량 유일성 (§6.3) |
| $\mathrm{Ric}=\lambda g$ (아인슈타인) | **거의 공짜** | 유일성으로 강제; 계산은 $\lambda=4$를 정할 뿐 (§6.3) |

---

## §8. 앞뒤 문서 정정

- **`6b` §1**: "켈러성은 공짜"는 **닫힘에만** 해당한다. 양정치는 §5로, 퍼텐셜의 전역 부재는 §0으로, $K$의 선택 근거는 §6으로 대체할 것.
- **`6b` §2**: "$K=\sum|p_{ij}|^2$" 앞에 **"차트 $(I\mid Z)$에서"**를 반드시 붙일 것. 문장 그대로는 정의되지 않는다.
- **`6c` §1.4**: "$[\omega]$는 $h$의 상수배"는 §4의 선다발 논증 + $H^2(\mathrm{Gr})=\mathbb{Z}\sigma_1$(외부 입력)에 근거한다.
- **`6c` §3.1** 표의 마지막 줄("$d\alpha$가 내려간다"): 왜 상수배로 일치하는지는 §6.3이 답한다.

**손계산 9.** ① $\mathbb{CP}^1$에서 두 차트 $z$와 $w=1/z$의 퍼텐셜을 각각 적고, $K_z=|w|^{-2}\cdot\!$… 꼴로 이어짐을 확인하라 (즉 $1+|z|^2=|z|^2(1+|w|^2)$). ② 그 차이가 $\log|z|^2$이고 $\partial\bar\partial\log|z|^2=0$($z\neq0$)임을 확인하라. ③ 그러므로 $\mathbb{CP}^1$에서도 퍼텐셜은 전역적이지 않았음을, 그리고 $\int\omega=\pi\neq0$이 그것을 강제함을 한 문단으로 쓰라. *(걸음 2에서 지나간 자리를 메우는 과제다.)*
