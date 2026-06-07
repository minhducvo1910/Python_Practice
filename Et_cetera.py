'''ET CETERA: '''

'''Set: none duplicate data type'''
students = [
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]
houses = set()   #NOTE: Create an empty set
for student in students:
    houses.add(student["house"])
for house in sorted(houses):
    pass

'''Global variable: '''
#balance = 0   #NOTE: global variable (cannot write to it) (or access using global <variable name>)
class Account:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n 
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance", account.balance)

if __name__ == "__main__":
    pass

'''Constant: '''

#MEOWS = 3       #NOTE: Captialize for indicating constant
class Cat:
    MEOWS = 3
    def meow(self):
        for _ in range(self.MEOWS):
            print("meow")
cat = Cat()


'''TYPE HINTs: mypy'''
import mypy
def meows(n: int) -> str:   #NOTE: Type hint: (: <data type>), -> None : show that the function return
    return "meow\n" * n

#number: int = int(input("Number: "))
#meo: str = meows(number)


'''Argparse library: '''
import argparse
parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1, help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    pass

'''Unpacking: '''
def total(galleons, sickles, knuts):
    return (galleons * 17+ sickles) * 29 + knuts

coins = [100, 50, 25]

#print(total(*coins), "knuts")   #NOTE: * unpacked list into 3 different variable, ** for dictionary (e.g **coins)

'''Visual Indicator: *arg, **kwargs'''
def f(*args, **kwargs):         #NOTE: pass any number of arguments
    print("Positional", args) 
#f(...)


'''Map, list comprehension '''
def yell(*phrase): 
    #uppercased = map(str.upper, phrase)          #NOTE: map() function
    uppercased = [word.upper() for word in phrase]
    '''print(*uppercased)'''

yell("Yay", "Woo", "Hurray")

gryffindors_1 = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors_1):
    '''print(gryffindor)'''

'''Filter: '''
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    '''print(gryffindor["name"])'''
        
'''Dictionary comprehension:'''

hoc_sinhs = ["Duc", "Chau", "Thuy"]

pct = {hoc_sinh:"phanchautrinh" for hoc_sinh in hoc_sinhs}
'''print(pct)'''

'''Enumerate(iterable, start=0)'''
for i, hoc_sinh in enumerate(hoc_sinhs):   #NOTE: enumerate take the current index and return the value respectively
    '''print(i+1, hoc_sinh)'''


'''Generators: yield'''

n = int(input("n = ?:"))
def sheep(n):
    for i in range(n):
        yield "sheep" * i  #NOTE: yield print 1 row at a time, doesnt hang

'''Recursion: (base case)'''

def factorial(n):
    if n == 1:   #NOTE: base case
        return 1 
    return n * factorial(n-1)   #NOTE: recursive call 
result = factorial(3)