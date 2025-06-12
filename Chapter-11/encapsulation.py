class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand 
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
my_car=Car("tata","nexon")
# print(my_car.__brand) ///this will not work ,you will be reqrd with getter method as given in next step.
print(my_car.get_brand())