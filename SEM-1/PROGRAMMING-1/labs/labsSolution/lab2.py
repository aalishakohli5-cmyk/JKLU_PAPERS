'''
n = int(input("Enter the number:"))

if n % 7 == 0:
    print("lucky")
else:
    print("unlukcy")'''

# ques -2

'''l = float(input("enter length:"))
b = float(input("enter  breadth:"))
h = float(input("enter height:"))

area = 2*h*(l+b)

print(f"Area of four walls = {area}")'''

# ques -3

'''rainfall = float(input("enter total  rainfall in mm :"))
total_days = int(input(" enter number of days:"))

avg = rainfall / total_days

if avg < 2:
    print("drought")
elif avg <= 5:
    print("deficient")
elif avg < 10:
    print("Excess")
else:
    print("flood alert")'''


# ques -4

'''n = input("enter a character:")

if n >= '0' and n <= '9':
    print("digit")

elif n >= 'a' and n <= 'z' or n >= 'A' and n <= "Z":
    print("alphabet")
else:
    print("special")'''

# ques -5

'''initial = 3.45*10**5
final = 4.12*10**5

growth = ((final - initial) / initial)*100
print("population growth=", round(growth))'''

# Ques -6


'''n = int(input("enter the total paisa amount : "))

rupee = n//100
remaining_paisa = n % 100

print("rupees=", rupee)
print("paisa =", remaining_paisa)'''


# Ques -7

'''card = input(" enter the card type  (student/regular):")
time = input(" enter the time : (peak /offpeak)")

if card == "student" and time == "peak":
    fare = 20
elif card == "student" and time == "offpeak":
    fare = 15

elif card == "Regular" and time == "peak":
    fare = 35
elif card == "Regular" and time == "offpeak":
    fare = 25

else:
    fare = 0

if fare == 0:
    print("invalid input")
else:
    print(" fare =", fare, "rupees")'''

# Ques -8

'''score_1 = int(input("enter score for team 1:"))
score_2 = int(input("enter score for team 2:"))

if score_1 == score_2:
    print("Match drawn")
elif score_1 > score_2:
    print("team 1 win by ", score_1-score_2, "points")
else:
    print("team 2 wins", score_2-score_1, "points")'''

# Ques -9
'''pages = int(input("Enter number of pages: "))

if pages < 50:
    cost = pages * 200
else:
    cost = pages * 150

print("Total cost =", cost, "paise")'''

# ques 10

'''litres = float(input("Enter litres filled: "))
cash = float(input("Enter cash given: "))

cost = litres * 96.50

if cash >= cost:
    change = cash - cost
    print("Change = Rs.", round(change, 2))
else:
    extra = cost - cash
    print("You owe Rs.", round(extra, 2), "more")'''


# ques -11

'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        smallest = a
    else:
        smallest = c
else:
    if b < c:
        smallest = b
    else:
        smallest = c

print("Smallest number =", smallest)'''

# ques -12

'''rent = float(input("Enter room rent: "))

service = rent * 10 / 100
gst = rent * 12 / 100
cess = rent * 3 / 100

total = rent + service + gst + cess

print("Room rent =", rent)
print("Service charge =", service)
print("GST =", gst)
print("Tourism cess =", cess)
print("Total bill =", round(total, 2))'''
