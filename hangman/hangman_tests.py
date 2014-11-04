import unittest
from hangman import Board, Word

class HangmanBoardTest(unittest.TestCase):
  def setUp(self):
    self.hangman_board = Board()

  def test_should_initialise_in_empty_state(self):
    self.assertEqual(0, self.hangman_board.state())

  def test_should_increment_board_state(self):
    self.hangman_board.increment()
    self.assertEqual(1, self.hangman_board.state())

  def test_should_load_in_board_from_files(self):
    self.assertTrue(isinstance(self.hangman_board.draw(), str))

  def test_progress_should_not_be_greater_than_file_number(self):
    board = Board()
    board.draw()
    board.increment()
    board.draw()
    board.increment()
    board.draw()
    board.increment()
    board.draw()
    board.increment()
    board.draw()
    board.increment()
    board.draw()
    board.increment()
    board.draw()

class WordTest(unittest.TestCase):
  def test_hide_content(self):
    testWord = Word('bob is my friend')
    self.assertEqual(testWord.hide_content(), '--- -- -- ------')

  def test_guess_indexes(self):
    testWord = Word('I was unable to add a aardvark')
    self.assertEqual(testWord.find('a'), [3, 8, 16, 20, 22, 23, 27])

  def test_no_hit(self):
    testWord = Word('none of that here')
    self.assertFalse(testWord.guess('s'))

  def test_got_hit(self):
    testWord = Word('all of that here')
    self.assertTrue(testWord.guess('a'))

  #def test_guess_and_replace(self):
  #  testWord = Word('giblets')
  #  testWord.guess('g')
  #  self.assertEqual(testWord.user_facing, 'g------')
  #  self.assertEqual(testWord.guesses, ['g'])

  def test_guess_input_is_ok(self):
    print ('')
    # assert guess is not shite

suite = unittest.TestLoader().loadTestsFromTestCase(HangmanBoardTest)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(WordTest)
unittest.TextTestRunner(verbosity=2).run(suite)
