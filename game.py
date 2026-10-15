"""A small, standard-library number guessing game for the terminal."""

import random


DIFFICULTIES = {
    "easy": (10, 5),
    "medium": (50, 7),
    "hard": (100, 8),
}


def play_round(input_fn=input, output_fn=print, rng=random):
    """Play one round; return True if the player guessed the number."""
    output_fn("Choose a difficulty: easy, medium, or hard.")
    while True:
        difficulty = input_fn("Difficulty: ").strip().lower()
        if difficulty in DIFFICULTIES:
            break
        output_fn("Please choose easy, medium, or hard.")

    upper_bound, max_attempts = DIFFICULTIES[difficulty]
    secret = rng.randint(1, upper_bound)
    output_fn(
        f"I'm thinking of a number from 1 to {upper_bound}. "
        f"You have {max_attempts} attempts."
    )

    attempts = 0
    while attempts < max_attempts:
        raw_guess = input_fn(f"Guess ({attempts + 1}/{max_attempts}): ").strip()
        try:
            guess = int(raw_guess)
        except ValueError:
            output_fn("Enter a whole number.")
            continue
        if not 1 <= guess <= upper_bound:
            output_fn(f"Choose a number from 1 to {upper_bound}.")
            continue

        attempts += 1
        if guess == secret:
            output_fn(f"Correct! You got it in {attempts} attempt(s).")
            return True
        if guess < secret:
            output_fn("Too low!")
        else:
            output_fn("Too high!")

    output_fn(f"Out of attempts! The number was {secret}.")
    return False


def main(input_fn=input, output_fn=print, rng=random):
    """Run rounds until the player declines to play again."""
    output_fn("Welcome to Number Guessing!")
    while True:
        play_round(input_fn, output_fn, rng)
        answer = input_fn("Play again? (y/n): ").strip().lower()
        if answer not in {"y", "yes"}:
            output_fn("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
