---
title: 'Integration of Externally Defined Constitutive Models into FEniCSx Using dolfinx-external-operator'
authors:
  - name:
      literal: 'Andrey Latyshev'
    affiliations:
      - 'University of Luxembourg'
      - 'Institut Jean Le Rond d''Alembert, Sorbonne Université'
    email: 'andrey.latyshev@uni.lu'
  - name:
      literal: 'Jørgen S. Dokken'
    affiliations:
      - 'Simula Research Laboratory'
  - name:
      literal: 'Jérémy Bleyer'
    affiliations:
      - 'Laboratoire Navier, École des Ponts ParisTech, Université Gustave Eiffel'
  - name:
      literal: 'Corrado Maurini'
    affiliations:
      - 'Institut Jean Le Rond d''Alembert, Sorbonne Université'
  - name:
      literal: 'Jack S. Hale'
    affiliations:
      - 'University of Luxembourg'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Software Demonstration

**Presenter:** Andrey Latyshev (University of Luxembourg, Institut Jean Le Rond d'Alembert, Sorbonne Université)

The Unified Form Language (UFL) (Alnaes et al., 2013) is essential for writing
variational forms of partial differential equations (PDEs) in automated finite
element solvers like FEniCS. However, UFL has a critical limitation: non-trivial
solid mechanics problems, such as complex plasticity or neural network
constitutive models, cannot be naturally formulated within it. This restriction
has slowed FEniCS adoption in the broader solid mechanics community.

To overcome this bottleneck, we introduce DOLFINx-External-Operator (Latyshev et
al., 2025), a novel software framework for FEniCSx. Based on DOLFINx's new
data-centric design (Baratta et al., 2023), automatic UFL Expression code
generation, and the UFL ExternalOperator extension (Bouziani & Ham, 2021), this
tool enables the seamless integration of arbitrary constitutive models via
third-party packages that support ndarray-like data structures, such as JAX
(Bradbury et al., 2018) and Numba (Lam et al., 2015).

As a particular outcome, we leverage JAX for forward-mode algorithmic automatic
differentiation (AD), eliminating the need for error-prone manual derivatives.
We demonstrate the use of AD on a complex non-associative Mohr-Coulomb
elastoplastic model with apex smoothing (Helfer et al., 2024). The framework and
examples are open-source under the LGPLv3 license.

# References
Alnæs, M. S., Logg, A., Ølgaard, K. B., Rognes, M. E., & Wells, G. N. (2014). Unified form language: A domain-specific language for weak formulations of partial differential equations. ACM Transactions on Mathematical Software, 40(2), 9:1-9:37. DOI: 10.1145/2566630

Baratta, I. A., Dean, J. P., Dokken, J. S., Habera, M., Hale, J. S., Richardson, C. N., Rognes, M. E., Scroggs, M. W., Sime, N., & Wells, G. N. (2023). DOLFINx: The next generation FEniCS problem solving environment. Zenodo. DOI: 10.5281/zenodo.10447666

Bouziani, N., & Ham, D. A. (2021). Escaping the abstraction: A foreign function interface for the Unified Form Language [UFL] (arXiv:2111.00945). arXiv. DOI: 10.48550/arXiv.2111.00945

Bradbury, J., Frostig, R., Hawkins, P., Johnson, M. J., Katariya, Y., Leary, C., Maclaurin, D., Necula, G., Paszke, A., Vander-Plas, J., Wanderman-Milne, S., & Zhang, Q. (2018). JAX: Composable transformations of Python+NumPy programs (Version 0.3.13) [Computer software]. http://github.com/jax-ml/jax

Helfer, T., Michel, B., Proix, J.-M., Sercombe, J., Casella, M., & Salvo, M. (2024). Invariant-based implementation of the Mohr-Coulomb elasto-plastic model in OpenGeoSys using MFront (Version 4.2.1) [Computer software]. https://thelfer.github.io/tfel/web/MohrCoulomb.html

Latyshev, A., Bleyer, J., Maurini, C., & Hale, J. (2025). Expressing general constitutive models in FEniCSx using external operators and algorithmic automatic differentiation. Journal of Theoretical, Computational and Applied Mechanics. DOI: 10.46298/jtcam.14449


