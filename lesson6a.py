# Functions = This a block of code that is performing a related task
# categories of functions
# Enclosed inside brackets
# Inbuilt Function ,print(), input(),type(), int()....
# User -Defined functions
# Keyword def,
# function name
# brackets
# full colon
# Any item of a function is indented -

# add two numbers
# creating
def add():
    a = 10
    b = 20
    sum = a + b
    print(sum)


# calling a function
# name , followed by brackets
add()

# create and call a function that computes the area of a circle

def area():
    PI = 3.142
    r = 6
    function = PI * r**2
    print(function)
area()

def volume ():
    PI = 3.142
    r = 3
    function = PI * 1/3 * 3.142 * r**3
    print(function)
volume()

# Parameters -> Values that are passed inside a function
def multiply(num1, num2):
    product = num1 * num2
    print(product)

# multiply(10,10)

for count in range(10):
    print(count)

def greet(name):
    print("Hi, how are you {}".format(name))
greet("James")

# using function create a bmi calculator

def bmi_calculator(weight= 55, height =1.6):
    bmi = weight / (height**2)
    print(bmi)
    return bmi
bmi_calculator()






