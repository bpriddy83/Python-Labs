# Brianna Priddy
# CSCI 101 MWF 12pm
# Lab 4C - unique visitors

# Request an input of a comma separated string (e.g. "orden, Azam, OrdeN, Nhan")

print("Enter a list of names separated with commas.")
inputNames = input("LIST>")

usedAlready = False
nameList = []

words = [word for word in inputNames.split(",")]

for word in words:

    # if the used words list is empty, add the word

    if len(nameList) == 0:
        nameList.append(word)

        # otherwise, if the word has been used already, let the program no

    else:
        for checkWord in nameList:
            if checkWord == word:
                usedAlready
                print("\n", word, "was already used")
        if not usedAlready:
            nameList.append(word)

for name in nameList:
    if not nameList[0]:
        print(end=",")
    print(name, end="")


for name in nameList:
    if not nameList[0]:
        print(end=",")
    print(name, ",", nameList.count(name), end="")