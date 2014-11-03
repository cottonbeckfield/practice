#!/usr/bin/env python

# Library/Functions
import random

# Global Variables

# Core of Game.
def core(x):

	word = "givers" # Update to read random words from file.
	usedLetters = ''
	turns = 5

	while turns < 5:
		guess = raw_input('Guess a Letter: ')
		
		if guess not in word:
			usedLetters += "," + guess
			print (o) # Should be game board, in creation.
		# If not in word, increase turns count +
		# update the board.

# How to update a line system? - - - - - (represnt words)

# Draw board / Update Board Function
