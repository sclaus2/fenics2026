---
title: 'L-PBF Processes via FEniCS: A Finite Element Framework for  Heat Modelling  and Accelerated Predictive Workflows'
authors:
  - name:
      literal: 'José Ángel Bejarano Vázquez'
    affiliations:
      - 'Isaac Toda Caraballo'
    email: 'ja.bejarano@cenim.csic.es'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** José Ángel Bejarano Vázquez (CENIM-CSIC, Universidad Complutense de Madrid (UCM))

In the scope of understanding the factors controlling the defects that commonly appear in the microstructures of materials produced by Additive Manufacturing (AM), a first step is the precise prediction of the thermal history. This work focuses on the development of a robust Finite Element Method (FEM) framework using FEniCS to simulate Laser Powder Bed Fusion (L-PBF) processes.
The core of the numerical model consists of a moving heat source that traverses a discretized mesh. To capture the underlying physics as accurately as possible, the material properties across the mesh are dynamically modified throughout the simulation, accounting for phase changes and the evolution from powder to solid state. This FEM approach in FEniCS provides high-fidelity results and it has been experimentally validated. Nevertheless, its computational cost for large-scale optimization remains a challenge.
Consequently, this study develops a methodology to accelerate these predictions. A key advantage of using FEniCS is its native Python integration, which makes the workflow for introducing Constrained Random Walks (CRW) extremely straightforward. These CRWs were used to efficiently generate a diverse dataset of scanning strategies and printing geometries within the FEM solver.
Finally, this dataset was used to evaluate several Machine Learning (ML) models, such as Extremely Randomized Trees (ERT) and Feedforward Neural Networks (FNN), as well as Long Short-Term Memory (LSTM) networks for temporal profiles. The results demonstrate that while the physics are grounded in the FEniCS FEM simulations, the resulting surrogate models offer quasi-instantaneous predictions with minimal error, enabling the exploration of a wide variety of printing parameters and strategies.


