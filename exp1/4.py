a=int(input("Enter the Grade : "))

if a>=0 and a<=100:
    if a > 0 and a < 35:
        print("Grade : F ")
    elif a>35 and a<45:
        print("Grade : E ")
    elif a>45 and a<55:
        print("Grade : D ")
    elif a>55 and a<65:
        print("Grade : C ")
    elif a>65 and a<75:
        print("Grade : B ")
    elif a>75 and a<85:
        print("Grade : A ")
    else:
        print("Grade : A+")    
else:
    print("Grade is invalid")