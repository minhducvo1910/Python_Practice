'''REGULAR EXPRESSION (Regexes)'''
'''Library for regular expression: re (e.g re.search(pattern, string, flags=0))'''
import re
def main():
    capture_group()

def validate_code():
    email = input("What's your email? ").strip()
    if re.search(r"^\w+@(\w\.)?[a-zA-Z0-9_]+\.(edu|com|net|gov|org)$", email, re.IGNORECASE):       #[^@] any character except of @, \w: word character = [a-zA-Z0-9_]
        print("Valid")
    else:
        print("Invalid")

def validate_name():
    name = input("What's your name? ").strip()
    if matches := re.search(r"(^.)+, ?(.+)$", name):     #() to capture data| use := to use if and assign a value
        last = matches.group(1)                          #Group() to get the group () in re.search
        first = matches.group(2)
        name = f"{first} {last}"
    print(name)

def twitter():
    url = input("What's your URl? ").strip()
    # username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)            #re.sub(pattern, repl, string, count=0, flags=0)
    matches = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE)
    if matches:
        print(f"Username: {matches.group(1)}")

'''NOTE: we can do code: pattern r"^#[a-z..]{6}$"   {6} mean 6 character in the set after #'''
    
'''NOTE: Capture group'''
def capture_group():
    locations = {"+1":"United Stated", "+62":"Indonesia", "+505":"Nicaragua"}
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}" #Inside () use ?P<name> to name it
    number = input("Number: ").strip()
    match = re.search(pattern, number)
    if match:
        country_code = match.group(1) #match.group("country_code")
        print(f"Phone number is from {locations[country_code]}")
    else:
        print("Invalid")
main()
  