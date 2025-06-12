# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector.

class two_DVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

class three_DVector(two_DVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k

    def printVector(self):
        print(f"The vector is {self.i}i+{self.j}j+{self.k}k.")


v=three_DVector(2,-4,+6)
v.printVector()
