---
title: 'POROMECHANICS TO INVESTIGATE THE IMPACT OF MECHANICAL LOADING ON HUMAN SKIN MICRO-CIRCULATION'
authors:
  - name:
      literal: 'Thomas Lavigne'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
    email: 'thomas.lavigne@polytechnique.edu'
  - name:
      literal: 'Stéphane Urcun'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Bérengère Fromy'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Audrey Josset-Lamaugarny'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Alexandre Lagache'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Camilo A. Suarez-Afanador'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Stéphane P. A. Bordas'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Pierre-Yves Rohan'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
  - name:
      literal: 'Giuseppe Sciumè'
    affiliations:
      - 'Laboratoire de mécanique des solides, Inria Research Center at Rennes University, LBTI Lyon, Claude Bernard University Lyon, Arts et Métiers Institute of Technology Paris, University of Luxembourg, University of Bordeaux, Institut Universitaire de France'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Thomas Lavigne (Laboratoire de mécanique des solides, CNRS, École polytechnique, Institut Polytechnique de Paris, Palaiseau, France)

Human skin functions as a complex multi-scale and multi-phase system where moving fluids significantly influence mechanical and biological responses. Effective management of skin injuries, such as pressure ulcers (PU), requires a deep understanding of this structural composition and mechanical behavior, particularly given that between 9% and 20% of hospitalized patients in Europe are affected (Vanderwee et al., 2007). This research introduces a hierarchical two-compartment poromechanical model that accounts for fluid distribution within the interstitium and blood micro-circulation. The model is grounded in a hierarchical porous media framework (Lavigne et al., 2025) that conceptualizes the interstitium as a biphasic system, distinguishing between the characteristic timescales of cells and interstitial fluid.

Experimental evaluation was performed using Laser Doppler Flowmetry (LDF) on 11 healthy volunteers. Controlled loads were applied directly to the skin via a specialized pivotmeter device (Fromy et al., 1998) to investigate ischaemic and hyperaemic responses. All numerical simulations were conducted using the open-source software FEniCSx v0.9.0. 

Results demonstrated that while absolute LDF values vary between individuals, relative responses to load-induced ischaemia and post-occlusive reactive hyperaemia (PORH) are comparable across sexes when normalized to basal blood flow. Sensitivity analysis identified Young's modulus and the vessel permeability exponent as dominant parameters governing the micro-circulatory response. This work successfully demonstrates the model's qualitative ability to replicate in vivo hemodynamic responses.

# References
Vanderwee, K., Clark, M., Dealey, C., Gunningberg, L., & Defloor, T. (2007). Pressure ulcer prevalence in Europe: a pilot study. Journal of evaluation in clinical practice, 13(2), 227-235. DOI: 10.1111/j.1365-2753.2006.00684.x

Fromy, B., Abraham, P., & Saumet, J. L. (1998). Non-nociceptive capsaicin-sensitive nerve terminal stimulation allows for an original vasodilatory reflex in the human skin. Brain research, 811(1-2), 166-168. DOI: 10.1016/s0006-8993(98)00973-1

Lavigne, T., Urcun, S., Fromy, B., Josset-Lamaugarny, A., Lagache, A., Suarez-Afanador, C. A., Bordas, S. P. A., Rohan, P. Y., & Sciumè, G. (2025). Hierarchical Poromechanical Approach to Investigate the Impact of Mechanical Loading on Human Skin Micro-Circulation. International journal for numerical methods in biomedical engineering, 41(7), e70066. DOI: 10.1002/cnm.70066


