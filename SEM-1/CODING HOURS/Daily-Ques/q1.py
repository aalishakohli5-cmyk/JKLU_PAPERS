
a = set(map(int, input().split()))
b = set(map(int, input().split()))

common = sorted(a & b)
all_nums = sorted(a | b)

if common:
    print("Common:", *common)
else:
    print("Common: none")

print("All:", *all_nums)
