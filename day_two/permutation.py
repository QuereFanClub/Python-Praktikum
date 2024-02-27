# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters
def isPermutation(list1, list2):
    help_list: list = list2.copy()

    if len(list1) is not len(list2):
        return False

    for i in range(len(list1)):
        element = list1[i]
        has_found = False
        for j in range(len(help_list)):
            if element == help_list[j]:
                has_found = True
                help_list.remove(help_list[j])
                break
        if not has_found:
            return False
    if len(help_list) == 0:
        return True
    else:
        return False



print(isPermutation([1, 2, 3], [3, 1, 2]))