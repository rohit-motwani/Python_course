def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))

n=int(input("Enter the number to be found a factorial : "))
if n<0:
    print("Factorial of this number does not exist ")
else:
    print("Factorial of {} is : {}".format(n,factorial(n)))