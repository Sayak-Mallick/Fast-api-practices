class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol / Diesel"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())
print(my_car.full_name())
print(my_car.fuel_type())
print(my_car.general_description())
print(Car.general_description())

my_new_car = Car("Tata", "Safari")
print(my_new_car.get_brand())
print(my_new_car.full_name())
print(my_new_car.fuel_type())
# my_new_car.model = "City"
print(my_new_car.model)

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())
print(my_tesla.full_name())
print(my_tesla.fuel_type())

print("Total cars till now: ", Car.total_cars)

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

class Engine:
    def engine(self):
        return "This is an engine"

class Battery:
    def battery(self):
        return "This is an battery"


class ElectricCarTwo(Engine, Battery, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Zedire")
print(my_new_tesla.battery())
print(my_new_tesla.engine())