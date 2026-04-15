---
title: 'Finite-Pressure Anisotropic Hyperelasticity in FEniCSx: A Phenomenological Approach for Shock Physics'
authors:
  - name:
      literal: 'Paul Bouteiller'
    affiliations:
      - 'CEA DAM'
    email: 'paul.bouteiller99@gmail.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Paul Bouteiller (CEA)

We present a finite-strain anisotropic hyperelastic model suited to materials
subjected to high-amplitude shock loading, where hydrostatic pressures far
exceed deviatoric stresses. The formulation relies on a multiplicative
decomposition of the deformation gradient, separating the pressure-induced
lattice distortion from the residual isochoric distortion. The Helmholtz free
energy is then expanded as a quadratic form in the intermediate Green-Lagrange
strain, cleanly decoupling three independently calibrated contributions: the
equation of state, the geometric lattice distortion, and the pressure-dependent
isochoric stiffness tensor. Each component can be identified directly from DFT
calculations, molecular dynamics simulations, or Diamond Anvil Cell
experiments. The model naturally covers all crystallographic symmetry classes
from cubic to triclinic through a gauge freedom in the isochoric stiffness.

The constitutive law is implemented in the open-source code CHARON
(https://github.com/PaulBouteiller/Charon), built on FEniCSx. The total
Lagrangian formulation and the UFL automatic differentiation framework allow
the free energy to be transcribed almost directly from its mathematical
expression, yielding both the stress and the consistent tangent without any
additional derivation effort from the user.

Validation is carried out on cubic copper, tetragonal PETN, orthorhombic
alpha-RDX. Polycrystal homogenisation on 500-grain
meshes generated with NEPER accurately reproduces the pressure dependence of
the macroscopic shear modulus.


