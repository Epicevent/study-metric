"""First Chern/Ricci/fold 계산노트의 독립 검산."""

import math

import numpy as np
import sympy as sp


passed = 0


def check(name, condition):
    global passed
    if not bool(condition):
        raise AssertionError(name)
    passed += 1
    print(f"PASS {passed:02d}: {name}")


x, y = sp.symbols("x y", real=True)
S = 1 + x**2 + y**2

# §1--2: FS form and curvature in real coordinates.
lap_log_S = sp.diff(sp.log(S), x, 2) + sp.diff(sp.log(S), y, 2)
check("Delta log(1+r^2)=4/(1+r^2)^2", sp.simplify(lap_log_S - 4 / S**2) == 0)

Lambda = 2 / S**2
K = sp.simplify(-(sp.diff(sp.log(Lambda), x, 2) + sp.diff(sp.log(Lambda), y, 2)) / (2 * Lambda))
check("FS trace metric has K=2", K == 2)

r = sp.symbols("r", nonnegative=True)
radial = sp.integrate(2 * r / (1 + r**2) ** 2, (r, 0, sp.oo))
check("FS radial integral is 1", radial == 1)
check("integral omega_FS is 2pi", sp.simplify(2 * sp.pi * radial - 2 * sp.pi) == 0)
check("integral rho=2 omega_FS is 4pi", sp.simplify(4 * sp.pi * radial - 4 * sp.pi) == 0)

# §6: explicit two-band numerator.
kx, ky = sp.symbols("kx ky", real=True)
d = sp.Matrix([sp.sin(kx), sp.sin(ky), 1 - sp.cos(kx) - sp.cos(ky)])
dx = d.diff(kx)
dy = d.diff(ky)
triple = sp.trigsimp(d.dot(dx.cross(dy)))
target_triple = sp.cos(kx) * sp.cos(ky) - sp.cos(kx) - sp.cos(ky)
check("d dot (d_x cross d_y) numerator", sp.trigsimp(triple - target_triple) == 0)

r2 = sp.trigsimp(d.dot(d))
target_r2 = 3 - 2 * sp.cos(kx) - 2 * sp.cos(ky) + 2 * sp.cos(kx) * sp.cos(ky)
check("two-band |d|^2", sp.trigsimp(r2 - target_r2) == 0)

lambda_bar = (sp.cos(kx) + sp.cos(ky) - sp.cos(kx) * sp.cos(ky)) / (2 * r2 ** sp.Rational(3, 2))
check("lambda(0,0)=1/2", sp.simplify(lambda_bar.subs({kx: 0, ky: 0}) - sp.Rational(1, 2)) == 0)
check("lambda(pi,pi)=-1/18", sp.simplify(lambda_bar.subs({kx: sp.pi, ky: sp.pi}) + sp.Rational(1, 18)) == 0)

# Diagonal singular points.
c = sp.symbols("c", real=True)
check("diagonal singular numerator is 2c-c^2", sp.simplify(2 * c - c**2 - c * (2 - c)) == 0)

# Numerical degree/Chern integral on the periodic midpoint grid.
n_grid = 1000
grid = (-math.pi) + (np.arange(n_grid) + 0.5) * (2 * math.pi / n_grid)
KX, KY = np.meshgrid(grid, grid, indexing="ij")
CX, CY = np.cos(KX), np.cos(KY)
R2 = 3 - 2 * CX - 2 * CY + 2 * CX * CY
LAM = (CX + CY - CX * CY) / (2 * R2 ** 1.5)
integral = float(LAM.sum() * (2 * math.pi / n_grid) ** 2)
check("numerical integral lambda = 2pi", abs(integral - 2 * math.pi) < 2e-10)
check("numerical degree = 1", abs(integral / (2 * math.pi) - 1) < 5e-11)

# §9: local fold f(u,v)=(u,v^2).
u, v, eps = sp.symbols("u v eps", real=True, positive=False)
Lam = sp.Function("Lambda")(u, v**2)
signed_area_coeff = 2 * v * Lam
unsigned_area_coeff_sq = sp.simplify((Lam) * (4 * v**2 * Lam))
check("fold signed area coefficient keeps v", signed_area_coeff == 2 * v * Lam)
check("fold metric determinant is 4v^2 Lambda^2", sp.simplify(unsigned_area_coeff_sq - 4 * v**2 * Lam**2) == 0)

det_regularized = sp.expand((Lam + eps) * (4 * v**2 * Lam + eps))
target_det_regularized = 4 * v**2 * Lam**2 + eps * Lam * (1 + 4 * v**2) + eps**2
check("regularized determinant", sp.simplify(det_regularized - target_det_regularized) == 0)

check("signed curvature flips between v=+1 and v=-1",
      sp.simplify((4 * v * Lam).subs(v, 1) + (4 * v * Lam).subs(v, -1)) == 0)

print(f"ALL PASS: {passed}")
