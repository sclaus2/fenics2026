---
title: 'FESTIM v2.0: Upgraded framework for multi-species hydrogen transport'
authors:
  - name:
      literal: 'Remi Delaporte-Mathurin'
    affiliations:
      - 'MIT PSFC'
    email: 'remidm@mit.edu'
  - name:
      literal: 'James Dark'
    affiliations:
      - 'MIT PSFC'
  - name:
      literal: 'J\o rgen S. Dokken'
    affiliations:
      - 'Simula'
  - name:
      literal: 'Kaelyn Dunnell'
    affiliations:
      - 'MIT PSFC'
  - name:
      literal: 'Chirag Khurana'
    affiliations:
      - 'MIT PSFC'
  - name:
      literal: 'Huihua Yang'
    affiliations:
      - 'MIT PSFC'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Remi Delaporte-Mathurin (Massachusetts Institute of Technology, Plasma Science and Fusion Center)

FESTIM is an open-source finite element code for modelling hydrogen isotope transport in materials and fluids, developed for applications in nuclear fusion technology. Built on the FEniCS/FEniCSx framework, FESTIM enables the simulation of coupled diffusion-reaction processes including trapping, surface recombination, permeation, and multi-material transport, which are central to predicting tritium inventories and losses in fusion systems.

While FEniCS provides a powerful and flexible environment for finite element modelling, developing application-specific models from scratch can be demanding for users who are not specialists in the finite element method. FESTIM addresses this challenge by providing a high-level, domain-specific abstraction layer that allows users to define complex tritium transport problems through a simplified, physics-oriented interface, while retaining the robustness and performance of the underlying FEniCS ecosystem.

This presentation will provide an overview of the FESTIM project and its role in supporting the design and safety assessment of fusion fuel cycle components. We will illustrate how the FEniCS-based implementation enables flexible multiphysics modelling and scalable simulations across a wide range of geometries and material configurations. Application examples will be presented for key elements of the fusion fuel cycle, including breeding blankets, plasma-facing components (first wall), heat exchangers, tritium extraction systems, and isotope separation units.

A short live demonstration will highlight the user workflow, from problem definition to post-processing, and showcase recent developments based on FEniCSx. The talk will also discuss current challenges, performance considerations, and opportunities for further FEniCS community contributions.

# References
10.1016/j.ijhydene.2026.153987


