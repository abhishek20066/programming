def update_cart(cart, item, qty):
    cart[item] = qty
    return cart


my_cart = {
    "Shoes": 1,
    "T-Shirt": 2
}

my_cart = update_cart(my_cart, "Shoes", 3)
print(my_cart)

my_cart = update_cart(my_cart, "Jeans", 1)
print(my_cart)