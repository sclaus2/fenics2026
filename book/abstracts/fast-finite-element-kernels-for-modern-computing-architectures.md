---
title: 'Fast Finite Element Kernels for Modern Computing Architectures'
authors:
  - name:
      literal: 'Joseph P. Dean'
    affiliations:
      - 'University of Cambridge'
    email: 'jpd62@cam.ac.uk'
  - name:
      literal: 'Igor A. Baratta'
    affiliations:
      - 'NVIDIA'
  - name:
      literal: 'Chris N. Richardson'
    affiliations:
      - 'University of Cambridge'
  - name:
      literal: 'Garth N. Wells'
    affiliations:
      - 'University of Cambridge'
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

**Submission type:** Presentation

**Presenter:** Joseph Dean (University of Cambridge)

Accurate simulation of increasingly complex systems requires numerical methods that can fully exploit modern HPC hardware. This demands algorithms that minimise memory traffic, make effective use of memory hierarchies, and exploit vectorisation. In this work, we present high-order matrix-free finite element kernels designed for modern CPU and GPU architectures and examine the key implementation challenges involved in achieving high performance. Using parameterisable algorithms that allow tuning for specific hardware, we explore how the balance of memory pressure can be shifted between different hardware components. We use profiling and benchmarking to investigate the effects on cache reuse, memory bandwidth, and register pressure. Performance results are presented for a range of hardware, including Intel Sapphire Rapids and NVIDIA Grace CPUs, as well as AMD MI300X and NVIDIA GH200 GPUs. In addition, we show that low-order methods can remain more competitive than is sometimes assumed.


