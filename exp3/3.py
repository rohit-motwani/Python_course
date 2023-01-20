def add(*nums):
    sum = 0
    for num in nums:
        sum = num+sum
    return sum


def sub(*nums):
    sum = 0
    for num in nums:
        sum = num-sum
    return sum


def mult(*nums):
    prod = 1
    for num in nums:
        prod = num*prod
    return prod

ch = int(input("1. Add\n2. Subtract\n3. Multiply\nEnter your choice : "))
print("To exit Enter '/' to stop entering numbers")

nums = []
while True:
    n = input()
    if n == '/':
        break
    else:
        nums.append(int(n))

if ch == 1:
    print("Sum of your numbers are {}".format(add(*nums)))
elif ch == 2:
    print("Subtraction of your numbers are {}".format(sub(*nums)))
elif ch == 3:
    print("Product of your numbers are {}".format(mult(*nums)))
