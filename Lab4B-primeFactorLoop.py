# Brianna Priddy
# CSCI 101 MWF 12pm
# Lab 4B - prime factors

factorList = []
playAgain = "y"

while playAgain.lower() == "y" or playAgain.lower() == "yes":

    # Get user input

    print("Enter a positive integer to find out its prime factors.")
    number = int(input("NUMBER>"))
    index = 2

    # if the number is divisible by 2 add a 2 to the list of prime factors
    # otherwise, add one to index

    while number != 1:
        if number % index == 0:
            factorList.append(index)
            number = number / index
        else:
            index = index + 1

    # print the list and results

    print("The prime factors of", number, "are:")
    print("OUTPUT>", end="")
    for x in factorList:
        if len(factorList) != 0:
            print("*", end="")
        print(x, end="")

    # does the user want to try another number?

    print("\nWould you like to play again? ")
    playAgain = input()
