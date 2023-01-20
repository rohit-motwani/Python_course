import array as arr
a=[]
b=[]
c=[]
don=[]

n=int(input("Enter the length of list : "))
def even(a):
    for i in range(0,n):
        if(a[i]%2==0):
            b.append(a[i])
    return b
    
def odd(a):
    for i in range(0,n):
        if(a[i]%2!=0):
            c.append(a[i])
    return c    

def merge_sort(e,o):
    merge=e+o
    print("After merging list : {} ".format(merge))
    print("After sorting the list is : {}".format(sorted(merge)))
    
def mid_term():
    x=n//2
    print("Middle term of a list is : {}".format(a[x]))

def replace():
    t=int(input("Enter the number by which you have to replace : "))
    a.remove(a[0])
    a.insert(0,t)
    print(a)
      
    
for j in range(0,n):
    ele=int(input("element {} : ".format(j)))
    a.append(ele)

choice=0
while  choice<5:
    print("-----------Choices---------------")
    print("1.Put even and odd elements in two different list\n2.Merge and sort two list\n3.Update the first element with a value X\n4.Print middle element of list\n5.Exit")
    choice=int(input("Enter the option : "))
    if(choice==1):
        print("Array of even elements is : {}".format(even(a)))
        print("Array of odd elements is : {}".format(odd(a)))    
    elif(choice==2):
        n2=int(input("Enter the length of second list : "))
        for i in range(0,n2):
            ele2=int(input("Element {} : ".format(i)))
            don.append(ele2)
        print(merge_sort(a,don))
    elif(choice==3):
        replace()
    elif(choice==4):
        mid_term()
    else:
        print("Exiting!!")