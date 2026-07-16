class Student:

    def __init__(self):
        self.__name = "Akash"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


s = Student()
print(s.get_name())
s.set_name("Ram")
print(s.get_name())