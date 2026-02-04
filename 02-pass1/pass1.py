"""First pass of the Hoshen-Kopelman cluster labeling algorithm.

This module implements the first pass which scans the lattice and assigns
provisional labels to occupied sites, recording which labels need to be
merged when clusters connect.
"""

import numpy as np
from plot import plot_occupancy, plot_labels


def pass1(occ):
    """Perform the first pass of Hoshen-Kopelman labeling.

    Scans the occupancy grid row by row, left to right. Each occupied site
    receives a label based on its already-labeled neighbors (up and left).
    When two different labels meet, they are recorded for later merging.

    Parameters
    ----------
    occ : array_like
        2D boolean or integer array where True/non-zero indicates occupied sites.

    Returns
    -------
    labels_lattice : numpy.ndarray
        2D integer array of provisional cluster labels (0 = unoccupied).
    to_be_merged : list of tuple
        List of (label1, label2) pairs that need to be merged.
    """
    occ = np.asarray(occ).astype(bool)
    h, w = occ.shape
    labels_lattice = np.zeros((h, w), dtype=np.int64)

    next_label = 1
    to_be_merged = []

    # 1st pass
    for y in range(h):
        for x in range(w):
            if not occ[y, x]:
                continue

            up = labels_lattice[y - 1, x] if y > 0 else 0
            left = labels_lattice[y, x - 1] if x > 0 else 0
            #TODO: vervollständigen Sie den 1. Durchgang
            # Setzen Sie dazu label_lattice[y,x]
            # Wenn linker und oberer Nachbar unbesetzt (=0):
            #   Neuer Cluster gefunden. Mit `next_label` beschriften und `next_label` um 1 erhöhen
            # Wenn nur der linke oder nur der obere Nachbar besetzt ist:
            #   der aktuelle Gitterpunkt gehört zum selben Cluster.
            #   Also das Label des Nachbarn übernehmen
            #   Hinweis: Als zwei if hinschreiben
            # Wenn beide Nachbarn besetzt sind (!=0):
            #    Wenn sie das selbe Label haben, dieses Label übernehemen (Nachbarn gehören zum selben Cluster, und somit auch der aktuelle Gitterpunkt)
            #    wenn sie unterschiedliche Labels haben (zu zwei unterschiedlichen Cluster gehören):
            #         1. das Label vom oberen Nachbarn übernehmen
            #         2. Zur Liste `to_be_merged` (oberer_nachbar, linker_nachbar) hinzufuegen, d.H. notieren, dass beide Labels zu ein und dem selben Cluster gehören

    return labels_lattice, to_be_merged



if __name__ == "__main__":
    print("=== Pass 1: Provisional Labeling Demo ===\n")
    occ = np.array((
        (1, 1, 0, 0, 1),
        (0, 1, 0, 0, 0),
        (1, 1, 0, 0, 1),
        (0, 0, 0, 1, 1)))


    print("Occupancy grid:")
    print(occ)
    plot_occupancy(occ,fname="pass1_occ.png")

    labels_lattice, to_be_merged = pass1(occ)
    unique_labels = set(np.unique(labels_lattice))
    unique_labels.discard(0)
    plot_labels(labels_lattice,title="provisional labels", fname="pass1_provisional_labels.png")

    print("\nProvisional labels (after pass 1):")
    print(labels_lattice)
    print(f"\nUnique labels: {unique_labels}")
    if to_be_merged:
        print("Merge operations needed:")
        for a, b in to_be_merged:
            print(f"  {a} <-> {b}")
    else:
        print("No merges needed.")

