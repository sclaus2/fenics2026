---
title: 'Inferring Human Intracranial CSF Absorption Sites via Inverse Modelling of Protein Transport'
authors:
  - name:
      literal: 'Marius Causemann'
    affiliations:
      - 'Simula Research Laboratory'
    email: 'mariusca@simula.no'
  - name:
      literal: 'Kent-Andre Mardal'
    affiliations:
      - 'Simula Research Laboratory'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Marius Causemann (Simula Research Laboratory)

The clearance of metabolic waste products and the distribution of therapeutic agents within the central nervous system are critically dependent on the circulation of cerebrospinal fluid (CSF). However, the precise anatomical locations of CSF production and absorption in the human brain remain subjects of ongoing investigation. 

Recent clinical research [Storås et al. 2025] and open tracer evolution datasets [Riseth et al. 2026] utilized high-resolution T1 mapping (R1) to demonstrate significant regional solute gradients in the CSF of healthy brains, where R1 in the subarachnoid space (SAS) correlates strongly with intrinsic protein concentration. These findings suggest that quantitative R1 maps can serve as a reliable, non-invasive proxy for protein distribution within the human intracranial space.

Building on this physiological insight, we present a computational framework to infer CSF absorption pathways by integrating mathematical modeling with clinically acquired R1 imaging data. We model the transport of proteins within the CSF-filled spaces using a coupled fluid flow and mass transport model. First, we generate a set of basis velocity fields by solving the steady-state Stokes equations, where each field represents a distinct hypothesis for a specific absorption site. Second, we model the transport of proteins using a stationary advection-diffusion equation driven by a linear combination of these basis fields.

To identify the active absorption sites, we formulate the inverse problem as a PDE-constrained optimization. We define a objective function that minimizes the mismatch between the computed equilibrium protein concentration and the measured R1 data field. By solving for the optimal combination of basis flows that best reproduces the observed protein gradients, this approach provides a mathematical tool for non-invasively characterizing intracranial fluid dynamics and validating physiological transport hypotheses.

# References
Storås, Tryggve Holck, et al. "T2-Weighted T1 Mapping and Automated Segmentation of CSF: Assessment of Solute Gradients in the Healthy Brain." Journal of Magnetic Resonance Imaging (2025).

Riseth, Jørgen N., et al. "Human brain MRI data of intrathecally injected tracer evolution over 72 hours for data-integrated simulations." Scientific Data (2026).


