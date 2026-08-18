#!/usr/bin/env python3
"""Symbolic checks for the note '다항식 관계를 모르는 상태에서'."""
from __future__ import annotations

import sympy as sp

checks: list[tuple[str, bool]] = []


def check(name: str, condition: object) -> None:
    ok = bool(condition)
    checks.append((name, ok))
    if not ok:
        raise AssertionError(name)


# ---------------------------------------------------------------------------
# 1. CP1: Veronese relation and the rank-one projector model.
# ---------------------------------------------------------------------------
z = sp.symbols("z")
check("Veronese affine graph", sp.expand(z**2 - z**2) == 0)

Z0, Z1, Z2 = sp.symbols("Z0 Z1 Z2")
check(
    "Veronese homogeneous relation",
    sp.expand((Z0 * Z2 - Z1**2).subs({Z0: 1, Z1: z, Z2: z**2})) == 0,
)

# Coefficients of Z0^2, Z0Z1, Z0Z2, Z1^2, Z1Z2, Z2^2 after
# substituting (Z0,Z1,Z2)=(1,z,z^2).
quad_map = sp.Matrix([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
])
null = quad_map.nullspace()
check("Veronese quadratic kernel dimension", len(null) == 1)
check("Veronese kernel generator", null[0] == sp.Matrix([0, 0, -1, 1, 0, 0]))

zz, zb = sp.symbols("z zb")
den = 1 + zz * zb
P = sp.Matrix([[1, zb], [zz, zz * zb]]) / den
check("CP1 projector idempotence", sp.simplify(P * P - P) == sp.zeros(2))
check("CP1 projector trace", sp.simplify(sp.trace(P) - 1) == 0)
check("CP1 projector antiholomorphic dependence", sp.simplify(sp.diff(P[0, 1], zb)) != 0)

# Formal independent symbols xbar,ybar,lambdabar avoid assumptions about
# SymPy's conjugation while checking exact scaling cancellation.
x, y, xb, yb, lam, lamb = sp.symbols("x y xb yb lam lamb", nonzero=True)
q = sp.Matrix([x, y])
qbar = sp.Matrix([[xb, yb]])
Pq = (q * qbar) / (qbar * q)[0]
q_scaled = lam * q
qbar_scaled = lamb * qbar
Pq_scaled = sp.simplify((q_scaled * qbar_scaled) / (qbar_scaled * q_scaled)[0])
check("CP1 projector scaling invariance", sp.simplify(Pq_scaled - Pq) == sp.zeros(2))

check(
    "Partial O2 coordinates identify z and minus z",
    sp.Matrix([1, zz**2]) == sp.Matrix([1, (-zz) ** 2]),
)
check("Complete O2 system recovers the affine coordinate", sp.simplify(zz / 1 - zz) == 0)


# ---------------------------------------------------------------------------
# 2. Gr(2,4): RREF coordinates, maximal minors, wedge reconstruction.
# ---------------------------------------------------------------------------
a, b, c, d = sp.symbols("a b c d")
A = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])


def minor(matrix: sp.Matrix, i: int, j: int) -> sp.Expr:
    return sp.expand(matrix[:, [i, j]].det())


plucker_coordinates = [
    minor(A, 0, 1),
    minor(A, 0, 2),
    minor(A, 0, 3),
    minor(A, 1, 2),
    minor(A, 1, 3),
    minor(A, 2, 3),
]
expected = [1, c, d, -a, -b, a * d - b * c]
for name, value, target in zip(
    ["p12", "p13", "p14", "p23", "p24", "p34"],
    plucker_coordinates,
    expected,
):
    check(name, sp.expand(value - target) == 0)

p12, p13, p14, p23, p24, p34 = plucker_coordinates
plucker_relation = sp.expand(p12 * p34 - p13 * p24 + p14 * p23)
check("Plucker relation", plucker_relation == 0)

# Row-basis change gives the same determinant weight to every maximal minor.
g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
g = sp.Matrix([[g11, g12], [g21, g22]])
gA = g * A
det_g = sp.expand(g.det())
changed_coordinates = [
    minor(gA, 0, 1),
    minor(gA, 0, 2),
    minor(gA, 0, 3),
    minor(gA, 1, 2),
    minor(gA, 1, 3),
    minor(gA, 2, 3),
]
check(
    "All maximal minors have determinant weight",
    all(
        sp.expand(changed - det_g * original) == 0
        for changed, original in zip(changed_coordinates, plucker_coordinates)
    ),
)

# Coefficients of v wedge omega in the bases e123,e124,e134,e234.
wedge_matrix = sp.Matrix([
    [p23, -p13, p12, 0],
    [p24, -p14, 0, p12],
    [p34, 0, -p14, p13],
    [0, p34, -p24, p23],
])
r1 = sp.Matrix([1, 0, a, b])
r2 = sp.Matrix([0, 1, c, d])
check("Wedge annihilates first basis vector", sp.simplify(wedge_matrix * r1) == sp.zeros(4, 1))
check("Wedge annihilates second basis vector", sp.simplify(wedge_matrix * r2) == sp.zeros(4, 1))
check("Wedge reconstruction has two-dimensional kernel", wedge_matrix.rank() == 2)

x13, x14, x23, x24, x34 = sp.symbols("x13 x14 x23 x24 x34")
recovered = {a: -x23, b: -x24, c: x13, d: x14}
graph_rhs = sp.expand((a * d - b * c).subs(recovered))
check("Local graph recovery", graph_rhs == x13 * x24 - x14 * x23)

# A transcendental parameterization still obeys the universal identity.
t = sp.symbols("t")
family = {a: sp.exp(t), b: sp.sin(t), c: t, d: sp.exp(-t)}
check("Transcendental pullback", sp.simplify(plucker_relation.subs(family)) == 0)


# ---------------------------------------------------------------------------
# 3. Projectors: complete invariance, extra complement data, symmetry class.
# ---------------------------------------------------------------------------
tau = sp.symbols("tau")
P_tau = sp.Matrix([[1, tau], [0, 0]])
check("Complex idempotent family", P_tau * P_tau == P_tau)
check("Idempotent family has common image vector", P_tau * sp.Matrix([1, 0]) == sp.Matrix([1, 0]))
check("Idempotent family has varying kernel vector", P_tau * sp.Matrix([-tau, 1]) == sp.zeros(2, 1))

# Exact rational example for the Grassmann projector.
M = sp.Matrix([[1, 0], [0, 1], [1, 2], [3, 4]])
g_exact = sp.Matrix([[2, 1], [1, 1]])


def projector(frame: sp.Matrix) -> sp.Matrix:
    return sp.simplify(frame * (frame.T * frame).inv() * frame.T)


P_M = projector(M)
check("Grassmann projector basis invariance", sp.simplify(projector(M * g_exact) - P_M) == sp.zeros(4))

U = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
check("Projector orthogonal equivariance", sp.simplify(projector(U * M) - U * P_M * U.T) == sp.zeros(4))

h = sp.diag(2, 1, 1, 1)
check(
    "Projector is not generally GL-equivariant",
    sp.simplify(projector(h * M) - h * P_M * h.inv()) != sp.zeros(4),
)


# ---------------------------------------------------------------------------
# 4. Metric meeting point: Cauchy-Binet and the common tangent metric.
# ---------------------------------------------------------------------------
ab, bb, cb, db = sp.symbols("ab bb cb db")
A_star = sp.Matrix([[1, 0], [0, 1], [ab, cb], [bb, db]])
gram_det = sp.expand((A * A_star).det())
bar_minors = [1, cb, db, -ab, -bb, ab * db - bb * cb]
sum_minor_norms = sp.expand(
    sum(p * qbar for p, qbar in zip(plucker_coordinates, bar_minors))
)
check("Cauchy-Binet / Gram determinant", sp.expand(gram_det - sum_minor_norms) == 0)

u, v, w, x0, ub, vb, wb, xb0 = sp.symbols("u v w x0 ub vb wb xb0")
D = sp.Matrix([[u, v], [w, x0]])
D_dagger = sp.Matrix([[ub, wb], [vb, xb0]])
zero = sp.zeros(2)
dP = zero.row_join(D_dagger).col_join(D.row_join(zero))
projector_metric = sp.expand(sp.trace(dP * dP) / 2)
expected_metric = sp.expand(sp.trace(D_dagger * D))
check("Projector metric at the origin", sp.expand(projector_metric - expected_metric) == 0)

epsilon = sp.symbols("epsilon")
potential = sp.log((sp.eye(2) + epsilon**2 * (D_dagger * D)).det())
quadratic_coefficient = sp.simplify(sp.diff(potential, epsilon, 2).subs(epsilon, 0) / 2)
check("Plucker potential metric at the origin", sp.expand(quadratic_coefficient - expected_metric) == 0)


# ---------------------------------------------------------------------------
# 5. Section multiplication: the conic relation as a kernel.
# ---------------------------------------------------------------------------
mult = quad_map
mult_null = mult.nullspace()
check("O2 multiplication rank", mult.rank() == 5)
check("O2 multiplication kernel dimension", len(mult_null) == 1)
check("O2 multiplication relation", mult_null[0] == sp.Matrix([0, 0, -1, 1, 0, 0]))


passed = sum(ok for _, ok in checks)
for name, ok in checks:
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
print(f"\n{passed}/{len(checks)} checks passed")
