"""Label replacement utilities for cluster labeling.

This module provides functions to replace cluster labels in a lattice
according to a given mapping.
"""

import numpy as np


def replace_labels(old_labels, replace_by):
    """Replace cluster labels according to a mapping.

    Creates a new label array where each non-zero label is replaced
    according to the provided mapping dictionary.

    Parameters
    ----------
    old_labels : numpy.ndarray
        2D integer array of original cluster labels.
    replace_by : dict
        Mapping from old labels to new labels. All non-zero labels
        in old_labels must be present as keys.

    Returns
    -------
    numpy.ndarray
        New 2D integer array with replaced labels. Sites with label 0
        remain unchanged.
    """
    new_labels = np.zeros_like(old_labels)
    rows, cols = new_labels.shape
    # TODO: Schreiben Sie Code, der new_labels an Hand von old_labels befüllt
    # Ersetzen Sie dabei die Werte aus old_labels mit den
    # im Dictionary `replace_by` hinterlegten Werten.
    # Beispiel `replace_by={3:2}` würde bedeuten, dass
    # da wo in old_labels 3 steht in new_labels eine 2 eingesetzt wird.
    # Bevor Sie ersetzen, prüfen Sie, ob für den Eintrag in old_labels überhaupt etwas im Dictionary replace_by vermerkt ist.
    
    return new_labels


if __name__ == "__main__":
    print("=== Label Replacement Demo ===\n")

    labels_lattice = np.array(
        [[1, 1, 0, 0, 2],
         [0, 1, 0, 0, 0],
         [3, 1, 0, 0, 4],
         [0, 0, 0, 5, 4]])

    # NOTE: all labels must appear in this dict
    replace_by = {1: 1, 2: 2, 3: 1, 4: 4, 5: 4}

    print("Original labels:")
    print(labels_lattice)
    print(f"\nReplacement mapping: {replace_by}")
    print("  (labels 3->1 and 5->4 due to cluster merging)")

    new_labels = replace_labels(labels_lattice, replace_by)
    print("\nLabels after replacement:")
    print(new_labels)


