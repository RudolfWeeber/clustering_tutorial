"""Second pass of the Hoshen-Kopelman cluster labeling algorithm.

This module implements the second pass which resolves label equivalences
and replaces provisional labels with their final representative labels.
"""

import numpy as np
import networkx as nx
from merge import get_representative_labels
from replace_labels import replace_labels
from pass1 import pass1
from plot import plot_occupancy, plot_labels

def pass2(labels_lattice, to_be_merged):
    """Perform the second pass of Hoshen-Kopelman labeling.

    Resolves all label equivalences recorded in the first pass and
    replaces each provisional label with its representative label.

    Parameters
    ----------
    labels_lattice : numpy.ndarray
        2D integer array of provisional cluster labels from pass1.
    to_be_merged : list of tuple
        List of (label1, label2) pairs that need to be merged.

    Returns
    -------
    labels_lattice : numpy.ndarray
        2D integer array with final cluster labels.
    unique_labels : set
        Set of unique final cluster labels (excluding 0).
    """
    unique_labels = set(np.unique(labels_lattice))
    unique_labels.discard(0)
    representative_labels = get_representative_labels(unique_labels, to_be_merged)

    labels_lattice = replace_labels(labels_lattice, representative_labels)
    return labels_lattice, set(representative_labels.values()) 





if __name__ == "__main__":
    print("=== Pass 2: Label Resolution Demo ===\n")

    occ = np.array((
        (1, 1, 0, 0, 1),
        (0, 1, 0, 0, 0),
        (1, 1, 0, 0, 1),
        (0, 0, 0, 1, 1)))
    plot_occupancy(occ, fname="pass2_occupancy.png")
    print("Occupancy grid:")
    print(occ)

    labels_lattice, to_be_merged = pass1(occ)
    unique_labels = set(np.unique(labels_lattice))
    unique_labels.discard(0)

    print("\nAfter pass 1 (provisional labels):")
    plot_labels(labels_lattice, title="Provisional labels (pass 1)", fname="pass2_provisional_labels.png")
    print(labels_lattice)
    print(f"Unique labels: {unique_labels}")
    if to_be_merged:
        print("Merge operations needed:")
        for a, b in to_be_merged:
            print(f"  {a} <-> {b}")
    else:
        print("No merges needed.")

    labels_lattice, unique_labels = pass2(labels_lattice, to_be_merged)
    print("\nAfter pass 2 (final labels):")
    plot_labels(labels_lattice, title="Final labels (pass 2)", fname="pass2_final_labels.png")
    print(labels_lattice)
    print(f"Final clusters: {unique_labels}")
    

