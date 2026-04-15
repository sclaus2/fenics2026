---
title: 'Numerical investigation of urban heat island within variable porous urban domain'
authors:
  - name:
      literal: 'Luis Gerardo Gutierrez Ibarra'
    affiliations:
      - 'University of Guadalajara'
    email: 'luis.gutierrez_i@alumnos.udg.mx'
  - name:
      literal: 'Néstor García Chan'
    affiliations:
      - 'University of Guadalajara'
  - name:
      literal: 'Juan Antonio Licea Salazar'
    affiliations:
      - 'University of Guadalajara'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Luis Gerardo Gutierrez Ibarra (University of Guadalajara, Mexico)

This paper presents a numerical study of the Urban Heat Island (UHI), defined as the temperature differential between urban and rural or suburban areas. Urban morphology is modeled as a variable porous medium, where buildings and streets represent the solid and fluid phases, respectively, enabling the meshing of large-scale cities. UHI intensity is measured through air temperature, coupled with an energy balance to account for the heating of streets and buildings due to solar radiation. To achieve this, a two-dimensional vertical dynamic model based on partial differential equations was employed, utilizing a Darcy-Forchheimer-Brinkman type equation to obtain the wind velocity field. Furthermore, a thermal exchange model is used between air and building temperatures; additionally, a surface energy balance equation is coupled, considering net radiation and the physical properties of the urban surface.Estimating UHI intensity at a macroscale can be instrumental in decision-making processes regarding urban planning, benefiting the environment and urban residents in both economic and health terms. Moreover, it provides a framework to explore UHI mitigation strategies. This study considers a domain of 11 km x 800 m with variable porosity throughout, assuming a concentric porosity distribution (lower in the center and higher in the suburbs), utilizing meteorological data for solar radiation. For the numerical solution, the Taylor-Hood finite element method and an IPCS scheme with BDF2 discretization and stabilizers were implemented using the FEniCSx software. Finally, various numerical experiments are presented to visualize the effects of porosity, wind, and radiation on UHI intensity.


