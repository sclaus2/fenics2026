---
title: 'Numerical quality factor statistics of multilayered superconducting radio-frequency cavity'
authors:
  - name:
      literal: 'Aaron Gobeyn'
    affiliations:
      - 'Technical University Darmstadt'
    email: 'aaron.gobeyn@tu-darmstadt.de'
  - name:
      literal: 'Wolfgang Ackermann'
    affiliations:
      - 'Technical University Darmstadt'
  - name:
      literal: 'Herbert De Gersem'
    affiliations:
      - 'Technical University Darmstadt'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Aaron Gobeyn (Technical University Darmstadt)

Bulk niobium (Nb) is currently the standard material for superconducting radio-frequency (SRF) cavities for particle accelerator 
applications. It has been observed that the benefits of using a superconducting material occur in only a thin layer [1]. This 
makes a proposal made by Gurevich [2] attractive for investigation, namely, coating the SRF cavity with alternating superconducting 
and insulating layers, referred to as superconductor-insulator-superconductor (SIS) structures. The thin coating shields the 
bulk interior from accelerating fields, allowing for higher operating fields than is even theoretically possible with Nb. Depositing 
such a coating on a complex geometry, such as a TESLA cavity, is likely to yield inhomogeneous coatings with potentially measurable 
impact on quantities of interest, such as the quality factor. We attempt to estimate these impacts through finite element (FE) simulations. 

In our work, we model the SIS multilayer by reducing it to a surface impedance using a first-order Leontovich boundary condition [3]. This 
surface impedance appears in the boundary condition of the complex eigenvalue problem for the eigenmodes of the SRF cavity, which we 
solve via the FE method. We further treat the coating thickness as a Gaussian random field, obtained by solving a 2D FE problem on the 
boundary [4], which yields a spatially inhomogeneous surface impedance. By sampling Gaussian random fields we generate a normal 
distribution for the quality factor. We perform these simulations for a single-cell TESLA cavity and repeat them for different 
correlation lengths in the Matérn kernel of the Gaussian random field. We then compare the distributions of the quality factors 
by statistical methods.

# References
[1] Valente-Feliciano, A.-M. (2016). Superconducting RF materials other than bulk niobium: a review. Superconductor Science & Technology, 29(11), 113002. DOI: 10.1088/0953-2048/29/11/113002

[2] Gurevich, A. (2006). Enhancement of rf breakdown field of superconductors by multilayer coating. Applied Physics Letters, 88(1), 012511. DOI: 10.1063/1.2162264

[3] Kubo, T. (2017). Multilayer coating for higher accelerating fields in superconducting radio-frequency cavities: a review of theoretical aspects. Superconductor Science & Technology, 30(2), 023001. DOI: 10.1088/1361-6668/30/2/023001

[4] Koh, K. J., & Cirak, F. (2023). Stochastic PDE representation of random fields for large-scale Gaussian process regression and statistical finite element analysis. Computer Methods in Applied Mechanics and Engineering, 417(116358), 116358. DOI: 10.1016/j.cma.2023.116358


