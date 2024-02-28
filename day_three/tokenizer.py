# Zusammenarbeit mit Luca Stoltenberg, Sandro Schusters

def tokenize(string):
    tokens = []
    pos = 0
    while pos < len(string):
        while pos < len(string):
            if string[pos] != ' ':
                break
            else:
                pos += 1
        if pos == len(string):
            break

        if string[pos] in {'(', ')'}:
            tokens.append(string[pos])
            pos += 1
        elif '0' <= string[pos] <= '9':
            start = pos
            while pos < len(string) and ('0' <= string[pos] <= '9'):
                pos += 1
            tokens.append(int(string[start:pos]))
        elif string[pos] in {'+', '-'}:
            tokens.append(string[pos])
            pos += 1
        else:
            raise ValueError("Invalid token at position " + str(pos))

    return tokens


print(tokenize("3+3-1"))
