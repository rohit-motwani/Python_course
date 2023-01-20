import array as arr
a=arr.array('i',[])
n=int(input("Enter the length of the Array : "))

for i in range(0,n):
    x=int(input("Element {} : ".format(i)))
    a.append(x)
print("Enter the element to be inserted and at which position ")
b=int(input("Enter the element : "))
c=int(input("Enter the index to be located : "))

a.insert(c,b)
print(a)