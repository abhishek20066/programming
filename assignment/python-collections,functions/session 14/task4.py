orders = {}

def add_order(order_id, restaurant, items, total):
    orders[order_id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }

def update_total(order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found")


add_order(101, "Pizza Hut", ["Pizza", "Garlic Bread"], 500)
add_order(102, "Dominos", ["Burger Pizza"], 250)

update_total(101, 600)

print(orders)