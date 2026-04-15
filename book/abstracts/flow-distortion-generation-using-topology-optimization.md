---
title: 'Flow distortion generation using topology optimization'
authors:
  - name:
      literal: 'Pierre Grenson'
    affiliations:
      - 'Research Scientist, DAAA, ONERA, 92190, Meudon, France'
  - name:
      literal: 'Julien Dandois'
    affiliations:
      - 'Research Scientist, DAAA, ONERA, 92190, Meudon, France'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Langlet Nathan (PhD student DAAA, ONERA, Institut Polytechnique de Paris, 92190, Meudon, France, nathan.langlet@onera.fr)

This study investigates the use of topology optimization to automatically identify aerodynamic designs that accurately generate a specific target velocity profile. The methodology couples the steady-state RANS equations with the Spalart-Allmaras turbulence model and a relaxed eikonal equation for dynamic wall-distance computation, implemented using the FEniCSx library. To ensure clearly defined solid-fluid interfaces, the Topology Optimization of Binary Structures (TOBS) method is employed, utilizing integer linear programming via the CPLEX software. The approach is validated on the wake reproduction of a square cylinder at Re = 10^5, and further applied to flow separation control in a 90° sharp-angled bend at Re = 10^4. Results demonstrate that the framework successfully creates streamlined guide vanes that eliminate flow separation, maintaining target velocity profiles within a ±5% tolerance. The influence of initial guesses and optimization parameters is analyzed, highlighting the existence of multiple local minima and the validation of the method for complex turbulent flows. The governing equations include incompressible RANS with Brinkman term for solid modeling, and the S-A model with penalty for turbulence in solids. The objective is a weighted sum of velocity error at AIP and regularization. Numerical implementation uses Newton solver for nonlinear system and branch-and-bound for ILP. In the square case, objective reduces 380-fold, with geometry matching the target wake. For the bend, four cases show curved vanes, with convergence varying by initial guess, revealing TOBS efficiency in adding material. Conclusion suggests extensions to 3D compressible flows and TOBS-GT for better interface.


