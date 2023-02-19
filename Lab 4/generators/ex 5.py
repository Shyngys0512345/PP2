def numbers():
    n=int(input("n="))
    for i in range(n,-1,-1):
        yield i

for num in numbers():
    print(num)