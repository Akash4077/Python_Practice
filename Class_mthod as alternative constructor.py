#Class mthod as alternative constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,data_string):
        name,age=data_string.split(',')
        return cls(name,int(age))
#using alternative constructor
p1=Person.from_string("Akash,21")
print(p1.name,p1.age)
print(help(Person))
