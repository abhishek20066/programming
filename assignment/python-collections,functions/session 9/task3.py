users = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]

result = filter(lambda x: x[1] > 1000, users)

for user in result:
    print(user[0])