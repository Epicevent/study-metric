# -*- coding: utf-8 -*-
"""verifyA1_targets — A1 워크시트의 검산 기준값 확인용. **다 푼 뒤에 돌릴 것.**

책 7장에 인쇄된 '검산용 답'과 워크시트의 검산 기준만 재확인한다. 풀이 과정은 없음.
"""
import sympy as sp

I = sp.I
ok = lambda name, cond: print(("[OK] " if cond else "[FAIL] ") + name)

# ---- G1: (i/2)(z dz̄ − z̄ dz) = x dy − y dx  (계수 비교로)
x, y = sp.symbols("x y", real=True)
dx, dy = sp.symbols("dx dy")           # 형식 기호
z = x + I * y
dz = dx + I * dy
dzb = dx - I * dy
expr = sp.expand((I / 2) * (z * dzb - sp.conjugate(z) * dz))
ok("G1: (i/2)(z dz̄ − z̄ dz) = x dy − y dx",
   sp.simplify(expr - (x * dy - y * dx)) == 0)

# ---- G5: dα = 2 Σ dx_r ∧ dy_r  (외미분을 성분으로: d(x dy − y dx) = 2 dx∧dy)
# 1-형식 f dx + g dy 의 d = (∂g/∂x − ∂f/∂y) dx∧dy 공식으로 확인
f, g = -y, x   # α 한 짝 = x dy − y dx → (f,g) = (−y, x)
ok("G5: d(x dy − y dx) 의 dx∧dy 계수 = 2",
   sp.simplify(sp.diff(g, x) - sp.diff(f, y) - 2) == 0)

# ---- H4/H5: dA = i dw∧dw̄/(1+|w|²)²,  i dw∧dw̄ = 2 dx∧dy → ω_FS = 2dx∧dy/(1+x²+y²)²
# H5 는 대수 항등식: dw∧dw̄ = (dx+idy)∧(dx−idy) = −2i dx∧dy
dw_w_dwb_coeff = sp.expand((1) * (-I) - (I) * (1))   # dx∧dy 계수: (1)(−i)−(i)(1) = −2i
ok("H5: dw∧dw̄ = −2i dx∧dy", sp.simplify(dw_w_dwb_coeff + 2 * I) == 0)

# ---- H6: ∫ 2 dxdy/(1+x²+y²)² = 2π
r, th = sp.symbols("r theta", positive=True)
total = sp.integrate(sp.integrate(2 * r / (1 + r ** 2) ** 2, (r, 0, sp.oo)), (th, 0, 2 * sp.pi))
ok("H6: ∫ ω_FS = 2π", sp.simplify(total - 2 * sp.pi) == 0)

# ---- A1-2: ω_FS 를 w = tan(θ2/2) e^{iθ1} 로 당기면 계수 크기 = ½ sinθ2
t1, t2 = sp.symbols("theta1 theta2", real=True)
X = sp.tan(t2 / 2) * sp.cos(t1)
Y = sp.tan(t2 / 2) * sp.sin(t1)
dens = 2 / (1 + X ** 2 + Y ** 2) ** 2
jac = sp.simplify(X.diff(t1) * Y.diff(t2) - X.diff(t2) * Y.diff(t1))  # dx∧dy → dθ1∧dθ2
pull = sp.simplify(sp.expand_trig(dens * jac))
ok("A1-2: ω_FS 당김 = −½sinθ2 · dθ1∧dθ2  (크기 ½sinθ2; 부호는 순서·규약 추적 과제)",
   sp.simplify(pull + sp.sin(t2) / 2) == 0)
# 5b 쪽 수치와 크기 비교: −2 Im Q12 = ½ sinθ2
psi = sp.Matrix([sp.cos(t2 / 2), sp.exp(I * t1) * sp.sin(t2 / 2)])
hd = lambda a, b: sum(sp.conjugate(p) * q for p, q in zip(a, b))
Q12 = sp.simplify(sp.expand_complex(
    hd(psi.diff(t1), psi.diff(t2)) - hd(psi.diff(t1), psi) * hd(psi, psi.diff(t2))))
ok("A1-2: |−2 Im Q12| = |당김 계수| = ½ sinθ2",
   sp.simplify(sp.Abs(-2 * sp.im(Q12)) - sp.Abs(pull)) == 0 or
   sp.simplify((-2 * sp.im(Q12)) ** 2 - pull ** 2) == 0)

# ---- A1-3: 한 점에서 Q 행렬의 두 얼굴
pt = {t1: sp.pi / 2, t2: sp.pi / 3}
def Q(i_, j_):
    di = psi.diff([t1, t2][i_]); dj = psi.diff([t1, t2][j_])
    return sp.simplify(sp.expand_complex(
        (hd(di, dj) - hd(di, psi) * hd(psi, dj)).subs(pt)))
Qm = sp.Matrix(2, 2, lambda i_, j_: Q(i_, j_))
ReQ = Qm.applyfunc(sp.re); ImQ = Qm.applyfunc(sp.im)
r3 = sp.sqrt(3)
ok("A1-3: Re Q = diag(3/16, 1/4)  (대칭 — 계량 H/4)",
   sp.simplify(ReQ - sp.diag(sp.Rational(3, 16), sp.Rational(1, 4))) == sp.zeros(2, 2))
ok("A1-3: Im Q = [[0, −√3/8],[√3/8, 0]]  (반대칭 — 2-형식 계수)",
   sp.simplify(ImQ - sp.Matrix([[0, -r3 / 8], [r3 / 8, 0]])) == sp.zeros(2, 2))

print("\n(G2·G3·G4·H3, A1-1은 손계산 확인 문제 — 스크립트 검산 대상 아님)")
