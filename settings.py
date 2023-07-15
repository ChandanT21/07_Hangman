import random

# small = 2-4; medium = 5-7; large = 7+
all_words = []
small_word_list = []
medium_word_list = []
large_word_list = []

level = [all_words, small_word_list, medium_word_list, large_word_list]

save_settings = [level[1], ]


def read_file():
    with open("word.txt") as file:
        lines = file.readlines()
        for line in lines:
            all_words.append(line.strip('\n'))
            if 2 <= len(line) < 5:
                small_word_list.append(line.strip('\n'))
                random.shuffle(small_word_list)
            elif 5 <= len(line) < 7:
                medium_word_list.append(line.strip('\n'))
                random.shuffle(medium_word_list)
            else:
                large_word_list.append(line.strip('\n'))
                random.shuffle(large_word_list)


def set_settings():
    game_mode = ['easy', 'medium', 'hard']
    mode = input(f'Select your game mode: {game_mode}')


