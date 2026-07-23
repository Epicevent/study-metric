# 차트 갈아타기 — $z'=1/z$에서 $Z'=Z^{-1}$로

> **이 문서가 무엇인가.** [사전](사전_1z에서_IZ로.html) §9의 4번 — "차트 갈아타기 실물: $Z'=Z^{-1}$ 판을 실제로 계산해서 $K$·$g$가 어떻게 변환되는지, ℂP¹의 $z'=1/z$와 나란히" — 를 닫는다. 그리고 하나 더: 갈아타 보니 **$k=1$에는 아예 없던 전이**(혼합 차트)가 처음 나타난다.
> **검산.** `verify_chart_change.py` — **15/15 통과**. 본문 [X*]는 그 검산 번호.

---

## §1. ℂP¹ 복습 — 세 줄이면 끝나던 것

차트 2개: $v_1\ne0$에서 $(1,z)$, $v_2\ne0$에서 $(z',1)$. 겹치는 곳($z\ne0$)에서:

**① 전이는 게이지다.** $(1,z)\cdot\underbrace{\tfrac1z}_{\lambda}=(\tfrac1z,1)=(z',1)$, 즉 $z'=1/z$ — 스칼라배 하나로 갈아탄다. $\lambda=1/z$는 겹침 위에서 **정칙**.

**② $K$는 $|\lambda|^2$배.** $K'=1+|z'|^2=\dfrac{K}{|z|^2}$ [X1a]. 퍼텐셜은 $\log K'=\log K-\log|z|^2$로 어긋나지만, $\log|z|^2=\log z+\log\bar z$ (정칙+반정칙)이라 $\partial\bar\partial$가 죽인다 [X1b] — $\omega$는 두 차트에서 같은 것.

**③ 계량은 텐서로 불변.** $dz'=-dz/z^2$이므로 $g'\,|dz'|^2=\dfrac{|z|^4}{K^2}\cdot\dfrac{|dz|^2}{|z|^4}=\dfrac{|dz|^2}{K^2}=g\,|dz|^2$ [X1c].

이 세 줄을 Gr(2,4)에서 재현하는 것이 이 문서다.

---

## §2. 풀스왑 — $Z'=Z^{-1}$, 역수의 행렬 승격

행 $\{3,4\}$를 항등 블록으로 쓰는 차트로 갈아탄다. 게이지는 $G=Z^{-1}$ ($\det Z\ne0$일 때, 겹침 위에서 정칙):

$$\begin{pmatrix}I\\Z\end{pmatrix}\cdot Z^{-1}=\begin{pmatrix}Z^{-1}\\I\end{pmatrix}
\qquad\Longrightarrow\qquad \boxed{\ Z'=Z^{-1}\ }\tag{[X2a]}$$

$z'=1/z$가 문자 그대로 $1\times1$ 판이다. 사영자는 그대로 [X2b] — 같은 2-평면의 두 이름.

**② $K$는 $|\det G|^2$배.** 실베스터 한 줄:

$$K'=\det\!\big(I+Z'^\dagger Z'\big)=\det\!\big(I+(ZZ^\dagger)^{-1}\big)
=\frac{\det(I+ZZ^\dagger)}{\det(ZZ^\dagger)}
=\boxed{\ \frac{K}{|\det Z|^2}\ }\tag{[X3]}$$

퍼텐셜 어긋남은 $\log|\det Z|^2=\log\det Z+\log\overline{\det Z}$ — 정칙+반정칙. 혼합미분 16개가 전부 0 [X4]. **6ab의 "퍼텐셜은 공짜가 아니다"가 여기서 실물이 된다**: $K$는 차트마다 다르지만 $\omega=\tfrac{i}{2}\partial\bar\partial\log K$는 갈아타도 그대로.

---

## §3. 계량 불변 — 밀어넘기기 세 번

**③의 행렬판.** 접벡터부터: $Z'=Z^{-1}$을 미분하면

$$dZ'=-Z^{-1}\,dZ\,Z^{-1}$$

— $dz'=-dz/z^2$의 승격이다 (행렬이라 $Z^{-1}$이 **양쪽에서** 낀다). 이제 $F'=I+Z'^\dagger Z'$, $G'=I+Z'Z'^\dagger$를 원래 것으로 표현한다:

$$Z'^\dagger Z'=(ZZ^\dagger)^{-1}\ \Longrightarrow\ F'=(ZZ^\dagger)^{-1}G\ \Longrightarrow\ F'^{-1}=G^{-1}ZZ^\dagger,$$
$$Z'Z'^\dagger=(Z^\dagger Z)^{-1}\ \Longrightarrow\ G'=(Z^\dagger Z)^{-1}F\ \Longrightarrow\ G'^{-1}=F^{-1}Z^\dagger Z.$$

대입하고 정리한다:

$$\mathrm{tr}\big[F'^{-1}\,dZ'^\dagger\,G'^{-1}\,dZ'\big]
=\mathrm{tr}\big[G^{-1}ZZ^\dagger\cdot Z^{-\dagger}dZ^\dagger Z^{-\dagger}\cdot F^{-1}Z^\dagger Z\cdot Z^{-1}dZ\,Z^{-1}\big]$$

$ZZ^\dagger Z^{-\dagger}=Z$, $Z^\dagger Z\,Z^{-1}=Z^\dagger$로 접고, 순환으로 마지막 $Z^{-1}$을 앞으로 돌리면

$$=\mathrm{tr}\big[\,\underbrace{Z^{-1}G^{-1}Z}_{=F^{-1}}\cdot dZ^\dagger\cdot\underbrace{Z^{-\dagger}F^{-1}Z^\dagger}_{=G^{-1}}\cdot dZ\,\big]
=\mathrm{tr}\big[F^{-1}dZ^\dagger G^{-1}dZ\big].$$

쓰인 것은 밀어넘기기 두 개뿐이다 — 6b §6.2의 그 도구:

$$ZF=GZ\ \Rightarrow\ F^{-1}=Z^{-1}G^{-1}Z\quad[\text{X5a}],\qquad
FZ^\dagger=Z^\dagger G\ \Rightarrow\ F^{-1}Z^\dagger=Z^\dagger G^{-1}\quad[\text{X5b}]$$

$$\boxed{\ \mathrm{tr}\big[F'^{-1}dZ'^\dagger G'^{-1}dZ'\big]=\mathrm{tr}\big[F^{-1}dZ^\dagger G^{-1}dZ\big]\ }\tag{[X6a]}$$

세스퀴선형 판(서로 다른 두 접벡터 $U,W$)도 그대로 성립하므로 [X6b], **실부(계량 = QFIM/4)만이 아니라 허부($\omega$)까지 통째로** 차트 무관이다. $k=1$로 줄이면 §1의 ③ 세 줄이 된다 — 모든 행렬이 $1\times1$이라 밀어넘기기가 자명해질 뿐.

---

## §4. $k=1$에는 없던 것 — 혼합 차트

ℂP¹은 차트가 2개라 전이가 $z'=1/z$ **하나**뿐이다. Gr(2,4)는 차트가 6개고, 풀스왑($\{1,2\}\to\{3,4\}$) 말고 **행을 하나만 바꾸는 전이**가 있다. $\{1,3\}$ 차트로 가 보자 (유효조건: 행 $\{1,3\}$ 소행렬식 $=p_{13}=b\ne0$):

$$G=\begin{pmatrix}1&0\\a&b\end{pmatrix}^{-1}
\qquad\Longrightarrow\qquad
Z'=\begin{pmatrix}-a/b & 1/b\\[2pt] -\det Z/b & d/b\end{pmatrix}\tag{[X7a]}$$

읽을 것 세 가지:

1. **분모가 전부 $p_{13}=b$다.** 사전 §3의 "차트 유효 ⟺ 해당 소행렬식 $\ne0$"이 전이함수의 분모로 실물화된다.
2. **성분이 섞인다.** $1/b$ 같은 단순 역수와 $\det Z/b$ 같은 소행렬식 비율이 한 행렬에 공존 — 스칼라 역수($1/z$)로는 흉내낼 수 없는, 순수하게 $k\ge2$의 현상.
3. **메커니즘은 동일.** $\det G=1/b$이므로 $K'=K/|p_{13}|^2$ [X7b], 퍼텐셜 어긋남은 $\log|p_{13}|^2$ (정칙+반정칙 → $\omega$ 무사), 계량도 불변 [X7c — 곡선 $Z(t)$를 실제로 갈아태워 $t=0$에서 미분, 정확산술].

---

## §5. 전역 그림 — 코시–비네가 여섯 차트를 한 식으로

세 차트에서 확인한 $K$들을 한 줄에 놓으면 패턴이 보인다 [X8]:

$$K_{\{1,2\}}=\frac{\sum_{ij}|p_{ij}|^2}{|p_{12}|^2},\qquad
K_{\{3,4\}}=\frac{\sum|p_{ij}|^2}{|p_{34}|^2},\qquad
K_{\{1,3\}}=\frac{\sum|p_{ij}|^2}{|p_{13}|^2}.$$

**분자는 차트 무관**(플뤼커 노름² — 코시–비네, 사전 §4.2)이고, **분모만 "내 차트의 소행렬식"**이다. 그래서 임의의 두 차트 사이에서

$$\frac{K_A}{K_B}=\left|\frac{p_B}{p_A}\right|^2,\qquad \frac{p_B}{p_A}\ \text{는 겹침 위에서 정칙}$$

— 전이가 뭐든(풀스왑이든 혼합이든) 퍼텐셜 어긋남은 항상 $\log|\text{정칙}|^2$이고 $\omega$는 항상 무사하다. ℂP¹ 판: $K=\dfrac{|v_1|^2+|v_2|^2}{|v_1|^2}$, 분모가 $|p_{\text{내 차트}}|^2=|v_1|^2$. **같은 문장.**

(6f의 언어로: 각 차트의 $\log K$는 "차트마다의 각도 $\theta$"이고, 어긋남 $\log|p_B/p_A|^2$가 "감김"이며, $\omega$가 "전역인 $d\theta$"다.)

---

## §6. 닫힘

사전 §9의 4번이 닫혔다. 확정된 문장:

> 차트 갈아타기는 ℂP¹에서나 Gr(2,4)에서나 **정칙 게이지 하나**다: $\lambda=1/z\ \to\ G=Z^{-1}$ (또는 혼합 차트의 부분 역행렬). $K$는 $|\det G|^2$배로 어긋나고 $\partial\bar\partial$가 그 어긋남을 죽이며, 계량·$\omega$는 밀어넘기기 두 번으로 문자 그대로 불변. $k\ge2$에서 새로 생기는 것은 **혼합 차트**뿐이고, 그마저 같은 메커니즘이다.

남은 것: **5번**($k=1$ 겹침 전수조사) 하나.

---

## 부록. 검산 대조표

| 번호 | 무엇 | 방법 |
|---|---|---|
| X1a–c | ℂP¹ 세 줄 ($K'=K/\lvert z\rvert^2$, $\partial\bar\partial\log\lvert z\rvert^2=0$, $g$ 불변) | 기호 |
| X2a,b | $(I;Z)Z^{-1}=(Z^{-1};I)$, 사영자 불변 | 무작위 정확산술 |
| X3 | $K'=K/\lvert\det Z\rvert^2$ | 무작위 정확산술 ×3 |
| X4 | $\partial\bar\partial\log\lvert\det Z\rvert^2=0$ (16개) | 기호 |
| X5a,b | 밀어넘기기 $F^{-1}=Z^{-1}G^{-1}Z$, $F^{-1}Z^\dagger=Z^\dagger G^{-1}$ | 무작위 정확산술 |
| X6a,b | 계량·세스퀴(=$\omega$ 포함) 불변 | 무작위 정확산술 |
| X7a–c | 혼합 차트 $Z'$ 성분식·$p_{13}$ 분모·$K'$·계량 불변 | 무작위 정확산술 + 곡선 미분 |
| X8 | $K_{\text{chart}}=\sum\lvert p\rvert^2/\lvert p_{\text{chart}}\rvert^2$ (세 차트) | 무작위 정확산술 |

```
python verify_chart_change.py     # 15/15
```
