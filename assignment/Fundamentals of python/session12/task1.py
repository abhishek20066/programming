def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


result = get_discounted_price(500, 10)
print(result)