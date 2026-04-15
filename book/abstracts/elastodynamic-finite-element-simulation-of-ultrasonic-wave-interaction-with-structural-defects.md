---
title: 'Elastodynamic Finite Element Simulation of Ultrasonic Wave Interaction with Structural Defects'
authors:
  - name:
      literal: 'Samyak Darshan C B'
    affiliations:
      - 'Affiliation unavailable'
    email: 'samyak.darshan1998@gmail.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Samyak Darshan C B (Baker Hughes)

Ultrasonic testing is widely used for non-destructive evaluation of
structural components. Conventional interpretation methods such as
B-scan and C-scan imaging rely primarily on echo amplitude and
time of flight information, which can limit the physical interpretation
of measured signals.

* This work presents a computational mechanics framework for simulating
ultrasonic wave interaction with structural defects using elastodynamic
finite element analysis. The approach focuses on understanding how
defects influence wave propagation and measured probe signals.

* A two dimensional elastic plate subjected to a transient ultrasonic
pulse is modeled using the open-source finite element platform FEniCS.
Defects such as circular voids and crack-like discontinuities are
represented as localized reductions in stiffness within the
computational domain.

* Time dependent displacement responses are recorded at selected probe
locations to emulate ultrasonic sensor measurements. Comparisons between
intact and defective configurations are used to evaluate changes in wave
arrival times, scattering behavior and signal amplitudes.

* A spatial sensitivity analysis is performed to identify regions where
localized stiffness perturbations produce the strongest influence on
measured signals. The resulting sensitivity maps provide a physics-based
indication of potential defect locations.

* The results demonstrate that elastodynamic simulations can capture
characteristic wave scattering patterns associated with structural
defects. The framework establishes a foundation for model-assisted
interpretation of ultrasonic measurements and supports future
development of inverse reconstruction methods for defect
characterization.

# References
Pratt, R. G. (1999). Seismic waveform inversion in the frequency domain,

Part 1: Theory and verification in a physical scale model. Geophysics,

64(3), 888-901. DOI: 10.1190/1.1444597

Virieux, J., & Operto, S. (2009). An overview of full-waveform inversion

in exploration geophysics. Geophysics, 74(6), WCC1-WCC26.

DOI: 10.1190/1.3238367

Tarantola, A. (1984). Inversion of seismic reflection data in the

acoustic approximation. Geophysics, 49(8), 1259-1266.

DOI: 10.1190/1.1441754


