---
title: 'Shape optimization using PhiFEM'
authors:
  - name:
      literal: 'Josué Daniel Díaz Avalos'
    affiliations:
      - 'Universität Duisburg-Essen'
  - name:
      literal: 'Raphaël Bulle'
    affiliations:
      - 'Inria de l''Université de Lorraine'
    email: 'raphael.bulle@inria.fr'
  - name:
      literal: 'Stéphane Cotin'
    affiliations:
      - 'Inria de l''Université de Lorraine'
  - name:
      literal: 'Louis Ducongé'
    affiliations:
      - 'Université de Lorraine'
  - name:
      literal: 'Michel Duprez'
    affiliations:
      - 'Inria de l''Université de Lorraine'
  - name:
      literal: 'Antoine Laurain'
    affiliations:
      - 'Universität Duisburg-Essen'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Raphaël Bulle (Inria de l'Université de Lorraine)

The level-set method for evolving interfaces was first introduced in [1] and has been applied to a variety of shape optimization problems (see e.g. [3,4,5,6,7,8]).
The core idea of this method is to use a level-set description of the domain to be optimized and modify this level-set e.g. by the derivation of optimality conditions via the shape derivative of the domain [3].

Like the level-set method, the φ-FEM takes advantage of a description of the domain via a level-set.
The φ-FEM is an immersed boundary finite element method (FEM) with optimal convergence rate and conditioning which does not require any non-standard quadrature rule on cut cells nor non-standard finite element shape functions [9,10].
Thus, the φ-FEM is naturally well suited to be used with the level-set method to perform shape optimization as it provides a good description of the evolving boundary without any re-meshing of the domain.

In this talk, we describe a preliminary study on a shape optimization algorithm using φ-FEM to solve the state equations.
This algorithm is implemented in FEniCSx via the recent FormOpt shape optimization toolbox [8] and the phiFEM python package [11].
We investigate the benefits of using φ-FEM instead of a standard non-conforming FEM by performing several numerical comparisons on different types of shape optimization problems.

# References
[1] Osher, Stanley, and James A. Sethian. 1988. "Fronts Propagating with Curvature-Dependent Speed: Algorithms Based on Hamilton-Jacobi Formulations." Journal of Computational Physics 79(1):12-49. DOI: 10.1016/0021-9991(88)90002-2.

[2] Sethian, J. A. 1999. Level Set Methods and Fast Marching Methods: Evolving Interfaces in Computational Geometry, Fluid Mechanics, Computer Vision, and Materials Science. Cambridge University Press.

[3] Allaire, Grégoire, François Jouve, and Anca-Maria Toader. 2002. "A Level-Set Method for Shape Optimization." Comptes Rendus Mathematique 334(12):1125-30. DOI: 10.1016/S1631-073X(02)02412-3.

[4] Feppon, F., G. Allaire, F. Bordeu, J. Cortial, and C. Dapogny. 2019. "Shape Optimization of a Coupled Thermal Fluid-Structure Problem in a Level Set Mesh Evolution Framework." SeMA Journal 76(3):413-58. DOI: 10.1007/s40324-018-00185-4.

[5] Maury, Aymeric, Grégoire Allaire, and François Jouve. 2018. "Elasto-Plastic Shape Optimization Using the Level Set Method." SIAM Journal on Control and Optimization 56(1):556-81. DOI: 10.1137/17M1128940.

[6] Maury, Aymeric, Grégoire Allaire, and François Jouve. 2017. "Shape Optimisation with the Level Set Method for Contact Problems in Linearised Elasticity." The SMAI Journal of Computational Mathematics 3:249-92. DOI: 10.5802/smai-jcm.27.

[7] Laurain, Antoine. 2018. "A Level Set-Based Structural Optimization Code Using FEniCS." Structural and Multidisciplinary Optimization 58(3):1311-34. DOI: 10.1007/s00158-018-1950-2.

[8] Díaz-Avalos, Josué D., and Antoine Laurain. 2026. "FormOpt: A FEniCSx Toolbox for Level Set-Based Shape Optimization Supporting Parallel Computing." DOI: 10.48550/arXiv.2601.05709.

[9] Duprez, Michel, and Alexei Lozinski. 2020. "φ-FEM: A Finite Element Method on Domains Defined by Level-Sets." SIAM Journal on Numerical Analysis 58(2):1008-28. DOI: 10.1137/19M1248947.

[10] Duprez, Michel, Vanessa Lleras, and Alexei Lozinski. 2023. "A New φ-FEM Approach for Problems with Natural Boundary Conditions." Numerical Methods for Partial Differential Equations 39(1):281-303. DOI: 10.1002/num.22878.

[11] Bulle, Raphael, Michel Duprez, and Killian Vuillemot. 2025. "phiFEM: A Convenience Package for Using phiFEM with FEniCSx." DOI: 10.6084/M9.FIGSHARE.30373546.


