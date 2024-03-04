# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters, 🤫🧏‍
def statistics(data):
    help_dict = {"mean": 0.0, "variance": 0.0, "median": 0.0, "minimum": 0.0, "maximum": 0.0}

    mean = sum(data) / len(data)

    is_medi_even = len(data) % 2 == 0
    sorted_data = sorted(data)
    length = len(sorted_data)

    help_dict["mean"] = mean

    if not is_medi_even:
        help_dict["median"] = sorted_data[length // 2]
    else:
        middle1 = sorted_data[length // 2 - 1]
        middle2 = sorted_data[length // 2]
        help_dict["median"] = (middle1 + middle2) / 2

    help_dict["minimum"] = min(data)
    help_dict["maximum"] = max(data)
    help_dict["variance"] = sum((x - mean) ** 2 for x in data) / len(data)

    return help_dict


