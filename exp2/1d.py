import array as arr
a=arr.array('i',[])
n=int(input("Enter the length of the array : "))

for i in range(0,n):
    a.append(int(input("Element : {}  ".format(i))))


print("Length in bytes of one array item %d"%a.itemsize)
    