X = int(input())
Y = int(input())
N = int(input())

count = 0

for i in range(X, Y + 1):
    if i % N != 0:
        print(i, end=" ")
        count = count + 1

print()
print(count)


q-2

n = int(input("Enter a positive integer: "))

product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print("Product =", product)


q-3


N = int(input("Enter N: "))

large = 0
small = 0

while True:
    bill = int(input("Enter bill amount: "))

    if bill == -999:
        break

    if bill > N:
        large = large + 1
    else:
        small = small + 1

print(large)
print(small)


q-4


N = int(input("Enter N: "))
P = int(input("Enter P: "))

if N <= 0 or P <= 0:
    print("Invalid input")
else:
    result = 1
    i = 1

    while i <= P:
        result = result * N
        i = i + 1

    print(result)


q-5

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

if reverse == b:
    print("Reverse")
else:
    print("Not reverse")

    q-6


N = int(input("Enter N: "))

term = 1
i = 1

while i <= N:
    print(term, end=" ")
    term = term * 2
    i = i + 1


q-7

n = int(input("Enter a positive integer: "))

if n <= 1:
    print("Not a perfect number")
else:
    total = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            total = total + i

            if i != n // i:
                total = total + n // i

        i = i + 1

    if total == n:
        print("Perfect number")
    else:
        print("Not a perfect number")

        q-7


N = int(input("Enter N: "))

if N <= 0:
    print("Invalid input")
else:
    for i in range(1, N + 1):
        for j in range(i):
            print("*", end=" ")
        print()


n = int(input("Enter a positive integer: "))
D = int(input("Enter a digit from 0 to 9: "))

count = 0

while n > 0:
    digit = n % 10

    if digit == D:
        count = count + 1

    n = n // 10

print("Count =", count)


N = int(input("Enter a positive integer: "))

if N <= 0:
    print("Invalid input")
else:
    count = 0

    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
            count = count + 1

    print("Number of divisors =", count)

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
