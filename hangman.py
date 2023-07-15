import random

word_list = ["apple", "banana", "carrot", "dragon", "elephant", "flamingo", "giraffe", "hippo", "iguana", "jaguar",
             "kangaroo", "lemon", "mango", "nectarine", "orange", "pineapple", "quince", "raspberry", "strawberry",
             "tangerine", "umbrella", "violet", "watermelon", "xylophone", "yellow", "zebra", "acorn", "butterfly",
             "cat", "dog"] 

word = random.choice(word_list)

errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Chances left: {errors}. Try again: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        errors -= 1
        if errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print("Congratulations, you found the word!")
else:
    print(f"Game over! The word was {word}!")
