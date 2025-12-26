#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW2.py
#Date: September 16, 2025

#Short Description: Calculate final selling price of a circuit board

#Program Description Output
print("This program will calculate and display the final selling price of a circuit board")

#Asks user for Input for Wholesale price of Circuit board and the percent profit of the board
Board= float(input("Enter wholesale price of circuit board: "))
Profit= float(input("Enter the percent profit (%): "))
            
#Calculation of Final Selling Price
Sell_Price = Board + (Board * Profit/100)


#Displays Result of Calculation
print("The final sale price with the percent profit and wholesale cost is: ",f"{Sell_Price:.2f}" )



#Output if the cost is $16.95 and 30% Profit

'''
Enter wholesale price of circuit board: 16.95
Enter the percent profit (%): 30
The final sale price with the percent profit and wholesale cost is:  22.04
 '''


#Output if the cost is $12.49 and 22% Profit

'''
Enter wholesale price of circuit board: 12.49
Enter the percent profit (%): 22
The final sale price with the percent profit and wholesale cost is:  15.24

'''

#Output if the cost is $19.22 and 44%
'''
Enter wholesale price of circuit board: 19.22
Enter the percent profit (%): 44
The final sale price with the percent profit and wholesale cost is:  27.68
'''

    
    


