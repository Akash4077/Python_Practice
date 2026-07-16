class Person:
    name="Akash"
    occupation="Data Analysis"
    network=45
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
c=Person()
a.name="puja"
a.occupation="HR"

b.name="Akash"
b.occupation="Data Analysis"

c.name="Ram"
c.occupation="Accountent"


a.info()
b.info() 
c.info()
print()


class Details:
    name = "Aakash"
    age = 21

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj = Details()
obj.desc()

