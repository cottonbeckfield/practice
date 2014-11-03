#!/usr/bin/env python

# Library/Functions
# comments are for chumps
import random

import glob

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

class Board:
  """Represents a hanging man"""
  BOARD_PIC_FILES = glob.glob('files/*.txt')
  BOARD_PICS = []
  
  def __init__(self):
    self.progress = 0
    for index in range(len(self.BOARD_PIC_FILES)):  
      board_pic_file_name = self.BOARD_PIC_FILES[index]
      board_pic_file = open(board_pic_file_name, 'r')
      board_pic_file_contents = ''.join(board_pic_file.read())
      self.BOARD_PICS.append(board_pic_file_contents)
      board_pic_file.close() 

  def draw(self):
    return self.BOARD_PICS[self.progress]

  def state(self):
    return self.progress

  def increment(self):
    if (self.progress < len(self.BOARD_PIC_FILES) - 1):
      self.progress += 1  


