import string
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
hangman_status = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O  |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===
 ''']

view = [logo, '\n', 'Game Over!', 'You Won!']

alphabet = list(string.ascii_uppercase)
alphabet_display = alphabet
alphabet_guessed = []


def print_display(display, stage):
    print(f'{display}')
    print(f'{stage}')
    print(f'Guess box: {alphabet_display}')
    if len(alphabet_guessed) != 0:
        print(f'Guessed box: {alphabet_guessed}')


def update_display(display, stage, guess):
    print(f'{display}')
    alphabet_display.remove(guess.upper())
    alphabet_guessed.append(guess.upper())
    alphabet_guessed.sort()
    print_display(display, stage)


def board(param):
    print(param)
