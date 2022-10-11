# if ..elif....else

# Grading system logical operators
# 40 ->D
# 41-5O ->C
# 51-69 ->B
# 70-100 and above -> A
# Above 100 , less than 0 invalid marks

marks = int(input("Enter your Marks"))
if marks > 0 and marks <= 40:
    print("You scored D")
elif marks >= 41 and marks <=50:
    print("You scored C")
elif marks >= 51 and marks <=60:
    print("you scored B")
elif marks >= 70 and marks <=100:
    print("you scored A")
else:
    print("Invalid marks!")

