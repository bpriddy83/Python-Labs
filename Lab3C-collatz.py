#Brianna Priddy
#Intro to comp sci
#Lab3C-Collatz

print('Enter a positive integer to see the Collatz Conjecture:')

#get a number from the user

number = int(input('NUMBER>'))
print('The Collatz conjecture for ', number, 'is:')

#print OUTPUT followed by a space and commas between numbers

print('OUTPUT', end=' ')
while number > 1:
    if number % 2 == 0:
        print(number,',', end='')
        number = int(number/2)
    else:
        print(number,',', end='')
        number = int((number * 3) +1)
print('1')
