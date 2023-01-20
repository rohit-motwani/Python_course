import string
  
def pangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return 0
    return 1
      
string = str(input("Enter the string : "))
if(pangram(string) == 1):
    print("Yes given string is a pangram")
else:
    print("Given string is not a pangram")