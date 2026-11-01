class OutOfStockError(Exception):
    pass


items = {
    "Hammer": {"quantity": 10, "price": 250},
    "Screwdriver": {"quantity": 15, "price": 100},
    "Drill": {"quantity": 5, "price": 1500},
    "Nails": {"quantity": 20, "price": 50},
    "Paint": {"quantity": 8, "price": 500},
    "Pipe": {"quantity": 12, "price": 300},
    "Wrench": {"quantity": 7, "price": 200},
    "Cement": {"quantity": 25, "price": 400}
}


def check_stock(item):
    if item not in items:
        raise OutOfStockError("Item not found")
    return items[item]["quantity"]


def reduce_stock(item, qty):
    if item not in items:
        raise OutOfStockError("Item not found")

    if qty > items[item]["quantity"]:
        raise OutOfStockError("Not enough stock")

    items[item]["quantity"] -= qty