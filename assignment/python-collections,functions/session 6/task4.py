titles = ["3 Idiots", "Dangal", "Jawan"]
genres = ["Comedy", "Drama", "Action"]
ratings = [8.4, 8.3, 7.0]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movies.append({
        "title": title,
        "genre": genre,
        "rating": rating
    })

print(movies)