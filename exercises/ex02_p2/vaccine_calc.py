"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730395244"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    x: str = days_to_target(population, doses, doses_per_day, target)
    y: str = future_date(x)
    print("We will reach " + target + "% vaccination in " + x + " days, which falls on " + y )


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Number of days to the target percent."""
    days: float = ((target / 100) * (2 * population) - doses) / doses_per_day
    days: round(days)
    return days


def future_date(x: int) -> str:
    """Future sate output."""
    today: datetime = datetime.today()
    date_1: timedelta = timedelta(x)
    future: datetime = today + date_1
    return future.strftime("%B %d, %Y")

if __name__ == "__main__":
    main()
