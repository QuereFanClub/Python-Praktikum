# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters

import numpy as np

def unique(arr):
	non_zero_entries = arr[arr != 0]
	return (len(np.unique(non_zero_entries)) == len(non_zero_entries))