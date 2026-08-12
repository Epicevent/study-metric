"""Independent checks for 계수합0에서_line_bundle까지.md."""

from __future__ import annotations

import sympy as sp


z, w, r, R = sp.symbols("z w r R", positive=True)
zc = sp.symbols("z")
f = zc * (zc - 1) ** 2 / (zc - 2) ** 2

checks: list[tuple[str, bool]] = []


def record(name: str, condition: object) -> None:
    checks.append((name, bool(condition)))


# §0: exact local orders and leading coefficients.
record("ord_0 leading coefficient", sp.limit(f / zc, zc, 0) == sp.Rational(1, 4))
record("ord_1 leading coefficient", sp.limit(f / (zc - 1) ** 2, zc, 1) == 1)
record("ord_2 pole coefficient", sp.limit((zc - 2) ** 2 * f, zc, 2) == 2)

f_at_infinity = sp.factor(f.subs(zc, 1 / w))
record("infinity normal form", sp.simplify(f_at_infinity - (1 / w) * (1 - w) ** 2 / (1 - 2 * w) ** 2) == 0)
record("ord_infinity leading coefficient", sp.limit(w * f_at_infinity, w, 0) == 1)
record("divisor degree zero", 1 + 2 - 2 - 1 == 0)

# §1: logarithmic derivative and residues.
log_derivative = sp.cancel(sp.diff(f, zc) / f)
expected_log_derivative = 1 / zc + 2 / (zc - 1) - 2 / (zc - 2)
record("df/f partial fractions", sp.simplify(log_derivative - expected_log_derivative) == 0)
record("residue at 0", sp.residue(log_derivative, zc, 0) == 1)
record("residue at 1", sp.residue(log_derivative, zc, 1) == 2)
record("residue at 2", sp.residue(log_derivative, zc, 2) == -2)
record("residue at infinity", sp.residue(-log_derivative.subs(zc, 1 / w) / w**2, w, 0) == -1)
record("all residues sum zero", sum([1, 2, -2, -1]) == 0)
record("large-circle degree one", sp.limit(f / zc, zc, sp.oo) == 1)

# §6: Fubini--Study potential, transition, and normalized mass.
laplacian_radial = sp.diff(sp.log(1 + r**2), r, 2) + sp.diff(sp.log(1 + r**2), r) / r
record("Delta log(1+r^2)", sp.simplify(laplacian_radial - 4 / (1 + r**2) ** 2) == 0)

h0 = 1 / (1 + R**2)
h_inf = 1 / (1 + 1 / R**2)
record("metric transition h_inf=|z|^2 h_0", sp.simplify(h_inf - R**2 * h0) == 0)

K0 = sp.log(1 + R**2)
K_inf = sp.log(1 + 1 / R**2)
record("potential transition", sp.simplify(sp.expand_log(K0 - K_inf, force=True) - sp.log(R**2)) == 0)

fs_mass = sp.integrate(2 * r / (1 + r**2) ** 2, (r, 0, sp.oo))
record("normalized FS mass", fs_mass == 1)

# §7: Poincare--Lelong mass balance in O(1) and O(2).
record("O(1) zero-curvature balance", 1 - fs_mass == 0)
record("O(2) zero-curvature balance", 2 - 2 * fs_mass == 0)

failed = [name for name, ok in checks if not ok]
for index, (name, ok) in enumerate(checks, start=1):
    print(f"[{index:02d}] {'PASS' if ok else 'FAIL'}  {name}")

if failed:
    raise SystemExit(f"{len(failed)} failed: {', '.join(failed)}")

print(f"\n{len(checks)}/{len(checks)} checks passed.")
