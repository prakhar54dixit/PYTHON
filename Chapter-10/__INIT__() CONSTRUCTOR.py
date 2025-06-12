class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self): # dunder method which is automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")



prakhar = Employee()
prakhar.name = "prakhar"
print(prakhar.name, prakhar.salary)

rohan = Employee()