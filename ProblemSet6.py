'''1:in a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines
If the user does not specify exactly one command-line argument, or if the specified file’s
name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.'''
import sys
import os

def main():
    clean_data()

def count_code():
    #Check argument count
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument!")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    #Check for file validiation
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a python file!")
    if not os.path.exists(filename):
        sys.exit("File doesn't exit")

    #Count line
    count = 0
    with open(filename, "r") as f:
        for line in f:
            if line.lstrip().startswith("#"):
                continue
            if line.strip() == "":
                continue
            count += 1
    
    print(count)

'''2: In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
Format the table using the library’s grid format.'''
from tabulate import tabulate
import csv
def get_pizza():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument!")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    #Check for file validiation
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a csv file!")
    if not os.path.exists(filename):
        sys.exit("File doesn't exit")
    #Format the table
    rows = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)                                 #Rows is not a list of dictionaries
    print(tabulate(rows, headers="keys", tablefmt="grid"))   #Use the tabulate library to format

'''3: In a file called scourgify.py, implement a program that:
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name.
 Assume that each student will have both a first name and last name.'''

def clean_data():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argument!")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    #Check for file validiation
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a csv file!")
    if not os.path.exists(filename):
        sys.exit("File doesn't exit")

    #Convert to a new csv file (first, last, house)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r") as before, open(output_file, "w", newline='') as after:  #Open 1 file to read, 1 file to write
        reader = csv.DictReader(before)                                                 #Read the file
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])  #Creates a CSV writer that knows how to write dictionaries into your output file
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({
                "first": first, "last":last, "house": row["house"] 
            }) #Write the dictionary into the csv file in order of the keys.


main()
    


