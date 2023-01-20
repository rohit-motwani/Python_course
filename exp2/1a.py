import array as arr
a=arr.array('i',[])
n=int(input("Enter the length of the Array : "))

for i in range(0,n):
    a.append(int(input("Element : {}  ".format(i))))

print(a)
    