# -*- coding: utf-8 -*-
"""verify_chart_change — 사전 §9-4: 차트 갈아타기 실물 (z′=1/z ↔ Z′=Z⁻¹).

PART X1  ℂP¹ 세 줄: K′=K/|z|², ∂∂̄log|z|²=0, g′|dz′|²=g|dz|²
PART X2  풀스왑 게이지: (I;Z)·Z⁻¹=(Z′;I), 사영자 불변
PART X3  K′ = K/|det Z|²  (실베스터)
PART X4  퍼텐셜 어긋남 log|det Z|² 은 ∂∂̄ 가 죽인다  (6ab 실물)
PART X5  밀어넘기기 보조정리 2개: F⁻¹=Z⁻¹G⁻¹Z,  F⁻¹Z†=Z†G⁻¹
PART X6  계량(에르미트 형식 전체, ω 포함) 불변: tr[F′⁻¹U′†G′⁻¹W′]=tr[F⁻¹U†G⁻¹W]
PART X7  혼합 차트 {1,3}: k=1엔 없는 전이 — Z′ 성분식, 유효조건 = p₁₃≠0, K′=K/|p₁₃|², 계량 불변
PART X8  전역 그림: K_chart = Σ|p_ij|² / |p_chart|²  (코시–비네 ↔ 차트)
"""
import sympy as sp
from itertools import combinations

I = sp.I
_n = [0, 0]
def ok(name, cond):
    _n[0] += 1
    _n[1] += 1 if cond else 0
    print(("[OK] " if cond else "[FAIL] ") + name, flush=True)

import random
random.seed(3)
def rC(nonzero=False):
    while True:
        v = sp.Rational(random.randint(-2, 2), random.randint(1, 3)) \
            + I * sp.Rational(random.randint(-2, 2), random.randint(1, 3))
        if not nonzero or v != 0:
            return v

def rZ_inv():
    """가역 무작위 유리복소 2×2"""
    while True:
        Zr = sp.Matrix(2, 2, lambda i_, j_: rC())
        if Zr.det() != 0:
            return Zr

S = lambda e: sp.simplify(sp.expand_complex(sp.expand(e)))
def Sm(M):
    return sp.Matrix(M.rows, M.cols, lambda i_, j_: S(M[i_, j_]))

print("=" * 74, flush=True)
print("PART X1 — ℂP¹ 세 줄", flush=True)
print("=" * 74, flush=True)
z, zb = sp.symbols("z zbar")
Kc = 1 + z * zb
Kcp = 1 + (1 / z) * (1 / zb)                       # K′ = 1+|z′|², z′=1/z
ok("X1a. K′ = K/|z|²", sp.simplify(Kcp - Kc / (z * zb)) == 0)
ok("X1b. ∂∂̄ log|z|² = 0  (log z + log z̄ 의 혼합미분)",
   sp.diff(sp.log(z) + sp.log(zb), z, zb) == 0)
# g′|dz′|² = g|dz|² : g=1/K², dz′=−dz/z² → |dz′|²=|dz|²/|z|⁴
g_ = 1 / Kc ** 2
gp = 1 / Kcp ** 2
ok("X1c. g′·|dz′/dz|² = g  (계량은 텐서로 불변)",
   sp.simplify(gp * (1 / (z ** 2 * zb ** 2)) - g_) == 0)

print(flush=True)
print("=" * 74, flush=True)
print("PART X2 — 풀스왑 게이지: (I;Z)·Z⁻¹ = (Z⁻¹;I), 사영자 불변", flush=True)
print("=" * 74, flush=True)
allok_frame = True; allok_P = True
for _ in range(2):
    Z0 = rZ_inv()
    V = sp.Matrix.vstack(sp.eye(2), Z0)
    V2 = Sm(V * Z0.inv())
    target = sp.Matrix.vstack(Sm(Z0.inv()), sp.eye(2))
    if Sm(V2 - target) != sp.zeros(4, 2):
        allok_frame = False
    P1 = Sm(V * (V.H * V).inv() * V.H)
    P2 = Sm(V2 * (V2.H * V2).inv() * V2.H)
    if Sm(P1 - P2) != sp.zeros(4, 4):
        allok_P = False
ok("X2a. (I;Z)·Z⁻¹ = (Z⁻¹; I)  — 아래 블록이 I가 되는 차트", allok_frame)
ok("X2b. 사영자 P 불변 (같은 2-평면의 두 차트)", allok_P)

print(flush=True)
print("=" * 74, flush=True)
print("PART X3 — K′ = K/|det Z|²", flush=True)
print("=" * 74, flush=True)
allok = True
for _ in range(3):
    Z0 = rZ_inv()
    Zp = Sm(Z0.inv())
    K0 = S((sp.eye(2) + Z0.H * Z0).det())
    Kp = S((sp.eye(2) + Zp.H * Zp).det())
    dz2 = S(Z0.det() * sp.conjugate(Z0.det()))
    if S(Kp - K0 / dz2) != 0:
        allok = False
ok("X3. K′ = K/|det Z|²  (무작위 가역 Z 3개, 정확산술) — ℂP¹의 K/|z|² 승격", allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART X4 — 퍼텐셜 어긋남은 ∂∂̄ 가 죽인다", flush=True)
print("=" * 74, flush=True)
a, b, c, d = sp.symbols("a b c d")
ab_, bb_, cb_, db_ = sp.symbols("abar bbar cbar dbar")
detZ = a * d - b * c
detZb = ab_ * db_ - bb_ * cb_
mismatch = sp.log(detZ) + sp.log(detZb)            # log|det Z|²
allok = all(sp.diff(mismatch, zj, zbk) == 0
            for zj in (a, b, c, d) for zbk in (ab_, bb_, cb_, db_))
ok("X4. ∂_j∂̄_k log|det Z|² = 0 (16개 전부) — 정칙+반정칙이라 혼합미분에 죽음 (6ab 실물)",
   allok)

print(flush=True)
print("=" * 74, flush=True)
print("PART X5 — 밀어넘기기 보조정리 2개", flush=True)
print("=" * 74, flush=True)
allok1 = True; allok2 = True
for _ in range(2):
    Z0 = rZ_inv()
    F0 = sp.eye(2) + Z0.H * Z0
    G0 = sp.eye(2) + Z0 * Z0.H
    if Sm(F0.inv() - Z0.inv() * G0.inv() * Z0) != sp.zeros(2, 2):
        allok1 = False
    if Sm(F0.inv() * Z0.H - Z0.H * G0.inv()) != sp.zeros(2, 2):
        allok2 = False
ok("X5a. F⁻¹ = Z⁻¹G⁻¹Z   (ZF=GZ 에서)", allok1)
ok("X5b. F⁻¹Z† = Z†G⁻¹  (FZ†=Z†G 에서)", allok2)

print(flush=True)
print("=" * 74, flush=True)
print("PART X6 — 에르미트 형식 전체(실부=계량, 허부=ω)가 불변", flush=True)
print("=" * 74, flush=True)
# 접벡터 변환: W′ = −Z⁻¹ W Z⁻¹  (dz′=−dz/z² 의 승격)
allok_diag = True; allok_sesq = True
for _ in range(2):
    Z0 = rZ_inv()
    W = sp.Matrix(2, 2, lambda i_, j_: rC())
    U = sp.Matrix(2, 2, lambda i_, j_: rC())
    Zi = Z0.inv()
    Wp = Sm(-Zi * W * Zi); Up = Sm(-Zi * U * Zi)
    Zp = Sm(Zi)
    F0 = sp.eye(2) + Z0.H * Z0; G0 = sp.eye(2) + Z0 * Z0.H
    Fp = sp.eye(2) + Zp.H * Zp; Gp = sp.eye(2) + Zp * Zp.H
    t_old = S(sp.trace(F0.inv() * W.H * G0.inv() * W))
    t_new = S(sp.trace(Fp.inv() * Wp.H * Gp.inv() * Wp))
    if S(t_old - t_new) != 0:
        allok_diag = False
    s_old = S(sp.trace(F0.inv() * U.H * G0.inv() * W))
    s_new = S(sp.trace(Fp.inv() * Up.H * Gp.inv() * Wp))
    if S(s_old - s_new) != 0:
        allok_sesq = False
ok("X6a. 대각: tr[F′⁻¹W′†G′⁻¹W′] = tr[F⁻¹W†G⁻¹W]  (계량 불변)", allok_diag)
ok("X6b. 세스퀴: tr[F′⁻¹U′†G′⁻¹W′] = tr[F⁻¹U†G⁻¹W]  (허부 = ω 까지 불변)", allok_sesq)

print(flush=True)
print("=" * 74, flush=True)
print("PART X7 — 혼합 차트 {1,3}: k=1 엔 없는 전이", flush=True)
print("=" * 74, flush=True)
# V=(I;Z) 의 행: r1=(1,0), r2=(0,1), r3=(a,b), r4=(c,d)
# 차트 {1,3}: 행 1,3 을 I 로 — 유효조건은 그 소행렬식 p13 = b ≠ 0
t = sp.symbols("t", real=True)
allok_form = True; allok_K = True; allok_metric = True
for _ in range(2):
    while True:
        Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
        if Z0[0, 1] != 0 and Z0.det() != 0:
            break
    av, bv, cv, dv = Z0[0, 0], Z0[0, 1], Z0[1, 0], Z0[1, 1]
    V = sp.Matrix.vstack(sp.eye(2), Z0)
    A13 = sp.Matrix([[1, 0], [av, bv]])            # 행 1,3
    Vp = Sm(V * A13.inv())
    Zp = sp.Matrix([[Vp[1, 0], Vp[1, 1]], [Vp[3, 0], Vp[3, 1]]])   # 행 2,4 가 새 좌표
    # 성분식: Z′ = [[−a/b, 1/b], [−detZ/b, d/b]]
    Zp_formula = sp.Matrix([[-av / bv, 1 / bv],
                            [-Z0.det() / bv, dv / bv]])
    if Sm(Zp - Zp_formula) != sp.zeros(2, 2):
        allok_form = False
    # p13 = 행{1,3} 소행렬식 = b
    p13 = V[[0, 2], :].det()
    if S(p13 - bv) != 0:
        allok_form = False
    # K′ = det(Vp† Vp) = K/|b|²  (게이지 det = 1/b)
    K0 = S((V.H * V).det())
    Kp = S((Vp.H * Vp).det())
    if S(Kp - K0 / (bv * sp.conjugate(bv))) != 0:
        allok_K = False
    # 계량 불변: 곡선 Z(t)=Z0+tW → 새 좌표 Z′(t), t=0 미분으로 접벡터 대응
    W = sp.Matrix(2, 2, lambda i_, j_: rC())
    Zt = Z0 + t * W
    Vt = sp.Matrix.vstack(sp.eye(2), Zt)
    A13t = sp.Matrix([[1, 0], [Zt[0, 0], Zt[0, 1]]])
    Vpt = Vt * A13t.inv()
    Zpt = sp.Matrix([[Vpt[1, 0], Vpt[1, 1]], [Vpt[3, 0], Vpt[3, 1]]])
    Wp = Sm(Zpt.diff(t).subs(t, 0))
    Zp0 = Sm(Zpt.subs(t, 0))
    F0 = sp.eye(2) + Z0.H * Z0; G0 = sp.eye(2) + Z0 * Z0.H
    Fp = sp.eye(2) + Zp0.H * Zp0; Gp = sp.eye(2) + Zp0 * Zp0.H
    t_old = S(sp.trace(F0.inv() * W.H * G0.inv() * W))
    t_new = S(sp.trace(Fp.inv() * Wp.H * Gp.inv() * Wp))
    if S(t_old - t_new) != 0:
        allok_metric = False
ok("X7a. Z′ = [[−a/b, 1/b],[−detZ/b, d/b]],  전이 분모 = p₁₃ = b  (차트 유효 ⟺ 소행렬식≠0)",
   allok_form)
ok("X7b. K′ = K/|p₁₃|²  (같은 메커니즘, 게이지 det = 1/b)", allok_K)
ok("X7c. 혼합 차트에서도 계량 불변 (곡선 미분으로 접벡터 대응, 정확산술)", allok_metric)

print(flush=True)
print("=" * 74, flush=True)
print("PART X8 — 전역 그림: K_chart = Σ|p_ij|² / |p_chart|²", flush=True)
print("=" * 74, flush=True)
allok = True
for _ in range(2):
    while True:
        Z0 = sp.Matrix(2, 2, lambda i_, j_: rC())
        if Z0[0, 1] != 0 and Z0.det() != 0:
            break
    V = sp.Matrix.vstack(sp.eye(2), Z0)
    ps = {rows: V[list(rows), :].det() for rows in combinations(range(4), 2)}
    tot = S(sum(p * sp.conjugate(p) for p in ps.values()))
    # 차트 {1,2}: p12=1 → K = tot/|p12|²
    K12 = S((V.H * V).det())
    if S(K12 - tot / (ps[(0, 1)] * sp.conjugate(ps[(0, 1)]))) != 0:
        allok = False
    # 차트 {3,4}: K′ = tot/|p34|²  (p34 = det Z — X3 과 합치)
    Vp = Sm(V * Z0.inv())
    K34 = S((Vp.H * Vp).det())
    if S(K34 - tot / (ps[(2, 3)] * sp.conjugate(ps[(2, 3)]))) != 0:
        allok = False
    # 차트 {1,3}: K″ = tot/|p13|²
    A13 = sp.Matrix([[1, 0], [Z0[0, 0], Z0[0, 1]]])
    Vq = Sm(V * A13.inv())
    K13 = S((Vq.H * Vq).det())
    if S(K13 - tot / (ps[(0, 2)] * sp.conjugate(ps[(0, 2)]))) != 0:
        allok = False
ok("X8. 세 차트 모두 K_chart = Σ|p_ij|²/|p_chart|²  (코시–비네가 여섯 차트를 한 식으로)",
   allok)

print(flush=True)
print("=" * 74, flush=True)
print(f"결과: {_n[1]}/{_n[0]} 통과", flush=True)
print("=" * 74, flush=True)
