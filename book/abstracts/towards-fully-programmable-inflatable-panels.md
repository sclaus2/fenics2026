---
title: 'Towards fully programmable inflatable panels'
authors:
  - name:
      literal: 'Ofir Mirkin'
    affiliations:
      - 'CNRS - LIPhy - Université Grenoble Alpes'
    email: 'ofir.mirkin@inria.fr'
  - name:
      literal: 'Mélina Skouras'
    affiliations:
      - 'INRIA - Université Grenoble Alpes'
  - name:
      literal: 'Emmanuel Siéfert'
    affiliations:
      - 'CNRS - LIPhy - Université Grenoble Alpes'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Ofir Mirkin (CNRS - LIPhy)

Self-deployable materials are expected to have wide application potential, e.g., in robotics, medicine, and architecture. So far, all responsive materials have limited deformation possibilities, and researchers lack control over the six local degrees of freedom (three for the metric and three for the curvature). Here, we introduce a strategy to address this limitation.

We investigate how variations in mesoscale properties and applied pressure influence the deformation of inflatable elastic architected materials. Our structures feature a triangular network of interconnected cylindrical cavities, and we study how their density, eccentricity, and orientation control the in-plane deformation. 
To program out-of-plane curvature, we superimpose two layers with distinct cavity geometries, achieving a 2D generalization of the bilayer effect.

The design and analysis of these structures are driven by a computational framework implemented in FEniCSx. We leverage the library to perform periodic homogenization and simulate the non-linear hyperelastic behavior of the underlying incompressible elastomers.
This high-fidelity numerical pipeline allows us to efficiently explore a vast design space of cavity geometries, that we then compare with experimental data.

This work paves the way for the inverse design of inflatable structures with fully programmable intermediate configurations and mechanical properties.


