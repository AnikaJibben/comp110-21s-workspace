"""Choose Your Own Adventure Project."""

__author__ = "730395244"

from random import randint 


player: str = "player"
points: int = 0
heads: int = 1
tails: int = 2
random: str = randint(1, 2)


def main() -> None:
       """The entry point of the program, when ran as a module."""
       COIN_EMOJI: str = "\U0001FA99"
       greet()
       global points
       print(f"{player}, let's flip the coin {COIN_EMOJI} !")
       while input("Choose one of the following paths: heads, tails, or end game- ") != "end game":
              answer_1: str = input("heads, tails, end game")
              if answer_1 == "heads":
                     direction_1()
              else:
                     if answer_1 == "tails":
                            direction_2(points)
       game_over()
       
                  
def greet() -> None:
       """Welcome player to the game"""
       print("Welcome to The Coin Flip!")
       print("Through this game you will make a guess as to if the coin flips to heads, or tails!")
       print("Every right answer, you gain points, every wrong you lose points.")
       print("Let's get started!")
       global player 
       player = str(input("Player name: "))
       

def direction_1() -> None:
       """Heads."""
       global points
       while input(f"{player} are you sure you want to pick Heads? yes/no- ") == "yes":
              if random == 1:
                     points += 1
              else:
                     random == 2 
                     points-= 1
       print(f"Total Points: {points}")
       

def direction_2(points: int) -> int:
       """Tails."""
       while input(f"{player} are you sure you want to pick Tails? yes/no- ") == "yes":
              if random == 2:
                     points += 1
              else:
                     random == 1 
                     points-= 1
       return print(f"Total Points: {points}")


def game_over() -> None:
       global points
       print(f"Total points: {points}")
       print("Good Game! Thanks for playing!")


if __name__ == "__main__":
  main()