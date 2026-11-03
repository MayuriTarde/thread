def diffie_hellman(p, g, a, b):
    # Alice's public value
    A = pow(g, a, p)

    # Bob's public value
    B = pow(g, b, p)

    print("Alice's Public Value:", A)
    print("Bob's Public Value:", B)

    # Both calculate the shared secret
    key1 = pow(B, a, p)
    key2 = pow(A, b, p)

    print("Alice's Shared Secret:", key1)
    print("Bob's Shared Secret:", key2)

    if key1 == key2:
        print("Shared Secret Established")
    else:
        print("Key Exchange Failed")


p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

diffie_hellman(p, g, a, b)
