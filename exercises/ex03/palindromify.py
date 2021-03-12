"""EX03 - palindromify function."""

__author__: str = "730395244"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    

def palindromify(x: str, y: bool) -> str:
    """Palindromify any word.""" 
    index = len(x)
    if y is True:
        while index > 0:   
            x += x[index - 1]
            index = index - 1
    if y is False:
        index = len(x) - 1
        while index > 0:
            x += x[index - 1]
            index = index - 1
    return x
    

if __name__ == "__main__":
    main()