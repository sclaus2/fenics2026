---
title: 'Thermoviscous Acoustic Modeling of Helmholtz-Resonator-Based Metamaterials with FEniCSx'
authors:
  - name:
      literal: 'Elio Di Giulio'
    affiliations:
      - 'Industrial Engineering Department University of Naples Federico II'
    email: 'elio.digiulio@unina.it'
  - name:
      literal: 'Raffaele Dragonetti'
    affiliations:
      - 'Industrial Engineering Department University of Naples Federico II'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Elio Di Giulio (Industrial Engineering Department University of Naples Federico II)

Acoustic metamaterials often rely on complex geometries characterized by resonant microcavities, where viscous and thermal dissipation significantly influence wave propagation. Accurate prediction of these effects requires models that go beyond classical lossless acoustics and account for thermoviscous phenomena.

This work presents a finite element implementation of thermoviscous acoustics based on the frequency-domain linearized Navier-Stokes equations (FLNS), developed using the FEniCSx framework. The solver resolves the coupled velocity, pressure, and temperature fields, enabling the simulation of viscous and thermal boundary layer effects in confined fluid domains.

The numerical formulation is first validated through analytical-numerical benchmarks based on the classical thermoviscous solutions proposed by Stinson for sound propagation in cylindrical ducts, representing simple pore-like geometries.

The approach is then applied to the simulation of Helmholtz-resonator-based acoustic metamaterials. Numerical predictions of acoustic quantities such as surface impedance, reflection coefficient, and absorption are compared with experimental measurements, demonstrating the capability of the proposed model to accurately capture dissipative effects in resonant metamaterial structures.


