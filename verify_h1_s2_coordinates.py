"""Independent symbolic checks for H1_S2_쌩좌표계산.md."""

from __future__ import annotations

import sympy as sp


x, y, u, v, t = sp.symbols("x y u v t", real=True)
r2 = x**2 + y**2
rho2 = u**2 + v**2

checks: list[tuple[str, bool]] = []


def record(name: str, condition: object) -> None:
    checks.append((name, bool(condition)))


# §0: stereographic transition w=1/z.
u_of_xy = x / r2
v_of_xy = -y / r2
record(
    "transition sends sigma_infinity to sigma_0: X",
    sp.simplify(
        (2 * u_of_xy / (1 + u_of_xy**2 + v_of_xy**2))
        - 2 * x / (1 + r2)
    )
    == 0,
)
record(
    "transition sends sigma_infinity to sigma_0: Y",
    sp.simplify(
        (-2 * v_of_xy / (1 + u_of_xy**2 + v_of_xy**2))
        - 2 * y / (1 + r2)
    )
    == 0,
)
record(
    "transition sends sigma_infinity to sigma_0: Z",
    sp.simplify(
        (1 - u_of_xy**2 - v_of_xy**2)
        / (1 + u_of_xy**2 + v_of_xy**2)
        - (r2 - 1) / (1 + r2)
    )
    == 0,
)
record("transition radius inversion", sp.simplify(u_of_xy**2 + v_of_xy**2 - 1 / r2) == 0)

ux = sp.diff(u_of_xy, x)
uy = sp.diff(u_of_xy, y)
vx = sp.diff(v_of_xy, x)
vy = sp.diff(v_of_xy, y)
record("u_x", sp.simplify(ux - (y**2 - x**2) / r2**2) == 0)
record("u_y", sp.simplify(uy + 2 * x * y / r2**2) == 0)
record("v_x", sp.simplify(vx - 2 * x * y / r2**2) == 0)
record("v_y", sp.simplify(vy - (y**2 - x**2) / r2**2) == 0)
record("transition Jacobian nonzero", sp.simplify(ux * vy - uy * vx - 1 / r2**2) == 0)

# §1: height form and the two reconstructed primitives.
H0 = (r2 - 1) / (1 + r2)
P0 = 4 * x / (1 + r2) ** 2
Q0 = 4 * y / (1 + r2) ** 2
record("height x derivative", sp.simplify(sp.diff(H0, x) - P0) == 0)
record("height y derivative", sp.simplify(sp.diff(H0, y) - Q0) == 0)
record("height form closed", sp.simplify(sp.diff(Q0, x) - sp.diff(P0, y)) == 0)

F0 = 2 * r2 / (1 + r2)
record("first primitive x derivative", sp.simplify(sp.diff(F0, x) - P0) == 0)
record("first primitive y derivative", sp.simplify(sp.diff(F0, y) - Q0) == 0)
record("first primitive shift", sp.simplify(F0 - H0 - 1) == 0)

Hinf = (1 - rho2) / (1 + rho2)
Ainf = -4 * u / (1 + rho2) ** 2
Binf = -4 * v / (1 + rho2) ** 2
Finf = -2 * rho2 / (1 + rho2)
record("north height u derivative", sp.simplify(sp.diff(Hinf, u) - Ainf) == 0)
record("north height v derivative", sp.simplify(sp.diff(Hinf, v) - Binf) == 0)
record("second primitive u derivative", sp.simplify(sp.diff(Finf, u) - Ainf) == 0)
record("second primitive v derivative", sp.simplify(sp.diff(Finf, v) - Binf) == 0)
record("second primitive shift", sp.simplify(Finf - Hinf + 1) == 0)

Finf_on_z = sp.simplify(Finf.subs({u: u_of_xy, v: v_of_xy}))
record("overlap primitive difference", sp.simplify(F0 - Finf_on_z - 2) == 0)
record("overlap difference x derivative", sp.simplify(sp.diff(F0 - Finf_on_z, x)) == 0)
record("overlap difference y derivative", sp.simplify(sp.diff(F0 - Finf_on_z, y)) == 0)

# Verify that the north-chart height form transforms into the south-chart one.
A_on_z = Ainf.subs({u: u_of_xy, v: v_of_xy})
B_on_z = Binf.subs({u: u_of_xy, v: v_of_xy})
record("1-form transition dx coefficient", sp.simplify(A_on_z * ux + B_on_z * vx - P0) == 0)
record("1-form transition dy coefficient", sp.simplify(A_on_z * uy + B_on_z * vy - Q0) == 0)

# §6: dtheta is closed but has nonzero circular integral.
eta_P = -y / r2
eta_Q = x / r2
record("dtheta closed off origin", sp.simplify(sp.diff(eta_Q, x) - sp.diff(eta_P, y)) == 0)

circle_pullback = sp.simplify(
    eta_P.subs({x: sp.cos(t), y: sp.sin(t)}) * sp.diff(sp.cos(t), t)
    + eta_Q.subs({x: sp.cos(t), y: sp.sin(t)}) * sp.diff(sp.sin(t), t)
)
record("dtheta circle pullback", circle_pullback == 1)
record("dtheta circle integral", sp.integrate(circle_pullback, (t, 0, 2 * sp.pi)) == 2 * sp.pi)

# Direct target in w-coordinates; its coefficients have pole order one at rho=0.
eta_w_A = v / rho2
eta_w_B = -u / rho2
x_of_uv = u / rho2
y_of_uv = -v / rho2
eta_P_on_w = eta_P.subs({x: x_of_uv, y: y_of_uv}, simultaneous=True)
eta_Q_on_w = eta_Q.subs({x: x_of_uv, y: y_of_uv}, simultaneous=True)
record(
    "dtheta transition du coefficient",
    sp.simplify(
        eta_P_on_w * sp.diff(x_of_uv, u)
        + eta_Q_on_w * sp.diff(y_of_uv, u)
        - eta_w_A
    )
    == 0,
)
record(
    "dtheta transition dv coefficient",
    sp.simplify(
        eta_P_on_w * sp.diff(x_of_uv, v)
        + eta_Q_on_w * sp.diff(y_of_uv, v)
        - eta_w_B
    )
    == 0,
)
record(
    "dtheta north expression singular",
    sp.limit(eta_w_B.subs(v, 0), u, 0, dir="+") == -sp.oo,
)

# §9 exercise 1.
P_ex = 2 * x * y + 1
Q_ex = x**2
F_ex = x + x**2 * y
record("exercise closed", sp.diff(Q_ex, x) == sp.diff(P_ex, y))
record("exercise primitive x derivative", sp.diff(F_ex, x) == P_ex)
record("exercise primitive y derivative", sp.diff(F_ex, y) == Q_ex)

failed = [name for name, ok in checks if not ok]
for index, (name, ok) in enumerate(checks, start=1):
    print(f"[{index:02d}] {'PASS' if ok else 'FAIL'}  {name}")

if failed:
    raise SystemExit(f"{len(failed)} failed: {', '.join(failed)}")

print(f"\n{len(checks)}/{len(checks)} checks passed.")
