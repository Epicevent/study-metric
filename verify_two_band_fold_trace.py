#!/usr/bin/env python3
"""Independent checks for the two-band fold/sheet calculation note.

The script intentionally keeps three routes separate:
1. winding/flux warm-ups independent of the two-band root solver;
2. closed-form meridian roots;
3. a seed-grid Newton solve near one cusp;
4. midpoint quadrature on the whole Brillouin torus.

Requires only NumPy.  It does not use any value copied from the note as an
input to the root solver or the global integral.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


PI = math.pi
SQRT3 = math.sqrt(3.0)
QC = -np.ones(3, dtype=float) / SQRT3
EA = np.array([1.0, 1.0, -2.0]) / math.sqrt(6.0)
EB = np.array([1.0, -1.0, 0.0]) / math.sqrt(2.0)


def wrap(k: np.ndarray) -> np.ndarray:
    """Wrap a point componentwise to [-pi, pi)."""

    return (k + PI) % (2.0 * PI) - PI


def d_vector(kx: float, ky: float) -> np.ndarray:
    return np.array(
        [math.sin(kx), math.sin(ky), 1.0 - math.cos(kx) - math.cos(ky)],
        dtype=float,
    )


def lower_bloch(kx: float, ky: float) -> np.ndarray:
    """Bloch vector n of P=(I+n.sigma)/2 for the lower band: n=-d/|d|."""

    d = d_vector(kx, ky)
    return -d / np.linalg.norm(d)


def north_oriented_chart(n: np.ndarray) -> np.ndarray:
    """Orientation-preserving stereographic chart centered at the north pole."""

    return np.array([n[0], n[1]]) / (1.0 + n[2])


def south_oriented_chart(n: np.ndarray) -> np.ndarray:
    """Orientation-preserving stereographic chart centered at the south pole."""

    return np.array([n[0], -n[1]]) / (1.0 - n[2])


def n_numerator(kx: float, ky: float) -> float:
    cx, cy = math.cos(kx), math.cos(ky)
    return cx + cy - cx * cy


def signed_density(kx: float, ky: float) -> float:
    n0 = n_numerator(kx, ky)
    return n0 / (2.0 * (3.0 - 2.0 * n0) ** 1.5)


def check_actual_torus_patches(h: float = 1e-6) -> dict[str, object]:
    """Check the two actual T^2 -> S^2 patches inserted in W5."""

    cases = (
        {
            "patch": "U_plus",
            "center": np.array([0.0, 0.0]),
            "chart": north_oriented_chart,
            "expected_jacobian": np.diag([-0.5, -0.5]),
            "expected_density": 0.5,
        },
        {
            "patch": "U_minus",
            "center": np.array([PI, PI]),
            "chart": south_oriented_chart,
            "expected_jacobian": np.diag([1.0 / 6.0, -1.0 / 6.0]),
            "expected_density": -1.0 / 18.0,
        },
    )
    rows = []
    for case in cases:
        center = case["center"]
        chart = case["chart"]
        columns = []
        for axis in range(2):
            step = np.zeros(2)
            step[axis] = h
            forward = chart(lower_bloch(*(center + step)))
            backward = chart(lower_bloch(*(center - step)))
            columns.append((forward - backward) / (2.0 * h))
        jacobian = np.column_stack(columns)
        expected_jacobian = case["expected_jacobian"]
        assert float(np.max(np.abs(jacobian - expected_jacobian))) < 2e-10
        determinant = float(np.linalg.det(jacobian))
        pulled_back_density = 2.0 * determinant  # w(center)=0
        expected_density = float(case["expected_density"])
        assert abs(pulled_back_density - expected_density) < 2e-10
        assert abs(signed_density(*center) - expected_density) < 1e-15
        rows.append(
            {
                "patch": case["patch"],
                "center": center.tolist(),
                "chart_jacobian": jacobian.tolist(),
                "determinant": determinant,
                "half_minus_laplacian_at_chart_origin": 2.0,
                "pullback_density": pulled_back_density,
                "global_formula_density": signed_density(*center),
            }
        )

    # The explicitly chosen pi/6 squares really land in the asserted open
    # hemispheres; sample their closure slightly inside the boundary.
    q = np.linspace(-PI / 6.0 + 1e-6, PI / 6.0 - 1e-6, 41)
    plus_n3 = [lower_bloch(x, y)[2] for x in q for y in q]
    minus_n3 = [lower_bloch(PI + x, PI + y)[2] for x in q for y in q]
    assert min(plus_n3) > 0.0
    assert max(minus_n3) < 0.0
    return {
        "rows": rows,
        "U_plus_min_n3": float(min(plus_n3)),
        "U_minus_max_n3": float(max(minus_n3)),
    }


def check_winding_warmups(samples: int = 16384) -> dict[str, object]:
    """Independently check W1, W3, W6, and the diagonal W7 values."""

    # W1: pull back (-Y dX + X dY)/(X^2+Y^2) to circles of
    # several radii and winding numbers.  Midpoint quadrature is used rather
    # than inserting the already simplified integral 2*pi*m.
    t = (np.arange(samples) + 0.5) * (2.0 * PI / samples)
    dt = 2.0 * PI / samples
    winding_rows = []
    for radius, winding in ((0.3, -3), (2.0, -1), (1.0, 1), (4.5, 2), (0.8, 5)):
        x = radius * np.cos(winding * t)
        y = radius * np.sin(winding * t)
        dxdt = -radius * winding * np.sin(winding * t)
        dydt = radius * winding * np.cos(winding * t)
        integrand = (-y * dxdt + x * dydt) / (x * x + y * y)
        integral = float(np.sum(integrand) * dt)
        expected = 2.0 * PI * winding
        assert abs(integral - expected) < 2e-12, (radius, winding, integral)
        winding_rows.append(
            {
                "radius": radius,
                "winding": winding,
                "integral": integral,
                "expected": expected,
            }
        )

    # W3: integrate the unsimplified radial boundary coefficients.  Round
    # curvature is twice the FS normalization used in the note.
    flux_rows = []
    for radius in (0.25, 1.0, 3.0, 20.0):
        round_integrand = np.full_like(t, 2.0 * radius**2 / (1.0 + radius**2))
        round_flux = float(np.sum(round_integrand) * dt)
        expected_round = 4.0 * PI * radius**2 / (1.0 + radius**2)
        fs_flux = 0.5 * round_flux
        expected_fs = 2.0 * PI * radius**2 / (1.0 + radius**2)
        assert abs(round_flux - expected_round) < 2e-12
        assert abs(fs_flux - expected_fs) < 2e-12
        flux_rows.append(
            {
                "radius": radius,
                "round_flux": round_flux,
                "fs_flux": fs_flux,
            }
        )

    # W6: F(p,q)=(p,q^2).  The two roots above the fold have opposite
    # Jacobian signs; at the fold the determinant is zero.
    target_b = 0.36
    fold_roots = (math.sqrt(target_b), -math.sqrt(target_b))
    fold_determinants = tuple(2.0 * q for q in fold_roots)
    assert fold_determinants[0] > 0.0 and fold_determinants[1] < 0.0
    assert sum(1 if det > 0.0 else -1 for det in fold_determinants) == 0
    assert 2.0 * 0.0 == 0.0

    # W7: exact special values on k(t)=(t,t).
    diagonal = {
        "t=0": signed_density(0.0, 0.0),
        "t=pi/2": signed_density(PI / 2.0, PI / 2.0),
        "t=pi": signed_density(PI, PI),
    }
    assert abs(diagonal["t=0"] - 0.5) < 1e-15
    assert abs(diagonal["t=pi/2"]) < 1e-15
    assert abs(diagonal["t=pi"] + 1.0 / 18.0) < 1e-15

    return {
        "circle_winding": winding_rows,
        "sphere_boundary_flux": flux_rows,
        "toy_fold_determinants": list(fold_determinants),
        "two_band_diagonal": diagonal,
    }


def bloch_and_jacobian(k: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return n(k) and the analytic 3x2 Jacobian dn/d(kx,ky)."""

    kx, ky = float(k[0]), float(k[1])
    d = d_vector(kx, ky)
    r = np.linalg.norm(d)
    ddx = np.array([math.cos(kx), 0.0, math.sin(kx)])
    ddy = np.array([0.0, math.cos(ky), math.sin(ky)])
    columns = []
    for dd in (ddx, ddy):
        columns.append(-(dd / r - d * np.dot(d, dd) / r**3))
    return -d / r, np.column_stack(columns)


def meridian_target(theta: float) -> np.ndarray:
    return np.array([math.sin(theta), 0.0, -math.cos(theta)])


def meridian_roots(theta: float) -> list[tuple[str, np.ndarray]]:
    """Closed-form roots for q(theta)=(sin theta,0,-cos theta)."""

    roots: list[tuple[str, np.ndarray]] = [
        ("A", np.array([-PI + theta, 0.0]))
    ]
    if abs(theta) < 1e-15:
        roots.extend(
            [
                ("B", np.array([0.0, PI])),
                ("C", np.array([-PI, PI])),
            ]
        )
        return roots

    a = math.tan(theta)
    discriminant = 1.0 - 3.0 * a * a
    if discriminant < -1e-13:
        return roots
    discriminant = max(0.0, discriminant)
    for sheet_id, sign in (("B", -1.0), ("C", 1.0)):
        t = (1.0 + sign * math.sqrt(discriminant)) / (3.0 * a)
        u = 2.0 * math.atan(t)
        roots.append((sheet_id, np.array([-u, PI])))
    return roots


def tangent_frame(q: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    t1 = EA - np.dot(EA, q) * q
    t1 /= np.linalg.norm(t1)
    t2 = np.cross(q, t1)
    t2 /= np.linalg.norm(t2)
    return t1, t2


def cusp_target(a: float, b: float) -> np.ndarray:
    q = QC + a * EA + b * EB
    return q / np.linalg.norm(q)


def solve_all_roots(q: np.ndarray, grid: int = 17) -> list[np.ndarray]:
    """Solve n(k)=q from an independent periodic seed grid.

    Newton is applied to two target-tangent components.  A candidate is kept
    only when the full three-vector residual is small, then periodic duplicates
    are clustered.
    """

    t1, t2 = tangent_frame(q)
    roots: list[np.ndarray] = []
    seeds = np.linspace(-PI, PI, grid, endpoint=False)
    for x0 in seeds:
        for y0 in seeds:
            k = np.array([x0, y0], dtype=float)
            for _ in range(35):
                n, j3 = bloch_and_jacobian(k)
                residual = np.array([np.dot(t1, n - q), np.dot(t2, n - q)])
                jac = np.vstack([t1 @ j3, t2 @ j3])
                if abs(np.linalg.det(jac)) < 1e-13:
                    break
                step = np.linalg.solve(jac, residual)
                k = wrap(k - step)
                if np.linalg.norm(step) < 1e-12:
                    break
            n, _ = bloch_and_jacobian(k)
            if np.linalg.norm(n - q) >= 1e-8:
                continue
            if any(np.linalg.norm(wrap(k - old)) < 1e-6 for old in roots):
                continue
            roots.append(k.copy())
    roots.sort(key=lambda z: (float(z[0]), float(z[1])))
    return roots


def check_closed_form_meridian() -> dict[str, object]:
    rows = []
    for degrees in (0.0, 10.0, 20.0, 25.0, 29.0, 29.9, 30.0, 30.1, 35.0, 40.0):
        theta = math.radians(degrees)
        q = meridian_target(theta)
        roots = meridian_roots(theta)
        signed_sum = 0
        for sheet_id, k in roots:
            residual = float(np.linalg.norm(lower_bloch(*k) - q))
            assert residual < 2e-8, (degrees, sheet_id, residual)
            n0 = n_numerator(*k)
            sign = 0 if abs(n0) < 2e-7 else (1 if n0 > 0.0 else -1)
            if degrees != 30.0:
                signed_sum += sign
            rows.append(
                {
                    "theta_deg": degrees,
                    "sheet": sheet_id,
                    "kx": float(k[0]),
                    "ky": float(k[1]),
                    "N": n0,
                    "lambda": signed_density(*k),
                    "orientation": sign,
                    "map_residual": residual,
                }
            )
        if degrees < 30.0:
            assert len(roots) == 3 and signed_sum == 1
        elif degrees > 30.0:
            assert len(roots) == 1 and signed_sum == 1
        else:
            assert len(roots) == 3  # B and C are the same critical root.
    return {"rows": rows}


def check_cusp_trace() -> dict[str, object]:
    a = 0.04
    b_values = (-0.012, -0.006, -0.005, 0.0, 0.005, 0.006, 0.012)
    expected_counts = (1, 1, 3, 3, 3, 1, 1)
    rows = []
    for b, expected in zip(b_values, expected_counts, strict=True):
        q = cusp_target(a, b)
        roots = solve_all_roots(q)
        assert len(roots) == expected, (b, len(roots), roots)
        signed_sum = 0
        for k in roots:
            n0 = n_numerator(*k)
            orientation = 1 if n0 > 0.0 else -1
            signed_sum += orientation
            rows.append(
                {
                    "A": a,
                    "B": b,
                    "qx": float(q[0]),
                    "qy": float(q[1]),
                    "qz": float(q[2]),
                    "kx": float(k[0]),
                    "ky": float(k[1]),
                    "N": n0,
                    "orientation": orientation,
                    "map_residual": float(np.linalg.norm(lower_bloch(*k) - q)),
                }
            )
        assert signed_sum == 1, (b, signed_sum)
    return {"rows": rows, "counts": list(expected_counts)}


def check_critical_parameterization() -> dict[str, float]:
    max_n = 0.0
    max_radius_error = 0.0
    for c in np.linspace(-1.0, 0.5, 301):
        cy = -c / (1.0 - c)
        for sx_sign in (-1.0, 1.0):
            for sy_sign in (-1.0, 1.0):
                sx = sx_sign * math.sqrt(max(0.0, 1.0 - c * c))
                sy = sy_sign * math.sqrt(max(0.0, 1.0 - cy * cy))
                d = np.array([sx, sy, 1.0 - c - cy])
                max_n = max(max_n, abs(c + cy - c * cy))
                max_radius_error = max(max_radius_error, abs(np.dot(d, d) - 3.0))
    assert max_n < 2e-15
    assert max_radius_error < 4e-15
    return {"max_abs_N": max_n, "max_abs_r2_minus_3": max_radius_error}


def check_finite_difference(samples: int = 100, h: float = 1e-6) -> dict[str, float]:
    rng = np.random.default_rng(251015760)
    errors = []
    for kx, ky in rng.uniform(-PI, PI, (samples, 2)):
        dx = (lower_bloch(kx + h, ky) - lower_bloch(kx - h, ky)) / (2.0 * h)
        dy = (lower_bloch(kx, ky + h) - lower_bloch(kx, ky - h)) / (2.0 * h)
        finite = 0.5 * np.dot(lower_bloch(kx, ky), np.cross(dx, dy))
        errors.append(abs(finite - signed_density(kx, ky)))
    maximum = float(max(errors))
    mean = float(np.mean(errors))
    assert maximum < 2e-9
    return {"samples": samples, "h": h, "max_abs_error": maximum, "mean_abs_error": mean}


def check_global_integrals(grid: int = 800) -> dict[str, float]:
    h = 2.0 * PI / grid
    k = -PI + (np.arange(grid) + 0.5) * h
    cx = np.cos(k)[:, None]
    cy = np.cos(k)[None, :]
    n0 = cx + cy - cx * cy
    density = n0 / (2.0 * (3.0 - 2.0 * n0) ** 1.5)
    signed = float(np.sum(density) * h * h)
    unsigned = float(np.sum(np.abs(density)) * h * h)
    negative_magnitude = float(np.sum(np.where(density < 0.0, -density, 0.0)) * h * h)
    assert abs(signed / (2.0 * PI) - 1.0) < 2e-8
    assert abs(unsigned / (2.0 * PI) - 1.1889493) < 2e-5
    return {
        "grid": grid,
        "signed_integral": signed,
        "signed_over_2pi": signed / (2.0 * PI),
        "unsigned_integral": unsigned,
        "unsigned_over_2pi": unsigned / (2.0 * PI),
        "negative_magnitude": negative_magnitude,
    }


def svg_point(x: float, y: float, box: tuple[float, float, float, float]) -> tuple[float, float]:
    left, top, width, height = box
    return left + (x + PI) * width / (2.0 * PI), top + (PI - y) * height / (2.0 * PI)


def write_svg(path: Path) -> None:
    """Write a small two-panel visual aid; calculations remain in the note."""

    width, height = 1100, 520
    domain_box = (60.0, 75.0, 430.0, 390.0)
    target_box = (610.0, 75.0, 390.0, 390.0)
    domain_paths = []
    target_paths = []
    for sx_sign in (-1.0, 1.0):
        for sy_sign in (-1.0, 1.0):
            dpoints = []
            tpoints = []
            for c in np.linspace(-1.0, 0.5, 501):
                cy = -c / (1.0 - c)
                x = sx_sign * math.acos(c)
                y = sy_sign * math.acos(cy)
                px, py = svg_point(x, y, domain_box)
                dpoints.append(f"{px:.2f},{py:.2f}")
                sx = sx_sign * math.sqrt(max(0.0, 1.0 - c * c))
                sy = sy_sign * math.sqrt(max(0.0, 1.0 - cy * cy))
                qx, qy = -sx / SQRT3, -sy / SQRT3
                left, top, w, h = target_box
                tx = left + (qx + 1.0) * w / 2.0
                ty = top + (1.0 - qy) * h / 2.0
                tpoints.append(f"{tx:.2f},{ty:.2f}")
            domain_paths.append(" ".join(dpoints))
            target_paths.append(" ".join(tpoints))

    cusp_marks = []
    for sx_sign in (-1.0, 1.0):
        for sy_sign in (-1.0, 1.0):
            qx, qy = -sx_sign / SQRT3, -sy_sign / SQRT3
            left, top, w, h = target_box
            tx = left + (qx + 1.0) * w / 2.0
            ty = top + (1.0 - qy) * h / 2.0
            cusp_marks.append(f'<circle cx="{tx:.2f}" cy="{ty:.2f}" r="6" class="cusp"/>')

    fold_source = svg_point(-PI / 3.0, PI, domain_box)
    left, top, w, h = target_box
    fold_target = (left + 0.75 * w, top + 0.5 * h)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
  .bg{{fill:#fbfaf7}} .panel{{fill:#fff;stroke:#cfc8bb;stroke-width:2}}
  .curve{{fill:none;stroke:#1e6b8c;stroke-width:3}} .axis{{stroke:#ddd5c8;stroke-width:1}}
  .trace{{stroke:#b54d38;stroke-width:3;stroke-dasharray:8 6}} .fold{{fill:#b54d38}}
  .cusp{{fill:#f3b33d;stroke:#7a4c00;stroke-width:2}} text{{font-family:Arial,sans-serif;fill:#2b2925}}
  .title{{font-size:22px;font-weight:700}} .label{{font-size:16px}}
</style>
<rect width="100%" height="100%" class="bg"/>
<rect x="60" y="75" width="430" height="390" rx="12" class="panel"/>
<rect x="610" y="75" width="390" height="390" rx="195" class="panel"/>
<text x="60" y="42" class="title">domain T²: singular set Σ</text>
<text x="610" y="42" class="title">target S²: critical-value curve (qₓ,qᵧ view)</text>
<line x1="275" y1="75" x2="275" y2="465" class="axis"/><line x1="60" y1="270" x2="490" y2="270" class="axis"/>
<line x1="805" y1="75" x2="805" y2="465" class="axis"/><line x1="610" y1="270" x2="1000" y2="270" class="axis"/>
{''.join(f'<polyline points="{p}" class="curve"/>' for p in domain_paths)}
{''.join(f'<polyline points="{p}" class="curve"/>' for p in target_paths)}
{''.join(cusp_marks)}
<line x1="805" y1="270" x2="930" y2="270" class="trace"/>
<circle cx="{fold_source[0]:.2f}" cy="{fold_source[1]:.2f}" r="6" class="fold"/>
<circle cx="{fold_target[0]:.2f}" cy="{fold_target[1]:.2f}" r="6" class="fold"/>
<text x="68" y="492" class="label">red point: k=(-π/3,π), ordinary fold</text>
<text x="618" y="492" class="label">dashed meridian crosses q=(1/2,0,-√3/2)</text>
</svg>'''
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=800)
    parser.add_argument("--write-svg", type=Path)
    args = parser.parse_args()

    report = {
        "winding_warmups": check_winding_warmups(),
        "actual_torus_patches": check_actual_torus_patches(),
        "critical_parameterization": check_critical_parameterization(),
        "meridian": check_closed_form_meridian(),
        "cusp": check_cusp_trace(),
        "finite_difference": check_finite_difference(),
        "global_integrals": check_global_integrals(args.grid),
    }
    if args.write_svg is not None:
        args.write_svg.parent.mkdir(parents=True, exist_ok=True)
        write_svg(args.write_svg)
        report["svg"] = str(args.write_svg)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
