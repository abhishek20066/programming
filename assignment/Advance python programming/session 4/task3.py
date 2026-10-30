class PaymentFailedError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Payment failed: Invalid amount.")

    print("Payment Successful")


try:
    process_payment(500)
    process_payment(0)

except PaymentFailedError as e:
    print(e)