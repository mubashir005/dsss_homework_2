
import unittest
from math_quiz import generate_problem_and_answer, random_integer, random_operator


class TestMathQuiz(unittest.TestCase):

    def test_generate_problem_and_answer(self):
        # Test if the generated problem and answer are valid
        problem, answer = generate_problem_and_answer()
        self.assertIsInstance(problem, str)
        self.assertIsInstance(answer, int)

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random operator generated is valid
        operator = random_operator()
        self.assertIn(operator, ['+', '-', '*'])


if __name__ == "__main__":
    unittest.main()

