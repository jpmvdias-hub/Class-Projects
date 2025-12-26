#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW7.py
#Date: October 28, 2025

#Short Description: Calculates and Displays Price of a Circuit Board

#Program Description Output if (Wholesale > 0) and (Markup > 0):
print("This program will calucalte the price of a Circuit Board")
print()

#Function that is later called
def Final_Calc(Wholesale, Markup):
    Result = Wholesale * (Markup/100)
    Final_Price = Result + Wholesale
    return Final_Price

#Inputs for User
if __name__ == '__main__':
    while True:
        print()
        Wholesale = input("What is the wholesale price of the circuit board($) or type Done if finished:")
        Markup = input("What is the Markup Percentage or type done if finished (%)?:")
        if (Wholesale.lower()=="done") or (Markup.lower()=="done"):
            print("Program End")
            break
        Wholesale = float(Wholesale)
        Markup = float(Markup)
#Checks if inputs are postive
        if (Wholesale > 0) and (Markup > 0):
            print()
            print(f"The final selling price is ${Final_Calc(Wholesale, Markup):.2f}")
        else:
            print("Please run code again and use positive numbers")


'''
This program will calucalte the price of a Circuit Board


What is the wholesale price of the circuit board($) or type Done if finished:22
What is the Markup Percentage or type done if finished (%)?:22

The final selling price is $26.84

What is the wholesale price of the circuit board($) or type Done if finished:11
What is the Markup Percentage or type done if finished (%)?:11

The final selling price is $12.21

What is the wholesale price of the circuit board($) or type Done if finished:Done
What is the Markup Percentage or type done if finished (%)?:Done
Program End
'''

'''
This program will calucalte the price of a Circuit Board


What is the wholesale price of the circuit board($) or type Done if finished:22
What is the Markup Percentage or type done if finished (%)?:11

The final selling price is $24.42

What is the wholesale price of the circuit board($) or type Done if finished:10
What is the Markup Percentage or type done if finished (%)?:Done
Program End
'''



            



