# Zusammenarbeit mit Sandro Schustets

import numpy as np

def unique(arr):
    non_zero_entries = arr[arr != 0]
    return len(np.unique(non_zero_entries)) == len(non_zero_entries)


def valid(arr):
    # Überprüfen der Zeilen
    for row in arr:
        if not unique(row):
            return False

    # Überprüfen der Spalten
    for col in arr.T:
        if not unique(col):
            return False

    # Überprüfen der 3x3-Blöcke
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = arr[i:i + 3, j:j + 3].flatten()
            if not unique(block):
                return False

    return True


def solve(arr, x=0, y=0):
    # Finden der ersten 0
    for i in range(x, 9):
        for j in range(y, 9):
            if arr[i, j] == 0:
                x, y = i, j
                break
        else:
            continue
        break

    # Wenn keine 0 gefunden wurde, ist das Sudoku gelöst
    if arr[x, y] == 0:
        return arr

    # Für jede Zahl 1 bis 9 probieren
    for num in range(1, 10):
        arr_copy = arr.copy()  # Kopie des Arrays, um das ursprüngliche nicht zu verändern
        arr_copy[x, y] = num

        # Überprüfen, ob das Feld gültig ist
        if valid(arr_copy):
            # Rekursiver Aufruf mit der Kopie des Arrays
            solution = solve(arr_copy, x, y)
            if solution is not None:
                return solution

    # Wenn keine Lösung gefunden wurde
    return None


def check(original, solution):
    if not np.array_equal(original[original != 0], solution[original != 0]):
        return "solution is invalid"
    elif not valid(solution):
        return "solution is invalid"
    else:
        return "solution is valid"