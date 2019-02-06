weight = 0.0
height = 0.0
BMI = 0.0

print("What is your weight in pounds?")
weight = float(input("WEIGHT> "))
print("What is your height in inches?")
height = float(input("HEIGHT> "))

weight = (weight*0.454)
height = (height*0.0254)
BMI = weight/(height*height)

print("Your body-mass index is: ")
print("OUTPUT ", BMI)
