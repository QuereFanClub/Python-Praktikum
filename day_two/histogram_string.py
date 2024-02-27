# Zusammenarbeit mit folgenden Teilnehmern:
def histogram(strings):
    histogram_dict = {}

    for string in strings:
        if string in histogram_dict:
            histogram_dict[string] += 1
        else:
            histogram_dict[string] = 1

    return histogram_dict

