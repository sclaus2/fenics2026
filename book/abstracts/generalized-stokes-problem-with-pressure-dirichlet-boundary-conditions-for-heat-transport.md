---
title: 'Generalized Stokes problem with pressure Dirichlet boundary conditions for heat transport'
authors:
  - name:
      literal: 'Juan José Seoane'
    affiliations:
      - 'Universitat Autònoma de Barcelona'
  - name:
      literal: 'Xavier Oriols'
    affiliations:
      - 'Universitat Autònoma de Barcelona'
  - name:
      literal: 'Xavier Cartoixà'
    affiliations:
      - 'Universitat Autònoma de Barcelona'
    email: 'Xavier.Cartoixa@uab.es'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Xavier Cartoixà (Universitat Autònoma de Barcelona)

The Boltzmann Transport Equation (BTE) describes semiclassical transport by charge and heat carriers: electrons and phonons, respectively. After some manipulations and approximations, the BTE naturally yields Ohm's law and diffusion effects for electrons, and Fourier's law in the case of phonons. If some of the approximations are relaxed, it was shown by Guyer and Krumhansl that there appear some extra terms in Fourier's law which endow the heat flux with viscous properties. These "phonon hydrodynamics" effects manifest typically in the nanoscale, and with geometries where the flux lines are expected to have a curvature radius of the order of a hydrodynamic length.
Mathematically, the steady-state Guyer-Krumhansl (GK) equations are analogous to the Generalized Stokes Problem (GSP) for an uncompressible fluid, with the temperature playing the role of the pressure, and the heat flux playing the role of the velocity field. The notable difference is that, while in the GSP the boundary conditions (BCs) are rarely expressed in terms of the pressure, in the GK equations it is natural to fix the temperature at, typically, hot and cold contacts, with the rest of the boundary under no- or partial-slip BCs.
We will report our experience solving the GK equations with FEniCSx, successfully implementing weak forms of the pressure Dirichlet BC with the Nitsche method in the case of Poiseuille flow, where the velocity/heat flux is guaranteed to exit and reach the contacts orthogonally to the contact surface. However, more complicated geometries with the heat flux possibly exiting/arriving at the contact at an angle do not seem to lend themselves naturally to symmetric forms, leaving us with a nonsymmetric formulation. We will discuss uniqueness and stability considerations in this setting.
We acknowledge financial support by Spain's Ministerio de Ciencia, Innovación e Universidades under project No. PID2024-161603NB-I00 (MICIU / AEI / 10.13039/501100011033 / FEDER, UE).


