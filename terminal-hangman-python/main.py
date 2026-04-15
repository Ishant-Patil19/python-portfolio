from hangman_art import logo, stages
from hangman_words import word_list
import random

lives = 6
print(logo)

word = random.choice(word_list)
word_length = len(word)

placeholder = ""

for letter in range(word_length):
    placeholder += "_"

print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = " "

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess:" + display)

    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {word}! YOU LOSE**********************")


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(stages[lives])