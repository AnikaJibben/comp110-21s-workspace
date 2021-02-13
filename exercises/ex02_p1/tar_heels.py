"""Tar Heels exercise redux as a structured program."""

__author__ = "730395244"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    number: int = int(input("Enter an int: "))
    print(tar_heels(number))


def tar_heels(number: int) -> str:
    """A fun function."""
    if number % 2 == 0 and number % 7 == 0:
        return("TAR HEELS")
    else:
        if number % 2 == 0:
            return("TAR")
        else:
            if number % 7 == 0:
                return("HEELS")
            else:
                return("CAROLINA")


if __name__ == "__main__":
    main()
