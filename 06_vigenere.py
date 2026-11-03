def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    if not key.isalpha():
        return "Invalid key"

    for char in text.upper():
        if char.isalpha():
            p = ord(char) - 65
            k = ord(key[j % len(key)]) - 65
            c = (p + k) % 26
            result += chr(c + 65)
            j += 1
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    if not key.isalpha():
        return "Invalid key"

    for char in text.upper():
        if char.isalpha():
            c = ord(char) - 65
            k = ord(key[j % len(key)]) - 65
            p = (c - k) % 26
            result += chr(p + 65)
            j += 1
        else:
            result += char

    return result


text = input("Enter plaintext: ")
key = input("Enter key: ")
cipher = encrypt(text, key)
print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))
