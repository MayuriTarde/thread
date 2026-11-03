# CONCEPTUAL TOY DEMONSTRATION ONLY.
# This is NOT the official ML-DSA algorithm.
# It only illustrates a simple arithmetic signing/verification pattern.

q = 97

private_key = [5, 8, 3]

# Toy public values
public_key = []
for value in private_key:
    public_key.append((value * 2) % q)

message = input("Enter message: ")

# Simple message-to-number conversion (not a cryptographic hash)
h = 0
for char in message:
    h = (h * 31 + ord(char)) % q

# Toy signing
signature = []
for value in private_key:
    signature.append((h * value) % q)

print("Public Key:", public_key)
print("Signature:", signature)

# Toy verification
check = []
for value in public_key:
    check.append((h * value) % q)

expected = []
for value in signature:
    expected.append((2 * value) % q)

if check == expected:
    print("Toy demonstration: Signature is Valid")
else:
    print("Toy demonstration: Signature is Invalid")
