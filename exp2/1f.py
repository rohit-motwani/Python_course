import array as arr
a=arr.array('i',[])
n=int(input("Enter the length of the Array : "))

for i in range(0,n):
    x=int(input("Element {} : ".format(i)))
    a.append(x)
print(a)

print("Enter the index of element to be popped from array : ")
b=int(input())
a.pop(b)
print("Array after popping ")
print(a)


