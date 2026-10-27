products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

result = list(filter(lambda item: item.startswith('M'), products))

print(result)