def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def euler_test(n, base):
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

    value = pow(base, (n - 1) // 2, n)

    if value != 1 and value != n - 1:
        return "Composite"

    return "Probably Prime"


n = int(input("Enter a number: "))
base = int(input("Enter base: "))
print(euler_test(n, base))
