def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        amount = amount * 0.9
    return amount

print(apply_coupon(1000))
print(apply_coupon(1000, "SAVE10"))