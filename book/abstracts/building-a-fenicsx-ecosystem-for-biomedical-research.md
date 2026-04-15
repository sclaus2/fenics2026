---
title: 'Building a FEniCSx Ecosystem for Biomedical Research'
authors:
  - name:
      literal: 'Henrik Finsberg'
    affiliations:
      - 'Department of Computational Physiology, Simula Research Laboratory, Oslo, Norway'
      - 'K.G. Jebsen Center for Brain Fluid Research, University of Oslo, Oslo, Norway'
    email: 'henriknf@simula.no'
  - name:
      literal: 'Jørgen S. Dokken'
    affiliations:
      - 'Department of Numerical Analysis and Scientific Computing, Simula Research Laboratory, Oslo, Norway'
  - name:
      literal: 'Cécile Daversin-Catty'
    affiliations:
      - 'Department of Numerical Analysis and Scientific Computing, Simula Research Laboratory, Oslo, Norway'
      - 'K.G. Jebsen Center for Brain Fluid Research, University of Oslo, Oslo, Norway'
  - name:
      literal: 'Marie E. Rognes'
    affiliations:
      - 'Department of Numerical Analysis and Scientific Computing, Simula Research Laboratory, Oslo, Norway'
      - 'K.G. Jebsen Center for Brain Fluid Research, University of Oslo, Oslo, Norway'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Henrik Finsberg (Simula Research Laboratory)

Translating physiological processes into predictive models requires robust and performant software pipelines. While DOLFINx offers a high-performance finite element backend, applying it to complex biomedical domains means bridging the gap between raw clinical data, specialized physical models, and scalable solvers. In this talk, we present a modular ecosystem of open-source FEniCSx-based tools designed to streamline workflows in brain and cardiac modelling.

For brain modelling, a major challenge is seamlessly integrating clinical imaging data into the finite element pipeline. We introduce MRI-toolkit, a specialized tool for converting MRI sequences into simulation-ready inputs, such as spatially varying concentration maps. We also discuss efficient strategies using wildmeshing and pyvista to generate high-quality computational meshes directly from medical image segmentations, bridging voxel data and FEniCSx-ready unstructured grids.

In cardiac modelling, we present a comprehensive suite of interoperable packages targeting various scales and physics. At the cellular level, gotranx facilitates the generation of ODE code for single-cell models. At the tissue and organ level, fenicsx-beat provides robust solvers for cardiac electrophysiology, while fenicsx-pulse simulates nonlinear cardiac mechanics. To support these models, we introduce cardiac-geometriesx for generating parametrised cardiac geometries, fenicsx-ldrb for assigning realistic myocardial fiber architectures, and circulation for coupling 3D finite element models to 0D lumped-parameter networks.

Finally, we share critical lessons learned from developing and maintaining this scientific software ecosystem, discussing our approaches to automated testing, package distribution (PyPI/Conda/Spack), and creating user-friendly documentation.

# References
[1] MRI-toolkit, https://github.com/scientificcomputing/mri-toolkit

[2] PyVista, https://github.com/pyvista/pyvista

[3] gotranx, https://github.com/finsberg/gotranx

[4] ap features, https://github.com/ComputationalPhysiology/ap_features

[5] fenicsx-beat, https://github.com/finsberg/fenicsx-beat

[6] fenicsx-pulse, https://github.com/finsberg/fenicsx-pulse

[7] cardiac-geometriesx, https://github.com/ComputationalPhysiology/cardiac-geometriesx

[8] fenicsx-ldrb, https://github.com/finsberg/fenicsx-ldrb

[9] circulation, https://github.com/ComputationalPhysiology/circulation


