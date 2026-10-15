# Number Guessing CLI Game

A small Python 3 terminal game. Choose easy, medium, or hard, then guess the
secret number before you run out of attempts. The game gives higher/lower hints,
counts valid guesses, and offers another round when you finish.

This project was built with AI coding assistance (an AI coding agent).

## Run

Requires Python 3. From this directory, run:

```sh
python3 game.py
```

## Tests

```sh
python -m unittest
```

## Example session

```text
Welcome to Number Guessing!
Choose a difficulty: easy, medium, or hard.
Difficulty: easy
I'm thinking of a number from 1 to 10. You have 5 attempts.
Guess (1/5): 4
Too low!
Guess (2/5): 7
Correct! You got it in 2 attempt(s).
Play again? (y/n): n
Thanks for playing!
```

Difficulty settings:

| Level | Range | Attempts |
| --- | ---: | ---: |
| Easy | 1–10 | 5 |
| Medium | 1–50 | 7 |
| Hard | 1–100 | 8 |
