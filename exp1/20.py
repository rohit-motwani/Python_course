num = int(input("Enter the number upto where do we have to check : "))

for i in range(1,num+1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if i == sum:
        print(i,"is an Armstrong number")