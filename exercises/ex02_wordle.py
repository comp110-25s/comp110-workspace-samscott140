"""Wordle Game"""

__author__: str = "730650345"


def contains_char(word: str, letter: str) -> bool:
    assert len(letter) == 1, f"len('{letter}') is not 1"
    """Tests to see if a given letter is in a word"""
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret), "Guess must be same length as secret"
    """Returns a graphic of the guess results"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    i: int = 0
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                result = result + GREEN_BOX
            else:
                result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        i = i + 1
    return result


def input_guess(expected_length: int) -> str:
    """Allows the user to input a guess until they match the required length"""
    word: str = input(f"Enter a {expected_length} character word:")
    while len(word) != expected_length:
        word = input(f"That wasn't {expected_length} chars! Try again:")
    return word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        attempt: str = input_guess(len(secret))
        print(emojified(attempt, secret))
        if attempt == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        if attempt != secret and turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


if __name__ == "__main__":
    main(secret="codes")
