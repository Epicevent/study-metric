# -*- coding: utf-8 -*-
# verify_ig0_onevar.py — IG0: 한 변수에서 §3.1 전체.
# 지표도 합도 없이, 곱의 미분(라이프니츠)과 연쇄법칙만으로 끝난다는 것을 확인한다.
#
#   D(x,y) = F(x) − F(y) − F'(y)(x − y)          ← y에서의 접선과 곡선의 세로 간격
#   ∂_x D  = F'(x) − F'(y)
#   ∂_y ∂_x D = −F''(y)                          (두 순서 모두)
#   g = −∂_x∂_y D |_{x=y} = F''(x)
#
# 실행: python 정보기하/verify_ig0_onevar.py   (요구: pip install sympy)
import sympy as sp

PASS = TOTAL = 0


def check(label, ok):
    global PASS, TOTAL
    TOTAL += 1
    PASS += bool(ok)
    print(f"[{TOTAL:02d}] {label}: {'OK' if ok else 'FAIL'}")


t, x, y = sp.symbols('t x y', real=True)


def bregman(F, dom=t):
    """D(x,y) = F(x) − F(y) − F'(y)(x−y).  F'는 '미분해서 만든 함수'를 y에 대입한 것."""
    Fx = F.subs(dom, x)
    Fy = F.subs(dom, y)
    Fp_at_y = sp.diff(F, dom).subs(dom, y)          # ← 미분 먼저, 대입 나중
    return sp.expand(Fx - Fy - Fp_at_y * (x - y))


# 서로 다른 성격의 F 네 개 (2차 / 3차 / 지수 / 음의 엔트로피)
eta = sp.symbols('eta', positive=True)
CASES = [
    ("F = t²",              t**2,                                       t),
    ("F = t³",              t**3,                                       t),
    ("F = eᵗ",              sp.exp(t),                                  t),
    ("F = 음의 엔트로피",    eta*sp.log(eta) + (1-eta)*sp.log(1-eta),     eta),
]

print("=" * 70)
print("PART 1. 세 줄 계산 — 네 개의 F 에서 전부")
print("=" * 70)
for name, F, dom in CASES:
    D = bregman(F, dom)
    Fp = lambda pt: sp.diff(F, dom).subs(dom, pt)
    Fpp = lambda pt: sp.diff(F, dom, 2).subs(dom, pt)

    check(f"{name}:  ∂_x D = F'(x) − F'(y)",
          sp.simplify(sp.diff(D, x) - (Fp(x) - Fp(y))) == 0)
    check(f"{name}:  ∂_y ∂_x D = −F''(y)   (∂_x 먼저)",
          sp.simplify(sp.diff(D, x, y) + Fpp(y)) == 0)
    check(f"{name}:  ∂_x ∂_y D = −F''(y)   (∂_y 먼저 — 상쇄 경로가 다르다)",
          sp.simplify(sp.diff(D, y, x) + Fpp(y)) == 0)
    check(f"{name}:  g = −∂_x∂_y D|_{{x=y}} = F''(x)",
          sp.simplify((-sp.diff(D, x, y)).subs(y, x) - Fpp(x)) == 0)

print()
print("=" * 70)
print("PART 2. 라이프니츠가 한 항이 되는 곳 vs 두 항이 되는 곳")
print("=" * 70)
for name, F, dom in CASES:
    Fp_y = sp.diff(F, dom).subs(dom, y)
    Fpp_y = sp.diff(F, dom, 2).subs(dom, y)
    term = -Fp_y * (x - y)                                   # 문제의 셋째 항

    # x로 미분: F'(y)에 x가 없어 상수 → 한 항으로 줄어든다
    check(f"{name}:  ∂_x[−F'(y)(x−y)] = −F'(y)   (한 항)",
          sp.simplify(sp.diff(term, x) + Fp_y) == 0)
    # y로 미분: 두 인자 모두 y를 가지므로 두 항이 다 나온다
    check(f"{name}:  ∂_y[−F'(y)(x−y)] = −F''(y)(x−y) + F'(y)   (두 항)",
          sp.simplify(sp.diff(term, y) - (-Fpp_y*(x - y) + Fp_y)) == 0)
    # 그리고 −F(y) 가 준 −F'(y) 와 상쇄되어 한 덩어리만 남는다
    D = bregman(F, dom)
    check(f"{name}:  ⟹ ∂_y D = −F''(y)(x−y)   (∓F'(y) 상쇄)",
          sp.simplify(sp.diff(D, y) + Fpp_y*(x - y)) == 0)

print()
print("=" * 70)
print("PART 3. 뜻 — 접선과의 세로 간격, 그리고 부호")
print("=" * 70)
for name, F, dom in CASES:
    D = bregman(F, dom)
    tangent = F.subs(dom, y) + sp.diff(F, dom).subs(dom, y) * (x - y)
    check(f"{name}:  D = F(x) − (y에서의 접선)(x)",
          sp.simplify(D - (F.subs(dom, x) - tangent)) == 0)

F2 = CASES[1][1]                                             # F = t³ 로 부호 시연
D2 = bregman(F2)
check("부호: ∂_x∂_x D = +F''(x)  (첫 슬롯만 두 번이면 안 뒤집힌다)",
      sp.simplify(sp.diff(D2, x, 2) - sp.diff(F2, t, 2).subs(t, x)) == 0)
check("부호: ∂_x∂_y D = −F''(y)  (슬롯을 나누면 뒤집힌다)",
      sp.simplify(sp.diff(D2, x, y) + sp.diff(F2, t, 2).subs(t, y)) == 0)

# 볼록한 F 에서 D ≥ 0 을 여러 점에서 수치 확인
Fe = sp.exp(t)
De = bregman(Fe)
pts = [(sp.Rational(a, 4), sp.Rational(b, 4)) for a in range(-4, 5) for b in range(-4, 5)]
check("볼록 F=eᵗ 에서 D(x,y) ≥ 0, 등호는 x=y 뿐 (81점)",
      all((De.subs({x: a, y: b}) == 0) if a == b else (sp.N(De.subs({x: a, y: b})) > 0)
          for a, b in pts))

print()
print("=" * 70)
print("PART 4. 동전 하나 — logit, Fisher 정보, KL 이 전부 나온다")
print("=" * 70)
Fb = eta*sp.log(eta) + (1-eta)*sp.log(1-eta)
check("F'(η) = log η − log(1−η) = logit  (log-ratio 좌표; ±1이 상쇄)",
      sp.simplify(sp.diff(Fb, eta) - (sp.log(eta) - sp.log(1-eta))) == 0)
check("F''(η) = 1/η + 1/(1−η) = 1/(η(1−η))  (베르누이 Fisher 정보)",
      sp.simplify(sp.diff(Fb, eta, 2) - 1/(eta*(1-eta))) == 0)

# Bregman = KL  (로그 가지 문제로 기호 단순화가 안 되므로 유리점에서 확인)
z = sp.symbols('zeta', positive=True)
Db = (Fb.subs(eta, x) - Fb.subs(eta, z) - sp.diff(Fb, eta).subs(eta, z)*(x - z))
KL = x*sp.log(x/z) + (1-x)*sp.log((1-x)/(1-z))
samples = [(sp.Rational(1, 4), sp.Rational(1, 3)), (sp.Rational(7, 10), sp.Rational(1, 5)),
           (sp.Rational(1, 2), sp.Rational(9, 10)), (sp.Rational(1, 100), sp.Rational(1, 2))]
check("D(η,ζ) = KL(η‖ζ)  (베르누이, 4개 유리점)",
      all(sp.simplify(Db.subs({x: a, z: b}) - KL.subs({x: a, z: b})) == 0 for a, b in samples))

g_b = sp.diff(Fb, eta, 2)
vals = [(sp.Rational(1, 2), 4), (sp.Rational(1, 4), sp.Rational(16, 3)),
        (sp.Rational(1, 10), sp.Rational(100, 9))]
check("계량 값: g(½)=4, g(¼)=16/3, g(1/10)=100/9  (가장자리로 갈수록 커진다)",
      all(sp.simplify(g_b.subs(eta, p) - v) == 0 for p, v in vals))
check("가장자리에서 발산: g(η) → ∞  (η→0⁺)", sp.limit(g_b, eta, 0, '+') == sp.oo)

print()
print("=" * 70)
print("PART 5. 지표로 올라가면 무엇이 새로 생기나 — 합과 δ 뿐")
print("=" * 70)
# n=2 를 손으로 풀어 쓴 것과 지표 표기가 같은지
x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2', real=True)
w1, w2 = sp.symbols('w1 w2', real=True)
Fn = w1**3*w2 + sp.exp(w2) + w1*w2**2                        # 아무 매끄러운 F
sub_x = [(w1, x1), (w2, x2)]
sub_y = [(w1, y1), (w2, y2)]
F_at = lambda s: Fn.subs(s, simultaneous=True)
Fa_at = lambda a, s: sp.diff(Fn, [w1, w2][a]).subs(s, simultaneous=True)

Dn = sp.expand(F_at(sub_x) - F_at(sub_y)
               - Fa_at(0, sub_y)*(x1 - y1) - Fa_at(1, sub_y)*(x2 - y2))
check("∂_1 D = F_1(x) − F_1(y)  — 합에서 a=1 항만 살아남는다 (δ의 정체)",
      sp.simplify(sp.diff(Dn, x1) - (Fa_at(0, sub_x) - Fa_at(0, sub_y))) == 0)
check("∂_2 D = F_2(x) − F_2(y)  — 같은 이유로 a=2 항만",
      sp.simplify(sp.diff(Dn, x2) - (Fa_at(1, sub_x) - Fa_at(1, sub_y))) == 0)

Fij = lambda i, j, s: sp.diff(Fn, [w1, w2][i], [w1, w2][j]).subs(s, simultaneous=True)
xs2, ys2 = [x1, x2], [y1, y2]
check("g_ij = −∂_i∂'_j D|_Δ = F_ij(x)  (2×2 네 성분) — 한 변수 g=F'' 의 지표판",
      all(sp.simplify((-sp.diff(Dn, xs2[i], ys2[j])).subs([(y1, x1), (y2, x2)],
                                                          simultaneous=True)
                      - Fij(i, j, sub_x)) == 0
          for i in range(2) for j in range(2)))

print()
print("=" * 70)
print(f"결과: {PASS}/{TOTAL} 통과")
print("=" * 70)
