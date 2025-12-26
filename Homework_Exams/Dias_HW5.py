#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW5.py
#Date: October 14, 2025

#Short Description: Calculate and display a Bank Account Balance


#Program Description Output
print("This program will calucalte a Bank Account Balance")


#Create and Display the input
Interest_Rate = float(input("Enter the Annual Interest Rate: "))
Starting_Balance = float(input("Enter the Starting Balance: "))
Months = float(input("Enter the amount of months you'll be depostiting for: "))
if Months < 0:
    print("Invalid Amount, Please run the Code again")
else:
    Count = 1
#Lists to keep count of User Inputs
Deposit = []
Withdrawal = []
Interest = []
Formatted_Interest = []

#Creation of Loop

while (Count <= Months):
    
#Monthly Deposit Description
    print()
    Month_Deposit = float(input("How much money did you deposit this month?: "))
    if Month_Deposit < 0:
            print("Please Enter a Positive Number")
    else:
       Starting_Balance = Starting_Balance + Month_Deposit
       print(f"Your balance is: ${Starting_Balance:.2f}")
       Deposit.append(Month_Deposit)
       
#Withdrawal Calculation
       print()
    Month_Withdrawal = float(input("How much money did you withdraw this month?: "))
    if Month_Deposit < 0:
            print("Please Enter a Positive Number")
    else:
       Starting_Balance = Starting_Balance - Month_Withdrawal
       print(f"Your balance is: ${Starting_Balance:.2f}")
       Withdrawal.append(Month_Withdrawal)

#Negative Balance Check
    if Starting_Balance < 0:
        print("The account is closed due to negative balance")
        break

#Interest Rate
    Interest_Monthly = (Interest_Rate/12) * Starting_Balance
    Starting_Balance = Starting_Balance + Interest_Monthly
    Interest.append(Interest_Monthly)
    Formatted_Interest = [round(item,2)for item in Interest]
    
    print()
    print(f"Your balance after Interest is: ${Starting_Balance:.2f}")
    Total_Deposit= sum(Deposit)
    Total_Withdrawal = sum(Withdrawal)
    Total_Interest = sum(Formatted_Interest)
    
    print()

#Monthly Summary
    print("Summary for the Month")
    print("You deposited: $",Total_Deposit)
    print("You Withdrew: $",Total_Withdrawal)
    print("Your Interest was: $",Total_Interest)
    print(f"Your Current Balance is: ${Starting_Balance:.2f}")
    Count +=1

#Final Total
Total_Deposit= sum(Deposit)
Total_Withdrawal = sum(Withdrawal)
Total_Interest = sum(Formatted_Interest)
print()
print(f"Your Final Balance is: ${Starting_Balance:.2f}")
print("You Desposited: $",Total_Deposit)
print("You Withdrew: $",Total_Withdrawal)
print("Your total interest is: $",Total_Interest)

#Sample Program Runs
'''
Interest of 2, Balance of $100, and 2 Month Deposit time

This program will calucalte a Bank Account Balance
Enter the Annual Interest Rate: 2
Enter the Starting Balance: 100
Enter the amount of months you'll be depostiting for: 2

How much money did you deposit this month?: 200
Your balance is: $300.00

How much money did you withdraw this month?: 30
Your balance is: $270.00

Your balance after Interest is: $315.00

Summary for the Month
You deposited: $ 200.0
You Withdrew: $ 30.0
Your Interest was: $ 45.0
Your Current Balance is: $315.00

How much money did you deposit this month?: 33
Your balance is: $348.00

How much money did you withdraw this month?: 110
Your balance is: $238.00

Your balance after Interest is: $277.67

Summary for the Month
You deposited: $ 233.0
You Withdrew: $ 140.0
Your Interest was: $ 84.67
Your Current Balance is: $277.67

Your Final Balance is: $277.67
You Desposited: $ 233.0
You Withdrew: $ 140.0
Your total interest is: $ 84.67

'''
'''
Interest of 10, Balance of $200, and What happens if months are 0

This program will calucalte a Bank Account Balance
Enter the Annual Interest Rate: 10
Enter the Starting Balance: 200
Enter the amount of months you'll be depostiting for: 0

Your Final Balance is: $200.00
You Desposited: $ 0
You Withdrew: $ 0
Your total interest is: $ 0
'''
'''
Interest of 3.3, Balance of $100, and 2 Month Deposit
What happens if program comes back negative

This program will calucalte a Bank Account Balance
Enter the Annual Interest Rate: 3.3
Enter the Starting Balance: 100
Enter the amount of months you'll be depostiting for: 2

How much money did you deposit this month?: 100
Your balance is: $200.00

How much money did you withdraw this month?: 20
Your balance is: $180.00

Your balance after Interest is: $229.50

Summary for the Month
You deposited: $ 100.0
You Withdrew: $ 20.0
Your Interest was: $ 49.5
Your Current Balance is: $229.50

How much money did you deposit this month?: 150
Your balance is: $379.50

How much money did you withdraw this month?: 380
Your balance is: $-0.50
The account is closed due to negative balance

Your Final Balance is: $-0.50
You Desposited: $ 250.0
You Withdrew: $ 400.0
Your total interest is: $ 49.5
'''

        
       


