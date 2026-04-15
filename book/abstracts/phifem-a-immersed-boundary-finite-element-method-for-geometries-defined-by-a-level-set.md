---
title: 'PhiFEM : a immersed boundary finite element method for geometries defined by a level-set'
authors:
  - name:
      literal: 'Raphaël Bulle'
    affiliations:
      - 'Inria'
  - name:
      literal: 'Michel Duprez'
    affiliations:
      - 'Inria'
    email: 'michel.duprez@inria.fr'
  - name:
      literal: 'Vanessa Lleras'
    affiliations:
      - 'Université de Montpellier'
  - name:
      literal: 'Alexei Lozinski'
    affiliations:
      - 'Université de Besançon'
  - name:
      literal: 'Killian Vuillemot'
    affiliations:
      - 'Université de Montpellier'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Michel Duprez (Inria)

In this talk, we will present a fictitious domain finite element method called φ-FEM, well suited for elliptic problems posed in a domain given by a level-set function without requiring a mesh fitting the boundary. Unlike other recent fictitious domain-type methods (XFEM, Cut-FEM), our approach does not need any non-standard numerical integration, neither on the cut mesh elements nor on the actual boundary. We shall present the proofs of optimal convergence of our methods on the example of Poisson equation using Lagrange finite elements of any order. Furthermore, we highlight the flexibility and efficiency of our method on different problems (crack, interface, Stokes, heat equation,...). We will also give numerical tests illustrating the optimal convergence of our methods and discuss the conditioning of resulting linear systems and the robustness with respect to the geometry.

# References
[1] R. Becker, R. Bulle, M. Duprez, V. Lleras. Residual-based a posteriori error estimates with boundary correction for φ-FEM, in preparation.

[2] M. Duprez, A. Lozinski, V. Lleras, V. Vigon, K. Vuillemot. A finite difference scheme with an optimal convergence for elliptic PDEs on domains defined by a levelset function, Journal of Scientific Computing, 104 (23), 2025.

[3] M. Duprez, V. Lleras, A. Lozinski. A new φ-FEM approach for problems with natural boundary conditions. Numerical Methods for Partial Differential Equations, 39(1):281-303, 2023.

[4] M. Duprez M, V. Lleras and A. Lozinski. φ-FEM: an optimally convergent and easily imple-

mentable immersed boundary method for particulate flows and Stokes equations. ESAIM: Mathematical Modelling and Numerical Analysis, 1;57(3):1111-42, 2023.

[5] S. Cotin, M. Duprez, V. Lleras, A. Lozinski and K. Vuillemot. φ-FEM: An Efficient Simulation

Tool Using Simple Meshes for Problems in Structure Mechanics and Heat Transfer. Partition of Unity Methods, 19:191-216, 2023.

[6] M.Duprez, V. Lleras, A. Lozinski, K. Vuillemot. φ-FEM for the heat equation: optimal convergence on unfitted meshes in space, Comptes Rendus. Mathématique, Tome 361, 1699:1710, 2023.

[7] M. Duprez, A. Lozinski. φ-FEM: a finite element method on domains defined by level-sets. SIAM Journal on Numerical Analysis, 58(2):1008-28, 2020.


