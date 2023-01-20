n=int(input("Enter the total numbers required : "))

a=0
b=1
c=0
print(a)
for i in range(0,n-1):
    a=b
    b=c
    c=a+b
    print(c)