from itertools import permutations

def get_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print("".join(perm))

input_string = input("Enter a string: ")
get_permutations(input_string)