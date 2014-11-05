#!/usr/bin/env python

import random
import glob

class Word:
  """Represents the word that a user is trying to guess"""
  def __init__(self, content):
    self.__content = content
    self.user_facing = self.hide_content()

  def hide_content(self):
    content = list(self.__content)

    for index, character in enumerate(content):
      if content[index] != ' ':
        content[index] = '-'
    
    hidden = "".join(content)
    return hidden

  def find(self, guess_letter):
    return [i for i, ltr in enumerate(self.__content) if ltr == guess_letter]

  def revealLettersForCharacters(self, arrayOfIndices):
    for i in arrayOfIndices:
      self.user_facing = self.replaceCharAtIndexWith(i, self.__content[i])

  def replaceCharAtIndexWith(self, index, replacement):
    return self.user_facing[:index] + replacement + self.user_facing[index:-1]

  def testGuess(self,guess):
    hits = self.find(guess)
    if len(hits) > 0:
      self.revealLettersForCharacters(hits)
      return True
    else:
      return False
 
class Hangman:
  """A class to represent the game and set up the board and word to guess"""
  def __init__(self):
    self.board = Board()
    self.answer = Word('giblets')
    self.userHasWon = False
    self.guesses = []

  def printState(self):
    print(self.board.draw())
    print(self.guesses)
    print(self.answer.user_facing)

  def invalidUserGuess(self, guess):
    return self.duplicateGuess(guess) or self.notSingleLetter(guess)

  def duplicateGuess(self, guess):
    if guess in self.guesses:
      print('You already guessed that')
      return True
 
  def notSingleLetter(self, guess):
    if len(guess) != 1:
      print('Guess should be a single character')
      return True

  def start(self):
    while not self.userHasWon:
      guess = raw_input('Guess a Letter: ')
      
      if self.invalidUserGuess(guess):
        continue 
      self.guesses.append(guess)

      if self.answer.testGuess(guess):
        print(self.answer.user_facing)
      else:      
        self.board.increment()
        print(self.answer.user_facing)

      self.printState()

      if self.board.hasLost:
        self.userHasLost = True
	  
  def guess(self, letter):
    self.guesses.append(letter)
    indexes = self.find(letter)
    if indexes == []:
      return False

    for i in indexes:
      first_letter = self.user_facing[i]
    return True

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

  def hasLost(self):
    return self.progress == len(self.BOARD_PIC_FILES - 1) 

  def increment(self):
    if (self.progress < len(self.BOARD_PIC_FILES) - 1):
      self.progress += 1  

hangman = Hangman().start()
