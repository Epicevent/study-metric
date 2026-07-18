# -*- coding: utf-8 -*-
# Reeb벡터장_완전계산.md 의 등식 검산  (요구: pip install sympy)
import sympy as sp

x1, y1, x2, y2, th = sp.symbols('x1 y1 x2 y2 theta', real=True)
X = [x1, y1, x2, y2]

# R_alpha 계수 (dx1, dy1, dx2, dy2 방향)
R = [-y1, x1, -y2, x2]

# alpha = x dy - y dx (계수 벡터: [dx1, dy1, dx2, dy2] 순)
alpha = [-y1, x1, -y2, x2]

ok = lambda name, cond: print(("[OK] " if cond else "[FAIL] ") + name)

# 1) G3: d/dth e^{i th} z_r at 0 == i z_r == (-y, x)
z1 = x1 + sp.I*y1
g = sp.exp(sp.I*th)*z1
v = sp.diff(g, th).subs(th, 0)
ok("생성원: d/dθ e^{iθ}z|_0 = -y + ix", sp.simplify(sp.re(v) - (-y1)) == 0 and sp.simplify(sp.im(v) - x1) == 0)

# 2) 곡선이 S^3 유지: X_r^2+Y_r^2 = x^2+y^2
Xr = x1*sp.cos(th) - y1*sp.sin(th); Yr = x1*sp.sin(th) + y1*sp.cos(th)
ok("궤도 norm 보존", sp.simplify(Xr**2 + Yr**2 - (x1**2 + y1**2)) == 0)

# 3) alpha(R) = N
aR = sum(a*r for a, r in zip(alpha, R))
N = x1**2 + y1**2 + x2**2 + y2**2
ok("α(R) = ‖v‖²", sp.simplify(aR - N) == 0)

# 4) dα = 2Σdx∧dy 이고 ι_R dα = -dN
# dα 를 반대칭 행렬 W[i][j] (dXi∧dXj 계수, i<j) 로: α = Σ a_i dX_i → W = ∂_i a_j − ∂_j a_i
W = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        W[i, j] = sp.diff(alpha[j], X[i]) - sp.diff(alpha[i], X[j])
ok("dα 계수 = 2 (dx∧dy 블록)", W[0, 1] == 2 and W[2, 3] == 2 and W[0, 2] == 0 and W[0, 3] == 0 and W[1, 2] == 0 and W[1, 3] == 0)
# ι_R dα 의 dX_j 계수 = Σ_i R_i W[i][j]
iota = [sp.simplify(sum(R[i]*W[i, j] for i in range(4))) for j in range(4)]
dN = [sp.diff(N, xi) for xi in X]
ok("ι_R dα = −dN", all(sp.simplify(iota[j] + dN[j]) == 0 for j in range(4)))

# 5) G2: c*α = dθ
sub = {x1: sp.cos(th), y1: sp.sin(th), x2: 0, y2: 0}
dsub = {x1: -sp.sin(th), y1: sp.cos(th), x2: 0, y2: 0}  # d(X_i∘c)/dθ
pull = sum(alpha[i].subs(sub)*dsub[X[i]] for i in range(4))
ok("c*α = dθ", sp.simplify(pull - 1) == 0)

# 6) 수치 한 점 (1/2,1/2,1/2,1/2): α(R)=1, ι_R dα(V)=0 (V=∂x1−∂y1)
pt = {x1: sp.Rational(1, 2), y1: sp.Rational(1, 2), x2: sp.Rational(1, 2), y2: sp.Rational(1, 2)}
ok("한 점 α(R)=1", aR.subs(pt) == 1)
V = [1, -1, 0, 0]
ok("한 점 접벡터 V 에서 ι_R dα(V)=0", sum(iota[j].subs(pt)*V[j] for j in range(4)) == 0
   and sum(dN[j].subs(pt)*V[j] for j in range(4)) == 0)

# 7) §2 미분식: X'(θ), Y'(θ)
ok("X'(θ)=-x sinθ - y cosθ", sp.simplify(sp.diff(Xr, th) - (-x1*sp.sin(th) - y1*sp.cos(th))) == 0)
ok("Y'(θ)= x cosθ - y sinθ", sp.simplify(sp.diff(Yr, th) - (x1*sp.cos(th) - y1*sp.sin(th))) == 0)
