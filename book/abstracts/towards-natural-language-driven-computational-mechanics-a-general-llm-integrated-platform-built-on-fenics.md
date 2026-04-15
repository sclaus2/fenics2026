---
title: 'Towards natural language-driven computational mechanics: A general LLM-integrated platform built on FEniCS'
authors:
  - name:
      literal: 'Guangjin Mou (presenter'
    affiliations:
      - 'Hong Kong University of Science and Technology'
    email: 'mouguangjin@ust.hk'
  - name:
      literal: 'Haoju Lin'
    affiliations:
      - 'Hong Kong University of Science and Technology'
  - name:
      literal: 'Tianju Xue'
    affiliations:
      - 'Hong Kong University of Science and Technology'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Guangjin Mou (Postdoctoral researcher in HKUST)

The increasing complexity of computational mechanics workflows, particularly in finite element analysis, creates a significant gap between high-level modeling intent and low-level numerical implementation. Recent advances in large language models (LLMs) offer a promising pathway to bridge this gap by enabling natural language interaction with scientific computing systems.

In this work, we present a general language-driven computational mechanics platform that integrates LLMs with the FEniCS ecosystem for PDE-based modeling and simulation. Building upon a modular agent architecture, the proposed framework connects user queries, LLM reasoning, and physics-based solvers through a structured tool interface. The system leverages a Model Context Protocol (MCP)-inspired design to expose FEniCS functionalities such as variational form definition, boundary condition specification, and solver execution as callable tools, enabling robust and controllable interaction between the LLM and the numerical backend.

Unlike existing approaches that are tightly coupled to specific numerical frameworks, the proposed platform exploits the symbolic variational formulation of FEniCS to support a wide range of problems in computational mechanics, including heat conduction, linear and nonlinear elasticity, and multi-physics simulations. The LLM operates as an orchestration layer that interprets user intent, constructs problem definitions, selects appropriate tools, and manages execution workflows, while explicit instruction design ensures reliability and prevents uncontrolled behavior.

The proposed framework transforms traditional finite element workflows into an interactive, language-driven process, significantly lowering the barrier to complex PDE modeling. This work demonstrates the feasibility of a new paradigm in computational mechanics, where natural language serves as a high-level interface for general-purpose simulation and design.


