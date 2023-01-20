def decor_add(func):
    def inner():
        value1 = func()
        return value1+4
    return inner

def decor_multiply(func):
    def inner():
        value2 = func()
        return value2*2
    return inner

n=int(input("Enter the number : "))
def square():
    return n**2
def cube():
    return n**3
# num=int(input("Enter the number : "))
res1=decor_add(square)
res2=decor_multiply(cube)
print("Square of number +4 {} ".format(res1()))
print("Cube of number *2 {} ".format(res1()))

