---
title: 'An Open-Source FEniCSx-Based Platform for Industrial Vibroacoustic Simulation'
authors:
  - name:
      literal: 'Antonio Baiano Svizzero'
    affiliations:
      - 'Undabit'
    email: 'antonio.bs@undabit.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Antonio Baiano Svizzero (Undabit)

An open-source vibroacoustic simulation platform built on FEniCSx is presented, designed as an alternative to established commercial solvers. The software targets a broad range of industrial applications, including automotive, aerospace and machinery noise control.
The platform follows a three-layer architecture. The core layer relies on FEniCSx for the assembly and solution of variational problems. On top of it, a custom Python API provides domain-specific tools for vibroacoustic analysis: perfectly matched layers for modelling unbounded acoustic domains, a general shell formulation for thin-walled structures, a non-conformal coupling strategy between fluid and structural meshes that removes the need for conforming interfaces, and a mesh translator to import existing Nastran models directly into the FEniCSx workflow. Further modules are currently under development.
The third layer is a graphical user interface based on PyQt6 and PyVista, which wraps the entire workflow into a desktop application that can be used without writing any Python code.
We describe the architecture of the platform and each of its tools, then illustrate the current capabilities of the prototype through representative vibroacoustic benchmark cases and compare the results with those obtained from commercial solvers. Although the platform is still at an early stage, its modular design makes it easy to extend with new physics and formulations. By combining FEniCSx with industry-oriented tools and a user-friendly interface, this project aims to make high-fidelity vibroacoustic simulation more accessible to both researchers and practising engineers.


