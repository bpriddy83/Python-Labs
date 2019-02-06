print('Enter a positive number.')
number = int(input('NUMBER>'))
print('The sibling(s) that will work with', number, 'is as follows:')

#Jimmy will only work with odd numbers.
#Jared will only work with numbers greater than 10 but less than 100 (inclusive).
#Josephine will only work with double digit numbers whose digits add up to 8.

if((number%2) != 0):
    print('OUTPUT Jimmy')
if((number >= 10) and (number <= 100)):
    print('OUTPUT Jared')
if(((number >= 10) and (number < 100)) and (((number//10) + (number%10)) == 8)):
    print('OUTPUT Josephine')
