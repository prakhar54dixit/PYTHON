class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    
my_car=Car("tata","nexon")
print(my_car.brand,my_car.model)

my_newcar=Car("toyota","corolla")
print(my_newcar.brand,my_newcar.model)