import array as arr
a=arr.array('i',[])

sum=0
n=int(input("Enter the total length of array : "))
for i in range(0,n):
    ele=int(input("Element {} : ".format(i)))
    a.append(ele)
    sum=sum+ele
    
print("Sum of all elements is : {}".format(sum))

import array as arr
a=arr.array('i',[])

prod=1
n=int(input("Enter the total length of array : "))
for i in range(0,n):
    ele=int(input("Element {} : ".format(i)))
    a.append(ele)
    prod=prod*ele
    
print("Sum of all elements is : {}".format(sum))
    
import array as arr
a=arr.array('i',[])

sum=0
n=int(input("Enter the total length of array : "))
for i in range(0,n):
    ele=int(input("Element {} : ".format(i)))
    a.append(ele)

for i in range(0,n):
    if i%2==0:
        sum=a[i]+sum    
print("Sum of all elements is : {}".format(sum))


import array as arr
a=arr.array('i',[])

b=int(input("Enter the element : "))
a.append(b)
print(a)