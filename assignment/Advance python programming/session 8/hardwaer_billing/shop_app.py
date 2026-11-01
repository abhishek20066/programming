import hardware_shop.pricing as pricing
import hardware_shop.stock as stock
from hardware_shop.stock import reduce_stock, OutOfStockError
from hardware_shop import new_bill_number


customers = [
    {"name": "Customer 1", "item": "Hammer", "quantity": 120, "box_size": 50},
    {"name": "Customer 2", "item": "Screwdriver", "quantity": 80, "box_size": 20},
    {"name": "Customer 3", "item": "Drill", "quantity": 700, "box_size": 100}
]


for customer in customers:
    print("\nCustomer:", customer["name"])

    boxes = pricing.boxes_needed(
        customer["quantity"], customer["box_size"]
    )

    try:
        reduce_stock(customer["item"], boxes)

        price = stock.items[customer["item"]]["price"]
        amount = boxes * price
        gst = pricing.gst_amount(amount)
        total = pricing.round_down_to_five(amount + gst)

        print("Bill Number:", new_bill_number())
        print("Item:", customer["item"])
        print("Boxes:", boxes)
        print("GST:", gst)
        print("Total:", total)

    except OutOfStockError as error:
        print("Stock Error:", error)