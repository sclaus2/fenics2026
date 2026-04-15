---
title: 'femOHL: A FEniCSx-based Framework for Structural Integrity and Resilience Assessment of Overhead Power Transmission Infrastructure'
authors:
  - name:
      literal: 'Daria Mesbah'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
    email: 'daria.mesbah@mews-labs.com'
  - name:
      literal: 'Elise Clavel'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
  - name:
      literal: 'John A. Redford'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
  - name:
      literal: 'Dorian Collot'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
  - name:
      literal: 'Daniel Chauveheid'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
  - name:
      literal: 'Julien Said'
    affiliations:
      - '(1) Mews Labs, (2) RTE'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Daria Mesbah (Mews Labs)

In the context of climate change and increasingly severe extreme wind events, assessing the structural integrity of overhead transmission infrastructure under environmental loading has become a major strategic challenge for Transmission System Operators (TSOs), particularly for RTE in France, which operates the largest transmission network in Europe. The goal of this project is to develop a robust and accessible tool that can be used by decision-makers and field experts, without requiring in-depth expertise in the underlying methods.

To achieve this objective, we have developed femOHL (Finite Element Method for Overhead Lines), a numerical simulation tool built upon the FEniCSx framework. The code relies on advanced finite element formulations to capture the geometric and material nonlinearities arising from the truss-like configurations of pylons, conductors and foundations. It incorporates component-specific constitutive behaviours and accounts for environmental effects such as wind loading, temperature variations, corrosion-induced degradation and soil-structure interaction. Both static and dynamic solvers are implemented, enabling the simulation of progressive failure mechanisms that may ultimately lead to cascading collapse of pylons.

Developed within an industrial context, femOHL incorporates operational constraints and engineering rules to ensure consistency with real-world practices. By enabling the evaluation of structural behaviour under realistic environmental and operational conditions, femOHL supports the quantification of safety margins and the identification of critical configurations. Its modular architecture promotes extensibility and maintainability, allowing adaptation to a wide range of study scenarios. By providing a robust and scalable computational framework, femOHL supports TSOs in anticipating risks and strengthening infrastructure resilience.


