a = int(input("Enter start of the range: "))  
b = int(input("Enter end of the range: "))  
  
for num in range(a,b):
    temp=num
    a=num%10
    b=num//100
    c=num//10
    d=c%10 
    arm=a**3 + b**3 + d**3
    # print(arm) 
    if arm==temp:
        print("Given number {} is an armstrong number ".format(temp))