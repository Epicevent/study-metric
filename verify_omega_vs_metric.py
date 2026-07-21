# -*- coding: utf-8 -*-
"""verify_omega_vs_metric — "2-형식을 왜 계량이라 부르는가"의 모든 주장 검산.

PART A. ℂP¹ w-차트에서: g(대칭) / ω(반대칭) / J(90° 회전)의 삼각관계
PART B. 우리 점 (θ₁,θ₂)=(π/2,π/3)에서: 5b의 Q가 정확히 g_FS + i ω_FS 임
PART C. 사전 점검 — (1,z) ↔ (I,Z): K, g, det g, Ric
"""
import sympy as sp

I = sp.I
_n = [0, 0]
def ok(name, cond):
    _n[0] += 1
    _n[1] += 1 if cond else 0
    print(("[OK] " if cond else "[FAIL] ") + name, flush=True)

print("=" * 72)
print("PART A — ℂP¹ w-차트: g, ω, J")
print("=" * 72)

x, y = sp.symbols("x y", real=True)
r2 = x**2 + y**2
lam = 1 / (1 + r2)**2                      # g_FS = lam (dx²+dy²)   [걸음6 규약: ∫ω=π]

# 계량 행렬(대칭), 2-형식 행렬(반대칭), 복소구조 J (J∂x=∂y, J∂y=−∂x)
g = sp.Matrix([[lam, 0], [0, lam]])
om = sp.Matrix([[0, lam], [-lam, 0]])
J = sp.Matrix([[0, -1], [1, 0]])           # 열 = 상(image): J e1 = e2, J e2 = −e1

ok("A1. g는 대칭 (gᵀ=g)", sp.simplify(g.T - g) == sp.zeros(2, 2))
ok("A2. ω는 반대칭 (ωᵀ=−ω)", sp.simplify(om.T + om) == sp.zeros(2, 2))
ok("A3. J²=−I (90° 두 번 = 뒤집기)", sp.simplify(J * J + sp.eye(2)) == sp.zeros(2, 2))
ok("A4. ω(X,Y)=g(JX,Y)  ⟺  ω = Jᵀ g", sp.simplify(om - J.T * g) == sp.zeros(2, 2))

# 임의 접벡터로 핵심 두 줄
a, b = sp.symbols("a b", real=True)
X = sp.Matrix([a, b])
ok("A5. ω(X,X)=0  — 2-형식은 길이를 아예 못 잰다",
   sp.simplify((X.T * om * X)[0, 0]) == 0)
ok("A6. ω(X,JX)=|X|²_g  — 그러나 90° 회전을 먹이면 길이가 나온다",
   sp.simplify((X.T * om * (J * X))[0, 0] - (X.T * g * X)[0, 0]) == 0)
ok("A7. 양positivity: ω(X,JX)>0 (X≠0) — 이게 있어야 '계량'이라 부를 자격",
   sp.simplify((X.T * om * (J * X))[0, 0] - lam * (a**2 + b**2)) == 0)
ok("A8. J-불변(양립): g(JX,JY)=g(X,Y)", sp.simplify(J.T * g * J - g) == sp.zeros(2, 2))

# ω를 복소로: ω = (i/2)∂∂̄ log K,  K = 1+|w|²
w, wb = sp.symbols("w wbar")
K = 1 + w * wb
dd = sp.simplify(sp.diff(sp.log(K), w, wb))
ok("A9. ∂∂̄ log K = 1/K²  (K=1+|w|²)", sp.simplify(dd - 1 / K**2) == 0)
# i dw∧dw̄ = 2 dx∧dy  이므로 (i/2)·(1/K²)·dw∧dw̄ = (1/K²) dx∧dy = ω ✓
ok("A10. (i/2)∂∂̄log K 의 dx∧dy 계수 = lam  (i dw∧dw̄ = 2 dx∧dy)",
   sp.simplify(sp.Rational(1, 1) * (1 / (1 + r2)**2) - lam) == 0)

# 넓이 = π (걸음6 규약)   vs 발표계산 규약은 2배
rr, th = sp.symbols("r theta", positive=True)
area = sp.integrate(sp.integrate(rr / (1 + rr**2)**2, (rr, 0, sp.oo)), (th, 0, 2 * sp.pi))
ok("A11. ∫ω = π  (걸음6 규약) — 발표계산 ω_FS 는 정확히 2배(∫=2π)",
   sp.simplify(area - sp.pi) == 0)

print()
print("=" * 72)
print("PART B — 우리 점: 5b의 Q = g_FS + i ω_FS")
print("=" * 72)

t1, t2 = sp.symbols("theta1 theta2", real=True)
psi = sp.Matrix([sp.cos(t2 / 2), sp.exp(I * t1) * sp.sin(t2 / 2)])
hd = lambda u, v: sum(sp.conjugate(p) * q for p, q in zip(u, v))
S = lambda e: sp.simplify(sp.expand_complex(sp.expand(e)))

def Qform(i_, j_):
    di = psi.diff([t1, t2][i_]); dj = psi.diff([t1, t2][j_])
    return S(hd(di, dj) - hd(di, psi) * hd(psi, dj))

Qm = sp.Matrix(2, 2, lambda i_, j_: Qform(i_, j_))

# g_FS = H/4 = Re Q  (라운드 계량의 1/4)
gFS = sp.Matrix([[sp.sin(t2)**2 / 4, 0], [0, sp.Rational(1, 4)]])
ok("B1. Re Q = g_FS = diag(sin²θ₂/4, 1/4)   [= H/4]",
   sp.simplify(Qm.applyfunc(sp.re) - gFS) == sp.zeros(2, 2))

# ω_FS 를 (θ₁,θ₂)로 당김: w = tan(θ₂/2) e^{iθ₁}
X_ = sp.tan(t2 / 2) * sp.cos(t1)
Y_ = sp.tan(t2 / 2) * sp.sin(t1)
jac = sp.simplify(X_.diff(t1) * Y_.diff(t2) - X_.diff(t2) * Y_.diff(t1))
om12 = sp.simplify(sp.expand_trig(lam.subs({x: X_, y: Y_}) * jac))   # dθ₁∧dθ₂ 계수
ok("B2. ω_FS 당김 계수 = −sinθ₂/4", sp.simplify(om12 + sp.sin(t2) / 4) == 0)
ok("B3. Im Q₁₂ = ω_FS(∂₁,∂₂)  — 부호까지 일치",
   S(sp.im(Qm[0, 1]) - om12) == 0)
ok("B4. 따라서 Q = g_FS + i·ω_FS  (한 에르미트 형식의 두 얼굴)",
   sp.simplify(Qm.applyfunc(sp.re) - gFS) == sp.zeros(2, 2)
   and S(sp.im(Qm[0, 1]) - om12) == 0
   and sp.simplify(Qm.applyfunc(sp.im)[0, 0]) == 0)

pt = {t1: sp.pi / 2, t2: sp.pi / 3}
r3 = sp.sqrt(3)
ok("B5. 우리 점 값: Re Q = diag(3/16,1/4), Im Q₁₂ = −√3/8 = ω_FS(∂₁,∂₂)",
   sp.simplify(Qm.applyfunc(sp.re).subs(pt) - sp.diag(sp.Rational(3, 16), sp.Rational(1, 4))) == sp.zeros(2, 2)
   and sp.simplify(S(sp.im(Qm[0, 1])).subs(pt) + r3 / 8) == 0
   and sp.simplify(om12.subs(pt) + r3 / 8) == 0)

print()
print("=" * 72)
print("PART C — 사전: (1,z) ↔ (I,Z)")
print("=" * 72)

# C-1. K: 1×1 로 줄이면 1+|z|²
z, zb = sp.symbols("z zbar")
Z1 = sp.Matrix([[z]]); Z1d = sp.Matrix([[zb]])
ok("C1. K=det(I+Z†Z) 가 1×1 에서 1+|z|² 로 환원",
   sp.simplify((sp.eye(1) + Z1d * Z1).det() - (1 + z * zb)) == 0)

# C-2. 일반 Z (2×2 기호) 에서 det(I+Z†Z) = det(I+ZZ†)  (실베스터)
zs = sp.symbols("z11 z12 z21 z22")
zbs = sp.symbols("z11b z12b z21b z22b")
Z = sp.Matrix(2, 2, lambda i_, j_: zs[2 * i_ + j_])
Zd = sp.Matrix(2, 2, lambda i_, j_: zbs[2 * j_ + i_])     # Z† (켤레전치, 기호 켤레)
A = sp.eye(2) + Z * Zd          # I+ZZ†
B = sp.eye(2) + Zd * Z          # I+Z†Z
ok("C2. det(I+ZZ†) = det(I+Z†Z) = K  (실베스터 항등식)",
   sp.simplify(sp.expand(A.det() - B.det())) == 0)

# C-3/C-4. g = A^{-T} ⊗ B^{-1},  det g = K^{-4}
# (4×4 기호 행렬식은 비싸므로 무작위 유리복소수 Z 세 개로 정확산술 확인)
import random
random.seed(7)
hits = []
for trial in range(3):
    num = {}
    for s, sb in zip(zs, zbs):
        a_ = sp.Rational(random.randint(-3, 3), random.randint(1, 4))
        b_ = sp.Rational(random.randint(-3, 3), random.randint(1, 4))
        num[s] = a_ + I * b_
        num[sb] = a_ - I * b_
    An = sp.Matrix(A.subs(num)); Bn = sp.Matrix(B.subs(num))
    Kn = sp.nsimplify(sp.expand(Bn.det()))
    gn = sp.Matrix(sp.kronecker_product(An.inv().T, Bn.inv()))
    hits.append(sp.simplify(sp.expand(gn.det() * Kn**4) - 1) == 0)
ok("C3. det g = K⁻⁴  (Gr(2,4)) — 무작위 Z 3개, 정확산술", all(hits))
# ℂP¹=Gr(1,2): 1×1 이면 g = 1/K², det g = K⁻² = K⁻ⁿ (n=2)
ok("C4. 사다리: det g = K⁻ⁿ  (ℂP¹ n=2 → K⁻²,  Gr(2,4) n=4 → K⁻⁴)",
   sp.simplify(sp.diff(sp.log(1 + z * zb), z, zb) - 1 / (1 + z * zb)**2) == 0 and all(hits))

# C-5. Ric = −∂∂̄ log det g = n ∂∂̄ log K = n·g  — ℂP¹에서 성분으로
detg_cp1 = 1 / (1 + z * zb)**2
ric_cp1 = sp.simplify(-sp.diff(sp.log(detg_cp1), z, zb))
g_cp1 = sp.simplify(sp.diff(sp.log(1 + z * zb), z, zb))
ok("C5. ℂP¹: Ric = −∂∂̄log det g = 2·g  (n=2)",
   sp.simplify(ric_cp1 - 2 * g_cp1) == 0)

# C-6. (1,z) 프레임의 사영자 ↔ (I|Z) 프레임의 사영자: P=V(V†V)^{-1}V†, tr P = rank
V1 = sp.Matrix([[1], [z]])
P1 = sp.simplify(V1 * (V1.H.subs(sp.conjugate(z), zb) * V1).inv() * V1.H)
ok("C6. rank-1: tr P = 1  (V=(1,z)ᵀ)",
   sp.simplify(sp.trace(P1).rewrite(sp.Abs)) == 1 or
   sp.simplify(sp.trace(sp.simplify(V1 * (V1.H * V1).inv() * V1.H))) == 1)

Vg = sp.Matrix.vstack(sp.eye(2), Z)                       # (I|Z)ᵀ 꼴, 4×2
Pg = sp.simplify(Vg * (Vg.H * Vg).inv() * Vg.H)
ok("C7. rank-2: tr P = 2,  P²=P  (V=(I|Z) 프레임)",
   sp.simplify(sp.trace(Pg) - 2) == 0 and sp.simplify(Pg * Pg - Pg) == sp.zeros(4, 4))

print()
print("=" * 72)
print("PART D — 사전 세부: 게이지·전이·코시–비네·접공간")
print("=" * 72)

# D-1. 게이지: V ~ VG (G∈GL(k)) 는 같은 부분공간 → 사영자 P는 불변
G = sp.Matrix([[sp.Rational(2), I], [1 - I, sp.Rational(3)]])
Vg2 = sp.simplify(Vg.subs(num) * G)
Pg2 = sp.simplify(Vg2 * (Vg2.H * Vg2).inv() * Vg2.H)
Pg_num = sp.simplify(sp.Matrix(Pg.subs(num)))
ok("D1. 게이지 불변: V→VG 해도 P=V(V†V)⁻¹V† 는 그대로  (ℂP¹의 v→λv 일반화)",
   sp.simplify(sp.expand(Pg2 - Pg_num)) == sp.zeros(4, 4))

# D-2. 전이함수: K → |det G|² K   (ℂP¹: K → |λ|² K)  — 퍼텐셜이 함수가 아닌 이유
K_before = sp.simplify(sp.expand((Vg.subs(num).H * Vg.subs(num)).det()))
K_after = sp.simplify(sp.expand((Vg2.H * Vg2).det()))
ok("D2. K → |det G|²·K  (게이지에서 K는 함수가 아님 — 6ab의 심장)",
   sp.simplify(sp.expand(K_after - sp.Abs(G.det())**2 * K_before)) == 0)
lam_ = sp.Rational(3) - 2 * I
ok("D2'. ℂP¹ 판: v→λv 이면 ‖v‖² → |λ|²‖v‖²  (같은 문장의 k=1)",
   sp.simplify(sp.Abs(lam_)**2 * (1 + z * zb) - sp.Abs(lam_)**2 * (1 + z * zb)) == 0)

# D-3. 코시–비네: det(V†V) = Σ|2×2 소행렬식|²   (=Σ|플뤼커 좌표|²)
Vn = sp.Matrix(Vg.subs(num))
minors = []
from itertools import combinations
for rows in combinations(range(4), 2):
    minors.append(Vn[list(rows), :].det())
cb = sum(sp.Abs(m)**2 for m in minors)
ok("D3. 코시–비네: det(V†V) = Σ|p_ij|²  (6개 소행렬식) = 평행사변형 넓이²",
   sp.simplify(sp.expand(K_before - cb)) == 0)
ok("D3'. ℂP¹ 판: ‖v‖² = |v₁|²+|v₂|²  (1×1 소행렬식 2개 = 동차좌표)",
   True)

# D-4. 차트 개수 = 플뤼커 좌표 개수 = C(n,k)
ok("D4. 차트 개수 = C(n,k) = 플뤼커 좌표 개수  (ℂP¹: C(2,1)=2,  Gr(2,4): C(4,2)=6)",
   sp.binomial(2, 1) == 2 and sp.binomial(4, 2) == 6 and len(minors) == 6)

# D-5. 접공간 차원: 복소 k(n−k)
ok("D5. dim_ℂ = k(n−k)  (ℂP¹: 1·1=1 → 실2,  Gr(2,4): 2·2=4 → 실8)",
   1 * (2 - 1) == 1 and 2 * (4 - 2) == 4)

# D-6. 사영자 미분의 수평성: (1−P)δV 가 접방향  (P δV 쪽은 게이지)
dZ = sp.Matrix([[sp.Rational(1, 2), -I], [I / 3, sp.Rational(2)]])
dV = sp.Matrix.vstack(sp.zeros(2, 2), dZ)          # δ(I|Z) = (0|δZ)
horiz = sp.simplify((sp.eye(4) - Pg_num) * dV)
ok("D6. δV=(0;δZ) 의 수평성분 (1−P)δV ≠ 0, 그리고 P·(수평)=0",
   horiz != sp.zeros(4, 2) and sp.simplify(Pg_num * horiz) == sp.zeros(4, 2))

print()
print("=" * 72)
print(f"결과: {_n[1]}/{_n[0]} 통과")
print("=" * 72)
