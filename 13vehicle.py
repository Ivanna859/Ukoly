#inheritance
#Animal and Dog
#Person and Student
#Vehicle and Truck Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_seats):
        super().__init__(brand, model, year)
        self.number_of_seats = number_of_seats

    def display_info(self):
        return f"Car: {self.brand} {self.model} ({self.year}), Number of seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, brand, model, year, payload_capacity):
        super().__init__(brand, model, year)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return f"Truck: {self.brand} {self.model} ({self.year}), Payload capacity: {self.payload_capacity} kg"

# Example usage:
car = Car("Toyota", "Corolla", 2021, 5)
truck = Truck("Volvo", "FH16", 2019, 25000)

print(car.display_info())
print(truck.display_info())
