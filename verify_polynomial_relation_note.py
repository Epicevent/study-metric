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


# 1. Veronese affine and homogeneous relations.
z = sp.symbols("z")
check("Veronese affine graph", sp.expand(z**2 - z**2) == 0)
Z0, Z1, Z2 = sp.symbols("Z0 Z1 Z2")
check(
    "Veronese homogeneous relation",
    sp.expand((Z0 * Z2 - Z1**2).subs({Z0: 1, Z1: z, Z2: z**2})) == 0,
)

# 2. All quadratic relations among (1,z,z^2): nullity one.
# Coefficients: Z0^2, Z0Z1, Z0Z2, Z1^2, Z1Z2, Z2^2.
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

# 3. Plücker coordinates from the Gaussian-eliminated chart.
a, b, c, d = sp.symbols("a b c d")
M = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])


def minor(i: int, j: int) -> sp.Expr:
    return sp.expand(M[:, [i, j]].det())


p12, p13, p14 = minor(0, 1), minor(0, 2), minor(0, 3)
p23, p24, p34 = minor(1, 2), minor(1, 3), minor(2, 3)
check("p12", p12 == 1)
check("p13", p13 == c)
check("p14", p14 == d)
check("p23", p23 == -a)
check("p24", p24 == -b)
check("p34", p34 == a * d - b * c)
plucker = sp.expand(p12 * p34 - p13 * p24 + p14 * p23)
check("Plücker relation", plucker == 0)

# 4. The first four affine outputs recover the four free inputs.
x13, x14, x23, x24, x34 = sp.symbols("x13 x14 x23 x24 x34")
recovered = {a: -x23, b: -x24, c: x13, d: x14}
graph_rhs = sp.expand((a * d - b * c).subs(recovered))
check("Graph recovery", graph_rhs == x13 * x24 - x14 * x23)

# 5. A transcendental family still satisfies the universal identity.
t = sp.symbols("t")
family = {a: sp.exp(t), b: sp.sin(t), c: t, d: sp.exp(-t)}
check("Transcendental pullback", sp.simplify(plucker.subs(family)) == 0)

# 6. Complex Cauchy-Binet, using independent symbols for conjugates.
ab, bb, cb, db = sp.symbols("ab bb cb db")
Mstar = sp.Matrix([[1, 0], [0, 1], [ab, cb], [bb, db]])
gram_det = sp.expand((M * Mstar).det())
bar_minors = [1, cb, db, -ab, -bb, ab * db - bb * cb]
sum_minor_norms = sp.expand(sum(
    p * q for p, q in zip([p12, p13, p14, p23, p24, p34], bar_minors)
))
check("Cauchy-Binet / Gram determinant", sp.expand(gram_det - sum_minor_norms) == 0)

# 7. Multiplication Sym^2 H^0(O(2)) -> H^0(O(4)).
# Domain: s0^2, s0s1, s0s2, s1^2, s1s2, s2^2.
# Target: X^4, X^3Y, X^2Y^2, XY^3, Y^4.
mult = sp.Matrix([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
])
mult_null = mult.nullspace()
check("O(2) multiplication rank", mult.rank() == 5)
check("O(2) multiplication kernel dimension", len(mult_null) == 1)
check("O(2) multiplication relation", mult_null[0] == sp.Matrix([0, 0, -1, 1, 0, 0]))

passed = sum(ok for _, ok in checks)
for name, ok in checks:
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
print(f"\n{passed}/{len(checks)} checks passed")
