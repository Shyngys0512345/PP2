def squares_number():
    N = int(input("N="))
    for i in range(1, N+1):
        yield i**2

squares = squares_number()
for square in squares:
    print(square)