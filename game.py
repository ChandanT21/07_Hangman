import display



def set_up(chosen_word):
    blank_space = ''
    for _ in range(len(chosen_word)):
        blank_space += '_'
    return blank_space


def trigger_game_logic(chosen_word, guess, hidden_word, wrong_guess):
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            hidden_word[position] = letter
    if guess not in hidden_word:
        wrong_guess += 1
        print(f'You guessed the letter {guess}, which is not in the word. You loose a life.')
    display.update_display(display.view[1], display.hangman_status[wrong_guess], guess)
    return [hidden_word, wrong_guess]
