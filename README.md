# Arithmetic Quantum Waveguides

**The Ouroboros Phase Transition in Safe Prime Polynomials**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18305185.svg)](https://doi.org/10.5281/zenodo.18305185)

## Abstract

This repository contains the paper, figures, and analysis scripts for our study of arithmetic phase transitions in prime-generating polynomials. We demonstrate that the polynomial $Q(n) = n^{47} - (n-1)^{47}$ acts as a "transparent waveguide" that preserves prime clustering coherence, exhibiting behavior analogous to Bose-Einstein Condensation.

**Key Finding:** Direct deep-space probing at $n \approx 10^{44}$ confirms a **Structural Boost Factor of 113×** relative to uncorrelated Poisson expectations—the first experimental evidence for arithmetic crystallization at cosmological scales.

## Repository Structure

```
Arithmetic-Quantum-Waveguides/
├── README.md
├── paper/
│   ├── Ouroboros_Paper_GUT.pdf    # Main paper
│   └── Ouroboros_Paper_GUT.tex    # LaTeX source
├── figures/
│   ├── fig1_riemann_correlation.png
│   ├── fig3_quadruplet_positions.png
│   ├── fig4_lattice_comparison.png
│   └── fig_phase_transition_v2.png
└── scripts/
    ├── enhancement_calculation.py  # 113× enhancement derivation
    └── phase_diagram.py            # Phase transition figure generator
```

## Data Source

The raw data (18,356,706 verified Q47 primes, 15 quadruplet coordinates) is available in our companion repository:

📊 **[Polynomial-Prime-Quadruplets](https://github.com/Ruqing1963/Polynomial-Prime-Quadruplets)**

Archived dataset: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18305185.svg)](https://doi.org/10.5281/zenodo.18305185)

## Key Results

| Result | Value | Significance |
|--------|-------|--------------|
| Quadruplets detected | 15 | vs 0 for Q41, Q61 |
| Riemann correlation | r = 0.994 | Standing wave nodes |
| Enhancement at 10^44 | 113× | Coherence persists |
| Magic number bound | k_max = 28 | Lattice constant |

## Theoretical Framework

### Arithmetic Temperature

We define the effective temperature as proportional to the interference potential:

$$k_B T_A \propto I(q) = d(q-1) - 2$$

where $d(n)$ is the divisor function.

### Phase Transition

| Phase | Polynomial | I(q) | Behavior |
|-------|------------|------|----------|
| Thermal Gas | Q41, Q61 | 6-10 | Disordered, no quadruplets |
| **Condensed** | **Q47** | **2** | **Ordered, 15 quadruplets** |

Critical temperature corresponds to $I(q) \lesssim 3$.

## Figures

### Phase Transition Diagram
![Phase Transition](figures/fig_phase_transition_v2.png)

### Riemann Zero Correlation
![Riemann Correlation](figures/fig1_riemann_correlation.png)

## Related Publications

1. **Math Paper:** Chen, R. (2026). Prime Clustering in Polynomial Q(n)=n^47-(n-1)^47. [Zenodo](https://doi.org/10.5281/zenodo.18305185)

2. **Information Entropy Paper:** Chen, R. (2026). Information Entropy and Structural Isomorphism in Arithmetic Systems: The Magic Number 28. [Zenodo](https://doi.org/10.5281/zenodo.18259473)

## Citation

If you use this work, please cite:

```bibtex
@article{chen2026waveguides,
  title={Arithmetic Quantum Waveguides: The Ouroboros Phase Transition in Safe Prime Polynomials},
  author={Chen, Ruqing},
  year={2026},
  note={Preprint}
}

@dataset{chen2026q47data,
  author={Chen, Ruqing},
  title={Prime Clustering in Polynomial Q(n)=n^47-(n-1)^47: Complete Dataset},
  year={2026},
  publisher={Zenodo},
  doi={10.5281/zenodo.18305185}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Contact

**Ruqing Chen**  
GUT Geoservice Inc., Montreal, Canada  
Email: ruqing@hotmail.com

---

*"The Ouroboros bites its tail. At the end of infinity, we find perfect order."*
