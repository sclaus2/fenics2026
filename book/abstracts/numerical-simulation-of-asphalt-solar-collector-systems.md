---
title: 'Numerical simulation of asphalt solar collector systems'
authors:
  - name:
      literal: 'Lucía Escudero Sartages'
    affiliations:
      - 'Centre de Recerca Matematica'
    email: 'lescudero@crm.cat'
  - name:
      literal: 'David Romero Sanchez'
    affiliations:
      - 'Spain'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Poster

**Presenter:** Lucia Escudero Sartages (Centre de Recerca Matematica, Spain)

Urban pavements absorb large amounts of solar radiation, raising surface temperatures and intensifying the urban heat island effect. These conditions reduce urban comfort, accelerate pavement deterioration, and increase cooling energy demand in surrounding buildings. To address these challenges, previous research has explored technologies to harness stored pavement heat, including geothermal paving systems and hybrid photovoltaic-thermal pavements. Nevertheless, challenges remain related to long-term pavement durability, climatic variability, and the optimisation of collector geometry and material properties.
The ENHANCE Europe project investigates an innovative solution based on asphalt solar collectors embedded within flexible pavement structures. The system aims to recover excess heat stored in the pavement and convert it into a usable thermal resource for nearby buildings, reducing fossil-fuel consumption, lowering operational energy costs, and enhancing the resilience of urban energy systems.
Within this framework, the present work introduces a finite-element numerical model for simulating coupled heat transfer and fluid flow in multilayer pavements with embedded collector networks. The model solves the incompressible Navier-Stokes and transient heat equations using an Incremental Pressure Correction Scheme. The simulations are implemented in DOLFINx, while the computational domain and mesh are generated using Gmsh. The model provides temperature distributions at critical pavement depths, quantifies heat extraction efficiency, and evaluates system performance under varying environmental and operational conditions.
The numerical results support informed design and construction decisions, enabling the optimisation of system geometry, material selection, and operating strategies. Future work will focus on model refinement using experimental data from four European living labs, contributing to digital and data-driven tools that support the urban energy transition.

# References
Bobes-Jesús, V., Pascual-Muñoz, P., Castro-Fresno, D., & Rodríguez-Hernández, J. (2013). Asphalt solar collectors: A literature review. Applied Energy, 102, 962-970. DOI: 10.1016/j.apenergy.2012.08.050

Qin, Y., & Hiller, J. E. (2014). Understanding pavement-surface energy balance and its implications on cool pavement development. Energy and Buildings, 85, 389-399. DOI: 10.1016/j.enbuild.2014.09.076

Dokken, J. S., Johansson, A., Massing, A. & Funke, S.W. (2020). A multimesh finite element method for the Navier-Stokes equations based on projection methods. Computer Methods in Applied Mechanics and Engineering, 368, 113129. DOI: 10.1016/j.cma.2020.113129


