---
title: 'Z3ST: A FEniCSx Framework for Multiscale Thermo-Mechanical Analysis with Automatic Differentiation'
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

Z3ST is an open-source finite element framework built on FEniCSx. The framework provides an organized environment for coupled thermo-mechanical analysis with emphasis on differentiable constitutive modeling and inverse problem workflows, ranging from engineering-scale simulations to meso-scale phenomena. The framework couples thermal conduction, linear and nonlinear elasticity, hyperelasticity, phase-field fracture for material damage, macroscopic and crystal plasticity, and cluster dynamics through staggered schemes with adaptive relaxation. This demonstrates FEniCSx capability for production-level multiphysics codes across multiple length scales. Native support for UFL's differentiable architecture (Latyshev et al., 2025) underpins automated discovery of physics-informed constitutive laws through symbolic regression coupled with automatic differentiation (Flaschel et al., 2022).
From the software engineering perspective, Z3ST provides complete simulation setup through external YAML configuration files for reproducibility while supporting Python-based customizable material laws. The framework includes 30+ verification cases ranging from analytical benchmarks to advanced applications. Z3ST demonstrates best practices for building domain-specific applications on FEniCSx, including effective use of quadrature function spaces for history variables, nonlinear solvers with adaptive relaxation, and seamless integration with visualization pipelines.
Three relevant applications showcase Z3ST capabilities: (1) thermo-mechanical design-by-analysis applied to pressure vessel components, (2) microstructural analysis of over-pressurized bubbles in ceramics with intergranular fracture modeling, and (3) inverse parametric estimation for automated discovery of constitutive equations in irradiated materials (Frydrych, 2023). Code availability: https://github.com/giozu/z3st.

# References
Alnaes, M. S., Logg, A., Olgaard, K. B., Rognes, M. E., & Wells, G. N. (2014). Unified form language: A domain-specific language for weak formulations of partial differential equations. ACM Transactions on Mathematical Software, 40(2), Article 9. DOI: 10.1145/2566630

Baratta, I. A., Dean, J. P., Dokken, J. S., Habera, M., Hale, J. S., Richardson, C. N., Rognes, M. E., Scroggs, M. W., Sime, N., & Wells, G. N. (2023). DOLFINx: The next generation FEniCS problem solving environment. Zenodo. DOI: 10.5281/zenodo.10447666

Flaschel, M., Kumar, S., & De Lorenzis, L. (2022). Discovering plasticity models without stress data. npj Computational Materials, 8, 91. DOI: 10.1038/s41524-022-00752-4

Frydrych, K. (2023). Modelling irradiation effects in metallic materials using the crystal plasticity theory - A review. Crystals, 13(5), 771. DOI: 10.3390/cryst13050771

Latyshev, A., et al. (2025). Expressing general constitutive models in FEniCSx using external operators and algorithmic automatic differentiation. Journal of Theoretical, Computational and Applied Mechanics. DOI: 10.46298/jtcam.14449

Scroggs, M. W., Dokken, J. S., Richardson, C. N., & Wells, G. N. (2022). Construction of arbitrary order finite element degree-of-freedom maps on polygonal and polyhedral cell meshes. ACM Transactions on Mathematical Software, 48(2), Article 18. DOI: 10.1145/3524456


