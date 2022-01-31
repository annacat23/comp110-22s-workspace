"""Ex 2 - One Shot Wordle and loops."""

__author__ = "730310234"

secret: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emoji_string: str = ""


while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

if len(guess) == len(secret):
    while i < len(guess):
        if (guess)[i] == (secret)[i]:
            emoji_string = emoji_string + GREEN_BOX
        else:
            in_secret: bool = False
            idx: int = 0
            while in_secret is not True and idx < len(secret):
                if (secret)[idx] == (guess)[i]:
                    in_secret = True
                else:
                    idx = idx + 1
            if in_secret is True:
                emoji_string = emoji_string + YELLOW_BOX
            else:
                emoji_string = emoji_string + WHITE_BOX      
        i = i + 1
    print(emoji_string)
    if guess == secret:
        print("Woo! You got it! ")
    else:
        print("Not quite. Play again soon! ")
