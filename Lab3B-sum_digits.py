#Brianna Priddy
#Intro to Comp Sci
#Lab2B - sum digits

print('Enter a number to sum its digits.')
number = input('NUMBER>')

#going through the list of numbers in the digits, add the sum

total = sum(int(digit) for digit in number)
print('The sum of the digits in ', number, 'is', total)
print('OUTPUT', len(number), 'digits')
print('OUTPUT', total, 'sum')
