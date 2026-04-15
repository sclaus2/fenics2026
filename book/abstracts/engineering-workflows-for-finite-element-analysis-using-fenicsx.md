---
title: 'Engineering Workflows for Finite Element Analysis Using FEniCSx'
authors:
  - name:
      literal: 'Bora Acur'
    affiliations:
      - 'Turkish Aerospace Industry'
    email: 'boraacur94@gmail.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Bora Acur (Turkish Aerospace Industry)

Open-source finite element frameworks such as FEniCSx provide powerful capabilities for the numerical solution of partial differential equations. However, their adoption in practical engineering workflows remains limited due to the complexity of model preparation, boundary condition assignment, and verification of numerical results. This work presents a verification-oriented engineering workflow built on top of FEniCSx to facilitate its use in structural analysis applications.

The proposed framework introduces a set of utilities designed to simplify common tasks encountered in engineering simulations. A boundary condition wizard is developed to streamline the assignment of loads and constraints directly from mesh-based data. In addition, automated mesh quality evaluation tools are implemented to inspect element metrics such as aspect ratio and identify potential numerical issues prior to the analysis stage.

To demonstrate the reliability of the workflow, several benchmark problems inspired by established verification studies are analyzed. The obtained numerical results are compared with reference solutions in order to assess accuracy and consistency of the implementation. The presented approach emphasizes reproducibility, automation, and practical usability for engineers working with open-source finite element frameworks.

The results illustrate how FEniCSx can be integrated into engineering-oriented analysis pipelines while maintaining verification-driven modeling practices. The proposed workflow aims to reduce the barrier for engineers adopting open-source simulation tools and provides a foundation for further development of advanced computational mechanics applications using FEniCSx.

# References
Logg, A., Mardal, K.-A., & Wells, G. N. (2012). Automated solution of differential equations by the finite element method: The FEniCS book. Springer. DOI: 10.1007/978-3-642-23099-8

Dokken, J. S., Wells, G. N., Richardson, C., et al. (2023). FEniCSx: The next generation FEniCS problem solving environment. ACM Transactions on Mathematical Software. DOI: 10.1145/3524456

Zienkiewicz, O. C., Taylor, R. L., & Zhu, J. Z. (2013). The finite element method: Its basis and fundamentals (7th ed.). Butterworth-Heinemann. DOI: 10.1016/C2009-0-24909-9

NAFEMS. (2015). Benchmark examples for finite element analysis verification. https://www.nafems.org


