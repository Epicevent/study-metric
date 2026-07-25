# -*- coding: utf-8 -*-
"""Projector 노트 §9 검산 — 정규화가 남긴 U(2) 자유도는 올(fiber)이다.

실행: python verify_projector_u2_fiber.py   (요구: pip install sympy numpy)

CP¹의 e^{iθ}가 U(2)로 승격되는 것을 확인한다:
  수직 생성원 iψ → ṼX (X∈u(2)) · (1−P)(iψ)=0 → (1−P)(ṼX)=0 ·
  접속 iα=s*ds → Θ=Ṽ*dṼ∈u(2) · 절단교체 s*α↦s*α+dθ → Θ↦U*ΘU+U*dU ·
  det:U(2)→U(1) 이 게이지를 SU(2)(V₂→Σ⁹)와 S¹(Σ⁹→Gr, Boothby–Wang)로 가른다.

기호 검산이 싼 것은 sympy로, 나머지는 무작위점 수치로 확인한다
(수치 검산의 전례: verify6_plucker.py 의 Monte Carlo).
"""
import numpy as np
import sympy as s

checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append((label, ok))
    print(("PASS" if ok else "FAIL") + "  " + label)


rng = np.random.default_rng(21)


def sqrtm_pd(M):
    """에르미트 양정치의 제곱근 — 유니터리 대각화(스펙트럼 정리)로."""
    w, U = np.linalg.eigh(M)
    return U @ np.diag(np.sqrt(w)) @ U.conj().T


def rand_u2(scale=1.0):
    """무작위 (e^X, X),  X ∈ u(2) 반에르미트."""
    X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    X = (X - X.conj().T) / 2 * scale
    w, U = np.linalg.eigh(1j * X)
    return U @ np.diag(np.exp(-1j * w)) @ U.conj().T, X


def expm_u2(X, t=1.0):
    w, U = np.linalg.eigh(1j * X)
    return U @ np.diag(np.exp(-1j * w * t)) @ U.conj().T


def frame(Z):
    """V=(I;Z), polar 절단 Ṽ=VG^{-1/2}, projector P."""
    V = np.vstack([np.eye(2), Z])
    Vt = V @ np.linalg.inv(sqrtm_pd(V.conj().T @ V))
    return V, Vt, Vt @ Vt.conj().T


def minors(V):
    out = []
    for i in range(4):
        for j in range(i + 1, 4):
            out.append(V[i, 0] * V[j, 1] - V[j, 0] * V[i, 1])
    return np.array(out)


# ── 1. 수직 생성원 — (1−P)(iψ)=0 의 rank-2 판 ──────────────────────────
# 기호: (I−P)V = 0 이면 ṼX = VG^{-1/2}X 는 V의 열공간이라 자동으로 죽는다.
a, b, c, d = s.symbols("a b c d")
ab, bb, cb, db = s.symbols("abar bbar cbar dbar")
Zs = s.Matrix([[a, b], [c, d]])
Zbs = s.Matrix([[ab, bb], [cb, db]])
Vs = s.eye(2).col_join(Zs)
Vbs = s.eye(2).col_join(Zbs)
Gs = Vbs.T * Vs
Ps = s.simplify(Vs * Gs.inv() * Vbs.T)
check(
    "1 (I-P)V = 0 (기호) — 수직 생성원 ṼX 가 사영에 죽는 이유의 전부",
    s.simplify((s.eye(4) - Ps) * Vs) == s.zeros(4, 2),
)

ok = True
for _ in range(100):
    Z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    V, Vt, P = frame(Z)
    _, X = rand_u2()
    ok &= np.allclose((np.eye(4) - P) @ (Vt @ X), 0)
check("2 (1-P)(VtX) = 0, X in u(2) — 실 4차원 수직 (무작위 100점)", ok)

ok = True
for _ in range(50):
    Z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    V, Vt, P = frame(Z)
    _, X = rand_u2()
    for t in (0.3, 0.7, 1.1):
        V2 = Vt @ expm_u2(X, t)
        ok &= np.allclose(V2 @ V2.conj().T, P)
check("3 수직 곡선 Vt e^{tX} 위에서 P(t) = P — §0.1의 X0 R(t)가 이 곡선", ok)

check("4 dim u(2) = 4 = 12 - 8 — V2(C4)→Gr(2,4) 올 차원 (걸음 6c §3.2)", 4 == 12 - 8)

# ── 2. 절단 교체와 비가환 접속 Θ = Ṽ*dṼ ──────────────────────────────
h = 1e-6
ok_th = ok_dec = ok_dp = ok_gauge = True
for _ in range(60):
    Z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    dZ = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    V, Vt, P = frame(Z)
    V2, Vt2, P2 = frame(Z + h * dZ)
    dVt = (Vt2 - Vt) / h
    Th = Vt.conj().T @ dVt
    ok_th &= np.allclose(Th + Th.conj().T, 0, atol=1e-4)
    ok_dec &= np.allclose(dVt, Vt @ Th + (np.eye(4) - P) @ dVt, atol=1e-4)
    hor = (np.eye(4) - P) @ dVt
    ok_dp &= np.allclose((P2 - P) / h, hor @ Vt.conj().T + Vt @ hor.conj().T, atol=1e-3)
    U0, _ = rand_u2()
    _, X1 = rand_u2(0.5)
    Uh = U0 @ expm_u2(X1, h)
    Vp, Vp2 = Vt @ U0, Vt2 @ Uh
    Thp = Vp.conj().T @ ((Vp2 - Vp) / h)
    dU = (Uh - U0) / h
    ok_gauge &= np.allclose(Thp, U0.conj().T @ Th @ U0 + U0.conj().T @ dU, atol=1e-3)
check("5 Theta = Vt*dVt in u(2) 반에르미트 — iα = s*ds 의 비가환 일반화", ok_th)
check("6 dVt = Vt·Theta + (1-P)dVt — 수직+수평 분해", ok_dec)
check("7 dP = (수평)Vt* + Vt(수평)* — dP는 수평 성분만 먹는다", ok_dp)
check("8 절단교체 Vt→VtU: Theta ↦ U*ThetaU + U*dU — s*α↦s*α+dθ 의 비가환판", ok_gauge)

# ── 3. det: U(2)→U(1) — 세 다발의 합류 ───────────────────────────────
ok_det = ok_su = ok_ph = True
for _ in range(100):
    Z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    V, Vt, P = frame(Z)
    U, _ = rand_u2()
    ok_det &= np.allclose(minors(Vt @ U), np.linalg.det(U) * minors(Vt))
    Us = U / np.sqrt(np.linalg.det(U))
    ok_su &= np.allclose(minors(Vt @ Us), minors(Vt), atol=1e-10)
    th = rng.uniform(0, 2 * np.pi)
    ok_ph &= np.allclose(minors(Vt * np.exp(1j * th)), np.exp(2j * th) * minors(Vt))
check("9 p(VtU) = det(U)·p(Vt) — U(2) 게이지가 Plücker엔 위상 detU 로만", ok_det)
check("10 SU(2)는 Plücker 고정 (V2→Σ9, 실 3차원)", ok_su)
check("11 e^{iθ}I2 는 위상 e^{2iθ} (Σ9→Gr 의 S¹, 실 1차원; 3+1=4)", ok_ph)

passed = sum(ok for _, ok in checks)
print(f"\n{passed}/{len(checks)} checks passed")
if passed != len(checks):
    raise SystemExit(1)
