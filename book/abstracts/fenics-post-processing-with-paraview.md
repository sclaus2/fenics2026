---
title: 'FEniCS Post-processing with ParaView'
authors:
  - name:
      literal: 'Louis Gombert'
    affiliations:
      - 'Kitware'
    email: 'louis.gombert@kitware.com'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Louis Gombert (Kitware)

In this presentation, we introduce the open source post-processing toolkit ParaView [0]. ParaView is an industry-standard graphical application that also provides a Python API, used for interactive 3D data exploration and analysis. ParaView can efficiently process data in parallel up to billions of cells, either from files on disk, or from in-memory data using the Catalyst framework. We show the different ways ParaView can be deployed: as a standalone graphical application, using remote rendering on a supercomputer, on the web through the Python interface. Then, we show how ParaView can be connected to FEniCS simulations, how its data model binds to ParaView data structures, and how it can produce publication-ready image and video renderings easily. We also discuss prospective topics regarding higher-order element support and advanced filters usage.

# References
[0] Ahrens, J., Geveci, B., & Law, C. (2005). Paraview: An end-user tool for large data visualization. The visualization handbook, 717(8).


