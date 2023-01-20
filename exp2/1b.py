import array as arr
a=arr.array('i',[])
    
n=int(input("Enter the length of array : "))
for i in range(0,n):
    x=int(input("Element {} : ".format(i+1)))
    a.append(x)

b=int(input("Enter the element to be appended : "))
a.append(b)
print(a)
