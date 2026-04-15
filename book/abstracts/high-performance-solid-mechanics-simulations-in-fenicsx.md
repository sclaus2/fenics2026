---
title: 'High-performance solid mechanics simulations in FEniCSx'
authors:
  - name:
      literal: 'Musa Choudhury'
    affiliations:
      - 'University of Cambridge'
    email: 'mmc83@cam.ac.uk'
  - name:
      literal: 'Garth Wells'
    affiliations:
      - 'University of Cambridge'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Musa Choudhury (University of Cambridge)

There is increasing demand for high-performance, nonlinear solid mechanics solvers, with simulations of component systems now being routinely three-dimensional and larger in scale. Previously we demonstrated a high-performance solid mechanics library in DOLFINx interfacing Abaqus style UMAT subroutines which are standardly used for writing constitutive algorithms. This capability allows us to run complex constitutive algorithms such as crystal plasticity models on massively scalable HPC hardware. A significant bottleneck becomes the memory required to deploy these models. We also demonstrated the performance gains when using an O(n) iterative solver as opposed to O(n^2) direct solver as is commonly used in industry. The problem now becomes ensuring that the iterative solver converges for the class of problems we are interested in. To overcome this, efficient and robust preconditioning techniques need to be developed. We analyse the algebraic multigrid preconditioner with the conjugate gradient method for solid mechanics problems including plasticity. We will then present ways to improve its performance to achieve a robust solver with respect to mesh refinement and material parameters.


