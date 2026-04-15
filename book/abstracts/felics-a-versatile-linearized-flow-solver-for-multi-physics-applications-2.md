---
title: 'FELiCS: A Versatile Linearized Flow Solver for Multi-Physics Applications'
authors:
  - name:
      literal: 'Sophie J. Knechtel'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
    email: 's.knechtel@tu-berlin.de'
  - name:
      literal: 'Simon Demange'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Lukas M. Fuchs'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Xiuyang Song'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Jens S. Müller'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Alexandre Villié'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Anant R. Talisikar'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Marina Matthaiou'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Kilian Oberleithner'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
  - name:
      literal: 'Thomas L. Kaiser'
    affiliations:
      - 'Technische Universität Berlin (all co-authors)'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Sophie Knechtel (Technische Universität Berlin)

We present FELiCS (http://felics.eu), an open-source Python package for the linearized analysis of multi-physics flows within the FEniCS ecosystem.

Understanding how small perturbations evolve in a flow is central to many engineering problems, including transition to turbulence, noise generation, and flow control. Linear analysis provides a tractable framework to study amplification mechanisms, coherent structures, and input-output behavior, even in complex and turbulent configurations.

FELiCS leverages the automated finite element formulation provided by FEniCS (Alnæs et al., 2015) to construct and discretize linearized operators derived from the incompressible and compressible Navier-Stokes equations. The framework extends naturally to heat and mass transport, turbulence modeling, and reacting flows, enabling a unified treatment of multi-physics systems.

The formulation is based on variational forms, allowing direct use of FEniCS abstractions for function spaces, boundary conditions, and unstructured meshes. The resulting linear systems and eigenvalue problems are solved using scalable solvers from PETSc (Balay et al., 2019) and SLEPc (Hernandez et al., 2005), enabling application to large-scale problems.

FELiCS adopts a modular design in which physical models are implemented as composable variational contributions. This facilitates extension to additional equations and coupled systems while maintaining consistency with the finite element formulation. The software can be used as a standalone tool via configuration files or as a Python library, enabling integration into workflows such as sensitivity analysis, shape optimization, data assimilation, and flow control.

FELiCS has been applied to a range of problems, including turbulent reacting flows and aeroacoustics (e.g., Casel et al., 2022; Demange et al., 2024). A detailed software description has been submitted to the Journal of Open Source Software.

# References
Alnæs, M. S., Blechta, J., Hake, J., Johansson, A., Kehlet, B., Logg, A., Richardson, C., Ring, J., Rognes, M. E., & Wells, G. N. (2015). The FEniCS project version 1.5. DOI: 10.11588/ans.2015.100.20553

Balay, S., Abhyankar, S., Adams, M., Brown, J., Brune, P., Buschelman, K., Dalcin, L., Dener, A., Eijkhout, V., Gropp, W., et al. (2019). PETSc users manual. DOI: 10.2172/2998643

Casel, M., Oberleithner, K., Zhang, F., Zirwes, T., Bockhorn, H., Trimis, D., & Kaiser, T. L. (2022). Resolvent-based modelling of coherent structures in a turbulent jet flame using a passive flame approach. Combustion and Flame, 236, 111695. DOI: 10.1016/j.combustflame.2021.111695

Demange, S., Yuan, Z., Jekosch, S., Hanifi, A., Cavalieri, A. V. G., Sarradj, E., Kaiser, T. L., & Oberleithner, K. (2024). Resolvent model for aeroacoustics of trailing edge noise. Theoretical and Computational Fluid Dynamics. DOI: 10.1007/s00162-024-00688-z

Hernandez, V., Roman, J. E., & Vidal, V. (2005). SLEPc: A scalable and flexible toolkit for the solution of eigenvalue problems. ACM Transactions on Mathematical Software, 31(3), 351-362. DOI: 10.1145/1089014.1089019


