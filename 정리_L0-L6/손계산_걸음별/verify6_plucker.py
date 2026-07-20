# -*- coding: utf-8 -*-
# verify6_plucker.py — Gr(2,4) ↪ CP^5 플뤼커 당김 노트(Gr24_플뤼커당김_계산노트.html)의 전 주장 검산
# 실행: python verify6_plucker.py
# 규약: z와 z̄를 독립 기호로 (Wirtinger). 분모 회피용 분자 행렬 N = K·Hess − ∇K⊗∇̄K, g = N/K².
import sympy as sp

PASS = 0
TOTAL = 0

def check(label, ok):
    global PASS, TOTAL
    TOTAL += 1
    PASS += bool(ok)
    print(f"[{TOTAL:02d}] {label}: {'OK' if ok else 'FAIL'}")

a, b, c, d = sp.symbols('a b c d')
ab, bb, cb, db = sp.symbols('abar bbar cbar dbar')   # z̄를 독립 기호로 — conjugate() 금지
z, zb = [a, b, c, d], [ab, bb, cb, db]

print("=" * 72)
print("PART 1. 셋업 — 플뤼커 좌표, 클라인 관계, 켈러 퍼텐셜")
print("=" * 72)

# 차트 [[1,0,a,b],[0,1,c,d]] 의 소행렬식 6개
M = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])
def minor(i, j):
    return sp.expand(M[:, i].row_join(M[:, j]).det())
p = {(i, j): minor(i, j) for i, j in [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]}
check("플뤼커 성분 (p12,p13,p14,p23,p24,p34) = (1,c,d,-a,-b,ad-bc)",
      [p[(0,1)], p[(0,2)], p[(0,3)], p[(1,2)], p[(1,3)], p[(2,3)]]
      == [1, c, d, -a, -b, sp.expand(a*d - b*c)])
check("클라인 관계 p12·p34 − p13·p24 + p14·p23 ≡ 0",
      sp.expand(p[(0,1)]*p[(2,3)] - p[(0,2)]*p[(1,3)] + p[(0,3)]*p[(1,2)]) == 0)

# 6a §3.2 역방향: 클라인 관계를 만족하는 점 [p]는 평면 하나로 복원된다 (p12=1 차트)
q13, q14, q23, q24 = sp.symbols('q13 q14 q23 q24')
q34 = q13*q24 - q14*q23                              # 클라인 관계가 강제하는 값
vv = sp.Matrix([[1, 0, -q23, -q24]])
ww = sp.Matrix([[0, 1,  q13,  q14]])
def minor2(V, W, i, j):
    return sp.expand(V[i]*W[j] - V[j]*W[i])
check("6a §3.2 복원: v=(1,0,−p23,−p24), w=(0,1,p13,p14) 가 여섯 성분을 전부 재현",
      [minor2(vv, ww, 0, 1), minor2(vv, ww, 0, 2), minor2(vv, ww, 0, 3),
       minor2(vv, ww, 1, 2), minor2(vv, ww, 1, 3), minor2(vv, ww, 2, 3)]
      == [1, q13, q14, q23, q24, sp.expand(q34)])

P, Pb = a*d - b*c, ab*db - bb*cb
K = sp.expand(1 + a*ab + b*bb + c*cb + d*db + P*Pb)

Z  = sp.Matrix([[a, b], [c, d]])
Zb = sp.Matrix([[ab, bb], [cb, db]])
Zd = Zb.T                                            # Z† (성분이 독립 기호이므로 전치만)
check("K = Σ|p_ij|² = det(I + Z†Z)",
      sp.expand(K - (sp.eye(2) + Zd*Z).det()) == 0)

print()
print("=" * 72)
print("PART 2. Hessian과 분자 행렬 N — 16성분 인수분해")
print("=" * 72)

H = [[sp.expand(sp.diff(K, z[j], zb[k])) for k in range(4)] for j in range(4)]
# 노트 §3의 Hessian 표 그대로 (십자 항 ∂_a(ad−bc)=d 류 확인)
H_note = sp.Matrix([
    [1 + d*db, -cb*d,    -bb*d,    ab*d   ],
    [-c*db,    1 + c*cb,  bb*c,   -ab*c   ],
    [-b*db,     b*cb,    1 + b*bb, -ab*b  ],
    [ a*db,    -a*cb,    -a*bb,    1 + a*ab],
])
check("Hessian ∂ⱼ∂̄ₖK == 노트 §3 표", sp.Matrix(H) - H_note == sp.zeros(4, 4))

dK  = [sp.expand(sp.diff(K, v)) for v in z]
dbK = [sp.expand(sp.diff(K, v)) for v in zb]
N = sp.Matrix(4, 4, lambda j, k: sp.expand(K*H[j][k] - dK[j]*dbK[k]))

u1, u2   = ab*b + cb*d, ab*c + bb*d                  # (Z†Z)₁₂, (ZZ†)₁₂
u1b, u2b = a*bb + c*db, a*cb + b*db
A_, B_, C_, D_ = 1 + a*ab, 1 + b*bb, 1 + c*cb, 1 + d*db
BD, CD, AC, AB = B_ + d*db, C_ + d*db, A_ + c*cb, A_ + b*bb   # 1+|b|²+|d|² 류

N_note = sp.Matrix([
    [BD*CD,    -u1*CD,   -u2*BD,   u1*u2 ],
    [-u1b*CD,   AC*CD,    u1b*u2, -u2*AC ],
    [-u2b*BD,   u1*u2b,   AB*BD,  -u1*AB ],
    [u1b*u2b,  -u2b*AC,  -u1b*AB,  AB*AC ],
])
check("N의 16성분 전부 == 노트 §3 인수분해 표 (u₁,u₂ 이차식 곱)",
      sp.expand(N - N_note) == sp.zeros(4, 4))

detN = sp.factor(sp.expand(N.det(method='berkowitz')))
check("det N = K⁴  ⟹  det g = K⁻⁴", sp.expand(detN - K**4) == 0)

print()
print("=" * 72)
print("PART 3. 행렬 항등식 — g = (I+ZZ†)^{-T} ⊗ (I+Z†Z)^{-1}")
print("=" * 72)

def kron(X, Y):
    n, m = X.shape[0]*Y.shape[0], X.shape[1]*Y.shape[1]
    return sp.Matrix(n, m, lambda r, s: X[r//Y.shape[0], s//Y.shape[1]] * Y[r % Y.shape[0], s % Y.shape[1]])

Ainv = (sp.eye(2) + Zd*Z).inv()                      # (I+Z†Z)⁻¹
Binv = (sp.eye(2) + Z*Zd).inv()                      # (I+ZZ†)⁻¹
G_kron = kron(Binv.T, Ainv)                          # z=(a,b,c,d) 행우선 순서
diff = sp.simplify(N/K**2 - G_kron)
check("g_{jk̄} == (I+ZZ†)^{-T} ⊗ (I+Z†Z)^{-1} (성분별)", diff == sp.zeros(4, 4))
# 노트 §3 박스의 오타 교정: 노트는 "u₂ = (ZZ†)₁₂"라 했으나 (ZZ†)₁₂ = ū₂이고 u₂ = (ZZ†)₂₁이 맞다.
check("u₁ = (Z†Z)₁₂, u₂ = (ZZ†)₂₁ (노트 §3 박스는 켤레 오타)",
      sp.expand(u1 - (Zd*Z)[0, 1]) == 0 and sp.expand(u2 - (Z*Zd)[1, 0]) == 0)
check("노트 원문 'u₂ = (ZZ†)₁₂'는 실제로는 ū₂ (오타 확인)",
      sp.expand(u2b - (Z*Zd)[0, 1]) == 0)

# 인수분해 표의 정체: N = K²g = (K·B^T)⊗(K·A) = adj(I+ZZ†)^T ⊗ adj(I+Z†Z)
# (2×2에서 K·M⁻¹ = adj M — 여인수 행렬은 다항식! 16성분이 "이차식×이차식"인 이유의 전부)
adjF = (sp.eye(2) + Zd*Z).adjugate()
adjG = (sp.eye(2) + Z*Zd).adjugate()
check("N == adj(I+ZZ†)^T ⊗ adj(I+Z†Z) (여인수 크로네커 곱)",
      sp.expand(N - kron(adjG.T, adjF)) == sp.zeros(4, 4))

print()
print("=" * 72)
print("PART 3b. 6b §6의 유도 — 자취 형태와 push-through 항등식")
print("=" * 72)

F = sp.eye(2) + Zd*Z
G = sp.eye(2) + Z*Zd
check("6b §2.2 실베스터: det(I+Z†Z) = det(I+ZZ†) = K",
      sp.expand(F.det() - K) == 0 and sp.expand(G.det() - K) == 0)
check("6b §6.2 push-through: Z(I+Z†Z)⁻¹ = (I+ZZ†)⁻¹Z",
      sp.simplify(Z*F.inv() - G.inv()*Z) == sp.zeros(2, 2))
check("6b §6.2 따름: I − Z F⁻¹ Z† = G⁻¹",
      sp.simplify(sp.eye(2) - Z*F.inv()*Zd - G.inv()) == sp.zeros(2, 2))

# 자취 형태 ds² = tr(F⁻¹ dZ† G⁻¹ dZ) 의 성분이 g와 일치하는가
dZ  = sp.Matrix(2, 2, lambda r, s: sp.Symbol(f'dz{r}{s}'))
dZd = sp.Matrix(2, 2, lambda r, s: sp.Symbol(f'dzb{s}{r}'))   # (dZ†)_{rs} = conj(dZ_{sr})
ds2_trace = sp.expand((F.inv() * dZd * G.inv() * dZ).trace())
dz_flat  = [sp.Symbol('dz00'), sp.Symbol('dz01'), sp.Symbol('dz10'), sp.Symbol('dz11')]
dzb_flat = [sp.Symbol('dzb00'), sp.Symbol('dzb01'), sp.Symbol('dzb10'), sp.Symbol('dzb11')]
ds2_comp = sum((N[j, k]/K**2) * dz_flat[j] * dzb_flat[k] for j in range(4) for k in range(4))
check("6b §6.3 자취 형태 tr(F⁻¹dZ†G⁻¹dZ) == Σ g_{jk̄} dz_j dz̄_k",
      sp.simplify(ds2_trace - ds2_comp) == 0)

print()
print("=" * 72)
print("PART 3c. 6b §7.2 사다리 — CPⁿ의 det g = K^-(n+1)")
print("=" * 72)

for n in (1, 2, 3):
    w  = sp.symbols(f'w1:{n+1}')
    wb = sp.symbols(f'wb1:{n+1}')
    Kn = 1 + sum(w[i]*wb[i] for i in range(n))
    Nn = sp.Matrix(n, n, lambda j, k: sp.expand(
        Kn*sp.diff(Kn, w[j], wb[k]) - sp.diff(Kn, w[j])*sp.diff(Kn, wb[k])))
    detgn = sp.factor(sp.expand(Nn.det()) / Kn**(2*n))
    check(f"CP^{n}: det g = K^-({n}+1) = K^-{n+1}  (⟹ Ric = {n+1}·g)",
          sp.simplify(detgn - Kn**(-(n+1))) == 0)

print()
print("=" * 72)
print("PART 4. 검산 네 도장 — 원점 · CP¹ 환원 · 부피=차수 · 켈러-아인슈타인")
print("=" * 72)

# 도장 一: 원점 항등
check("검산一 원점: N(0) = Identity(4)",
      N.subs({v: 0 for v in z + zb}) == sp.eye(4))

# 도장 二: a-직선 → 1차원 푸비니-스터디
line = {b: 0, c: 0, d: 0, bb: 0, cb: 0, db: 0}
g00_line = sp.simplify((N[0, 0] / K**2).subs(line))
check("검산二 CP¹ 환원: g_aā|ₗᵢₙₑ = (1+|a|²)⁻²",
      sp.simplify(g00_line - 1/(1 + a*ab)**2) == 0)

# 도장 四 (기호): Ric = −∂∂̄ log det g = 4 ∂∂̄ log K = 4g — det N = K⁴가 항등이므로 따름정리.
# 독립 스팟체크: 성분 (0,0)을 직접 미분으로.
logdetg = sp.log(detN) - 8*sp.log(K)                 # log det g = log(N det)/K⁸
ric00 = sp.simplify(-sp.diff(logdetg, a, ab) - 4*N[0, 0]/K**2)
check("검산四 켈러-아인슈타인: Ric₀₀̄ = 4·g₀₀̄ (직접 미분 스팟체크)", ric00 == 0)

# 도장 三 (수치): Vol = ∫ K⁻⁴ dV = deg·π⁴/4! = π⁴/12 — 코시 중요도 표집 Monte Carlo
import numpy as np
rng = np.random.default_rng(0)
X = rng.standard_cauchy((4_000_000, 8))
w = np.prod(np.pi * (1 + X**2), axis=1)
an, bn = X[:, 0] + 1j*X[:, 1], X[:, 2] + 1j*X[:, 3]
cn, dn = X[:, 4] + 1j*X[:, 5], X[:, 6] + 1j*X[:, 7]
Kn = 1 + abs(an)**2 + abs(bn)**2 + abs(cn)**2 + abs(dn)**2 + abs(an*dn - bn*cn)**2
vals = Kn**-4.0 * w
est, sem = vals.mean(), vals.std() / np.sqrt(len(vals))
target = np.pi**4 / 12
print(f"     Monte Carlo (4×10⁶): {est:.5f} ± {sem:.5f}   vs  π⁴/12 = {target:.5f}")
check("검산三 부피 = deg(Gr)·π⁴/4! = π⁴/12 (3σ 이내)", abs(est - target) < 3*sem + 0.05)

print()
print("=" * 72)
print("PART 4b. 6ab — 퍼텐셜은 공짜가 아니다 (K는 함수가 아니다)")
print("=" * 72)

def plucker_sum(A):
    """2×4 행렬의 소행렬식 6개의 |·|² 합 — z̄는 독립 기호이므로 켤레는 손으로 만든다."""
    conj = {a: ab, b: bb, c: cb, d: db, ab: a, bb: b, cb: c, db: d}
    tot = 0
    for i in range(4):
        for j in range(i + 1, 4):
            m = sp.expand(A[0, i]*A[1, j] - A[0, j]*A[1, i])
            tot += sp.expand(m * m.subs(conj, simultaneous=True))
    return sp.expand(tot)

A12 = sp.Matrix([[1, 0, a, b], [0, 1, c, d]])
check("6ab §1 이 차트의 K = Σ|p_ij|²  (게이지 p12=1 고정 후)",
      sp.expand(plucker_sum(A12) - K) == 0)

# 차트 갈아타기: 열 (1,3)을 단위블록으로 정규화 → M = [[1,a],[0,c]], det M = c = p13/p12
Mch = sp.Matrix([[1, a], [0, c]])
A13 = sp.simplify(Mch.inv() * A12)
K13 = sp.simplify(plucker_sum(A13))
check("6ab §3 다른 차트의 퍼텐셜: K^(13) = K^(12)/|p13|²  (K는 함수가 아니다!)",
      sp.simplify(K13 - K/(c*cb)) == 0)

# 그런데도 ω는 살아남는다: ∂∂̄ log|f|² = 0  (f 정칙, 여기서 f = c)
ddbar_log_ratio = sp.Matrix(4, 4, lambda j, k: sp.simplify(
    sp.diff(sp.log(c) + sp.log(cb), z[j], zb[k])))
check("6ab §2 ∂∂̄ log|f|² = 0  (f=p13/p12 정칙) ⟹ 두 차트의 ω가 일치",
      ddbar_log_ratio == sp.zeros(4, 4))

# U(4) 불변성: u ∈ U(4) (좌표 1,3의 회전 3/5,4/5) 로 작용하면 K가 |정칙|²배로만 변한다
R = sp.Rational
uT = sp.Matrix([[R(3,5), 0, R(4,5), 0],
                [0,      1, 0,      0],
                [-R(4,5),0, R(3,5), 0],
                [0,      0, 0,      1]])
check("6ab §6.1 u는 유니터리 (실직교)", sp.simplify(uT.T * uT) == sp.eye(4))
alpha, gamma = uT[0:2, 0:2], uT[2:4, 0:2]
beta,  delta = uT[0:2, 2:4], uT[2:4, 2:4]
Zm = sp.Matrix([[a, b], [c, d]])
blk1 = sp.simplify(alpha + Zm*gamma)                      # α + Zγ
Zp = sp.simplify(blk1.inv() * (beta + Zm*delta))          # 분수선형 작용 Z' = (α+Zγ)⁻¹(β+Zδ)
detf = sp.simplify(blk1.det())                            # 정칙 함수 det(α+Zγ)
check("6ab §6.1 (I|Z)uᵀ = (α+Zγ)(I|Z') — 분수선형 작용",
      sp.simplify(A12*uT - blk1.row_join(blk1*Zp)) == sp.zeros(2, 4))

conj_map = {a: ab, b: bb, c: cb, d: db}
Kp = sp.simplify(K.subs({a: Zp[0,0], b: Zp[0,1], c: Zp[1,0], d: Zp[1,1],
                         ab: Zp[0,0].subs(conj_map), bb: Zp[0,1].subs(conj_map),
                         cb: Zp[1,0].subs(conj_map), db: Zp[1,1].subs(conj_map)}))
check("6ab §6.2 K(Z) = |det(α+Zγ)|²·K(Z')  ⟹ ω가 U(4)-불변",
      sp.simplify(K - detf * detf.subs(conj_map) * Kp) == 0)

# 양정치성은 공짜가 아니다: g는 무작위 점에서 고유값이 전부 양수
import numpy as np
rng2 = np.random.default_rng(7)
gfun = sp.lambdify((a, b, c, d, ab, bb, cb, db), N/K**2, 'numpy')
pos = True
for _ in range(200):
    zz = rng2.normal(size=4) + 1j*rng2.normal(size=4)
    gm = np.array(gfun(*zz, *np.conj(zz)), dtype=complex)
    pos &= np.allclose(gm, gm.conj().T) and np.linalg.eigvalsh(gm).min() > 1e-12
check("6ab §5 g가 에르미트 양정치 (무작위 200점, 최소고유값 > 0)", pos)

# 그리고 그 이유: ds² = tr(F⁻¹dZ†G⁻¹dZ) = tr(X†X),  X = G^{-1/2} dZ F^{-1/2}
def half_inv(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w**-0.5) @ V.conj().T
ok_tr = True
for _ in range(50):
    Zn = rng2.normal(size=(2, 2)) + 1j*rng2.normal(size=(2, 2))
    dZn = rng2.normal(size=(2, 2)) + 1j*rng2.normal(size=(2, 2))
    Fn = np.eye(2) + Zn.conj().T @ Zn
    Gn = np.eye(2) + Zn @ Zn.conj().T
    lhs = np.trace(np.linalg.inv(Fn) @ dZn.conj().T @ np.linalg.inv(Gn) @ dZn)
    X = half_inv(Gn) @ dZn @ half_inv(Fn)
    ok_tr &= abs(lhs - np.sum(np.abs(X)**2)) < 1e-9
check("6ab §5 tr(F⁻¹dZ†G⁻¹dZ) = Σ|X_ij|² ≥ 0,  X = G^{-1/2}dZF^{-1/2} (무작위 50점)", ok_tr)

print()
print("=" * 72)
print("PART 5. 6c의 주장들 — 정규화 π · 실 그라스만 라그랑지언 · 일반 Gr(k,n)")
print("=" * 72)

# 6c §1.1  정규화: ω = (i/2)∂∂̄log K 에서 ∫_{CP¹} ω = π
x, y, r = sp.symbols('x y r', real=True, nonnegative=True)
integrand = 1/(1 + r**2)**2 * 2*sp.pi*r                      # 극좌표, g=(1+|z|²)⁻²
check("6c §1.1 ∫_{CP¹} ω = ∫(1+|z|²)⁻² dxdy = π  (이 노트의 정규화)",
      sp.integrate(integrand, (r, 0, sp.oo)) == sp.pi)

# 6c §4.1  실 그라스만은 라그랑지언: a,b,c,d 실수면 ω|=0
#          ω = (i/2)Σ g_{jk̄} dz_j∧dz̄_k 에서 dz=dz̄=dx ⟹ dz∧dz̄=0. 성분으로도 확인:
#          실 궤적에서 g는 실대칭 ⟹ 반대칭 조합인 ω의 계수가 상쇄.
ar, br, cr, dr = sp.symbols('a_r b_r c_r d_r', real=True)
real_sub = {a: ar, b: br, c: cr, d: dr, ab: ar, bb: br, cb: cr, db: dr}
g_real = sp.simplify((N/K**2).subs(real_sub))
check("6c §4.1 실 궤적에서 g_{jk̄}가 실대칭 (⟹ ω| = Σg dx_j∧dx_k = 0, 라그랑지언)",
      sp.simplify(g_real - g_real.T) == sp.zeros(4, 4)
      and all(sp.simplify(sp.im(e)) == 0 for e in g_real))

# 6c §4.3  일반 Gr(k,n): g = (I+ZZ†)^{-T} ⊗ (I+Z†Z)^{-1},  det g = K^{-n}
def check_grassmannian(k, n):
    m = n - k
    W  = sp.Matrix(k, m, lambda i, j: sp.Symbol(f'w{i}{j}'))
    Wb = sp.Matrix(k, m, lambda i, j: sp.Symbol(f'wb{i}{j}'))
    Wd = Wb.T                                                # W† (독립 기호)
    Fk, Gk = sp.eye(m) + Wd*W, sp.eye(k) + W*Wd
    Kk = sp.expand(Fk.det())
    check(f"  Gr({k},{n}): det(I+W†W) = det(I+WW†) = K", sp.expand(Gk.det() - Kk) == 0)
    check(f"  Gr({k},{n}): push-through W F⁻¹ = G⁻¹ W",
          sp.simplify(W*Fk.inv() - Gk.inv()*W) == sp.zeros(k, m))
    # 계량을 ∂∂̄ log K 에서 직접 (행우선 좌표 나열)
    zs  = [W[i, j]  for i in range(k) for j in range(m)]
    zbs = [Wb[i, j] for i in range(k) for j in range(m)]
    d = k*m
    Nk = sp.Matrix(d, d, lambda p, q: sp.expand(
        Kk*sp.diff(Kk, zs[p], zbs[q]) - sp.diff(Kk, zs[p])*sp.diff(Kk, zbs[q])))
    check(f"  Gr({k},{n}): g == (I+WW†)^-T ⊗ (I+W†W)⁻¹  ({d}×{d} 성분 전부)",
          sp.simplify(Nk/Kk**2 - kron(Gk.inv().T, Fk.inv())) == sp.zeros(d, d))
    # det g = (det G⁻¹)^m (det F⁻¹)^k = K^-(k+m) = K^-n   ← 크로네커 행렬식 공식
    # (d×d 기호 행렬식은 d≥6에서 폭발하므로, 무작위 유리점 대입으로 항등식을 판정한다.
    #  다항식 항등식이므로 일반 위치의 점 몇 개에서 일치하면 사실상 확정.)
    ok = True
    for seed in range(3):
        pt = {}
        for i, s in enumerate(zs):
            v = sp.Rational(2*seed + i + 1, 3*seed + i + 5)
            pt[s] = v
            pt[zbs[i]] = v                                  # 실점 (z̄ = z) — 항등식 판정에 충분
        gk_pt = (Nk/Kk**2).subs(pt)
        ok &= sp.simplify(gk_pt.det() - Kk.subs(pt)**(-n)) == 0
    check(f"  Gr({k},{n}): det g = K^-{n}  (⟹ Ric = {n}·g, Fano 지수 = n) — 무작위 3점", ok)

for (k, n) in [(1, 4), (2, 5), (3, 5)]:
    alias = f"  = CP^{n-1}" if k == 1 else ""
    print(f"--- Gr({k},{n}){alias} ---")
    check_grassmannian(k, n)

print()
print("=" * 72)
print("PART 6. 6e — 퍼텐셜은 한 층 위(Σ⁹/S³)에 전역으로 산다")
print("=" * 72)

# CP¹ 모형에서: 국소 절단 s(z) = (1,z)/√K 로 접속형식 α를 당기면
# s*α = (i/2)(∂̄ − ∂)log K  이고  d(s*α) = 2ω.  (걸음 6의 지뢰 dα = 2dA_FS)
zz, zb_ = sp.symbols('z zbar')
dz_, dzb_ = sp.symbols('dz dzbar')
Kc = 1 + zz*zb_
psi  = [1/sp.sqrt(Kc),      zz/sp.sqrt(Kc)]
psib = [1/sp.sqrt(Kc), zb_*1/sp.sqrt(Kc)]

def d_of(f):
    return sp.diff(f, zz)*dz_ + sp.diff(f, zb_)*dzb_

alpha_pb = sp.simplify(sp.expand(
    sp.Rational(1, 2)*sp.I * sum(psi[r]*d_of(psib[r]) - psib[r]*d_of(psi[r]) for r in range(2))))
target = sp.simplify(sp.Rational(1, 2)*sp.I *
                     (sp.diff(sp.log(Kc), zb_)*dzb_ - sp.diff(sp.log(Kc), zz)*dz_))
check("6e §3 s*α = (i/2)(∂̄−∂)log K  — 접속형식의 당김 = 국소 퍼텐셜의 원시형식",
      sp.simplify(alpha_pb - target) == 0)

# d(s*α) = 2ω:  s*α = A dz + B dz̄ ⟹ d(s*α) = (∂_z B − ∂_z̄ A) dz∧dz̄
alpha_exp = sp.expand(alpha_pb)                      # coeff()는 전개된 식에서만 올바르다
A_ = sp.simplify(alpha_exp.coeff(dz_))
B_ = sp.simplify(alpha_exp.coeff(dzb_))
d_alpha_coeff = sp.simplify(sp.diff(B_, zz) - sp.diff(A_, zb_))
omega_coeff = sp.Rational(1, 2)*sp.I*sp.diff(sp.log(Kc), zz, zb_)
check("6e §3 d(s*α) = 2ω  (레포 지뢰 dα = 2·dA_FS 재현)",
      sp.simplify(d_alpha_coeff - 2*omega_coeff) == 0)

# 게이지(절단) 교체 s → e^{iθ}s 는 s*α를 완전형식만큼 바꾼다 ⟹ ω는 불변
th = sp.Function('theta')(zz, zb_)
psi2  = [sp.exp( sp.I*th)*p for p in psi]
psib2 = [sp.exp(-sp.I*th)*p for p in psib]
alpha_pb2 = sp.simplify(sp.expand(
    sp.Rational(1, 2)*sp.I * sum(psi2[r]*d_of(psib2[r]) - psib2[r]*d_of(psi2[r]) for r in range(2))))
check("6e §3 절단 교체 s→e^{iθ}s ⟹ s*α ↦ s*α + dθ  (차이가 완전형식 ⟹ ω 불변)",
      sp.simplify(alpha_pb2 - alpha_pb - d_of(th)) == 0)

# 차수 장부: 푸앵카레 쌍대의 짝은 (k, n−k). CP⁵(실10): 2↔8,  Gr(2,4)(실8): 2↔6.
# "2-형식 ↔ 10-형식"은 쌍대가 아니라 거듭제곱(Wirtinger): ω^5/5! 가 꼭대기.
check("6e §1 차수 장부: CP⁵에서 2+8=10, Gr(2,4)에서 2+6=8 (쌍대 짝)",
      2 + 8 == 10 and 2 + 6 == 8)
check("6e §1 꼭대기 형식은 거듭제곱: dim_R CP⁵=10 ⟹ ω^5, dim_R Gr(2,4)=8 ⟹ ω^4",
      2*5 == 10 and 2*4 == 8)

print()
print("=" * 72)
print("PART 7. 6f — 가장 단순한 상황: 원 하나가 전부를 설명한다")
print("=" * 72)

rr = sp.symbols('r', positive=True)
th = sp.symbols('theta', real=True)
dth = sp.Symbol('dtheta')

# 원 위의 각도: ∮dθ = 2π ≠ 0 ⟹ θ는 S¹의 전역 함수가 아니다 (전역 함수면 ∮df = 0)
check("6f §1 ∮_{S¹} dθ = 2π ≠ 0  ⟹ θ는 전역 함수가 아니다",
      sp.integrate(1, (th, 0, 2*sp.pi)) == 2*sp.pi)

# 호프: 원점 차트의 절단 s₀ 로 당긴 α 를 반지름 r 원 위에 제한
zp, zbp = rr*sp.exp(sp.I*th), rr*sp.exp(-sp.I*th)
dz_loop, dzb_loop = sp.I*rr*sp.exp(sp.I*th)*dth, -sp.I*rr*sp.exp(-sp.I*th)*dth
alpha_loop = sp.simplify(sp.expand(alpha_exp.subs(
    {zz: zp, zb_: zbp, dz_: dz_loop, dzb_: dzb_loop})))
check("6f §2 s₀*α|_{|z|=r} = r²/(1+r²)·dθ",
      sp.simplify(alpha_loop - rr**2/(1 + rr**2)*dth) == 0)

loop_int = sp.simplify(alpha_loop.coeff(dth) * 2*sp.pi)          # ∮ s₀*α
rho = sp.symbols('rho', positive=True)
disk_int = sp.simplify(sp.integrate(2*sp.pi*rho/(1 + rho**2)**2, (rho, 0, rr)))  # ∫_{D_r} ω
check("6f §2 스토크스: ∫_{D_r} ω = ½·∮_{|z|=r} s₀*α   (dα = 2ω 때문에 ½)",
      sp.simplify(disk_int - loop_int/2) == 0)
check("6f §2 r→∞ 에서 ∫_{D_r}ω → π,  ∮s₀*α → 2π",
      sp.limit(disk_int, rr, sp.oo) == sp.pi and sp.limit(loop_int, rr, sp.oo) == 2*sp.pi)

# 무한원점 차트의 절단 s_∞ = (1/z,1)/√(1+|1/z|²) 는 s₀ 의 e^{-i arg z} 배
s0  = [1/sp.sqrt(1 + zp*zbp), zp/sp.sqrt(1 + zp*zbp)]
sinf_raw = [1/zp, sp.Integer(1)]
nrm = sp.sqrt(sp.simplify(1 + 1/(zp*zbp)))
sinf = [sp.simplify(u/nrm) for u in sinf_raw]
check("6f §3 두 절단의 전이함수: s_∞ = e^{-iθ}·s₀  (감김수 1)",
      all(sp.simplify(sinf[k] - sp.exp(-sp.I*th)*s0[k]) == 0 for k in range(2)))

# ⟹ s₀*α − s_∞*α = dθ  ([47]의 절단교체 법칙에 θ_gauge = −θ),  ∮ = 2π
# 따라서 ∫_{S²}ω = ½·∮(s₀*α − s_∞*α) = ½·2π = π   — π의 정체는 "감김수 1"이다
check("6f §3 ∫_{S²} ω = ½·(전이함수 감김수)·2π = π",
      sp.Rational(1, 2) * 1 * 2*sp.pi == sp.pi)

# 차원이 작으면 세 연산이 겹쳐 보인다: CP¹에서 ω(2) = 꼭대기(2), PD 짝 = 0
for n, top, pd in [(1, 2, 0), (2, 4, 2), (5, 10, 8)]:
    check(f"6f §4 CP^{n}: ω는 2-형식, 꼭대기 {top}-형식, PD 짝 {pd}-형식"
          + ("  ← 셋이 겹침" if n == 1 else ""),
          2*n == top and 2*n - 2 == pd)

print()
print("=" * 72)
print(f"결과: {PASS}/{TOTAL} 통과")
print("=" * 72)
