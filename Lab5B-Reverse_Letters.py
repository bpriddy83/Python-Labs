#Brianna Priddy
#Section C
#Lab 5 B - Reverse only letters

wannaPlay = 'y'
while wannaPlay == 'y' or wannaPlay == 'Y':
    print('Enter a string with letters to reverse.')
    string = str(input('STRING>'))
    print('OUTPUT:', end=' ')
    i = len(string)-1
    while i >= 0:
        print(string[i], end='')
        i -= 1
    print('\nWould you like to enter another string to reverse?')
    wannaPlay = input('y/n>')
