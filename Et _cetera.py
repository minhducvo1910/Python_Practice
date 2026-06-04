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
def meows(n: int):   #NOTE: Type hint: (: <data type>)
    for _ in range(n):
        print("meow")

number: int = input("Number: ")
meows(number)