
# ques -1

'''print(" Addition Table")


for i in range(1, 10):
    print(i, end="   ")


for i in range(1, 10):
    print(i, "|", end="   ")

    for j in range(1, 10):
        print(i + j, end="   ")

    print()'''

# ques -2

'''N = int(input())

i = 1

while i <= 1000:

    if i % N != 0 or i % 4 == 0:
        i += 1
        continue

    print(i, end=" ")
    i += 1'''


'''nums = [1, 2, 2, 3, 1]

total = 0

for x in nums:
    total = total + x

print(total)'''

nums = [2, 3, 5]

total = 0
for x in nums:
    total = (total + x) + 1

print(total)
