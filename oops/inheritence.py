# base class
class Laptop:
    def __init__(self, brand="hp", ram=8):
        self.brand = brand
        self.ram = ram
    def show_specs(self):
        return f"brand: {self.brand}, ram: {self.ram}GB"


class GamingLaptop(Laptop):
    def __init__(self, brand, ram, gpu):
        super().__init__(brand, ram)
        self.gpu = gpu
    def show_specs(self):
        return f"brand: {self.brand}, ram: {self.ram}GB, gpu: {self.gpu}"
obj=Laptop()
g = GamingLaptop("asus", 16,10)
print(g.show_specs())

print(obj.show_specs())
