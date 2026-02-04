"""Percolation threshold analysis through Monte Carlo sweeps.

This module provides functions to estimate the percolation probability
as a function of site occupation probability by running many random
samples and checking for spanning clusters.
"""

import numpy as np
from hk import hoshen_kopelman
from percolate import percolates_lr, percolates_tb
from gen_occupancy import gen_random_occupancy
import matplotlib.pyplot as plt
import matplotlib

def estimate_spanning_probability(L, p_values, n_samples=200, direction="lr", seed=0):
    """Estimate spanning probability for different occupation probabilities.

    For each occupation probability p, generates n_samples random lattices
    and counts the fraction that have a spanning cluster.

    Parameters
    ----------
    L : int
        Linear size of the square lattice (L x L grid).
    p_values : array_like
        Array of occupation probabilities to test.
    n_samples : int, optional
        Number of random samples per probability value. Default is 200.
    direction : str, optional
        Direction to check for percolation: "lr" (left-right) or "tb" (top-bottom).
        Default is "lr".
    seed : int, optional
        Seed for the random number generator. Default is 0.

    Returns
    -------
    numpy.ndarray
        Array of spanning probabilities, one for each p value.

    Raises
    ------
    ValueError
        If direction is not "lr" or "tb".
    """
    rng = np.random.default_rng(seed)
    probs = []

    for p in p_values:
        count = 0
        for _ in range(n_samples):
            occ = gen_random_occupancy((L, L), p, rng)
            labels_lattice, _ = hoshen_kopelman(occ)

            if direction == "lr":
                ok = percolates_lr(labels_lattice)
            elif direction == "tb":
                ok = percolates_tb(labels_lattice)
            else:
                raise ValueError("direction must be 'lr' or 'tb'")

            count += int(ok)

        probs.append(count / n_samples)

    return np.array(probs)


def sweep_and_plot(
    L_list=(16, 32, 64, 128, 256),
    p_min=0.52,
    p_max=0.66,
    n_p=31,
    n_samples=100,
    direction="lr",
    seed=0,
):
    """Run percolation sweep for multiple system sizes and plot results.

    Generates a plot of spanning probability vs. occupation probability
    for different lattice sizes, useful for studying finite-size scaling
    near the percolation threshold.

    Parameters
    ----------
    L_list : tuple of int, optional
        List of lattice sizes to simulate. Default is (16, 32, 64, 128, 256).
    p_min : float, optional
        Minimum occupation probability. Default is 0.52.
    p_max : float, optional
        Maximum occupation probability. Default is 0.66.
    n_p : int, optional
        Number of probability points to sample. Default is 31.
    n_samples : int, optional
        Number of Monte Carlo samples per point. Default is 100.
    direction : str, optional
        Direction to check for percolation: "lr" or "tb". Default is "lr".
    seed : int, optional
        Base seed for random number generation. Default is 0.

    Notes
    -----
    The percolation threshold for 2D site percolation with 4-connectivity
    is approximately p_c = 0.5927.
    """
    matplotlib.rcParams.update({"font.size": 20})
    p_values = np.linspace(p_min, p_max, n_p)

    plt.figure(figsize=(12,9))
    for i, L in enumerate(L_list):
        print(f"Running L={L}...", end=" ", flush=True)
        P = estimate_spanning_probability(
            L, p_values, n_samples=n_samples, direction=direction, seed=seed + 1000 * i
        )
        print("done")
        plt.plot(p_values, P, linewidth=2, markersize=5, label=f"L={L}")

    plt.xlabel("occupation probability p")
    plt.ylabel(f"spanning probability P_span ({direction})")
    plt.ylim(-0.02, 1.02)
    plt.legend()
    plt.grid(True)
    plt.savefig("percolation_versus_occupancy.png", dpi=600)
    plt.show()


if __name__ == "__main__":
    print("=== Percolation Threshold Analysis ===\n")
    print("Theoretical 2D site percolation threshold: p_c ≈ 0.5927")
    print("Running simulations...\n")

    sweep_and_plot(
        L_list=(16, 32),
        p_min=0.52, p_max=0.66, n_p=25,
        n_samples=300,
        direction="lr",
        seed=1,
    )

    print("\nSaved plot to: percolation_versus_occupancy.png")
