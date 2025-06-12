class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The sqaure of number is {self.n**2}.")

    def cube(self):
        print(f"The cube of number is {self.n**3}.")

    def squarert(self):
        print(f"The sqaurert of number is {self.n**0.5}.")


prakhar=Calculator(4)
prakhar.square()
prakhar.cube()
prakhar.squarert()



