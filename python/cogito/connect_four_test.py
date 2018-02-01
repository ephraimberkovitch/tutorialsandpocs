import unittest

import connect_four

class ConnectFourTests(unittest.TestCase):

    def test_connect_four_with_winner(self):
        board = [
            [0, 0, 1, 2, 1, 1, 0],
            [0, 0, 1, 2, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 2, 1, 1, 0],
            [0, 0, 0, 2, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
        ]
        self.assertEqual(
            1,
            connect_four.find_winner(board)
        )

    def test_connect_four_without_winner(self):
        board = [
            [0, 0, 1, 2, 1, 1, 0],
            [0, 0, 0, 2, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
            [0, 0, 1, 2, 1, 1, 0],
            [0, 0, 0, 2, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 0],
        ]
        self.assertEqual(
            0,
            connect_four.find_winner(board)
        )

if __name__ == '__main__':
    unittest.main()
