#PYTHON PROGRAM EXPLORING LISTS
def even_odd(list1):
  even=[]
  odd=[]
  for i in list1:
    if(i%2==0):
      even.append(i)
    else:
      odd.append(i)
  print("List of even numbers is:",even)
  print("List of odd numbers is:",odd)

def merge_sort(list1):
  l1=[]
  num=int(input("Enter the no. of elements of a list:"))
  for i in range(num):
    print("Enter the element",i+1,":")
    element=int(input())
    l1.append(element)
  print("Newly created list is:",l1)
  l3=list1+l1
  print("Merged list is:",l3)
  print("Sorted list is:",sorted(l3))

def update_first(list1):
  insert=int(input("Enter the element to be inserted:"))
  l4=[]
  l4=list1.insert(0,insert)
  print(l4)

def middle(list1):
  print("Middle element of the list is:",end=" ")
  print(list1[int(len(list1)//2)])

l=[]
n=int(input("Enter the no. of elements of a list:"))
for i in range(n):
  print("Enter the element",i+1,":")
  ele=int(input())
  l.append(ele)
print(l)

choice =0
while(choice <5):
    print("1.EVEN ODD \n2.MERGE AND SORT \n3. UPDATE THE FIRST ELEMENT \n4. GET MIDDLE OF LIST")
    print("Enter your choice:")
    choice=int(input())
    if(choice==1):
        even_odd(l)
    elif(choice==2):
        merge_sort(l)
    elif(choice==3):
        update_first(l)
    elif(choice==4):
        middle(l)   
    else:
        print("Invalid choice")