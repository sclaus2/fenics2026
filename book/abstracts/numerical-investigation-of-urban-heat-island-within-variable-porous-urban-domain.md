---
title: 'Numerical investigation of urban heat island within variable porous urban domain'
authors:
  - name:
      literal: 'Luis Gerardo Gutierrez Ibarra'
    affiliations:
      - 'University of Guadalajara'
    email: 'luis.gutierrez_i@alumnos.udg.mx'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Luis Gerardo Gutierrez Ibarra (University of Guadalajara)

This study presents a numerical analysis of the Urban Heat Island (UHI) effect, defined as the temperature differential between urban and rural areas. To efficiently mesh and simulate large-scale cities, urban morphology is modeled as a variable porous medium, where buildings and streets represent the solid and fluid phases, respectively. We analyze an 11000 mts x 800 mts domain with a concentric porosity distribution-dense at the city center and sparse in the suburbs-driven by real meteorological solar radiation data. The computational solver is built on FEniCSx, extending Jørgen S. Dokken's fractional-step Navier-Stokes pipeline to include porous media resistance and thermal coupling. For the spatial discretization, Taylor-Hood elements are used to ensure velocity-pressure stability, augmented by SUPG (Streamline-Upwind/Petrov-Galerkin) and GLS (Galerkin/Least-Squares) stabilizers. Temporal discretization is handled via a second-order Backward Differentiation Formula (BDF2) integrated into an Incremental Pressure Correction Scheme (IPCS), a standard variation of the Chorin projection method. We present interesting results from the wind velocity field, demonstrating that the variable porous medium induces von Kármán vortices. This phenomenon occurs despite the simulation not yet resolving a full turbulence model (a feature currently under development). This effect is analyzed across different city morphologies (dense vs. dispersed) to visualize their respective impacts on air temperature and overall UHI intensity.


