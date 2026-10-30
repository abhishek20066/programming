def book_movie_ticket(tickets):
    wallet_balance = 1000

    try:
        tickets = int(tickets)
        price = wallet_balance / tickets
        print("Price per ticket:", price)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero.")

    except ValueError:
        print("Error: Please enter a valid number.")

book_movie_ticket(5)
book_movie_ticket(0)
book_movie_ticket("abc")