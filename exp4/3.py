def inter(a,b):
    a&=b
    print("INTERSECTION:",a)
def un(a,b):
    a|=b
    print("UNION:",a)
def diff(a,b):
    a-=b
    print("DIFFERENCE:",a)
def sym_diff(a,b):
    a^=b
    print("SYMMETRIC DIFFERENCE:",a)

x=set()
y=set()
nx=int(input("Enter the number of elements in x set:"))
ny=int(input("Enter the number of elements in y set:"))
for i in range(nx):
    print("Enter the element", i+1 ,"for x set:")
    elementx=int(input())
    x.add(elementx)
    print(x)
for i in range(ny):
    print("Enter the element", i+1 ,"for y set:")
    elementy=int(input())
    y.add(elementy)
    print(y)
choice=0
while(choice<5):
    print("1.INTERSECTION \n 2.UNION \n 3.DIFFERENCE \n 4.SYMMETRIC DIFFERENCE")
    print("Enter your choice:")
    choice=int(input())
    if(choice==1):
        inter(x,y)
    elif(choice==2):
        un(x,y)
    elif(choice==3):
        diff(x,y)
    elif(choice==4):
        sym_diff(x,y)
    else:
        print("Invalid choice")