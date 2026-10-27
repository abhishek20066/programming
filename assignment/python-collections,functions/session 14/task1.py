cart = {}

cart.setdefault("Rahul", {})
cart["Rahul"]["Shoes"] = {"name": "Shoes", "quantity": 2, "price": 1500}
cart["Rahul"]["Bag"] = {"name": "Bag", "quantity": 1, "price": 800}

cart.setdefault("Amit", {})
cart["Amit"]["Watch"] = {"name": "Watch", "quantity": 1, "price": 2000}
cart["Amit"]["Shirt"] = {"name": "Shirt", "quantity": 3, "price": 500}

print(cart)