# Q1: Calculate employee bonus

import math
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if salary < 0 or years < 0:
    print("Invalid input")
elif years > 5:
    bonus = salary * 0.05
    print("Bonus amount =", round(bonus, 2))
else:
    print("Bonus amount = 0")

# Q2: Password verification

password = input("Enter password: ")

if password == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")


# Q3: Calculate the area of a shape


shape = input("Enter shape (square/rectangle/circle/triangle): ").lower()

if shape == "square":
    side = float(input("Enter side: "))

    if side <= 0:
        print("Invalid input")
    else:
        area = side * side
        print("Area =", format(area, ".3f"))

elif shape == "rectangle":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    if length <= 0 or breadth <= 0:
        print("Invalid input")
    else:
        area = length * breadth
        print("Area =", format(area, ".3f"))

elif shape == "circle":
    radius = float(input("Enter radius: "))

    if radius <= 0:
        print("Invalid input")
    else:
        area = math.pi * radius * radius
        print("Area =", format(area, ".3f"))

elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    if base <= 0 or height <= 0:
        print("Invalid input")
    else:
        area = 0.5 * base * height
        print("Area =", format(area, ".3f"))

else:
    print("Invalid shape")


# Q4: Calculate time 15 minutes later

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
    print("Invalid input")
else:
    total_minutes = hours * 60 + minutes + 15
    total_minutes = total_minutes % 1440

    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    print(str(new_hours) + ":" + format(new_minutes, "02d"))


# Q5: Find the cheapest transport

distance = float(input("Enter distance in km: "))
period = input("Enter period (day/night): ").lower()

if distance <= 0 or period not in ("day", "night"):
    print("Invalid input")
else:
    if period == "day":
        taxi_rate = 37.89
    else:
        taxi_rate = 43.17

    taxi = 33.58 + taxi_rate * distance

    cheapest = taxi
    transport = "Taxi"

    if distance >= 20:
        bus = 4.32 * distance

        if bus < cheapest:
            cheapest = bus
            transport = "Bus"

    if distance >= 100:
        train = 2.88 * distance

        if train < cheapest:
            cheapest = train
            transport = "Train"

    print("Cheapest transport =", transport)
    print("Price =", round(cheapest, 2), "INR")


# Q6: Calculate Tom Cat's playtime difference

holidays = int(input("Enter number of holidays: "))

if holidays < 0 or holidays > 365:
    print("Invalid input")
else:
    workdays = 365 - holidays

    total_playtime = workdays * 63 + holidays * 127
    difference = abs(total_playtime - 30000)

    if total_playtime < 30000:
        print("Tom sleeps well")
        print("Below norm by", difference, "minutes")
    elif total_playtime > 30000:
        print("Tom will not sleep well")
        print("Exceeds norm by", difference, "minutes")
    else:
        print("Tom will sleep exactly as required")
        print("Difference = 0 minutes")


# Q7: Vacation destination and spending

budget = float(input("Enter budget in BGN: "))
season = input("Enter season (summer/winter): ").lower()

if budget < 0 or season not in ("summer", "winter"):
    print("Invalid input")

elif budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        place = "Camping"
        spending = budget * 0.30
    else:
        place = "Hotel"
        spending = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        place = "Camping"
        spending = budget * 0.40
    else:
        place = "Hotel"
        spending = budget * 0.80

else:
    destination = "Europe"
    place = "Hotel"
    spending = budget * 0.90

if budget >= 0 and season in ("summer", "winter"):
    print("Destination =", destination)
    print("Accommodation =", place)
    print("Money spent =", format(spending, ".2f"), "BGN")


# Q8: Display numbers ending in 6

for i in range(1, 1001):
    if i % 10 == 6:
        print(i, end=" ")


# Q9: Calculate the sum of n integers

n = int(input("How many numbers? "))

if n <= 0:
    print("Invalid input")
else:
    total = 0

    for i in range(n):
        number = int(input("Enter a number: "))
        total = total + number

    print("Sum =", total)


# Q10: Multiplication table

N = int(input("Enter a positive integer: "))

if N <= 0:
    print("Invalid input")
else:
    for i in range(1, 21):
        print(N, "x", i, "=", N * i)
