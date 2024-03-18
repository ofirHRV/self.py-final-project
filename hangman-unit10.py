import re

HANGMAN_ASCII_ART = ("""  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n """)  # welcome screen hangman logo

MAX_TRIES = ("6")  # welcome screen maximum tries per game

HANGMAN_PHOTOS = {0: """    x-------x""", 1: """    x-------x
    |
    |
    |
    |
    |
""", 2: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}  # hangman ascii art dict. attempts: hangman "stage"


def welcome_screen():
    """prints the hangman ascii logo and the maximum tries per game.
    :return: none"""
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def valid_file_path():
    """ Checks if the given file path exists.
    If so - returns it as a string.
    :return file_path: a valid file path"""
    flag = False  # default value
    file_path = ""  # a string which will eventually contain a valid file path
    while flag == False:
        file_path = input("Enter file path: ")  # a file path inserted by the player
        try:
            flag = True
            with open(file_path, "r") as open_file:
                open_file.read()
                open_file.close()
        except IOError:  # if the file path doesn't exist
            print("File path doesn't exist.")
            flag = False  # returns to the beginning of the loop in order to get a valid file path
    return file_path


def valid_index():
    """ Checks if the given index is valid (numeric).
    If so - returns it as an integer.
    :return: a valid index
    :rtype: int"""
    flag = False  # default value
    while flag == False:
        index = input("Enter index: ")  # an index inserted by the player
        if index.isnumeric():  # if the index is numeric
            flag = True
        else:
            print("index isn't numeric.")
            flag = False  # returns to the beginning of the loop in order to get a valid index
    return int(index)


def check_win(secret_word, old_letters_guessed):
    """Determines if the player won the Hangman game (guessed all the letters of the secret word).
    :param secret_word: The word that the player need to reveal.
    :param old_letters_guessed: The letters that the player already guessed.
    :type secret_word: str
    :type old_letters_guessed: list
    :return: If the player guessed all the letters of the secret word - True.
    If the player hasn't guessed all the letters of the secret word - False.
    :rtype: bool"""
    right_letters_guess = []  # a list which will contain the right guesses in the order of their appearance in the secret word.
    for letter in secret_word:
        if letter in old_letters_guessed:  # the right letter guessed
            right_letters_guess.append(letter)  # adds the right letters guessed to right_letter_guess list
    right_letters_guess_str = "".join(right_letters_guess)  # right_letters_guess as a string
    if right_letters_guess_str == secret_word:
        return True  # the player won
    else:
        return False  # the player hasn't won


def show_hidden_word(secret_word, old_letters_guessed):
    """Shows the right letter guesses of the secret word, in the right order.
    The letters yet to guess appears as underscores.
    :param secret_word: The word that the player need to reveal.
    :param old_letters_guessed: The letters that the player already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return secret_word_guess_str: The right letter guessed in the right places.
    Letters yet to be guessed as underscore.
    :rtype: str"""
    secret_word_guess = []  # a list which will contain the right guesses and the yet to guess letters as underscore.
    # (in the order of their appearance in the secret word)
    for letter in secret_word:
        if letter in old_letters_guessed:  # the right guesses
            secret_word_guess.append(letter + " ")  # appends the letter to secret_word_guess
        elif letter not in old_letters_guessed:  # the yet to guess letters
            secret_word_guess.append("_ ")  # appends an underscore to secret_word_guess
    secret_word_guess_str = "".join(secret_word_guess)  # secret_word_guess as a string
    return secret_word_guess_str


def check_valid_input(letter_guessed, old_letters_guessed):
    """Determine whether or not the input is valid (one English letter, hasn't been guessed before)
    :param letter_guessed: the note or notes entered
    :param old_letters_guessed: The letters that already've been guessed before
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if one new english letter. False otherwise
    :rtype: bool"""
    valid_letter = (
            re.match("[a-z]", letter_guessed.lower()) and len(letter_guessed.lower()) == 1)  # one English letter
    valid_new = letter_guessed.lower() not in old_letters_guessed  # new letter.
    if valid_letter and valid_new == True:
        return True  # the note is one english letter that hasn't been guessed before
    else:
        return False  # the note isn't one english letter that hasn't been guessed before


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Determine if an input is valid and if so, adds it to guesses list.
     :param letter_guessed: the note or notes entered.
     :param old_letters_guessed: The letters that already've been guessed before.
     :type letter_guessed: str
     :type old_letters_guessed: list
     :return: True if one new english letter that hasn't been guessed before. False otherwise
     :rtype: bool"""
    if check_valid_input(letter_guessed, old_letters_guessed):
        # if the note is one english letter that hasn't been guessed before
        old_letters_guessed += [letter_guessed]
        # appends the letter to the list of letters that already've been guessed
        return True
    else:  # if the note isn't one english letter that hasn't been guessed before
        separator1 = ' -> '
        print("X\n", separator1.join(sorted(old_letters_guessed)))
        # print "X", and a the letters that already've been guessed in alphabetic order separated by "->"
        return False


def choose_word(file_path, index):
    """The function returns a word in a position obtained as an argument to a function (index),
    which will be used as the secret word for guessing.
     :param file_path: A path to a txt file which contains optional secret words.
     :param index: a number which represents the location of a particular word in a file.
     :type file_path: str
     :type index: int
     :return: the secret word
     :rtype: str"""
    file_open_r = open(file_path, "r")  # opens file_name for reading
    file_content = file_open_r.read()  # reads the opened file
    splited_list = file_content.split(" ")  # makes a list from the words that appear in the txt file.
    secret_word = splited_list[
        (index - 1) % len(splited_list)]  # choose a word from the words list. the slicing is based on the index given.
    # (when the index is larger than the number of words in the list, the function continues to count circularly)
    file_open_r.close()
    return secret_word  # the secret word


def one_game_run():
    """ The computer randomly selects a word and displays to the player its number of letters as underscores.
     The player need to guess the letters:
    if the letter he guesses appears in the word, the computer reveals the letter in all the places where it appears.
    If the guessed letter doesn't appear in the word, the player is given an attempt to try again.
    the number of attempts is limited.
    -
    The function runs the hangman game once.
    :return: none"""
    welcome_screen()  # the hangman ascii logo and the maximum tries per game
    file_path = valid_file_path()  # A path to a txt file which contains optional secret words
    index = valid_index()  # a number which represents the location of a particular word in the file
    secret_word = choose_word(file_path, index)  # the word that the player need to guess.
    num_of_tries = 0  # the number of wrong guesses the player has. updates (max 6).
    old_letters_guessed = []  # the letters that the player already guessed. updates.
    print(HANGMAN_PHOTOS[num_of_tries])  # prints the first "stage" of the hangman ascii (0)
    print(
        show_hidden_word(secret_word, old_letters_guessed))  # prints an underscore for each letters in the hidden word
    while num_of_tries < 6 and check_win(secret_word, old_letters_guessed) == False:
        # while the player hasn't won or lose
        letter_guessed = (input("Guess a letter: ")).lower()  # the letter guessed by the player
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            # updates the guessed letter in the secret word if it contains it.
            if letter_guessed not in secret_word:  # if the word doesn't contains the guessed letter:
                num_of_tries = num_of_tries + 1  # updates number of tries
                print(":(")
                print(HANGMAN_PHOTOS[num_of_tries])
                # prints the "stage" of the hangman ascii according to the players number of tries.
            print(show_hidden_word(secret_word, old_letters_guessed))
            # prints the right letter guesses of the secret word and the letters yet to reveal as underscores.
    if num_of_tries == 6:  # if the player lost the game:
        print(secret_word + "\nLOSE")  # prints the secret word and "lose".
    else:  # if the player won the game:
        print("WIN")  # prints "win"


def main():
    """ The hangman program
    :return: none"""
    play_again = 'y'
    while play_again == 'y':
        one_game_run()  # runs one round of the hangman game
        play_again = (input("would you like to play again? y/n ")).lower()
        # asks the player if he would like to play again at the end of the game.
        # y = rerun the game; n = finish process.
        while play_again != "y" and play_again != "n":  # if the input isn't valid
            print("input isn't valid")
            play_again = (input("would you like to play again? y/n ")).lower()
            # re-ask the player if he would like to lay again.
    print("Goodbye!")


if __name__ == "__main__":
    main()
