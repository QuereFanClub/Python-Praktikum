"""
This doesn't function

class Bijection:
    def __init__(self, other=None):
        self.mapping = {}
        self.inverse_mapping = {}

        if other is not None:
            if isinstance(other, Bijection):
                self.mapping = dict(other.mapping)
                self.inverse_mapping = dict(other.inverse_mapping)
            elif isinstance(other, dict):
                for key, value in other.items():
                    self[key] = value

    def __str__(self):
        return "{" + ",".join(f"{key}->{value}" for key, value in self.mapping.items()) + "}"

    def __getitem__(self, key):
        return self.mapping.get(key, None)

    def __setitem__(self, key, value):
        if value in self.inverse_mapping and key != self.inverse_mapping[value]:
            raise KeyError("duplicate value")
        if key in self.mapping:
            del self.inverse_mapping[self.mapping[key]]
        self.mapping[key] = value
        self.inverse_mapping[value] = key

    def __delitem__(self, key):
        if key in self.mapping:
            value = self.mapping[key]
            del self.mapping[key]
            del self.inverse_mapping[value]

    def __len__(self):
        return len(self.mapping)

    def __mul__(self, other):
        result = Bijection()
        for key, value in self.mapping.items():
            if value in other.inverse_mapping:
                result[key] = other.inverse_mapping[value]
            else:
                raise KeyError(f"missing key: {value} in {other}")
        return result

    def inverse(self):
        result = Bijection()
        result.mapping = dict(self.inverse_mapping)
        result.inverse_mapping = dict(self.mapping)
        return result

"""