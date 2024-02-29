"""# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters

class Statistics:
    def __init__(self, data):
        self.data = data

    mean = sum(data) / len(data)

    is_medi_even = len() % 2 == 0
    sorted_data = sorted(data)
    length = len(sorted_data)

    if not is_medi_even:
        median = sorted_data[length // 2]
    else:
        middle1 = sorted_data[length // 2 - 1]
        middle2 = sorted_data[length // 2]
        median = (middle1 + middle2) / 2

    def mean(self):
        from statistics import mean
        return mean

    def variance(self):
        from statistics import mean
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def median(self):
        from statistics import median
        return median

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)
"""

class Statistics:
    def __init__(self, data):
        self.data = data
        self.mean_val = None
        self.variance_val = None
        self.median_val = None
        self.minimum_val = None
        self.maximum_val = None

    def calculate_statistics(self):
        mean = sum(self.data) / len(self.data)

        is_median_even = len(self.data) % 2 == 0
        sorted_data = sorted(self.data)
        length = len(sorted_data)

        if not is_median_even:
            median = sorted_data[length // 2]
        else:
            middle1 = sorted_data[length // 2 - 1]
            middle2 = sorted_data[length // 2]
            median = (middle1 + middle2) / 2

        minimum_val = min(self.data)
        maximum_val = max(self.data)
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)

        self.mean_val = mean
        self.variance_val = variance
        self.median_val = median
        self.minimum_val = minimum_val
        self.maximum_val = maximum_val

    def mean(self):
        if self.mean_val is None:
            self.calculate_statistics()
        return self.mean_val

    def variance(self):
        if self.variance_val is None:
            self.calculate_statistics()
        return self.variance_val

    def median(self):
        if self.median_val is None:
            self.calculate_statistics()
        return self.median_val

    def minimum(self):
        if self.minimum_val is None:
            self.calculate_statistics()
        return self.minimum_val

    def maximum(self):
        if self.maximum_val is None:
            self.calculate_statistics()
        return self.maximum_val