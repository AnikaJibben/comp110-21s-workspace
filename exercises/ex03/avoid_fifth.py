"""EX03 - avoid_fifth function."""

__author__: str = "730395244"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello there"))
    print(avoid_fifth("Even this sentence has many of the wrong letter, in different sizes."))


def avoid_fifth(x: str) -> str:
    """Avoid the Letter E."""
    i: int = 0
    while i < len(x):
        if x[i] != "e" or "E":
            x = x.translate({ord(i): None for i in 'eE'})
        i += 1
    return (x)
    
   
if __name__ == "__main__":
    main()