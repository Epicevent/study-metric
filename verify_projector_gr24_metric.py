"""Projector로 Gr(2,4)에 metric 주기 — 본문 핵심 등식 검산.

실행: python verify_projector_gr24_metric.py
"""
import sympy as s


checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append((label, ok))
    print(("PASS" if ok else "FAIL") + "  " + label)


def meq(a, b):
    return s.simplify(a - b) == s.zeros(*a.shape)


t = s.symbols("t", real=True)
c, q = s.cos(t), s.sin(t)
I = s.I

X0 = s.Matrix([
    [1, 0],
    [0, 1],
    [0, 0],
    [0, 0],
])
P0 = X0 * X0.H
R = s.Matrix([[c, -q], [q, c]])
Xsame = X0 * R
Psame = s.simplify(Xsame * Xsame.H)

check("01 X0^* X0 = I2", meq(X0.H * X0, s.eye(2)))
check("02 P0^* = P0", meq(P0.H, P0))
check("03 P0^2 = P0", meq(P0 * P0, P0))
check("04 tr(P0) = 2", s.trace(P0) == 2)
check("05 R^* R = I2", meq(s.simplify(R.H * R), s.eye(2)))
check("06 basis rotation keeps P fixed", meq(Psame, P0))
check("07 basis rotation has dP = 0", meq(s.diff(Psame, t), s.zeros(4)))

X = s.Matrix([
    [1, 0],
    [0, c],
    [0, q],
    [0, 0],
])
P = s.simplify(X * X.H)
dP = s.simplify(s.diff(P, t))
A = dP.subs(t, 0)

check("08 moving frame stays orthonormal", meq(s.simplify(X.H * X), s.eye(2)))
check("09 moving P remains a projector", meq(s.simplify(P * P), P))
check("10 moving P has trace 2", s.simplify(s.trace(P)) == 2)
check("11 dP(0) is Hermitian", meq(A.H, A))
check("12 differentiated projector equation", meq(A * P0 + P0 * A, A))
check("13 tr(dP(0)) = 0", s.trace(A) == 0)
check("14 tr(dP(t)^2) = 2", s.trigsimp(s.trace(dP * dP)) == 2)
check("15 QFI speed squared = 4", s.trigsimp(2 * s.trace(dP * dP)) == 4)
check("16 FS speed squared = 1", s.trigsimp(s.trace(dP * dP) / 2) == 1)
check(
    "17 chord square = 4 sin^2(t)",
    s.trigsimp(2 * s.trace((P - P0) * (P - P0)) - 4 * q**2) == 0,
)

# Exact nontrivial complex tangent block.
B = s.Matrix([[1 + I, 2 - I], [-1 + 2 * I, 3]])
Z2 = s.zeros(2)
Atan = Z2.row_join(B.H).col_join(B.row_join(Z2))

check("18 block tangent satisfies AP+PA=A", meq(Atan * P0 + P0 * Atan, Atan))
check("19 block norm identity", s.simplify(s.trace(Atan * Atan) - 2 * s.trace(B.H * B)) == 0)
check("20 positivity on nonzero tangent", s.simplify(2 * s.trace(Atan * Atan)) > 0)

passed = sum(ok for _, ok in checks)
print(f"\n{passed}/{len(checks)} checks passed")
if passed != len(checks):
    raise SystemExit(1)
