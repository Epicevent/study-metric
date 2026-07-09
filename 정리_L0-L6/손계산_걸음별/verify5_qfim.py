# -*- coding: utf-8 -*-
# verify5_qfim_gr24.py — 손노트(Notes_260704) 막힌 계산의 진단 + 완성 + Gr(2,4) 기술 검산
# 실행: python verify5_qfim_gr24.py
import sympy as sp

th1, th2 = sp.symbols('theta1 theta2', real=True, positive=True)
I = sp.I

def bra(a, b):
    """물리 convention: <a|b> = a^dagger b (오른쪽에 complex-linear)"""
    return sp.expand_complex((a.H * b)[0, 0])

def Q(psi, i, j, vars=(th1, th2)):
    """quantum geometric tensor Q_ij = <d_i psi|d_j psi> - <d_i psi|psi><psi|d_j psi>"""
    di, dj = psi.diff(vars[i]), psi.diff(vars[j])
    return sp.simplify(sp.expand_complex(bra(di, dj) - bra(di, psi) * bra(psi, dj)))

def H(psi, i, j, vars=(th1, th2)):
    return sp.simplify(4 * sp.re(Q(psi, i, j, vars)))

print("=" * 72)
print("PART 1. 손노트 라인 재현 — 어디까지 맞고 어디서 깨졌나")
print("=" * 72)
c = 1 + sp.cos(th2)

# 손노트 p2의 psi (제곱근 없는 정규화 그대로):
psi_his = sp.Matrix([c**2, c * sp.exp(I * th1)]) / (1 + c**2)
norm2_his = sp.simplify(sp.expand_complex(bra(psi_his, psi_his)))
print("[1a] 손노트 psi의 노름제곱 ||psi||^2 =", sp.simplify(norm2_his), " (1이어야 하는데 아님 → Assertion 1 위반)")
print("     theta2=pi/2 값:", norm2_his.subs(th2, sp.pi / 2))

# 손노트 p3의 d1 psi 라인 재현 (그의 입력 기준 미분은 맞았는가)
d1_claim = sp.Matrix([0, I * sp.exp(I * th1) * c]) / (1 + c**2)
print("[1b] 손노트 d1psi 라인 == 직접미분? ",
      sp.simplify(psi_his.diff(th1) - d1_claim) == sp.zeros(2, 1))

# 손노트 p3 마지막 d2 psi 라인 재현
d2_claim = sp.sin(th2) / (1 + c**2)**2 * sp.Matrix([-2 * c, (c**2 - 1) * sp.exp(I * th1)])
print("[1c] 손노트 d2psi 최종라인 == 직접미분? ",
      sp.simplify(sp.expand_complex(psi_his.diff(th2) - d2_claim)) == sp.zeros(2, 1))

# 손노트 p4의 H11 = 4(c^2 - c^4)/(1+c^2)^2 재현 + 부호 문제
# p4 중간줄: Re[(d1psi)* psi . psi* (d1psi)] = c^4/(1+c^2)^2 라고 적음 → 검증
reterm_his_claim = c**4 / (1 + c**2)**2
d1h = psi_his.diff(th1)
reterm_actual = sp.simplify(sp.expand_complex(bra(d1h, psi_his) * bra(psi_his, d1h)))
print("[1d-i] p4 중간줄 Re[(d1psi)*psi psi*(d1psi)]: 그의 값 c^4/(1+c^2)^2, 실제(그의 psi 기준) =",
      sp.simplify(reterm_actual), " → 같은가?", sp.simplify(reterm_actual - reterm_his_claim) == 0)
H11_his = H(psi_his, 0, 0)
H11_claim = sp.simplify(4 * (c**2 - c**4) / (1 + c**2)**2)
print("[1d-ii] 공식을 그의 psi에 그대로 적용한 H11 (닫힌형) =", sp.simplify(H11_his))
print("        손노트 p4 최종 H11 = 4(c^2-c^4)/(1+c^2)^2 과 같은가?",
      sp.simplify(H11_his - H11_claim) == 0)
print("        theta2=pi/3: 손노트 H11 =", float(H11_claim.subs(th2, sp.pi / 3)),
      " ← 음수 (H11 = 4Var >= 0, P082 위반)")
print("                     공식-on-his-psi H11 =", float(H11_his.subs(th2, sp.pi / 3)),
      " vs 올바른 sin^2(pi/3) =", float(sp.sin(sp.pi / 3)**2))

# 손노트 p5의 H12: Re = 0
H12_his = H(psi_his, 0, 1)
print("[1e] 그의 psi로도 H12 = 4 Re Q12 =", sp.simplify(H12_his), " (Re=0 결론 자체는 재현됨)")
print("     Im Q12 (그가 본 '복소부') =", sp.simplify(sp.im(Q(psi_his, 0, 1))))

# 진단 1: 입체사영 자체 — 남극에서 직선 긋기
print()
print("[1f] 남극 (0,0,-1)에서 p=(cos t1 sin t2, sin t1 sin t2, cos t2)를 지나는 직선의 z=0 교점:")
t = sp.symbols('t', real=True)
p3 = sp.cos(th2)
line = sp.Matrix([t * sp.cos(th1) * sp.sin(th2), t * sp.sin(th1) * sp.sin(th2), -1 + t * (p3 + 1)])
t_star = sp.solve(line[2], t)[0]
zeta = sp.simplify(line[0].subs(t, t_star) + I * line[1].subs(t, t_star))
print("     zeta =", zeta, "= e^{i th1} sin(th2)/(1+cos th2)")
print("     반각: sin/(1+cos) - tan(t2/2) =",
      sp.simplify(sp.sin(th2) / (1 + sp.cos(th2)) - sp.tan(th2 / 2)))
print("     → 손노트의 e^{i th1}/(1+cos th2) 에는 sin(th2) 인자가 빠져 있음 (북극이 1/2로 감)")

print()
print("=" * 72)
print("PART 2. 교정 계산 — z = tan(th2/2) e^{i th1}, psi = (1,z)/sqrt(1+|z|^2)")
print("=" * 72)
half = th2 / 2
S = 1 + sp.tan(half)**2
print("[2a] S = 1+|z|^2 = 1+tan^2 = sec^2 :", sp.simplify(S - 1 / sp.cos(half)**2) == 0)

psi = sp.Matrix([1, sp.tan(half) * sp.exp(I * th1)]) / sp.sqrt(S)
psi_simple = sp.Matrix([sp.cos(half), sp.sin(half) * sp.exp(I * th1)])
# 0<th2<pi 에서 cos(th2/2)>0 이므로 1/sqrt(S)=cos(th2/2); 제곱 일치 + 부호 양수로 확인
sq_ok = sp.simplify(1 / S - sp.cos(half)**2) == 0
num_ok = all(abs(complex(sp.N((psi - psi_simple)[k].subs({th1: 0.7, th2: v}))))
             < 1e-12 for k in range(2) for v in (0.3, 1.1, 2.9))
print("[2b] (1,z)/sqrt(S) == (cos(t2/2), e^{i t1} sin(t2/2)) ? 제곱일치:", sq_ok,
      ", 수치일치(3점):", num_ok)
psi = psi_simple
print("[2c] ||psi||^2 =", sp.simplify(sp.expand_complex(bra(psi, psi))))

d1, d2 = psi.diff(th1), psi.diff(th2)
print("[2d] d1 psi =", list(d1))
print("     d2 psi =", list(d2))
print("[2e] 내적들:")
print("     <d1|d1> =", sp.simplify(sp.expand_complex(bra(d1, d1))))
print("     <d1|psi> =", sp.simplify(sp.expand_complex(bra(d1, psi))))
print("     <d2|d2> =", sp.simplify(sp.expand_complex(bra(d2, d2))))
print("     <d2|psi> =", sp.simplify(sp.expand_complex(bra(d2, psi))))
print("     <d1|d2> =", sp.simplify(sp.expand_complex(bra(d1, d2))))

Hm = sp.Matrix(2, 2, lambda i, j: H(psi, i, j))
print("[2f] QFIM H =", Hm.tolist(), "  (= diag(sin^2 th2, 1))")
print("     H11 - sin^2(th2) =", sp.simplify(Hm[0, 0] - sp.sin(th2)**2))
Q12 = Q(psi, 0, 1)
print("[2g] Q12 =", Q12, " → Re=0 (H12=0), ImQ12 =", sp.im(Q12), "= -sin(th2)/4")
print("     FS 넓이형식 계수 sqrt(det(H/4)) =",
      sp.simplify(sp.sqrt(sp.det(Hm / 4))), " → |Im Q12| 와 동일 (복소부 = 넓이형식)")
print("     적분 int |ImQ12| dth1 dth2 =",
      sp.integrate(sp.integrate(sp.sin(th2) / 4, (th1, 0, 2 * sp.pi)), (th2, 0, sp.pi)),
      "= pi (반지름 1/2 구의 넓이)")

# Bloch 방식
n = sp.Matrix([sp.sin(th2) * sp.cos(th1), sp.sin(th2) * sp.sin(th1), sp.cos(th2)])
Hb = sp.Matrix(2, 2, lambda i, j: sp.simplify(
    n.diff([th1, th2][i]).dot(n.diff([th1, th2][j]))))
print("[2h] Bloch |dn|^2 방식 H =", Hb.tolist(), " → 일치:", sp.simplify(Hm - Hb) == sp.zeros(2, 2))

# projector 방식 2 tr(dP dP)
P = psi * psi.H
Hp = sp.Matrix(2, 2, lambda i, j: sp.simplify(sp.expand_complex(
    2 * sp.trace(P.diff([th1, th2][i]) * P.diff([th1, th2][j])))))
print("[2i] projector 2tr(dPdP) 방식 H =", Hp.tolist(), " → 일치:",
      sp.simplify(sp.expand_complex(Hm - Hp)) == sp.zeros(2, 2))

# affine 차트 검산: H = 4/S^2 |dz|^2  (P074, n=1)
x, y = sp.symbols('x y', real=True)
v = sp.Matrix([1, x + I * y])
K_ = sp.expand_complex(bra(v, v))
gFS = sp.simplify(sp.expand_complex(
    bra(v.diff(x), v.diff(x)) / K_ - bra(v.diff(x), v) * bra(v, v.diff(x)) / K_**2))
print("[2j] P074 공식 (실좌표 x방향): g_xx^FS =", gFS, " → 4g = 4/S^2  ('4/D^2') :",
      sp.simplify(gFS - 1 / (1 + x**2 + y**2)**2) == 0)

# 곡률: H를 계량으로 보고 K 계산 (직교 계량 Gauss 공식)
E, G = Hm[0, 0], Hm[1, 1]  # F=0, 좌표 (th1, th2)
K_gauss = sp.simplify(-1 / (2 * sp.sqrt(E * G)) * (
    sp.diff(sp.diff(E, th2) / sp.sqrt(E * G), th2) +
    sp.diff(sp.diff(G, th1) / sp.sqrt(E * G), th1)))
print("[2k] QFIM 계량의 Gauss 곡률 K =", K_gauss, " (단위구면 규격 K=1);  FS=H/4 → K=4")

# Berry connection/curvature 연결: A_i = i<psi|d_i psi>, F_12 = d1 A2 - d2 A1
A1 = sp.simplify(sp.expand_complex(I * bra(psi, d1)))
A2 = sp.simplify(sp.expand_complex(I * bra(psi, d2)))
F12 = sp.simplify(A2.diff(th1) - A1.diff(th2))
print("[2l] Berry: A1 =", A1, ", A2 =", A2, ", F12 = d1A2-d2A1 =", F12,
      " = 2*(-ImQ12) → dα = 2 dA_FS (p43 정규화 경고와 일치),  ∫F =",
      sp.integrate(sp.integrate(F12, (th1, 0, 2 * sp.pi)), (th2, 0, sp.pi)))

# Plücker 좌표 항등식 (Z=[[a,b],[c,d]]): ||p||^2 = 1+Σ|z|^2+|det Z|^2 = det(I+Z†Z), 그리고 quadric
a_, b_, c_, d_ = sp.symbols('a b c d')
Zs = sp.Matrix([[a_, b_], [c_, d_]])
p12, p13, p14, p23, p24, p34 = 1, b_, d_, -a_, -c_, a_ * d_ - b_ * c_
quadric = sp.simplify(p12 * p34 - p13 * p24 + p14 * p23)
detIZZ = sp.det(sp.eye(2) + Zs.H * Zs)
normp = 1 + sum(sp.Abs(t)**2 for t in (a_, b_, c_, d_)) + sp.Abs(a_ * d_ - b_ * c_)**2
print("[2m] Plücker quadric p12p34-p13p24+p14p23 =", quadric,
      ";  det(I+Z†Z) - (1+Σ|z|²+|detZ|²) =",
      sp.simplify(sp.expand_complex(detIZZ - normp)))

print()
print("=" * 72)
print("PART 3. Gr(2,4) — 기준집 Part H 규약 검산 (P086, P088, P089) + 닫힌형 + Plücker")
print("=" * 72)
import numpy as np
rng = np.random.default_rng(7)

def rc(m, n):
    return rng.standard_normal((m, n)) + 1j * rng.standard_normal((m, n))

Z0, W = rc(2, 2), rc(2, 2)   # 임의 기준점, 임의 접방향 (dZ = W dt)
I2 = np.eye(2)

def Pof(Z):
    Vt = np.vstack([I2, Z])
    return Vt @ np.linalg.inv(I2 + Z.conj().T @ Z) @ Vt.conj().T

# (a) 2 tr(P' P') — 수치미분
eps = 1e-6
Pdot = (Pof(Z0 + eps * W) - Pof(Z0 - eps * W)) / (2 * eps)
a = 2 * np.trace(Pdot @ Pdot).real
# (b) 닫힌형 4 Re tr[(I+Z*Z)^{-1} W* (I+ZZ*)^{-1} W]
b = 4 * np.trace(np.linalg.inv(I2 + Z0.conj().T @ Z0) @ W.conj().T
                 @ np.linalg.inv(I2 + Z0 @ Z0.conj().T) @ W).real
print("[3a] 2tr(dPdP) =", a)
print("[3b] 4Re tr[(I+Z*Z)^-1 dZ* (I+ZZ*)^-1 dZ] =", b, " → 상대오차:", abs(a - b) / abs(b))

# (c) Plücker(=2-fermion Slater) 순수상태의 QFIM (P074 공식, 정규화 전 벡터)
def pluecker(Z):
    Vt = np.vstack([I2, Z])
    idx = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    return np.array([Vt[i, 0] * Vt[j, 1] - Vt[j, 0] * Vt[i, 1] for i, j in idx])

pv = pluecker(Z0)
pdot = (pluecker(Z0 + eps * W) - pluecker(Z0 - eps * W)) / (2 * eps)
K0 = (pv.conj() @ pv).real
cval = 4 * ((pdot.conj() @ pdot).real / K0 - abs(pdot.conj() @ pv)**2 / K0**2)
print("[3c] Plücker 순수상태 QFIM (CP^5, P074) =", cval, " → (a)와 상대오차:", abs(a - cval) / abs(a))

# (d) Plücker 노름 = det Gram 검산
lhs = K0
rhs = np.linalg.det(I2 + Z0.conj().T @ Z0).real
print("[3d] ||v1^v2||^2 == det(I+Z*Z)?  ", lhs, "vs", rhs, " 상대오차:", abs(lhs - rhs) / abs(rhs))

# (e) 원점 접벡터 규약: Z=0, A=[[0,B*],[B,0]] → g(A,A)=4tr(B*B)=2tr(A^2)
B = rc(2, 2)
A = np.block([[np.zeros((2, 2)), B.conj().T], [B, np.zeros((2, 2))]])
lhsA = 2 * np.trace(A @ A).real
rhsA = 4 * np.trace(B.conj().T @ B).real
print("[3e] 원점: 2tr(A^2) =", lhsA, " vs 4tr(B*B) =", rhsA)
# 원점에서 dP/dt = A 인지: Z(t)=tB
Pdot0 = (Pof(eps * B) - Pof(-eps * B)) / (2 * eps)
print("     ||dP/dt|_0 - A|| =", np.linalg.norm(Pdot0 - A), " (P090)")

# (f) CP^1 = Gr(1,2) 환원 (P091): k=1, N=2 로 같은 코드
z0, w = complex(rc(1, 1)[0, 0]), complex(rc(1, 1)[0, 0])
def Pof1(z):
    v = np.array([[1], [z]])
    return v @ v.conj().T / (1 + abs(z)**2)
Pd1 = (Pof1(z0 + eps * w) - Pof1(z0 - eps * w)) / (2 * eps)
a1 = 2 * np.trace(Pd1 @ Pd1).real
b1 = 4 * (abs(w)**2 - 0) / (1 + abs(z0)**2)**2 * 1  # 4|dz|^2/S^2 의 실곡선 버전: 4 Re[wbar w]/S^2
b1 = 4 * (w.conjugate() * w).real / (1 + abs(z0)**2)**2
print("[3f] Gr(1,2): 2tr(dPdP) =", a1, " vs 4|dz|^2/S^2 =", b1)

# (g) 혼합상태 rho = P/2 의 SLD-QFIM 수치 (계수 확인용) — 무작위 3점
print("[3g] rho=P/2 SLD-QFIM 비율 F / [2tr(dPdP)] (무작위 3점):")
for trial in range(3):
    Zt, Wt = rc(2, 2), rc(2, 2)
    Pd = (Pof(Zt + eps * Wt) - Pof(Zt - eps * Wt)) / (2 * eps)
    at = 2 * np.trace(Pd @ Pd).real
    lam, U = np.linalg.eigh(Pof(Zt))
    Ld = U.conj().T @ (Pd / 2) @ U
    lam = lam / 2
    F = 0.0
    for i_ in range(4):
        for j_ in range(4):
            if lam[i_] + lam[j_] > 1e-12:
                F += 2 * abs(Ld[i_, j_])**2 / (lam[i_] + lam[j_])
    print("     trial", trial, ": F =", F, ", 비율 =", F / at)
