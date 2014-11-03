import unittest
from hangman import Board

class HangmanBoard(unittest.TestCase):
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

suite = unittest.TestLoader().loadTestsFromTestCase(HangmanBoard)
unittest.TextTestRunner(verbosity=2).run(suite)
