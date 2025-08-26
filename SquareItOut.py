def square_values(start: int, end: int):
    squares = [num ** 2 for num in range(start, end + 1)]

    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("All squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)


square_values(1, 10)

