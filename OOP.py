''' Object-Oriented Programming (OOP):'''

'''Class: A blue print fro creating object.'''
import random
import sys
class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __add__(self, other):  #NOTE: overide operator + for class (__sub__, __mul__,...)
        '''galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        return Vault(galleons, sickles)'''   #NOTE: In main() we can do: vault1 + vault2 to add two vault together


class Student(Wizard):              #NOTE: Class inheritance (Student is a subclass of Wizard)
    def __init__(self, name,house):   #Instance method        #NOTE: Methods are function in class  
        super().__init__(name)
        self.house = house

    def __str__(self):                                   #NOTE: __str__ method return a string repres of the obj
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House:")
        try:
            return cls(name, house)
        except ValueError as e:
            print(e)
            return None 


    '''@property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    #Getter (get value)
    @property
    def house(self):            #NOTE: @properties of obj
        return self._house
    
    #Setter (set value)
    @house.setter              #NOTE: @house.setter is a decorater
    def house(self, house):
        self._house = house'''
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)         #NOTE:  Call the parent class's __init__ method
        self.subject = subject
    

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


def main():
    student = Student.get()
    #Hat.sort("MINH")
    professor = Professor("Dumbledore", "Transfiguration")
    wizard = Wizard("Merlin")
    #print(student)          #NOTE: call __str__ automatically

    mushroom_skewer = Food(ingredients = ["Mushroom", "Hearty Mushroom"])
    print(f"This mushroom heal: {mushroom_skewer.hearts} hearts")


'''def get_student():
    #student = Student()                        #NOTE: create an object from class Student, obj is a instantation(instance) of class
    #student.name = input("Name: ").strip()     #NOTE: add attribute to obj (instance variable)
    #student.house = input("House: ").strip()
    #return student

    name = input("Name: ")
    house = input("House: ")
    try: 
        return Student(name, house)             #NOTE: constructor call (call __init__ method in class)
    except ValueError as e:
        print(e)
        return None'''

    #return [name, house]   #NOTE: Use [] to return list(changable)   #NOTE: Return multiple value as tuple (immutable), we can unpack it in main() function
    #return {"name": name, "house": house}
class Food:
    base_heart = 1 #NOTE: class varible (shared by all instance of class)

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_heart(ingredients)

    @classmethod
    def calculate_heart(cls, ingredients):
        hearts = cls.base_heart
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])   #Create a new instance of food with empty ingredients
        food.hearts = hearts         #Set the heart manually
        return food                  #Return the food instance
    
if __name__ == "__main__":
    main()

