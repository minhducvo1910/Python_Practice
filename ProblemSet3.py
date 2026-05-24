'''1: Fuel Gauge: implement a program that prompts the user for a fraction, 
    formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, 
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
    If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
    And if 99% or more remains, output F instead to indicate that the tank is essentially full.'''

'''def main():
    while True:
        try:
            fraction = input("Enter fraction (X/Y): ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)
    fuel_gauge(percentage)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError("Invalid input. Please enter a fraction in the format X/Y.")
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be 0")
    elif x < 0 or y < 0:
        raise ValueError("Numerator and denominator must be greater than 0")
    elif x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    else: 
        return round( x / y * 100)

def fuel_gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >=99:
        print("F")
    else:
        print(percentage, "%")

main()'''

'''2: In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d 
(which is a common way of ending one’s input to a program).
 After each inputted item, display the total cost of all items inputted thus far,
   prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively.
     Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased''' 
    

'''def main():
    menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
             }    
    get_total(menu)                    
    
def get_total(menu):
    total = 0
    while True:
        try:
            order = input("Item:").title()
            if order in menu:
                total += menu[order]
                print(f"Total: ${total:.2f}")
            else:
                print("Item not found. Please try again.")
        except EOFError:
            break
    return total

main()'''



'''3: In a file called grocery.py, implement a program that prompts the user for items, one per line,
 until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively.'''

'''def main():
    items = {}
    while True:
        try:
            item = input("Items (e.g X item):").strip()
            x, y = item.split(" ", 1)
            x, y = int(x), y.upper()
            if y in items:
                items[y] += x
            else: 
                items[y] = x
        except EOFError:
            break
        except ValueError:
            print("Invalid input. Please enter in the format 'X item'.")
    for y in sorted(items):
        print(f"{items[y]} {y}") 
main()'''


'''4:'''

def main():
    months = [  "January","February","March","April","May","June","July",
                "August","September","October","November","December"]
    while True:
        try:
            date = input("Date (MM/DD/YY or Month Day, Year): ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
            else:
                month, day, year = date.replace(",", "").split()
                if month not in months:
                    raise ValueError("Invalid month. Please enter a valid month name.")
                else:
                    month = months.index(month.title()) + 1
                    day, year = int(day), int(year)
            if month < 1 or month > 12:
                raise ValueError("Invalid month. Please enter a month between 1 and 12.")
            if day < 1 or day > 31:
                raise ValueError("Invalid day. Please enter a day between 1 and 31.")
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError as e:
            print(e)
        except EOFError:
            break
main()
    
    


