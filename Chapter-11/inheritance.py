class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print(f"The car name is {self.brand} {self.model} .")

    def full_name(self):
        return f"{self.brand} {self.model}"
        

class Electric_car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
        print(f"The car name is {self.brand} {self.model} and battery is {self.battery_size}.")

p=Car("tesla","motar")
mytesla=Electric_car("Tesla","S Series","85kWh")
print(mytesla.full_name())
print(mytesla.battery_size)
print(mytesla.brand)

# my_car=Car("tata","nexon")
# print(my_car.brand,my_car.model)
# print(my_car.full_name())
# my_newcar=Car("toyota","corolla")
# print(my_newcar.brand,my_newcar.model)