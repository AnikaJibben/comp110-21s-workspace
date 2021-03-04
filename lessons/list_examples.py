"""Some examples of list concepts."""

rolls: list[int] # declare a variable whose type is list of ints

rolls = [2, 3, 2, 6] # initialize w/list literal syntax

print(f"Length of rolls is {len(rolls)}")

from random import randint
rolls.append(randint(1, 6)) #lists append method adds to end of list
print(rolls)

rolls.pop() #lists pop method with no argument removes the last item of the list
rolls.pop(0)  # pops a speific index
print(rolls)

words: list[str] = list() #construct empty list using the list constructor
words.append("Hello")
print(words)
