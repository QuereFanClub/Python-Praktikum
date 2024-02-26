# Bearbeitet mit Enno Pieper & Sandro Schusters

def shortName(name: str):
    name_array: list = name.split(" ")

    final_name, i = "", 0
    if len(name_array) == 1:
        final_name = name_array[0]
        return final_name

    while i < (len(name_array) - 1):
        final_name += str(name_array[i][0]) + "."
        i += 1

    final_name += " " + str(name_array[len(name_array) - 1])
    return final_name


print(shortName(input("Gib einen Namen ein: \n")))