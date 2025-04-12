import random

def guess_the_number():
    # Project 2 : Guess The Number Game
    # 1 to 1100 number
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    guesses_left = 7
    
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        
        try:
             guess = int(input("Take a guess of another number : "))
        except ValueError:
            print("Invalid input: Please enter a number.")
            continue
        
        # Guess the secret number 
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1
    
    # Jab sab guess finished ho jaen gy
    print(f"\nYou ran out of guesses. The number was {number}.")

# Run the game
guess_the_number()
