'''1: Because emoji aren’t quite as easy to type as text, at least on laptops and desktops,
some programs support “codes,” whereby you can type, for instance, :thumbs_up:,
which will be automatically converted to 👍. Some programs additionally support aliases,
whereby you can more succinctly type, for instance, :thumbsup:,
which will also be automatically converted to 👍.

See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias
for a list of codes with aliases.

In a file called emojize.py, implement a program that prompts the user for a str in English
and then outputs the “emojized” version of that str, converting any codes (or aliases)
therein to their corresponding emoji.'''

import requests
import json
import emoji


'''def main():
    text = input("Enter the text to emojize: ")
    emojized_text = emoji.emojize(f":{text}:", language='alias')
    print(emojized_text)

main()'''


'''2:In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font,
in which case the first of the two should be -f or --font,
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font
or the second is not the name of a font, the program should exit via sys.exit
with an error message.'''

import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
valid_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(valid_fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ("-f", "--font") and sys.argv[2] in valid_fonts:
        font = sys.argv[2]
    else: 
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

figlet.setFont(font=font)
#text = input("Input: ")
#print(figlet.renderText(text))

'''3: In a file called adieu.py, implement a program that prompts the user for names
, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and,
and 𝑛 names with 𝑛 −1 commas and one and, as in the below:'''

import inflect

p = inflect.engine()
names = []
'''while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
print(f"Adieu, adieu, to {p.join(names)}")'''

'''4: Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.'''

'''while True:
    try:
        level = int(input("Enter a level: "))
        if level > 0:
            break
        else:
            print("Please enter a positive number")
    except ValueError:
            print("Enter a number")

random_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess the number:"))
        if guess < random_num:
            print("Too small!")
        elif guess > random_num:
            print("Too large!")
        elif guess == random_num:
            print("Just right!")
            break
    except ValueError:
        print("Enter a number")'''

'''5: Professor Calculator:'''

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempt = 0
        while attempt < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    attempt +=1
            except ValueError:
                attempt += 1
                print("EEE")
        if attempt == 3:
            print(f"{x} + {y} = {answer}")
    print(f"Your score: {score}")      
                  
def get_level():
    while True:
        try:
            level = int(input("Enter a level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            print("Please enter a number")
            
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

main()


