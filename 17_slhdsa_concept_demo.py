# CONCEPTUAL TOY DEMONSTRATION ONLY.
# This is NOT SLH-DSA and is NOT a secure public-key signature.
# It illustrates message processing and signature checking without libraries.

def simple_hash(text):
    value = 0
    for char in text:
        value = (value * 31 + ord(char)) % 100000
    return value


private_key = 12345

# For demonstration only: public key is made equal to private key.
# This is NOT how a real public-key signature scheme works.
public_key = private_key

message = input("Enter message: ")

signature = simple_hash(message + str(private_key))
print("Toy Signature:", signature)

check = simple_hash(message + str(public_key))

if signature == check:
    print("Toy demonstration: Signature is Valid")
else:
    print("Toy demonstration: Signature is Invalid")
