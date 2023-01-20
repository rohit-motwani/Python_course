def perfect_num(n):
    Sum = 0
    for i in range(1, n):
        if(n % i == 0):
            Sum = Sum + i
    if (Sum == n):
        print(" %d is a Perfect Number" %n)
    else:
        print(" %d is not a Perfect Number" %n)  

num = int(input("Enter the number: "))
perfect_num(num)
   