---
title: 'Finite Element Modeling of Electrochemical Impedance Spectroscopy in All-Solid-State Batteries using FEniCSx'
authors:
  - name:
      literal: 'Théo Bermond'
    affiliations:
      - 'Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Liten, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France'
    email: 'theo.bermond.pro@gmail.com'
  - name:
      literal: 'Lara Casiez'
    affiliations:
      - 'Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Liten, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France'
  - name:
      literal: 'Jacopo Cele'
    affiliations:
      - 'Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Liten, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France'
  - name:
      literal: 'Marion Chandesris'
    affiliations:
      - 'Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Liten, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France'
  - name:
      literal: 'Sami Oukassi'
    affiliations:
      - 'Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Liten, F-38000 Grenoble, France, Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Poster

**Presenter:** Théo Bermond (Univ. Grenoble Alpes, CEA, Leti, F-38000 Grenoble, France)

All-solid-state thin-film batteries are key components for the development of autonomous integrated systems, where performance depends on complex charge transport and interface kinetics [1]. Electrochemical Impedance Spectroscopy (EIS) represents a non-destructive  technique used to characterize these phenomena by decoupling the resistive and capacitive contributions of the solid electrolyte and its interfaces [2].
In this work, we implement a numerical framework within FEniCSx to simulate the EIS response of such systems based on the Poisson-Nernst-Planck (PNP) model. This model couples electrostatic potential and ionic concentrations, accounting for the formation of the electrical double layers at the electrode-electrolyte interfaces [3]. We utilize the Unified Form Language (UFL) to perform an automatic linearization of the non-linear coupled system around various electrode bias potentials. This approach allows for a direct resolution in the frequency domain.
The central feature of the implementation is the post-processing of the frequency-domain results, using a residual-based current calculation to ensure strict electrical conservation. We demonstrate the framework's validity by comparing simulated Nyquist plots with experimental data obtained from thin -film batteries. This work provides a physically consistent tool for  the study of electrochemical phenomena in solid-state energy storage.

# References
[1] Wu, T., Dai, W., Ke, M., Huang, Q., & Lu, L. (2021). All-Solid-State Thin Film μ-Batteries for Microelectronics. Advanced Science, 8(19), 2100774. DOI: 10.1002/advs.202100774

[2] Orazem, M. E., & Tribollet, B. (2020). A tutorial on electrochemical impedance spectroscopy. ChemTexts, 6(2), 12. DOI: 10.1007/s40828-020-0110-7

[3] Bazant, M. Z., Thornton, K., & Ajdari, A. (2004). Diffuse-charge dynamics in electrochemical systems. Physical Review E, 70(2), 021506. DOI: 10.1103/PhysRevE.70.021506


