def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in text.upper():
        if char in alphabet:
            index = alphabet.index(char)
            result += key[index]
        else:
            result += char

    return result


def decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in text.upper():
        if char in key:
            index = key.index(char)
            result += alphabet[index]
        else:
            result += char

    return result


key = input("Enter 26-letter substitution key: ").upper()

if len(key) != 26 or len(set(key)) != 26 or not key.isalpha():
    print("Invalid key. Enter 26 different letters.")
else:
    text = input("Enter plaintext: ")
    cipher = encrypt(text, key)
    print("Encrypted text:", cipher)
    print("Decrypted text:", decrypt(cipher, key))
