def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

numbers = list(map(int, input("Enter numbers: ").strip().split()))
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list are: ", prime_numbers)