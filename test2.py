import unittest
import Excercise
class TestGame(unittest.TestCase):
    def test_game(self):
        result = Excercise.run_guess(5, 5)
        self.assertTrue(result)

    def test_game_wrong_guess(self):
        result = Excercise.run_guess(5, 1)
        self.assertFalse(result)


if __name__ == '__main__' :
    unittest.main()

        
