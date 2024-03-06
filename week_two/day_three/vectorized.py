# Zusammenarbeit mit folgenden Teilnehmern: Luca Stoltenberg, Philip Langenbrink

import numpy as np


def circle(n):
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = np.cos(angles)
    y = np.sin(angles)
    points = np.column_stack((x, y))
    return points


def ellipse(n):
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = 3 * np.cos(angles)
    y = 0.5 * np.sin(angles)
    points = np.column_stack((x, y))
    return points
