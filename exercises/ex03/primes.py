"""EX03 - prime functions."""

__author__: str = "730395244"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(15))
    print(list_prime(10, 20))

def is_prime(x: int) -> bool:
    """Prime number evaluator.""" 
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0 :
        return False
    i: int = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i = i + 6
    return True


def list_prime(x: int, y: int) -> list[int]:
    """Making a list of all primes in range."""
    start: int = 10
    primes: list[int] = []
    while start < 20:
        if is_prime(start) == True:
           primes.append(start) 
        start += 1
    return primes


if __name__ == "__main__":
    main()