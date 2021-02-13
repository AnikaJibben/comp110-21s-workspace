"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730395244"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Fortune options.""" 
    random: int = randint(1, 100)
    if random < 25:
        return "Your weekend will be amazing!"
    else: 
        if random < 50:
            return "A large amount of money will come into your life shortly."
        else:
            if random < 75:
                return "2021 will be a great year!"
            else:
                return "Someone special is near."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
