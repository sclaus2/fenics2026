---
title: 'Large scale random vibration analysis using FEniCS'
authors:
  - name:
      literal: 'Shubham Saurabh'
    affiliations:
      - 'Bridge Engineering and Structures Division, CSIR-Central Road Research Institute (CRRI), New Delhi, India; Department of Civil Engineering, Indian Institute of Technology Roorkee, India; Department of Civil and Environmental Engineering Vanderbilt University USA; Department of Civil Engineering, Indian Institute of Technology Roorkee, India'
    email: 'shubham.crri@csir.res.in'
  - name:
      literal: 'Anurag Gupta'
    affiliations:
      - 'Bridge Engineering and Structures Division, CSIR-Central Road Research Institute (CRRI), New Delhi, India; Department of Civil Engineering, Indian Institute of Technology Roorkee, India; Department of Civil and Environmental Engineering Vanderbilt University USA; Department of Civil Engineering, Indian Institute of Technology Roorkee, India'
  - name:
      literal: 'Abhinav Gupta'
    affiliations:
      - 'Bridge Engineering and Structures Division, CSIR-Central Road Research Institute (CRRI), New Delhi, India; Department of Civil Engineering, Indian Institute of Technology Roorkee, India; Department of Civil and Environmental Engineering Vanderbilt University USA; Department of Civil Engineering, Indian Institute of Technology Roorkee, India'
  - name:
      literal: 'Rajib Chowdhury'
    affiliations:
      - 'Bridge Engineering and Structures Division, CSIR-Central Road Research Institute (CRRI), New Delhi, India; Department of Civil Engineering, Indian Institute of Technology Roorkee, India; Department of Civil and Environmental Engineering Vanderbilt University USA; Department of Civil Engineering, Indian Institute of Technology Roorkee, India'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Dr. Shubham Saurabh (Bridge Engineering and Structures Division, CSIR-Central Road Research Institute (CRRI), New Delhi, India)

Large-scale engineering structures, such as bridges, high-rise buildings, and offshore platforms, are often subjected to dynamic loads induced by environmental factors like earthquakes, wind, and traffic [1, 2]. Base excitation random vibration analysis plays a crucial role in assessing the structural response under stochastic excitations. This study investigates the dynamic behavior of large-scale structures under random base excitations using FEniCS. To simulate the real world, additional mass is applied to incorporate additional geometry of the assembly. Modal analysis is performed to determine the dynamic characteristics of the structure, including natural frequencies and mode shapes. The frequency response function is derived based on the system's natural frequency, damping ratio, and excitation frequency. Using the modal properties, the transfer function relating displacement response to base excitation is formulated. This expression incorporates the influence of mass, mode shapes, and transformation matrices. The acceleration response transfer function is obtained by considering the displacement response along with an additional transformation term. The power spectral density of the output response is then computed by multiplying the transfer function matrix with its conjugate transpose and the input power spectral density of the excitation. This formulation enables the evaluation of structural response characteristics under stochastic base excitations. Results of modal and random vibration analysis with and without additional mass are validated with an industry-standard commercial package.

# References
[1] Saurabh, S., Gupta, A., Chowdhury, R., & Podugu, P. (2024). Robust topology optimization for transient dynamic response minimization. Computer Methods in Applied Mechanics and Engineering, 426, 117009.

[1] Saurabh, S., Gupta, A., Chowdhury, R., & Duddu, R. (2025). Robust topology optimization for transient dynamic response minimization. Reliability Engineering & System Safety, 264, 111440.


