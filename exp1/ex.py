a = str(input("Enter any string: "))
b=a
print("\nRemoving vowels from the given string")
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
for x in a.lower():
    if x in vowels:
        b = b.replace(x,"")
for y in a.upper():
    if y in vowels:
        b = b.replace(y,"")
print("New string after successfully removed all the vowels:")
print(b)