import random

while True:
    number = random.randint(1, 10)
    guess = input("Guess the number between 1 to 10:\n ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == number:
        
        print("🎉 You Won!\n")
    else:
        
        print(f"❌ You Lost. The number was {number}\n")
