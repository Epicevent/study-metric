# -*- coding: utf-8 -*-
"""비례좌표 한 줄에서 시작하여 — 사영공간의 두 계산선 검산.

실행:
    python verify_projective_counting_hrr.py
"""
from math import comb

import sympy as sp

H, k, z, t = sp.symbols("H k z t")
checks = []


def check(name, actual, expected):
    """정확산술로 두 식이 같은지 검사한다."""
    ok = sp.simplify(actual - expected) == 0
    checks.append((name, sp.simplify(actual), sp.simplify(expected), ok))
    if not ok:
        raise AssertionError(f"{name}: got {actual}, expected {expected}")


def truncate(expr, degree):
    # ASSERTION: P^n에서는 H^(n+1)=0; 급수는 H^n까지만 남긴다.
    return sp.series(expr, H, 0, degree + 1).removeO().expand()


# 1. dual metric chart change
Ki, a = sp.symbols("Ki a", positive=True)
Kj = Ki / a**2
hj = 1 / Kj
check("dual metric chart change", hj, a**2 / Ki)

# 2. tensor power logarithm
h = sp.symbols("h", positive=True)
check("log tensor metric", sp.expand_log(sp.log(h**k), force=True), k * sp.log(h))

# 3. P1 tangent transition
w = sp.symbols("w", nonzero=True)
check("dz/dw=-w^-2", sp.diff(1 / w, w), -w**-2)

# 4--7. rank-one determinant lemma:
# det(KI-uv^T)=K^n(1-v^Tu/K), K=1+v^Tu.
rho = sp.symbols("rho")
for n in range(1, 5):
    Kdet = 1 + rho
    det_G = sp.simplify(Kdet**n * (1 - rho / Kdet) / Kdet ** (2 * n))
    check(f"det G n={n}", det_G, Kdet ** (-(n + 1)))

# 8--12. u=r^2, t=u/(1+u) 뒤의 beta integral.
for n in range(1, 6):
    radial = sp.Rational(1, 2) * sp.beta(n, 1)
    check(f"radial n={n}", sp.simplify(radial), sp.Rational(1, 2 * n))

# 13--16. sphere area와 H^n 적분 정규화.
for n in range(1, 5):
    sphere = 2 * sp.pi**n / sp.factorial(n - 1)
    integral = sp.factorial(n) / sp.pi**n * sphere * sp.Rational(1, 2 * n)
    check(f"integral H^n n={n}", integral, 1)

# 17--20. P1: 1,z,...,z^k.
for kk in range(4):
    check(f"P1 count k={kk}", kk + 1, comb(kk + 1, 1))

# 21--24. P2: a+b <= k인 격자점.
for kk in range(4):
    lattice_count = sum(kk - a0 + 1 for a0 in range(kk + 1))
    check(f"P2 count k={kk}", lattice_count, comb(kk + 2, 2))

# 25--28. P3: a0+a1+a2+a3=k인 네쌍 전수조사.
for kk in range(4):
    brute = sum(
        1
        for a0 in range(kk + 1)
        for a1 in range(kk + 1)
        for a2 in range(kk + 1)
        for a3 in range(kk + 1)
        if a0 + a1 + a2 + a3 == kk
    )
    check(f"P3 count k={kk}", brute, comb(kk + 3, 3))

# 29. 한 line의 Todd factor.
Q = sp.series(H / (1 - sp.exp(-H)), H, 0, 6).removeO().expand()
check("Todd factor expansion", Q, 1 + H / 2 + H**2 / 12 - H**4 / 720)

# 30--32. Euler sequence에서 나오는 P1,P2,P3 Todd class.
td1 = truncate(Q**2, 1)
td2 = truncate(Q**3, 2)
td3 = truncate(Q**4, 3)
check("Td P1", td1, 1 + H)
check("Td P2", td2, 1 + sp.Rational(3, 2) * H + H**2)
check("Td P3", td3, 1 + 2 * H + sp.Rational(11, 6) * H**2 + H**3)

# 33--35. e^(kH)Td(TP^n)의 top coefficient.
ch1 = truncate(sp.exp(k * H), 1)
ch2 = truncate(sp.exp(k * H), 2)
ch3 = truncate(sp.exp(k * H), 3)
check("HRR P1", sp.expand(ch1 * td1).coeff(H, 1), k + 1)
check("HRR P2", sp.expand(ch2 * td2).coeff(H, 2), (k + 1) * (k + 2) / 2)
check("HRR P3", sp.expand(ch3 * td3).coeff(H, 3), (k + 1) * (k + 2) * (k + 3) / 6)

# 36--40. residue 치환 뒤 [z^n](1-z)^(-k-1).
for n in range(1, 6):
    coefficient = sp.series((1 - z) ** (-k - 1), z, 0, n + 1).removeO().expand().coeff(z, n)
    polynomial = sp.prod(k + j for j in range(1, n + 1)) / sp.factorial(n)
    check(f"residue n={n}", coefficient, polynomial)

# 41--42. generating function과 stars-and-bars 표본.
hilbert_p2 = sp.series((1 - t) ** -3, t, 0, 6).removeO().expand()
check("Hilbert P2 k=5", hilbert_p2.coeff(t, 5), comb(7, 2))
check("stars bars n=4 k=5", comb(9, 4), 126)

# 43--48. 음수 k에서 top cohomology가 지표를 메운다.
check("P1 h1 k=-2", -(-2) - 1, 1)
check("P1 h1 k=-5", -(-5) - 1, 4)
check("P1 chi k=-5", 0 - (-(-5) - 1), -4)
check("P2 top h2 k=-3", comb(2, 2), 1)
check("P2 top h2 k=-5", comb(4, 2), 6)
n, kk = 4, -7
chi_polynomial = sp.prod(kk + j for j in range(1, n + 1)) / sp.factorial(n)
top_cohomology_with_sign = (-1) ** n * comb(-kk - 1, n)
check("negative identity n=4 k=-7", chi_polynomial, top_cohomology_with_sign)

print(f"검산 완료: {len(checks)}/{len(checks)}")
for name, actual, _, _ in checks:
    print(f"  OK  {name}: {actual}")
