a = str(input("Enteer the string : "))
print("The original string is : " + a)
res = a[0] + a[1:].replace(a[0], '@')
print("Replaced String : " + str(res))