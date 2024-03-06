# Zusammenarbeit mit folgenden Teilnehmern: Luca Stoltenberg, Philip Langenbrink

import numpy as np


def brightness(x, n, c, l, h, k):
    # Richtung vom Punkt zur Kamera als Einheitsvektor berechnen
    v = (x - c) / np.linalg.norm(x - c)

    # Richtung des Lichtstrahls von der Lichtquelle zum Punkt berechnen
    s = l - x
    t = s - 2 * np.dot(s, n) * n
    m = t / np.linalg.norm(t)

    # Helligkeit berechnen
    brightness = h * np.dot(v, m) ** k / np.linalg.norm(x - l)

    return brightness