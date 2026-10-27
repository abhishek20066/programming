ratings = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]

result = [rating for restaurant in ratings for rating in restaurant if rating > 4]

print(result)