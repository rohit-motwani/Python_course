def sort(dict1):
  print(sorted(dict1.keys()))  
  print(sorted(dict1.items()))

def concate(dict1):
  n=int(input("Enter the elements:"))
  d={}
  for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
  d.update({key:value})
  print(d)
  dict1.update(d)
  print(dict1)

n=int(input("Enter the elements:"))
dict={}
for i in range(n):
  key=input("Enter the key:")
  value=input("Enter the value:")
  dict.update({key:value})
print(dict)

print("1.SORT \n 2.CONCATENATE")
print("Enter your choice:")
choice=int(input())
if(choice==1):
  sort(dict)
elif(choice==2):
  concate(dict)
else:
  print("Invalid choice")