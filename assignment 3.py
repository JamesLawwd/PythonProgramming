# BMI Calculator
# weight (kg)
# height (m)

# bmi = weight / (height)
# if < 18.5:
weight = float(input("Enter your weight"))
height = float(input(" Enter your height"))

bmi = weight / (height*height)

if bmi < 18.5:
    print("underweight")

elif bmi > 18.5 and bmi <=22.9:
    print( "you are noraml")

elif bmi >=22.9 and bmi <=24.9:
    print( "you are over weight")
elif bmi >= 24.9 and bmi <=29.9:
    print("Preobese")
elif bmi >= 29.9 and bmi <=34.9:
    print("obese class 1")
elif bmi >= 34.9 and bmi <= 39.9:
    print("obese class 2 ")
elif bmi >=40.0:
    print("obese class 3  ")

else:
    print("ERROR")



