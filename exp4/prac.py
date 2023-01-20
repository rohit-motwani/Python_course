roll_no=[]
name=[]
sub1=[]
sub2=[]
sub3=[]

details=()
n=int(input("Enter the number of students : "))
def details_of_students():
    for i in range(0,n):
        roll_nos=str(input("Enter the Roll Number of student : "))
        roll_no.append(roll_nos)
        names=str(input("Enter the name of student : "))
        name.append(names)
        subj1=str(input("Enter the Marks of first subject : "))
        sub1.append(subj1)
        subj2=str(input("Enter the Marks of second subject : "))
        sub2.append(subj2)
        subj3=str(input("Enter the Marks of third subject : "))
        sub3.append(subj3)        
    
    lst_tuple=list(zip(name,roll_no,sub1,sub2,sub3))
    details=tuple(lst_tuple)
    print("Details of student are ")
    print(details)
    
def details_of_particular_student():
    n1=str(input("Enter the Name of student to be displayed : "))
    for i in range(0,n):
        if(details[i][0]==n1):
            print("Roll No. of Student is : {}".format(details[i][0]))
            print("Name : {}".format(details[i][1]))
            print("Marks in subject 1 : {}".format(details[i][2]))
            print("Marks in subject 2 : {}".format(details[i][3]))
            print("Marks in subject 3 : {}".format(details[i][4]))
choice=0
while(choice<3):
    print("1. Add and show details i.e roll no, name and marks of three subjects of N students in a list of tuple \n2.Display details of a student whose name is X\n3.Exit")
    choice=int(input("Select the option : "))
    if(choice==1):
        details_of_students()
    elif(choice==2):
        details_of_particular_student()
    else:
        print("Exitting!!!!")