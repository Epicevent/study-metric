# -*- coding: utf-8 -*-
"""Self-contained Plücker/Mayer--Vietoris/Chern/Ricci note checks."""
from __future__ import annotations
import sympy as sp

checks: list[tuple[str, bool]] = []

def check(name: str, expr) -> None:
    ok = bool(expr) if isinstance(expr, (bool, sp.logic.boolalg.Boolean)) else sp.simplify(expr) == 0
    checks.append((name, ok))
    print(f"[{'OK' if ok else 'FAIL'}] {name}")
    if not ok:
        raise AssertionError(name)

# ------------------------------------------------------------------ Plücker
la, lb, lc, ld = sp.symbols('la lb lc ld')
L = sp.Matrix([[la, lb], [lc, ld]])
detL = sp.det(L)
a = sp.symbols('a1:5')
b = sp.symbols('b1:5')
A = sp.Matrix([a, b])
LA = L*A
pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for i,j in pairs:
    pA = sp.det(A[:,[i,j]])
    pLA = sp.det(LA[:,[i,j]])
    check(f"minor ({i+1},{j+1}) scales by det L", pLA-detL*pA)

x,y,z,w = sp.symbols('x y z w')
A0 = sp.Matrix([[1,0,x,y],[0,1,z,w]])
p = [sp.det(A0[:,[i,j]]) for i,j in pairs]
check("Gaussian chart minors", sp.Matrix(p)-sp.Matrix([1,z,w,-x,-y,x*w-y*z]) == sp.zeros(6,1))
check("Plücker relation in p12 chart", p[0]*p[5]-p[1]*p[4]+p[2]*p[3])

J = sp.Matrix([[0,1],[-1,0]])
check("G^T J G = det(G)J", L.T*J*L-detL*J == sp.zeros(2))
P = sp.simplify(A.T*J*A)
for idx,(i,j) in enumerate(pairs):
    check(f"A^T J A entry ({i+1},{j+1}) is minor", P[i,j]-sp.det(A[:,[i,j]]))

# conic
X,Y = sp.symbols('X Y')
Aq,Bq,Cq = X**2, X*Y, Y**2
check("conic determinant relation", Aq*Cq-Bq**2)

# ------------------------------------------------------------------ complex calculus / FS / Chern
zr, zi, n = sp.symbols('x y n', real=True)
S = 1+zr**2+zi**2
Acoef_x = -n*zi/S   # coefficient of dx
Acoef_y = n*zr/S    # coefficient of dy
Fcoef = sp.diff(Acoef_y,zr)-sp.diff(Acoef_x,zi)
check("O(n) curvature coefficient", Fcoef-2*n/S**2)
radial = sp.integrate(2*sp.symbols('r', positive=True)/(1+sp.symbols('r', positive=True)**2)**2, (sp.symbols('r', positive=True),0,sp.oo))
check("FS radial integral", radial-1)

zz, zb = sp.symbols('z zb')
Sc = 1+zz*zb
gcp1 = sp.diff(sp.diff(sp.log(Sc), zb), zz)
check("CP1 FS Hessian", gcp1-Sc**-2)
riccp1 = -sp.diff(sp.diff(sp.log(gcp1),zb),zz)
check("CP1 Ricci coefficient 2", riccp1-2*Sc**-2)
check("normalized Veronese norm", 1+2*zz*zb+(zz*zb)**2-Sc**2)

# Gaussian curvature
lam = 2/S**2
laplog = sp.diff(sp.log(lam),zr,2)+sp.diff(sp.log(lam),zi,2)
check("Gaussian curvature of CP1 is 2", -laplog/(2*lam)-2)

# ------------------------------------------------------------------ Mayer--Vietoris
rU,rV,c = sp.symbols('rhoU rhoV c')
check("partition algebra", sp.expand(((rU+rV)*c-c).subs(rV,1-rU)))
check("angle jump gives 2pi", (0-(-2*sp.pi))-2*sp.pi)
r = sp.symbols('r', positive=True)
A0theta = n*r**2/(1+r**2)
Aitheta = -n/(1+r**2)
check("local connections differ by n dtheta", A0theta-Aitheta-n)
check("radial curvature derivative", sp.diff(A0theta,r)-2*n*r/(1+r**2)**2)

# ------------------------------------------------------------------ Torus complex coordinate
Tau,Tb,Aper,Bper = sp.symbols('tau taub A B')
coef_z = (-Aper*Tb+Bper)/(Tau-Tb)
coef_b = (Aper*Tau-Bper)/(Tau-Tb)
check("recover ds coefficient", coef_z+coef_b-Aper)
check("recover dt coefficient", Tau*coef_z+Tb*coef_b-Bper)
check("integer a class maps to tau", (Tau-Tb)*coef_b.subs({Aper:1,Bper:0})-Tau)
check("integer b class maps to -1", (Tau-Tb)*coef_b.subs({Aper:0,Bper:1})+1)

# ------------------------------------------------------------------ Cauchy--Binet / Gr metric determinant
xb,yb,zbv,wb = sp.symbols('xb yb zb wb')
Z = sp.Matrix([[x,y],[z,w]])
Zdag = sp.Matrix([[xb,zbv],[yb,wb]])
G = sp.eye(2)+Z*Zdag
F = sp.eye(2)+Zdag*Z
K1 = sp.expand(sp.det(G))
K2 = sp.expand(sp.det(F))
check("det(I+ZZ*) = det(I+Z*Z)", K1-K2)
Kpl = 1+x*xb+y*yb+z*zbv+w*wb+(x*w-y*z)*(xb*wb-yb*zbv)
check("Cauchy-Binet chart potential", K1-Kpl)

# inverse identity and metric determinant at exact sample points
for idx, Zn in enumerate([
    sp.Matrix([[1,2],[3,4]]),
    sp.Matrix([[sp.Rational(1,2),-1],[2,sp.Rational(3,2)]]),
    sp.Matrix([[0,1],[-2,3]]),
], 1):
    Gnum = sp.eye(2)+Zn*Zn.T
    Fnum = sp.eye(2)+Zn.T*Zn
    Wnum = sp.eye(2)-Zn.T*Gnum.inv()*Zn-Fnum.inv()
    check(f"Woodbury identity sample {idx}", all(sp.simplify(e)==0 for e in Wnum))
    Mnum = sp.kronecker_product(Gnum.inv().T,Fnum.inv())
    Knum = sp.det(Gnum)
    check(f"Gr metric determinant sample {idx}", sp.det(Mnum)*Knum**4-1)

# abstract Kronecker determinant exponent
f1,f2,g1,g2 = sp.symbols('f1 f2 g1 g2', nonzero=True)
Mdiag = sp.diag(1/(g1*f1),1/(g1*f2),1/(g2*f1),1/(g2*f2))
check("Kronecker determinant exponents", sp.det(Mdiag)-1/((g1*g2)**2*(f1*f2)**2))

# Schubert line
q,qb = sp.symbols('q qb')
As = sp.Matrix([[1,0,0,0],[0,1,q,0]])
Asdag = sp.Matrix([[1,0],[0,1],[0,qb],[0,0]])
check("Schubert line potential", sp.det(As*Asdag)-(1+q*qb))

passed = sum(ok for _,ok in checks)
print(f"\nALL CHECKS PASSED: {passed}/{len(checks)}")
