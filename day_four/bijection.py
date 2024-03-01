class Bijection:
    def __init__(self, other=None):
        self._f = {}
        self._inverse = {}
        if isinstance(other, dict):
            for key, value in other.items():
                self[key] = value
        elif isinstance(other, Bijection):
            self._f = other._f.copy()
            self._inverse = other._inverse.copy()
        elif other is not None:
            raise ValueError("Argument error")

    def __str__(self):
        pairs = [key + "->" + value for key, value in self._f.items()]
        return "{" + ", ".join(pairs) + "}"

    def __getitem__(self, key):
        if key in self._f:
            return self._f[key]
        return None

    def __setitem__(self, key, value):
        if value in self._f.values() or value in self._inverse.values():
            raise KeyError("Duplicate")

        if key in self._f:
            old_value = self._f[key]
            del self._inverse[old_value]


        if value in self._inverse:

            o_key = self._inverse[value]
            del self._f[o_key]

        self._f[key] = value
        self._inverse[value] = key

    def __delitem__(self, key):
        if key not in self._f:
            raise KeyError("Key does not exist!")
        value = self._f.pop(key)
        del self._inverse[value]

    def __len__(self):
        return len(self._f)

    def __mul__(self, other):
        if not isinstance(other, Bijection):
            raise ValueError("Value Error")

        composition = Bijection()
        for key, value in other._f.items():
            if value in self._f:
               composition[key] = self._f[value]
            else:
                raise KeyError(f"Missing key: {value}")
        return composition

    def inverse(self):
        inversed = Bijection()
        inversed._f, inversed._inverse = self._inverse.copy(), self._f.copy()
        return inversed
