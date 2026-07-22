# -*- coding: utf-8 -*-
"""Reeb_CP1에서_Gr24로.md의 계산 검산."""

import sympy as sp


I = sp.I
count = [0, 0]


def ok(name, cond):
    count[0] += 1
    passed = bool(cond)
    count[1] += int(passed)
    print(("[OK] " if passed else "[FAIL] ") + name, flush=True)


print("=" * 78)
print("PART A — 단위구면: alpha가 위상속도를 읽는가")
print("=" * 78)

# 일반 C^m 대신 m=6을 쓰면 CP1(m=2)은 앞 두 블록으로 제한된다.
xs = sp.symbols("x12 x13 x14 x23 x24 x34", real=True)
ys = sp.symbols("y12 y13 y14 y23 y24 y34", real=True)
coords = []
R = []
alpha = []
for x, y in zip(xs, ys):
    coords.extend([x, y])
    R.extend([-y, x])
    alpha.extend([-y, x])  # alpha=x dy-y dx의 (dx,dy) 계수

N = sum(x**2 + y**2 for x, y in zip(xs, ys))
alpha_R = sp.expand(sum(a * r for a, r in zip(alpha, R)))
ok("A1. alpha(R)=N", sp.simplify(alpha_R - N) == 0)

# d alpha의 반대칭 행렬과 i_R d alpha
W = sp.zeros(12, 12)
for i in range(12):
    for j in range(12):
        W[i, j] = sp.diff(alpha[j], coords[i]) - sp.diff(alpha[i], coords[j])

standard = sp.diag(*([sp.Matrix([[0, 2], [-2, 0]])] * 6))
ok("A2. d alpha=2 sum dx_I wedge dy_I", W == standard)

iota = sp.Matrix([
    sp.simplify(sum(R[i] * W[i, j] for i in range(12)))
    for j in range(12)
])
gradN = sp.Matrix([sp.diff(N, u) for u in coords])
ok("A3. i_R d alpha=-dN", sp.simplify(iota + gradN) == sp.zeros(12, 1))

# 한 복소성분에서 (i/2)(p dbarp-barp dp)=xdy-ydx
x, y = sp.symbols("x y", real=True)
p = x + I * y
pbar = x - I * y
dp = sp.Matrix([1, I])
dpbar = sp.Matrix([1, -I])
real_form = sp.simplify(I / 2 * (p * dpbar - pbar * dp))
ok("A4. 복소 alpha가 실좌표 (-y,x)를 준다", real_form == sp.Matrix([-y, x]))

# §0의 CP1 세 곡선: 먼저 사영에서 무엇이 보이지 않는지 확인
tau = sp.symbols("tau", real=True)
p0_cp1 = sp.Matrix([1, 0])
gamma1 = sp.Matrix([sp.exp(I * tau), 0])
gamma2 = sp.Matrix([sp.cos(tau), sp.sin(tau)])
gamma3 = sp.exp(2 * I * tau) * gamma2

# [u1:u2]=[v1:v2] iff u1 v2-u2 v1=0 (두 벡터가 0이 아닐 때)
projective_det_1 = sp.expand(
    gamma1[0] * p0_cp1[1] - gamma1[1] * p0_cp1[0]
)
ok("A5. gamma1(t)=(e^{it},0)는 CP1에서 [1:0]으로 고정",
   projective_det_1 == 0)

projective_det_23 = sp.simplify(
    gamma2[0] * gamma3[1] - gamma2[1] * gamma3[0]
)
ok("A6. gamma2와 e^{2it}gamma2는 CP1에서 같은 곡선",
   projective_det_23 == 0)

vel1 = sp.diff(gamma1, tau).subs(tau, 0)
vel2 = sp.diff(gamma2, tau).subs(tau, 0)
vel3 = sp.diff(gamma3, tau).subs(tau, 0)
alpha_at_p0 = lambda vel: sp.simplify(-I * (p0_cp1.T * vel)[0])
ok("A7. 세 속도를 alpha가 각각 1,0,2로 읽는다",
   alpha_at_p0(vel1) == 1
   and alpha_at_p0(vel2) == 0
   and alpha_at_p0(vel3) == 2)
ok("A8. gamma3'(0)=2ip0+gamma2'(0)",
   sp.simplify(vel3 - 2 * I * p0_cp1 - vel2) == sp.zeros(2, 1))

# §1.3: S^3로 올린 속도에서 alpha가 읽은 위상속도를 빼면 CP1 길이가 나온다.
u, v = sp.symbols("u v", real=True)
S_cp1 = 1 + x**2 + y**2
c_cp1 = x * u + y * v
b_cp1 = x * v - y * u
lift_norm_sq = (u**2 + v**2) / S_cp1 - c_cp1**2 / S_cp1**2
horizontal_norm_sq = sp.simplify(lift_norm_sq - b_cp1**2 / S_cp1**2)
cp1_metric_sq = (u**2 + v**2) / S_cp1**2
ok("A9. Reeb 속도를 뺀 S3 속도의 길이는 CP1 계량",
   sp.simplify(horizontal_norm_sq - cp1_metric_sq) == 0)

# X=(u,v), X^perp=(-v,u)에 dA=2 dx wedge dy/S^2를 넣은 값의 절반
half_dA_X_JX = sp.simplify(
    sp.Rational(1, 2) * 2 / S_cp1**2 * (u * u - v * (-v))
)
ok("A10. (1/2)dA(X,X^perp)가 같은 길이제곱을 준다",
   sp.simplify(half_dA_X_JX - cp1_metric_sq) == 0)

# §1.3의 숫자곡선 z(t)=1+it: alpha=1/2를 빼면 남은 길이제곱은 1/4
s0_numeric = sp.Matrix([1, 1]) / sp.sqrt(2)
sdot_numeric = sp.Matrix([0, I]) / sp.sqrt(2)
R_numeric = I * s0_numeric
phase_numeric = sp.simplify(-I * (sp.conjugate(s0_numeric).T * sdot_numeric)[0])
h_numeric = sp.simplify(sdot_numeric - phase_numeric * R_numeric)
h_norm_numeric = sp.simplify((sp.conjugate(h_numeric).T * h_numeric)[0])
ok("A11. z(t)=1+it에서 alpha=1/2, 남은 속도 길이제곱=1/4",
   phase_numeric == sp.Rational(1, 2)
   and h_norm_numeric == sp.Rational(1, 4))


print()
print("=" * 78)
print("PART B — Plucker cone과 Sigma^9")
print("=" * 78)

a, b, c, d = sp.symbols("a b c d")
ab, bb, cb, db = sp.symbols("abar bbar cbar dbar")
Delta = a * d - b * c
Deltab = ab * db - bb * cb
q = sp.Matrix([1, c, d, -a, -b, Delta])
qb = sp.Matrix([1, cb, db, -ab, -bb, Deltab])

Fq = sp.expand(q[0] * q[5] - q[1] * q[4] + q[2] * q[3])
ok("B1. q=(1,c,d,-a,-b,ad-bc)는 Klein 관계를 만족", Fq == 0)

Ksum = sp.expand((qb.T * q)[0])
Z = sp.Matrix([[a, c], [b, d]])
Zdag = sp.Matrix([[ab, bb], [cb, db]])
Kdet = sp.expand((sp.eye(2) + Zdag * Z).det())
ok("B2. ||q||^2=det(I+Z^dagger Z)", sp.simplify(Ksum - Kdet) == 0)

# 숫자점 (a,b,c,d)=(1,0,0,i)
num = {a: 1, b: 0, c: 0, d: I, ab: 1, bb: 0, cb: 0, db: -I}
qnum = q.subs(num) / 2
qbnum = qb.subs(num) / 2
Fnum = sp.simplify(qnum[0] * qnum[5] - qnum[1] * qnum[4] + qnum[2] * qnum[3])
Nnum = sp.simplify((qbnum.T * qnum)[0])
ok("B3. 숫자점 p=(1,0,i,-1,0,i)/2: F=0, N=1", Fnum == 0 and Nnum == 1)

# F(lambda p)=lambda^2 F(p)
lam = sp.symbols("lambda")
pvars = sp.symbols("p12 p13 p14 p23 p24 p34")
F = pvars[0] * pvars[5] - pvars[1] * pvars[4] + pvars[2] * pvars[3]
Flam = sp.expand((lam * pvars[0]) * (lam * pvars[5])
                 - (lam * pvars[1]) * (lam * pvars[4])
                 + (lam * pvars[2]) * (lam * pvars[3]))
ok("B4. Klein 식은 2차 동차", sp.simplify(Flam - lam**2 * F) == 0)

dF_ip = sp.expand(sum(sp.diff(F, pj) * I * pj for pj in pvars))
ok("B5. dF_p(ip)=2iF(p)", sp.simplify(dF_ip - 2 * I * F) == 0)

# 본문의 한 변수 평면 a=t, b=c=d=0
t = sp.symbols("t", real=True)
pcurve = sp.Matrix([1, 0, 0, -t, 0, 0]) / sp.sqrt(1 + t**2)
dpcurve = sp.diff(pcurve, t)
expected_dpcurve = sp.Matrix([-t, 0, 0, -1, 0, 0]) / (1 + t**2) ** sp.Rational(3, 2)
ok("B6. a=t 곡선의 단위 Plucker 벡터 미분",
   sp.simplify(dpcurve - expected_dpcurve) == sp.zeros(6, 1))
ok("B7. a=t 곡선에서 p^dagger p'=0",
   sp.simplify((pcurve.T * dpcurve)[0]) == 0)

# a,b,c,d가 동시에 움직일 때 연쇄법칙으로 얻는 q의 속도
adot, bdot, cdot, ddot = sp.symbols("adot bdot cdot ddot")
velocity = sp.Matrix([adot, bdot, cdot, ddot])
qdot = q.jacobian((a, b, c, d)) * velocity
expected_qdot = sp.Matrix([
    0, cdot, ddot, -adot, -bdot,
    adot * d + a * ddot - bdot * c - b * cdot,
])
F_along_q = sp.expand(
    qdot[0] * q[5] + q[0] * qdot[5]
    - qdot[1] * q[4] - q[1] * qdot[4]
    + qdot[2] * q[3] + q[2] * qdot[3]
)
ok("B8. 일반 곡선 q(t)의 연쇄법칙과 dF/dt=0",
   sp.simplify(qdot - expected_qdot) == sp.zeros(6, 1) and F_along_q == 0)


print()
print("=" * 78)
print("PART C — Sigma^9의 Reeb 조건과 p0의 접촉성")
print("=" * 78)

pt_real = {
    xs[0]: sp.Rational(1, 2), ys[0]: 0,
    xs[1]: 0, ys[1]: 0,
    xs[2]: 0, ys[2]: sp.Rational(1, 2),
    xs[3]: -sp.Rational(1, 2), ys[3]: 0,
    xs[4]: 0, ys[4]: 0,
    xs[5]: 0, ys[5]: sp.Rational(1, 2),
}
Rnum_real = sp.Matrix(R).subs(pt_real)
expected_R = sp.Matrix([
    0, sp.Rational(1, 2), 0, 0,
    -sp.Rational(1, 2), 0, 0, -sp.Rational(1, 2),
    0, 0, -sp.Rational(1, 2), 0,
])
ok("C1. 숫자점의 Reeb 성분", Rnum_real == expected_R)
ok("C2. 숫자점에서 alpha(R)=1", sp.simplify(alpha_R.subs(pt_real)) == 1)
ok("C3. 숫자점에서 dN(R)=0", sp.simplify((gradN.T.subs(pt_real) * Rnum_real)[0]) == 0)

# p0=e12의 horizontal 8x8 위 d alpha
horizontal_indices = list(range(2, 10))  # 13,14,23,24의 x,y
Wh = W.extract(horizontal_indices, horizontal_indices)
ok("C4. p0의 ker(alpha) 위 det(d alpha)=2^8", Wh.det() == 2**8)
ok("C5. alpha wedge (d alpha)^4 계수=384", 2**4 * sp.factorial(4) == 384)


print()
print("=" * 78)
print("PART D — U(2): SU(2)는 사라지고 determinant만 Reeb로 남는가")
print("=" * 78)

v = sp.Matrix(sp.symbols("v1:5"))
w = sp.Matrix(sp.symbols("w1:5"))
g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
vp = g11 * v + g21 * w
wp = g12 * v + g22 * w
detG = g11 * g22 - g12 * g21

minor_checks = []
for i in range(4):
    for j in range(i + 1, 4):
        old = v[i] * w[j] - v[j] * w[i]
        new = sp.expand(vp[i] * wp[j] - vp[j] * wp[i])
        minor_checks.append(sp.simplify(new - detG * old) == 0)
ok("D1. Q->QG이면 여섯 Plucker 성분 모두 det(G)배", all(minor_checks))

A1 = sp.Matrix([[0, 1], [-1, 0]])
A2 = sp.Matrix([[0, I], [I, 0]])
A3 = sp.Matrix([[I, 0], [0, -I]])
A0 = I * sp.eye(2) / 2
ok("D2. su(2)의 세 생성원은 trace 0", all(A.trace() == 0 for A in (A1, A2, A3)))
ok("D3. -i tr(iI/2)=1", sp.simplify(-I * A0.trace()) == 1)

theta = sp.symbols("theta", real=True)
Gsu = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
ok("D4. 실수 회전 기저곡선의 determinant는 1", sp.simplify(Gsu.det() - 1) == 0)
Gsu_imag = sp.Matrix([
    [sp.cos(theta), I * sp.sin(theta)],
    [I * sp.sin(theta), sp.cos(theta)],
])
ok("D5. i가 섞인 기저곡선의 determinant는 1",
   sp.simplify(Gsu_imag.det() - 1) == 0)
Gopposite = sp.diag(sp.exp(I * theta), sp.exp(-I * theta))
ok("D6. 반대 위상 기저곡선의 determinant는 1",
   sp.simplify(Gopposite.det() - 1) == 0)
Ghalf = sp.exp(I * theta / 2) * sp.eye(2)
ok("D7. 절반 공통위상은 Plucker 위상 e^{it}를 만든다",
   sp.simplify(Ghalf.det() - sp.exp(I * theta)) == 0)
ok("D8. 공통 frame 위상은 wedge 위상을 두 배로 만든다",
   sp.simplify((sp.exp(I * theta) * sp.eye(2)).det() - sp.exp(2 * I * theta)) == 0)

# §5의 비교곡선: v를 e3 방향으로 움직이면 새 p23 성분이 생겨 평면이 변한다.
plane_curve = sp.Matrix([
    sp.cos(theta), 0, 0, -sp.sin(theta), 0, 0
])
plane_velocity = sp.diff(plane_curve, theta).subs(theta, 0)
p0_plucker = plane_curve.subs(theta, 0)
ok("D9. e3 방향 비교곡선은 위상이 아닌 새 p23 방향으로 움직인다",
   plane_velocity == sp.Matrix([0, 0, 0, -1, 0, 0])
   and all(sp.simplify(plane_velocity[j] - I * p0_plucker[j]) != 0
           for j in [0, 3]))

# 임의의 u(2) 속도는 trace 한 방향과 traceless 세 방향으로 갈린다.
r0, r1, zx, zy = sp.symbols("r0 r1 zx zy", real=True)
zeta_u2 = zx + I * zy
A_general = sp.Matrix([
    [I * r0, zeta_u2],
    [-sp.conjugate(zeta_u2), I * r1],
])
A_center = sp.simplify(A_general.trace() / 2) * sp.eye(2)
A_traceless = sp.simplify(A_general - A_center)
ok("D10. u(2) 속도는 중앙 1방향과 trace 0인 3방향으로 분해",
   sp.simplify(A_general.conjugate().T + A_general) == sp.zeros(2)
   and sp.simplify(A_traceless.trace()) == 0
   and sp.simplify(A_center + A_traceless - A_general) == sp.zeros(2))


print()
print("=" * 78)
print("PART E — local section, connection, curvature, chart transition")
print("=" * 78)

us = (a, b, c, d)
ubs = (ab, bb, cb, db)
expected_Ku = sp.Matrix([
    ab + d * Deltab,
    bb - c * Deltab,
    cb - b * Deltab,
    db + a * Deltab,
])
actual_Ku = sp.Matrix([sp.diff(Ksum, u) for u in us])
ok("E1. K_a,K_b,K_c,K_d 네 식", sp.simplify(actual_Ku - expected_Ku) == sp.zeros(4, 1))

r = sp.Matrix([d, -c, -b, a])
rb = sp.Matrix([db, -cb, -bb, ab])
actual_Kuv = sp.Matrix(4, 4, lambda i, j: sp.diff(Ksum, us[i], ubs[j]))
expected_Kuv = sp.eye(4) + r * rb.T
ok("E2. K_{u,bar v}=I+r r^dagger", sp.simplify(actual_Kuv - expected_Kuv) == sp.zeros(4, 4))

g = sp.Matrix(4, 4, lambda i, j:
              sp.factor((Ksum * actual_Kuv[i, j]
                         - actual_Ku[i] * sp.diff(Ksum, ubs[j])) / Ksum**2))
origin = {a: 0, b: 0, c: 0, d: 0, ab: 0, bb: 0, cb: 0, db: 0}
ok("E3. g_{u,bar v}(0)=delta_uv", g.subs(origin) == sp.eye(4))

# CP1 slice
z, zb = sp.symbols("z zbar")
Kcp = 1 + z * zb
gcp = sp.simplify(sp.diff(sp.log(Kcp), z, zb))
ok("E4. CP1 slice curvature coefficient=1/(1+|z|^2)^2",
   sp.simplify(gcp - 1 / Kcp**2) == 0)

# diagonal slice a=z,d=w,b=c=0
wvar, wb = sp.symbols("w wbar")
Kdiag = sp.expand(Ksum.subs({
    a: z, ab: zb, d: wvar, db: wb,
    b: 0, bb: 0, c: 0, cb: 0,
}))
ok("E5. diagonal slice K=(1+|z|^2)(1+|w|^2)",
   sp.simplify(Kdiag - (1 + z * zb) * (1 + wvar * wb)) == 0)

actual_num = sp.Matrix([
    -sp.diff(Kdiag, z), sp.diff(Kdiag, zb),
    -sp.diff(Kdiag, wvar), sp.diff(Kdiag, wb),
])
expected_num = sp.Matrix([
    -(1 + wvar * wb) * zb,
    (1 + wvar * wb) * z,
    -(1 + z * zb) * wb,
    (1 + z * zb) * wvar,
])
ok("E6. diagonal slice A 분자가 두 CP1 분자로 인수분해",
   sp.simplify(actual_num - expected_num) == sp.zeros(4, 1))

ok("E7. dA와 걸음6 omega의 계수비는 2", sp.simplify(I / (I / 2) - 2) == 0)

# a=r e^{it} 원에서 A와 dA를 직접 계산
rad = sp.symbols("r", nonnegative=True, real=True)
scircle = sp.Matrix([
    1, 0, 0, -rad * sp.exp(I * theta), 0, 0,
]) / sp.sqrt(1 + rad**2)
scircle_bar = sp.conjugate(scircle)
A_circle = sp.simplify(-I * (scircle_bar.T * sp.diff(scircle, theta))[0])
ok("E8. a=r e^{it} 원에서 A_t=r^2/(1+r^2)",
   sp.simplify(A_circle - rad**2 / (1 + rad**2)) == 0)
ok("E9. 원판에서 dA의 dr wedge dt 계수",
   sp.simplify(sp.diff(A_circle, rad) - 2 * rad / (1 + rad**2)**2) == 0)

# P=(a,c)=(1,1)을 지나는 같은/반대 복소직선
zeta, zetab = sp.symbols("zeta zetabar")
Kplus = 3 + 2 * zeta + 2 * zetab + 2 * zeta * zetab
Kminus = 3 + 2 * zeta * zetab
def mixed_log_at_zero(expr):
    first = sp.diff(expr, zeta)
    second = sp.diff(expr, zetab)
    mixed = sp.diff(expr, zeta, zetab)
    return sp.simplify(
        ((expr * mixed - first * second) / expr**2).subs({zeta: 0, zetab: 0})
    )

hplus = mixed_log_at_zero(Kplus)
hminus = mixed_log_at_zero(Kminus)
ok("E10. 같은 방향 L_+의 mixed Hessian은 2/9", hplus == sp.Rational(2, 9))
ok("E11. 반대 방향 L_-의 mixed Hessian은 2/3", hminus == sp.Rational(2, 3))

point_ac = {a: 1, b: 0, c: 1, d: 0, ab: 1, bb: 0, cb: 1, db: 0}
block_ac = g.extract([0, 2], [0, 2]).subs(point_ac)
expected_block_ac = sp.Matrix([[2, -1], [-1, 2]]) / 9
plus_dir = sp.Matrix([1, 1])
minus_dir = sp.Matrix([1, -1])
ok("E12. P의 (a,c) Hessian 블록이 두 직선 값을 함께 재현",
   block_ac == expected_block_ac
   and (plus_dir.T * block_ac * plus_dir)[0] == hplus
   and (minus_dir.T * block_ac * minus_dir)[0] == hminus)

# chart transition c=1+i인 한 점
chart_num = {
    a: 1, b: 1 - I, c: 1 + I, d: 2,
    ab: 1, bb: 1 + I, cb: 1 - I, db: 2,
}
q12 = q.subs(chart_num)
K12 = sp.simplify((qb.T * q).subs(chart_num)[0])
cnum = 1 + I
q13 = q12 / cnum
K13 = sp.simplify(K12 / (cnum * sp.conjugate(cnum)))
s12 = q12 / sp.sqrt(K12)
s13 = q13 / sp.sqrt(K13)
transition = sp.Abs(cnum) / cnum
ok("E13. overlap에서 s13=(|c|/c)s12",
   sp.simplify(s13 - transition * s12) == sp.zeros(6, 1))

# c=e^{it}인 겹침 곡선에서 A12=dt/2, A13=-dt/2
s12_curve = sp.Matrix([1, sp.exp(I * theta), 0, 0, 0, 0]) / sp.sqrt(2)
s13_curve = sp.Matrix([sp.exp(-I * theta), 1, 0, 0, 0, 0]) / sp.sqrt(2)
A12_curve = sp.simplify(
    -I * (sp.conjugate(s12_curve).T * sp.diff(s12_curve, theta))[0]
)
A13_curve = sp.simplify(
    -I * (sp.conjugate(s13_curve).T * sp.diff(s13_curve, theta))[0]
)
ok("E14. c=e^{it}에서 A13-A12=-dt",
   A12_curve == sp.Rational(1, 2)
   and A13_curve == -sp.Rational(1, 2)
   and A13_curve - A12_curve == -1)

print()
print("=" * 78)
print(f"결과: {count[1]}/{count[0]} 통과")
print("=" * 78)
if count[0] != count[1]:
    raise SystemExit(1)
