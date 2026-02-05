"""Hoshen-Kopelman algorithm for cluster labeling on 2D lattices.

This module provides the main interface to the Hoshen-Kopelman algorithm,
which efficiently labels connected clusters of occupied sites on a 2D grid.
The algorithm uses a two-pass approach with union-find for label merging.

Reference:
    Hoshen, J., & Kopelman, R. (1976). Percolation and cluster distribution.
    I. Cluster multiple labeling technique and critical concentration algorithm.
    Physical Review B, 14(8), 3438.
"""

import numpy as np
from plot import plot_labels, plot_occupancy
from pass1 import pass1
from pass2 import pass2
from gen_occupancy import gen_random_occupancy
from percolate import percolates


def hoshen_kopelman(occ):
    """Label connected clusters using the Hoshen-Kopelman algorithm.

    Identifies and labels all connected clusters of occupied sites on a
    2D lattice using 4-connectivity (up, down, left, right neighbors).

    Parameters
    ----------
    occ : array_like
        2D boolean or integer array where True/non-zero indicates occupied sites.

    Returns
    -------
    labels_lattice : numpy.ndarray
        2D integer array where each occupied site is labeled with its cluster ID.
        Unoccupied sites have label 0.
    unique_labels : set
        Set of unique cluster labels (excluding 0).
    """
    labels_lattice, to_be_merged = pass1(occ)
    labels_lattice, unique_labels = pass2(labels_lattice, to_be_merged)
    return labels_lattice, unique_labels


def parse_args():
    """Parse command-line arguments for the Hoshen-Kopelman demo.

    Returns
    -------
    argparse.Namespace
        Parsed arguments with attributes:
        - l: Grid size (int)
        - p: Occupation probability (float)
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Demonstrate Hoshen-Kopelman cluster labeling"
    )
    parser.add_argument("-l", type=int, default=32, help="Grid size")
    parser.add_argument(
        "-p", type=float, default=0.3, help="probability that a site is occupied (0..1)"
    )
    return parser.parse_args()





if __name__ == "__main__":
    print("=== Hoshen-Kopelman Algorithm Demo ===\n")

    args = parse_args()
    print(f"Grid size: {args.l}x{args.l}")
    print(f"Occupation probability: {args.p}")

    occ = gen_random_occupancy((args.l, args.l), args.p)
    actual_p = np.sum(occ) / np.prod(occ.shape)
    print(f"Actual occupation fraction: {actual_p:.3f}")

    print("\nStep 1: Visualizing occupancy...")
    plot_occupancy(occ, title=f"Occupancy (p={args.p})",fname="hk_occupancy.png")

    print("Step 2: Pass 1 - Provisional labeling...")
    labels_lattice, to_be_merged = pass1(occ)
    plot_labels(labels_lattice, title="After pass 1 (provisional labels)", fname="hk_provisional_labels.png")

    print("Step 3: Pass 2 - Resolving equivalences...")
    labels_lattice, unique_labels = pass2(labels_lattice, to_be_merged)
    plot_labels(labels_lattice, title="After pass 2 (final labels)",fname="hk_final_labels.png")

    print(f"\nResult: {len(unique_labels)} clusters identified")
    print(f"Percolation: {percolates(labels_lattice)}")

