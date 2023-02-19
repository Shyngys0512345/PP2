def even_number():
    n = int(input("n="))
    for i in range(0, n+1):
        if i%2==0:
            yield i

even = even_number()
print(*even, sep=",")