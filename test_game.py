import unittest

from game import DIFFICULTIES, main, play_round


class FixedRandom:
    def __init__(self, number):
        self.number = number

    def randint(self, lower, upper):
        assert lower <= self.number <= upper
        return self.number


class GameTests(unittest.TestCase):
    def run_round(self, answers, number):
        prompts = iter(answers)
        messages = []
        result = play_round(lambda _prompt: next(prompts), messages.append, FixedRandom(number))
        return result, messages

    def test_difficulty_settings(self):
        self.assertEqual(DIFFICULTIES["easy"], (10, 5))
        self.assertEqual(DIFFICULTIES["medium"], (50, 7))
        self.assertEqual(DIFFICULTIES["hard"], (100, 8))

    def test_correct_guess_reports_attempt_count(self):
        won, messages = self.run_round(["easy", "4", "7"], 7)
        self.assertTrue(won)
        self.assertTrue(any("in 2 attempt(s)" in message for message in messages))

    def test_hints_and_attempt_limit(self):
        won, messages = self.run_round(["easy", "3", "9", "1", "2", "4"], 5)
        self.assertFalse(won)
        self.assertIn("Too low!", messages)
        self.assertIn("Too high!", messages)
        self.assertTrue(any("Out of attempts! The number was 5." == message for message in messages))

    def test_invalid_input_does_not_use_an_attempt(self):
        won, messages = self.run_round(["easy", "nope", "0", "5"], 5)
        self.assertTrue(won)
        self.assertIn("Enter a whole number.", messages)
        self.assertIn("Choose a number from 1 to 10.", messages)
        self.assertTrue(any("in 1 attempt(s)" in message for message in messages))

    def test_invalid_difficulty_is_reprompted(self):
        won, messages = self.run_round(["extreme", "medium", "12"], 12)
        self.assertTrue(won)
        self.assertIn("Please choose easy, medium, or hard.", messages)

    def test_play_again_loop(self):
        answers = iter(["easy", "2", "y", "hard", "2", "n"])
        messages = []
        main(lambda _prompt: next(answers), messages.append, FixedRandom(2))
        self.assertEqual(sum(message.startswith("I'm thinking of") for message in messages), 2)
        self.assertIn("Thanks for playing!", messages)


if __name__ == "__main__":
    unittest.main()
