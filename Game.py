import os
import random

# Makes colors work in Windows terminals too
os.system("")

# ---------- Colors ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"


def paint(text, *styles):
    """Wrap text in color/style codes."""
    return "".join(styles) + str(text) + RESET


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    width = 34
    title = "GUESS  THE  NUMBER".center(width)
    print(paint("╔" + "═" * width + "╗", MAGENTA))
    print(paint("║", MAGENTA) + paint(title, BOLD, YELLOW) + paint("║", MAGENTA))
    print(paint("╚" + "═" * width + "╝", MAGENTA))


def hearts(remaining, total):
    return paint("♥ " * remaining, RED) + paint("♡ " * (total - remaining), DIM)


def hot_or_cold(guess, secret):
    diff = abs(guess - secret)
    if diff <= 5:
        return paint("🔥 Burning hot!", BOLD, RED)
    if diff <= 15:
        return paint("☀️  Warm", YELLOW)
    if diff <= 30:
        return paint("🌥  Cool", CYAN)
    return paint("❄️  Freezing cold", BLUE)


def ask_number(prompt, low, high):
    """Keep asking until the player enters a valid whole number."""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(paint(f"  Pick a number between {low} and {high}.", DIM))
        except ValueError:
            print(paint("  That's not a whole number, try again.", DIM))


def play_round():
    secret = random.randint(1, 100)
    max_attempts = 7
    low, high = 1, 100

    clear_screen()
    banner()
    print(f"\n  I'm thinking of a number between {paint(1, BOLD)} and {paint(100, BOLD)}.")

    for attempt in range(1, max_attempts + 1):
        remaining = max_attempts - attempt + 1
        print(paint("\n  ─────────────────────────────", DIM))
        print(f"  Lives: {hearts(remaining, max_attempts)}")
        print(f"  Range: {paint(low, BOLD, CYAN)} to {paint(high, BOLD, CYAN)}")

        guess = ask_number(paint(f"  Guess #{attempt} ▶ ", BOLD), 1, 100)

        if guess == secret:
            print(paint(f"\n  ★ You got it in {attempt} guess(es)! ★", BOLD, GREEN))
            return True

        if guess < secret:
            print(f"  {paint('Too low', BOLD, YELLOW)}  ⬆   {hot_or_cold(guess, secret)}")
            low = max(low, guess + 1)
        else:
            print(f"  {paint('Too high', BOLD, YELLOW)}  ⬇   {hot_or_cold(guess, secret)}")
            high = min(high, guess - 1)

    print(paint(f"\n  ✖ Out of guesses! The number was {secret}.", BOLD, RED))
    return False


def main():
    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        print(f"\n  Score: {paint(wins, BOLD, GREEN)} win(s) / {paint(rounds, BOLD)} round(s)")
        again = input(paint("  Play again? (y/n) ▶ ", BOLD)).strip().lower()
        if again != "y":
            print(paint("\n  Thanks for playing! 👋\n", MAGENTA))
            break


if __name__ == "__main__":
    main()
