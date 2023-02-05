def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits


numheads = int(input("Enter the number of heads: "))
numlegs = int(input("Enter the number of legs: "))

chickens, rabbits = solve(numheads, numlegs)

if chickens == None:
    print("No solution found")
else:
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
# input: 35 94