def tokenize(string, pos=0):
    tokens = []

    # Function to remove spaces by recursively advancing the position
    def remove_spaces():
        nonlocal pos  # refers to pos variable in the outer scope from parent function
        # Check if there is a space at the current position
        if pos < len(string) and string[pos] == ' ':
            pos += 1
            # Recursively call remove_spaces to move to the next non-space character
            remove_spaces()

    # Initial call to remove_spaces to skip leading spaces
    remove_spaces()

    # Check if there are more characters in the string
    if pos < len(string):
        # Check for parentheses '(' or ')'
        if string[pos] in {'(', ')'}:
            tokens.append(string[pos])
            pos += 1
            # Recursively call tokenize_recursive for the remaining string
            tokens.extend(tokenize(string, pos))

        # Check for numeric digits
        elif '0' <= string[pos] <= '9':
            start = pos
            # Find the end position of the numeric token
            pos = next((i for i, c in enumerate(string[start:], start) if not '0' <= c <= '9'), len(string))
            # Convert the numeric token to an integer and append to tokens
            tokens.append(int(string[start:pos]))
            # Recursively call tokenize_recursive for the remaining string
            tokens.extend(tokenize(string, pos))

        # Check for operators '+' or '-'
        elif string[pos] in {'+', '-'}:
            tokens.append(string[pos])
            pos += 1
            # Recursively call tokenize_recursive for the remaining string
            tokens.extend(tokenize(string, pos))
        else:
            # Raise an error if an invalid token is encountered
            raise ValueError("Invalid token at position " + str(pos))

    return tokens


# Example usage
print(tokenize("3+3-1"))
