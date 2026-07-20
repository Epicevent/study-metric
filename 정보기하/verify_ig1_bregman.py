# -*- coding: utf-8 -*-
# verify_ig1_bregman.py — 강의노트(Dually Flat Geometry v2) §3.1 "Second derivative:
# Hessian metric" 의 전 주장 검산 + 문서 IG1이 추가로 세운 것들.
#
#   D(x,y) = B_F[x:y] = F(x) − F(y) − F_a(y)(x^a − y^a)
#   ① ∂_i D            = F_i(x) − F_i(y)
#   ② ∂_i ∂'_j D       = −F_ij(y)            (두 미분 순서 모두)
#   ③ g_ij = −∂_i∂'_j D|_Δ = F_ij(x)          (Hessian metric)
#
# 실행: python 정보기하/verify_ig1_bregman.py   (요구: pip install sympy)
import sympy as sp

PASS = TOTAL = 0


def check(label, ok):
    global PASS, TOTAL
    TOTAL += 1
    PASS += bool(ok)
    print(f"[{TOTAL:02d}] {label}: {'OK' if ok else 'FAIL'}")


n = 3
xs = sp.symbols(f'x1:{n+1}', real=True)
ys = sp.symbols(f'y1:{n+1}', real=True)
F = sp.Function('F')                       # 임의의 매끄러운 F — 특정 형태를 가정하지 않는다

Fx, Fy = F(*xs), F(*ys)
# F_a(y) = (∂F/∂x^a)(y).  F(*ys) 를 y^a 로 미분한 것과 같다 (안쪽 합성이 항등사상).
D = Fx - Fy - sum(sp.diff(Fy, ys[a]) * (xs[a] - ys[a]) for a in range(n))

print("=" * 70)
print("PART 1. 1계 도함수 — 두 슬롯")
print("=" * 70)
check("① ∂_i D = F_i(x) − F_i(y)   (모든 i)",
      all(sp.simplify(sp.diff(D, xs[i]) - (sp.diff(Fx, xs[i]) - sp.diff(Fy, ys[i]))) == 0
          for i in range(n)))
# 둘째 슬롯: −F_j(y) 와 +F_j(y) 가 상쇄되어 한 항만 남는다 (문서 IG1 §3의 교차검증)
check("보조 ∂'_j D = −F_aj(y)(x^a − y^a)   — 두 항이 상쇄된 결과",
      all(sp.simplify(sp.diff(D, ys[j]) +
                      sum(sp.diff(Fy, ys[a], ys[j]) * (xs[a] - ys[a]) for a in range(n))) == 0
          for j in range(n)))

diag = list(zip(ys, xs))
check("보조 D|_Δ = 0", sp.simplify(D.subs(diag)) == 0)
check("보조 ∂_i D|_Δ = 0  (대각이 임계점)",
      all(sp.simplify(sp.diff(D, xs[i]).subs(diag)) == 0 for i in range(n)))
check("보조 ∂'_j D|_Δ = 0  (같은 이유)",
      all(sp.simplify(sp.diff(D, ys[j]).subs(diag)) == 0 for j in range(n)))

print()
print("=" * 70)
print("PART 2. 혼합 2계 도함수 — 미분 순서를 바꿔 교차검증")
print("=" * 70)
ok_a = ok_b = True
for i in range(n):
    for j in range(n):
        tgt = -sp.diff(Fy, ys[i], ys[j])
        ok_a &= sp.simplify(sp.diff(D, xs[i], ys[j]) - tgt) == 0     # ∂_i 먼저
        ok_b &= sp.simplify(sp.diff(D, ys[j], xs[i]) - tgt) == 0     # ∂'_j 먼저
check(f"② ∂_i ∂'_j D = −F_ij(y)   (∂_i 먼저, {n*n}성분 전부)", ok_a)
check(f"② ∂'_j ∂_i D = −F_ij(y)   (∂'_j 먼저 — 상쇄 경로가 다르다)", ok_b)
check("참고 ∂_i∂_j D = F_ij(x) — y에 무관 ⟹ §3.2의 Γ_ij,k = 0",
      all(sp.simplify(sp.diff(D, xs[i], xs[j]) - sp.diff(Fx, xs[i], xs[j])) == 0
          for i in range(n) for j in range(n)))

print()
print("=" * 70)
print("PART 3. 대각 제한 — Hessian metric")
print("=" * 70)
check("③ g_ij = −∂_i∂'_j D|_Δ = F_ij(x)",
      all(sp.simplify((-sp.diff(D, xs[i], ys[j])).subs(diag) - sp.diff(Fx, xs[i], xs[j])) == 0
          for i in range(n) for j in range(n)))
check("③ g 대칭 (F_ij = F_ji)",
      all(sp.simplify(sp.diff(Fx, xs[i], xs[j]) - sp.diff(Fx, xs[j], xs[i])) == 0
          for i in range(n) for j in range(n)))

print()
print("=" * 70)
print("PART 4. 부호의 근거 — 왜 −∂∂'D 인가")
print("=" * 70)
u = sp.symbols(f'u1:{n+1}', real=True)
Fq = sum(ui**2 for ui in u) / 2                        # 볼록, Hessian = I
Dq = (Fq.subs(list(zip(u, xs))) - Fq.subs(list(zip(u, ys)))
      - sum(sp.diff(Fq, u[a]).subs(list(zip(u, ys))) * (xs[a] - ys[a]) for a in range(n)))
check("F=½|x|² 이면 D = ½|x−y|² ≥ 0 (Bregman이 실제로 divergence)",
      sp.simplify(Dq - sum((xs[a] - ys[a])**2 for a in range(n))/2) == 0)
check("같은 F에서 ∂_i∂'_j D = −I  (슬롯을 나눠 미분하면 음정치)",
      sp.Matrix(n, n, lambda i, j: sp.diff(Dq, xs[i], ys[j])) == -sp.eye(n))
check("따라서 −∂_i∂'_j D = I  (부호를 뒤집어야 계량)",
      sp.Matrix(n, n, lambda i, j: -sp.diff(Dq, xs[i], ys[j])) == sp.eye(n))
check("한편 ∂_i∂_j D = +I  (첫 슬롯만 두 번이면 부호가 안 뒤집힌다)",
      sp.Matrix(n, n, lambda i, j: sp.diff(Dq, xs[i], xs[j])) == sp.eye(n))

print()
print("=" * 70)
print("PART 5. 노트 §1의 ½ 규약과 일관성 — 그리고 §6.1 예고")
print("=" * 70)
# D[P_ξ : P_{ξ+dξ}] = ½ g_ij dξ^i dξ^j + O(‖dξ‖³) 가 g = −∂∂'D|_Δ 와 같은 g인가?
#
# 주의(sympy 함정): 미정의 Function 을 t로 미분하면 연쇄법칙이 내부 더미 심볼을 만들고,
# subs(t,0) 이 합성 인자 속 Derivative 안까지 닿지 않는다. 3차까지의 주장이므로
# **계수가 임의 기호인 일반 3차 다항식**으로 대체한다 — 임의의 매끄러운 F 는 3차까지
# 자기 테일러 다항식과 일치하므로 이 대체는 주장을 약화시키지 않는다.
t = sp.symbols('t', real=True)
vv = sp.symbols(f'v1:{n+1}', real=True)                 # 방향 Δ (이름 충돌 회피: d→v)
ws = sp.symbols(f'w1:{n+1}', real=True)                 # F의 변수


def generic_cubic(vars_):
    terms, coeffs = [], []
    k = 0
    for deg in range(0, 4):
        for mono in sp.itermonomials(vars_, deg, deg):
            c = sp.Symbol(f'c{k}')
            k += 1
            coeffs.append(c)
            terms.append(c * mono)
    return sp.expand(sum(terms))


Fp = generic_cubic(ws)                                   # 일반 3차 다항식
at = lambda pt: Fp.subs(list(zip(ws, pt)), simultaneous=True)
grad_at = lambda pt, a: sp.diff(Fp, ws[a]).subs(list(zip(ws, pt)), simultaneous=True)

Y = list(ys)
Yd = [ys[a] + t*vv[a] for a in range(n)]
D_fwd = sp.expand(at(Yd) - at(Y) - sum(grad_at(Y, a) * (t*vv[a]) for a in range(n)))
D_bwd = sp.expand(at(Y) - at(Yd) + sum(grad_at(Yd, a) * (t*vv[a]) for a in range(n)))

H = lambda a, b: sp.diff(Fp, ws[a], ws[b]).subs(list(zip(ws, Y)), simultaneous=True)
T = lambda a, b, c: sp.diff(Fp, ws[a], ws[b], ws[c]).subs(list(zip(ws, Y)), simultaneous=True)
quad = sum(H(a, b) * vv[a]*vv[b] for a in range(n) for b in range(n)) / 2
cubic = sum(T(a, b, c) * vv[a]*vv[b]*vv[c]
            for a in range(n) for b in range(n) for c in range(n)) / 6

taylor = lambda e, k: sp.expand(sp.diff(e, t, k).subs(t, 0) / sp.factorial(k))

check("0차·1차항은 0 (대각에서 값도 기울기도 0)",
      sp.simplify(taylor(D_fwd, 0)) == 0 and sp.simplify(taylor(D_fwd, 1)) == 0)
check("2차항 = ½·F_ab(y)Δ^aΔ^b  ⟹ 노트 §1의 ½ 규약과 같은 g",
      sp.simplify(taylor(D_fwd, 2) - quad) == 0)
check("역방향 B_F[y : y+Δ] 도 2차항이 같다 (§6.1: 2차는 방향을 잊는다)",
      sp.simplify(taylor(D_bwd, 2) - quad) == 0)
check("3차에서 갈라진다: 순방향 ⅙F_abcΔ³, 역방향 ⅓F_abcΔ³ (차이 ⅙F_abcΔ³)",
      sp.simplify(taylor(D_fwd, 3) - cubic) == 0
      and sp.simplify(taylor(D_bwd, 3) - 2*cubic) == 0)
check("일반 3차 다항식 자체의 검증: −∂_i∂'_j D|_Δ = F_ij  (같은 F로 ③ 재확인)",
      all(sp.simplify(
          (-sp.diff(sp.expand(at(list(xs)) - at(Y)
                              - sum(grad_at(Y, a)*(xs[a]-ys[a]) for a in range(n))),
                    xs[i], ys[j])).subs(list(zip(ys, xs)), simultaneous=True)
          - sp.diff(Fp, ws[i], ws[j]).subs(list(zip(ws, list(xs))), simultaneous=True)) == 0
          for i in range(n) for j in range(n)))

print()
print("=" * 70)
print("PART 6. 노트의 예 — F = 음의 엔트로피 ⟹ g = Fisher 계량")
print("=" * 70)
m = 3                                                  # outcomes 0..3, η는 m차원
eta = sp.symbols(f'e1:{m+1}', positive=True)
p0 = 1 - sum(eta)
phi = p0 * sp.log(p0) + sum(e * sp.log(e) for e in eta)          # §2.2의 φ(η)

# sympy는 p0 = 1−Σe 의 양수성을 모르므로 log(a/b) 로 합치지 않는다 → 분리형으로 비교
check("φ_i = log p_i − log p_0  ( = log(p_i/p_0), dual log-ratio 좌표)",
      all(sp.simplify(sp.diff(phi, eta[i]) - (sp.log(eta[i]) - sp.log(p0))) == 0
          for i in range(m)))

g_hess = sp.Matrix(m, m, lambda i, j: sp.simplify(sp.diff(phi, eta[i], eta[j])))
check("g_ij = φ_ij = δ_ij/p_i + 1/p_0",
      sp.simplify(g_hess - sp.Matrix(m, m, lambda i, j:
                                     (1/eta[i] if i == j else 0) + 1/p0)) == sp.zeros(m, m))

# Fisher 계량의 정의로 완전히 독립 계산: g_ij = Σ_a (1/p_a) ∂_i p_a ∂_j p_a
ps = [p0] + list(eta)
g_fisher = sp.Matrix(m, m, lambda i, j: sp.simplify(
    sum(sp.diff(pa, eta[i]) * sp.diff(pa, eta[j]) / pa for pa in ps)))
check("g(Hessian) == g(Fisher 정의로 독립 계산)",
      sp.simplify(g_hess - g_fisher) == sp.zeros(m, m))

check("구조: g = diag(1/p_i) + (1/p_0)·11ᵀ  (양정치 + rank-1 양반정치)",
      sp.simplify(g_hess - (sp.diag(*[1/e for e in eta]) + sp.ones(m, m)/p0)) == sp.zeros(m, m))

pt = {eta[0]: sp.Rational(1, 5), eta[1]: sp.Rational(1, 4), eta[2]: sp.Rational(1, 10)}
G = sp.Matrix(g_hess.subs(pt))
minors = [sp.simplify(G[:k, :k].det()) for k in range(1, m + 1)]
check("한 점에서 양정치 (실베스터: 선행 주소행렬식 전부 > 0)", all(mi > 0 for mi in minors))
print("     주소행렬식 =", minors, "≈", [float(mi) for mi in minors])

# Bregman divergence 가 실제로 KL 인가 (§2.2의 주장) — 한 점에서 수치 확인
q = {eta[0]: sp.Rational(1, 3), eta[1]: sp.Rational(1, 4), eta[2]: sp.Rational(1, 6)}
Bphi = (phi.subs(pt) - phi.subs(q)
        - sum(sp.diff(phi, eta[i]).subs(q) * (pt[eta[i]] - q[eta[i]]) for i in range(m)))
p_list = [1 - sum(pt.values())] + [pt[e] for e in eta]
q_list = [1 - sum(q.values())] + [q[e] for e in eta]
KL = sum(pa * sp.log(pa / qa) for pa, qa in zip(p_list, q_list))
check("B_φ[η(p) : η(q)] = D_KL[p : q]  (§2.2, 한 점에서)", sp.simplify(Bphi - KL) == 0)

print()
print("=" * 70)
print(f"결과: {PASS}/{TOTAL} 통과")
print("=" * 70)
