---
title: 'Data-integrated simulations of solute transport in the rodent brain using Fenicsx'
authors:
  - name:
      literal: 'Andreas Solheim'
    affiliations:
      - 'Numerical Analysis and Scientific Computing (SCAN) Simula Research Laboratory'
      - 'Department of Mathematics University of Oslo'
    email: 'solheim@simula.no'
  - name:
      literal: 'Björn Sigurdsson'
    affiliations:
      - 'Center for Translational Neuromedicine University of Copenhagen'
  - name:
      literal: 'Peter Bork'
    affiliations:
      - 'Center for Translational Neuromedicine University of Copenhagen'
  - name:
      literal: 'Maiken Nedergaard'
    affiliations:
      - 'Center for Translational Neuromedicine University of Copenhagen'
      - 'Center for Translational Neuromedicine University of Rochester Medical Center'
  - name:
      literal: 'Kent-Andre Mardal'
    affiliations:
      - 'Numerical Analysis and Scientific Computing (SCAN) Simula Research Laboratory'
      - 'Department of Mathematics University of Oslo'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Andreas Solheim (Simula)

The glymphatic theory describes the extra-vascular transport and clearance of solutes in the brain. This solute transport is mediated by a set of barriers which are only partially understood. In this work, we emphasize the role of the pia membrane, the interface between the brain parenchyma and the cerebrospinal fluid (CSF), in determining solute transport in brain tissue. We use finite element simulations using Fenicsx with previously published data of tracer injection in 8 rats recorded by Single-Photon Emission Computed Tomography (SPECT) (Sigurdsson et al 2022). Parameter sweeps are performed using a quasi-Monte Carlo approach to estimate transport properties of this tracer, validating model outcomes with data recorded experimentally. Simulations use experimental data on the boundary of the domain, and we explore how the formulation of the boundary condition changes the transport properties predicted by the model. We show how Fenicsx can be combined with experimental data to provide insight into biological models and potentially inform new experiments.

# References
Sigurdsson, et al., A spect-based method for dynamic imaging of the glymphatic system in

rats. J. Cereb. Blood Flow & Metab. 43, 1153-1165 (2023) PMID: 36809165.


