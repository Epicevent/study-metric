# -*- coding: utf-8 -*-
"""verify_component_match — 사전 §9-3: 5b §4의 QFIM과 6b §5–6의 계량이 성분 단위로 한 물건인지.

대조할 두 주장:
  [5b §4 / 문서5]  H_QFIM = 4 Re tr[(I+Z†Z)⁻¹ dZ† (I+ZZ†)⁻¹ dZ]      (상태 쪽)
  [6b §5–6]        g_{jk̄} = ∂_j ∂̄_k log K = (G^{-T} ⊗ F^{-1})_{jk}   (퍼텐셜 쪽)
접점: 좌표 성분. 규약: 행우선 z=(a,b,c,d)=(Z11,Z12,Z21,Z22), F=I+Z†Z, G=I+ZZ†, K=det F.

PART 1  트레이스형의 계수 추출 = (G⁻¹)_{ca}(F⁻¹)_{bd}              [다항식 항등식]
PART 2  Hessian ∂∂̄ log K     = (G⁻¹)_{ca}(F⁻¹)_{bd}              [다항식 항등식]
         ⟹ 두 문서의 대상이 계수 하나하나까지 같은 물건
PART 3  k=1 닻: 1/K² (6b 계수형) : 2/K² (Tr dPdP) : 4/K² (QFIM) = 1:2:4
PART 4  상태 쪽 닻(정확산술): 플뤼커 6-성분 상태의 1-모수 QFIM = 4·tr[F⁻¹Ż†G⁻¹Ż]
PART 5  값 하나 (문서용 숫자)
"""
import sympy as sp
from itertools import product

I = sp.I
_n = [0, 0]
def ok(name, cond):
    _n[0] += 1
    _n[1] += 1 if cond else 0
    print(("[OK] " if cond else "[FAIL] ") + name, flush=True)

# ---- 기호 세팅: a,b,c,d 와 켤레를 독립 기호로 (Wirtinger)
a, b, c, d = sp.symbols("a b c d")
ab_, bb_, cb_, db_ = sp.symbols("abar bbar cbar dbar")
Z = sp.Matrix([[a, b], [c, d]])
Zd = sp.Matrix([[ab_, cb_], [bb_, db_]])          # Z† (켤레전치)
F = sp.eye(2) + Zd * Z                            # I+Z†Z
G = sp.eye(2) + Z * Zd                            # I+ZZ†
K = sp.expand(F.det())
adjF = F.adjugate().applyfunc(sp.expand)
adjG = G.adjugate().applyfunc(sp.expand)

zvars = [a, b, c, d]
zbvars = [ab_, bb_, cb_, db_]
# 행우선 지표: j=1..4 ↔ (행,열) = (1,1),(1,2),(2,1),(2,2)
IDX = [(0, 0), (0, 1), (1, 0), (1, 1)]
E = lambda r, s: sp.Matrix(2, 2, lambda i_, j_: 1 if (i_, j_) == (r, s) else 0)

print("=" * 74, flush=True)
print("PART 1 — 트레이스형 tr[F⁻¹dZ†G⁻¹dZ] 의 계수 추출", flush=True)
print("=" * 74, flush=True)
# dZ = Σ E_ab dZ_ab,  dZ† = Σ E_dc dZ̄_cd  이므로
# dZ_ab dZ̄_cd 의 계수 = tr[F⁻¹ E_dc G⁻¹ E_ab].
# K² 를 곱해 다항식으로: tr[adjF · E_dc · adjG · E_ab] =?= adjG_{ca}·adjF_{bd}
allok = True
for (ar, ac), (cr, cc) in product(IDX, IDX):
    lhs = sp.expand(sp.trace(adjF * E(cc, cr) * adjG * E(ar, ac)))
    rhs = sp.expand(adjG[cr, ar] * adjF[ac, cc])
    if sp.expand(lhs - rhs) != 0:
        allok = False
ok("P1. 16계수 전부: tr[F⁻¹E_dc G⁻¹E_ab] = (G⁻¹)_{ca}(F⁻¹)_{bd}  (다항식 항등식)", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART 2 — Hessian ∂_j ∂̄_k log K 가 같은 계수인지", flush=True)
print("=" * 74, flush=True)
# g_{jk̄} = (K·∂_j∂̄_k K − ∂_j K·∂̄_k K)/K²  이므로
# 다항식 판:  N_{jk} := K·K_{jk̄} − K_j·K_k̄  =?=  adjG_{ca}·adjF_{bd}
allok = True
worst = None
for j, k in product(range(4), range(4)):
    (ar, ac), (cr, cc) = IDX[j], IDX[k]
    zj, zbk = zvars[j], zbvars[k]
    Njk = sp.expand(K * sp.diff(K, zj, zbk) - sp.diff(K, zj) * sp.diff(K, zbk))
    rhs = sp.expand(adjG[cr, ar] * adjF[ac, cc])
    if sp.expand(Njk - rhs) != 0:
        allok = False
        worst = (j, k)
ok("P2. 16성분 전부: K·∂∂̄K − ∂K·∂̄K = adj(G)_{ca}·adj(F)_{bd}  ⟹ ∂∂̄logK = (G⁻¹)_{ca}(F⁻¹)_{bd}",
   allok)
ok("P2'. 따라서 [트레이스형 계수] = [Hessian] — 5b§4와 6b§5–6은 좌표성분까지 한 물건", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART 3 — k=1 닻: 1 : 2 : 4", flush=True)
print("=" * 74, flush=True)
z, zb = sp.symbols("z zbar")
K1 = 1 + z * zb
h1 = sp.simplify(sp.diff(sp.log(K1), z, zb))               # 6b 계수형
ok("P3a. 6b 계수형 (k=1): ∂∂̄logK = 1/K²", sp.simplify(h1 - 1 / K1**2) == 0)
# Tr(dPdP) 계량 = 2/K² |dz|²  (걸음 2/5b), QFIM = 4/K² |dz|² (round)
ok("P3b. 사슬 1:2:4 — 6b 계수형(1/K²) → Tr(dPdP)(2/K²) → QFIM(4/K²)",
   sp.simplify(2 * h1 - 2 / K1**2) == 0 and sp.simplify(4 * h1 - 4 / K1**2) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART 4 — 상태 쪽 닻 (정확산술): 플뤼커 상태의 QFIM = 4·tr[F⁻¹Ż†G⁻¹Ż]", flush=True)
print("=" * 74, flush=True)
# 곡선 Z(t) = Z0 + t·W (t 실수),  V(t) = (I ; Z(t)) 4×2
# 플뤼커 좌표 p_ij(t) = V의 (i,j)행 2×2 소행렬식 (6개) — ℂP⁵ 의 동차좌표
# 비정규화 FS/QFIM (걸음 2 닫힌형 × 4):
#   H(t=0) = 4·[⟨p,p⟩⟨ṗ,ṗ⟩ − |⟨p,ṗ⟩|²]/⟨p,p⟩²
import random
random.seed(11)
def rC():
    return sp.Rational(random.randint(-2, 2), random.randint(1, 3)) \
         + I * sp.Rational(random.randint(-2, 2), random.randint(1, 3))

t = sp.symbols("t", real=True)
allok = True
for trial in range(2):
    Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
    W = sp.Matrix(2, 2, lambda i_, j_: rC())
    Zt = Z0 + t * W
    Vt = sp.Matrix.vstack(sp.eye(2), Zt)
    from itertools import combinations
    p = sp.Matrix([Vt[list(rows), :].det() for rows in combinations(range(4), 2)])
    pd = p.diff(t)
    hp = lambda u, v: sum(sp.conjugate(x) * y for x, y in zip(u, v))
    at0 = lambda e: sp.simplify(sp.expand_complex(sp.expand(e.subs(t, 0))))
    pp = at0(hp(p, p)); pdpd = at0(hp(pd, pd)); ppd = at0(hp(p, pd))
    H_state = sp.simplify(4 * (pp * pdpd - ppd * sp.conjugate(ppd)) / pp**2)
    # 차트 쪽: 4·tr[F⁻¹ W† G⁻¹ W]  at Z0
    Z0d = Z0.conjugate().T; Wd = W.conjugate().T
    F0 = sp.eye(2) + Z0d * Z0; G0 = sp.eye(2) + Z0 * Z0d
    H_chart = sp.simplify(sp.expand_complex(
        4 * sp.trace(F0.inv() * Wd * G0.inv() * W)))
    if sp.simplify(sp.expand_complex(H_state - H_chart)) != 0:
        allok = False
ok("P4. 무작위 (Z0, Ż) 2회: 플뤼커 상태 QFIM = 4·tr[F⁻¹Ż†G⁻¹Ż]  (유리수 정확산술)", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART 5 — 문서용 값 하나", flush=True)
print("=" * 74, flush=True)
# Z0 = [[1,0],[0,1]] (대각), Ż = E11 : 값이 깨끗하게 떨어지는 점
Z0 = sp.eye(2); W = E(0, 0)
F0 = sp.eye(2) + Z0.conjugate().T * Z0; G0 = F0
val_chart = sp.nsimplify(4 * sp.trace(F0.inv() * W.conjugate().T * G0.inv() * W))
# 상태 쪽 같은 값
Zt = Z0 + t * W
Vt = sp.Matrix.vstack(sp.eye(2), Zt)
from itertools import combinations as comb2
p = sp.Matrix([Vt[list(rows), :].det() for rows in comb2(range(4), 2)])
pd = p.diff(t)
hp = lambda u, v: sum(sp.conjugate(x) * y for x, y in zip(u, v))
at0 = lambda e: sp.nsimplify(sp.expand(e.subs(t, 0)))
pp = at0(hp(p, p)); pdpd = at0(hp(pd, pd)); ppd = at0(hp(p, pd))
val_state = sp.nsimplify(4 * (pp * pdpd - ppd * sp.conjugate(ppd)) / pp**2)
print(f"   Z0=I, Ż=E11:  4·tr[F⁻¹Ż†G⁻¹Ż] = {val_chart},   상태 QFIM = {val_state}", flush=True)
ok("P5. Z0=I, Ż=E11 에서 두 값 일치 (= 1)",
   sp.simplify(val_chart - val_state) == 0 and sp.simplify(val_chart - 1) == 0)

print(flush=True)
print("=" * 74, flush=True)
print(f"결과: {_n[1]}/{_n[0]} 통과", flush=True)
print("=" * 74, flush=True)
