# -*- coding: utf-8 -*-
"""verify_volume_side_by_side — 사전 §9-2: 부피를 ℂP¹과 Gr(2,4) 나란히, 같은 기계로 직접 적분.

6c §1은 Vol(Gr(2,4)) = ∫K⁻⁴dV 를 위상(차수 2)으로 '예측'하고 MC로 '표본'했다.
여기서는 그 8차원 적분을 특이값 좌표 + 가우스 보정으로 **정확하게** 계산한다.

PART W1–W3  ℂPⁿ 부피 = πⁿ/n!  (n=1,2,3 — 직접 중적분)
PART W4     ω^n/n! = det(g) dV  (n=2 일반 켈러, 쐐기곱을 성분으로)
PART W5     특이값 측도의 보정상수: 가우스 검문 2개가 같은 c₂ = π⁴/2 를 줌
PART W6     반지름 적분: ∫∫(x₁−x₂)² (1+x₁)⁻⁴(1+x₂)⁻⁴ dx₁dx₂ = 1/6  (베타적분 3개)
PART W7     조립: Vol = (π⁴/2)·(1/6) = π⁴/12 = 2·π⁴/4!  (차수 경로와 일치)
PART W8     클라인 이차식의 차수 = 2  (무작위 직선과의 교점 2개, 정확산술)
PART W9     끝-대-끝 수치: 8차원 MC(중요도표집)가 π⁴/12 를 가리키는지
PART W10    k=1 같은 기계: c₁=π (가우스), ∫(1+x)⁻²dx=1 → Vol(ℂP¹)=π=1·π¹/1!
"""
import sympy as sp

I = sp.I
_n = [0, 0]
def ok(name, cond):
    _n[0] += 1
    _n[1] += 1 if cond else 0
    print(("[OK] " if cond else "[FAIL] ") + name, flush=True)

x, y, r, th = sp.symbols("x y r theta", positive=True)

print("=" * 74, flush=True)
print("PART W1–W3 — ℂPⁿ 부피 = πⁿ/n!  (직접 중적분)", flush=True)
print("=" * 74, flush=True)
# 규약: ω=(i/2)∂∂̄logK, ω^n/n! = det g · dV,  det g = S^{-(n+1)}, S=1+Σ|z_k|²
# 각 복소변수 극좌표: dV_k = π dx_k  (x_k=r_k², 각도 2π·(1/2))
x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
V1 = sp.pi * sp.integrate((1 + x1) ** -2, (x1, 0, sp.oo))
ok("W1. Vol(ℂP¹) = π·∫(1+x)⁻²dx = π", sp.simplify(V1 - sp.pi) == 0)
V2 = sp.pi ** 2 * sp.integrate(
    sp.integrate((1 + x1 + x2) ** -3, (x2, 0, sp.oo)), (x1, 0, sp.oo))
ok("W2. Vol(ℂP²) = π²·∬(1+x₁+x₂)⁻³ = π²/2", sp.simplify(V2 - sp.pi ** 2 / 2) == 0)
V3 = sp.pi ** 3 * sp.integrate(sp.integrate(sp.integrate(
    (1 + x1 + x2 + x3) ** -4, (x3, 0, sp.oo)), (x2, 0, sp.oo)), (x1, 0, sp.oo))
ok("W3. Vol(ℂP³) = π³/6 — 사다리 πⁿ/n! 확인", sp.simplify(V3 - sp.pi ** 3 / 6) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART W4 — ω²/2! = det(g)·dV  (일반 2변수 켈러, 쐐기곱 성분 계산)", flush=True)
print("=" * 74, flush=True)
# ω = (i/2) Σ g_{jk̄} dz_j∧dz̄_k.  형식 계산: dz_j∧dz̄_k 를 반대칭 기호로 처리.
# 2변수에서 ω∧ω 의 (i/2)²dz1∧dz̄1∧dz2∧dz̄2 계수가 2!·det(g) 인지 확인.
g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
# ω∧ω 에서 살아남는 항: (j,k),(j',k') 로 {z1,z2},{z̄1,z̄2} 를 다 덮는 조합
# = g11 g22 (dz1dz̄1dz2dz̄2) + g22 g11 (dz2dz̄2dz1dz̄1) + g12 g21 (dz1dz̄2dz2dz̄1) + g21 g12 (dz2dz̄1dz1dz̄2)
# 부호: dz1dz̄1dz2dz̄2 기준으로 재배열
#  dz2∧dz̄2∧dz1∧dz̄1 = +기준 (2-형식 두 개 교환: 부호 +)
#  dz1∧dz̄2∧dz2∧dz̄1 = dz1∧dz̄1∧dz2∧dz̄2 로 재배열: dz̄2↔dz2 (−), dz̄2↔dz̄1 (−)… 직접 순열 부호로:
import itertools
base = ["z1", "zb1", "z2", "zb2"]
def sign_of(order):
    # order: 리스트 (base 의 순열), 전치 횟수 부호
    perm = [base.index(o) for o in order]
    s = 1
    p = list(perm)
    for i_ in range(len(p)):
        for j_ in range(i_ + 1, len(p)):
            if p[i_] > p[j_]:
                s = -s
    return s
terms = []
labels = ["z1", "z2"]; lab_b = ["zb1", "zb2"]
for (j, k), (jp, kp) in itertools.product(itertools.product(range(2), range(2)), repeat=2):
    order = [labels[j], lab_b[k], labels[jp], lab_b[kp]]
    if len(set(order)) < 4:
        continue
    gjk = [[g11, g12], [g21, g22]][j][k]
    gjpkp = [[g11, g12], [g21, g22]][jp][kp]
    terms.append(sign_of(order) * gjk * gjpkp)
coeff = sp.expand(sum(terms))
ok("W4. ω∧ω 계수 = 2!·det g  (g11g22−g12g21 의 2배)",
   sp.expand(coeff - 2 * (g11 * g22 - g12 * g21)) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART W5 — 특이값 측도 보정: 가우스 검문 2개", flush=True)
print("=" * 74, flush=True)
# 주장: ℂ^{2×2} 에서 Z†Z 고유값 (x₁,x₂) 만 보는 적분은
#   ∫ f(x₁,x₂) dZ = c₂ ∬ f·(x₁−x₂)² dx₁dx₂   (x_i ≥ 0, 비순서)
# 보정 검문 ① ∫e^{-tr Z†Z}dZ = π⁴ (복소 가우스 4개)
gauss1_flat = sp.pi ** 4
e1 = sp.integrate(sp.integrate(
    sp.exp(-x1 - x2) * (x1 - x2) ** 2, (x2, 0, sp.oo)), (x1, 0, sp.oo))
c2 = sp.simplify(gauss1_flat / e1)
ok(f"W5a. 검문①: ∬e^{{-x₁-x₂}}(x₁−x₂)² = {e1} → c₂ = π⁴/{sp.simplify(sp.pi**4/c2)}",
   sp.simplify(c2 - sp.pi ** 4 / 2) == 0)
# 보정 검문 ② ∫ tr(Z†Z)·e^{-tr}dZ = 4π⁴  (성분당 ∫|z|²e^{-|z|²} = π)
gauss2_flat = 4 * sp.pi ** 4
e2 = sp.integrate(sp.integrate(
    (x1 + x2) * sp.exp(-x1 - x2) * (x1 - x2) ** 2, (x2, 0, sp.oo)), (x1, 0, sp.oo))
ok("W5b. 검문②: ∬(x₁+x₂)e^{-x₁-x₂}(x₁−x₂)² = 8 → 같은 c₂ = π⁴/2  (두 검문 일치)",
   sp.simplify(gauss2_flat / e2 - sp.pi ** 4 / 2) == 0)
# K 가 특이값에서 인수분해되는지: K = det(I+Z†Z) = (1+x₁)(1+x₂)  — 무작위 정확산술
import random
random.seed(5)
def rC():
    return sp.Rational(random.randint(-2, 2), random.randint(1, 3)) \
         + I * sp.Rational(random.randint(-2, 2), random.randint(1, 3))
allok = True
for _ in range(2):
    Zr = sp.Matrix(2, 2, lambda i_, j_: rC())
    Hm = (Zr.conjugate().T) * Zr
    Kv = sp.expand((sp.eye(2) + Hm).det())
    # 고유값 대칭식으로: (1+x₁)(1+x₂) = 1 + tr + det
    Kv2 = sp.expand(1 + sp.trace(Hm) + Hm.det())
    if sp.simplify(Kv - Kv2) != 0:
        allok = False
ok("W5c. K = det(I+Z†Z) = 1+tr+det = (1+x₁)(1+x₂)  (특이값 인수분해, 정확산술)", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART W6 — 반지름 적분 (베타적분 3개)", flush=True)
print("=" * 74, flush=True)
a0 = sp.integrate((1 + x1) ** -4, (x1, 0, sp.oo))
a1 = sp.integrate(x1 * (1 + x1) ** -4, (x1, 0, sp.oo))
a2 = sp.integrate(x1 ** 2 * (1 + x1) ** -4, (x1, 0, sp.oo))
ok(f"W6a. a₀,a₁,a₂ = ∫xᵐ(1+x)⁻⁴dx = {a0}, {a1}, {a2}",
   (a0, a1, a2) == (sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 3)))
R = sp.integrate(sp.integrate(
    (x1 - x2) ** 2 * (1 + x1) ** -4 * (1 + x2) ** -4, (x2, 0, sp.oo)), (x1, 0, sp.oo))
ok("W6b. ∬(x₁−x₂)²(1+x₁)⁻⁴(1+x₂)⁻⁴ = 2(a₂a₀−a₁²) = 1/6",
   sp.simplify(R - sp.Rational(1, 6)) == 0
   and sp.simplify(2 * (a2 * a0 - a1 ** 2) - sp.Rational(1, 6)) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART W7 — 조립: 적분값 = 위상 예측값", flush=True)
print("=" * 74, flush=True)
Vol = sp.simplify(c2 * R)
ok("W7a. Vol(Gr(2,4)) = c₂·(1/6) = π⁴/12  (적분을 직접 한 값)",
   sp.simplify(Vol - sp.pi ** 4 / 12) == 0)
ok("W7b. 차수 경로와 일치: π⁴/12 = 2·π⁴/4!  (6c §1.4)",
   sp.simplify(Vol - 2 * sp.pi ** 4 / sp.factorial(4)) == 0)
ok("W7c. ℂP¹ 나란히: π = 1·π¹/1!  (차수 1)",
   sp.simplify(V1 - 1 * sp.pi / sp.factorial(1)) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART W8 — 클라인 이차식의 차수 2 (무작위 직선 교점, 정확산술)", flush=True)
print("=" * 74, flush=True)
# Q(p) = p12·p34 − p13·p24 + p14·p23,  무작위 직선 p(t) = u + t·v 에서 근 2개
t = sp.symbols("t")
random.seed(9)
allok = True
for _ in range(2):
    u = [rC() for _ in range(6)]
    v = [rC() for _ in range(6)]
    p = [u[i_] + t * v[i_] for i_ in range(6)]
    Q = sp.expand(p[0] * p[5] - p[1] * p[4] + p[2] * p[3])
    poly = sp.Poly(Q, t)
    disc = poly.discriminant()
    if poly.degree() != 2 or disc == 0:
        allok = False
ok("W8. 무작위 직선 2개: Q 제한 = t의 이차식, 판별식 ≠ 0 → 교점 정확히 2개 = deg", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART W9 — 끝-대-끝 수치: 8차원 MC (중요도표집)", flush=True)
print("=" * 74, flush=True)
# 각 성분 z 를 FS 밀도 q(z)=1/(π(1+|z|²)²) 로 표집: x=|z|² 는 x=u/(1−u), 위상 균등
# 가중치 = K⁻⁴ / Πq = K⁻⁴ · π⁴ · Π(1+|z_i|²)²
import numpy as np
rng = np.random.default_rng(42)
N = 300_000
uu = rng.random((N, 4))
xx = uu / (1 - uu)                       # |z|²
ph = rng.random((N, 4)) * 2 * np.pi
zz = np.sqrt(xx) * np.exp(1j * ph)       # N×4 : a,b,c,d
A_, B_, C_, D_ = zz[:, 0], zz[:, 1], zz[:, 2], zz[:, 3]
Kv = 1 + np.abs(A_) ** 2 + np.abs(B_) ** 2 + np.abs(C_) ** 2 + np.abs(D_) ** 2 \
     + np.abs(A_ * D_ - B_ * C_) ** 2
wgt = (np.pi ** 4) * np.prod((1 + xx) ** 2, axis=1) / Kv ** 4
est = wgt.mean(); se = wgt.std(ddof=1) / np.sqrt(N)
target = float(sp.pi ** 4 / 12)
print(f"   MC 추정 = {est:.4f} ± {se:.4f}   (참값 π⁴/12 = {target:.5f})", flush=True)
ok("W9. |MC − π⁴/12| < 4σ  (끝-대-끝: 8차원 적분이 정확값을 가리킴)",
   abs(est - target) < 4 * se)

print(flush=True)
print("=" * 74, flush=True)
print("PART W10 — k=1 같은 기계", flush=True)
print("=" * 74, flush=True)
# 가우스 보정: ∫_ℂ e^{-|z|²}dV = π = c₁·∫e^{-x}dx → c₁ = π
c1 = sp.pi / sp.integrate(sp.exp(-x1), (x1, 0, sp.oo))
ok("W10. c₁ = π,  Vol(ℂP¹) = c₁·∫(1+x)⁻² = π — 같은 기계의 k=1 (밴더몬드 없음)",
   sp.simplify(c1 - sp.pi) == 0 and sp.simplify(c1 * sp.integrate((1 + x1) ** -2, (x1, 0, sp.oo)) - sp.pi) == 0)

print(flush=True)
print("=" * 74, flush=True)
print(f"결과: {_n[1]}/{_n[0]} 통과", flush=True)
print("=" * 74, flush=True)
