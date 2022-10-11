# Algorithm -> Step-by-step procedure of accomplishing a given task

# Simple Interest

#1. store value of principle of variable
#2. Store value of rate
#3. store the value of time

#interest = (principle*rate * time )/100
#output the value of variable interest
#Generating a user input

principle = int(input("Enter your principle: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time : "))


#
interest = ((principle * rate * time) / 100)
print("The interest is :", interest)

# 1. Using above concept ,write a code that will be prompting a user to enter amount in
# dollars then convert to kenyan shilling
# exchange rate : 1$ = 100 kshs

# Lists, Tuples , Dictionaries, array (sets)

#2. # Write a code to calculate the volume of a cylinder, generating the dimentions  from the user
#PI * r**2 *H

amount = int(input ("Enter the amount of money you wish to spend in dollars : "))

amount_kshs = amount * 100

print(amount_kshs)



# code to calculate a person's bmi body mass index

# weight(kg)
# height(m) 1.5 -2m

# bmi = weight /height **2)

weight = float(input ("Enter your mass in kgs"))
height = float(input(" Enter your height in m"))
bmi = weight/(height**2)
print(" your bmi:",bmi)


