"""Generate random occupancy grids for percolation simulations.

This module provides functions to create 2D boolean arrays representing
site occupancy on a lattice, where each site is occupied with a given
probability.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from plot import plot_occupancy


def gen_random_occupancy(shape, prob, rng=np.random.default_rng()):
    """Generate a random occupancy grid.

    Creates a 2D boolean array where each site is independently occupied
    with probability `prob`.

    Parameters
    ----------
    shape : tuple of int
        Shape of the output array (rows, cols).
    prob : float
        Probability that each site is occupied (0 to 1).
    rng : numpy.random.Generator, optional
        Random number generator instance. Defaults to a new default generator.

    Returns
    -------
    numpy.ndarray
        Boolean array where True indicates an occupied site.
    """
    TODO: Ziehen Sie mit Hilfe von rng.random() ein 2D-Array aus Zufallszahlen
    zwischen 0 und 1. Erzeugen Sie daraus ein 2D Array, in dem (im Mittel)
    in einem Anteil `prob` der Elemente True steht.
    
    return occupancy

if __name__ == "__main__":
    print("=== Random Occupancy Generation Demo ===\n")

    shape = (20, 30)
    prob = 0.2

    occ = gen_random_occupancy(shape, prob)
    print(f"Grid shape: {shape}")
    print(f"Target probability: {prob}")
    print(f"Actual fraction occupied: {np.sum(occ) / np.prod(occ.shape):.3f}")
    print("\nOccupancy grid (1=occupied, 0=empty):")
    print(np.array(occ, dtype=int))
    plot_occupancy(occ, title=f"Random occupancy (p={prob})")

