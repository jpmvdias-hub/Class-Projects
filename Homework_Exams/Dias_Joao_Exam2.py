#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_Joao_Exam2.py
#Date: November 18, 2025

#Short Description: This program will calculate the area/volume of selected shapes


#Import Math Functions
import math

#Description Output
def description():
    print("This program is a Geometric Calculator for different shapes.")

#Menu Printout
def menu():
    print()
    print("Choose one of the following options:")
    print("1. Rectangle")
    print("2. Circle ")
    print("3. Triangle")
    print("4. Sphere ")
    print("5. Exit")
    Choice = int(input("Enter Selection:"))
    print()
    menu_validate(Choice)

    if menu_validate(Choice):
        return Choice
    else:
        print("Input Invalid! Please try again")
        return menu()

#Validation Functions
def menu_validate(Choice):
    return 1 <= Choice <= 5

def shape_validate(List):
    for i in List:
        if i <= 0:
            return False
        else:
            return True
        
#Calculations for the area/volume of shapes
def rectangle_area(Width, Length):
    if shape_validate([Width, Length]):
        Area_Rectangle = Width * Length
        return Area_Rectangle

def circle_area(Radius):
    if shape_validate([Radius]):
        Area_Circle = (math.pi)*(Radius ** 2)
        return Area_Circle

def triangle_area(Edge1, Edge2, Edge3):
    if shape_validate([Edge1,Edge2,Edge3]):
        S = (Edge1 + Edge2 + Edge3)/2
        Area_Triangle = math.sqrt(S*(S-Edge1)*(S-Edge2)*(S-Edge3))
        return Area_Triangle


def sphere_volume(Radius):
    if shape_validate([Radius]):
        Volume_Sphere = (4/3)*(math.pi)*(Radius ** 3)
        return Volume_Sphere


if __name__ == '__main__':
    description()
    #Loop for the user
    while True:
        Choice = menu()
        if Choice == 1:
            Width = int(input("Please enter the Rectangle Width:"))
            Length = int(input("Please enter the Rectangle Length:"))
            print()
            print(f"The rectangle's area is {rectangle_area(Width, Length):.2f}")
                 
        elif Choice == 2:
            Radius = int(input("Please enter the Circle's Radius:"))
            print(f"The circle's area is {circle_area(Radius):.2f}")
        elif Choice == 3:
            Edge1 = int(input("Please enter the first edge of the triangle:"))
            Edge2 = int(input("Please enter the second edge of the triangle:"))
            Edge3 = int(input("Please enter the third edge of the triangle:"))
            print()
            print(f"The area of the triangle with the above Edges is {triangle_area(Edge1, Edge2, Edge3):.2f}")
        elif Choice == 4:
           Radius = int(input("Please enter the Sphere's Radius:"))
           print()
           print(f"The sphere's volume is {sphere_volume(Radius):.2f}")
        elif Choice == 5:
            print("Thanks for using the program: Goodbye!")
            break

#Example Outputs
'''
Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.

= RESTART: /Users/joaodias/Desktop/Computer Codes/CMPSC131Fall2025/Dias_Joao_Exam2.py
This program is a Geometric Calculator for different shapes.

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:1

Please enter the Rectangle Width:10
Please enter the Rectangle Length:20

The rectangle's area is 200.00

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:2

Please enter the Circle's Radius:24
The circle's area is 1809.56

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:3

Please enter the first edge of the triangle:10
Please enter the second edge of the triangle:20
Please enter the third edge of the triangle:30

The area of the triangle with the above Edges is 0.00

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:4

Please enter the Sphere's Radius:33

The sphere's volume is 150532.55

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:5

Thanks for using the program: Goodbye!
'''

'''
This program is a Geometric Calculator for different shapes.

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection: 11

Input Invalid! Please try again

Choose one of the following options:
1. Rectangle
2. Circle 
3. Triangle
4. Sphere 
5. Exit
Enter Selection:5

Thanks for using the program: Goodbye!
'''

                        
                         
        
    
