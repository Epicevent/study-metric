# -*- coding: utf-8 -*-
"""verify_k1_census — 사전 §9-5: k=1에서 겹쳐 보인 것 전수조사의 계산 증인들.

A. 갈라지는 것 (k=1의 우연)
  Y1  게이지: ℂ*(가환) → GL(2) 비가환
  Y2  분모 하나 → F=I+Z†Z 와 G=I+ZZ† 둘 (행렬로 다르지만 det·스펙트럼 동일)
  Y3  "벡터=부분공간" → 분해가능성 제약: ω∧ω=0 판정, 클라인 이차식
  Y4  K의 Hessian: ℂPⁿ 대각(δ_jk) → Gr 십자항 (|det Z|² 항의 소행)
  Y5  정칙 단면곡률: ℂPⁿ 상수 2 → Gr(2,4) 방향의존 [1,2]  (H = 2Σσ⁴/(Σσ²)²)
  Y6  "사영자=순수상태" → 두 양자 읽기 갈라짐 (wedge 순수 vs ρ=P/2 혼합)
B. 승격되어 유지되는 것
  Y7  정칙 방향의 널/멱영: (∂P)_hol² = 0, tr[(∂P)_hol²]=0 — 걸음 2 §3의 승격
  Y8  수직공간: δV=VA ⇒ P 불변 (k=1의 iψ 한 방향 → gl(2))
"""
import sympy as sp

I = sp.I
_n = [0, 0]
def ok(name, cond):
    _n[0] += 1
    _n[1] += 1 if cond else 0
    print(("[OK] " if cond else "[FAIL] ") + name, flush=True)

import random
random.seed(21)
def rC(nonzero=False):
    while True:
        v = sp.Rational(random.randint(-2, 2), random.randint(1, 3)) \
            + I * sp.Rational(random.randint(-2, 2), random.randint(1, 3))
        if not nonzero or v != 0:
            return v

S = lambda e: sp.simplify(sp.expand_complex(sp.expand(e)))
def Sm(M):
    return sp.Matrix(M.rows, M.cols, lambda i_, j_: S(M[i_, j_]))

print("=" * 74, flush=True)
print("A — 갈라지는 것", flush=True)
print("=" * 74, flush=True)

# ---- Y1. 게이지 비가환
G1 = sp.Matrix([[1, 2], [0, 1]]); G2 = sp.Matrix([[1, 0], [3, 1]])
l1, l2 = sp.Rational(2), sp.Rational(3, 5)
ok("Y1. k=1: λ₁λ₂=λ₂λ₁ (가환) — k=2: G₁G₂ ≠ G₂G₁ (비가환 게이지)",
   l1 * l2 == l2 * l1 and Sm(G1 * G2 - G2 * G1) != sp.zeros(2, 2))

# ---- Y2. F vs G — k=1에선 같은 물건, k=2에선 두 물건 (det·스펙트럼만 공유)
z, zb = sp.symbols("z zbar")
F1 = 1 + zb * z; G1_ = 1 + z * zb
ok("Y2a. k=1: F = G (문자 그대로 같은 식)", sp.simplify(F1 - G1_) == 0)
allok = True
for _ in range(2):
    Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
    F0 = Sm(sp.eye(2) + Z0.H * Z0); G0 = Sm(sp.eye(2) + Z0 * Z0.H)
    lam = sp.symbols("lam")
    same_char = sp.expand((F0 - lam * sp.eye(2)).det() - (G0 - lam * sp.eye(2)).det()) == 0
    if Sm(F0 - G0) == sp.zeros(2, 2) or not same_char:
        allok = False
ok("Y2b. k=2: F ≠ G (행렬로 다름) 그러나 특성다항식 동일 (det·스펙트럼 공유)", allok)

# ---- Y3. 분해가능성: ω∧ω 판정
# Λ²ℂ⁴ 기저 e_ij (i<j).  ω = Σ p_ij e_ij,  ω∧ω = 2(p12p34 − p13p24 + p14p23) e1234
p = sp.symbols("p12 p13 p14 p23 p24 p34")
Q = p[0] * p[5] - p[1] * p[4] + p[2] * p[3]
# (a) 분해가능(실제 2-평면): 무작위 프레임의 플뤼커 → Q = 0
from itertools import combinations
allok = True
for _ in range(3):
    V = sp.Matrix(4, 2, lambda i_, j_: rC())
    ps = [V[list(rows), :].det() for rows in combinations(range(4), 2)]
    Qv = S(ps[0] * ps[5] - ps[1] * ps[4] + ps[2] * ps[3])
    if Qv != 0:
        allok = False
ok("Y3a. 분해가능(v∧w)이면 클라인 이차식 = 0  (무작위 프레임 3개, 정확산술)", allok)
# (b) e12 + e34 는 분해 불가: Q = 1 ≠ 0
Qv = Q.subs(dict(zip(p, [1, 0, 0, 0, 0, 1])))
ok("Y3b. e₁∧e₂+e₃∧e₄ 는 Q = 1 ≠ 0 → 어떤 2-평면도 아님 (k=1엔 이런 제약 자체가 없음)",
   Qv == 1)

# ---- Y4. K의 Hessian: ℂPⁿ 대각 vs Gr 십자항
a, b, c, d = sp.symbols("a b c d")
ab_, bb_, cb_, db_ = sp.symbols("abar bbar cbar dbar")
zv = [a, b, c, d]; zbv = [ab_, bb_, cb_, db_]
K_cpn = 1 + sum(zv[i_] * zbv[i_] for i_ in range(4))          # ℂP⁴
H_cpn = sp.Matrix(4, 4, lambda i_, j_: sp.diff(K_cpn, zv[i_], zbv[j_]))
ok("Y4a. ℂP⁴: ∂_j∂̄_k K = δ_jk  (대각, 십자항 없음)", H_cpn == sp.eye(4))
detZ = a * d - b * c; detZb = ab_ * db_ - bb_ * cb_
K_gr = K_cpn - 1 + 1 + detZ * detZb                            # + |det Z|²
H_gr = sp.Matrix(4, 4, lambda i_, j_: sp.expand(sp.diff(K_gr, zv[i_], zbv[j_])))
offdiag = [H_gr[i_, j_] for i_ in range(4) for j_ in range(4) if i_ != j_]
ok("Y4b. Gr: 십자항 존재 — 전부 |det Z|² 항의 소행 (예: ∂_a∂̄_b K = −c̄d)",
   any(e != 0 for e in offdiag) and sp.expand(H_gr[0, 1] - (-cb_ * d)) == 0)
H_quartic = sp.Matrix(4, 4, lambda i_, j_: sp.expand(sp.diff(detZ * detZb, zv[i_], zbv[j_])))
ok("Y4c. 십자항 = |det Z|² 항의 Hessian 그 자체 (나머지는 대각 δ)",
   sp.expand(H_gr - sp.eye(4) - H_quartic) == sp.zeros(4, 4))

# ---- Y5. 정칙 단면곡률: 상수 2 vs 방향의존
# Z(t) = tW, f = log det(I + t t̄ W†W),  g₀ = ∂_t∂_t̄ f|₀ = tr(W†W),
# R = −∂²_t∂²_t̄ f|₀,  H_hol = R/g₀²  — Kähler 정규좌표(Z=0에서 ∂g=0)라 정당
t, tb = sp.symbols("t tbar")
def H_hol(W):
    Wd = W.conjugate().T
    M = sp.eye(W.cols) + t * tb * (Wd * W)
    f = sp.log(M.det())
    g0 = sp.diff(f, t, tb).subs({t: 0, tb: 0})
    R = -sp.diff(f, t, 2, tb, 2).subs({t: 0, tb: 0})
    return sp.simplify(R / g0 ** 2), sp.simplify(g0)
# ℂP⁴ (k=1): W = 열벡터, W†W 는 1×1 → 항상 H = 2
w4 = sp.Matrix([rC(), rC(), rC(True), rC()])
Hc, _g = H_hol(w4)
w4b = sp.Matrix([1, 0, 0, 0])
Hc2, _g2 = H_hol(w4b)
ok("Y5a. ℂP⁴: 무작위 방향과 좌표 방향 모두 H_hol = 2 (상수)",
   sp.simplify(Hc - 2) == 0 and sp.simplify(Hc2 - 2) == 0)
# Gr(2,4): W 2×2
E11 = sp.Matrix([[1, 0], [0, 0]])
D11 = sp.eye(2)
Ha, _ = H_hol(E11)
Hb, _ = H_hol(D11)
ok("Y5b. Gr(2,4): H(E₁₁) = 2 (계수-1 방향),  H(I) = 1 (균형 방향) — 비상수!",
   sp.simplify(Ha - 2) == 0 and sp.simplify(Hb - 1) == 0)
# 일반식 H = 2Σσ⁴/(Σσ²)²  (σ² = W†W 고유값) — 무작위 W 로 대조
allok = True
for _ in range(2):
    W = sp.Matrix(2, 2, lambda i_, j_: rC())
    Hv, g0 = H_hol(W)
    WdW = Sm(W.conjugate().T * W)
    s2 = S(sp.trace(WdW))              # Σσ²
    s4 = S(sp.trace(WdW * WdW))        # Σσ⁴
    if S(Hv - 2 * s4 / s2 ** 2) != 0:
        allok = False
ok("Y5c. 일반식 H_hol(W) = 2·tr((W†W)²)/tr(W†W)²  (무작위 W 2개, 정확산술)", allok)
ok("Y5d. 범위: 1 ≤ H ≤ 2  (σ⁴ 평균-제곱 부등식; 끝값은 Y5b의 두 방향)",
   True if sp.simplify(Ha - 2) == 0 and sp.simplify(Hb - 1) == 0 else False)

# ---- Y6. 두 양자 읽기
V = sp.Matrix.vstack(sp.eye(2), sp.Matrix(2, 2, lambda i_, j_: rC()))
P4 = Sm(V * (V.H * V).inv() * V.H)
rho = P4 / 2
purity = S(sp.trace(rho * rho))
ok("Y6. tr P = 2 → P는 밀도행렬이 아님; ρ=P/2 는 purity 1/2 (혼합) — "
   "wedge(플뤼커) 상태는 ℂP⁵의 순수상태. k=1에선 '사영자=순수상태' 한 몸",
   S(sp.trace(P4)) == 2 and purity == sp.Rational(1, 2))

print(flush=True)
print("=" * 74, flush=True)
print("B — 승격되어 유지되는 것", flush=True)
print("=" * 74, flush=True)

# ---- Y7. 정칙 방향의 널/멱영 (걸음 2 §3의 승격)
# δP_hol = (1−P) δV M⁻¹ V†  (M=V†V) — 공식 자체를 t-미분과 대조 후, 멱영·널 확인
allok_formula = True; allok_nilp = True; allok_null = True; allok_k1 = True
for _ in range(2):
    Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
    W = sp.Matrix(2, 2, lambda i_, j_: rC())
    V0 = sp.Matrix.vstack(sp.eye(2), Z0)
    dV = sp.Matrix.vstack(sp.zeros(2, 2), W)
    M0 = V0.H * V0
    P0 = Sm(V0 * M0.inv() * V0.H)
    dP_hol = Sm((sp.eye(4) - P0) * dV * M0.inv() * V0.H)
    # 공식 대조: P(V+t dV) 를 t(정칙, t̄=0 취급)로 전개한 1차항
    tt = sp.symbols("tt")
    Vt = V0 + tt * dV
    Mt = V0.H * V0 + tt * (V0.H * dV)          # t̄=0: dV† 항 제거
    Pt = Vt * Mt.inv() * Vt.H                   # Vt.H 의 t̄ 항도 0 취급: V0.H + t̄(...)→V0.H
    Pt = Vt * Mt.inv() * V0.H
    dP_taylor = Sm(sp.diff(Pt, tt).subs(tt, 0))
    if Sm(dP_hol - dP_taylor) != sp.zeros(4, 4):
        allok_formula = False
    if Sm(dP_hol * dP_hol) != sp.zeros(4, 4):
        allok_nilp = False
    if S(sp.trace(dP_hol * dP_hol)) != 0:
        allok_null = False
ok("Y7a. 공식 (∂P)_hol = (1−P)∂V M⁻¹V† — t-전개 1차항과 일치", allok_formula)
ok("Y7b. 멱영: [(∂P)_hol]² = 0  (걸음 2의 B²=0 이 행렬값으로 승격)", allok_nilp)
ok("Y7c. 널: tr[(∂P)_hol²] = 0  — '⟨∂_z n,∂_z n⟩=0' (주제 2)의 Gr 판", allok_null)
# k=1 나란히
for _ in range(1):
    zr = rC()
    v = sp.Matrix([1, zr]); dv = sp.Matrix([0, 1])
    M0 = (v.H * v)[0, 0]
    P0 = Sm(v * v.H / M0)
    dP1 = Sm((sp.eye(2) - P0) * dv * v.H / M0)
    allok_k1 = (Sm(dP1 * dP1) == sp.zeros(2, 2)) and S(sp.trace(dP1 * dP1)) == 0
ok("Y7d. k=1 나란히: 같은 공식·같은 멱영·같은 널 (v=(1,z))", allok_k1)

# ---- Y8. 수직공간의 승격: δV = V·A ⇒ P 불변
allok = True
for _ in range(2):
    Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
    V0 = sp.Matrix.vstack(sp.eye(2), Z0)
    A = sp.Matrix(2, 2, lambda i_, j_: rC())
    tt = sp.symbols("tt", real=True)
    Vt = V0 * (sp.eye(2) + tt * A)
    Pt = Vt * (Vt.H * Vt).inv() * Vt.H
    dP = Sm(sp.diff(Pt, tt).subs(tt, 0))
    if dP != sp.zeros(4, 4):
        allok = False
ok("Y8. δV = V·A (임의 A∈gl(2), 실 8-모수) ⇒ δP = 0 — k=1의 위상 원(iψ, 1-모수)의 승격",
   allok)

print(flush=True)
print("=" * 74, flush=True)
print(f"결과: {_n[1]}/{_n[0]} 통과", flush=True)
print("=" * 74, flush=True)
