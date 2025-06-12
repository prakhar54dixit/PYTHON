class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car=Car("tata","nexon")
print(my_car.brand,my_car.model)
print(my_car.full_name())
my_newcar=Car("toyota","corolla")
print(my_newcar.brand,my_newcar.model)