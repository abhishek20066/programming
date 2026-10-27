def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print(movie_name, seat_type, snacks)

book_movie_ticket("Jawan", "VIP", "Popcorn")
book_movie_ticket(movie_name="Pathaan", seat_type="Regular", snacks="Cold Drink")
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")