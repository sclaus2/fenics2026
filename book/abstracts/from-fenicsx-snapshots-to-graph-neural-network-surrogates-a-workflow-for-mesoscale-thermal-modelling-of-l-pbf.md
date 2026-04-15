---
title: 'From FEniCSx Snapshots to Graph Neural Network Surrogates: A Workflow for Mesoscale Thermal Modelling of L-PBF'
authors:
  - name:
      literal: 'Quentin SCHMID'
    affiliations:
      - 'RMIT Europe'
    email: 'quentin.schmid@rmit.edu.au'
  - name:
      literal: 'Andrey MOLOTNIKOV'
    affiliations:
      - 'RMIT Center for Additive Manufacturing'
  - name:
      literal: 'Maciej MAZUR'
    affiliations:
      - 'RMIT Center for Additive Manufacturing'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Quentin SCHMID (RMIT Europe)

Laser Powder Bed Fusion (L-PBF) involves highly localised, transient heat transfer with non-linear material behaviour and phase change, making high-fidelity simulations expensive when exploring many process parameters. This work builds a flexible thermal solver workflow in FEniCSx and uses it as a data source for a graph-based surrogate, with a strong focus on implementation details.

The solver tackles a non-linear heat equation in enthalpy form: conductivity, density and effective heat capacity depend on temperature, and melting/solidification is handled via an enthalpy-based transition between solid and liquid. A laser-like volumetric source is prescribed as a Gaussian term defined by power, radius and position. Time integration is implicit with a non-linear Newton-Krylov solve configured for robustness across strong thermal gradients and multi-material regions (substrate plus powder).

Geometry and meshing are generated via scripted Gmsh workflows: separate substrate and powder volumes, physical groups for domains and boundaries, and local refinement around the laser and within the powder layer. Meshes are converted with meshio to XDMF/HDF5 and re-imported into FEniCSx with consistent connectivity and markers. Particular care is taken with DOF-node alignment, index conventions and explicit topology creation, as these are often the fragile parts of such pipelines.

On top of this solver backbone, a Graph Neural Network surrogate is introduced only in a second step: snapshots of temperature and liquid fraction are extracted from HDF5, turned into graphs (nodal coordinates, connectivity, node/edge features) and normalised. An Encode-Process-Decode GNN based on message passing is trained to approximate nodal fields. The emphasis is the end-to-end, implementation-oriented workflow-Gmsh -> FEniCSx -> XDMF/HDF5 -> graph data-that can serve as a robust basis for surrogate modelling in more realistic L-PBF scenarios.


