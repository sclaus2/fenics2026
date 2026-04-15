---
title: 'Nonlinear Inversion Framework - Magnetic Resonance Elastography (MRE)'
authors:
  - name:
      literal: 'Henrik Palme'
    affiliations:
      - 'KTH - Royal Institute of Technology, Department of Biomedical Engineering and Health Systems, Stockholm, Sweden'
    email: 'hepalme@kth.se'
  - name:
      literal: 'Rodrigo Moreno'
    affiliations:
      - 'KTH - Royal Institute of Technology, Department of Biomedical Engineering and Health Systems, Stockholm, Sweden'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Henrik Palme (KTH - Royal Institute of Technology, Department of Biomedical Engineering and Health Systems, Stockholm, Sweden)

Magnetic Resonance Elastography (MRE) is an emerging technique to map the material properties of soft tissue using Magnetic Resonance Imaging (MRI). While the method has been clinically implemented to assess the liver, further developments have to be made to expand the technique to other organs, such as the brain (Pepin et al., 2022). In brain MRE, the material field has been linked to neurodegenerative diseases, such as Parkinson's disease (Olsson et al., 2025) and Alzheimer's (Murphy et al., 2011). One clear obstacle toward the clinical implementation is the inversion process, where the displacement field of the tissue is used to generate the material parameters. While various methods are utilised to conduct the inversion, what is commonly seen as the most robust is nonlinear inversion (NLI) using the finite element method. NLI utilises a subzone-based iterative optimisation process to, by consecutive forward simulations, reach a material field that most closely creates a corresponding displacement field that matches the measured data (McGarry et al., 2012). This method is, however, very computationally expensive, requiring CPU clusters. Furthermore, the current implementation of NLI utilises Fortran and is not open source. For the further development of brain MRE, it is clear that improvements have to be made to the inversion methods. An open source framework utilising FEniCS is therefore being developed, both as a transparent alternative to the current implementation of NLI, but also as a way to generate physically accurate synthetic displacement fields from phantom geometries and material fields. This would enable both the validation of other inversion techniques and new ways of regularising deep learning methods using synthetically generated fields. In its current stage, the framework is limited to smaller phantom geometries and 2D inversion. Full 3D inversion of brain MRE data is currently being developed.

# References
McGarry, M. D., Van Houten, E. E., Johnson, C. L., Georgiadis, J. G., Sutton, B. P., Weaver, J. B., & Paulsen, K. D. (2012). Multiresolution MR elastography using nonlinear inversion. Medical physics, 39(10), 6388-6396. DOI: 10.1118/1.4754649

Murphy, M. C., Huston, J., 3rd, Jack, C. R., Jr, Glaser, K. J., Manduca, A., Felmlee, J. P., & Ehman, R. L. (2011). Decreased brain stiffness in Alzheimer's disease determined by magnetic resonance elastography. Journal of magnetic resonance imaging : JMRI, 34(3), 494-498. DOI: 10.1002/jmri.22707

Olsson, C., Skorpil, M., Svenningsson, P., & Moreno, R. (2025). Effects of Parkinson's disease on mechanical and microstructural properties of the brain. NeuroImage. Clinical, 48, 103857. DOI: 10.1016/j.nicl.2025.103857

Pepin, K. M., Welle, C. L., Guglielmo, F. F., Dillman, J. R., & Venkatesh, S. K. (2022). Magnetic resonance elastography of the liver: everything you need to know to get started. Abdominal radiology (New York), 47(1), 94-114. DOI: 10.1007/s00261-021-03324-0


