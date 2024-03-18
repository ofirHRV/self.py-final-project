
--------------------------HANGMAN GAME: CAMPUS-IL SELF.PY FINAL PROJECT------------------------------

name:	Ofir Haruvi
grade: 	100

-----------------------------------------------------------------------------------------------------

Welcome to Hangman Game Instructions:

1. Selecting Secret Word:

	- You will be prompted to enter:
		(a) the path to a word file.
		(b) a position (index) for a word in the file.
	- Based on your input, a secret word will be selected for the game.

2. Displaying Hangman State:

	- You'll see the appropriate state of the hanging man based on your number of failed attempts.
	- The game starts with the opening position, which is the first position among the seven 
	  positions (the horizontal line of the rack).

3. Displaying Secret Word:

	- Below the hanging man, the secret word will be displayed using underscores (with spaces) 
	  representing each letter of the word.

4. Guessing Process:

	- You need to input one character each round.
	- Input validation:
		- If your input is incorrect (not a single English letter or already guessed), you'll 
		  see "X" on the screen.
		- The list of letters guessed in the past will be displayed in lowercase letters, sorted 
		  in descending order and separated by arrows.
		- You'll be asked to input another character until a correct one is entered.

5. Updating Secret Word:

	- After each correct guess, the secret word will be displayed again with updated underscores, 
	  showing the correctly guessed letters.

6. Handling Failed Guess:

	- If your guess is incorrect, you'll see ":(" on the screen.
	- Below that, a picture of the hanging man in a more advanced state will be displayed.

7. End of the Game:

	- If you guessed the whole word correctly, "WIN" will be displayed on the screen.
	- If you reach six failed attempts, "LOSE" will be displayed on the screen.