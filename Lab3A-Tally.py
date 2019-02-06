#Brianna Priddy
#INTRO TO PROGRAMINT
#LAB3A - TALLY

number = 0
total = 0
quantity = -1

#prompt user for input

print('Enter values to add. Enter \'quit\' to exit')

#check for input being a string 'quit' while adding numbers used

while number != 'quit':
    #add the new number to the total
    total = total + int(number)
    #increment the number of numbers entered(because of the programs format, initialized at -1 because quit will count as a number
    quantity += 1
    #take the input from the user
    number = input('NUMBER>')

    #print the quantity and total

print('The sum of the', quantity, 'numbers entered was', total)
print('OUTPUT', quantity, 'numbers')
print('OUTPUT', total, 'total')
