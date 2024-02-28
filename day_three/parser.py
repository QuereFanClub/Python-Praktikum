# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters, Luca Stoltenberg

class Subtraction:
    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        l = "(" + str(self.left) + ")" if isinstance(self.left, Subtraction) else str(self.left)
        r = "(" + str(self.right) + ")" if isinstance(self.right, Subtraction) else str(self.right)
        return l + " - " + r

    def __call__(self):
        l = self.left() if isinstance(self.left, Subtraction) else int(self.left)
        r = self.right() if isinstance(self.right, Subtraction) else int(self.right)
        return l - r


def parseMinus(array):
    expr = None
    pos = 0

    while True:
        if pos == len(array) or array[pos] == ")" or array[pos] == "-":
            raise Exception("-1")
        elif isinstance(array[pos], int):
            t = array[pos]
            pos += 1
        elif array[pos] == "(":
            subtree, length = parseMinus(array[pos + 1:])
            t = subtree
            pos += length + 1

            if pos >= len(array) or array[pos] != ")":
                raise Exception("-2")
            pos += 1

        if expr is None:
            expr = t
        else:
            expr = Subtraction(expr, t)

        if pos >= len(array):
            break

        if array[pos] == "-":
            pos += 1
            continue
        elif array[pos] == ")":
            break
        else:
            raise Exception("-3")

    return (expr, pos)
