# Zusammenarbeit mit folgenden Teilnehmern: Luca Stoltenberg, Philip Langenbrink
import numpy as np


def circle(n):
    points = []
    for k in range(n):
        points.append([np.cos(2 * np.pi * k / n), np.sin(2 * np.pi * k / n)])
    return np.array(points)


def ellipse(n):
    points = []
    for k in range(n):
        points.append([np.cos(2 * np.pi * k / n) * 3, np.sin(2 * np.pi * k / n)/2])
    return np.array(points)