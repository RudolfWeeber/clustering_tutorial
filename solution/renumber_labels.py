"""Label renumbering utilities for cluster labeling.

This module provides functions to renumber cluster labels to be
contiguous integers starting from 1, eliminating gaps in the numbering.
"""

import numpy as np
from replace_labels import replace_labels


def _get_replacements(unique_labels):
    """Create a mapping from original labels to contiguous integers.

    Parameters
    ----------
    unique_labels : iterable
        Collection of unique labels (e.g., [1, 2, 4, 6]).

    Returns
    -------
    dict
        Mapping from original labels to new contiguous labels (1, 2, 3, ...).
    """
    n = len(unique_labels)
    new_labels = list(range(1, n + 1))
    replacements = {orig: new for orig, new in zip(unique_labels, new_labels)}
    return replacements


def renumber_labels(labels_lattice, unique_labels):
    """Renumber cluster labels to be contiguous integers.

    Replaces labels in the lattice so they form a contiguous sequence
    starting from 1 with no gaps (e.g., [1, 4, 7] becomes [1, 2, 3]).

    Parameters
    ----------
    labels_lattice : numpy.ndarray
        2D integer array of cluster labels.
    unique_labels : iterable
        Collection of unique non-zero labels in the lattice.

    Returns
    -------
    numpy.ndarray
        New 2D integer array with renumbered labels.
    """
    replacements = _get_replacements(unique_labels)
    return replace_labels(labels_lattice, replacements)


if __name__ == "__main__":
    print("=== Label Renumbering Demo ===\n")

    labels_lattice = np.array(
        [[1, 1, 0, 0, 2],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 4],
         [0, 0, 0, 4, 4]])
    unique_labels = (1, 2, 4)

    print("Original labels (with gaps: 1, 2, 4):")
    print(labels_lattice)

    print(f"\nUnique labels: {unique_labels}")
    replacements = _get_replacements(unique_labels)
    print(f"Replacement mapping: {replacements}")

    print("\nRenumbered labels (contiguous: 1, 2, 3):")
    print(renumber_labels(labels_lattice, unique_labels))



