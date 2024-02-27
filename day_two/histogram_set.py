# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters

def histogram(lists):
    local_dict = {}
    for i in lists:
        local_set = set(i)
        local_frozen_set = frozenset(local_set)
        if local_frozen_set in local_dict:
            local_dict[local_frozen_set] += 1
        else:
            local_dict[local_frozen_set] = 1
    return local_dict
