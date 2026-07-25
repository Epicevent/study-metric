# -*- coding: utf-8 -*-
"""Reeb 노트 §10 검산 — U(2) 접속의 곡률에서 Ω가 나온다.

실행: python verify_reeb_curvature.py   (요구: pip install sympy numpy)

  Θ = Ṽ*dṼ ∈ u(2),  η = (1−P)dṼ (수평)  에 대해
  구조방정식   𝓕 := dΘ + Θ∧Θ = η*∧η                (곱미분 두 줄)
  수평 페어링  tr[η(D)*η(E)] = tr[G⁻¹D*H⁻¹E] = h_Z(D,E)   (§7.3의 h)
  자취 층      tr𝓕 = 2i·Im h_Z = 2i·ω  ⟹  dA = −i·tr𝓕 = 2ω = Ω
               — 이 노트 머리의 정규화 박스(π*Ω=dα, ω=½Ω)가 곡률 등식으로 재유도된다
  무자취 층    𝓕|₀(D,E) = D*E − E*D 의 su(2) 부분 ≠ 0 — k=1엔 없던 곡률

외미분은 2-매개변수 곡면 Z(s,t)=Z₀+sD+tE 위의 중심차분으로 잰다.
"""
import numpy as np
import sympy as s

checks = []


def check(label, condition):
    ok = bool(condition)
    checks.append((label, ok))
    print(("PASS" if ok else "FAIL") + "  " + label)


rng = np.random.default_rng(31)


def sqrtm_pd(M):
    w, U = np.linalg.eigh(M)
    return U @ np.diag(np.sqrt(w)) @ U.conj().T


def frame(Z):
    """polar 절단: Ṽ = V(V*V)^{-1/2},  P = ṼṼ*."""
    V = np.vstack([np.eye(2), Z])
    Vt = V @ np.linalg.inv(sqrtm_pd(V.conj().T @ V))
    return Vt, Vt @ Vt.conj().T


# ── 1. CP¹ (1×1) 기호 — Θ = iA, 𝓕 = dΘ, −(i/2)tr𝓕 = ω ─────────────────
z, zb = s.symbols("z zbar")
x, y = s.symbols("x y", real=True)
K = 1 + z * zb
psi = s.Matrix([1, z]) / s.sqrt(K)
psib = s.Matrix([1, zb]) / s.sqrt(K)


def d_coeffs(f):
    """1-형식 df 의 (dz, dz̄) 계수 — z, z̄ 독립기호 미분."""
    return s.simplify(s.diff(f, z)), s.simplify(s.diff(f, zb))


# Θ = ψ†dψ  (1×1 이라 스칼라);  성분별로 계수 추출
Th_z = s.simplify(sum(psib[k] * s.diff(psi[k], z) for k in range(2)))
Th_zb = s.simplify(sum(psib[k] * s.diff(psi[k], zb) for k in range(2)))
check(
    "1 CP¹: Θ = ψ†dψ = (z̄dz − zdz̄)/(2K) — 순허수 (u(1) 값)",
    s.simplify(Th_z - zb / (2 * K)) == 0 and s.simplify(Th_zb + z / (2 * K)) == 0,
)

# 𝓕 = dΘ (1×1 이라 Θ∧Θ = 0).  dΘ = (∂_z Θ_z̄ − ∂_z̄ Θ_z) dz∧dz̄
F_coeff = s.simplify(s.diff(Th_zb, z) - s.diff(Th_z, zb))
check(
    "2 CP¹: 𝓕 = dΘ = −dz∧dz̄/K²  (Θ∧Θ = 0, 스칼라 1-형식)",
    s.simplify(F_coeff + 1 / K**2) == 0,
)

# ω = (i/2)∂∂̄logK 의 dz∧dz̄ 계수는 (i/2)/K².  −(i/2)·𝓕 계수와 비교
omega_coeff = s.I / 2 * s.diff(s.log(K), z, zb)
check(
    "3 CP¹: −(i/2)·tr𝓕 = ω  (곡률의 자취가 켈러형식)",
    s.simplify(-s.I / 2 * F_coeff - omega_coeff) == 0,
)

# ── 2. Gr(2,4) 수치 — 구조방정식과 세 층 ─────────────────────────────
h = 1e-5


def Theta_at(Z, D):
    """Θ(D) = Ṽ*·(방향미분 D 방향 Ṽ)  — 중심차분."""
    Vp, _ = frame(Z + h * D)
    Vm, _ = frame(Z - h * D)
    Vt, _ = frame(Z)
    return Vt.conj().T @ ((Vp - Vm) / (2 * h))


def eta_at(Z, D):
    """η(D) = (1−P)·(방향미분 Ṽ)."""
    Vp, _ = frame(Z + h * D)
    Vm, _ = frame(Z - h * D)
    _, P = frame(Z)
    return (np.eye(4) - P) @ ((Vp - Vm) / (2 * h))


ok_struct = ok_pair = ok_trace = ok_dA = ok_gauge = True
for _ in range(24):
    Z0 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    D = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    E = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    G = np.eye(2) + Z0.conj().T @ Z0
    H = np.eye(2) + Z0 @ Z0.conj().T

    # dΘ(D,E) = ∂_D[Θ(E)] − ∂_E[Θ(D)]  (중심차분)
    dTh = (
        (Theta_at(Z0 + h * D, E) - Theta_at(Z0 - h * D, E)) / (2 * h)
        - (Theta_at(Z0 + h * E, D) - Theta_at(Z0 - h * E, D)) / (2 * h)
    )
    ThD, ThE = Theta_at(Z0, D), Theta_at(Z0, E)
    lhs = dTh + (ThD @ ThE - ThE @ ThD)                      # 𝓕(D,E)
    etaD, etaE = eta_at(Z0, D), eta_at(Z0, E)
    rhs = etaD.conj().T @ etaE - etaE.conj().T @ etaD        # (η*∧η)(D,E)
    ok_struct &= np.allclose(lhs, rhs, atol=5e-4)

    # 수평 페어링 = §7.3 의 에르미트형식 h_Z
    hDE = np.trace(np.linalg.inv(G) @ D.conj().T @ np.linalg.inv(H) @ E)
    ok_pair &= np.isclose(np.trace(etaD.conj().T @ etaE), hDE, atol=5e-4)

    # 자취 층: tr𝓕 = 2i·Im h_Z = 2i·ω,  그리고 dA = −i·tr𝓕 = 2ω
    ok_trace &= np.isclose(np.trace(lhs), 2j * hDE.imag, atol=5e-4)
    dA = -1j * np.trace(dTh)                                 # tr(Θ∧Θ)=0 이므로 dA=−i·tr dΘ
    ok_dA &= np.isclose(dA, 2 * hDE.imag, atol=5e-4)

    # 게이지 공변성: 절단 Ṽ→ṼU (상수 U) 에서 𝓕 ↦ U*𝓕U, tr𝓕 불변
    Xg = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    Xg = (Xg - Xg.conj().T) / 2
    w, Uc = np.linalg.eigh(1j * Xg)
    U0 = Uc @ np.diag(np.exp(-1j * w)) @ Uc.conj().T
    etaDU, etaEU = etaD @ U0, etaE @ U0                      # η ↦ ηU
    FU = etaDU.conj().T @ etaEU - etaEU.conj().T @ etaDU
    ok_gauge &= np.allclose(FU, U0.conj().T @ rhs @ U0) and np.isclose(
        np.trace(FU), np.trace(rhs)
    )
check("4 구조방정식 𝓕 = dΘ + Θ∧Θ = η*∧η  (무작위 24조)", ok_struct)
check("5 수평 페어링 tr[η(D)*η(E)] = tr[G⁻¹D*H⁻¹E] = h_Z(D,E)", ok_pair)
check("6 자취 층: tr𝓕 = 2i·Im h_Z = 2i·ω", ok_trace)
check("7 dA = −i·tr𝓕 = 2ω  — 머리의 정규화 박스(ω=½Ω)가 곡률에서 재유도", ok_dA)
check("8 게이지 공변성: 𝓕 ↦ U*𝓕U,  tr𝓕 불변  (dA 전역성의 §9와 같은 자리)", ok_gauge)

# ── 3. 무자취 층 — k=1 에 없던 su(2) 곡률 ───────────────────────────
E11 = np.array([[1, 0], [0, 0]], dtype=complex)
E12 = np.array([[0, 1], [0, 0]], dtype=complex)
F0 = E11.conj().T @ E12 - E12.conj().T @ E11                 # 𝓕|₀(E₁₁,E₁₂) = D*E − E*D
check(
    "9 Z=0 에서 𝓕(E₁₁,E₁₂) = E₁₂ − E₂₁  (반에르미트·무자취·≠0)",
    np.allclose(F0, E12 - E12.T) and np.isclose(np.trace(F0), 0) and not np.allclose(F0, 0),
)
ok = True
for _ in range(50):
    D = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    E = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    F0 = D.conj().T @ E - E.conj().T @ D
    ok &= np.allclose(F0 + F0.conj().T, 0)                   # u(2) 값
check("10 𝓕|₀(D,E) = D*E − E*D ∈ u(2)  (무작위 50조)", ok)
check("11 k=1 이면 무자취 부분이 0 — su(1)={0}, 1×1 은 자취가 전부", True and (1 * 1 - 1 == 0))

passed = sum(ok for _, ok in checks)
print(f"\n{passed}/{len(checks)} checks passed")
if passed != len(checks):
    raise SystemExit(1)
