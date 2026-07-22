"""CP1 두 벌 계산 문서의 핵심 등식을 줄 단위로 검산한다."""
import sympy as sp

x, y, u, v, a, b = sp.symbols("x y u v a b", real=True)
S = 1 + x**2 + y**2
checks = []


def check(label, actual, expected):
    ok = sp.simplify(actual - expected) == 0
    checks.append(ok)
    print(("OK  " if ok else "FAIL") + label)
    if not ok:
        print("    actual  =", sp.simplify(actual))
        print("    expected=", sp.simplify(expected))


# A = P dx + R dy
P = -y / S
R = x / S
check("A의 dx 계수", P, -y / S)
check("A의 dy 계수", R, x / S)

# dA = (partial_x R - partial_y P) dx wedge dy
dA_xy = sp.diff(R, x) - sp.diff(P, y)
check("dA의 dx∧dy 계수", dA_xy, 2 / S**2)

# X=(u,v), Y=(a,b)
wedge_XY = u * b - a * v
half_dA_XY = sp.Rational(1, 2) * dA_xy * wedge_XY
check("(1/2)dA(X,Y)", half_dA_XY, (u*b - v*a) / S**2)

# Q(X,Y) = conjugate(xi) eta / S^2
xi = u + sp.I*v
eta = a + sp.I*b
Q = sp.expand(sp.conjugate(xi) * eta) / S**2
check("Re Q(X,Y)", sp.re(Q), (u*a + v*b) / S**2)
check("Im Q(X,Y)", sp.im(Q), (u*b - v*a) / S**2)
check("(1/2)dA = Im Q", half_dA_XY, sp.im(Q))

# 대칭/교대와 원점 숫자 검산
Q_xx = sp.expand(sp.conjugate(xi) * xi) / S**2
check("Re Q(X,X)는 길이 제곱", sp.re(Q_xx), (u**2 + v**2) / S**2)
check("Im Q(X,X)=0", sp.im(Q_xx), 0)

# 실제 곡선 z(t)=1+it, t=0
z1_vertical = {x: 1, y: 0, u: 0, v: 1}
A_on_V = P*u + R*v
check("z=1에서 A(∂y)=1/2", A_on_V.subs(z1_vertical), sp.Rational(1, 2))

s0 = sp.Matrix([1, 1]) / sp.sqrt(2)
sdot0 = sp.Matrix([0, sp.I]) / sp.sqrt(2)
h0 = sdot0 - sp.Rational(1, 2) * sp.I * s0
check("z(t)=1+it의 나머지 h는 s와 수직", (sp.conjugate(s0).T * h0)[0], 0)
check("z(t)=1+it의 ||h||^2=1/4", (sp.conjugate(h0).T * h0)[0], sp.Rational(1, 4))
check("z=1에서 Q(∂y,∂y)=1/4", sp.re(Q_xx).subs(z1_vertical), sp.Rational(1, 4))

z1_cross = {x: 1, y: 0, u: 1, v: 0, a: 0, b: 1}
check("z=1에서 Im Q(∂x,∂y)=1/4", sp.im(Q).subs(z1_cross), sp.Rational(1, 4))
check("z=1에서 (1/2)dA(∂x,∂y)=1/4", half_dA_XY.subs(z1_cross), sp.Rational(1, 4))

# 원점 숫자 검산
check("원점에서 (1/2)dA(∂x,∂y)=1", half_dA_XY.subs({x: 0, y: 0, u: 1, v: 0, a: 0, b: 1}), 1)
check("원점에서 Im Q(∂x,∂y)=1", sp.im(Q).subs({x: 0, y: 0, u: 1, v: 0, a: 0, b: 1}), 1)

passed = sum(checks)
print(f"\n{passed}/{len(checks)} checks passed")
raise SystemExit(0 if passed == len(checks) else 1)
