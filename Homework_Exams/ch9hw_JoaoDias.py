#Name: Joao Dias
#Course: CMPSC 131, Section 002
#File Name: Dias_HW9.py
#Date: November 22, 2025

#Short Description: Calculates and Displays A Scrabble total for a word


if __name__ == '__main__':
    #Dictionary of Tile Amounts Based on Letter
    tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }
    #User Input
    User_input = input("Please enter a word:").upper()
    Point_Total = 0

    #Loop that calculates points of word
    for letter in User_input:
        if letter in tile_dict:
            Point_Total += tile_dict[letter]
            
#Output of points
print("Total points:", Point_Total)

'''
Please enter a word:python
Total points: 14
'''

'''
Please enter a word:Germany
Total points: 13
'''

'''
Please enter a word:POTATO
Total points: 8
'''
        
    
    
    
