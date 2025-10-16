class Parentclass:
    def __init__(self, name, age, isWorking, *company):
        self.name = name
        self.age = age
        self.isWorking = isWorking
        self.company = company
    
    def displayDetails(self):
        print(f"My Name is {self.name} age of {self.age} company working {self.company} currently working is {self.isWorking}")

    # def __str__(self):
    #     return f"Name of company is {self.name} with addess of {self.age} {self.isWorking} {self.company}"

person = Parentclass("Sathishkumar", 26, True, "Candesent")
person.displayDetails()

class ChildClass(Parentclass):
    pass

child = ChildClass("Sathishkumar", 26, True, "Candesent")
print(child)
child.displayDetails()

class JobDetails(Parentclass):
    def __init__(self, name, age, isWorking, company):
        Parentclass.__init__(self, name, age, isWorking, company)

z = JobDetails("Tamil", 25, True, "Effeten")
z.displayDetails()

class JobDetails2(Parentclass):
    def __init__(self, name, age, isWorking, *company):
        super().__init__(name, age, isWorking, *company)

w = JobDetails2("Sabari", 25, False)
w.displayDetails()

class EmployeeDetails(Parentclass):
    def __init__(self, name, age, isWorking, *company):
        super().__init__(name, age, isWorking, *company)
        self.employeeStart = 2021

e = EmployeeDetails("Karthik", 25, True, "Unknow Company")
e.displayDetails()
print(e.employeeStart)

class EmployeeDetails2(Parentclass):
    def __init__(self, name, age, isWorking, company, employeeStart):
        super().__init__(name, age, isWorking, company)
        self.employeeStart = employeeStart
    
    # def __str__(self):
    #     return super().__str__(se) + f"EmployeeDetails {self.employeeStart}"

    def displayDetails(self):
         print(f"{self.employeeStart}")
    def welcome(self):
        print("Welcome", self.name, self.age, "to the class of", self.employeeStart)


e = EmployeeDetails2("Hello", 25, True, "Unknow Company", 2020)
e.displayDetails()
e.welcome()        




