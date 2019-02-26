# Brianna Priddy
# CSCI 101 MWF 12pm
# Lab 4A - What are the factors of the number?

print("Enter a positive integer and I will tell you its factors")
number = int(input("NUMBER>"))
index = 1
counter = 0

# count the number of factors

while index <= number:
    if number % index == 0:
        counter += 1
    index += 1
print("There are", counter, "factors in the number ", number, end=".\n")
index = 1
print("OUTPUT> ", end="[")

# list the factors

while index < number:
    if number % index == 0:
        print(index, end=", ")
    index += 1
print(number, "]")
