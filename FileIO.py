'''File I/O (Input/Output): list. open. with. sorted. CSV. dict. csv. PIL (savving data persistanly)'''

#name = input("What's your name?")

'''
file = open("names.txt", "a")          #NOTE: Create a file
file.write(f"{name}\n")                   # Write data into designated file
file.close()'''                           

'''
with open("names.txt", "a") as file:   #NOTE: Close the file automatically
    file.write(f"{name}\n")''' 

'''
with open("names.txt", "r") as file:
    lines = file.readlines()                 #NOTE: Readlines(), rstrip()
for line in lines:
    print(line.rstrip())'''

'''
with open("names.txt", "r") as file:
    for line in file:                          #NOTE: Read through each line in the file
        print(line.rstrip())'''

'''
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())                #NOTE: Append name to a list first
for name in sorted(names, reverse=True):           #NOTE: Edit the data (sort, lower, upper, title, etc)
    print(name)'''

'''NOTE: CSV(Comma-seperated Values) - convention to store multiple piece of info'''

'''
with open("students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")    #NOTE: Assign to name and house by splitting by ','
        print(f"{name} is in {house}")'''

'''
students =[]
with open("students.csv", "r") as file:
    for line in file:
        name, city = line.rstrip().split(',')
        student = {"name": name, "city": city}  #NOTE: create an empty list and assign key and value
        students.append(student)

def get_name(student):
    return student["name"]
def get_city(student):
    return student["city"]

for student in sorted(students, key=get_name, reverse=True):     #NOTE: or using key=lambda student: student["name"]
    print(f"{student['name']} is in {student['city']} ")'''

'''NOTE: Use of CSV module'''
import csv

students = []
'''
with open("students.csv") as file:
    reader = csv.reader(file)                     #NOTE: Common use of csv.reader (return a list)
    for name, home in reader:
        students.append({"name":name, "home":home})'''

'''
with open("students.csv") as file:
    reader = csv.DictReader(file)                    #NOTE: return a dict, treat csv file like excel, take the header(home, name)  
    for row in reader:
        students.append({"name":row["name"], "home":row["home"]})   #NOTE: or students.append(row) (row is already a dict)     
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']} ")'''

'''
name = input("What's your name? ")
home = input("Where's your home? ")
with open("students.csv", "a", newline='') as file:         #NOTE: newline= to remove extra line
    writer = csv.DictWriter(file, fieldnames=["name", "home"])       #NOTE: fieldnames=["x", "y"], header name
    writer.writerow({"name": name, "home":home})                            #NOTE: write row into csv file'''

'''PIL: Image processing library'''
import sys
from PIL import Image  #NOTE: Pillow's main purpose is to let Python read, edit, and save image file
images = []
for argv in sys.argv[1:]:
    image = Image.open(argv)  
    images.append(image)
images[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)