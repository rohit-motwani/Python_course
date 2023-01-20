class Student:
    stu_count=0
    def __init__(self):
        self.r_no = input("Enter the Student roll number : ") 
        self.name=input("Enter the name : ")
        self.marks=input("Enter the marks : ")
        
    def Fail(Exception):
        '''Student scored less marks Faill!!!!'''

    @classmethod
    def set_stu_count(self):
        while 1:
            try:
                self.stu_count=int(input('Enter the total number of Students : '))
                return self.stu_count
            except:
                print("Invald input!!")
                continue

n=Student.set_stu_count()
a=[]
print("-----------Enter the Details of Students ----------")
for i in range(0,n):
    stu=Student()
    a.append(stu)
print("-----------Details of Students are----------")

print("Roll Number\tName\tMarks")
for i in range(0,n):
    print("{}\t\t{}\t{}".format(a[i].r_no,a[i].name,a[i].marks))

print("------------Details after checking grades--------------")
for i in range(0,n):
    try:
        if(int(a[i].marks)<40):
            raise Fail
        else:
            print("{}\t\t{}\t{}".format(a[i].r_no,a[i].name,a[i].marks))
    except:
        print("{}\t\t{}\tF".format(a[i].r_no,a[i].name))