---
title: 'In-silico drug delivery in the human brain'
authors:
  - name:
      literal: 'Cécile Daversin Catty'
    affiliations:
      - 'Simula Research Laboratory (Oslo, Norway) and K.G. Jebsen Center for Brain Fluid Research (Oslo, Norway)'
    email: 'cecile@simula.no'
  - name:
      literal: 'Marius Causemann'
    affiliations:
      - 'Simula Research Laboratory (Oslo, Norway)'
  - name:
      literal: 'Marie E. Rognes'
    affiliations:
      - 'Simula Research Laboratory (Oslo, Norway) and K.G. Jebsen Center for Brain Fluid Research (Oslo, Norway)'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Cécile Daversin Catty (Simula Research Laboratory)

Characterizing brain fluid dynamics and solute transport is a key ingredient in refining treatment delivery for neurological diseases. Despite extensive research, the underlying mechanisms are still subject to debate, and drug dosages are not yet tailored at the individual level. Biomedical computational models represent an innovative shift towards personalized adjustment of therapeutic dosage. These models must address the complexity and multi-scale aspect of the brain, and account for the large variability between individuals. Yet, this approach raises multiple challenges with respect to patient-specific parameterization, multiphysics coupling, and computational cost.

An inherent challenge lies in the processing and analysis of raw MRI data [1], as well as the subsequent generation of anatomically accurate, personalized meshes [2, 3]. We showcase a pipeline capable of generating FEniCSx-ready personalized meshes, delineating the critical stages of the workflow. Drug delivery predictions based on these meshes are derived from a 3D transport model, governed by an advection-diffusion equation and coupled with a Stokes model predicting the cerebrospinal fluid flow [4]. We present patient-specific simulations, with particular emphasis on comparison against MRI-derived quantities of interest.

# References
[1] MRI-toolkit, https://github.com/scientificcomputing/mri-toolkit

[2] WildMeshing, https://github.com/wildmeshing

[3] PyVista, https://github.com/pyvista/pyvista

[4] Marius Causemann et al. (2025) In-silico molecular enrichment and clearance of the human intracranial space. https://www.biorxiv.org/content/10.1101/2025.01.30.635680v1


