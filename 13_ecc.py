def mod_inverse(a, p):
    a %= p
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return -1


def point_add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        numerator = (3 * x1 * x1 + a) % p
        denominator = (2 * y1) % p
    else:
        numerator = (y2 - y1) % p
        denominator = (x2 - x1) % p

    inv = mod_inverse(denominator, p)
    if inv == -1:
        return None

    slope = (numerator * inv) % p
    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_multiply(d, G, a, p):
    result = None
    for i in range(d):
        result = point_add(result, G, a, p)
    return result


p = int(input("Enter prime p: "))
a = int(input("Enter curve parameter a: "))
b = int(input("Enter curve parameter b: "))

x = int(input("Enter base point x: "))
y = int(input("Enter base point y: "))
G = (x, y)

d = int(input("Enter private key: "))

# Check that the supplied base point is on the curve.
if (y * y - (x * x * x + a * x + b)) % p != 0:
    print("Base point is not on the curve.")
else:
    Q = scalar_multiply(d, G, a, p)
    print("Base Point:", G)
    print("Private Key:", d)
    print("Public Key:", Q)
