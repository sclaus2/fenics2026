---
title: 'Effects of Pre-existing Defects on Helium Bubble Nucleation and Growth in Tungsten'
authors:
  - name:
      literal: 'E. Frikha a'
    affiliations:
      - 'a Sorbonne Paris Nord University, Laboratory of Process and Materials Sciences, LSPM, CNRS, UPR 3407, F-93430, Villetaneuse, France b Aix-Marseille University, CNRS, CINaM, Centre Interdisciplinaire de Nanoscience de Marseille, UMR 7325, F-13288 Marseille, France c Department of Mechanical Engineering, University of Michigan, Ann Arbor, 48109, Michigan, USA'
    email: 'emna.frikha@lspm.cnrs.fr'
  - name:
      literal: 'T. Swinburne b'
    affiliations:
      - 'a Sorbonne Paris Nord University, Laboratory of Process and Materials Sciences, LSPM, CNRS, UPR 3407, F-93430, Villetaneuse, France b Aix-Marseille University, CNRS, CINaM, Centre Interdisciplinaire de Nanoscience de Marseille, UMR 7325, F-13288 Marseille, France c Department of Mechanical Engineering, University of Michigan, Ann Arbor, 48109, Michigan, USA'
  - name:
      literal: 'c'
    affiliations:
      - 'a Sorbonne Paris Nord University, Laboratory of Process and Materials Sciences, LSPM, CNRS, UPR 3407, F-93430, Villetaneuse, France b Aix-Marseille University, CNRS, CINaM, Centre Interdisciplinaire de Nanoscience de Marseille, UMR 7325, F-13288 Marseille, France c Department of Mechanical Engineering, University of Michigan, Ann Arbor, 48109, Michigan, USA'
  - name:
      literal: 'J. Mougenot a'
    affiliations:
      - 'a Sorbonne Paris Nord University, Laboratory of Process and Materials Sciences, LSPM, CNRS, UPR 3407, F-93430, Villetaneuse, France b Aix-Marseille University, CNRS, CINaM, Centre Interdisciplinaire de Nanoscience de Marseille, UMR 7325, F-13288 Marseille, France c Department of Mechanical Engineering, University of Michigan, Ann Arbor, 48109, Michigan, USA'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Emna Frikha (Sorbonne University Paris Nord ( LSPM))

The tokamak is a machine designed to produce nuclear fusion reactions, enabling the generation of abundant, sustainable, low-carbon energy. One of its essential components is the divertor, made of tungsten monoblocks. Helium, produced by fusion reactions, becomes embedded in the tungsten and causes the formation of bubbles and other microstructural defects [1]. These changes gradually alter the mechanical and thermal properties of the material. Some models describe bubble formation through a self-trapping mechanism, but there is still no model intrinsic defect (both vacancies and dislocations) in the material.

In this work, we model a cluster dynamics problem in a continuous medium describing the formation of helium bubbles by trap mutation and nucleation at dislocations and vacancies. The evolution of bubble concentrations promotes their coalescence. Based on previous model, solved with legacy Fenics [2], we develop a one-dimensional finite element model on FEniCSx, with a variational formulation of the coupled equations governing these phenomena and a bursting model [3]. The resulting nonlinear system is assembled using the Unified Form Language (UFL) formalism and solved by the PETSc nonlinear solvers integrated into Dolfinx, via Krylov linearization to ensure numerical robustness and convergence using recommendations from [4]. 

The model allows us to track the spatial and temporal distributions of helium concentrations, as well as the evolution of the bubble radius. We focus on the coupling equations between three sources of nucleation (trap mutation, vacancies and dislocations) and bubbles. We introduce an additional to describe the reduction of nucleation rate by annihilation of vacancies and dislocations when bubbles are created. We show the precautions necessary in this case to achieve convergence.

# References
[1] Dutta, N.J. et al., Journal of Nuclear Materials 452 (2014) 51-56.

[2] Delaporte-Mathurin, R. et al., Scientific Reports 11 (2021) 14681.

[3] Pappalardo, F. et al., Journal of Physics D: Applied Physics 59 (2026) 085203.

[4] Balay, S. et al., Argonne National Laboratory (2024).


