import array as arr
a=arr.array('i',[])
b=arr.array('i',[])
n=int(input("Enter the length of the array : "))

for i in range(0,n):
    x=int(input("Element {} : ".format(i)))
    a.append(x)
b.append(2)

for i in a:
    for j in range(2,i):
        if(i % j==0):
            break
        if(j==i-1):
            b.append(i)

for s in b:
    while s in a:
        a.remove(s)
print(a)