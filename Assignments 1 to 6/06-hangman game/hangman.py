"""Bhaiya, tumne 10/10 sahi jawab diye! 🎉🔥

✅ Full Marks: 10/10 ⭐⭐⭐⭐⭐

Mubarak ho, tum Hangman game ka MCQ champion ban gaye ho! 😃💪 Ab koi aur topic chahiye practice ke liye?"""




import random

def hangman():
    words = ["python", "hangman", "game", "code", "fun"]
    word = random.choice(words)
    guessed = "_" * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(guessed)

    while tries > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            guessed = "".join([letter if letter in guessed_letters else "_" for letter in word])
        else:
            print("Wrong guess!")
            tries -= 1
            guessed_letters.append(guess)

        print(guessed)
        print(f"Tries left: {tries}")

    if "_" not in guessed:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was: {word}")

hangman()