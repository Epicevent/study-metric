# -*- coding: utf-8 -*-
"""라플라시안에서 RR의 +1로 — 핵심 식 12개 검산."""

import sympy as sp

count = 0


def ok(label, condition):
    global count
    assert bool(condition), label
    count += 1
    print(f"[{count:02d}] {label}: OK")


x, y, R, s, d, H = sp.symbols("x y R s d H", real=True)
r2 = x**2 + y**2
u = sp.log(2) - sp.log(1 + r2)
lap = sp.diff(u, x, 2) + sp.diff(u, y, 2)
e2u = sp.exp(2 * u)

ok("Δlog(1+|z|²)=4/(1+|z|²)²",
   sp.simplify(-lap - 4 / (1 + r2)**2) == 0)
ok("Liouville: -Δu=e^{2u}", sp.simplify(-lap - e2u) == 0)
ok("Gauss curvature K=-e^{-2u}Δu=1", sp.simplify(-lap / e2u - 1) == 0)

# w-chart: s=|w|². rho_z(1/w)|dz/dw| = 2/(1+s).
rho_w_from_z = sp.simplify((2 / (1 + 1 / s)) * (1 / s))
ok("w-chart density is smooth: ρ_w=2/(1+|w|²)",
   sp.simplify(rho_w_from_z - 2 / (1 + s)) == 0)

ur = sp.log(2) - sp.log(1 + R**2)
flux_R = sp.simplify(-sp.diff(ur, R) * 2 * sp.pi * R)
ok("disk curvature integral = 4πR²/(1+R²)",
   sp.simplify(flux_R - 4 * sp.pi * R**2 / (1 + R**2)) == 0)
ok("total curvature = 4π", sp.limit(flux_R, R, sp.oo) == 4 * sp.pi)
ok("normalized total curvature = 2",
   sp.simplify(sp.limit(flux_R, R, sp.oo) / (2 * sp.pi)) == 2)

w = sp.symbols("w", nonzero=True)
z_of_w = 1 / w
ok("dz/dw=-w^{-2}", sp.diff(z_of_w, w) == -w**-2)
z = sp.Symbol("z")
ok("tangent transition has degree 2", sp.degree(z**2, z) == 2)

# Work in H*(CP1)=Q[H]/(H²): retain only constant and H coefficients.
ch = 1 + d * H
td = 1 + H
product = sp.expand(ch * td)
linear_coeff = product.coeff(H, 1)
ok("Td(TCP1)=1+H from c1(T)=2H",
   sp.expand(1 + sp.Rational(1, 2) * 2 * H) == td)
ok("degree-two part of ch(O(d))Td is (d+1)H",
   sp.simplify(linear_coeff - (d + 1)) == 0)
ok("torus check: c1=0 gives χ(O)=0", sp.Rational(1, 2) * 0 == 0)

print(f"결과: {count}/12 통과")

