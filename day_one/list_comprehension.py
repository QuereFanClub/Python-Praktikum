# Bearbeitet mit Enno Pieper & Sandro Schusters

def comprehend(a):
    return [x.upper() for x in a if x[0].upper() != 'Z']


print(comprehend(["Hallo", "Welt", "zeitung", "Leser"]))
