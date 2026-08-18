#!/usr/bin/env python3
"""Finite checks for the calculation-first note.

This script checks byte integrity and the algebraic calculations explicitly
performed in the note. It does not claim to prove the analytic input theorems
about the Weierstrass function or compact Riemann surfaces.
"""
from __future__ import annotations

from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "이해를_후일로_미루지_않기_세토이모델_실제계산.md"

checks: list[tuple[str, bool]] = []


def check(name: str, condition: object) -> None:
    ok = bool(condition)
    checks.append((name, ok))
    if not ok:
        raise AssertionError(name)


# ---------------------------------------------------------------------------
# 1. Source integrity and site-shell checks.
# ---------------------------------------------------------------------------
text = SOURCE.read_text(encoding="utf-8")
bs = chr(92)

check("no form-feed corruption", chr(12) not in text)
standalone = sum(line.strip() == "$$" for line in text.splitlines())
check("paired display-math delimiters", standalone % 2 == 0 and standalone > 0)
check("conic affine ratio preserved", "u=" + bs + "frac{Z_1}{Z_0}" in text)
check("torus test variable preserved", "u" + bs + "longmapsto" + bs + "wp(u)-" + bs + "wp(z)" in text)
check("Plucker affine ratios preserved", "u_{ij}=" + bs + "frac{p_{ij}}{p_{12}}" in text)


# ---------------------------------------------------------------------------
# 2. P1 / Veronese calculations.
# ---------------------------------------------------------------------------
z = sp.symbols("z")
Z0, Z1, Z2 = sp.symbols("Z0 Z1 Z2")
veronese = sp.expand((Z0 * Z2 - Z1**2).subs({Z0: 1, Z1: z, Z2: z**2}))
check("Veronese relation", veronese == 0)
check("incomplete system identifies z and minus z", sp.Matrix([1, z**2]) == sp.Matrix([1, (-z) ** 2]))
check("Veronese tangent never vanishes on finite chart", sp.Matrix([1, 2 * z]) != sp.zeros(2, 1))
w = sp.symbols("w")
check("Veronese tangent at infinity chart", sp.Matrix([2 * w, 1]).subs(w, 0) != sp.zeros(2, 1))

quad_map = sp.Matrix([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
])
null = quad_map.nullspace()
check("quadratic kernel has dimension one", len(null) == 1)
check("quadratic kernel generator", null[0] == sp.Matrix([0, 0, -1, 1, 0, 0]))


# ---------------------------------------------------------------------------
# 3. Formal Laurent cancellation in the Weierstrass relation.
# ---------------------------------------------------------------------------
t, g2, g3 = sp.symbols("t g2 g3")
wp = t**-2 + g2 * t**2 / 20 + g3 * t**4 / 28
wpp = -2 * t**-3 + g2 * t / 10 + g3 * t**3 / 7
H = sp.expand(wpp**2 - 4 * wp**3 + g2 * wp + g3)
check("Weierstrass z^-6 coefficient cancels", sp.expand(H).coeff(t, -6) == 0)
check("Weierstrass z^-2 coefficient cancels", sp.expand(H).coeff(t, -2) == 0)
check("Weierstrass constant coefficient cancels", sp.expand(H).coeff(t, 0) == 0)
check("formal wp is even", sp.expand(wp.subs(t, -t) - wp) == 0)
check("formal wp prime is odd", sp.expand(wpp.subs(t, -t) + wpp) == 0)


# ---------------------------------------------------------------------------
# 4. Gr(2,4): maximal minors, projector, graph kernel.
# ---------------------------------------------------------------------------
a, b, c, d = sp.symbols("a b c d")
A = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])


def minor(matrix: sp.Matrix, i: int, j: int) -> sp.Expr:
    return sp.expand(matrix[:, [i, j]].det())


p12, p13, p14 = minor(A, 0, 1), minor(A, 0, 2), minor(A, 0, 3)
p23, p24, p34 = minor(A, 1, 2), minor(A, 1, 3), minor(A, 2, 3)
check("six RREF minors", [p12, p13, p14, p23, p24, p34] == [1, c, d, -a, -b, a * d - b * c])
check("Plucker relation", sp.expand(p12 * p34 - p13 * p24 + p14 * p23) == 0)

x13, x14, x23, x24 = sp.symbols("x13 x14 x23 x24")
recovered = sp.expand((a * d - b * c).subs({a: -x23, b: -x24, c: x13, d: x14}))
check("local graph formula", recovered == x13 * x24 - x14 * x23)

# Exact rational frame for basis-change invariance of the orthogonal projector.
M = sp.Matrix([[1, 0], [0, 1], [1, 2], [3, 4]])
g = sp.Matrix([[2, 1], [1, 1]])


def projector(frame: sp.Matrix) -> sp.Matrix:
    return sp.simplify(frame * (frame.T * frame).inv() * frame.T)


check("projector basis invariance", sp.simplify(projector(M * g) - projector(M)) == sp.zeros(4))

# Every maximal minor acquires the same determinant weight under row-basis change.
g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
G = sp.Matrix([[g11, g12], [g21, g22]])
GA = G * A
detG = sp.expand(G.det())
original = [p12, p13, p14, p23, p24, p34]
changed = [minor(GA, 0, 1), minor(GA, 0, 2), minor(GA, 0, 3), minor(GA, 1, 2), minor(GA, 1, 3), minor(GA, 2, 3)]
check("all minors have determinant weight", all(sp.expand(q - detG * p) == 0 for q, p in zip(changed, original)))

passed = sum(ok for _, ok in checks)
for name, ok in checks:
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
print(f"\n{passed}/{len(checks)} finite checks passed")
