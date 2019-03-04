#Brianna Priddy
#Section C
#Lab 5 A - It's Full of stars

name = str(input('NAME>'))
size = len(name)
for numRows in range(0, size):
    for numSpaces in range(0, size-1-numRows):
        print(' ', end='')
    for numStars in range(0, numRows+1):
        print('* ', end='')
    print('\r')
for letter in name:
    if letter == ' ':
        print('_', end=' ')
    else:
        print(letter, end=' ')
