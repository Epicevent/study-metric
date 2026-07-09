# Selected Problems — *Calculus for Learning Riemannian Geometry* (교수님)

Verbatim transcription (English original) of the Basic Formulas section and Problems 1, 2, 5, 6, 7, 9, 10, 11, 12, 13, 22, 23, 24, 25, 28, 30, 31, 32, 33, 36.

---

## Basic Formulas
<!-- LRG p.03 -->

Let $g = g_{ij}\,dx^i dx^j$ be a Riemannian metric. The inverse metric is denoted by $(g^{ij})$. The volume form is

$$d\operatorname{vol}_g = \sqrt{\det(g_{ij})}\, dx^1 \wedge \cdots \wedge dx^n.$$

For a smooth function $f$,

$$(\operatorname{grad} f)^i = g^{ij}\partial_j f.$$

For a vector field $X = X^i \partial_i$,

$$\operatorname{div} X = \frac{1}{\sqrt{\det g}}\,\partial_i\!\left(\sqrt{\det g}\, X^i\right).$$

The Laplace–Beltrami operator is

$$\Delta f = \operatorname{div}(\operatorname{grad} f) = \frac{1}{\sqrt{\det g}}\,\partial_i\!\left(\sqrt{\det g}\, g^{ij}\partial_j f\right).$$

The Christoffel symbols of the Levi–Civita connection are

$$\Gamma^k_{ij} = \frac{1}{2} g^{k\ell}\left(\partial_i g_{j\ell} + \partial_j g_{i\ell} - \partial_\ell g_{ij}\right).$$

The Hessian of $f$ is

$$(\nabla^2 f)_{ij} = \partial_i \partial_j f - \Gamma^k_{ij}\partial_k f.$$

The Riemann curvature tensor is

$$R^\ell{}_{kij} = \partial_i \Gamma^\ell_{jk} - \partial_j \Gamma^\ell_{ik} + \Gamma^m_{jk}\Gamma^\ell_{im} - \Gamma^m_{ik}\Gamma^\ell_{jm}.$$

For differential forms, the Hodge Laplacian is

$$\Delta_H = d\delta + \delta d,$$

where

$$\delta = (-1)^{n(k+1)+1} * d\, *$$

on $k$-forms in dimension $n$. On functions, up to sign convention,

$$\Delta_H f = \delta d f.$$

The Bochner formula for a smooth function is

$$\frac{1}{2}\Delta |\operatorname{grad} f|^2 = |\nabla^2 f|^2 + \langle \operatorname{grad} f, \operatorname{grad} \Delta f\rangle + \operatorname{Ric}(\operatorname{grad} f, \operatorname{grad} f).$$

---

### LRG Problem 1
<!-- LRG p.04 -->

**Problem 1. Area Form on $S^2$ in Spherical Coordinates**

Let

$$S^2 = \{(x, y, z) \in \mathbb{R}^3 : x^2 + y^2 + z^2 = 1\}$$

and use

$$X(\theta, \phi) = (\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta).$$

(a) Compute $X_\theta$ and $X_\phi$.

(b) Compute $g_{\theta\theta}$, $g_{\theta\phi}$, and $g_{\phi\phi}$.

(c) Verify that

$$g = d\theta^2 + \sin^2\theta\, d\phi^2.$$

(d) Compute $\sqrt{\det(g)}$.

(e) Show that

$$dA = \sin\theta\, d\theta \wedge d\phi.$$

(f) Compute $\operatorname{Area}(S^2) = 4\pi$.

---

### LRG Problem 2
<!-- LRG p.05 -->

**Problem 2. Area Form on $S^2$ in Stereographic Coordinates**

Use stereographic coordinates

$$X(u, v) = \left(\frac{2u}{1 + u^2 + v^2},\ \frac{2v}{1 + u^2 + v^2},\ \frac{u^2 + v^2 - 1}{1 + u^2 + v^2}\right).$$

(a) Compute $X_u$ and $X_v$.

(b) Compute $g_{uu}$, $g_{uv}$, and $g_{vv}$.

(c) Verify that

$$g = \frac{4}{(1 + u^2 + v^2)^2}(du^2 + dv^2).$$

(d) Compute

$$dA = \frac{4}{(1 + u^2 + v^2)^2}\, du \wedge dv.$$

(e) Compute the area by converting to polar coordinates.

---

### LRG Problem 5
<!-- LRG p.08 -->

**Problem 5. The Upper Half-Plane Metric**

Let

$$H = \{z = x + iy : y > 0\}$$

with metric

$$g_H = \frac{dx^2 + dy^2}{y^2}.$$

(a) Compute $g_{ij}$, $g^{ij}$, and $\sqrt{\det g}$.

(b) Compute the area form.

(c) Compute $\operatorname{grad} f$ for a general function $f(x, y)$.

(d) Compute $\operatorname{div} X$ for $X = X^x \partial_x + X^y \partial_y$.

(e) Derive

$$\Delta_H f = y^2(f_{xx} + f_{yy})$$

up to the chosen sign convention.

---

### LRG Problem 6
<!-- LRG p.09 -->

**Problem 6. The Poincaré Disk Metric**

Let

$$D = \{z = x + iy : |z| < 1\}$$

with metric

$$g_D = \frac{4(dx^2 + dy^2)}{(1 - x^2 - y^2)^2}.$$

(a) Compute $g_{ij}$, $g^{ij}$, and $\sqrt{\det g}$.

(b) Compute the area form.

(c) Compute $\operatorname{grad} f$.

(d) Compute $\operatorname{div} X$.

(e) Compute $\Delta_D f$.

---

### LRG Problem 7
<!-- LRG p.10 -->

**Problem 7. Cayley Transform and Arc Length**

Let

$$w = \frac{z - i}{z + i}.$$

(a) Compute

$$dw = \frac{2i}{(z + i)^2}\, dz.$$

(b) Show that

$$1 - |w|^2 = \frac{4\operatorname{Im} z}{|z + i|^2}.$$

(c) Verify

$$\frac{4|dw|^2}{(1 - |w|^2)^2} = \frac{|dz|^2}{(\operatorname{Im} z)^2}.$$

(d) Conclude that the Cayley transform is an isometry between the two models.

---

### LRG Problem 9
<!-- LRG p.12 -->

**Problem 9. Lie Bracket of Vector Fields**

Let

$$X = X^i \partial_i, \qquad Y = Y^j \partial_j.$$

(a) Define

$$[X, Y](f) = X(Y(f)) - Y(X(f)).$$

(b) Expand both terms and show that second derivatives cancel.

(c) Prove

$$[X, Y] = (X^i \partial_i Y^k - Y^i \partial_i X^k)\partial_k.$$

(d) Compute the bracket for

$$X = x\partial_x + y\partial_y, \qquad Y = -y\partial_x + x\partial_y.$$

---

### LRG Problem 10
<!-- LRG p.13 -->

**Problem 10. Flows of Vector Fields**

Let $X$ be a vector field on a manifold $M$.

(a) Define the flow $\varphi_t$ of $X$.

(b) Compute the flow of $X = \partial_x$ on $\mathbb{R}^2$.

(c) Compute the flow of $X = -y\partial_x + x\partial_y$ on $\mathbb{R}^2$.

(d) Interpret this vector field as a rotation field.

(e) Explain how flows are used to define Lie derivatives.

---

### LRG Problem 11
<!-- LRG p.14 -->

**Problem 11. Lie Derivative of Functions and Vector Fields**

Let $X, Y$ be vector fields and $f$ a smooth function.

(a) Show that

$$\mathcal{L}_X f = X(f).$$

(b) Show that

$$\mathcal{L}_X Y = [X, Y].$$

(c) Compute $\mathcal{L}_X Y$ for the rotation field on $\mathbb{R}^2$.

(d) Compute $\mathcal{L}_{\partial_\theta}\partial_\phi$ on $S^2$.

---

### LRG Problem 12
<!-- LRG p.15 -->

**Problem 12. Lie Derivative of One-Forms and Cartan Formula**

Let $\alpha$ be a one-form.

(a) State Cartan's formula:

$$\mathcal{L}_X \alpha = d(\iota_X \alpha) + \iota_X d\alpha.$$

(b) Verify it for $\alpha = dx$ on $\mathbb{R}^2$.

(c) Verify it for $\alpha = x\,dy - y\,dx$.

(d) Compute $\mathcal{L}_X(d\theta)$ and $\mathcal{L}_X(d\phi)$ on $S^2$ for $X = \partial_\phi$.

---

### LRG Problem 13
<!-- LRG p.16 -->

**Problem 13. Lie Derivative of Metrics and Killing Fields**

Let $g$ be a metric.

(a) Show that

$$(\mathcal{L}_X g)(Y, Z) = X(g(Y, Z)) - g([X, Y], Z) - g(Y, [X, Z]).$$

(b) Derive the coordinate formula

$$(\mathcal{L}_X g)_{ij} = X^k \partial_k g_{ij} + g_{kj}\partial_i X^k + g_{ik}\partial_j X^k.$$

(c) Compute $\mathcal{L}_{\partial_\phi} g$ for

$$g = d\theta^2 + \sin^2\theta\, d\phi^2.$$

(d) Conclude that $\partial_\phi$ is a Killing field on $S^2$.

(e) Compute Killing fields on the flat torus.

---

### LRG Problem 22
<!-- LRG p.25 -->

**Problem 22. Covariant Derivative by Normal Projection on $S^2$**

Let $S^2 \subset \mathbb{R}^3$ have unit normal $N(p) = p$.

(a) Define

$$\nabla_X Y = D_X Y - \langle D_X Y, N\rangle\, N.$$

(b) Compute $X_\theta, X_\phi$.

(c) Compute $D_{X_i} X_j$.

(d) Remove the normal component.

(e) Verify

$$\nabla_{\partial_\theta}\partial_\theta = 0,$$
$$\nabla_{\partial_\theta}\partial_\phi = \nabla_{\partial_\phi}\partial_\theta = \cot\theta\, \partial_\phi,$$
$$\nabla_{\partial_\phi}\partial_\phi = -\sin\theta\cos\theta\, \partial_\theta.$$

---

### LRG Problem 23
<!-- LRG p.26 -->

**Problem 23. Covariant Derivative by Normal Projection on the Torus**

Use

$$X(u, v) = ((R + r\cos v)\cos u,\ (R + r\cos v)\sin u,\ r\sin v).$$

(a) Compute $X_u, X_v$.

(b) Compute

$$N = \frac{X_u \times X_v}{\|X_u \times X_v\|}.$$

(c) Compute $X_{uu}, X_{uv}, X_{vv}$.

(d) Remove the normal component from each second derivative.

(e) Extract the Christoffel symbols.

---

### LRG Problem 24
<!-- LRG p.27 -->

**Problem 24. Christoffel Symbols on $S^2$**

Use

$$g = d\theta^2 + \sin^2\theta\, d\phi^2.$$

(a) Compute $g_{ij}$ and $g^{ij}$.

(b) Compute all derivatives of $g_{ij}$.

(c) Compute all nonzero Christoffel symbols.

(d) Verify agreement with the normal projection method.

---

### LRG Problem 25
<!-- LRG p.28 -->

**Problem 25. Christoffel Symbols on the Torus**

Use

$$g = (R + r\cos v)^2 du^2 + r^2 dv^2.$$

(a) Compute $g_{ij}$ and $g^{ij}$.

(b) Compute all derivatives of $g_{ij}$.

(c) Compute all nonzero Christoffel symbols.

(d) Verify agreement with the normal projection method.

---

### LRG Problem 26
<!-- LRG p.29 -->

**Problem 26. Levi–Civita Connection**

Let $\nabla$ be a connection on $TM$.

(a) Define torsion:

$$T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y].$$

(b) Define metric compatibility:

$$X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z).$$

(c) Show that the normal projection connection on a regular surface is torsion-free.

(d) Show that it is metric-compatible.

(e) Conclude that it is the Levi–Civita connection.

---

### LRG Problem 27
<!-- LRG p.30 -->

**Problem 27. Covariant Derivatives of Tensors**

Let

$$T = T^{i_1\cdots i_r}{}_{j_1\cdots j_s}\,\partial_{i_1} \otimes \cdots \otimes \partial_{i_r} \otimes dx^{j_1} \otimes \cdots \otimes dx^{j_s}.$$

(a) Write the formula for $\nabla_k T$.

(b) Specialize it to vector fields.

(c) Specialize it to one-forms.

(d) Specialize it to $(0, 2)$-tensors.

(e) Verify explicitly that $\nabla g = 0$ on $S^2$.

---

### LRG Problem 28
<!-- LRG p.31 -->

**Problem 28. Hessian of a Function**

Let $f \in C^\infty(M)$.

(a) Define

$$\nabla^2 f(X, Y) = X(Yf) - (\nabla_X Y)f.$$

(b) Derive the coordinate formula

$$(\nabla^2 f)_{ij} = \partial_i \partial_j f - \Gamma^k_{ij}\partial_k f.$$

(c) Show that the Hessian is symmetric for the Levi–Civita connection.

(d) Show that

$$\Delta f = \operatorname{tr}_g \nabla^2 f.$$

---

### LRG Problem 30
<!-- LRG p.33 -->

**Problem 30. Geodesic Equation**

Let $\gamma(t) = (x^1(t), \ldots, x^n(t))$.

(a) Define geodesics by

$$\nabla_{\dot\gamma}\dot\gamma = 0.$$

(b) Derive

$$\ddot{x}^k + \Gamma^k_{ij}\dot{x}^i \dot{x}^j = 0.$$

(c) Derive the geodesic equations on $S^2$.

(d) Derive the geodesic equations on the torus.

---

### LRG Problem 31
<!-- LRG p.34 -->

**Problem 31. Great Circles and Normal Projection**

Let $a, b \in \mathbb{R}^3$ be orthonormal and define

$$\gamma(t) = \cos t\, a + \sin t\, b.$$

(a) Show that $\gamma(t) \in S^2$.

(b) Compute $\gamma''(t)$.

(c) Show that $\gamma''(t) = -\gamma(t)$.

(d) Since $N(\gamma) = \gamma$, show that $\gamma''$ is normal.

(e) Conclude that great circles are geodesics.

---

### LRG Problem 32
<!-- LRG p.35 -->

**Problem 32. Hopf Fibers as Totally Geodesic Curves**

Let

$$S^3 = \{(z_1, z_2) \in \mathbb{C}^2 : |z_1|^2 + |z_2|^2 = 1\}.$$

The Hopf fiber through $p = (z_1, z_2)$ is

$$\gamma(t) = e^{it}(z_1, z_2).$$

(a) Compute $\gamma'(t)$.

(b) Compute $\gamma''(t)$.

(c) Show that $\gamma''(t) = -\gamma(t)$.

(d) Show that the acceleration is normal to $S^3$.

(e) Conclude that Hopf fibers are geodesics.

(f) Explain why one-dimensional geodesic submanifolds are totally geodesic.

---

### LRG Problem 33
<!-- LRG p.36 -->

**Problem 33. Shape Operator and Second Fundamental Form on $S^2$**

Let $S^2 \subset \mathbb{R}^3$ have outward normal $N(p) = p$.

(a) Define

$$S(X) = -D_X N.$$

(b) Compute $S(X)$.

(c) Compute the principal curvatures.

(d) Compute the second fundamental form.

(e) Compute Gaussian curvature by

$$K = \det S.$$

---

### LRG Problem 36
<!-- LRG p.39 -->

**Problem 36. Riemann Curvature Tensor on $S^2$**

Use the Christoffel symbols on $S^2$.

(a) Compute $R^\theta{}_{\phi\theta\phi}$.

(b) Compute $R_{\theta\phi\theta\phi}$.

(c) Compute

$$K = \frac{R_{\theta\phi\theta\phi}}{g_{\theta\theta}g_{\phi\phi} - g_{\theta\phi}^2}.$$

(d) Verify $K = 1$.

(e) Compare this with the shape operator calculation.
