#CMPSC 131
#Student Name: Joao Dias
#Date: 12/18/2025
#File Name: final_JoaoDias.py

#Gives description of the code
def description():
    print("This program is to read sale data from a file, then calculate the sales amount and commission for distributors and save it into another file")

#Reads Data from given text file
def read_data(file_name):
    OpenFile = open(f"{file_name}")
    Contents = OpenFile.readlines()
    OpenFile.close()
    return Contents

def calculate_sales(Contents):
    #Lists we will fill out
    Sales_list = []
    Distributors = []
    Sales = []
    for i in Contents[1:]:
        parts = i.split()
        Distributor_num = int(parts[0])
        Distributors.append(Distributor_num)
        
        Product1 = float(parts[1]) * 15
        
        Product2 = float(parts[2]) * 5
        
        Product3 = float(parts[3]) * 45
        
        Product4 = float(parts[4]) * 150

        #Checks if Products are positive
        if (Product1 or Product2 or Product3 or Product4) < 0:
            print("Your products cannot be negative")
        else:
            Final_sale = Product1 + Product2 + Product3 + Product4
            if Final_sale < 0:
                print("Your final sale cannot be negative")
            else:
                Sales.append(Final_sale)

            
    #Connects each distributor number with their sales numbers
    for i in range(len(Distributors)):
        Sales_list.append([Distributors[i], Sales[i]])
    return Sales_list

def calculate_commision(Sales_list):
    Final_list = []
    #Calculates Commission amounts based on sales
    for Distributor, Sales in Sales_list:
        if Sales > 100000:
            Commision = (20/100) * Sales
        elif Sales > 50000 and Sales < 100000:
            Commision = (15/100) * Sales
        elif Sales > 10000 and Sales < 50000:
            Commision = (12/100) * Sales
        else:
            Commision = (10/100) * Sales
            #Appends everything to a final list
        Final_list.append([Distributor, Sales, Commision])
    return Final_list
    

def write_data(Final_list):
    #Writes down the information into a new list
    result_file = open("result.txt", "w")
    result_file.write("Name, Sales, Commission\n")
    for i in range(len(Final_list)):
        result_file.write(str(Final_list[i][0]) + " ")
        result_file.write(str(Final_list[i][1]) + " ")
        result_file.write(str(Final_list[i][2]) + "\n")
    result_file.close()

if __name__ == '__main__':
    description()
    print()
    #Asks user for their input
    User_Input = input("Enter the file name for sales:")
    print()
    #Calling the various functions
    read_data(User_Input)
    calculate_sales(read_data(User_Input))
    calculate_commision(calculate_sales(read_data(User_Input)))
    write_data(calculate_commision(calculate_sales(read_data(User_Input))))
    print()
    #Prints out the Result Text File
    OpenFile = open("result.txt")
    Contents_Result = OpenFile.readlines()
    OpenFile.close()
    print(Contents_Result)
    print()
    print("Thanks for testing the program!")


'''
This program is to read sale data from a file, then calculate the sales amount and commission for distributors and save it into another file

Enter the file name for sales:sales.txt


['Name, Sales, Commission\n', '1 17700.0 2124.0\n', '2 15100.0 1812.0\n', '3 8700.0 870.0\n', '4 43800.0 5256.0\n', '5 22350.0 2682.0\n', '6 8575.0 857.5\n', '7 5975.0 597.5\n', '8 11075.0 1329.0\n', '9 19150.0 2298.0\n', '10 21575.0 2589.0\n', '11 12450.0 1494.0\n', '12 25550.0 3066.0\n', '13 22350.0 2682.0\n', '14 62250.0 9337.5\n', '15 52925.0 7938.75\n', '16 76325.0 11448.75\n', '17 17400.0 2088.0\n', '18 18850.0 2262.0\n', '19 20150.0 2418.0\n', '20 43800.0 5256.0\n', '21 4550.0 455.0\n', '22 8425.0 842.5\n', '23 52050.0 7807.5\n', '24 9075.0 907.5\n', '25 5800.0 580.0\n', '26 35125.0 4215.0\n', '27 14100.0 1692.0\n', '28 23350.0 2802.0\n', '29 6350.0 635.0\n', '30 16625.0 1995.0\n', '31 6425.0 642.5\n', '32 37775.0 4533.0\n']

Thanks for testing the program!
'''







