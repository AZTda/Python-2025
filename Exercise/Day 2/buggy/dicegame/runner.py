from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        return sum(die.value for die in self.dice)

    @classmethod
    def run(cls):
        runner = cls()
        consecutive_wins = 0
        while True:
            print(f"\nRound {runner.round}\n")
            for die in runner.dice:
                die.roll()
                print(die.show())

            guess = input("\nWhat is your guess?: ")
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            correct_answer = runner.answer()

            if guess == correct_answer:
                print("Correct!\n")
                runner.wins += 1
                consecutive_wins += 1
            else:
                print(f"Wrong! The answer was: {correct_answer}\n")
                runner.loses += 1
                consecutive_wins = 0

            print(f"Wins: {runner.wins} | Losses: {runner.loses}\n")
            runner.round += 1

            if consecutive_wins == 6:
                print("You won 6 rounds in a row! Congratulations!")
                break

            prompt = input("Play again? [Y/n]: ").strip().lower()
            if prompt not in ['y', '']:
                i_just_throw_an_exception()