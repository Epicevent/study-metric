"""Independent checks for Winding_Form에서_Degree까지_한노트.md."""

from __future__ import annotations

import json
import math

import numpy as np
import sympy as sp


PI = math.pi
SQRT3 = math.sqrt(3.0)


def winding_of_parametric_curve(
    xy: np.ndarray, dxy_dt: np.ndarray, period: float = 2.0 * PI
) -> float:
    numerator = -xy[:, 1] * dxy_dt[:, 0] + xy[:, 0] * dxy_dt[:, 1]
    denominator = np.sum(xy * xy, axis=1)
    return float(np.mean(numerator / denominator) * period)


def check_circle_and_ellipse(samples: int = 200_000) -> dict[str, object]:
    t = np.arange(samples, dtype=float) * (2.0 * PI / samples)
    rows = []
    for radius, winding in ((3.0, -2), (0.7, 1), (2.5, 3)):
        xy = np.column_stack(
            [radius * np.cos(winding * t), radius * np.sin(winding * t)]
        )
        dxy = np.column_stack(
            [
                -radius * winding * np.sin(winding * t),
                radius * winding * np.cos(winding * t),
            ]
        )
        integral = winding_of_parametric_curve(xy, dxy)
        expected = 2.0 * PI * winding
        assert abs(integral - expected) < 2e-12
        rows.append(
            {
                "radius": radius,
                "winding": winding,
                "integral": integral,
                "expected": expected,
            }
        )

    ellipse_rows = []
    for a, b in ((2.0, -3.0), (-0.6343318695521013, -0.8696098242131741),
                 (0.2796059453934639, -0.3833136701680371)):
        xy = np.column_stack([a * np.cos(t), b * np.sin(t)])
        dxy = np.column_stack([-a * np.sin(t), b * np.cos(t)])
        integral = winding_of_parametric_curve(xy, dxy)
        expected = 2.0 * PI * (1.0 if a * b > 0.0 else -1.0)
        assert abs(integral - expected) < 2e-12
        ellipse_rows.append(
            {
                "a": a,
                "b": b,
                "determinant": a * b,
                "integral": integral,
                "expected": expected,
            }
        )
    return {"circles": rows, "ellipses": ellipse_rows}


def check_fs_potential() -> dict[str, str]:
    x, y = sp.symbols("x y", real=True)
    denominator = 1 + x**2 + y**2
    alpha_x = -y / denominator
    alpha_y = x / denominator
    exterior_derivative = sp.simplify(
        sp.diff(alpha_y, x) - sp.diff(alpha_x, y)
    )
    expected = 2 / denominator**2
    assert sp.simplify(exterior_derivative - expected) == 0

    r = sp.symbols("r", positive=True)
    total_area = sp.integrate(2 * r / (1 + r**2) ** 2, (r, 0, sp.oo)) * 2 * sp.pi
    assert sp.simplify(total_area - 2 * sp.pi) == 0
    return {
        "d_alpha_coefficient": str(exterior_derivative),
        "total_fs_area": str(total_area),
    }


def d_vector(kx: float, ky: float) -> np.ndarray:
    return np.array(
        [
            math.sin(kx),
            math.sin(ky),
            1.0 - math.cos(kx) - math.cos(ky),
        ],
        dtype=float,
    )


def bloch_and_jacobian(kx: float, ky: float) -> tuple[np.ndarray, np.ndarray]:
    d = d_vector(kx, ky)
    radius = float(np.linalg.norm(d))
    ddx = np.array([math.cos(kx), 0.0, math.sin(kx)])
    ddy = np.array([0.0, math.cos(ky), math.sin(ky)])
    columns = []
    for derivative in (ddx, ddy):
        columns.append(
            -(derivative / radius - d * float(np.dot(d, derivative)) / radius**3)
        )
    return -d / radius, np.column_stack(columns)


def meridian_target(theta: float) -> np.ndarray:
    return np.array([math.sin(theta), 0.0, -math.cos(theta)])


def meridian_roots(theta: float) -> list[tuple[str, np.ndarray]]:
    roots = [("A", np.array([-PI + theta, 0.0]))]
    tangent = math.tan(theta)
    discriminant = 1.0 - 3.0 * tangent * tangent
    if discriminant < 0.0:
        return roots
    square_root = math.sqrt(max(0.0, discriminant))
    for name, sign in (("B", -1.0), ("C", 1.0)):
        half_angle_tangent = (1.0 + sign * square_root) / (3.0 * tangent)
        u = 2.0 * math.atan(half_angle_tangent)
        roots.append((name, np.array([-u, PI])))
    return roots


def winding_of_linear_map(matrix: np.ndarray, samples: int = 200_000) -> float:
    t = np.arange(samples, dtype=float) * (2.0 * PI / samples)
    circle = np.vstack([np.cos(t), np.sin(t)])
    circle_derivative = np.vstack([-np.sin(t), np.cos(t)])
    xy = (matrix @ circle).T
    dxy = (matrix @ circle_derivative).T
    return winding_of_parametric_curve(xy, dxy)


def check_paper_meridian() -> dict[str, object]:
    reports = []
    for degrees, expected_count in ((20.0, 3), (35.0, 1)):
        theta = math.radians(degrees)
        q = meridian_target(theta)
        t1 = np.array([math.cos(theta), 0.0, math.sin(theta)])
        t2 = np.array([0.0, -1.0, 0.0])
        assert np.linalg.norm(np.cross(t1, t2) - q) < 1e-14

        roots = meridian_roots(theta)
        assert len(roots) == expected_count
        rows = []
        signed_sum = 0
        winding_sum = 0.0
        for name, k in roots:
            n, jacobian_3d = bloch_and_jacobian(float(k[0]), float(k[1]))
            assert np.linalg.norm(n - q) < 5e-15
            matrix = np.vstack([t1 @ jacobian_3d, t2 @ jacobian_3d])
            determinant = float(np.linalg.det(matrix))
            sign = 1 if determinant > 0.0 else -1
            winding_integral = winding_of_linear_map(matrix)
            assert abs(winding_integral - sign * 2.0 * PI) < 2e-12
            signed_sum += sign
            winding_sum += winding_integral
            rows.append(
                {
                    "sheet": name,
                    "k": [float(k[0]), float(k[1])],
                    "jacobian": matrix.tolist(),
                    "determinant": determinant,
                    "winding_integral": winding_integral,
                }
            )
        assert signed_sum == 1
        assert abs(winding_sum / (2.0 * PI) - 1.0) < 1e-12
        reports.append(
            {
                "theta_degrees": degrees,
                "target": q.tolist(),
                "root_count": len(roots),
                "rows": rows,
                "signed_sum": signed_sum,
                "winding_sum_over_2pi": winding_sum / (2.0 * PI),
            }
        )
    return {"targets": reports}


def check_global_signed_area(grid: int = 800) -> dict[str, float]:
    spacing = 2.0 * PI / grid
    coordinates = -PI + (np.arange(grid) + 0.5) * spacing
    cx = np.cos(coordinates)[:, None]
    cy = np.cos(coordinates)[None, :]
    numerator = cx + cy - cx * cy
    density = numerator / (2.0 * (3.0 - 2.0 * numerator) ** 1.5)
    signed = float(np.sum(density) * spacing**2)
    unsigned = float(np.sum(np.abs(density)) * spacing**2)
    assert abs(signed / (2.0 * PI) - 1.0) < 2e-8
    assert abs(unsigned / (2.0 * PI) - 1.1889492578) < 2e-8
    return {
        "grid": grid,
        "signed_integral": signed,
        "signed_over_2pi": signed / (2.0 * PI),
        "unsigned_integral": unsigned,
        "unsigned_over_2pi": unsigned / (2.0 * PI),
        "curvature_unsigned_over_2pi": 2.0 * unsigned / (2.0 * PI),
    }


def check_fold_pair(samples: int = 200_000) -> dict[str, object]:
    t = np.arange(samples, dtype=float) * (2.0 * PI / samples)
    epsilon = 1e-3
    rows = []
    winding_sum = 0.0
    for q0 in (0.5, -0.5):
        delta_p = epsilon * np.cos(t)
        delta_q = epsilon * np.sin(t)
        x = delta_p
        y = (q0 + delta_q) ** 2 - 0.25
        dx = -epsilon * np.sin(t)
        dy = 2.0 * (q0 + delta_q) * epsilon * np.cos(t)
        integral = winding_of_parametric_curve(
            np.column_stack([x, y]), np.column_stack([dx, dy])
        )
        expected = 2.0 * PI * (1.0 if q0 > 0.0 else -1.0)
        assert abs(integral - expected) < 2e-12
        winding_sum += integral
        rows.append({"q0": q0, "integral": integral, "expected": expected})
    assert abs(winding_sum) < 2e-12
    return {"rows": rows, "sum": winding_sum}


def check_weierstrass_local_model(samples: int = 200_000) -> dict[str, float]:
    t = np.arange(samples, dtype=float) * (2.0 * PI / samples)
    epsilon = 0.2
    # The exact leading branch model z -> z^2. Higher O(z^6) terms do not
    # change the winding for sufficiently small epsilon.
    x = epsilon**2 * np.cos(2.0 * t)
    y = epsilon**2 * np.sin(2.0 * t)
    dx = -2.0 * epsilon**2 * np.sin(2.0 * t)
    dy = 2.0 * epsilon**2 * np.cos(2.0 * t)
    integral = winding_of_parametric_curve(
        np.column_stack([x, y]), np.column_stack([dx, dy])
    )
    assert abs(integral - 4.0 * PI) < 2e-12

    radii = (0.05, 0.2, 0.7)
    curvature_values = []
    for radius in radii:
        area_density = 8.0 * radius**2 / (1.0 + radius**4) ** 2
        minus_laplacian = 16.0 * radius**2 / (1.0 + radius**4) ** 2
        curvature = minus_laplacian / area_density
        assert abs(curvature - 2.0) < 1e-12
        curvature_values.append(curvature)
    return {
        "branch_winding_integral": integral,
        "degree": integral / (2.0 * PI),
        "curvature_samples": curvature_values,
        "point_defect": -2.0 * PI,
    }


def main() -> None:
    report = {
        "circle_and_ellipse": check_circle_and_ellipse(),
        "fs_potential": check_fs_potential(),
        "paper_meridian": check_paper_meridian(),
        "fold_pair": check_fold_pair(),
        "global_signed_area": check_global_signed_area(),
        "weierstrass_control": check_weierstrass_local_model(),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
