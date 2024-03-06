# Zusammenarbeit mit folgenden Teilnehmern: Luca Stoltenberg, Philip Langenbrink

import numpy as np


def perspective(points):
    # Position der Kamera
    c = -3

    # Extrahiere x, y, z Koordinaten der Punkte
    x, y, z = points[:, 0], points[:, 1], points[:, 2]

    # Perspektivische Projektion berechnen
    u = x / (z - c)
    v = y / (z - c)

    # 2D-Punkte zurückgeben
    return np.column_stack((u, v))
