---
title: 'Variational Solvers for Irreversible Evolutionary Systems: Orchestration'
authors:
  - name:
      literal: 'Andrés A. León Baldelli ; Pierluigi Cesana'
    affiliations:
      - 'Institut Jean Le Rond d''Alembert, CNRS, Sorbonne Université ; Institute of Mathematics for Industry, Kyushu University'
    email: 'leon.baldelli@cnrs.fr'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Andrés A León Baldelli (∂'Alembert / CNRS, Sorbonne Université)

Irreversible variational models for fracture and damage are challenging for numerical simulation: the problem is non-convex, constrained, and may admit multiple admissible paths. The predictive power of simulations depends not only on the model itself, but on how equilibria are identified, tracked, and selected.

In this talk, I present a modular computational framework for the simulation of irreversible evolutionary systems, built on FEniCSx and integrating three nonlinear variational solvers addressing complementary aspects of the problem:  constrained equilibrium, loss of uniqueness of evolution paths, and a rigorous criterion to assess the stability of computed states.

Rather than treating these components independently, I focus on their orchestration. At each load increment, the system is first brought to constrained equilibrium, then interrogated for bifurcation, and finally tested for stability. This structured interaction between first- and second-order information provides a strategy way to navigate the multiplicity of solutions and to track physically meaningful evolution paths.

The framework is implemented in Python using DOLFINx, PETSc, and SLEPc, leveraging automatic differentiation and scalable linear algebra.

More broadly, with this approach I illustrate how variational solvers can be composed into a transparent and extensible workflow for irreversible systems driven by energetic principles, providing a scalable foundation for more complex models, where additional internal variables and solver components can be integrated in a systematic manner, facilitating the implementation of experimental validation pipelines.

# References
A. A. León Baldelli and P. Cesana. Variational solvers for irreversible evolutionary systems. Journal of Open Source Software, 9(104), 2024.


