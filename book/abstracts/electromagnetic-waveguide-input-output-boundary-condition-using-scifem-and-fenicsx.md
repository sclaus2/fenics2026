---
title: 'Electromagnetic Waveguide Input/Output Boundary Condition using SciFEM and FEniCSx'
authors:
  - name:
      literal: 'G. William Slade'
    affiliations:
      - 'Independent'
    email: 'slade_bill@hotmail.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** G. William Slade (Independent)

The ability to simulate the introduction and absorption of electromagnetic power at waveguide port boundaries is a fundamental challenge of computational electromagnetics.  From the results of the internal Maxwell problem, this boundary model is used to compute a set of scattering parameters that define the performance of a microwave device.  We approach the problem by augmenting the internal electromagnetic field problem (solved using the FEniCSx suite) with a boundary operator that models the exterior waveguide problem using a mode-matching approach.  In order to construct this boundary operator, we use the SciFEM [1] real space facility to construct the required modal projection operators on the waveguide port boundaries.  We cover the derivation and implementation of the method and describe how, in most cases, the sparseness of the finite element matrix operator is not noticeably degraded.  Moreover, the boundary operator implementation directly yields the scattering parameters between ports and modes.  Some illustrative examples are presented to demonstrate the efficacy of the method, as well as a comparison with a simpler, but less general impedance boundary condition method that we have long used [2].  We also briefly discuss how one might go about automatically generating the mode functions required by this method as well as linking this approach to the modeling of general open-region problems.

# References
[1]Henrik Finsberg, & Jørgen Schartum Dokken. (2024). scientificcomputing/scifem: v0.2.2 (Version v0.2.2) [Computer software]. scientificcomputing/scifem: v0.2.2

[2] G. W. Slade, "Solving the Time-Harmonic MaxwellEquations in 3-D Using the FEniCSx FiniteElement Package", Available at Researchgate-- https://www.researchgate.net/publication/367450648_Solving_the_Time-Harmonic_Maxwell_Equations_in_3-D_Using_the_FEniCSx_Finite_Element_Package_-_2023_Update


