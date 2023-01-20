a=[]
def add_all():
    x=len(a)
    sum=0
    for i in range(0,x):
        sum=sum+a[i]
    print("Sum of all elements is {} ".format(sum))
    
def product_all():
    x=len(a)
    prod=1
    for i in range(0,x):
        prod=prod*a[i]
    print("Sum of all elements is {} ".format(prod))

def add_at_even():
    x=len(a)
    sum2=0
    for i in range(0,x):
        if i%2!=0:
            sum2=sum2+a[i]
    print("Sum of elements at even places is : {} ".format(sum2))

def insert_an_element():
    ele=int(input("Insert the element : "))
    a.append(ele)

choice=0
while choice<5:
    print("1.ADD all the elements\n2.Product of all elements\n3.Summation of elements at even indices\n4.Add elements in the list\n5.Exit\n")
    choice=int(input("Select the option : "))
    
    if choice ==1:
        add_all()
    elif choice==2:
        product_all()
    elif choice == 3:
        add_at_even()
    elif choice==4:
        insert_an_element()
    else:
        print("Exiting!!")