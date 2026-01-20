import time

class Food:
    def __init__(self, food_id, name, category, price):
        # Encapsulation: private variables
        self.__food_id = food_id
        self.__name = name
        self.__category = category
        self.__price = price

    def get_food_id(self):
        return self.__food_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def details(self):
        return f"{self.__food_id}  {self.__name}  {self.__category}  ${self.__price}"

class Outlet:
    def __init__(self, outlet_id, name):
        self.__outlet_id = outlet_id
        self.__name = name
        self.__menu = []

    def add_food_item(self, food_item):
        self.__menu.append(food_item)

    def show_menu(self):
        print(f"\n--- Menu at {self.__name} ---")
        print("ID  Name                 Type     Price")
        print("----------------------------------------")
        for item in self.__menu:
            print(item.details())
        print("----------------------------------------")

    def get_menu(self):
        return self.__menu.copy()


class Cart:
    def __init__(self):
        self.__items = [] 
        self.__total = 0

    def add_to_cart(self, food, quantity):
        self.__items.append((food, quantity))
        print(f"Added {quantity} x {food.get_name()} to cart.")

    def remove_from_cart(self, food_id):
        for i, (food, qty) in enumerate(self.__items):
            if food.get_food_id() == food_id:
                removed_item = self.__items.pop(i)
                print(f"Removed {removed_item[0].get_name()} from the cart.")
                return
        print("Food ID not found in cart.")

    def calculate_total(self):
        self.__total = 0
        for food, qty in self.__items:
            self.__total += food.get_price() * qty
        return self.__total

    def show_cart(self):
        if not self.__items:
            print("\nCart is empty!")
            return
        print("\n--- Current Cart ---")
        print("Item                 Qty   Price")
        print("-------------------------------")
        for food, qty in self.__items:
            print(f"{food.get_name():<18} {qty:<5} ${food.get_price() * qty}")
        print("-------------------------------")
        print(f"Total Amount: ${self.calculate_total()}")
        print("-------------------------------")

    def checkout(self):
        if not self.__items:
            print("Cart is empty. Cannot checkout.")
            return
        print("Processing your order", end="")
        for _ in range(5):
            time.sleep(0.5)
            print(".", end="")
        print(f"\nOrder placed successfully!\nTotal to pay: ${self.calculate_total()}\nThank you for ordering!")


def main():
    food_list = [
        Food(1, "Onion Pizza", "Veg", 8),
        Food(2, "Chicken Pizza", "Non-Veg", 10),
        Food(3, "Veg Burger", "Veg", 5),
        Food(4, "Chicken Burger", "Non-Veg", 7),
        Food(5, "Coke", "Drink", 6),
        Food(6, "Pepsi", "Drink", 3)
    ]

    pizza_hut = Outlet(101, "Pizza Hut")
    for food_item in food_list:
        pizza_hut.add_food_item(food_item)

    cart = Cart()

    while True:
        print("\n1. Show Menu")
        print("2. Add Item to Cart")
        print("3. Show Cart")
        print("4. Remove Item from Cart")
        print("5. Place Order and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            pizza_hut.show_menu()

        elif choice == "2":
            try:
                food_id = int(input("Enter Food ID to add: "))
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be greater than 0.")
                selected_food = None
                for food_item in pizza_hut.get_menu():
                    if food_item.get_food_id() == food_id:
                        selected_food = food_item
                        break
                if selected_food:
                    cart.add_to_cart(selected_food, quantity)
                else:
                    print("Food ID not found in menu.")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "3":
            cart.show_cart()

        elif choice == "4":
            try:
                food_id = int(input("Enter Food ID to remove: "))
                cart.remove_from_cart(food_id)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            cart.show_cart()
            cart.checkout()
            break

        else:
            print("Invalid choice. Please choose the correct option.")


if __name__ == "__main__":
    main()
