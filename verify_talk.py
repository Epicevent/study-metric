# -*- coding: utf-8 -*-
# 발표계산_완전판.md 의 등식 검산  (요구: pip install sympy)
# 발표 "Hopf fibration에서 Fubini-Study 계량 유도와 오일러 지표 계산"의
# 모든 계산 단계를 기호로 재현한다.
import sympy as sp

ok = lambda name, cond: print(("[OK] " if cond else "[FAIL] ") + name)

# ───────────────────────── Part I. 구면 계량 = R³ 내적 ─────────────────────────
x, y = sp.symbols('x y', real=True)
s = x**2 + y**2
S = 1 + s

# §1 남극 역입체사영: 남극 (0,0,-1) 에서 (x,y,0) 을 지나는 직선이 구면과 만나는 점
t = sp.symbols('t', positive=True)
line = sp.Matrix([t*x, t*y, t - 1])
sols = sp.solve(sp.Eq(line.dot(line), 1), t)
ok("§1 직선∩구면: t = 2/S (t=0 남극 제외)", sp.simplify(max(sols, key=lambda e: sp.count_ops(e)) - 2/S) == 0
   or any(sp.simplify(so - 2/S) == 0 for so in sols))
n = sp.Matrix([2*x/S, 2*y/S, (1 - s)/S])
ok("§1 n(z) 가 구면 위: |n|² = 1", sp.simplify(n.dot(n) - 1) == 0)
ok("§1 z=0 ↦ 북극 (0,0,1)", n.subs({x: 0, y: 0}) == sp.Matrix([0, 0, 1]))

# §2 접벡터와 내적 (제1기본형식 = R³ 내적의 제한)
nx = n.diff(x); ny = n.diff(y)
E = sp.simplify(nx.dot(nx)); F = sp.simplify(nx.dot(ny)); G = sp.simplify(ny.dot(ny))
ok("§2 E = ∂ₓn·∂ₓn = 4/S²", sp.simplify(E - 4/S**2) == 0)
ok("§2 F = ∂ₓn·∂ᵧn = 0", F == 0)
ok("§2 G = ∂ᵧn·∂ᵧn = 4/S²", sp.simplify(G - 4/S**2) == 0)

# 숫자 한 점: z = 1+i (s=2, S=3) → n = (2/3, 2/3, -1/3)
pt = {x: 1, y: 1}
ok("§2 한 점 z=1+i: n=(2/3,2/3,-1/3), E=F 값", n.subs(pt) == sp.Matrix([sp.Rational(2,3), sp.Rational(2,3), -sp.Rational(1,3)])
   and E.subs(pt) == sp.Rational(4, 9))

# ───────────────────────── Part II. Hopf 사상 ─────────────────────────
a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2', real=True)   # z1 = a1+i b1, z2 = a2+i b2
z1 = a1 + sp.I*b1; z2 = a2 + sp.I*b2
N = a1**2 + b1**2 + a2**2 + b2**2
h = sp.conjugate(z1)*z2
n1 = 2*sp.re(h); n2 = 2*sp.im(h); n3 = sp.expand(sp.Abs(z1)**2 - sp.Abs(z2)**2)
n3 = a1**2 + b1**2 - (a2**2 + b2**2)

# §4 상이 구면: n1²+n2²+n3² = N²
ok("§4 n₁²+n₂²+n₃² = (|z₁|²+|z₂|²)²", sp.simplify(sp.expand(n1**2 + n2**2 + n3**2) - N**2) == 0)

# §5 위상 불변: v ↦ e^{iθ}v 에서 z̄₁z₂ 불변
th = sp.symbols('theta', real=True)
rot = lambda zz: sp.exp(sp.I*th)*zz
ok("§5 z̄₁z₂ 는 위상 불변", sp.simplify(sp.conjugate(rot(z1))*rot(z2) - h) == 0)

# §4b 차트 [1:z]: z1=1, z2=z 로 두면 Part I 의 n(z) 복원 (N=S)
sub_chart = {a1: 1, b1: 0, a2: x, b2: y}
chart = sp.Matrix([n1, n2, n3]).subs(sub_chart) / N.subs(sub_chart)
ok("§4b 차트 [1:z] ↦ Part I 의 n(z)", sp.simplify(chart - n) == sp.zeros(3, 1))

# 숫자 한 점: v=(1, 1+i) → n=(2/3, 2/3, -1/3)
sub_pt = {a1: 1, b1: 0, a2: 1, b2: 1}
ok("§4c 한 점 [1:1+i]", (sp.Matrix([n1, n2, n3]).subs(sub_pt) / N.subs(sub_pt)) == sp.Matrix([sp.Rational(2,3), sp.Rational(2,3), -sp.Rational(1,3)]))

# ───────────────────────── Part III. FS 계량 ─────────────────────────
# §6 위상 무관: (e^{iθ}ψ)(e^{iθ}ψ)* = ψψ*
psi = sp.Matrix([1, x + sp.I*y]) / sp.sqrt(S)
P = psi * psi.H
psi_rot = sp.exp(sp.I*th) * psi
ok("§6 ψψ* 위상 무관", sp.simplify(psi_rot*psi_rot.H - P) == sp.zeros(2, 2))
ok("§6b P 가 사영자: P²=P, trP=1", sp.simplify(P*P - P) == sp.zeros(2, 2) and sp.simplify(P.trace() - 1) == 0)

# §7-8 Q_ij = <∂iψ,∂jψ> - <∂iψ,ψ><ψ,∂jψ>  (첫 인자 켤레)
dpsi = [psi.diff(x), psi.diff(y)]
inner = lambda u, v: (u.H * v)[0, 0]
Q = sp.zeros(2, 2)
for i in range(2):
    for j in range(2):
        Q[i, j] = sp.simplify(inner(dpsi[i], dpsi[j]) - inner(dpsi[i], psi) * inner(psi, dpsi[j]))
ok("§8 Re Q = diag(1/S², 1/S²)", sp.simplify(sp.re(Q[0, 0]) - 1/S**2) == 0
   and sp.simplify(sp.re(Q[1, 1]) - 1/S**2) == 0 and sp.simplify(sp.re(Q[0, 1])) == 0)
ok("§8b <ψ,∂ᵢψ> 는 순허수", sp.simplify(sp.re(inner(psi, dpsi[0]))) == 0 and sp.simplify(sp.re(inner(psi, dpsi[1]))) == 0)
# 문서 §8 의 중간값들
ok("§8(i) <ψ,∂ₓψ> = -iy/S, <ψ,∂ᵧψ> = ix/S",
   sp.simplify(inner(psi, dpsi[0]) + sp.I*y/S) == 0 and sp.simplify(inner(psi, dpsi[1]) - sp.I*x/S) == 0)
ok("§8(ii) <∂ₓψ,∂ₓψ> = (S-x²)/S²", sp.simplify(inner(dpsi[0], dpsi[0]) - (S - x**2)/S**2) == 0)
ok("§8(iii) <∂ᵧψ,∂ᵧψ> = (S-y²)/S²", sp.simplify(inner(dpsi[1], dpsi[1]) - (S - y**2)/S**2) == 0)
ok("§8(iv) <∂ₓψ,∂ᵧψ> = (i-xy)/S²", sp.simplify(inner(dpsi[0], dpsi[1]) - (sp.I - x*y)/S**2) == 0)
ok("§8(v) Q_xy = i/S²", sp.simplify(Q[0, 1] - sp.I/S**2) == 0)

# (1-P)∂ψ 로도 같은 값 (사영으로 빼기 = 둘째 항 빼기)
I2 = sp.eye(2)
Qp = sp.zeros(2, 2)
for i in range(2):
    for j in range(2):
        Qp[i, j] = sp.simplify(inner((I2 - P)*dpsi[i], (I2 - P)*dpsi[j]))
ok("§8c <(1-P)∂ᵢψ,(1-P)∂ⱼψ> = Q_ij", sp.simplify(Qp - Q) == sp.zeros(2, 2))

# §9 스케일: FS 실수부 = (1/4)|dn|²  (E=4/S² 대비 1/S²)
ok("§9 FS = 구면 계량의 1/4", sp.simplify(4*sp.re(Q[0, 0]) - E) == 0)

# ───────────────────────── Part IV. α 와 Reeb (verify_reeb.py 와 동일 대상) ─────────────────────────
X4 = [sp.Symbol('x1', real=True), sp.Symbol('y1', real=True), sp.Symbol('x2', real=True), sp.Symbol('y2', real=True)]
x1s, y1s, x2s, y2s = X4
alpha = [-y1s, x1s, -y2s, x2s]         # dx1,dy1,dx2,dy2 계수
R = [-y1s, x1s, -y2s, x2s]
Nf = x1s**2 + y1s**2 + x2s**2 + y2s**2
ok("§12 α(R) = ‖v‖²", sp.simplify(sum(a*r for a, r in zip(alpha, R)) - Nf) == 0)
W = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        W[i, j] = sp.diff(alpha[j], X4[i]) - sp.diff(alpha[i], X4[j])
iota = [sp.simplify(sum(R[i]*W[i, j] for i in range(4))) for j in range(4)]
ok("§14 ι_R dα = -dN", all(sp.simplify(iota[j] + sp.diff(Nf, X4[j])) == 0 for j in range(4)))

# ───────────────────────── Part V. 아래층으로: s₀*α, 게이지 분해, ω_FS, 적분 ─────────────────────────
# §16 s₀*α: z1 = S^{-1/2}, z2 = w S^{-1/2}, 실좌표 계수로 (x dy - y dx)/S
w_x, w_y = x, y     # w = x+iy 재사용
s0 = [1/sp.sqrt(S), 0, x/sp.sqrt(S), y/sp.sqrt(S)]   # (x1,y1,x2,y2) 성분
# α 당김 = Σ (x_r dy_r - y_r dx_r) 에 x_r=s0, dx_r = ∂s0/∂x dx + ∂s0/∂y dy 대입
def pull_alpha(comp, vars):
    # comp: [x1,y1,x2,y2] 를 vars 의 함수로. 반환: [dx 계수, dy 계수, ...] (vars 순)
    coeffs = []
    for v in vars:
        c = 0
        for r in (0, 1):
            xr, yr = comp[2*r], comp[2*r + 1]
            c += xr * sp.diff(yr, v) - yr * sp.diff(xr, v)
        coeffs.append(sp.simplify(c))
    return coeffs
A_coeff = pull_alpha(s0, [x, y])
ok("§16 s₀*α = (x dy - y dx)/S", sp.simplify(A_coeff[0] + y/S) == 0 and sp.simplify(A_coeff[1] - x/S) == 0)

# §17 게이지 분해: Φ(x,y,θ) = e^{iθ} s₀(w) 로 당기면 α = dθ + s₀*α
c_, s_ = sp.cos(th), sp.sin(th)
# e^{iθ}(a+ib) = (a cosθ - b sinθ) + i(a sinθ + b cosθ)
def rot2(a, b):
    return (a*c_ - b*s_, a*s_ + b*c_)
X1, Y1 = rot2(s0[0], s0[1]); X2, Y2 = rot2(s0[2], s0[3])
Phi = [X1, Y1, X2, Y2]
G_coeff = pull_alpha(Phi, [x, y, th])
ok("§17 Φ*α 의 dθ 계수 = 1", sp.simplify(G_coeff[2] - 1) == 0)
ok("§17 Φ*α 의 dx,dy 계수 = s₀*α 의 것", sp.simplify(G_coeff[0] - A_coeff[0]) == 0 and sp.simplify(G_coeff[1] - A_coeff[1]) == 0)

# §18 dA: d[(x dy - y dx)/S] = (2/S²) dx∧dy
Ax, Ay = -y/S, x/S
dA_coeff = sp.simplify(sp.diff(Ay, x) - sp.diff(Ax, y))
ok("§18 dA = (2/S²) dx∧dy", sp.simplify(dA_coeff - 2/S**2) == 0)

# §18b 복소식 검증: i dw∧dw̄/S² 의 실좌표 = 2 dx∧dy/S²  (dw∧dw̄ = -2i dx∧dy)
ok("§19 i·(-2i) = 2", sp.simplify(sp.I * (-2*sp.I) - 2) == 0)

# §20 ∫ ω_FS = 2π (극좌표), §21 ∫ 4/S² = 4π (구면 넓이 = ∫K dA, K=1)
r = sp.symbols('r', nonnegative=True)
I_fs = sp.integrate(2*r/(1 + r**2)**2, (r, 0, sp.oo)) * 2*sp.pi
ok("§20 ∫ω_FS = 2π", sp.simplify(I_fs - 2*sp.pi) == 0)
I_area = sp.integrate(4*r/(1 + r**2)**2, (r, 0, sp.oo)) * 2*sp.pi
ok("§21 ∫K dA = 구면 넓이 = 4π", sp.simplify(I_area - 4*sp.pi) == 0)
ok("§21b 치환 적분의 원시함수: ∫2r/(1+r²)² dr = -1/(1+r²)", sp.simplify(sp.diff(-1/(1 + r**2), r) - 2*r/(1 + r**2)**2) == 0)
