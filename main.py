import random

import display
import game
import settings

hidden_word = []
wrong_guess = 0
word = ''

game_stats = [hidden_word, wrong_guess]

if __name__ == '__main__':
    settings.read_file()
    display.print_display(display.view[0], display.hangman_status[0])
    # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    chosen_word = random.choice(settings.all_words)
    hidden_word = list(game.set_up(chosen_word))
    display.board(''.join(str(element) for element in hidden_word))

    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    while game_stats[1] < 6 and word != chosen_word:
        guess = input("Guess a Letter: ").lower()
        if guess.isnumeric():
            print("You can only guess letter not numbers.")
        elif len(guess) > 1:
            print("You can only guess 1 letter at a time.")
        elif guess.upper() in display.alphabet_guessed:
            print(f'You have already guessed the letter {guess}, pick another letter.')
        else:
            # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
            game_stats = game.trigger_game_logic(chosen_word, guess, hidden_word, game_stats[1])
            word = ''.join(str(element) for element in hidden_word)
            display.board(word)

    if word == chosen_word:
        print(display.view[3])
    elif game_stats[1] == 6:
        print(display.view[2])
