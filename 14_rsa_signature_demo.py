# Educational textbook RSA signature demonstration.
# This is NOT RSA-PSS and is NOT secure.

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return -1


p = 3
q = 11
n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = mod_inverse(e, phi)

message = int(input("Enter a small numeric message (0 to n-1): "))

if message < 0 or message >= n:
    print("Message must be between 0 and n-1.")
else:
    signature = pow(message, d, n)
    print("Public Key:", (e, n))
    print("Private Key:", (d, n))
    print("Digital Signature:", signature)

    verified = pow(signature, e, n)

    if verified == message:
        print("Signature is Valid")
    else:
        print("Signature is Invalid")
