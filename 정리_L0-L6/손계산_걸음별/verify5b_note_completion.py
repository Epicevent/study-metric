# -*- coding: utf-8 -*-
"""verify5b — 손노트 완성본(5b_손노트완성본_CP1_QFIM.md)의 전 줄 검산.

노트(Notes_260704)의 결 그대로: 남극 입체사영 → ψ(θ1,θ2) → ∂ψ → 내적 5개
→ H11, H12, H22 → H = round 계량 = 제1기본형식 = z좌표 4/D².
마지막에 원본 노트의 파손 3줄(E1·E2·E3)을 그대로 두면 노트 4쪽의 식이
정확히 재현됨을 확인한다 (진단의 실측).
"""
import sympy as sp

t1, t2 = sp.symbols("theta1 theta2", real=True)
I = sp.I

def hermdot(a, b):
    """<a,b> = a† b (물리 규약: 첫 인자에 켤레)"""
    return sum(sp.conjugate(ai) * bi for ai, bi in zip(a, b))

def S(e):
    return sp.simplify(sp.expand_complex(sp.expand(e)))

ok = lambda name, cond: print(("[OK] " if cond else "[FAIL] ") + name)

# ---------------------------------------------------------------- [1] 입체사영
p = sp.Matrix([sp.sin(t2) * sp.cos(t1), sp.sin(t2) * sp.sin(t1), sp.cos(t2)])
Spole = sp.Matrix([0, 0, -1])
t = sp.symbols("t", real=True)
ell = Spole + t * (p - Spole)
tstar = sp.solve(sp.Eq(ell[2], 0), t)[0]
ok("[1a] t* = 1/(1+cos θ2)", sp.simplify(tstar - 1 / (1 + sp.cos(t2))) == 0)
xq, yq = [sp.simplify(c.subs(t, tstar)) for c in (ell[0], ell[1])]
z = sp.simplify(xq + I * yq)
z_half = sp.tan(t2 / 2) * sp.exp(I * t1)
# 반지름: sinθ2/(1+cosθ2) = tan(θ2/2)  (반각 항등식; θ2 = 2u 로 배각 전개)
u = sp.symbols("u", real=True)
radial = sp.simplify(
    sp.expand_trig(sp.sin(2 * u)) / (1 + sp.expand_trig(sp.cos(2 * u))) - sp.tan(u))
phase = S(z - sp.sin(t2) / (1 + sp.cos(t2)) * sp.exp(I * t1))
ok("[1b] z = sinθ2/(1+cosθ2) e^{iθ1} = tan(θ2/2) e^{iθ1}",
   radial == 0 and phase == 0)
# 원본 노트 E1: z_note = e^{iθ1}/(1+cosθ2)  (sinθ2 누락)
z_note = sp.exp(I * t1) / (1 + sp.cos(t2))
ok("[1c] E1 확인: 노트의 z는 sinθ2 배 빠져 있다 (z = sinθ2 · z_note)",
   S(z - sp.sin(t2) * z_note) == 0)

# ---------------------------------------------------------------- [2] ψ 와 정규화
D = 1 + sp.Abs(z_half) ** 2  # 1+|z|^2
Dsimp = sp.simplify(sp.expand_trig(1 + sp.tan(t2 / 2) ** 2))
ok("[2a] 1+|z|² = 1/cos²(θ2/2)",
   sp.simplify(Dsimp - 1 / sp.cos(t2 / 2) ** 2) == 0)
psi = sp.Matrix([sp.cos(t2 / 2), sp.exp(I * t1) * sp.sin(t2 / 2)])
# ψ = (1/√(1+|z|²)) (1, z)  와 성분 일치 (θ2 ∈ (0,π) 에서 cos(θ2/2)>0)
psi_from_z = sp.Matrix([1, z_half]) * sp.cos(t2 / 2)
ok("[2b] ψ = (1/√(1+|z|²))(1,z)ᵀ = (cos(θ2/2), e^{iθ1} sin(θ2/2))ᵀ",
   all(S(a - b) == 0 for a, b in zip(psi, psi_from_z)))
ok("[2c] ‖ψ‖² = 1  (E2 해소: Assertion 1)", S(hermdot(psi, psi) - 1) == 0)

# ---------------------------------------------------------------- [3] 도함수
d1, d2 = psi.diff(t1), psi.diff(t2)
d1_closed = sp.Matrix([0, I * sp.exp(I * t1) * sp.sin(t2 / 2)])
d2_closed = sp.Matrix([-sp.sin(t2 / 2) / 2, sp.exp(I * t1) * sp.cos(t2 / 2) / 2])
ok("[3a] ∂₁ψ = (0, i e^{iθ1} sin(θ2/2))ᵀ",
   all(S(a - b) == 0 for a, b in zip(d1, d1_closed)))
ok("[3b] ∂₂ψ = (−½sin(θ2/2), ½e^{iθ1} cos(θ2/2))ᵀ",
   all(S(a - b) == 0 for a, b in zip(d2, d2_closed)))

# ---------------------------------------------------------------- [4] 내적 5개
ips = {
    "⟨∂₁ψ,∂₁ψ⟩ = sin²(θ2/2)": (hermdot(d1, d1), sp.sin(t2 / 2) ** 2),
    "⟨ψ,∂₁ψ⟩ = i sin²(θ2/2)": (hermdot(psi, d1), I * sp.sin(t2 / 2) ** 2),
    "⟨∂₂ψ,∂₂ψ⟩ = 1/4": (hermdot(d2, d2), sp.Rational(1, 4)),
    "⟨ψ,∂₂ψ⟩ = 0": (hermdot(psi, d2), 0),
    "⟨∂₁ψ,∂₂ψ⟩ = −(i/4) sinθ2": (hermdot(d1, d2), -I * sp.sin(t2) / 4),
}
for name, (lhs, rhs) in ips.items():
    ok("[4] " + name, S(lhs - rhs) == 0)

# ---------------------------------------------------------------- [P] 사영을 눈으로
# 공식 이전의 관찰 사슬: 위상 사영 → Pauli 접공간 → trace = 유클리드 → H = |dn|²
sig = [sp.Matrix([[0, 1], [1, 0]]),
       sp.Matrix([[0, -I], [I, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]
Pmat = psi * psi.H
nvec = sp.Matrix([sp.simplify(sp.re(sp.trace(Pmat * s))) for s in sig])
ok("[P1] Bloch 좌표 n_a = Tr(Pσ_a) 가 정확히 Example 1의 구면점 p",
   sp.simplify(nvec - p) == sp.zeros(3, 1))

x1, x2, x3, y1, y2, y3 = sp.symbols("x1 x2 x3 y1 y2 y3", real=True)
X = x1 * sig[0] + x2 * sig[1] + x3 * sig[2]
Y = y1 * sig[0] + y2 * sig[1] + y3 * sig[2]
ok("[P2] 접공간 Σx_iσ_i 위의 trace 내적: Tr[(x·σ)(y·σ)] = 2 x·y  (계수 2 빼고 유클리드)",
   sp.simplify(sp.trace(X * Y) - 2 * (x1 * y1 + x2 * y2 + x3 * y3)) == 0)

dPs = [Pmat.diff(t1), Pmat.diff(t2)]
ok("[P3] ∂_iP = ½ (∂_i n⃗)·σ⃗  (I-성분 없음: 사영자의 접공간은 Σx_iσ_i 꼴)",
   all(sp.simplify(sp.expand_complex(
           dPs[i_] - sum((nvec.diff([t1, t2][i_])[a] * sig[a] for a in range(3)),
                         sp.zeros(2, 2)) / 2))
       == sp.zeros(2, 2) for i_ in range(2)))
ok("[P4] Tr(∂_iP ∂_jP) = ½ ∂_i n⃗·∂_j n⃗  (P2+P3 의 귀결)",
   all(sp.simplify(sp.trace(dPs[i_] * dPs[j_])
                   - sp.Rational(1, 2) * nvec.diff([t1, t2][i_]).dot(nvec.diff([t1, t2][j_])))
       == 0 for i_ in range(2) for j_ in range(2)))

# 위상 사영: dψ_⊥ = dψ − ψ⟨ψ,dψ⟩ = (1−P)dψ
d1p = sp.simplify(d1 - psi * hermdot(psi, d1))
d2p = sp.simplify(d2 - psi * hermdot(psi, d2))
d1p_closed = sp.Matrix([-I * sp.sin(t2 / 2) ** 2 * sp.cos(t2 / 2),
                        I * sp.exp(I * t1) * sp.sin(t2 / 2) * sp.cos(t2 / 2) ** 2])
ok("[P5a] (∂₁ψ)_⊥ = (−i sin²(θ2/2)cos(θ2/2),  i e^{iθ1} sin(θ2/2)cos²(θ2/2))ᵀ",
   all(S(a - b) == 0 for a, b in zip(d1p, d1p_closed)))
ok("[P5b] ⟨ψ,(∂₁ψ)_⊥⟩ = 0  (위상 성분이 정확히 제거됨)",
   S(hermdot(psi, d1p)) == 0)
ok("[P5c] (∂₂ψ)_⊥ = ∂₂ψ  (∂₂ψ 는 애초에 위상 성분이 없다)",
   all(S(a - b) == 0 for a, b in zip(d2p, d2)))
ok("[P5d] 4‖(∂₁ψ)_⊥‖² = sin²θ2  (공식 없이, 사영된 길이만으로 H11)",
   sp.simplify(4 * sp.re(S(hermdot(d1p, d1p))) - sp.sin(t2) ** 2) == 0)

def Qform(di, dj):
    return S(hermdot(di, dj) - hermdot(di, psi) * hermdot(psi, dj))

def zero_halfangle(e):
    """θ2 = 2u 로 통일해 배각을 전개한 뒤 0 판정 (반각·배각 혼재 식용)."""
    uu = sp.symbols("uu", real=True)
    return sp.simplify(sp.expand_trig(sp.expand(e.subs(t2, 2 * uu)))) == 0

ok("[P6] 항등식: ⟨(∂_iψ)_⊥,(∂_jψ)_⊥⟩ = ⟨∂_iψ,∂_jψ⟩−⟨∂_iψ,ψ⟩⟨ψ,∂_jψ⟩  (공식의 괄호 = 사영된 내적)",
   all(zero_halfangle(S(hermdot([d1p, d2p][i_], [d1p, d2p][j_])
                        - Qform([d1, d2][i_], [d1, d2][j_])))
       for i_ in range(2) for j_ in range(2)))
ok("[P7] H_ij = ∂_i n⃗·∂_j n⃗  (H = 진짜 유클리드 길이 |dn⃗|²)",
   all(sp.simplify(4 * sp.re(Qform([d1, d2][i_], [d1, d2][j_]))
                   - nvec.diff([t1, t2][i_]).dot(nvec.diff([t1, t2][j_])))
       == 0 for i_ in range(2) for j_ in range(2)))

# ---------------------------------------------------------------- [5] QGT 와 H
def Q(i_, j_):
    di = psi.diff([t1, t2][i_])
    dj = psi.diff([t1, t2][j_])
    return S(hermdot(di, dj) - hermdot(di, psi) * hermdot(psi, dj))

H = sp.Matrix(2, 2, lambda i_, j_: sp.simplify(4 * sp.re(Q(i_, j_))))
ok("[5a] H11 = sin²θ2", sp.simplify(H[0, 0] - sp.sin(t2) ** 2) == 0)
ok("[5b] H12 = H21 = 0", H[0, 1] == 0 and H[1, 0] == 0)
ok("[5c] H22 = 1", H[1, 1] == 1)
Q12 = Q(0, 1)
ok("[5d] Q12 = −(i/4) sinθ2 (순허수 — '여튼 복소부가 있기는 하다')",
   S(Q12 + I * sp.sin(t2) / 4) == 0)

# H11 = 4 Var(N),  N = diag(0,1) (∂₁ψ = iNψ 의 생성원)
N = sp.diag(0, 1)
var = S(hermdot(psi, N * N * psi) - hermdot(psi, N * psi) ** 2)
ok("[5e] ∂₁ψ = iNψ, N=diag(0,1)", all(S(a - b) == 0 for a, b in zip(d1, I * N * psi)))
ok("[5f] H11 = 4·Var_ψ(N) ≥ 0 (기준집 ⑤P082)", sp.simplify(4 * var - H[0, 0]) == 0)

# ---------------------------------------------------------------- [6] 세 검산
# (i) 제1기본형식: H_ij = ∂_i p · ∂_j p  (QFIM = ambient dot, ⑤P101)
Ifund = sp.Matrix(2, 2, lambda i_, j_: sp.simplify(
    p.diff([t1, t2][i_]).dot(p.diff([t1, t2][j_]))))
ok("[6a] H = (∂_i p·∂_j p)  — 단위구면 제1기본형식과 성분 일치",
   sp.simplify(H - Ifund) == sp.zeros(2, 2))

# (ii) z-좌표: round 4|dz|²/(1+|z|²)² 를 z=tan(θ2/2)e^{iθ1} 로 당기면 H
x_, y_ = sp.symbols("x y", real=True)
lam = 4 / (1 + x_ ** 2 + y_ ** 2) ** 2
zx = sp.tan(t2 / 2) * sp.cos(t1)
zy = sp.tan(t2 / 2) * sp.sin(t1)
J = sp.Matrix([[zx.diff(t1), zx.diff(t2)], [zy.diff(t1), zy.diff(t2)]])
G = sp.simplify((J.T * J * lam.subs({x_: zx, y_: zy})).applyfunc(sp.trigsimp))
ok("[6b] (4/D² round 계량의 pullback) = H — '4/D²가 세 방식 모두'",
   sp.simplify(G - H) == sp.zeros(2, 2))

# (iii) 2 Tr(dP dP) 방식: P = ψψ†
P = psi * psi.H
M1, M2 = P.diff(t1), P.diff(t2)
TrH = sp.Matrix(2, 2, lambda i_, j_: sp.simplify(sp.re(
    2 * sp.trace([M1, M2][i_] * [M1, M2][j_]))))
ok("[6c] 2Tr(∂_iP ∂_jP) = H  (사영자 방식)",
   sp.simplify(TrH - H) == sp.zeros(2, 2))

# ---------------------------------------------------------------- [7] 복소부의 정체
F12 = sp.simplify(-2 * sp.im(Q12))          # Berry curvature (규약 명시)
ok("[7a] F12 := −2 Im Q12 = ½ sinθ2", sp.simplify(F12 - sp.sin(t2) / 2) == 0)
# FS 넓이밀도: √det(H/4) = |sinθ2|/4 = sinθ2/4  (θ2∈(0,π) 에서 sinθ2>0)
ok("[7b] F = 2·dA_FS  (기준집 경고 dα = 2dA_FS 의 그 factor)",
   sp.simplify(F12 ** 2 - 4 * sp.det(H / 4)) == 0
   and all(float(F12.subs(t2, v)) > 0 for v in (0.3, 1.5, 2.8)))
total = sp.integrate(sp.integrate(F12, (t2, 0, sp.pi)), (t1, 0, 2 * sp.pi))
ok("[7c] ∫F = 2π  (c₁ = 1)", sp.simplify(total - 2 * sp.pi) == 0)

# ---------------------------------------------------------------- [8] 원본 재현 (E1·E2·E3)
c = sp.symbols("c", positive=True)  # c = 1+cosθ2
# E1+E2 상태의 노트 2쪽 ψ̃: (1/(1+1/c²))·(1, e^{iθ1}/c) = (c², c e^{iθ1})/(1+c²)
psit = sp.Matrix([c ** 2, c * sp.exp(I * t1)]) / (1 + c ** 2)
norm2 = S(hermdot(psit, psit))
ok("[8a] ‖ψ̃‖² = c²/(1+c²) ≠ 1  (E2의 증상)",
   sp.simplify(norm2 - c ** 2 / (1 + c ** 2)) == 0)
d1t = psit.diff(t1)
term1 = S(hermdot(d1t, d1t))                       # = c²/(1+c²)²   (노트 4쪽 첫 항)
term2 = S(sp.Abs(hermdot(d1t, psit)) ** 2)         # = c⁴/(1+c²)⁴   (올바른 둘째 항)
ok("[8b] 첫 항 = c²/(1+c²)²  (노트 4쪽과 일치)",
   sp.simplify(term1 - c ** 2 / (1 + c ** 2) ** 2) == 0)
ok("[8c] 둘째 항 = c⁴/(1+c²)⁴  (올바른 값)",
   sp.simplify(term2 - c ** 4 / (1 + c ** 2) ** 4) == 0)
H11_note = 4 * c ** 2 * (1 - c ** 2) / (1 + c ** 2) ** 2      # 노트 4쪽 마지막 줄
H11_E3 = 4 * (term1 - c ** 4 / (1 + c ** 2) ** 2)             # 분모 (1+c²)² 증발시킨 조립
ok("[8d] E3 재현: 둘째 항의 분모를 (1+c²)⁴→(1+c²)² 로 쓰면 노트 4쪽 식 그대로",
   sp.simplify(H11_E3 - H11_note) == 0)
H11_fixE3 = sp.simplify(4 * (term1 - term2))
ok("[8e] E3만 고쳐도 (E1·E2 때문에) sin²θ2 가 아니다",
   sp.simplify(H11_fixE3 - 4 * c ** 2 * ((1 + c ** 2) ** 2 - c ** 2) / (1 + c ** 2) ** 4) == 0
   and sp.simplify(H11_fixE3.subs(c, 1 + sp.cos(t2)) - sp.sin(t2) ** 2) != 0)
ok("[8f] 노트 4쪽 식은 c>1 (북반구 θ2<π/2) 에서 음수 — H=4Var≥0 모순",
   sp.simplify(H11_note.subs(c, sp.Rational(3, 2))) < 0)

# ---------------------------------------------------------------- [N] 한 점에서 숫자로
# θ1 = π/2, θ2 = π/3 : 모든 값이 정확한 분수·√3 으로 떨어지는 점.
pt = {t1: sp.pi / 2, t2: sp.pi / 3}
sub = lambda e: sp.nsimplify(sp.simplify(sp.expand_complex(sp.Matrix(e).subs(pt)
                             if hasattr(e, "__iter__") else sp.sympify(e).subs(pt))))
r3 = sp.sqrt(3)

zv = sp.simplify(z_half.subs(pt))
ok("[N1] z = i/√3  (|z| = 1/√3 ≈ 0.577;  노트의 z라면 (2/3)i, |z| = 0.667)",
   sp.simplify(zv - I / r3) == 0
   and sp.simplify(sp.Abs(z_note.subs(pt)) - sp.Rational(2, 3)) == 0)

psiv = sub(psi)
ok("[N2a] ψ = (√3/2, i/2),  ‖ψ‖² = 3/4 + 1/4 = 1",
   psiv == sp.Matrix([r3 / 2, I / 2]))
psitv = sub(psit.subs(c, sp.Rational(3, 2)))
ok("[N2b] 노트의 ψ̃ = (9/13, 6i/13),  ‖ψ̃‖² = 117/169 = 9/13 ≠ 1",
   psitv == sp.Matrix([sp.Rational(9, 13), sp.Rational(6, 13) * I])
   and S(hermdot(psitv, psitv)) == sp.Rational(9, 13))

d1v, d2v = sub(d1), sub(d2)
ok("[N3a] ∂₁ψ = (0, −1/2)", d1v == sp.Matrix([0, -sp.Rational(1, 2)]))
sv = S(hermdot(psiv, d1v))
ok("[N3b] ⟨ψ,∂₁ψ⟩ = i/4  (가짜 위상 성분의 크기)", sv == I / 4)
phase_vec = sp.expand(psiv * sv)
ok("[N3c] 위상 성분 벡터 ψ·(i/4) = (√3i/8, −1/8)",
   sp.simplify(phase_vec - sp.Matrix([r3 * I / 8, -sp.Rational(1, 8)])) == sp.zeros(2, 1))
d1pv = sub(d1p)
ok("[N3d] (∂₁ψ)_⊥ = (−√3i/8, −3/8)",
   sp.simplify(d1pv - sp.Matrix([-r3 * I / 8, -sp.Rational(3, 8)])) == sp.zeros(2, 1))

ok("[N4] 길이의 회계: ‖∂₁ψ‖² = 1/4 = (가짜 1/16) + (진짜 3/16);  4·(3/16) = 3/4 = sin²60°",
   S(hermdot(d1v, d1v)) == sp.Rational(1, 4)
   and S(sp.Abs(sv) ** 2) == sp.Rational(1, 16)
   and S(hermdot(d1pv, d1pv)) == sp.Rational(3, 16)
   and sp.simplify(sp.sin(sp.pi / 3) ** 2 - sp.Rational(3, 4)) == 0)

ok("[N5] Bloch 값: n⃗ = (0, √3/2, 1/2) = p(π/2, π/3)  (숫자로 되돌아옴)",
   sp.simplify(nvec.subs(pt) - sp.Matrix([0, r3 / 2, sp.Rational(1, 2)])) == sp.zeros(3, 1)
   and sp.simplify(p.subs(pt) - sp.Matrix([0, r3 / 2, sp.Rational(1, 2)])) == sp.zeros(3, 1))

tr11 = sp.simplify(sp.trace((dPs[0] * dPs[0]).subs(pt)))
dn1 = nvec.diff(t1).subs(pt)
ok("[N6] 같은 3/4 세 번: 4‖(∂₁ψ)_⊥‖² = 2Tr(∂₁P∂₁P) = |∂₁n⃗|² = 3/4",
   S(4 * hermdot(d1pv, d1pv)) == sp.Rational(3, 4)
   and sp.simplify(2 * tr11 - sp.Rational(3, 4)) == 0
   and sp.simplify(dn1.dot(dn1) - sp.Rational(3, 4)) == 0)

Q12v = S(Qform(d1, d2).subs(pt))
ok("[N7] Q12 = −√3i/8 (순허수 → H12 = 0),  F12 = −2ImQ12 = √3/4 = ½sin60°",
   Q12v == -r3 * I / 8 and sp.re(Q12v) == 0
   and sp.simplify(-2 * sp.im(Q12v) - r3 / 4) == 0)

ok("[N8] H22 값: ∂₂ψ = (−1/4, √3i/4) 는 위상 성분 0 → 4‖∂₂ψ‖² = 1 = |∂₂n⃗|²",
   d2v == sp.Matrix([-sp.Rational(1, 4), r3 * I / 4])
   and S(hermdot(psiv, d2v)) == 0
   and S(4 * hermdot(d2v, d2v)) == 1
   and sp.simplify(nvec.diff(t2).subs(pt).dot(nvec.diff(t2).subs(pt)) - 1) == 0)

ok("[N9] 노트 4쪽 식의 값: c = 3/2 에서 −180/169 ≈ −1.065 < 0  (참값 +3/4)",
   sp.simplify(H11_note.subs(c, sp.Rational(3, 2)) + sp.Rational(180, 169)) == 0)

print("\n모든 검산 통과 여부는 위 [OK]/[FAIL] 라인 참조.")
