# Zusammenarbeit mit Luca Stoltenberg, Sandro Schusters

def loop(n):
    triangle = [[1]]
    for i in range(1, n + 1):
        last = triangle[-1]
        row = [1]
        for j in range(1, len(last)):
            row.append(last[j-1] + last[j])
        row.append(1)
        triangle.append(row)
    return triangle
