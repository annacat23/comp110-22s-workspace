"""Exercise 3: A structured wordle using function definitions."""

__author__: str = "730310234"


def contains_char(searched_word: str, single_char: str) -> bool:
    """Searches word for single character."""
    assert len(single_char) == 1
    i: int = 0
    in_secret: bool = False
    while in_secret is not True and i < len(searched_word):
        if single_char == (searched_word)[i]:
            in_secret = True
        else:
            i = i + 1
    if in_secret is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns appropriate emoji for guess."""
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    emoji_string: str = ""
    idx: int = 0
    assert len(guess) == len(secret)
    while idx < len(guess):
        if (guess)[idx] == (secret)[idx]:
            emoji_string += GREEN_BOX 
        else:  
            if contains_char(secret, (guess)[idx]) is True:
                emoji_string += YELLOW_BOX
            else:
                emoji_string += WHITE_BOX
        idx += 1
    return emoji_string


def input_guess(secret_length: int) -> str:
    """Ensures length of guess matches length of secret word."""
    guess: str = input(f"Enter a {secret_length} character word: ")
    while len(guess) != secret_length:
        guess = input(f"That wasn't {secret_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    won: bool = False
    while turn <= 6 and won is False:
        print(f"=== Turn {turn}/6 ===")
        guess = (input_guess(len(secret)))
        print(f"{emojified(guess, secret)}")
        turn += 1
        if guess == secret:
            won = True
            print(f"You won in {turn - 1}/6 turns! ")
    if won is False:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()