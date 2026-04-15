---
title: 'A Finite-Element Method for Fluctuating Navier--Stokes Equations'
authors:
  - name:
      literal: 'Dimitrios Gourzoulidis'
    affiliations:
      - 'Imperial College London'
    email: 'd.gourzoulidis@imperial.ac.uk'
  - name:
      literal: 'Mirko Gallo'
    affiliations:
      - 'Sapienza University of Rome'
  - name:
      literal: 'Soumaya Elkantassi'
    affiliations:
      - 'University of Lausanne'
  - name:
      literal: 'Toby Kay'
    affiliations:
      - 'Imperial College London'
  - name:
      literal: 'Serafim Kalliadasis'
    affiliations:
      - 'Imperial College London'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Dimitrios Gourzoulidis (Imperial College London)

Thermal fluctuations play a fundamental role in fluid dynamics, from Brownian motion at microscopic scales to activated processes such as cavitation, boiling, condensation, crystallisation, and hydrodynamic instabilities. While fluctuating Navier--Stokes equations have been studied extensively, finite-element discretisations for these systems remain comparatively underexplored. In this work, we present a finite-element framework for simulating compressible fluids governed by the fluctuating Navier--Stokes equations. The method preserves the fluctuation--dissipation balance at the discrete level by defining the stochastic forcing through its variational action, so that its covariance is proportional to the discrete viscous dissipation operator. Time integration is performed using a Crank--Nicolson scheme to ensure stability and accuracy. Numerical validation in one, two, and three spatial dimensions shows that the method correctly reproduces equilibrium fluctuation statistics for different mesh sizes and time steps.

# References
Gourzoulidis, D., Gallo, M., Elkantassi, S., Kay, T., and Kalliadasis, S. A finite-element method for fluctuating Navier--Stokes equations. To be submitted.


