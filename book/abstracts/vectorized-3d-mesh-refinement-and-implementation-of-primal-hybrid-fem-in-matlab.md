---
title: 'Vectorized 3D mesh refinement and implementation of primal hybrid FEM in MATLAB'
authors:
  - name:
      literal: 'Harish Nagula Mallesham'
    affiliations:
      - 'Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India. High Energy Materials Research Laboratory, Sutarwadi, Pune, Maharashtra, 411021, India. Department of Mathematics, Faculty of Science, University of South Bohemia, Branišovská 31, 37005 Budweis, Czech Republic. Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India.'
  - name:
      literal: 'Sharat Gaddam'
    affiliations:
      - 'Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India. High Energy Materials Research Laboratory, Sutarwadi, Pune, Maharashtra, 411021, India. Department of Mathematics, Faculty of Science, University of South Bohemia, Branišovská 31, 37005 Budweis, Czech Republic. Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India.'
  - name:
      literal: 'Jan Valdman'
    affiliations:
      - 'Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India. High Energy Materials Research Laboratory, Sutarwadi, Pune, Maharashtra, 411021, India. Department of Mathematics, Faculty of Science, University of South Bohemia, Branišovská 31, 37005 Budweis, Czech Republic. Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India.'
  - name:
      literal: 'Sanjib Kumar Acharya.'
    affiliations:
      - 'Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India. High Energy Materials Research Laboratory, Sutarwadi, Pune, Maharashtra, 411021, India. Department of Mathematics, Faculty of Science, University of South Bohemia, Branišovská 31, 37005 Budweis, Czech Republic. Institute of Chemical Technology Mumbai IndianOil Odisha Campus, Bhubaneswar, Odisha, 751013, India.'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Harish Mallesham Nagula (Dr)

This article presents a MATLAB software package for solving a three-dimensional (3D) second-order elliptic problem with mixed boundary conditions using the primal hybrid finite element method (FEM). First, we introduce a novel fast 3D uniform finite element mesh refinement technique implemented in MATLAB and establish the Nodes-to-Edge and Faces-to-Tetrahedron connectivity through an efficient and systematic approach. We then describe an efficient MATLAB assembly procedure for the 3D lowest-order primal hybrid finite element matrices. Furthermore, we develop a vectorized Schur complement solver, where the computational improvement over MATLAB's default direct solver (mldivide) arises from reducing the original block system to a substantially smaller Schur complement system. The run-time performance of the software is demonstrated through numerical experiments.


