#!/usr/bin/env python3
"""
Arithmetic Phase Transition Diagram Generator

Creates a visualization of the phase transition from thermal gas (Q41) 
to condensed crystal (Q47) in prime-generating polynomials.

Reference: Chen, R. (2026). Arithmetic Quantum Waveguides: The Ouroboros 
Phase Transition in Safe Prime Polynomials.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

# Set up figure style
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'DejaVu Sans'

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
plt.subplots_adjust(wspace=0.15)

# === Panel 1: Q41 (Hot Gas Phase) ===
ax1 = axes[0]
ax1.set_xlim(-0.5, 10.5)
ax1.set_ylim(-3, 12)
ax1.set_aspect('equal')

# Random scattered points (thermal gas)
np.random.seed(42)
n_points = 50
x = np.random.uniform(1, 9, n_points)
y = np.random.uniform(1, 9, n_points)
colors = plt.cm.Reds(np.random.uniform(0.4, 0.9, n_points))
sizes = np.random.uniform(50, 130, n_points)

ax1.scatter(x, y, c=colors, s=sizes, alpha=0.8, edgecolors='darkred', linewidths=0.5)

# Add thermal motion arrows
for i in range(10):
    dx = np.random.uniform(-0.5, 0.5)
    dy = np.random.uniform(-0.5, 0.5)
    ax1.annotate('', xy=(x[i]+dx, y[i]+dy), xytext=(x[i], y[i]),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.6, lw=1.5))

# Title - two lines
ax1.text(5, 11, r'$\mathbf{Q_{41}}$', fontsize=16, ha='center', va='bottom', 
         fontweight='bold', color='darkred')
ax1.text(5, 10.2, 'Thermal Gas Phase', fontsize=13, ha='center', va='bottom', 
         color='darkred')

# Top label box
bbox1 = FancyBboxPatch((0.5, 9.0), 9, 0.9, boxstyle="round,pad=0.05", 
                        facecolor='mistyrose', edgecolor='darkred', linewidth=1.5)
ax1.add_patch(bbox1)
ax1.text(5, 9.45, 'DISORDERED: Maxwell-Boltzmann Gas', fontsize=10, ha='center', 
         color='darkred', fontweight='bold')

# Bottom labels
ax1.text(5, -1.5, r'$T_A > T_c$', fontsize=14, ha='center', color='darkred', fontweight='bold')
ax1.text(5, -2.5, r'$I(q) = 6$ (HIGH)', fontsize=11, ha='center', color='darkred')

ax1.axis('off')

# === Panel 2: Phase Transition Arrow ===
ax2 = axes[1]
ax2.set_xlim(-0.5, 10.5)
ax2.set_ylim(-3, 12)
ax2.set_aspect('equal')

# Large arrow
ax2.annotate('', xy=(9, 5), xytext=(1, 5),
            arrowprops=dict(arrowstyle='-|>', color='purple', lw=6, 
                           mutation_scale=35))

# Critical point circle
circle = Circle((5, 5), 2.0, fill=True, facecolor='gold', edgecolor='purple', linewidth=4)
ax2.add_patch(circle)
ax2.text(5, 5, r'$\mathbf{T_c}$', fontsize=24, ha='center', va='center', 
         fontweight='bold', color='purple')

# Upper labels
ax2.text(5, 10.5, 'ARITHMETIC', fontsize=16, ha='center', va='center', 
         fontweight='bold', color='purple')
ax2.text(5, 9.3, 'PHASE TRANSITION', fontsize=14, ha='center', va='center', 
         fontweight='bold', color='purple')

# Lower formulas
ax2.text(5, 2.0, r'$I(q): 6 \longrightarrow 2$', fontsize=14, ha='center', 
         va='center', color='purple')
ax2.text(5, 0.8, r'$\sigma_{scatt}:$ HIGH $\longrightarrow$ MIN', fontsize=11, 
         ha='center', va='center', color='purple')

# Bottom Ouroboros label
ax2.text(5, -1.5, 'OUROBOROS LIMIT', fontsize=13, ha='center', 
         fontweight='bold', color='darkviolet')

ax2.axis('off')

# === Panel 3: Q47 (Condensed Crystal Phase) ===
ax3 = axes[2]
ax3.set_xlim(-0.5, 10.5)
ax3.set_ylim(-3, 12)
ax3.set_aspect('equal')

# Ordered lattice
grid_x, grid_y = np.meshgrid(np.linspace(1.5, 8.5, 6), np.linspace(1.5, 8.5, 6))
ax3.scatter(grid_x, grid_y, c='royalblue', s=60, alpha=0.9, edgecolors='darkblue', linewidths=1)

# Draw lattice lines
for i in range(6):
    ax3.plot([1.5, 8.5], [1.5 + i*7/5, 1.5 + i*7/5], 'b-', alpha=0.2, lw=1)
    ax3.plot([1.5 + i*7/5, 1.5 + i*7/5], [1.5, 8.5], 'b-', alpha=0.2, lw=1)

# Highlight quadruplet (standing wave node)
quad_x = [2.9, 4.3, 5.7, 7.1]
quad_y = [5.0, 5.0, 5.0, 5.0]
ax3.scatter(quad_x, quad_y, c='cyan', s=280, edgecolors='blue', linewidths=3, zorder=10)
ax3.plot(quad_x, quad_y, 'c-', lw=4, zorder=9)

# Annotation
ax3.annotate('QUADRUPLET', xy=(5, 5), xytext=(5, 7.8),
            fontsize=10, ha='center', color='darkblue', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='darkblue', lw=2))
ax3.text(5, 7.0, '(Standing Wave Node)', fontsize=9, ha='center', color='darkblue')

# Title
ax3.text(5, 11, r'$\mathbf{Q_{47}}$', fontsize=16, ha='center', va='bottom',
         fontweight='bold', color='darkblue')
ax3.text(5, 10.2, 'Condensed Crystal Phase', fontsize=13, ha='center', va='bottom',
         color='darkblue')

# Top label box
bbox3 = FancyBboxPatch((0.5, 9.0), 9, 0.9, boxstyle="round,pad=0.05", 
                        facecolor='lightcyan', edgecolor='darkblue', linewidth=1.5)
ax3.add_patch(bbox3)
ax3.text(5, 9.45, 'ORDERED: Bose-Einstein Condensate', fontsize=10, ha='center', 
         color='darkblue', fontweight='bold')

# Bottom labels
ax3.text(5, -1.5, r'$T_A < T_c$', fontsize=14, ha='center', color='darkblue', fontweight='bold')
ax3.text(5, -2.5, r'$I(q) = 2$ (MINIMAL)', fontsize=11, ha='center', color='darkblue')

ax3.axis('off')

# Main title
plt.suptitle('Arithmetic Phase Transition: From Thermal Gas to Quantum Crystal', 
             fontsize=18, fontweight='bold', y=0.98)

# Save figure
plt.savefig('fig_phase_transition.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Figure saved: fig_phase_transition.png")
plt.close()
