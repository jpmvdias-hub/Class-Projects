#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_Joao_Exam1.py
#Date: October 7, 2025

#Short Description: Calculate a length in feet and
#and display it as different units like inches,meters,


#Program Description Output
print("This program will convert your length in feet to different units")


#Create and Display the input
Length = float(input("Please enter the volume in feet: "))

#Prints out menu for user to choose from
print()
print("Conversion Menu")
print()
print("C or c - convert to centimeters")
print("I or i - convert to inches")
print("M or m - conver to meters")
print("Y or y - convert to yards")


# User Input
User_Convert = input("Please enter the character for the conversion"
                     " units according to the chart above: ")


#Checks to make sure input is valid
if (Length <= 0):
    print("This input is invalid as it is less than or equal to 0. Please re-run the code.")
else:
    if (User_Convert == "C") or (User_Convert == "c"):
        Inches = Length * 12
        Centimeter = Inches * 2.54
        print(f"{Length:.3f} feet is equal to {Centimeter:.3f} centimeters")
        
    elif (User_Convert == "I") or (User_Convert == "i"):
        Inches = Length * 12
        print(f"{Length:.3f} feet is equal to {Inches:.3f} inches")
        
    elif (User_Convert == "M") or (User_Convert == "m"):
        Inches = Length * 12
        Centimeter = Inches * 2.54
        Meter = Centimeter/100
        print(f"{Length:.3f} feet is equal to {Meter:.3f} Meters")

    elif (User_Convert == "Y") or (User_Convert == "y"):
        Yards = Length/3
        print(f"{Length:.3f} feet is equal to {Yards:.3f} Yards")

    else:
        print("This input is invalid, please restart the code")


'''
Input was 0 feet and I
This program will convert your length in feet to different units
Please enter the volume in feet: 0

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: I
This input is invalid as it is less than or equal to 0. Please re-run the code.
'''

'''
Input was 10 and C

This program will convert your length in feet to different units
Please enter the volume in feet: 10

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: C
10.000 feet is equal to 304.800 centimeters
'''

'''
Input was 10 and c

This program will convert your length in feet to different units
Please enter the volume in feet: 10

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: c
10.000 feet is equal to 304.800 centimeters

'''

'''
Input was 3 and I
This program will convert your length in feet to different units
Please enter the volume in feet: 3

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: I
3.000 feet is equal to 36.000 inches
'''

'''
Input was 3 and i
This program will convert your length in feet to different units
Please enter the volume in feet: 3

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: i
3.000 feet is equal to 36.000 inches
'''

'''
Input was 10 and M
This program will convert your length in feet to different units
Please enter the volume in feet: 10

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: M
10.000 feet is equal to 3.048 Meters
'''

'''
Input was 10 and m
This program will convert your length in feet to different units
Please enter the volume in feet: 10

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: m
10.000 feet is equal to 3.048 Meters
'''

'''
Input was 3 and Y
This program will convert your length in feet to different units
Please enter the volume in feet: 3

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: Y
3.000 feet is equal to 1.000 Yards


'''

'''
Input was 4 and y
This program will convert your length in feet to different units
Please enter the volume in feet: 4

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: y
4.000 feet is equal to 1.333 Yards

'''

'''
Input was 10 and z
This program will convert your length in feet to different units
Please enter the volume in feet: 10

Conversion Menu

C or c - convert to centimeters
I or i - convert to inches
M or m - conver to meters
Y or y - convert to yards
Please enter the character for the conversion units according to the chart above: Z
This input is invalid, please restart the code
'''
