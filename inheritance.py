#inheritance
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee:{self.id} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is python")
e1 = Employee("Akash Mandal",400)
e1.showDetails()
e2 = Employee("Aman Mandal",402)
e2.showDetails()
e3 = Employee("Bipin Mandal Mandal",403)
e3.showDetails()
e3.showLanguage()
