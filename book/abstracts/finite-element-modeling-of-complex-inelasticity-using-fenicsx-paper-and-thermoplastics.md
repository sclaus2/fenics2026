---
title: 'Finite-Element Modeling of Complex Inelasticity Using FEniCSx: Paper and Thermoplastics'
authors:
  - name:
      literal: 'Nadir Kopic-Osmanovic'
    affiliations:
      - 'same as corresponding author'
  - name:
      literal: 'Tiansheng Liu'
    affiliations:
      - 'same as corresponding author'
  - name:
      literal: 'Jaan-Willem Simon'
    affiliations:
      - 'same as corresponding author'
  - name:
      literal: 'Johannes Neumann'
    affiliations:
      - 'same as corresponding author'
    email: 'johannes.neumann@uni-wuppertal.de'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Johannes Neumann (Computational Applied Mechanics, University of Wuppertal, Pauluskirchstraße 7, 42285 Wuppertal, Germany)

Predicting the mechanical response of materials such as paper and thermoplastics is crucial for a wide range of applications, from sustainable to high-performance. Despite their different origins, both exhibit nonlinear behaviors under large deformations that challenge conventional computational frameworks. This work presents constitutive models for simulating their inelastic and coupled thermomechanical responses, implemented in FEniCSx.

For paper, an advanced large-deformation elasto-plastic model was developed to capture anisotropic behavior. The formulation distinguishes between in-plane and out-of-plane responses in the free energy and yield surface, reflecting the layered architecture of paper. Refinements address inconsistencies in initial yield and plastic strain ratios, while stiffness evolution due to densification during compression is included. Anisotropic hardening is modeled via coupled internal variables governing yield surface evolution.

For semi-crystalline thermoplastics, a visco-hyperelastic-plastic framework is introduced to describe the interaction between deformation, microstructure, and temperature. Based on a two-potential formulation, it ensures thermodynamic consistency while enabling viscoelastic relaxation, plastic flow, and thermal coupling. Crystallinity-dependent stiffening and self-heating effects capture temperature-driven transitions during loading. Both models are formulated using a specific intermediate configuration, offering physical clarity and algorithmic advantages.

The implementations rely on FEMExternalOperators and JAX for local solution schemes and automatic differentiation of consistent tangents; for thermoplastics, CUDA-based vectorization yields substantial speedups. Numerical studies confirm robustness and predictive capability. Overall, these developments highlight how FEniCSx supports rapid, reproducible modeling of complex inelastic materials within a unified open-source finite element environment.

# References
- Cui, J., Liu, T., Valsecchi, M., Giersberg, M., Çelik, H., Simon, J.-W., Kumar, S., Petersen, J., & Fish, J. (2025). Thermodynamically consistent coupled chemo-thermo-mechanical model of interfaces in overmolded thermoplastic parts. Computer Methods in Applied Mechanics and Engineering, 447, 118359. DOI: 10.1016/j.cma.2024.118359

- Felder, S., Holthusen, H., Hesseler, S., Pohlkemper, F., Gries, T., Simon, J.-W., & Reese, S. (2020). Incorporating crystallinity distributions into a thermo-mechanically coupled constitutive model for semi-crystalline polymers. International Journal of Plasticity, 135, 102751. DOI: 10.1016/j.ijplas.2020.102751

- Holthusen, H., Rothkranz, C., Lamm, L., Brepols, T., & Reese, S. (2023). Inelastic material formulations based on a co-rotated intermediate configuration: Application to bioengineered tissues. Journal of the Mechanics and Physics of Solids, 172, 105174. Elsevier BV. DOI: 10.1016/j.jmps.2023.105174

- Kopic-Osmanovic, N., Prume, E., Felder, S., Kloppenburg, G., & Simon, J.-W. (2023). Modeling the anisotropic elasto-plastic material behavior of paper and paperboard at finite deformations. Conference Proceedings, 22, e202200293.

- Latyshev, A., Bleyer, J., Maurini, C., & Hale, J. (2025, October 8). Expressing general constitutive models in FEniCSx using external operators and algorithmic automatic differentiation. Journal of Theoretical, Computational and Applied Mechanics. Centre pour la Communication Scientifique Directe (CCSD). DOI: 10.46298/jtcam.14449

- Liu, T., Cui, J., Kantert, A., Tabib, M., Kopic, N., Valsecchi, M., Kumar, S. K., Fish, J., & Simon, J.-W. (submitted). Thermomechanically coupled visco-hyperelastic-plastic model with self-heating for thermoplastics.


