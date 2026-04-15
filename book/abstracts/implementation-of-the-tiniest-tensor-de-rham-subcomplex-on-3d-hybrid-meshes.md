---
title: 'Implementation of the TiNiest Tensor de Rham subcomplex on 3D Hybrid Meshes'
authors:
  - name:
      literal: 'Johnny Vogels'
    affiliations:
      - 'Affiliation unavailable'
    email: 'jmvogels@live.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Johnny Vogels

The differential resolution is given by the de Rham complex. In three dimensions, the operators gradient, curl, and divergence constitute the differentials that map scalars, covectors, vectors, and densities to the next level in the sequence of the complex.

Once the domain is equipped with a mesh, discrete subcomplexes with commuting projections can be constructed, forming the foundation for stability using Finite Element Exterior Calculus (FEEC) with Hodge-Laplacian or Hodge-Dirac formulations. This becomes essential when considering mixed formulations where (co-)vectorial quantities get endowed with degrees of freedom.

On simplicial meshes, either full or trimmed spaces of specific polynomial orders are used. This choice determines the relative accuracy of quantities in mixed formulations. For hybrid meshes - comprising tetrahedra, hexahedra, prisms, and pyramids - additional choices arise. With full spaces, one uses the serendipity subcomplex. We are exploring further options. For trimmed (Ciarlet-)elements, three subcomplexes with successively increasing accuracy under non-affine mappings are available: trimmed serendipity, TiNiest Tensor (TNT), and full tensor-product (Q-).

We apply the mathematically required corrections to the formulations of Cockburn and Fu (2017). On this basis, we present the first implementation of the complete TiNiest Tensor De Rham subcomplex on 3D hybrid meshes. This is also the first implementation of any 3D hybrid-mesh subcomplex in symfem and basix.

This enables simulations of basic 3D processes on hybrid meshes with (co-)vectorial degrees of freedom such as electromagnetism.

Keywords: TiNiest Tensor, transition elements, prism, pyramid, de Rham, conformal, Sobolev complex, FEEC, commuting projections, Hodge-Laplacian, Hodge-Dirac, symfem, basix, Ciarlet, saddle-point systems, mixed methods, vectorial quantities, electromagnetism, element families, discrete subcomplexes, hybrid meshes, serendipity spaces, trimmed spaces

# References
Cockburn, B., Fu, G. (2017). A systematic construction of finite element commuting exact sequences. SIAM Journal on Numerical Analysis, 55(4), 1650-1688.


