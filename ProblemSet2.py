#Loop problem set 2:
#1. Camel Case: camel.py
'''
user_input = input("Camel case: ")
snake_case = ""
for char in user_input:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print(snake_case)
'''
#2. Coke Machine: Coke Machine.py (Suppose that a machine sells bottles of Coca-Cola (Coke) 
# for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
'''amount_due= 50
while amount_due >0:       #For while to keep running until the amount due is 0 or less
    print(f"Amount due: {amount_due} cents")
    coin = int(input("Insert coin: "))   
    if coin in [25, 10, 5]:
        amount_due -= coin
    else:
        print("Invalid coin.")
change = -amount_due
print(f"Change owed: {change} cents")
'''    
#3. Just setting up my X: setup.py
'''while True:
    text = input("User input (Type \"Quit\" to exit): ").lower().strip()

    if text == "quit":
        print("Good bye!")
        break

    new_text = ""
    for c in text:
        if c in ["a", "u", "o", "e", "i"]:
            continue
        else:
            new_text += c
    print(f"Output: {new_text}")'''
#4: Vanity Plates: plates.py
'''
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    return (check_for_length(s) and
            check_for_numbers(s) and
            check_puntuation(s) and
            check_for_first_two(s) and
            check_for_first_number(s) and
            check_numbers_at_end(s)
            )
    

def check_for_length(s):
    return 2 <= len(s) <= 6

    
def check_for_numbers(s):
    if s.isdigit():
        return False
    else: 
        return True
    
def check_puntuation(s):
    return s.isalnum()

def check_for_first_two(s):
    return len(s) >=2 and s[0:2].isalpha()

def check_for_first_number(s):
    for c in s:
        if c.isdigit():       #Looping through input and only take digit.
            return c != "0"   #Looping through input, if digit is found, the "return" stop the loop and check the digit
        return True           #Automatically return True if no digit is found, or if the first digit is not "0"
def check_numbers_at_end(s):
    reached_number = False    #No digit found yet
    for c in s:
        if c.isdigit():       
            reached_number = True              # we hit a number, FIRST CONDITION DONE
        if reached_number and c.isalpha():     
            return False                       # letter after number → invalid
    return True

main()'''
#5: Nutrition Facts: nutrition.py
fruits = {"apple": 130, "banana": 110,
          "avocado": 50, "cantaloupe": 50,
          "grapefruit": 60, "grapes": 90,
          "honeydew melon": 50, "kiwifruit": 90,
          "lemon": 15, "lime": 20, "nectarine": 60,
          "orange": 80, "peach": 60, "pear": 100,
          "pineapple": 50, "plums": 70, "strawberries": 50,
          "sweet cherries": 100, "tangerine": 50, "watermelon": 80
          }
while True:
    user_input = input("Item (Type \"quit\" to exit): ").lower().strip()
    if user_input == "quit":
        print("Good bye!")
        break
    if user_input in fruits:
        print(f"calories: {fruits[user_input]}")
    else:
        print("Sorry, we don't have that item. Try again.")