# ℂP¹에서 두 벌로 계산하기 — $A\to dA$와 $Q\to(\operatorname{Re}Q,\operatorname{Im}Q)$

<style>
:root{--lane-a:#9a492f;--lane-a-soft:#fff5ed;--lane-a-line:#e9c2ae;--lane-q:#315d8f;--lane-q-soft:#f1f6fc;--lane-q-line:#b9d0e8;--merge:#315f4d;--merge-soft:#eff8f3}
@media (prefers-color-scheme:dark){:root{--lane-a:#f0a37f;--lane-a-soft:#2d2420;--lane-a-line:#704a39;--lane-q:#91bce8;--lane-q-soft:#202832;--lane-q-line:#3e5b78;--merge:#9bd0b8;--merge-soft:#202c27}}
main,header.titlepage{max-width:78rem}
header.titlepage{padding-top:2.7em}
header.titlepage h1{max-width:31em;margin:.25em auto;font-size:1.85em}
.opening{max-width:66rem;margin:0 auto 2.2rem;font-size:1.05em}
.rule-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;margin:1.5rem 0 2.5rem}
.rule{border:1px solid var(--line);border-radius:10px;background:var(--card);padding:.8rem 1rem;min-width:0}
.rule b{display:block;font-size:.78em;letter-spacing:.08em;color:var(--muted);margin-bottom:.2rem}
.tracks{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.6rem 0 1rem}
.track-title{border-radius:12px;padding:1rem 1.2rem;color:var(--fg);border:1px solid}
.track-title.a{background:var(--lane-a-soft);border-color:var(--lane-a-line)}
.track-title.q{background:var(--lane-q-soft);border-color:var(--lane-q-line)}
.track-title strong{display:block;font-size:1.18em;margin-bottom:.15rem}
.track-title.a strong{color:var(--lane-a)}
.track-title.q strong{color:var(--lane-q)}
.track-title span{color:var(--muted);font-size:.9em}
.stage{display:grid;grid-template-columns:4.7rem minmax(0,1fr) minmax(0,1fr);gap:1rem;margin:1rem 0;align-items:stretch}
.stage-tag{grid-column:1;grid-row:1;align-self:start;border-top:3px solid var(--line);padding:.5rem .25rem 0;color:var(--muted);font-size:.78em;line-height:1.35;letter-spacing:.04em}
.stage-tag b{display:block;color:var(--fg);font-size:1.25em;margin-bottom:.1rem}
.lane{min-width:0;border:1px solid var(--line);border-radius:12px;background:var(--card);padding:1.05rem 1.2rem 1.2rem;box-shadow:0 1px 2px rgba(0,0,0,.035)}
.lane.a{grid-column:2;border-top:4px solid var(--lane-a)}
.lane.q{grid-column:3;border-top:4px solid var(--lane-q)}
.lane h3{margin:.05rem 0 .85rem;font-size:1.04em}
.lane.a h3{color:var(--lane-a)}
.lane.q h3{color:var(--lane-q)}
.lane p{margin:.65em 0}
.lane .katex-display{font-size:.92em;margin:.65em 0}
.why{border-left:3px solid var(--line);padding:.05rem 0 .05rem .9rem;color:var(--muted);margin:.9rem 0}
.why b{color:var(--fg)}
.calc{background:var(--box);border-radius:8px;padding:.6rem .8rem;margin:.75rem 0}
.calc p:first-child{margin-top:.15rem}.calc p:last-child{margin-bottom:.15rem}
.a .calc{background:var(--lane-a-soft)}
.q .calc{background:var(--lane-q-soft)}
.no-cross{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:1rem;border:1px dashed var(--line);border-radius:12px;padding:.75rem 1rem;margin:1.7rem 0;color:var(--muted);text-align:center}
.no-cross strong{color:var(--fg)}
.no-cross .bar{font-size:1.4em;color:var(--accent)}
.gate{border:2px solid var(--merge);background:var(--merge-soft);border-radius:14px;padding:1.2rem 1.5rem;margin:2rem 0}
.gate h2{border:0;margin:.05rem 0 .8rem;padding:0;color:var(--merge);font-size:1.25em}
.gate .result{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.gate .result>div{background:var(--card);border:1px solid var(--line);border-radius:9px;padding:.7rem 1rem;min-width:0}
.warning{border-left:5px solid var(--accent);background:var(--pen);padding:.8rem 1rem;border-radius:7px;margin:1.2rem 0}
.point-check{border:1px solid var(--line);border-radius:12px;padding:1rem 1.2rem;background:var(--card);margin:1.5rem 0}
.point-check h2{margin:.1rem 0 .7rem;border:0;padding:0;font-size:1.2em}
.point-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.point-grid>div{min-width:0;padding:.2rem .7rem;border-left:3px solid var(--line)}
.point-grid .left{border-color:var(--lane-a)}.point-grid .right{border-color:var(--lane-q)}
@media(max-width:850px){
  main,header.titlepage{padding-left:.85rem;padding-right:.85rem}
  .rule-strip{grid-template-columns:1fr}
  .tracks{display:none}
  .stage{grid-template-columns:1fr;gap:.65rem;margin:1.5rem 0}
  .stage-tag,.lane.a,.lane.q{grid-column:1}
  .stage-tag{grid-row:auto;border-top:1px solid var(--line);display:flex;gap:.5rem;align-items:baseline}
  .lane{padding:.9rem 1rem 1rem}
  .lane.a{grid-row:auto}.lane.q{grid-row:auto}
  .lane.a h3:before{content:"A 쪽 · ";font-size:.78em}.lane.q h3:before{content:"Q 쪽 · ";font-size:.78em}
  .no-cross{grid-template-columns:1fr}.no-cross .bar{transform:rotate(90deg)}
  .gate .result,.point-grid{grid-template-columns:1fr}
}
</style>

<div class="opening" markdown="1">

이 페이지에서는 처음부터 $\tfrac12dA=\operatorname{Im}Q$라고 쓰지 않는다. 그러면 어느 계산에서 허수부가 생겼는지 다시 흐려진다. **왼쪽 계산과 오른쪽 계산을 끝까지 따로 한다.** 두 결과가 모두 손에 들어온 뒤, 마지막 초록색 문에서만 서로 대조한다.

<div class="rule-strip">
<div class="rule"><b>공통 좌표</b>$z=x+iy$, &nbsp;$S=1+|z|^2=1+x^2+y^2$</div>
<div class="rule"><b>공통 벡터</b>$q=(1,z)^T$, &nbsp;$s=q/\sqrt S$</div>
<div class="rule"><b>내적 규약</b>$\langle r,t\rangle=r^\dagger t$ — 첫 슬롯을 켤레</div>
</div>

두 접벡터도 처음에 고정한다.

$$
X=u\,\partial_x+v\,\partial_y,\qquad
Y=a\,\partial_x+b\,\partial_y.
$$

따라서 $X$ 방향의 복소 속도와 $Y$ 방향의 복소 속도는

$$
\begin{aligned}
\xi&=dz(X)=u+iv,\\
\eta&=dz(Y)=a+ib.
\end{aligned}
$$

이다. 뒤에서 나오는 $u,v,a,b$는 새로운 기호가 아니라, 두 화살표의 $x,y$ 성분이다.

</div>

<div class="tracks">
<div class="track-title a"><strong>왼쪽 계산: $s\longrightarrow A\longrightarrow dA$</strong><span>단위구면 위에서 위상 방향의 속도를 읽고, 그 1-형식을 외미분한다.</span></div>
<div class="track-title q"><strong>오른쪽 계산: $q\longrightarrow Q\longrightarrow \operatorname{Re}Q,\operatorname{Im}Q$</strong><span>$q$와 나란한 성분을 뺀 뒤, 남은 두 속도의 복소 내적을 계산한다.</span></div>
</div>

<div class="stage" markdown="1">
<div class="stage-tag"><b>01</b>왜 이 식인가</div>
<div class="lane a" markdown="1">

### $A=-i\,s^\dagger ds$는 무엇을 재는가

먼저 이 곡선이 $\mathbb{CP}^1$에서 정말 안 움직이는지 확인한다. 단위벡터 $s_0$를 잡고

$$
s(t)=e^{it}s_0
$$

라 하면, 사영점은

$$
[s(t)]=[e^{it}s_0]=[s_0]
$$

이다. $e^{it}\ne0$인 복소수를 곱한 두 벡터는 같은 사영점을 나타내기 때문이다. 따라서 $s(t)$는 단위구면에서는 돌지만, $\mathbb{CP}^1$에서는 한 점에 가만히 있는 곡선이다.

그 속도는 $\dot s(t)=i\,e^{it}s_0=i\,s(t)$이다. 특히

$$
\begin{aligned}
\dot s(0)&=i\,s_0,\\
-i\,s_0^\dagger\dot s(0)
&=-i\,s_0^\dagger(i\,s_0)=1.
\end{aligned}
$$

즉 $-i\,s^\dagger\dot s$는 “사영점은 그대로 둔 채 위상만 도는 속도” $is$에 값 $1$을 준다.

이제 임의의 속도 $\dot s$에서도 정확히 무엇을 읽는지 계산한다. $s^\dagger s=1$을 미분하면

$$
\dot s^\dagger s+s^\dagger\dot s=0.
$$

첫 항은 둘째 항의 켤레이므로 $s^\dagger\dot s$의 실수부는 $0$이다. 따라서 어떤 실수 $c$에 대하여

$$
s^\dagger\dot s=ic,\qquad c=-i\,s^\dagger\dot s
$$

이다. 이제

$$
h=\dot s-c\,is
$$

라고 놓으면

$$
s^\dagger h=s^\dagger\dot s-ci\,s^\dagger s=ic-ci=0.
$$

그러므로 임의의 속도가 실제로

$$
\boxed{\dot s=c\,is+h,\qquad s^\dagger h=0}
$$

로 갈라진다. 여기에 $A=-i\,s^\dagger ds$를 넣으면

$$
A(\dot s)=-i\,s^\dagger(c\,is+h)=c.
$$

<div class="why"><b>그래서 이 식이다.</b> $A$는 임의의 속도 $\dot s$ 안에 “$\mathbb{CP}^1$에서는 안 움직이고 위상만 도는 속도” $is$가 몇 배 들어 있는지를 정확히 꺼낸다.</div>

</div>
<div class="lane q" markdown="1">

### $Q$는 왜 $q$ 방향을 빼는가

$\lambda\ne0$이면 $[\lambda q]=[q]$이다. 따라서 $\dot q$ 안에서 $q$와 나란한 부분은 대표벡터의 길이·위상만 바꾸며, 사영점의 실제 움직임으로 세면 안 된다.

$q$ 방향 성분은 평범한 정사영 공식으로

$$
\dot q_{\parallel}
=q\frac{q^\dagger\dot q}{q^\dagger q}
$$

이고, 실제로 남길 속도는

$$
\dot q_{\perp}=\dot q-q\frac{q^\dagger\dot q}{q^\dagger q}
$$

이다. 정말 수직인지 바로 곱해 보면

$$
\begin{aligned}
q^\dagger\dot q_\perp
&=q^\dagger\dot q
-q^\dagger q\,\frac{q^\dagger\dot q}{q^\dagger q}\\
&=0.
\end{aligned}
$$

두 방향 $X,Y$에서 남은 속도끼리 내적하면

$$
\dot q_{\perp,X}^\dagger\dot q_{\perp,Y}
=\dot q_X^\dagger\dot q_Y
-\frac{(\dot q_X^\dagger q)(q^\dagger\dot q_Y)}{S}.
$$

마지막으로 $S=q^\dagger q$로 나눈다. 그러면 대표벡터를 $\lambda q$로 바꾸어 분자와 분모가 모두 $|\lambda|^2$배 되어도 값이 바뀌지 않는다. 그 결과가

$$
Q(X,Y)
=\frac{\dot q_X^\dagger\dot q_Y}{S}
-\frac{(\dot q_X^\dagger q)(q^\dagger\dot q_Y)}{S^2}.
$$

<div class="why"><b>그래서 이 식이다.</b> 먼저 $q$와 나란한 가짜 움직임을 정사영으로 빼고, 남은 실제 사영공간 속도끼리 내적한다. 마지막의 $1/S$는 어느 길이의 대표벡터를 골라도 답이 같게 만든다.</div>

</div>
</div>

<div class="stage" markdown="1">
<div class="stage-tag"><b>02</b>좌표에 대입</div>
<div class="lane a" markdown="1">

### $s^\dagger ds$를 한 줄씩 편다

먼저

$$
dS=\bar z\,dz+z\,d\bar z
$$

이고, 곱의 미분을 그대로 쓰면

$$
ds
=\frac{(0,dz)^T}{\sqrt S}
-\frac{(1,z)^T}{2S^{3/2}}\,dS.
$$

왼쪽에서 $s^\dagger=(1,\bar z)/\sqrt S$를 곱한다.

<div class="calc" markdown="1">

$$
\begin{aligned}
s^\dagger ds
&=\frac{\bar z\,dz}{S}-\frac{dS}{2S}\\
&=\frac{2\bar z\,dz-(\bar z\,dz+z\,d\bar z)}{2S}\\
&=\frac{\bar z\,dz-z\,d\bar z}{2S}.
\end{aligned}
$$

</div>

아직 마지막 줄에 $i$가 숨어 있다. $z=x+iy$를 정말 곱해 보면

$$
\bar z\,dz
=x\,dx+y\,dy+i(x\,dy-y\,dx),
$$

$$
z\,d\bar z
=x\,dx+y\,dy-i(x\,dy-y\,dx).
$$

따라서

$$
s^\dagger ds=i\frac{x\,dy-y\,dx}{S},
$$

$$
\boxed{A=\frac{x\,dy-y\,dx}{S}}.
$$

<div class="why"><b>$A$에 허수부가 안 보이는 이유.</b> 없어진 것이 아니다. $s^\dagger ds$에 있던 $i$를 정의의 $-i$가 이미 없앴다. 그래서 $A$는 실수값 1-형식이다.</div>

</div>
<div class="lane q" markdown="1">

### $Q$의 네 조각을 각각 계산한다

$X,Y$ 방향의 속도는

$$
\dot q_X=(0,\xi)^T,\qquad
\dot q_Y=(0,\eta)^T
$$

이다. 내적 규약에서 첫 슬롯만 켤레하므로

<div class="calc" markdown="1">

$$
\begin{aligned}
\dot q_X^\dagger\dot q_Y&=\bar\xi\eta,\\
\dot q_X^\dagger q&=\bar\xi z,\\
q^\dagger\dot q_Y&=\bar z\eta,\\
q^\dagger q&=S.
\end{aligned}
$$

</div>

이 네 줄을 정의에 넣는다.

$$
\begin{aligned}
Q(X,Y)
&=\frac{\bar\xi\eta}{S}
-\frac{(\bar\xi z)(\bar z\eta)}{S^2}\\
&=\bar\xi\eta\frac{S-|z|^2}{S^2}\\
&=\boxed{\frac{\bar\xi\eta}{S^2}},
\end{aligned}
$$

마지막 줄에서는 $S-|z|^2=(1+|z|^2)-|z|^2=1$만 썼다.

</div>
</div>

<div class="no-cross"><span><strong>여기까지 왼쪽에는 $Q$가 없다.</strong><br>$A$는 실수값 1-형식이다.</span><span class="bar">∦</span><span><strong>여기까지 오른쪽에는 $dA$가 없다.</strong><br>$Q$는 복소수값을 내는 두-슬롯 식이다.</span></div>

<div class="stage" markdown="1">
<div class="stage-tag"><b>03</b>각자 끝까지</div>
<div class="lane a" markdown="1">

### $A$를 외미분한다

$A=P\,dx+R\,dy$라고 놓으면

$$
P=-\frac{y}{S},\qquad R=\frac{x}{S}.
$$

이제 외미분의 규칙 $d(f\alpha)=df\wedge\alpha+f\,d\alpha$를 그대로 쓴다. $d(dx)=d(dy)=0$이므로

$$
\begin{aligned}
dA
&=dP\wedge dx+dR\wedge dy\\
&=(P_x\,dx+P_y\,dy)\wedge dx\\
&\quad +(R_x\,dx+R_y\,dy)\wedge dy\\
&=P_y\,dy\wedge dx+R_x\,dx\wedge dy\\
&=(R_x-P_y)\,dx\wedge dy.
\end{aligned}
$$

$dx\wedge dx=dy\wedge dy=0$이고 $dy\wedge dx=-dx\wedge dy$라서 가운데 두 항만 살아남았다. 이것이 이차원 curl 공식

$$
dA=(\partial_xR-\partial_yP)\,dx\wedge dy
$$

가 나오는 이유다. 이제 두 편미분을 몫의 미분으로 계산한다.

<div class="calc" markdown="1">

$$
\partial_x\!\left(\frac{x}{S}\right)
=\frac{S-2x^2}{S^2},
$$

$$
\partial_y\!\left(-\frac{y}{S}\right)
=\frac{-S+2y^2}{S^2}.
$$

</div>

그러므로

$$
\begin{aligned}
\partial_xR-\partial_yP
&=\frac{S-2x^2}{S^2}\\
&\quad-\frac{-S+2y^2}{S^2}\\
&=\frac{2(S-x^2-y^2)}{S^2}\\
&=\frac{2}{S^2}.
\end{aligned}
$$

왼쪽 계산의 최종 결과는

$$
\boxed{dA=\frac{2}{S^2}\,dx\wedge dy}
$$

이다. $d$는 계수를 미분하고 $dx\wedge dy$로 묶었을 뿐이다.

</div>
<div class="lane q" markdown="1">

### $Q$의 실수부와 허수부를 직접 가른다

$\xi=u+iv$, $\eta=a+ib$였으므로 첫 슬롯을 켤레하여

$$
\begin{aligned}
\bar\xi\eta
&=(u-iv)(a+ib)\\
&=(ua+vb)+i(ub-va).
\end{aligned}
$$

따라서 오른쪽 계산의 최종 결과는

$$
\boxed{\operatorname{Re}Q(X,Y)=\frac{ua+vb}{S^2}},
$$

$$
\boxed{\operatorname{Im}Q(X,Y)=\frac{ub-va}{S^2}}
$$

이다.

두 식의 모양도 직접 확인할 수 있다.

<div class="calc" markdown="1">

$$
\operatorname{Re}Q(X,X)=\frac{u^2+v^2}{S^2}\ge0,
$$

$$
\operatorname{Im}Q(X,X)=\frac{uv-vu}{S^2}=0.
$$

</div>

분자는 고등학교 좌표 계산에서 이미 본 두 식이다.

$$
ua+vb=(u,v)\mathbin{\boldsymbol\cdot}(a,b),
$$

$$
ub-va=
\det\begin{pmatrix}u&v\\a&b\end{pmatrix}.
$$

첫째는 두 화살표의 내적이므로 순서를 바꾸어도 같고, $X=X$를 넣으면 길이 제곱이 된다. 둘째는 두 화살표가 만드는 **방향 있는 평행사변형의 넓이**이므로 순서를 바꾸면 부호가 바뀌고, 같은 화살표를 두 번 넣으면 넓이가 $0$이 된다. 여기에는 아직 $J$가 필요하지 않다.

</div>
</div>

<div class="stage" markdown="1">
<div class="stage-tag"><b>04</b>같은 입력에 평가</div>
<div class="lane a" markdown="1">

### $dA$에 $X,Y$를 넣는다

쐐기곱의 뜻을 좌표에 대입하면

$$
\begin{aligned}
(dx\wedge dy)(X,Y)
&=dx(X)dy(Y)\\
&\quad-dx(Y)dy(X)\\
&=ub-av.
\end{aligned}
$$

따라서

$$
dA(X,Y)=\frac{2(ub-va)}{S^2},
$$

즉

$$
\boxed{\frac12dA(X,Y)=\frac{ub-va}{S^2}}.
$$

</div>
<div class="lane q" markdown="1">

### $Q$에서는 이미 같은 입력의 값이 나왔다

오른쪽 계산의 두 상자는

$$
\boxed{\operatorname{Re}Q(X,Y)=\frac{ua+vb}{S^2}},
$$

$$
\boxed{\operatorname{Im}Q(X,Y)=\frac{ub-va}{S^2}}
$$

였다.

여기서 중요한 점은 $\operatorname{Im}Q$가 추상적인 이름으로 끼어든 것이 아니라는 것이다. $(u-iv)(a+ib)$를 보통 복소수 곱셈으로 전개했을 때 $i$ 앞에 실제로 남은 계수가 $ub-va$였다.

</div>
</div>

<div class="gate" markdown="1">

## 이제 처음으로 두 계산을 만난다

<div class="result" markdown="1">
<div markdown="1">왼쪽과 오른쪽의 $ub-va$가 같으므로

$$
\boxed{\frac12dA=\operatorname{Im}Q}
$$
</div>
<div markdown="1">오른쪽의 대칭이고 길이를 재는 부분을 이름 붙이면

$$
\boxed{g_{\mathrm{FS}}=\operatorname{Re}Q}
$$
</div>
</div>

따라서 한 덩어리로 쓰면 $Q=g_{\mathrm{FS}}+\tfrac{i}{2}dA$이다. 이것은 출발점이 아니라, **두 벌의 계산이 끝난 다음 얻은 대조표**다.

</div>

<div class="warning" markdown="1">

**여기서 $d$가 허수부를 꺼낸 것이 아니다.** 순서는 정확히 이렇다. $s^\dagger ds$는 순허수였다 → $-i$가 그 계수를 실수 1-형식 $A$로 바꾸었다 → $d$는 $A$를 평범하게 외미분했다. 그와 독립적으로 $Q$를 계산해 보니, 그 허수부의 계수가 우연이 아니라 정확히 $\tfrac12dA$와 같았다.

</div>

<div class="point-check" markdown="1">

## 화면의 곡선 $z(t)=1+it$를 두 벌 계산에 꽂는다

이제 추상적인 $X,Y$를 잠시 내려놓고, 실제로 보았던 곡선을 넣는다. $t=0$에서

$$
\begin{aligned}
z(0)&=1,&S(0)&=2,\\
V&=\dot z(0)=\partial_y.
\end{aligned}
$$

이다.

<div class="point-grid" markdown="1">
<div class="left" markdown="1">

**왼쪽: 이 속도에는 위상 회전이 얼마나 들어 있는가.**

단위벡터 곡선은

$$
s(t)=\frac{(1,1+it)^T}{\sqrt{2+t^2}}.
$$

$t=0$에서는 분모의 미분이 $0$이므로

$$
s_0=\frac{(1,1)^T}{\sqrt2},
\qquad
\dot s_0=\frac{(0,i)^T}{\sqrt2}.
$$

$A=(x\,dy-y\,dx)/S$에 $x=1,y=0,V=\partial_y$를 넣으면

$$
\boxed{A(V)=\frac12}.
$$

따라서 $\dot s_0$ 안의 위상 속도는 $\tfrac12\,is_0$이다. 실제로 나머지를 빼면

$$
\begin{aligned}
h
&=\dot s_0-\frac12\,is_0\\
&=\frac{1}{2\sqrt2}(-i,i)^T,
\qquad s_0^\dagger h=0.
\end{aligned}
$$

그리고

$$
\|h\|^2=\frac18+\frac18=\boxed{\frac14}.
$$

</div>
<div class="right" markdown="1">

**오른쪽: 사영공간에서 실제로 남은 속도의 길이는 얼마인가.**

$V=\partial_y$이므로 복소 속도는 $\xi=i$이다. 같은 속도를 두 슬롯에 넣으면

$$
Q(V,V)=\frac{\bar\xi\xi}{S^2}
=\frac{(-i)i}{2^2}
=\boxed{\frac14}.
$$

왼쪽에서 위상 성분을 뺀 뒤 남은 $h$의 길이 제곱과 정확히 같다.

그런데 이 값에는 허수부가 없다. 계산이 실패한 것이 아니다. 같은 화살표를 두 번 넣으면

$$
\operatorname{Im}Q(V,V)
=\frac{\det\!\begin{pmatrix}0&1\\0&1\end{pmatrix}}{4}
=0
$$

이기 때문이다. **허수부를 보려면 서로 다른 두 방향이 필요하다.**

같은 점 $z=1$에서 $X=\partial_x$, $Y=\partial_y$를 넣으면 $\xi=1,\eta=i$이고

$$
Q(X,Y)=\frac{\bar\xi\eta}{S^2}
=\frac{i}{4}.
$$

따라서

$$
\boxed{
\begin{aligned}
\operatorname{Im}Q(X,Y)&=\frac14,\\
\frac12dA(X,Y)&=\frac14.
\end{aligned}}
$$

</div>
</div>

이 예에서 $A(V)=\tfrac12$와 $Q(V,V)=\tfrac14$는 서로 경쟁하는 두 답이 아니다. 첫째는 들어 올린 속도 안의 **위상 성분의 계수**이고, 둘째는 그 위상 성분을 뺀 뒤 남은 **사영공간 속도의 길이 제곱**이다.

</div>

<div class="point-check" markdown="1">

## 원점에서 한 번 더: $A$가 0이어도 $dA$는 0이 아니다

$z=0$에서 $S=1$이고 $X=\partial_x$, $Y=\partial_y$를 넣는다. 즉 $u=1,v=0,a=0,b=1$이다.

<div class="point-grid" markdown="1">
<div class="left" markdown="1">

**왼쪽.** 원점에서 $A=(x\,dy-y\,dx)/S$의 값은 $0$이다. 그러나 주변에서 계수가 변하므로

$$
dA(X,Y)=2,
$$

$$
\frac12dA(X,Y)=1.
$$

</div>
<div class="right" markdown="1">

**오른쪽.** $\xi=1$, $\eta=i$이므로

$$
Q(X,Y)=\bar\xi\eta=i,
$$

$$
\operatorname{Im}Q(X,Y)=1.
$$

</div>
</div>

이 숫자 검산에서 두 결과가 정확히 만난다. 동시에 “한 점에서 $A=0$”과 “그 점에서 $dA\ne0$”가 모순이 아님도 보인다. 함수 $f$가 한 점에서 $0$이어도 그 점의 미분 $df$는 0일 필요가 없는 것과 같다.

</div>

---

이 페이지의 계산은 $z$-차트 하나에서 했다. 다른 차트와 겹치는 곳에서는 $A$의 식 자체는 위상 선택에 따라 바뀔 수 있지만, $dA$와 $Q$의 위 두 결과는 같은 사영공간의 양으로 맞물린다.
