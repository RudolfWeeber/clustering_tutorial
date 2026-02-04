"""Percolation detection for labeled lattices.

This module provides functions to check whether a cluster spans
(percolates) across a 2D lattice in different directions.
"""

import numpy as np


def percolates_lr(labels_lattice):
    """Check if any cluster spans from left to right.

    A cluster percolates left-to-right if the same non-zero label
    appears in both the leftmost and rightmost columns.

    Parameters
    ----------
    labels_lattice : numpy.ndarray
        2D integer array of cluster labels (0 = unoccupied).

    Returns
    -------
    bool
        True if at least one cluster spans left to right.
    """
    #TODO: Erzeugen Sie die Mengen left und right, die 
    # die Labels am linken und rechten Rand von labels_lattice enthalten,
    # also die beiden Raender.
    # Nutzen Sie dazu set(), np.unique() und eine Slice. 
    # left  TODO
    # right  TODO

    # Um herauszufinden, ob es ein Cluster gibt, das vom linken
    # zum rechten Rand reicht, überprüfen Sie, ob es
    # Überschneidungen zwischen den beiden Mengen (left und right) gibt.



def percolates_tb(labels_lattice):
    """Check if any cluster spans from top to bottom.

    A cluster percolates top-to-bottom if the same non-zero label
    appears in both the top and bottom rows.

    Parameters
    ----------
    labels_lattice : numpy.ndarray
        2D integer array of cluster labels (0 = unoccupied).

    Returns
    -------
    bool
        True if at least one cluster spans top to bottom.
    """
    return percolates_lr(labels_lattice.T)


def percolates(labels_lattice):
    """Check if any cluster percolates in either direction.

    Parameters
    ----------
    labels_lattice : numpy.ndarray
        2D integer array of cluster labels (0 = unoccupied).

    Returns
    -------
    bool
        True if at least one cluster spans either left-right or top-bottom.
    """
    return percolates_tb(labels_lattice) or percolates_lr(labels_lattice)


if __name__ == "__main__":
    print("=== Percolation Detection Demo ===\n")

    perc = np.array(
        [[1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0],
         [2, 0, 0, 0, 0]])

    not_perc = np.array(
        [[1, 1, 1, 0, 0],
         [0, 0, 1, 0, 2],
         [0, 0, 1, 0, 0],
         [3, 0, 0, 0, 0]])

    print("Test lattice 1 (cluster 1 spans left-to-right):")
    print(perc)
    print(f"  percolates_lr: {percolates_lr(perc)}")
    print(f"  percolates_tb: {percolates_tb(perc)}")
    print(f"  percolates:    {percolates(perc)}")

    print("\nTest lattice 1 transposed (cluster 1 spans top-to-bottom):")
    print(perc.T)
    print(f"  percolates_lr: {percolates_lr(perc.T)}")
    print(f"  percolates_tb: {percolates_tb(perc.T)}")
    print(f"  percolates:    {percolates(perc.T)}")

    print("\nTest lattice 2 (no spanning cluster):")
    print(not_perc)
    print(f"  percolates_lr: {percolates_lr(not_perc)}")
    print(f"  percolates_tb: {percolates_tb(not_perc)}")
    print(f"  percolates:    {percolates(not_perc)}")

    # Verify correctness
    assert percolates(perc)
    assert percolates(perc.T)
    assert not percolates(not_perc)
    assert not percolates(not_perc.T)
    print("\nAll tests passed.")

