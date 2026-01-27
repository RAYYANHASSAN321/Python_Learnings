from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def rent_price(self, days):
        pass

    @abstractmethod
    def vehicle_type(self):
        pass

class Car(Vehicle):
    def rent_price(self, days):
        return 5000 * days

    def vehicle_type(self):
        return "Car"


class Bike(Vehicle):
    def rent_price(self, days):
        return 1000 * days

    def vehicle_type(self):
        return "Bike"


class Truck(Vehicle):
    def rent_price(self, days):
        return 8000 * days

    def vehicle_type(self):
        return "Truck"


vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    days = int(input(f"Enter rental days for {vehicle.vehicle_type()}: "))
    print(f"Vehicle Type: {vehicle.vehicle_type()}")
    print(f"Total Rent: {vehicle.rent_price(days)}\n")
