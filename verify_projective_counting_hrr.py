# -*- coding: utf-8 -*-
"""사영공간의 두 계산선 검산.

왼쪽: homogeneous monomial / stars-and-bars 카운팅.
오른쪽: Td(TP^n)=Q(H)^(n+1)와 HRR의 H^n 계수.

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
    checks.append((name, actual, expected, ok))
    if not ok:
        raise AssertionError(f"{name}: got {actual}, expected {expected}")


def truncate(expr, degree):
    # ASSERTION: P^n에서는 H^(n+1)=0; 급수는 H^n까지만 남긴다.
    return sp.series(expr, H, 0, degree + 1).removeO().expand()


# 1--4. P^1: 1,z,...,z^k.
for kk in range(4):
    check(f"P1 count k={kk}", kk + 1, comb(kk + 1, 1))

# 5--8. P^2: a+b <= k인 격자점.
for kk in range(4):
    lattice_count = sum(kk - a + 1 for a in range(kk + 1))
    check(f"P2 count k={kk}", lattice_count, comb(kk + 2, 2))

# 9--12. P^3: a0+a1+a2+a3=k인 네쌍을 직접 전수조사.
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

# 13. 한 line의 Todd factor.
Q = sp.series(H / (1 - sp.exp(-H)), H, 0, 6).removeO().expand()
check("Bernoulli expansion", Q, 1 + H / 2 + H**2 / 12 - H**4 / 720)

# 14--16. Euler sequence에서 나오는 P^1, P^2, P^3의 Todd class.
td1 = truncate(Q**2, 1)
td2 = truncate(Q**3, 2)
td3 = truncate(Q**4, 3)
check("Td P1", td1, 1 + H)
check("Td P2", td2, 1 + sp.Rational(3, 2) * H + H**2)
check("Td P3", td3, 1 + 2 * H + sp.Rational(11, 6) * H**2 + H**3)

# 17--19. e^(kH)Td(TP^n)의 top coefficient.
ch1 = truncate(sp.exp(k * H), 1)
ch2 = truncate(sp.exp(k * H), 2)
ch3 = truncate(sp.exp(k * H), 3)
check("HRR P1", sp.expand(ch1 * td1).coeff(H, 1), k + 1)
check("HRR P2", sp.expand(ch2 * td2).coeff(H, 2), (k + 1) * (k + 2) / 2)
check("HRR P3", sp.expand(ch3 * td3).coeff(H, 3), (k + 1) * (k + 2) * (k + 3) / 6)

# 20--21. 일반 stars-and-bars와 Hilbert series의 표본.
check("stars bars n=4 k=5", comb(9, 4), 126)
hilbert_p2 = sp.series((1 - t) ** -3, t, 0, 6).removeO().expand()
check("Hilbert series P2 k=5", hilbert_p2.coeff(t, 5), comb(7, 2))

# 22--24. residue 치환 뒤 [z^n](1-z)^(-k-1).
for n in (1, 2, 3):
    coefficient = sp.series((1 - z) ** (-k - 1), z, 0, n + 1).removeO().expand().coeff(z, n)
    polynomial = sp.prod(k + j for j in range(1, n + 1)) / sp.factorial(n)
    check(f"residue n={n}", coefficient, polynomial)

# 25--30. 음수 k에서 h^0와 chi가 갈라지고 top cohomology가 메운다.
check("P1 chi k=-2", -2 + 1, -1)
check("P1 h1 k=-2", -(-2) - 1, 1)
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
