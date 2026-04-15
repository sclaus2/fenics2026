---
title: 'Graph-Based Execution Framework for Finite Element Simulation and Optimization in FEniCSx'
authors:
  - name:
      literal: 'Hamza Elma'
    affiliations:
      - 'Hamza ELMA'
    email: 'elmahamza64@gmail.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Software Demonstration

**Presenter:** Hamza Elma (Indenpendent)

The increasing complexity of numerical simulations in computational mechanics calls for more structured and efficient computational workflows. Traditional notebook-based approaches remain largely linear, making iterative tasks such as mesh refinement studies and parameter sweeps computationally expensive and difficult to manage.

In this work, we propose a graph-based execution model for FEniCSx simulations, where each stage of the workflow-geometry definition, mesh generation, variational formulation, solution, and post-processing-is represented as a set of computational nodes with explicit dependencies. This structure enables automatic tracking of dependencies between computational steps, selective re-execution of modified components, and persistent caching of intermediate results, thereby reducing redundant computation in iterative simulation workflows.

We further extend this framework to support structured parameter studies inspired by machine learning workflow optimization strategies. In particular, we demonstrate how mesh convergence studies and parameter sweeps can be expressed as structured exploration over computational graphs, allowing efficient reuse of previously computed simulation states.

A cantilever beam problem is used to demonstrate the approach. The results show that the proposed execution model significantly reduces recomputation effort during mesh refinement studies while maintaining full reproducibility of simulation pipelines.

This work demonstrates how ideas from graph-based workflow execution can be used to improve reproducibility and efficiency in finite element simulation pipelines within the FEniCSx ecosystem.


