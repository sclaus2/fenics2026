---
title: 'Live Demonstration of Z3ST: A FEniCSx Framework for Multiscale Thermo-Mechanical Analysis with Automatic Differentiation'
authors:
  - name:
      literal: 'Giovanni Zullo'
    affiliations:
      - 'Politecnico di Milano, Department of Energy, Nuclear Engineering Division, Via La Masa 34, Milan 20156, Italy'
    email: 'giovanni.zullo@polimi.it'
  - name:
      literal: 'Giovanni Nicodemo'
    affiliations:
      - 'Politecnico di Milano, Department of Energy, Nuclear Engineering Division, Via La Masa 34, Milan 20156, Italy'
  - name:
      literal: 'Elisa Cappellari'
    affiliations:
      - 'Politecnico di Milano, Department of Energy, Nuclear Engineering Division, Via La Masa 34, Milan 20156, Italy'
  - name:
      literal: 'Davide Pizzocri'
    affiliations:
      - 'Politecnico di Milano, Department of Energy, Nuclear Engineering Division, Via La Masa 34, Milan 20156, Italy'
  - name:
      literal: 'Lelio Luzzi'
    affiliations:
      - 'Politecnico di Milano, Department of Energy, Nuclear Engineering Division, Via La Masa 34, Milan 20156, Italy'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Giovanni Zullo (Politecnico di Milano)

This software demonstration showcases Z3ST, an open-source framework for multiphysics thermo-mechanical simulations with automatic differentiation, built on FEniCSx (Baratta et al., 2023; Scroggs et al., 2022). The demonstration focuses on crystal plasticity and automated constitutive law discovery, highlighting how UFL symbolic differentiation (Alnaes et al., 2014; Latyshev et al., 2025) enables rapid development of complex material models.
The demonstration walks through a single-crystal viscoplastic deformation simulation under uniaxial loading, showing how automatic differentiation eliminates manual Jacobian derivation with good convergence properties. The implementation includes FCC slip systems with power-law kinetics and history variables managed through quadrature function spaces.
A second highlight is automated discovery of constitutive laws (Flaschel et al., 2022). The demonstration shows how gradients computed via automatic differentiation enable training interpretable material models from data, bridging machine learning and computational mechanics for irradiated materials (Frydrych, 2023).
The practical workflow is demonstrated: YAML-based simulation setup, custom constitutive laws defined as Python functions with automatic differentiation, convergence monitoring, and visualization using PyVista. Pre-computed results illustrate broader capabilities including thermo-mechanical design-by-analysis for pressure vessels and microstructural analysis of over-pressurized bubbles with phase-field fracture. All code is open-source with 30+ verification cases. Code availability: https://github.com/giozu/z3st.

# References
Alnaes, M. S., Logg, A., Olgaard, K. B., Rognes, M. E., & Wells, G. N. (2014). Unified form language: A domain-specific language for weak formulations of partial differential equations. ACM Transactions on Mathematical Software, 40(2). DOI: 10.1145/2566630

Baratta, I. A., Dean, J. P., Dokken, J. S., Habera, M., Hale, J. S., Richardson, C. N., Rognes, M. E., Scroggs, M. W., Sime, N., & Wells, G. N. (2023). DOLFINx: The next generation FEniCS problem solving environment. Zenodo. DOI: 10.5281/zenodo.10447666

Flaschel, M., Kumar, S., & De Lorenzis, L. (2022). Discovering plasticity models without stress data. npj Computational Materials, 8, 91. DOI: 10.1038/s41524-022-00752-4

Frydrych, K. (2023). Modelling irradiation effects in metallic materials using the crystal plasticity theory - A review. Crystals, 13(5), 771. DOI: 10.3390/cryst13050771

Latyshev, A., et al. (2025). Expressing general constitutive models in FEniCSx using external operators and algorithmic automatic differentiation. Journal of Theoretical, Computational and Applied Mechanics. DOI: 10.46298/jtcam.14449

Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of arbitrary order finite element degree-of-freedom maps on polygonal and polyhedral cell meshes. ACM Transactions on Mathematical Software, 48(2), Article 18. DOI: 10.1145/3524456


