def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    result = ""

    for char in key + alphabet:
        if char.isalpha() and char not in result:
            result += char

    return [list(result[i:i + 5]) for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def make_pairs(text):
    text = text.upper().replace("J", "I")
    text = "".join(char for char in text if char.isalpha())

    pairs = []
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 >= len(text):
            second = "X"
            i += 1
        elif text[i] == text[i + 1]:
            second = "X"
            i += 1
        else:
            second = text[i + 1]
            i += 2

        pairs.append((first, second))

    return pairs


def process(text, matrix, mode):
    if mode == "encrypt":
        pairs = make_pairs(text)
        shift = 1
    else:
        clean = text.upper().replace("J", "I")
        clean = "".join(char for char in clean if char.isalpha())
        if len(clean) % 2 != 0:
            return "Invalid ciphertext: length must be even"
        pairs = [(clean[i], clean[i + 1]) for i in range(0, len(clean), 2)]
        shift = -1

    result = ""

    for first, second in pairs:
        r1, c1 = find_position(matrix, first)
        r2, c2 = find_position(matrix, second)

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = create_matrix(key)
print("Playfair Matrix:")
for row in matrix:
    print(" ".join(row))

cipher = process(text, matrix, "encrypt")
print("Encrypted text:", cipher)

plain = process(cipher, matrix, "decrypt")
print("Decrypted text (may contain filler X):", plain)
