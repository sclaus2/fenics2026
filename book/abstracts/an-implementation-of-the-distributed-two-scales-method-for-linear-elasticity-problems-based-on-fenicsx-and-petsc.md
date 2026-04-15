---
title: 'An implementation of the distributed two scales method for linear elasticity problems based on FEniCSx and PETSc'
authors:
  - name:
      literal: 'Salzman Alexis'
    affiliations:
      - 'Nantes université, Ecole centrale de Nantes, GeM Institute UMR CNRS 6180, 1 rue de la Noë 44321 Nantes, France'
    email: 'alexis.salzman@ec-nantes.fr'
  - name:
      literal: 'Stainier Laurent'
    affiliations:
      - 'Nantes université, Ecole centrale de Nantes, GeM Institute UMR CNRS 6180, 1 rue de la Noë 44321 Nantes, France'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Salzman Alexis (Nantes université, Ecole centrale de Nantes, GeM Institute, UMR CNRS 6180, 1 rue de la Noë, 44321, Nantes, France)

The distributed two-scale method, proposed in Salzman and Moës (2023), has been reimplemented with FEniCSx and PETSc libraries as an independent Python/C++ library. This method uses enrichment techniques to compute a fine-scale discretized problem without solving the associated linear algebra system. Instead, a set of small problems covering the main zone of interest are solved, and their solutions are used as enrichment functions for a coarser scale problem. Solving this coarse-scale problem is expected to be relatively cheap. The result of this coarse system can then be projected at the fine scale. Recomputing the small problems with these new boundary conditions leads to loops between the two scales and converges to the solution of the fine scale problem.

This talk gives the state of the art of this ongoing work. It discusses the various approaches used to implement this method, and, in particular, the choices made on which parts are treated by FEniCSx, by PETSc, and coded in the library. Comparison with seminal implementation on some computation shows that the current version of the library is providing same numerical results. Some other test cases also confirm the correct implementation in the context of parallel computation with use of multi point constraints, thanks to dolfinx mpc.

Finally, an extra numerical analysis of the use of the distributed two-scale method as a preconditioner illustrates the interest of coding in the FEniCSx ecosystem, which offers a high level of flexibility for prototyping in research.

# References
Salzman, A. & Moës, N. (2023)  A two-scale solver for linear elasticity problems in the context of parallel message passing. Computer Methods in Applied Mechanics and Engineering.  DOI: 10.1016/j.cma.2023.115914


