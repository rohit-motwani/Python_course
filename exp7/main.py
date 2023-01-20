from package.Account.salary import Salary
from package.Employee.profile import Profile
from package.Employee.Qualification import Qualification
n = int(input("Enter number of Employees: "))
emp_list = []
for i in range(n):
 name = input(f"Enter Name of Employee {i+1}: ")
 age = input(f"Enter Age of Employee {i+1}: ")
 dob = input(f"Enter Birth Year of Employee {i+1}: ")
 degree = input(f"Enter Degree of Employee {i+1}: ")
 experience = input(f"Enter Experience of Employee {i+1} (in years): ")
 basic = int(input(f"Enter Basic Pay of Employee {i+1}: "))
 hra = int(input(f"Enter HRA of Employee {i+1}: "))
 pf = int(input(f"Enter PF of Employee {i+1}: "))
 emp_prof = Profile(name, age, dob)
 emp_q = Qualification(degree, experience)
 emp_s = Salary(pf, basic, hra)
 t_salary = basic + hra - pf
 new_employee = [emp_prof, emp_q, emp_s, t_salary]
 emp_list.append(new_employee)
print()
print("Name\tAge\tDob\tDegree\tExp\tBasic\tHRA\tPF\tSalary")
print('-'*75)
for emp in emp_list:
 print(emp[0].name, emp[0].age, emp[0].dob, emp[1].degree, emp[1].experience,
emp[2].basicpay, emp[2].HRA, emp[2].PF, emp[3], sep='\t')