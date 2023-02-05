import random

print("Hello! What is your name?")
name = input()

print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
number = random.randint(1, 20)

attempts = 0
while True:
    attempts += 1
    print("Take a guess.")
    guess = int(input())

    if guess == number:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, attempts))
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")