"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395244"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print ("Your fortune cookie says...")

random: int = randint(1,100)

if random < 25:
    print("You will have the best day of your life this weekend.")
else:
    if random < 50:
        print("You will work your dream job!")
    else: 
        if random < 75:
            print("Get ready to meet your soulmate very soon.")
        else:
            print("A large amount of money will come into your life soon.")

print("Now, go spread positive vibes!")