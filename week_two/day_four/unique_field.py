# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters

import numpy as np


def unique(arr):
    non_zero_entries = arr[arr != 0]
    return len(np.unique(non_zero_entries)) == len(non_zero_entries)


def valid(arr):
    for row in arr:
        if not unique(row):
            return False

    for col in arr.T:
        if not unique(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = arr[i:i + 3, j:j + 3].flatten()
            if not unique(block):
                return False
    return True