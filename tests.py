# Importing only the necessary functions within the module
import unittest

from src.floyd_package.floyd import solve_paths, no_path


class Test(unittest.TestCase):
    def test_one(self):
        test = [[0, 5, no_path, 10],
                [no_path, 0, 3, no_path],
                [no_path, no_path, 0, 1],
                [no_path, no_path, no_path, 0]]

        expected = [[0, 5, 8, 9],
                    [no_path, 0, 3, 4],
                    [no_path, no_path, 0, 1],
                    [no_path, no_path, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)

    def test_two(self):
        test = [[0, 6, 2, no_path],
                [no_path, 0, no_path, 2],
                [no_path, no_path, 0, 6],
                [no_path, no_path, no_path, 0]]

        expected = [[0, 6, 2, 8],
                    [no_path, 0, no_path, 2],
                    [no_path, no_path, 0, 6],
                    [no_path, no_path, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)

    def test_three(self):
        test = [[0, 6, 2, 8],
                [2, 0, no_path, no_path],
                [5, 3, 0, 8],
                [no_path, 2, no_path, 0]]

        expected = [[0, 5, 2, 8],
                    [2, 0, no_path, no_path],
                    [5, 3, 0, 8],
                    [4, 2, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)


if __name__ == '__main__':
    # Begin testing
    unittest.main()
