def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def filter_prime(numbers):
    return list(filter(is_prime, numbers))


numbers = list(map(int, input("Enter numbers: ").split()))
print("Prime numbers in the list:", filter_prime(numbers))