# Mit Luca Stoltenberg und Sandro Schusters bearbeitet

def tokenize(string, pos=0):
    tokens = []

    def remove_spaces():
        nonlocal pos
        if pos < len(string) and string[pos] == ' ':
            pos += 1
            remove_spaces()

    remove_spaces()

    if pos < len(string):
        if string[pos] in {'(', ')'}:
            tokens.append(string[pos])
            pos += 1
            tokens.extend(tokenize(string, pos))

        elif '0' <= string[pos] <= '9':
            start = pos
            pos = next((i for i, c in enumerate(string[start:], start) if not '0' <= c <= '9'), len(string))
            tokens.append(int(string[start:pos]))
            tokens.extend(tokenize(string, pos))

        elif string[pos] in {'+', '-'}:
            tokens.append(string[pos])
            pos += 1
            tokens.extend(tokenize(string, pos))
        else:
            raise ValueError("Invalid token at position " + str(pos))

    return tokens
