# -*- coding: utf-8 -*-
# 파트 IV 완전 상세 (Reeb벡터장_완전계산.md) 의 등식 검산  (요구: pip install sympy)
import sympy as sp

ok = lambda name, cond: print(("[OK] " if cond else "[FAIL] ") + name)

x1, y1, x2, y2, th = sp.symbols('x1 y1 x2 y2 theta', real=True)
X = [x1, y1, x2, y2]
R = [-y1, x1, -y2, x2]            # R_alpha 계수 (dx1,dy1,dx2,dy2 순)
alpha = [-y1, x1, -y2, x2]        # α = Σ(x dy - y dx) 의 [dx1,dy1,dx2,dy2] 계수
N = x1**2 + y1**2 + x2**2 + y2**2

# §2 G1: (i/2)(z dz̄ − z̄ dz) = x dy − y dx  (성분 하나로)
z = x1 + sp.I*y1
# dz̄, dz 를 (dx, dy) 기저의 복소계수 [1, -i], [1, i] 로 표현해 계산
zdzbar = [sp.expand(z*1), sp.expand(z*(-sp.I))]          # z dz̄ 의 (dx, dy) 계수
zbardz = [sp.expand(sp.conjugate(z)*1), sp.expand(sp.conjugate(z)*sp.I)]
comb = [sp.expand(sp.I/2*(a - b)) for a, b in zip(zdzbar, zbardz)]
ok("§2a (i/2)(z dz̄ − z̄ dz) = x dy − y dx", sp.simplify(comb[0] + y1) == 0 and sp.simplify(comb[1] - x1) == 0)
ok("§2b 괄호는 순허수 (켤레 = −자신)",
   all(sp.simplify(sp.conjugate(a - b) + (a - b)) == 0 for a, b in zip(zdzbar, zbardz)))

# §3 생성원
g = sp.exp(sp.I*th)*z
v = sp.diff(g, th).subs(th, 0)
ok("§3d d/dθ e^{iθ}z|₀ = iz = −y + ix", sp.simplify(sp.re(v) + y1) == 0 and sp.simplify(sp.im(v) - x1) == 0)
Xr = x1*sp.cos(th) - y1*sp.sin(th); Yr = x1*sp.sin(th) + y1*sp.cos(th)
ok("§3b X'(θ), Y'(θ)", sp.simplify(sp.diff(Xr, th) + x1*sp.sin(th) + y1*sp.cos(th)) == 0
   and sp.simplify(sp.diff(Yr, th) - x1*sp.cos(th) + y1*sp.sin(th)) == 0)
ok("§3e 궤도 norm 보존", sp.simplify(Xr**2 + Yr**2 - (x1**2 + y1**2)) == 0)
ok("§3f |R|² = N", sp.simplify(sum(r**2 for r in R) - N) == 0)

# §5 α(R) = N
aR = sum(a*r for a, r in zip(alpha, R))
ok("§5 α(R) = ‖v‖²", sp.simplify(aR - N) == 0)

# §6 수직/수평 분해: α(V − α(V)R) = α(V)(1−N)
u1, u2, u3, u4 = sp.symbols('u1 u2 u3 u4', real=True)
V = [u1, u2, u3, u4]
aV = sum(a*w for a, w in zip(alpha, V))
H = [w - aV*r for w, r in zip(V, R)]
aH = sum(a*h for a, h in zip(alpha, H))
ok("§6a α(V − α(V)R) = α(V)(1−N)", sp.simplify(aH - aV*(1 - N)) == 0)

# §6b 숫자: p=(1/2,1/2,1/2,1/2), V=∂x1−∂y1 → α(V)=−1, H=V+R, α(H)=0, dN(H)=0
half = sp.Rational(1, 2)
pt = {x1: half, y1: half, x2: half, y2: half}
Vnum = [1, -1, 0, 0]
aVnum = sum(a.subs(pt)*w for a, w in zip(alpha, Vnum))
Rnum = [r.subs(pt) for r in R]
Hnum = [w - aVnum*r for w, r in zip(Vnum, Rnum)]
dN = [sp.diff(N, xi) for xi in X]
ok("§6b α(V)=−1, H=(1/2,−1/2,−1/2,1/2), α(H)=0, dN(H)=0",
   aVnum == -1 and Hnum == [half, -half, -half, half]
   and sum(a.subs(pt)*h for a, h in zip(alpha, Hnum)) == 0
   and sum(d.subs(pt)*h for d, h in zip(dN, Hnum)) == 0)

# §6c (1−P)(iψ) = 0  (임의의 단위 ψ 대신 차트 ψ=(1,z)/√S 로)
xx, yy = sp.symbols('xx yy', real=True)
S = 1 + xx**2 + yy**2
psi = sp.Matrix([1, xx + sp.I*yy]) / sp.sqrt(S)
P = psi*psi.H
ok("§6c (1−P)(iψ) = 0", sp.simplify((sp.eye(2) - P)*(sp.I*psi)) == sp.zeros(2, 1))

# §7 dα, ι_R dα
W = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        W[i, j] = sp.diff(alpha[j], X[i]) - sp.diff(alpha[i], X[j])
ok("§7a dα = 2Σdx∧dy", W[0, 1] == 2 and W[2, 3] == 2 and W[0, 2] == 0 and W[0, 3] == 0 and W[1, 2] == 0 and W[1, 3] == 0)
iota = [sp.simplify(sum(R[i]*W[i, j] for i in range(4))) for j in range(4)]
ok("§7e ι_R dα = −dN", all(sp.simplify(iota[j] + dN[j]) == 0 for j in range(4)))
dalpha_RV = sum(Rnum[i] * W[i, j].subs(pt) * Vnum[j] for i in range(4) for j in range(4))
ok("§7g 한 점: (ι_R dα)(V) = 0, dα(R,V) = 0",
   sum(io.subs(pt)*w for io, w in zip(iota, Vnum)) == 0 and dalpha_RV == 0)

# §8 fiber pullback
sub = {x1: sp.cos(th), y1: sp.sin(th), x2: 0, y2: 0}
dsub = {x1: -sp.sin(th), y1: sp.cos(th), x2: 0, y2: 0}
pull = sum(alpha[i].subs(sub)*dsub[X[i]] for i in range(4))
ok("§8c c*α = dθ", sp.simplify(pull - 1) == 0)
ok("§8d c'(θ) = R(c(θ))", all(sp.simplify(r.subs(sub) - dsub[xi]) == 0 for xi, r in zip(X, R)))

# §5c 한 점 α(R)=1
ok("§5c 한 점 α(R)=1", aR.subs(pt) == 1)
