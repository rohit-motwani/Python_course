import array as arr
a=arr.array('i',[])
b=arr.array('i',[])
n=int(input("Enter the length of the first array : "))

for i in range(0,n):
    a.append(int(input("Element : {}  ".format(i))))

n2=int(input("Enter the length of the second array : "))
for i in range(0,n2):
    b.append(int(input("Element : {}  ".format(i))))

for i in b:
    a.append(i)
print(a)