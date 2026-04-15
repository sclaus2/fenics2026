---
title: 'Multi-physics Modelling of Nuclear Fusion Reactor Components using FESTIM'
authors:
  - name:
      literal: 'James Dark'
    affiliations:
      - 'MIT'
    email: 'darkj385@mit.edu'
  - name:
      literal: 'Remi Delaporte-Mathurin'
    affiliations:
      - 'MIT'
  - name:
      literal: 'Jorgen Dokken'
    affiliations:
      - 'Simula Research Laboratory'
  - name:
      literal: 'Huihua Yang'
    affiliations:
      - 'MIT'
  - name:
      literal: 'Chirag Khurana'
    affiliations:
      - 'MIT'
  - name:
      literal: 'Kaelyn Dunnel'
    affiliations:
      - 'MIT'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** James Dark (MIT)

The design of tritium-facing components in nuclear fusion reactors demands accurate multi-physics simulations that capture the complex interplay of physical phenomena across diverse spatial and temporal scales. This work presents a modelling approach centred on tritium transport, leveraging FESTIM, a flexible, open-source simulation tool for hydrogen isotope migration in fusion-relevant materials and geometries.

FESTIM has been developed with extensibility and interoperability in mind, making it well-suited to receive input from a range of high-fidelity physics codes. We present workflows in which outputs from OpenMC (neutron-induced tritium generation and nuclear heating) and OpenFOAM (temperature and velocity fields) are coupled with FESTIM to enable detailed, multiphysics modelling of tritium permeation, retention, and inventory under reactor-relevant conditions.

Applications include tritium migration in breeding blankets, plasma-facing components, and coupled liquid-solid domains such as heat exchangers or tritium extraction systems. In each case, external tools provide FESTIM with local source terms and operational conditions, enabling accurate evaluation of tritium transport. Validation of these multi-physics workflows has begun through collaborative projects, such as LIBRA (MIT), but further experimental validation remains a critical need for modelling tritium-facing components.

This framework supports design iteration, analysis of experimental setups, and extrapolation to reactor scale, accelerating the development of fuel-cycle components. The Python-based architecture of FESTIM also facilitates automated, scriptable workflows, making it well-suited for integration into iterative component optimisation loops. With permissive licensing and a growing user community, FESTIM is well-positioned as a flexible code for integrated multi-physics tritium transport modelling.


