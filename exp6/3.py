class Customer:
    stu_count=0
    def __init__(self):
        self.cust_id = input("Enter the Customer id : ") 
        self.cust_name=input("Enter the Customer name : ")
        self.cust_number=input("Enter the Customer mobile number : ")
        
    @classmethod
    def set_cust_count(self):
        while 1:
            try:
                self.stu_count=int(input('Enter the total number of Customers : '))
                return self.stu_count
            except:
                print("Invald input!!")
                continue
n=Customer.set_cust_count()
a=[]
print("-----------Enter the Details of Students ----------")
with open("Customer_detail.txt","a") as f:
    for i in range(0,n):
        cust=Customer()
        a.append(cust)

#-----------------write the details of customer------------------------
with open("Customer_detail.txt","w") as f:
    string="Customer_id\tCustomer_name\tCustomer_Number"
    f.write(string)
    for i in range(0,n):
        detail='\n'+a[i].cust_id+'\t\t\t'+a[i].cust_name+'\t\t\t'+a[i].cust_number
        f.write(detail)
#------------------read the written details----------------------
with open("Customer_detail.txt","r") as f:
    details=f.read()
    print(details)