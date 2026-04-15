---
title: 'CutFEMx: A Cut Finite Element Library for FEniCSx'
authors:
  - name:
      literal: 'Susanne Claus'
    affiliations:
      - 'ONERA'
    email: 'susanne.claus@onera.fr'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Susanne Claus (ONERA)

CutFEMx is an extension to FEniCSx for cut finite element methods, released under the MIT license and available at https://github.com/sclaus2/CutFEMx. It extends DOLFINx with support for unfitted discretisations based on level set geometries, enabling the solution of partial differential equations on complex and evolving domains without meshing.

CutFEMx builds on two additional open-source components. The first, CutCells (MIT, available at https://github.com/sclaus2/CutCells), provides robust and efficient algorithms for computing intersections between level set functions and finite element cells of various types. It supports higher-order cutting up to polynomial degree (p=4) and generates both cut meshes for visualisation and quadrature rules on cut cells. The second component, runintgen (MIT, available at https://github.com/sclaus2/runintgen), extends FFCx with runtime quadrature kernel generation, allowing the integration of UFL forms over quadrature rules that vary between elements and are only defined at runtime, as required for cut cell integration.

The framework is designed with an emphasis on performance and modularity, combining cell-local operations, zero-copy data exchange, and compatibility with automatic differentiation workflows. The capabilities of CutFEMx are illustrated on representative examples, including Poisson, Stokes, and elasticity problems posed on implicitly defined domains. Application areas include shape and topology optimization, fluid-structure interaction, multi-material problems, and simulations involving evolving interfaces, where unfitted finite element methods provide a flexible alternative to mesh-conforming approaches.


