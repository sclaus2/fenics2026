---
title: 'Contact modeling using the Third Medium Contact (TMC) method: toward the application of a femoral stem insertion inside a bone cavity'
authors:
  - name:
      literal: 'Pierre Bichon'
    affiliations:
      - 'Univ Paris Est Creteil-Univ Gustave Eiffel CNRS-UMR 8208 MSME-F-94010 Créteil France'
    email: 'pierre.bichon@u-pec.fr'
  - name:
      literal: 'Felipe Rocha'
    affiliations:
      - 'Univ Paris Est Creteil-Univ Gustave Eiffel CNRS-UMR 8208 MSME-F-94010 Créteil France'
  - name:
      literal: 'Salah Naili'
    affiliations:
      - 'Univ Paris Est Creteil-Univ Gustave Eiffel CNRS-UMR 8208 MSME-F-94010 Créteil France'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Pierre Bichon (Univ Paris Est Creteil, Univ Gustave Eiffel, CNRS, UMR 8208, MSME, F-94010, Créteil, France)

Contact problems are among the most challenging in computational mechanics. Classical approaches such as the penalty method, the Augmented Lagrange Multiplier method [4], and the Nitsche method [3] require the definition of source-destination contact pairs and distance searches to evaluate the gap function. These approaches are not straightforward to implement in FEniCSx.
From a different perspective, the so-called Third Medium Contact (TMC) method [6] introduces a fictitious medium between the contacting bodies with extremely low stiffness. From a strain energy barrier viewpoint, the energy remains negligible when the bodies are separated and increases abruptly as they approach contact. However, the method remained limited due to numerical issues caused by extremely distorted elements. Recently, some works have addressed these difficulties through strain-gradient-type regularization [2] or relaxed mixed formulations with low-order elements [5], making the method practically usable.
From an implementation standpoint in FEniCSx, the TMC approach is relatively straightforward because it bypasses contact pair searches and instead relies directly on energy minimization, leveraging the FEniCSx's native automatic differentiation support.
In this work, we focus on the simulation of total hip arthroplasty using a cementless approach, commonly employed in orthopedic surgery, where friction is the primary mechanism responsible for implant stability. To model this problem, we consider an elastodynamic formulation using the Newmark method for time discretization in a simplified axisymmetric geometry representing the insertion of a femoral stem into a bone cavity. Using the analogy between plasticity and friction, the formulation of a friction law is introduced in the TMC method which is implemented with the help of the dolfinx_materials library [1].
Finally, a parametric study will be performed, and the results will be contrasted with the Nitsche method provided by COMSOL.

# References
[1] Bleyer, J. (2025). dolfinx_materials: A Python package for advanced material modelling, DOI: 10.5281/zenodo.13882183

[2] Bluhm, G. L., Sigmund, O. & Poulios, K. (2021). Internal contact modeling for finite strain topology optimization. Computational Mechanics, 67, 1099-1114. DOI: 10.1007/s00466-021-01974-x 

[3] Chouly, F., Hild, P. & Renard, Y. (2023). Finite Element Approximation of Contact and Friction in Elasticity (Birkhäuser Cham, AMMA, 48, ACM). DOI: 10.1007/978-3-031-31423-0

[4] Laursen, T. A. (2003). Computational contact and impact mechanics: fundamentals of modeling interfacial phenomena in nonlinear finite element analysis (Springer Science & Business Media, 1). DOI: 10.1007/978-3-662-04864-1

[5] Wriggers, P., Korelc, J. & Junker, Ph., (2025). A Third Medium Approach for Contact Using first and Second Order finite Elements. Computer Methods in Applied Mechanics and Engineering, 436, 117740. DOI: 10.1016/j.cma.2025.117740

[6] Wriggers, P., Schröder, J., Schwarz, A., (2013). A finite element method for contact using a third medium. Computational Mechanics, 52(4), 837-847. DOI: 10.1007/s00466-013-0848-5


