import random


def get_valid_guess(low: int, high: int) -> int:
    """Prompt the user until they enter a valid integer within [low, high]."""
    while True:
        raw_input = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            guess = int(raw_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"Out of range! Please choose a number between {low} and {high}.")
            continue

        return guess


def evaluate_guess(secret: int, guess: int) -> tuple[bool, str]:
    """Compare the guess against the secret number and return (is_correct, hint)."""
    if guess < secret:
        return False, "Too low! Try a higher number."
    elif guess > secret:
        return False, "Too high! Try a lower number."
    else:
        return True, "Correct! You nailed it."


def play_round(low: int = 1, high: int = 100, max_attempts: int = 7) -> bool:
    """Play a single round and return True if the player wins, False otherwise."""
    secret = random.randint(low, high)
    print(f"\nI am thinking of a number between {low} and {high}. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        guess = get_valid_guess(low, high)
        is_correct, message = evaluate_guess(secret, guess)
        print(message)

        if is_correct:
            return True

    print(f"\nOut of attempts! The secret number was {secret}.")
    return False


def ask_replay() -> bool:
    """Ask the player whether they want another round."""
    while True:
        choice = input("\nPlay another round? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main() -> None:
    """Coordinate rounds and track session score."""
    wins = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        if play_round(low=1, high=100, max_attempts=7):
            wins += 1

        print(f"Score: {wins}/{rounds_played} rounds won.")

        if not ask_replay():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()