import random
words = ["apple", "mango", "python", "computer", "school"]
word = random.choice(words)

guessed = ["_"] * len(word)
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
