"""A vaccination calculator."""

__author__ = "730395244"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population:"))
doses_admin: int = int(input("Doeses Administered:"))
doses_day: int = int(input("Doses given per day:"))
target_percent: int = int(input("Target percent vaccinated:"))

today: datetime = datetime.today()
days: float = (target_percent / 100) * population - doses_admin / doses_day
date_1: timedelta = timedelta(days)
future: datetime = today + date_1

population: str = str(population)
doses_admin: str = str(doses_admin)
doses_day: str = str(doses_day)
target_percent: str = str(target_percent)
days: str = str(days)

print("We will reach " + target_percent + "% vaccination in " + days + "days, which falls on " + future.strftime("%B %d, %Y"))