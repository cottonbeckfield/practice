#!/usr/bin/env python

# Library/Functions
# comments are for chumps
import random

import glob

# Global Variables
# global variables!?  but... what if they change somewhere?

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
# represent words using a word representation...
class Word:
  def __init__(self, content):
    self.__content = content
    self.user_facing = self.hide_content()
    self.guesses = []

  def hide_content(self):
    content = list(self.__content)

    for index, character in enumerate(content):
      if content[index] != ' ':
        content[index] = '-'
    
    hidden = "".join(content)
    return hidden

  def find(self, guess_letter):
    return [i for i, ltr in enumerate(self.__content) if ltr == guess_letter]

  def guess(self, letter):
    self.guesses.append(letter)
    indexes = self.find(letter)
    if indexes == []:
      return False

    for i in indexes:
      print i
      first_letter = self.user_facing[i]
      print first_letter
      #first_letter = self.__content[i]
    return True
    
    
# Draw board / Update Board Function
class Hangman:
  def __init__(self):
    self.board = Board()
    self.answer = Word('giblets')

  def start(self):
    print('start')
         

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


hangman = Hangman().start()
