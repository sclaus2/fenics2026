---
title: 'Material model discovery with FEMU in FEniCSx'
authors:
  - name:
      literal: 'Saeid Ghouli'
    affiliations:
      - 'Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Institute of Applied Mechanics, Egerlandstraße 5, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, 91058, Germany , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland'
    email: 'sghouli@ethz.ch'
  - name:
      literal: 'Antoine Benady'
    affiliations:
      - 'Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Institute of Applied Mechanics, Egerlandstraße 5, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, 91058, Germany , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland'
  - name:
      literal: 'Moritz Flaschel'
    affiliations:
      - 'Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Institute of Applied Mechanics, Egerlandstraße 5, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, 91058, Germany , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland'
  - name:
      literal: 'Laura De Lorenzis'
    affiliations:
      - 'Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland , Institute of Applied Mechanics, Egerlandstraße 5, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, 91058, Germany , Department of Mechanical and Process Engineering, ETH Zürich, 8092 Zürich, Switzerland'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Saeid Ghouli (ETH Zurich)

Our group has developed a computational framework based on sparse regression, denoted as EUCLID (Efficient Unsupervised Constitutive Law Identification & Discovery; Flaschel et al., 2021, 2023), to perform automated discovery of material laws out of a library of candidate functions. The loss function in the inverse problem has been formulated based on unbalanced internal and boundary forces computed from full-field displacement and global force data, similar to identification strategies such as the equilibrium gap and the virtual fields methods. The computation of the loss function thus involves the numerical differentiation of the experimental displacement data to obtain the strains, an operation that is notoriously sensitive to noise. In the present work, we aim at combining the discovery process of EUCLID based on sparse regression with a loss function based on the displacement field and reaction forces, in the spirit of the so-called finite element model updating (FEMU) technique. Exploiting the experimentally measured displacement data directly (without differentiation) provides a more noise-robust discovery algorithm; however, the new inverse problem becomes non-convex, requiring robust optimisation techniques, and involves finite element analyses at each iteration, requiring an efficient implementation. Also, since there are many models in the candidate library, we need to rely on automatic differentiation to avoid deriving all linearisations by hand. For all these reasons, we implement FEMU (forward and backward problems) via FEniCSx. In this talk, we present the key points of the implementation, illustrate the solution to the non-convex, non-linear inverse problem, and highlight the potential of our new approach.

# References
Flaschel, M., Kumar, S., & De Lorenzis, L. (2021). Unsupervised discovery of interpretable hyperelastic constitutive laws. Computer Methods in Applied Mechanics and Engineering, 381, 113852. DOI: 10.1016/j.cma.2021.113852.

Flaschel, M., Kumar, S., & De Lorenzis, L. (2023). Automated discovery of generalized standard material models with EUCLID. Computer Methods in Applied Mechanics and Engineering, 405, 115867. DOI: 10.1016/j.cma.2022.115867.


