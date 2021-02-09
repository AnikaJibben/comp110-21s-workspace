"""An exercise in remainders and boolean logic."""

__author__ = "730395244"


# Begin your solution here...
number: int = int(input("Enter an int:"))

if  number % 2 == 0 and  number % 7 == 0:
    print("TARHEELS")
else:
    if number % 2 == 0:
        print("TAR")
    else:
        if number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")

  
