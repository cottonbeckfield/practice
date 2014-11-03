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

suite = unittest.TestLoader().loadTestsFromTestCase(HangmanBoard)
unittest.TextTestRunner(verbosity=2).run(suite)
