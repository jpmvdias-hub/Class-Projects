#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW4.py
#Date: September 30, 2025

#Short Description: Calculate and display BMI Index


#Program Description Output
print("This program will calucalte your BMI")


#Create and Display the input
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

#BMI Calculation
BMI = (weight * 703)/(height**2)

#BMI Check
if (BMI < 18.5):
    print(f"Your BMI is {BMI:.2f}, this means you are underweight")
elif (BMI >= 18.5) and (BMI <= 25):
    print(f"Your BMI is {BMI:.2f}, this means you have an optimal weight")
elif (BMI > 25):
    print(f"Your BMI is {BMI:.2f}, this means you are overweight")

'''
The inputs were 200 pounds and 72 inches
This program will calucalte your BMI
Enter your weight in pounds: 200
Enter your height in inches: 72
Your BMI is 27.12, this means you are overweight
'''

'''
The inputs were 100 pounds and 72 inches
This program will calucalte your BMI
Enter your weight in pounds: 100
Enter your height in inches: 72
Your BMI is 13.56, this means you are underweight
'''

'''
The inputs were 150 pounds and 72 inches
This program will calucalte your BMI
Enter your weight in pounds: 150
Enter your height in inches: 72
Your BMI is 20.34, this means you have an optimal weight
'''

