from flask import Flask, jsonify

# Define food class
class Food:
    def __init__(self, id, food_name, price):
        self.id = id
        self.food_name = food_name
        self.price = price

    def to_dict(self):
        """Convert Food object to dictionary for JSON"""
        return {
            "id": self.id,
            "food_name": self.food_name,
            "price": self.price
        }

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/test")
def test():
    return "Test Method!"

@app.route("/nums")
def nums():
    nums_list = [10, 20, 30]
    return jsonify(nums_list) 


@app.route("/food")
def food_item():
    f = Food(101, "burger", 100)
    return jsonify(f.to_dict())


@app.route("/food_items")
def food_items():
    items = [Food(101, "burger", 100), Food(102, "pizza", 200)]
   
    items_dict = [item.to_dict() for item in items]
    return jsonify(items_dict)

if __name__ == "__main__":
    app.run(debug=True)
