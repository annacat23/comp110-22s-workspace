"""An example of love function definitions."""

name: str = input("What is your name? ")


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


print(love(name))


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        # Concatenation
        love_note += f"{love(to)}\n"
        i += 1
    return love_note