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
# Exact nontrivial complex tangent block.
B = s.Matrix([[1 + I, 2 - I], [-1 + 2 * I, 3]])
Z2 = s.zeros(2)
Atan = Z2.row_join(B.H).col_join(B.row_join(Z2))

check("17 block tangent satisfies AP+PA=A", meq(Atan * P0 + P0 * Atan, Atan))
check("18 block norm identity", s.simplify(s.trace(Atan * Atan) - 2 * s.trace(B.H * B)) == 0)
check("19 positivity on nonzero tangent", s.simplify(2 * s.trace(Atan * Atan)) > 0)

# One complex chart direction: V(z) = [e1, e2 + z e3].
x, y = s.symbols("x y", real=True)
z = x + I * y
S = 1 + x**2 + y**2
Vz = s.Matrix([
    [1, 0],
    [0, 1],
    [0, z],
    [0, 0],
])
Gz = s.simplify(Vz.H * Vz)
Pz = s.simplify(Vz * Gz.inv() * Vz.H)
Pzx = s.simplify(s.diff(Pz, x))
Pzy = s.simplify(s.diff(Pz, y))

check("20 one-slot Gram matrix", meq(Gz, s.diag(1, S)))
check("21 one-slot P remains a projector", meq(s.simplify(Pz * Pz), Pz))
check(
    "22 one-slot FS coefficient in x direction",
    s.simplify(s.trace(Pzx * Pzx) / 2 - 1 / S**2) == 0,
)
check(
    "23 one-slot FS coefficient in y direction",
    s.simplify(s.trace(Pzy * Pzy) / 2 - 1 / S**2) == 0,
)
check(
    "24 one-slot real cross term vanishes",
    s.simplify(s.trace(Pzx * Pzy) / 2) == 0,
)

# The real curve from the note is z = tan(t).
P_tan = s.simplify(Pz.subs({x: s.tan(t), y: 0}))
dP_tan = s.simplify(s.diff(P_tan, t))
check(
    "25 z=tan(t) has unit FS speed",
    s.trigsimp(s.trace(dP_tan * dP_tan) / 2) == 1,
)

qz = s.Matrix([1, z, 0, 0, 0, 0])
check(
    "26 one-slot Plucker norm equals 1+|z|^2",
    s.simplify((qz.H * qz)[0] - S) == 0,
)

Ax = -y / S
Ay = x / S
half_dA_xy = s.simplify((s.diff(Ay, x) - s.diff(Ax, y)) / 2)
check("27 half dA equals the FS area coefficient", s.simplify(half_dA_xy - 1 / S**2) == 0)

# Exact nontrivial 2x2 chart point and two tangent directions.
Z0 = s.Matrix([[1 + I, 2 - I], [-I, 1]])
D = s.Matrix([[2, 1 + I], [-1 + 2 * I, I]])
E = s.Matrix([[1 - I, -2], [I, 3 + I]])
V0 = s.eye(2).col_join(Z0)
G0 = s.simplify(V0.H * V0)
H0 = s.simplify(s.eye(2) + Z0 * Z0.H)
Pg = s.simplify(V0 * G0.inv() * V0.H)
Q0 = s.eye(4) - Pg

check(
    "28 lower complementary block identity",
    meq(s.simplify(s.eye(2) - Z0 * G0.inv() * Z0.H), H0.inv()),
)

def projector_velocity(direction):
    dV = s.zeros(2).col_join(direction)
    first = Q0 * dV * G0.inv() * V0.H
    return s.simplify(first + first.H)


AD = projector_velocity(D)
AE = projector_velocity(E)
hDD = s.simplify(s.trace(G0.inv() * D.H * H0.inv() * D))
hDE = s.simplify(s.trace(G0.inv() * D.H * H0.inv() * E))

check(
    "29 full-chart projector speed equals closed formula",
    s.simplify(s.trace(AD * AD) / 2 - hDD) == 0,
)
check(
    "30 polarization gives the real part of the Hermitian form",
    s.simplify(s.trace(AD * AE) / 2 - (hDE + s.conjugate(hDE)) / 2) == 0,
)

minor_norm = 0
for i in range(4):
    for j in range(i + 1, 4):
        minor = V0.extract([i, j], [0, 1]).det()
        minor_norm += s.conjugate(minor) * minor

check(
    "31 Cauchy-Binet: Plucker norm equals det(V^*V)",
    s.simplify(minor_norm - G0.det()) == 0,
)

# Mixed derivative of log det G, written out algebraically.
hessian_DE = s.simplify(
    s.trace(
        G0.inv() * D.H * E
        - G0.inv() * D.H * Z0 * G0.inv() * Z0.H * E
    )
)
check(
    "32 log-det mixed derivative equals the projector Hermitian form",
    s.simplify(hessian_DE - hDE) == 0,
)

passed = sum(ok for _, ok in checks)
print(f"\n{passed}/{len(checks)} checks passed")
if passed != len(checks):
    raise SystemExit(1)
