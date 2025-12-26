#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW8.py
#Date: November 14, 2025

#Short Description: Calculates and Displays A Quadratic Equation

#Important math equations that will be later used
import math

#Program Description Output:
print("This program will calucalte a quadratic function based on User Input")
print()

#Functions that are later called
#Calculates Discriminant and checks if positive or negative or 0
def disc(A,B,C):
    Result = (B ** 2)-(4*A*C)
    if Result > 0:
        quadRoots(A,B,C,Result)
    elif Result == 0:
        quadRoots(A,B,C,Result)
    else:
        print("No real Roots Exist")

#Calcualtes the equation depending on previous function result
def quadRoots(A,B,C,Result):
    if Result > 0:
        Solution1 = ((-1*B)+ math.sqrt(Result))/(2*A)
        Solution2 = ((-1*B)- math.sqrt(Result))/(2*A)
        print(f"The Two Roots are {Solution1:.2f} and {Solution2:.2f}")
    elif Result == 0:
        One_Solution = -B/(2*A)
        print(f"The Single Root is {One_Solution:.2f}")
        

#Inputs for User
if __name__ == '__main__':
        A = int(input("Please type the A Value:"))
        B = int(input("Please type the B Value:"))
        C = int(input("Please type the C Value:"))
        
        #Checks for valid numbers
        if A == 0:
            print("0 can't be chosen for A")
        else:
            disc(A,B,C)

'''
Discriminant is positive using 10,22,8

This program will calucalte a quadratic function based on User Input

Please type the A Value:10
Please type the B Value:22
Please type the C Value:8
The Two Roots are -0.46 and -1.74

'''

'''
Discriminant is negative

This program will calucalte a quadratic function based on User Input

Please type the A Value:10
Please type the B Value:1
Please type the C Value:20
No real Roots Exist
'''

'''
Discriminant is 0

This program will calucalte a quadratic function based on User Input

Please type the A Value:1
Please type the B Value:2
Please type the C Value:1
The Single Root is -1.00
'''
