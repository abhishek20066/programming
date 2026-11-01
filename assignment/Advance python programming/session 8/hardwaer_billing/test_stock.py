import hardware_shop.stock as stock

print(stock.check_stock("Hammer"))

stock.reduce_stock("Hammer", 2)

print(stock.check_stock("Hammer"))

try:
    stock.reduce_stock("Hammer", 100)
except stock.OutOfStockError as error:
    print(error)