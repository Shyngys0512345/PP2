def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

numbers = list(map(int, input("Enter a list of numbers: ").split()))
result = unique_list(numbers)
print(result)