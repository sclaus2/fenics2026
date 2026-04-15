---
title: 'A fully monolithic formulation for multiphase fluid-structure interaction'
authors:
  - name:
      literal: 'Marc Hirschvogel'
    affiliations:
      - 'Division 2.2 Process Simulation, Bundesanstalt für Materialforschung und -prüfung (BAM)'
    email: 'marc.hirschvogel@bam.de'
  - name:
      literal: 'John-Paul Gerakis'
    affiliations:
      - 'Division 2.2 Process Simulation, Bundesanstalt für Materialforschung und -prüfung (BAM)'
  - name:
      literal: 'Erik Esche'
    affiliations:
      - 'Division 2.2 Process Simulation, Bundesanstalt für Materialforschung und -prüfung (BAM)'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Marc Hirschvogel (Division 2.2 Process Simulation, Bundesanstalt für Materialforschung und -prüfung (BAM))

Computational modeling of fluid-structure interaction as well as multiphase fluid flow represent highly relevant approaches for insights into many engineering systems, but few works have thoroughly studied the combined effects from a numerical perspective. To-date approaches are either partitioned schemes [3] or fully Eulerian [2], limiting solver robustness or resolution of the fluid-solid interface. We present a first unified and monolithic finite element approach to multiphase fluid-structure interaction, where the flow is described by a coupled five-field Cahn-Hilliard Navier-Stokes equation system [1] in Arbitrary Lagrangian-Eulerian (ALE) description, and the structure is governed by finite strain elastodynamics. Unknowns of the resulting six-field system are fluid velocities, pressures, phase field, chemical potential, domain displacements, and structural deformation. Coupling of fluid and solid is achieved with a monolithic Neumann-Dirichlet scheme, where the structure is constrained by fluid kinematics and the fluid receives the reaction forces, circumventing the introduction of a Lagrange multiplier. Avenues for the effective solution of the resulting system are shown, and applications to elasto-capillarity and bubble-membrane interactions in electrolyzers are demonstrated.

# References
[1] Brunk, A. and ten Eikelder, M. F. P. (2026). A simple, fully-discrete, unconditionally energy-stable method for the two-phase Navier-Stokes Cahn-Hilliard model with arbitrary density ratios. Journal of Computational Physics, 548:114558. DOI: 10.1016/j.jcp.2025.114558

[2] Valizadeh, N., Zhuang, X., and Rabczuk, T. (2025). A monolithic finite element method for phase-field modeling of fully Eulerian fluid-structure interaction. Computer Methods in Applied Mechanics and Engineerings, 435:117618. DOI: 10.1016/j.cma.2024.117618

[3] Zheng, X. and Karniadakis, G. E. (2016). A phase-field/ALE method for simulating fluid-structure interactions in two-phase flow. Computer Methods in Applied Mechanics and Engineering, 309:19-40. DOI: 10.1016/j.cma.2016.04.035


