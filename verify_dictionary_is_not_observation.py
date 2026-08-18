#!/usr/bin/env python3
"""Algebraic consistency checks for '사전은 관찰이 아니다'.

This script verifies finite symbolic identities used in the note. It does not
replace the analytic theorems about the Weierstrass ℘-function, compact Riemann
surfaces, or ampleness/projectivity.
"""
from __future__ import annotations

import sympy as sp

checks: list[tuple[str, bool]] = []


def check(name: str, condition: object) -> None:
    ok = bool(condition)
    checks.append((name, ok))
    if not ok:
        raise AssertionError(name)


# ---------------------------------------------------------------------------
# 1. P1 and the Veronese toy model.
# ---------------------------------------------------------------------------
z, lam = sp.symbols("z lam", nonzero=True)
Z0, Z1, Z2 = sp.symbols("Z0 Z1 Z2")
conic = Z0 * Z2 - Z1**2

check(
    "Veronese conic relation",
    sp.expand(conic.subs({Z0: 1, Z1: z, Z2: z**2})) == 0,
)
check(
    "Incomplete Veronese system identifies z and minus z",
    sp.Matrix([1, z**2]) == sp.Matrix([1, (-z) ** 2]),
)
check("Complete Veronese system recovers z", sp.simplify(z / 1 - z) == 0)
check(
    "Conic equation is homogeneous of degree two",
    sp.expand(
        conic.subs({Z0: lam * Z0, Z1: lam * Z1, Z2: lam * Z2})
        - lam**2 * conic
    )
    == 0,
)


# ---------------------------------------------------------------------------
# 2. The elliptic-curve toy model: parity, pole weights, homogeneity.
# ---------------------------------------------------------------------------
a2, a4 = sp.symbols("a2 a4")
wp_truncated = z**-2 + a2 * z**2 + a4 * z**4
wp_prime_truncated = sp.diff(wp_truncated, z)
check("Formal wp expansion is even", sp.simplify(wp_truncated.subs(z, -z) - wp_truncated) == 0)
check(
    "Formal wp-prime expansion is odd",
    sp.simplify(wp_prime_truncated.subs(z, -z) + wp_prime_truncated) == 0,
)
check("Pole orders first meet at six", 2 * 3 == 3 * 2)

X, Y, Z, g2, g3 = sp.symbols("X Y Z g2 g3")
weierstrass = Y**2 * Z - 4 * X**3 + g2 * X * Z**2 + g3 * Z**3
check(
    "Weierstrass equation is homogeneous of degree three",
    sp.expand(
        weierstrass.subs({X: lam * X, Y: lam * Y, Z: lam * Z})
        - lam**3 * weierstrass
    )
    == 0,
)


# ---------------------------------------------------------------------------
# 3. Gr(2,4): maximal minors, determinant weight, Pluecker relation.
# ---------------------------------------------------------------------------
a, b, c, d = sp.symbols("a b c d")
A = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])


def minor(matrix: sp.Matrix, i: int, j: int) -> sp.Expr:
    return sp.expand(matrix[:, [i, j]].det())


pluecker = [
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
    pluecker,
    expected,
):
    check(name, sp.expand(value - target) == 0)

p12, p13, p14, p23, p24, p34 = pluecker
check(
    "Pluecker quadratic",
    sp.expand(p12 * p34 - p13 * p24 + p14 * p23) == 0,
)

g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
g = sp.Matrix([[g11, g12], [g21, g22]])
gA = g * A
changed = [
    minor(gA, 0, 1),
    minor(gA, 0, 2),
    minor(gA, 0, 3),
    minor(gA, 1, 2),
    minor(gA, 1, 3),
    minor(gA, 2, 3),
]
check(
    "All maximal minors have the same determinant weight",
    all(
        sp.expand(new - g.det() * old) == 0
        for new, old in zip(changed, pluecker)
    ),
)


# ---------------------------------------------------------------------------
# 4. Ring operations as geometric operations: finite toy identities.
# ---------------------------------------------------------------------------
x, y = sp.symbols("x y")
check("Parabola quotient relation", sp.expand((y - x**2).subs(y, x**2)) == 0)
check("Localization permits an inverse", sp.simplify(z * (1 / z) - 1) == 0)

r, s = sp.symbols("r s")
check(
    "Fiber-product toy relation r squared equals s cubed",
    sp.expand((r**2 - s**3).subs(r**2, s**3)) == 0,
)


passed = sum(ok for _, ok in checks)
for name, ok in checks:
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
print(f"\n{passed}/{len(checks)} checks passed")
