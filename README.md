# Percolation Threshold Estimation using Monte Carlo Simulation

## Overview
This project investigates the percolation phenomenon in 2D grids using Monte Carlo simulation.  
The goal is to estimate the **percolation threshold**, a critical value at which a system transitions from a non-percolating to a percolating state.

Percolation is a classical problem in statistical physics and probability theory, with applications in network connectivity, material science, and epidemiology.

---

## Methodology

The approach consists of:

1. Modeling an \( N \times N \) grid where sites can be open or blocked  
2. Randomly opening sites until the system percolates  
3. Repeating the experiment multiple times (Monte Carlo simulation)  
4. Estimating:
   - Mean percolation threshold  
   - Variance  
   - Confidence intervals  
5. Analyzing the probability of percolation as a function of open sites  

---

## Implementation Details

- Connectivity is efficiently handled using the :contentReference[oaicite:0]{index=0} data structure  
- Weighted quick union with path compression is used for performance optimization  
- The simulation is designed to be reproducible with controlled randomness  

---

## Results

The simulation produces:

- Distribution of percolation thresholds  
- Estimated mean and variance  
- Confidence intervals  
- Probability curves (sigmoid behavior)

### Example Insights
- The percolation threshold converges to approximately **0.59** for large grids  
- The probability curve exhibits a sharp transition around the critical point  

---

## Project Structure
```
percolation-threshold-monte-carlo/
│
├── WeightedQuickUnionUF.py # Disjoint-set structure (Union-Find)
├── Percolation.py # Grid and percolation logic
├── MonteCarloSimulation.ipynb # Simulation engine (main)
├── README.md
└── Requirements.txt
```

## How to Run

1. Clone the repository:
git clone https://github.com/KleberMouraJr89/percolation-threshold-monte-carlo.git

2. Enter the project directory
cd percolation-threshold-monte-carlo

3. Install dependencies
pip install -r requirements.txt

4. Run the simulation
python MonteCarloSimulation.ipynb
