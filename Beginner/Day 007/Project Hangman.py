import random
from hangman_words import word_list
from hangman_stage import stages, logo

print(logo)

game_over = False
heart = 6
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")

blank_word = ""
for char in chosen_word:
    blank_word += "_"
print(blank_word)
blank_word_list = list(blank_word)

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in blank_word_list:
        print(f"You've already guessed {guess}")

    if guess in chosen_word:
        for index in range(0, len(chosen_word)):
            if chosen_word[index] == guess:
                blank_word_list[index] = guess
                display_word = "".join(blank_word_list)
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        heart -= 1
        display_word = "".join(blank_word_list)

    print(display_word)
    print(f"You have {heart} live(s) left.\n")
    print(stages[heart])

    if "_" not in display_word:
        print("Game Over. You Win!")
        game_over = True

    if heart == 0:
        print("Game Over. You Lose!")
        print(f"The correct answer is {chosen_word}")
        game_over = True