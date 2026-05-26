'''
librabry practice: "IMPORT" and "FROM" are used to import modules in Python.
'''
from gettext import install
import random
import math
import statistics
import sys

import pip
 
test = random.choice([1, 2, 3, 4, 5])

cards = ["Jack", "Queen", "King", "Ace"]
random.seed(0)
random.sample(cards, k=2)
num = random.randint(1, 10)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
#Checked for conditions

if len(sys.argv) < 2:
    #sys.exit("No name provided.")
#print(f"Hello, {sys.argv[1]}!")
#Print name provided as an argument
    for arg in sys.argv[1:]:

        '''Install packages(libraries) using pip in the command line:
        pip install package_name (e.g., pip install numpy)
        py -m pip install package_name (e.g., py -m pip install numpy)'''


import cowsay
#   cowsay.cow("Hello, " + sys.argv[1] + "!")

'''APIs (Application Programming Interfaces) are sets of rules and 
protocols that allow different software applications to communicate
with each other. They define how requests and responses should be 
structured, enabling developers to access and use functionalities
provided by other software or services without needing to understand
 their internal workings. APIs are commonly used for web services,
   allowing applications to interact with external data or services over the internet.'''

'''Request Libraries: Requests is a popular Python library for making HTTP requests.'''

'''JSON Libraries: JSON (JavaScript Object Notation) is a lightweight data-interchange format.
Python's built-in json library allows you to parse JSON data and convert it into Python objects'''

import requests
import json

'''if len(sys.argv) != 2:
    sys.exit("No name provided.") 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
store = response.json()
for result in store['results']:
    print(result['trackName'])'''


'''from saying import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])'''


'''Style of Python coding: PEP 8 (pycodestyle, pip install pycodestyle)
In terminal: black filename.py (e.g., black ProblemSet3.py) to format code'''

'''APIs call: '''
def main():
    artist = input("Enter an artist: ")
    artworks = get_artworks(artist, 5)
    for artwork in artworks:
        print(artwork['title'])

def get_artworks(query, limit):
    try:
        collection = requests.get("https://api.artic.edu/api/v1/artworks/search",
                                  {"q": query, "limit": limit})
        collection.raise_for_status()  # Check if the request was successful
        data = collection.json()
        return data['data']     # Return the list of artworks from the API response
    except requests.HTTPError:
        print("HTTP error occurred.")

if __name__ == "__main__":
    main()
    
'''Create package with multiple file in one folder, and import functions from one file
   to another using "from" and "import" statements. 
   For example, create a package named "saying" with two files: "hello.py" and "goodbye.py".
   Put in 1 folder, make sure to have an __init__.py file in the folder to make it a package'''

