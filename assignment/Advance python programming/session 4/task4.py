class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie, seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError("Seat number must be positive")

    print("Ticket booked for", movie)


try:
    book_ticket("Avengers", -2)

except InvalidSeatNumberError as e:
    print(e)