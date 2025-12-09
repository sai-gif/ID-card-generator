# MPI Projects README

This repository contains MPI-based C++ programs for parallel computing exercises:

1. **Parallel Matrix Multiplication (Q1.cpp)**
2. **Monte Carlo Pi Calculation (Q2Serial.cpp & Q2Parallel.cpp)**
3. **MPI Laplace Solver (Q3.cpp & Q32D.cpp)**

---

## **Q1: Parallel Matrix Multiplication**

**Description:**  
This program performs parallel multiplication of two square matrices using MPI with 1-D row-wise partitioning.

**Files:**  
- `Q1.cpp` — MPI matrix multiplication program.

**Requirements:**  
- MPI library (e.g., OpenMPI)  
- C++ compiler with MPI support (`mpicxx`)

**Compilation:**  
```bash
mpicxx -O2 -o matmul Q1.cpp
