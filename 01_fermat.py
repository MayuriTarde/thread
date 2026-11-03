n = int(input("Enter number: "))

if n <= 1:
    print("Neither Prime nor Composite")
elif n == 2:
    print("Prime")
else:
    a = int(input("Enter base: "))

    if a <= 1 or a >= n:
        print("Invalid base")
    elif pow(a, n - 1, n) == 1:
        print("Probably Prime")
    else:
        print("Composite")
