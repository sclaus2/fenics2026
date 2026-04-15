---
title: 'Can we predict stress fields without models? Recent adventures of ddfenicsx for Data-driven Identification'
authors:
  - name:
      literal: 'Felipe Rocha'
    affiliations:
      - 'Université Paris-Est Créteil'
    email: 'felipe.figueredo-rocha@u-pec.fr'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Felipe Rocha (MSME - Université Paris-Est Créteil)

Conservation laws are fundamental to physical modelling in electromagnetism, solid mechanics, and fluid dynamics. While the associated PDEs are universal, they require constitutive models -- relating flux-gradient pairs (e.g., stress-strain) -- to close the system. However, such models are not unique and often introduce assumptions that may bias predictions.
Data-Driven Computational Mechanics (DDCM) [1] offers a paradigm shift: instead of assuming a constitutive law, it directly integrates discrete material data into the solution process. By reformulating the classical PDE problem as a mixed-integer minimisation, DDCM identifies mechanical states that satisfy equilibrium and kinematic compatibility while remaining closest to a dataset of stress-strain pairs. By operating directly on raw data, DDCM provides an alternative modeling route to both classical constitutive modeling and ML-based surrogates [2]. One interesting application of this approach lies in the intersection of experimental and computational mechanics, allowing stress field identification without explicit postulating a parametric constitutive model, the so-called Data-Driven Identification (DDI) method [3]. 
This presentation shows recent advances of ddfenicsx [4], a library embedding DDCM within the FEniCSx ecosystem, preserving a familiar UFL-based workflow. Previous applications include coupled computational homogenisation [5], conservative mixed formulations for Darcy flow [6], and finite-strain problems [2], showcasing its versatility.
In this talk, we focus on a new application of ddfenicsx to DDI using full-field displacement data, along with recent framework improvements: I) migration from legacy FeniCSs to FEniCSx (0.10) ; ii) non-intrusive operation mode; iii) algorithmic enhancements such as the Accelerated Projection-to-Equilibrium [5] and Locally Convex Reconstruction [7] for noisy datasets and v) on-the-fly database generation [5].

# References
[1] Kirchdoerfer, T., & Ortiz, M. (2016). Data-driven computational mechanics. Computer Methods in Applied Mechanics and Engineering, 304, 81-101. DOI: 10.1016/j.cma.2016.02.001

[2] Zlatic, M., Rocha, F., Stainier, L., & Canadija, M. (2024). Data-driven methods for computational mechanics: A fair comparison between neural networks based and model-free approaches. Computer Methods in Applied Mechanics and Engineering, 431, 117289. DOI: 10.1016/j.cma.2024.117289

[3] Leygue, A., Seghir, R., Réthoré, J., Tinnes, J.-P., & Coret, M. (2019). Non-parametric material state field extraction from full field measurements. Computational Mechanics, 64, 501-509. DOI: 10.1007/s00466-019-01725-z

[4] Rocha, F. (2023-). ddfenics: A FEniCS(x)-based (model-free) data-driven computational mechanics implementation [Software]. Zenodo. DOI: 10.5281/zenodo.7646226

[5] Rocha, F., Platzer, A., Leygue, A., & Stainier, L. (2025). On-the-fly adaptive sampling strategy for data-driven computational mechanics: Applications to computational homogenisation. Mechanics of Materials, 207, 105382. DOI: 10.1016/j.mechmat.2025.105382

[6] Rocha, F., Quinelato, T., & Stainier, L. (2024). Some experiences in mixed finite element formulations for (model-free) data-driven computational mechanics. In Proceedings of the 16ème Colloque National en Calcul de Structures (CSMA 2024). CNRS; CSMA. https://hal.science/hal-04611046

[7] He, Q., & Chen, J. S. (2020). A physics-constrained data-driven approach based on locally convex reconstruction for noisy database. Computer Methods in Applied Mechanics and Engineering, 363, 112791. DOI: 10.1016/j.cma.2019.112791


