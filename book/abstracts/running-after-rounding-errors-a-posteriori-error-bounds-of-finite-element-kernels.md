---
title: 'Running after rounding errors: a posteriori error bounds of finite element kernels'
authors:
  - name:
      literal: 'Michal Habera'
    affiliations:
      - 'University of Luxembourg'
    email: 'michal.habera@uni.lu'
  - name:
      literal: 'Paul T. Kühner'
    affiliations:
      - 'University of Luxembourg'
  - name:
      literal: 'Matteo Croci'
    affiliations:
      - 'Basque Center for Applied Mathematics'
  - name:
      literal: 'Andreas Zilian'
    affiliations:
      - 'University of Luxembourg'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Michal Habera (University of Luxembourg)

Rounding errors in finite element computations can lead to significant inaccuracies, stalled convergence, and incorrect results.
Moreover, the effects of rounding errors accumulated within automatically generated and compiled kernels are difficult to analyze a priori.
In this contribution, we use an a posteriori technique called Running Error Analysis (REA), where a forward error bound is computed concurrently with the value.

We present the implementation of REA for the FEniCS Form Compiler (FFCx), based on a C++ backend for generating type-generic templated kernels over a custom arithmetic type that tracks both the value and its error bound.
As an example, we demonstrate REA for detecting catastrophic cancellation in the assembly of a Neo-Hookean hyperelastic model in the small deformation regime. We also show that REA offers small performance overhead compared to higher- or multi-precision kernel evaluation (e.g., `std::float128` or `mpfr_t`). Applications of this work include: robust reduced-precision computations in embedded systems, numerical debugging of new, possibly ill-conditioned or unstable PDE formulations, and guiding the design of mixed-precision kernels.

The functionality is available for arbitrary UFL forms supported by FFCx and is implemented in the [`dolfiny` framework](https://github.com/fenics-dolfiny/dolfiny).


