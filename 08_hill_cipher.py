def mod_inverse(det):
    for i in range(26):
        if (det * i) % 26 == 1:
            return i
    return -1


def inverse_matrix(key):
    det = (key[0][0] * key[1][1] -
           key[0][1] * key[1][0]) % 26

    inv_det = mod_inverse(det)
    if inv_det == -1:
        return None

    inverse = [
        [(key[1][1] * inv_det) % 26,
         (-key[0][1] * inv_det) % 26],
        [(-key[1][0] * inv_det) % 26,
         (key[0][0] * inv_det) % 26]
    ]
    return inverse


def encrypt(text, key):
    text = text.upper().replace(" ", "")
    if not text.isalpha():
        return "Use alphabetic text only"

    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - 65
        p2 = ord(text[i + 1]) - 65

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        result += chr(c1 + 65) + chr(c2 + 65)

    return result


def decrypt(text, key):
    inv = inverse_matrix(key)
    if inv is None:
        return "Key inverse does not exist"

    result = ""
    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - 65
        c2 = ord(text[i + 1]) - 65

        p1 = (inv[0][0] * c1 + inv[0][1] * c2) % 26
        p2 = (inv[1][0] * c1 + inv[1][1] * c2) % 26

        result += chr(p1 + 65) + chr(p2 + 65)

    return result


key = [[3, 3], [2, 5]]
text = input("Enter plaintext: ")
cipher = encrypt(text, key)
print("Encrypted text:", cipher)
print("Inverse key:", inverse_matrix(key))
print("Decrypted text:", decrypt(cipher, key))
