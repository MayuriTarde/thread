def encrypt(text, key):
    if key <= 1:
        return text

    rail = [""] * key
    row = 0
    direction = 1

    for char in text:
        rail[row] += char

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return "".join(rail)


def decrypt(cipher, key):
    if key <= 1:
        return cipher

    pattern = []
    row = 0
    direction = 1

    for char in cipher:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    rail = [""] * key
    index = 0

    for i in range(key):
        count = pattern.count(i)
        rail[i] = cipher[index:index + count]
        index += count

    result = ""
    position = [0] * key

    for r in pattern:
        result += rail[r][position[r]]
        position[r] += 1

    return result


text = input("Enter plaintext: ")
key = int(input("Enter number of rails: "))

cipher = encrypt(text, key)
print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))
