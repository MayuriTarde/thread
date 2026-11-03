def mod_inverse(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return -1


def elgamal(p, g, x, message, k):
    if not (0 < message < p):
        print("Message must be between 1 and p-1.")
        return

    if not (1 <= x < p - 1 and 1 <= k < p - 1):
        print("Choose x and k between 1 and p-2.")
        return

    y = pow(g, x, p)
    print("Public Key:", (p, g, y))
    print("Private Key:", x)

    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    print("Ciphertext:", (c1, c2))

    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)

    if s_inv == -1:
        print("Could not calculate modular inverse.")
        return

    plain = (c2 * s_inv) % p
    print("Decrypted message:", plain)


p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
message = int(input("Enter numeric message: "))
k = int(input("Enter random k: "))

elgamal(p, g, x, message, k)
