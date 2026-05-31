'''1: In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str
 and then returns True or False, respectively, if that input is a valid IPv4 address or not.'''
import re
import sys
def main():
    '''try:
        time = input("Hours: ").strip()
        print(convert(time))
    except ValueError as e:
        print(f"{e}")'''
    response()


def validate_number():
    ip = input("IPv4 address: ").strip()
    pattern =  r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    if match:
        numbers = match.groups()
        #Check for invalid cases:
        for number in numbers:
            if int(number) > 255:
                print("False")
                return
            if len(number) > 1 and number.startswith("0"):
                print("False")
                return
        print("True")
    else:
        print("False") 

'''2: In a file called watch.py, implement a function called parse that expects a str of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter,
shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below.
Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL.
If the input does not contain any such URL at all, return None.'''

def parse():
    html = input("HTML: ").strip()
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    match = re.search(pattern, html)
    if match: 
        print(f"https://youtu.be/{match.group(1)}")
    else:
        return None

'''3:Working 9-5: In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.'''

def convert(s):
    #Match for pattern
    pattern = r"([0-9]{1,2})\:?([0-9]{2})? (AM|PM) to ([0-9]{1,2})\:?([0-9]{2})? (AM|PM)"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Wrong format")
    
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    hour1, minute1, hour2, minute2 = (
        int(hour1), int(minute1) if minute1 else 0, int(hour2), int(minute2)  if minute2 else 0
    )  #NOTE: Minute can return None from match.groups()
    start = to_24(hour1, minute1 if minute1 else 0, period1)
    end = to_24(hour2, minute2 if minute2 else 0, period2)

    return f"{start[0]:02}:{start[1]:02} to {end[0]:02}:{end[1]:02}"

def to_24(hour, minute, period):
    #Check for value input
    if not (1 <= hour <= 12) or not (0 <= minute <= 59):
        raise ValueError("Invalid time")
    #Convert time
    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12
    return hour, minute #Return a tuple to access data
    
'''4: In a file called um.py, implement a function called count that expects a line of text as input as a str and returns,
as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself,
not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1.
Given text like yummy, though, the function should return 0.'''

r'''NOTE: Note that (\ b) is “defined as the boundary between a \ w and a \ W character (or vice versa),
 or between \ w at the beginning/end of the string'''

def count():
    text = input("Input: ").strip()
    pattern = r"\bum\b" #NOTE: \ B is the opposite of \ b 
    matchs = re.findall(pattern, text, re.IGNORECASE)     #NOTE: re.findall find all the match and return a list (re.search find the first match)
    count = len(matchs)
    print(f"Count is: {count}")

'''5: In a file called response.py, using either validator-collection or validators from PyPI,
implement a program that prompts the user for an email address via input and then prints Valid or Invalid,
respectively, if the input is a syntatically valid email address. You may not use re.
And do not validate whether the email address’s domain name actually exists'''

from validator_collection import is_email  #NOTE: Check the documentation for more function
def response():
    user_email = input("Email: ").strip()
    if is_email(user_email, allow_empty=False):
        print("Valid")
    else: 
        print("Invalid")

main()