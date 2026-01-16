class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        # Default behavior for a standard car
        print(f"{self.brand}: Vroom vroom! (Engine roaring)")

class ElectricCar(Car):
    def drive(self):
        # Overriding the parent behavior with something specific
        print(f"{self.brand}: ... (Silent electric hum)")

class Truck(Car):
    def drive(self):
        # Another variation
        print(f"{self.brand}: Rumble rumble! (Heavy diesel engine)")