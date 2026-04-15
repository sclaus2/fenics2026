---
title: 'Flexibility Method for Contact Mechanics in FEniCSx. Finite Element Construction and Hierarchical Compression of Compliance Operators.'
authors:
  - name:
      literal: 'Yahya Boye'
    affiliations:
      - 'Mines Paris -- PSL'
    email: 'yahya.boye@minesparis.psl.eu'
  - name:
      literal: 'Jérémy Bleyer'
    affiliations:
      - 'École des Ponts ParisTech'
  - name:
      literal: 'Stéphanie Chaillat'
    affiliations:
      - 'CNRS--ENSTA--INRIA'
  - name:
      literal: 'V. A. Yastrebov'
    affiliations:
      - 'Mines Paris -- PSL'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Yahya Boye (Mines Paris PSL)

Contact problems in solid mechanics are classically formulated by the Moreau-Signorini conditions, expressing non-penetration, non-adhesion, and complementarity. This leads to a variational inequality with a unique solution (Duvaut & Lions, 1976). In practice, these problems are often solved with FEM using penalty, Lagrange multiplier, or augmented Lagrangian methods (Laursen, 2002). Although effective, such approaches introduce user -defined parameters or additional unknowns and are intrusive, since they require modifications of the tangent matrix structure.

In this work, we investigate the flexibility method originally introduced by Francavilla and Zienkiewicz (1975). This approach reformulates the contact problem using the Neumann-to-Dirichlet operator restricted to the contact interface. This operator maps contact tractions to surface displacements, allowing the problem to be recast as a linear complementarity problem (Cottle et al., 1992). The contact forces are solved as an auxiliary problem and then applied as Neumann boundary conditions in the FEM model.

A main limitation of this approach is the dense compliance operator, which leads to poor scalability. To address this, we use hierarchical matrices (Hackbusch, 2015), which compress low-rank far-field interactions and reduce storage and matrix-vector costs.

We also investigate several strategies to construct the compliance operator, including sampling, Schur complement, and BEM. A key advantage of the method is its non-intrusive character: contact is solved as an auxiliary problem without modifying the finite element formulation. The method is implemented in an open-source framework based on FEniCSx. Future work will address frictional contact and nonlinear materials

# References
[1] Duvaut, G., & Lions, J.-L. (1976). *Les inéquations en mécanique et en physique*. Springer. DOI: 10.1007/978-3-642-66165-5

[2] Laursen, T. A. (2002). *Computational contact and impact mechanics*. Springer. DOI: 10.1007/978-3-662-04864-1

[3] Francavilla, A., & Zienkiewicz, O. C. (1975). A note on numerical computation of elastic contact problems. *International Journal for Numerical Methods in Engineering, 9*(4), 913-924. DOI: 10.1002/nme.1620090410

[4] Cottle, R. W., Pang, J.-S., & Stone, R. E. (1992). *The linear complementarity problem*. SIAM. DOI: 10.1137/1.9780898719000.fm

[5] Hackbusch, W. (2015). *Hierarchical matrices: Algorithms and analysis*. Springer. DOI: 10.1007/978-3-662-47324-5


