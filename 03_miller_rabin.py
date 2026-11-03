def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def miller_rabin(n, base):
    if n < 2:
        return "Neither Prime nor Composite"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0:
        return "Composite"
    if base <= 1 or base >= n:
        return "Invalid Base"
    if gcd(base, n) != 1:
        return "Invalid Base: GCD is not 1"

    # Write n - 1 as 2^s * d, where d is odd.
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    x = pow(base, d, n)

    if x == 1 or x == n - 1:
        return "Probably Prime"

    for i in range(s - 1):
        x = (x * x) % n
        if x == n - 1:
            return "Probably Prime"

    return "Composite"


n = int(input("Enter a number: "))
base = int(input("Enter base: "))
print(miller_rabin(n, base))
