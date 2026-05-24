'''
###Else if statements

def main():
    time = input("Time: ").strip()
    time = convert(time)
    print(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(t):
    if "a.m" in t or "p.m" in t:
        period = "p.m" if "p.m" in t else "a.m"
        t = t.replace(period, '').strip()
        hour, minute = t.split(":")
        hour, minute = int(hour), int(minute)
        if period == "a.m":
            if hour == 12:
                hour = 0
        else: 
            if hour != 12:
                hour += 12
    else: 
        hour, minute = t.split(":")
        hour, minute = int(hour), int(minute)
    return hour + minute /60


if __name__ == "__main__":
   main()

###For and while loops
def main():
    num = get_number()
    Meo(num)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            print("Positive number entered.")
            return n
        
def Meo(n):
    for _ in range(n):
        print("Meow!")
main()

student = {"Minh": 90, 
           "John": 85,   #Dictionary {key: value pairs}, for loops can be used to iterate through the keys or values of a dictionary
           "Sarah": 92
}

students = [
    {"name": "Minh", "grade": 90, "group": "A"},
    {"name": "John", "grade": 85, "group": "B"},
    {"name": "Sarah", "grade": 92, "group": None}
]
for student in students:
    print(student)

def main():
    get_square(3)                            

def get_square(size):          
    for i in range(size):                  #Or: for i in range(size):
        print("#" * size)                           #for j in range(size):
main()                                                    #print("#", end="")
                                                  #print()

lower_case_word = [word.lower() for word in words]
# ["apple", "banana", "apple", "cherry", "banana"]                             #List and dictionary comprehensions are a concise way to create lists and dictionaries based on existing iterables. In this example, we are creating a new list called lower_case_word by converting each word in the original list words to lowercase using a list comprehension.

counts = {word: lower_case_word.count(word) for word in lower_case_word}

def main():                          
    x = get_int("what is Y?")
    y = get_int("what is X?")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))              #Exception ( Try - excetp - else ) handling is a way to handle errors that may occur during the execution of a program. In this example, we are using a while loop to continuously prompt the user for input until they provide a valid integer. The try block attempts to convert the input to an integer, and if it fails (e.g., if the user enters a non-integer value), it raises a ValueError, which is caught by the except block. The except block simply passes, allowing the loop to continue and prompt the user again until a valid integer is entered.
        except ValueError:
            pass
main() '''

def main():
    height = int(input("Height: "))
    pryramid(height)
def pryramid(h):
    for i in range(h):
        print((" " * (h - i - 1) + "#" * (i + 2)) * 2)
main()
