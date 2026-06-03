'''1: Seasons of love: 
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD 
format and then sings prints how old they are in minutes (using English words instead of numerals).
Assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date
Assume that the current time is also midnight. In other words, even if the user runs the program at noon,
Assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date'''

from datetime import date
import sys
import inflect
import re

p = inflect.engine() #NOTE: Create an inflect engine to convert number to words

def main():
    birthdate = get_input()
    age_in_minutes = calculate_age_in_minutes(birthdate)
    print(f"{p.number_to_words(age_in_minutes, andword='').capitalize()} minutes") #NOTE: andword='' remove "and" in the output


#Get user input, validate it, and return a date object
def get_input():
    input_date = input("Date of Birth: ").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", input_date):
        sys.exit("Invalid date")

    try:
        year, month, day = input_date.split("-")
        birthdate =date(int(year), int(month), int(day))   #NOTE: create a date obj (datetime validate the date)
    except ValueError:
        sys.exit("Invalid date")

    if birthdate > date.today():
        sys.exit("Invalid date")

    return birthdate

def calculate_age_in_minutes(birthdate):
    today = date.today()
    timedelta = today - birthdate
    minutes = timedelta.days * 24 * 60
    return minutes

'''2:Cookie Jar:  In a file called jar.py, implement a class called Jar with these methods:
__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit
in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with 𝑛 🍪, where 𝑛 is the number of cookies in the cookie jar.
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

Deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though,
deposit should instead raise a ValueError.

Withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar,
though, withdraw should instead raise a ValueError.

Capacity should return the cookie jar’s capacity.

Size should return the number of cookies actually in the cookie jar, initially 0'''

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._cookies = 0  #NOTE: Use _cookies to store the cookie in the jar

    def __str__(self):
        return "🍪" * self._cookies #Return the amount of cookies
    
    def deposit(self, n):
        if self._capacity - self._cookies < n:
            raise ValueError("Too many cookies")
        elif self._capacity - self._cookies == 0:
            raise ValueError("Jar is full")
        else:
            self._cookies += n
    
    def withdraw(self, n):
        if self._cookies < n:
            raise ValueError("Not enough cookies")
        else:
            self._cookies -= n
    @property       
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._cookies

'''3: '''
if __name__ == "__main__":
    main()
    