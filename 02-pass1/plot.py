"""Visualization utilities for occupancy and cluster label lattices.

This module provides functions to visualize 2D occupancy grids and
cluster-labeled lattices using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from renumber_labels import renumber_labels


def plot_labels(labels_lattice, ax=None, title=None, fname=None):
    """
    labels_lattice: 2D integer array with values in {0, 1, ..., n}
      - 0 is plotted as white
      - 1..n get distinct-ish colors
    Uses tab20 for n<=20; for n>20 uses hsv.
    Labels are renumbered to be contiguous before plotting.
    The original array is not modified.
    """
    labels_lattice = np.asarray(labels_lattice).copy()

    # renumber labels to be contiguous (1, 2, 3, ..., n)
    unique_labels = tuple(sorted(set(np.unique(labels_lattice)) - {0}))
    if unique_labels:
        labels_lattice = renumber_labels(labels_lattice, unique_labels)




    if labels_lattice.ndim != 2:
        raise ValueError("labels_lattice must be a 2D array")
    if labels_lattice.min() < 0:
        raise ValueError("labels_lattice must be non-negative integers")
    if not np.issubdtype(labels_lattice.dtype, np.integer):
        raise TypeError("labels_lattice must have integer dtype")

    n = int(labels_lattice.max())  # assumes max label equals n

    # Pick base colormap
    base = plt.get_cmap("tab20" if n <= 20 else "hsv")

    # Colors for classes 1..n (0 is reserved for white)
    class_colors = base(np.linspace(0, 1, n, endpoint=False))

    # Prepend white for label 0
    rng = np.random.default_rng(seed=1)
    class_colors = rng.permutation(class_colors)
    colors = np.vstack([np.array([[1, 1, 1, 1]]), class_colors])
    cmap = ListedColormap(colors)

    # Integer bins centered on integers
    boundaries = np.arange(-0.5, n + 1.5, 1.0)  # for 0..n
    norm = BoundaryNorm(boundaries, cmap.N)

    if ax is None:
        _, ax = plt.subplots()

    im = ax.imshow(labels_lattice, cmap=cmap, norm=norm, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])


    if title:
        ax.set_title(title)
    if fname:
        plt.savefig(fname)
    plt.show()

    return ax



def plot_occupancy(occ, title=None, fname=None):
    """Plot a binary occupancy grid.

    Displays occupied sites in black and unoccupied sites in white.

    Parameters
    ----------
    occ : array_like
        2D boolean or integer array where True/non-zero indicates occupied sites.
    title : str, optional
        Title to display above the plot.
    fname : str, optional
        If provided, saves the figure to this filename.
    """
    plt.imshow(occ, cmap=ListedColormap(["white", "black"]), interpolation="nearest")
    plt.axis("off")
    if title:
        plt.title(title)
    if fname:
        plt.savefig(fname)
    plt.show()

if __name__ == "__main__":
    print("=== Plotting Demo ===\n")

    labels_lattice = np.array(
        [[1, 1, 0, 0, 2],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 3],
         [0, 0, 0, 3, 3]])

    print("Cluster labels (3 clusters):")
    print(labels_lattice)
    plot_labels(labels_lattice, title="Cluster labels (color-coded)")

    occ = np.array(
        [[1, 1, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 1, 1]])

    print("Occupancy grid:")
    print(occ)
    plot_occupancy(occ, title="Occupancy (black=occupied)")
     
