class phone:
    def __init__(self,model,price,color):
        self.model=model
        self.price=price
        self.color=color
    def offer(self):
        print(f"The {self.color} colour {self.model} which costs {self.price} is now having 20% discount")
my_phone=phone("iphone",100000,"black")
print(my_phone.model)
print(my_phone.price)
print(my_phone.color)
my_phone.offer()