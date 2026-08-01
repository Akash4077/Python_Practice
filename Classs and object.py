class Person:
    name="Akash"
    occupation="Data Analysis"
    network=45
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person
b=Person
c=Person
a.name="puja"
a.occupation="HR"

b.name="Akash"
b.occupation="Data Analysis"

a.info()
b.info() 
c.info()