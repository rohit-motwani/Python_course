class Employee:
    def __init__(self, ID):
        self.ID = ID
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_id(self):
        return self.ID
class Student:
    def __init__(self, college):
        self.college
    def get_college(self):
        return self.college
class Intern(Employee, Student):
    def __init__(self, ID, college, period):
        self.ID = ID
        self.college = college
        self.period = period
    def set_details(self, name):
        self.name = name
    def get_details(self):
        print("***** Intern Details ******\n")
        print('Intern Name:', self.name)
        print('College Name:', self.college)
        print('Intern Name:', str(self.ID))
        print('Internship Period:', str(self.period), 'months ')
I1 = Intern(2003114, 'TSEC', 3)
I1.set_details('Rohit Motwani')
I1.get_details()