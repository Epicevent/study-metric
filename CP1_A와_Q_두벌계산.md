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
\xi=dz(X)=u+iv,\qquad \eta=dz(Y)=a+ib
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

### $A=-i,s^\dagger ds$는 무엇을 재는가

$s^\dagger s=1$을 곡선 $s(t)$를 따라 미분하면

$$
\dot s^\dagger s+s^\dagger\dot s=0.
$$

첫 항은 둘째 항의 켤레이므로, $s^\dagger\dot s$의 실수부는 $0$이다. 즉 어떤 실수 $c$가 있어서

$$
s^\dagger\dot s=ic
$$

이다. 여기에 $-i$를 곱하면 $A(\dot s)=c$라는 **실수**가 남는다.

실제로 점은 그대로 두고 대표벡터의 위상만 돌리는 곡선

$$
s(t)=e^{it}s_0
$$

을 넣으면 $\dot s(0)=is_0$이고

$$
A(\dot s(0))=-i,s_0^\dagger(is_0)=1.
$$

<div class="why"><b>그래서 이 식이다.</b> $A$는 “이 속도에 $is$ 방향, 곧 같은 사영점 위에서 도는 위상 속도가 얼마나 들어 있는가”를 숫자로 읽는다.</div>

</div>
<div class="lane q" markdown="1">

### $Q$는 왜 $q$ 방향을 빼는가

$q$와 $\lambda q$는 같은 사영점을 나타낸다. 그러므로 속도 $\dot q$ 안에서 $q$와 나란한 부분은 사영공간의 실제 움직임으로 세면 안 된다.

$q$ 방향 성분은 평범한 정사영 공식으로

$$
\dot q_{\parallel}
=q\frac{q^\dagger\dot q}{q^\dagger q}
$$

이고, 실제로 남길 속도는

$$
\dot q_{\perp}=\dot q-q\frac{q^\dagger\dot q}{q^\dagger q}
$$

이다. 두 방향 $X,Y$에서 이 남은 속도끼리 내적하고 길이 $q^\dagger q=S$로 한 번 더 나누면

$$
Q(X,Y)
=\frac{\dot q_X^\dagger\dot q_Y}{S}
-\frac{(\dot q_X^\dagger q)(q^\dagger\dot q_Y)}{S^2}.
$$

<div class="why"><b>그래서 이 식이다.</b> 첫 항은 전체 속도의 내적이고, 둘째 항은 그중 $q$와 나란해서 사영공간에서는 가짜인 부분이다.</div>

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
-\frac{(1,z)^T}{2S^{3/2}},dS.
$$

왼쪽에서 $s^\dagger=(1,\bar z)/\sqrt S$를 곱한다.

<div class="calc" markdown="1">

$$
\begin{aligned}
s^\dagger ds
&=\frac{\bar z\,dz}{S}-\frac{dS}{2S}\\
&=\frac{2\bar z,dz-(\bar z,dz+z,d\bar z)}{2S}\\
&=\frac{\bar z,dz-z,d\bar z}{2S}.
\end{aligned}
$$

</div>

아직 마지막 줄에 $i$가 숨어 있다. $z=x+iy$를 정말 곱해 보면

$$
\bar z,dz
=x,dx+y,dy+i(x,dy-y,dx),
$$

$$
z,d\bar z
=x,dx+y,dy-i(x,dy-y,dx).
$$

따라서

$$
s^\dagger ds=i\frac{x,dy-y,dx}{S},
\qquad
\boxed{A=\frac{x,dy-y,dx}{S}}.
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

$A=P,dx+R,dy$라고 놓으면

$$
P=-\frac{y}{S},\qquad R=\frac{x}{S}.
$$

미적분학의 이차원 curl 공식은

$$
dA=(\partial_xR-\partial_yP),dx\wedge dy
$$

이다. 두 편미분은 몫의 미분으로

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
&=\frac{S-2x^2-(-S+2y^2)}{S^2}\\
&=\frac{2(1+x^2+y^2)-2x^2-2y^2}{S^2}\\
&=\frac{2}{S^2}.
\end{aligned}
$$

왼쪽 계산의 최종 결과는

$$
\boxed{dA=\frac{2}{S^2},dx\wedge dy}
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

첫 식은 화살표의 길이를 재고, 둘째 식은 같은 화살표를 두 번 넣으면 죽는다. 이 단계에서는 그것만 관찰하면 된다.

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
&=dx(X)dy(Y)-dx(Y)dy(X)\\
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

## 원점에서 한 번 더: $A$가 0이어도 $dA$는 0이 아니다

$z=0$에서 $S=1$이고 $X=\partial_x$, $Y=\partial_y$를 넣는다. 즉 $u=1,v=0,a=0,b=1$이다.

<div class="point-grid" markdown="1">
<div class="left" markdown="1">

**왼쪽.** 원점에서 $A=(x,dy-y,dx)/S$의 값은 $0$이다. 그러나 주변에서 계수가 변하므로

$$
dA(X,Y)=2,qquad \frac12dA(X,Y)=1.
$$

</div>
<div class="right" markdown="1">

**오른쪽.** $\xi=1$, $\eta=i$이므로

$$
Q(X,Y)=\bar\xi\eta=i,qquad \operatorname{Im}Q(X,Y)=1.
$$

</div>
</div>

이 숫자 검산에서 두 결과가 정확히 만난다. 동시에 “한 점에서 $A=0$”과 “그 점에서 $dA\ne0$”가 모순이 아님도 보인다. 함수 $f$가 한 점에서 $0$이어도 그 점의 미분 $df$는 0일 필요가 없는 것과 같다.

</div>

---

이 페이지의 계산은 $z$-차트 하나에서 했다. 다른 차트와 겹치는 곳에서는 $A$의 식 자체는 위상 선택에 따라 바뀔 수 있지만, $dA$와 $Q$의 위 두 결과는 같은 사영공간의 양으로 맞물린다.
