import random

secret_number = random.randint(1, 100)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too High!")
    
    elif guess < secret_number:
        print("Too Low!")
    
    else:
        print("Congratulations! You guessed the correct number.")
        break