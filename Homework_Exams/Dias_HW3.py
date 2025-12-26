#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW3.py
#Date: September 22, 2025

#Short Description: Create a password using inputs from the user.


#Program Description Output
print("This program will create two new passwords on your inputs")

#Create and Display the input
Color = input("Enter your favorite color: ")
Flower = input("Enter your favorite flower: ")
Number = input("Enter your favorite number: ")

#Create the Password
numbercolornumber =  Number + Color + Number
color_flower =  Color + "_" + Flower

#Displays passwords
print("First password: ", color_flower)
print("Second password: ", numbercolornumber)

#Counts number of characters in password and displays it
Mycharacter1 = len(color_flower)
print ("Number of characters in", color_flower, ":", Mycharacter1)
Mycharacter2 = len(numbercolornumber)
print ("Number of characters in", numbercolornumber, ":", Mycharacter2)

'''
Inputs were red, lily, and 8

This program will create two new passwords on your inputs
Enter your favorite color: red
Enter your favorite flower: lily
Enter your favorite number: 8
First password:  red_lily
Second password:  8red8
Number of characters in red_lily : 8
Number of characters in 8red8 : 5
'''

'''
Inputs were purple, tulip, and 99

This program will create two new passwords on your inputs
Enter your favorite color: purple
Enter your favorite flower: tulip
Enter your favorite number: 99
First password:  purple_tulip
Second password:  99purple99
Number of characters in purple_tulip : 12
Number of characters in 99purple99 : 10
'''

'''
Inputs were aquamarine, lotus, and 2

This program will create two new passwords on your inputs
Enter your favorite color: aquamarine
Enter your favorite flower: lotus
Enter your favorite number: 2
First password:  aquamarine_lotus
Second password:  2aquamarine2
Number of characters in aquamarine_lotus : 16
Number of characters in 2aquamarine2 : 12
'''




