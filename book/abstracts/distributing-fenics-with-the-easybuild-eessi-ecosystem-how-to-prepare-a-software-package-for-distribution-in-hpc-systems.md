---
title: 'Distributing FEniCS with the EasyBuild/EESSI ecosystem: how to prepare a software package for distribution in HPC systems'
authors:
  - name:
      literal: 'Georgios Kafanas'
    affiliations:
      - 'University of Luxembourg'
    email: 'georgios.kafanas@uni.lu'
  - name:
      literal: 'Hassan Md Jahid'
    affiliations:
      - 'University of Luxembourg'
  - name:
      literal: 'Julien Schleich'
    affiliations:
      - 'University of Luxembourg'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Georgios Kafanas (University of Luxembourg)

Very often getting a piece of scientific software working properly is the greatest impediment in starting using a new software system. Modern scientific software like FEniCS is usually composed of a large collection of software packages, and each of these package was dependencies of their own. Furthermore, the deployment targets of FEniCS are equally varied, with HPC centers hosting a variety of CPU architectures and models, and an equally varied amount of peripherals, like storage, accelerators, and networking. To manage this complexity, source code software management systems like EasyBuild and Spack have been developed. The process of distribution is now automated to a significant degree as well, with services like EESSI, which offers streaming access to a uniform and platform-optimized set of software modules and is deployed in all EuroHPC Federated centers.

Software distribution system operated in distinct phases, to compile source code, and then test, and deploy binaries. This talk will describe the deployment of FEniCS in the EasyBuild/EESSI ecosystem, that relies in EasyBuild for source code compilation, ReFrame for testing, and EESSI for the streaming of platform-optimized binaries. Emphasis will be placed on the subtle design modification required so that the software build and test systems follow the conventions in place in the EasyBuild/EESSI ecosystem. Although the presentation focuses on FEniCS and EESSI, the underlying principle and practices presented are applicable to the build and test systems of any piece of software that aims to be distributed with a modern software deployment system.

# References
Karakasis, V., Manitaras, T., Rusu, V. H., Sarmiento-Pérez, R., Bignamini, C., Kraushaar, M., ... Tomko, K. (2020). Enabling continuous testing of HPC systems using ReFrame. In Tools and Techniques for High Performance Computing (pp. 49-68). DOI: 10.1007/978-3-030-44728-1_3

Geimer, M., Hoste, K., & McLay, R. (2014, November). Modern Scientific Software Management Using EasyBuild and Lmod. 2014 First International Workshop on HPC User Support Tools. DOI: 10.1109/hust.2014.8

Gamblin, T., LeGendre, M., Collette, M. R., Lee, G. L., Moody, A., de Supinski, B. R., & Futral, S. (2015, November). The Spack package manager: bringing order to HPC software chaos. Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, 1-12. DOI: 10.1145/2807591.2807623

Dolstra, E. (2006). The Purely Functional Software Deployment Model (Doctoral dissertation, Utrecht, The Netherlands). Retrieved from https://researchr.org/publication/Dolstra2006

Dolstra, E., Löh, A., & Pierron, N. (2010). NixOS: a purely functional Linux distribution. Journal of Functional Programming, 20(5-6), 577-615. DOI: 10.1017/s0956796810000195

Malka, J., Zacchiroli, S., & Zimmermann, T. (2025, April). Does Functional Package Management Enable Reproducible Builds at Scale? Yes. 2025 IEEE/ACM 22nd International Conference on Mining Software Repositories (MSR), 775-787. DOI: 10.1109/msr66628.2025.00115


