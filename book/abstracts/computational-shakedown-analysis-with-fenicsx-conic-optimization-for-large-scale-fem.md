---
title: 'Computational Shakedown Analysis with FEniCSx: Conic Optimization for Large-Scale FEM'
authors:
  - name:
      literal: 'Lavakumar Veludandi'
    affiliations:
      - 'Computational Applied Mechanics (University of Wuppertal)'
    email: 'lavakumar.veludandi@uni-wuppertal.de'
  - name:
      literal: 'Reza Vafadari'
    affiliations:
      - 'Computational Applied Mechanics (University of Wuppertal)'
  - name:
      literal: 'Lilian Aurora Ochoa'
    affiliations:
      - 'Computational Applied Mechanics (University of Wuppertal)'
  - name:
      literal: 'Jaan-Willem Simon'
    affiliations:
      - 'Computational Applied Mechanics (University of Wuppertal)'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Lavakumar Veludandi (Computational Applied Mechanics, University of Wuppertal)

Shakedown analysis offers a robust framework for assessing the long-term structural integrity of materials under variable loading. Classical lower-bound approaches, based on Melan's Theorem, formulate this as a constrained optimization problem to determine the maximum safe load multiplier while satisfying equilibrium and yield criteria. However, discretizing these continuous variational inequalities into tractable large-scale finite element models remains computationally challenging due to the enormous number of resulting discrete constraints.

We present a modular, extensible computational framework for lower-bound shakedown analysis integrated natively within the FEniCSx ecosystem. This framework couples FE formulations with large-scale conic optimization. By leveraging the low-level assembly capabilities of FEniCSx, the approach maintains explicit control over constraint sparsity, enabling the construction of large block-sparse matrices suitable for high-resolution discretizations. The framework provides a flexible solver interface allowing users to select from high-performance backends like MOSEK or Gurobi, or integrate custom solvers, which facilitates direct result comparison and adaptable solution strategies while preserving the automation and versatility of the FEniCSx workflow.

Validation against benchmark problems confirms the accuracy and robustness of the proposed framework. The methodology is further applied to structures exhibiting heterogeneous and anisotropic material behavior under multidimensional loading. The approach efficiently computes structural shakedown limits and demonstrates the potential of combining automated finite element frameworks with advanced conic optimization for scalable structural limit analysis across diverse material systems.

# References
François, A., Abdelkader, H., An, L. T. H., Said, M., & Tao, P. D. (2007). Application of lower bound direct method to engineering structures. Journal of Global Optimization, 37(4), 609-630. DOI: 10.1007/s10898-006-9069-1;

Simon, J.-W., & Weichert, D. (2011). Numerical lower bound shakedown analysis of engineering structures. Computer Methods in Applied Mechanics and Engineering, 200(41-44), 2828-2839. DOI: 10.1016/j.cma.2011.05.006;

Simon, J.-W., & Weichert, D. (2011). Shakedown analysis with multidimensional loading spaces. Computational Mechanics, 49(4), 477-485. DOI: 10.1007/s00466-011-0656-8;


