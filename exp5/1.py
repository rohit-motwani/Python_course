class Employee:
    emp_count=0
    def __init__(self):
        self.emp_id = input("Enter the emp_id : ") 
        Employee.emp_count+=1
        
    def set_name(self):
        self.emp_name=str(input("Enter the name : "))
    
    def get_name(self):
        print("My name is ",self.emp_name)
        
    def get_id(self):
        print("Id of the given name is ",self.emp_id)
    
    @classmethod
    def set_emp_count(self):
        while 1:
            try:
                self.emp_count=int(input('Enter the total number of employees : '))
                return self.emp_count
            except:
                print("Invald input!!")
                continue

n=Employee.set_emp_count()
a=[]
print("-----------Enter the Details of employee ----------")
for i in range(0,n):
    emp1=Employee()
    emp1.set_name()
    a.append(emp1)
print("-----------Details of employee are----------")
for i in range(0,n):
    a[i].get_name()
    a[i].get_id()


    
    

    