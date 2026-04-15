---
title: 'Developing numerical tools to improve the diagnosis of peripheral artery disease'
authors:
  - name:
      literal: 'Luke Barratt'
    affiliations:
      - 'University of Leeds'
    email: 'scljb@leeds.ac.uk'
  - name:
      literal: 'Al Benson'
    affiliations:
      - 'University of Leeds'
  - name:
      literal: 'Marc Bailey'
    affiliations:
      - 'University of Leeds'
  - name:
      literal: 'Toni Lassila'
    affiliations:
      - 'University of Leeds'
  - name:
      literal: 'Yasina Somani'
    affiliations:
      - 'University of Leeds'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Luke J Barratt (University of Leeds)

Peripheral artery disease (PAD) is an age-related condition present in >10% of adults over 65 years and is characterised by atherosclerotic narrowing of arteries classically affecting the legs [1]. This reduces oxygen delivery to skeletal muscle and leads to pain during walking (intermittent claudication, IC) [2]. Early diagnosis of PAD is key to reducing risk of cardiovascular events; a risk that is two-fold greater in PAD than in those with stable coronary artery disease [3].The gold-standard diagnostic method for PAD is the ankle-brachial index (ABI; the ratio of leg to arm systolic blood pressure), sometimes supplemented with ultrasound, MRI or CT [4]. However, traditional diagnostic methods do not always detect PAD, particularly in patients with calcified arteries or atypical presentations often occurring in women. As a result, PAD frequently remains underdiagnosed and undertreated compared with other cardiovascular conditions [5].
To address the limitations of current diagnostic methods, we are developing numerical methods to improve risk prediction algorithms by assessing factors local to the occluded limbs. Three mathematical models are being developed that can assess: (1) blood flow in the large arteries using 1D Navier-Stokes for flow in compliant tubes [6], (2) microvascular flow using Poiseuille's Law in networks [7], (3) dilation of vascular beds mediated by shear forces within the microvasculature and metabolic activity in the muscle; and (4) lumped oxygenation of the skeletal muscle using a coupled set of equations representing oxygen transport in the blood and muscle fibres and cellular metabolism [8]. Ultrasond and NIRS data during transition to exercise in will be used to validate the numerical model. 
By linking vascular anatomy and function, plaque severity, and muscle metabolism on oxygen dynamics, this work aims to help identify key causes of IC in PAD patients and guide support targeted strategies for improved diagnosis and treatment.

# References
[1] Houghton, J. S. M., Saratzis, A. N., Sayers, R. D., & Haunton, V. J. (2024). New Horizons in Peripheral Artery Disease. Age and Ageing, 53(6), afae114.

[2] Fowkes, F. G. R., Rudan, D., Rudan, I., Aboyans, V., Denenberg, J. O., McDermott, M. M., Norman, P. E., Sampson, U. K. A., Williams, L. J., Mensah, G. A., & Criqui, M. H., 2013, Comparison of global estimates of prevalence and risk factors for peripheral artery disease in 2000 and 2010: a systematic review and analysis. The Lancet, 382(9901), pp. 1329-1340.

[3] Sprenger, L., Mader, A., Larcher, B., Mächler, M., Vonbank, A., Zanolin-Purin, D., Leiherer, A., Muendlein, A., Drexel, H., & Saely, C. H. (2021). Type 2 diabetes and the risk of cardiovascular events in peripheral artery disease versus coronary artery disease. BMJ Open Diabetes Research & Care, 9(2), e002407. 

[4] Parwani, D., Ahmed, M. A., Mahawar, A., & Gorantla, V. R. (2023). Peripheral Arterial Disease: A Narrative Review. Cureus, 15(6), e40267.

[5] Pabon, M., Cheng, S., Altin, S. E., Sethi, S., Nelson, M. D., et al. (2022). Sex differences in peripheral artery disease. Circulation Research, 130(4), 496-511.

[6] Alastruey, J., Parker, K. H., & Sherwin, S. J. (2012). Arterial pulse wave haemodynamics. In S. Anderson (Ed.), 11th International Conference on Pressure Surges (pp. 401-443). Virtual PiE Led t/a BHR Group. 

[7] Karshafian, R., Burns, P. N., & Henkelman, M. R. (2003). Transit time kinetics in ordered and disordered vascular trees. Physics in medicine and biology, 48(19), 3225-3237.

[8] Lai, N., Camesasca, M., Saidel, G.M. et al. (2007) Linking Pulmonary Oxygen Uptake, Muscle Oxygen Utilization and Cellular Metabolism during Exercise. Ann Biomed Eng 35, 956-969


