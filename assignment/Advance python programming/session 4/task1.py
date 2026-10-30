class InvalidCouponCodeError(Exception):
    pass


valid_coupons = ["ZOMATO50", "FOOD20", "SAVE100"]

coupon = input("Enter coupon code: ")

try:
    if coupon not in valid_coupons:
        raise InvalidCouponCodeError("Invalid coupon code!")

    print("Coupon applied successfully.")

except InvalidCouponCodeError as e:
    print(e)