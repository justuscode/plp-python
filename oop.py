# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is powering on..."

    def power_off(self):
        return f"{self.brand} {self.model} is shutting down..."

# Child class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_life = battery_life

    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo!"

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

# Creating an object of Smartphone
my_phone = Smartphone("Apple", "iPhone 14", "128GB", "24 hours")


print(my_phone.power_on())
print(my_phone.take_photo())
print(my_phone.make_call("+123456789"))
print(my_phone.power_off())


#polymorphsm challenge
# Base class
class Vehicle:
    def move(self):
        pass

# Derived class
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Function to demonstrate polymorphism
def show_movement(vehicle):
    print(vehicle.move())

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
show_movement(car)
show_movement(plane)
show_movement(boat)
