"""Examples of lists and loop algorithm."""

def sum_algo(xs: list[int]) -> int:
    """Summnation of input lost is returned."""
    # 1. initialize total and index i to 0
    total: int = 0
    i: int = 0
    # 2. while index i is valid, meaning i < len(xs)
    while i < len(xs):
        #   2. True) take xs[i] and add to total
        total += xs[i]
        #   2. True) increase i by 1, moving it to the next index
        i += 1

    # 2.False) result is stroed in total variable
    return total


# example usage of the sum _algo function
odds: list[int] = [1, 3, 5, 7]
odds_sum: int = sum_algo(odds)
print(odds_sum)

# from diagram video
single: list[int] = [110]
many: list[int] = [1, 3, 5]
print(sum_algo(single))
print(sum_algo(many))