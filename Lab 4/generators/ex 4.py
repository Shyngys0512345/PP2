def squares():
    a=int(input("a="))
    b=int(input("b="))
    for i in range(a,b+1):
        yield i**2
square = squares()
for sqa in square:
    print(sqa)