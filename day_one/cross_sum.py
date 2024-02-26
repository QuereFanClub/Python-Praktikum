# Zusammenarbeit mit folgenden Teilnehmern: Sandro Schusters & Enno Pieper

def cross_sum(n, b):
    if n < 0 or b < 2:
        return "Ungültige Eingabe"

    result = 0
    while n > 0:
        digit = n % b
        result += digit
        n = n // b

    return result

# Beispiel:
dezimalzahl = 212
basis = 16
ergebnis = cross_sum(dezimalzahl, basis)
print(f"Die Quersumme der Dezimalzahl {dezimalzahl} zur Basis {basis} ist: {ergebnis}")
