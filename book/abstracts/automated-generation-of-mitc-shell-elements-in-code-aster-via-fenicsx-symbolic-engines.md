---
title: 'Automated generation of MITC shell elements in code\_aster via FEniCSx symbolic engines'
authors:
  - name:
      literal: 'A. Bouaziz'
    affiliations:
      - 'EDF Lab Paris-Saclay'
  - name:
      literal: 'J. Cornejo'
    affiliations:
      - 'EDF Lab Paris-Saclay'
    email: 'joaquin.cornejo-fuentes@edf.fr'
  - name:
      literal: 'N. Tardieu'
    affiliations:
      - 'EDF Lab Paris-Saclay'
  - name:
      literal: 'V. Le Corvec'
    affiliations:
      - 'EDF Lab Paris-Saclay'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Joaquin Cornejo (EDF Lab Paris Saclay)

This project introduces a novel framework that bridges the symbolic automation of FEniCSx with Code_Aster. While traditional element development in Code_Aster requires tedious manual derivation and Fortran implementation, this approach takes advantage of FEniCSx to automatically generate optimized C-code kernels directly from variational energy formulations. This paradigm shift not only accelerates development cycles but also ensures mathematical exactness by eliminating manual differentiation.

The core of this work details the integration of a Reissner-Mindlin shell formulation using Mixed Interpolation of Tensorial Components (MITC) to inherently bypass shear locking. We address the non-trivial architectural challenges of mapping FEniCSx-generated kernels onto Code_Aster's Fortran environment, specifically regarding disparate nodal numbering conventions and the management of non-standard degree of freedom.

A significant breakthrough was achieved in the treatment of Nédélec-type elements. To maintain compatibility with Code_Aster's assembler, we implemented a local static condensation strategy. By eliminating Nédélec degrees of freedom at the element level, we successfully recovered a nodal-only interface that matches the efficiency and structure of Code_Aster solvers while preserving the benefits of the MITC formulation.

Current results demonstrate perfect agreement with established benchmarks in linear elasticity. However, the true potential of this framework lies in its future: we are working on integrating MFront and JAX to handle non-linear constitutive laws through automatic differentiation and code generation. This work paves the way for a new shell element in Code_Aster, one that combines the flexibility of modern research tools with the rigorous safety standards required for nuclear industry simulations.

# References
Hale JS, Brunetti M, Bordas SP, Maurini C. Simple and extensible plate and shell finite element models through automatic code generation tools. Computers & Structures. 2018 Oct 15;209:163-81.

Latyshev A, Bleyer J, Maurini C, Hale J. Expressing general constitutive models in FEniCSx using external operators and algorithmic automatic differentiation. Journal of Theoretical, Computational and Applied Mechanics. 2025 Sep 22.


