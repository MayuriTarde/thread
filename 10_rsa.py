def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return -1


def rsa(p, q, message):
    if p == q or p < 2 or q < 2:
        print("Enter two distinct prime numbers.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    if d == -1:
        print("Could not find private exponent.")
        return

    if message < 0 or message >= n:
        print("Message must be between 0 and n-1.")
        return

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    cipher = pow(message, e, n)
    print("Encrypted message:", cipher)

    plain = pow(cipher, d, n)
    print("Decrypted message:", plain)


p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
message = int(input("Enter numeric message (0 to n-1): "))
rsa(p, q, message)
