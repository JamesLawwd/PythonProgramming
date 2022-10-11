# create a list of students .
# 1. Add 2 new students
# Show the 4th to 7th students
# Replace the 3rd student
# Check if a certain student is not existing , add the student
#
students = ["Mark", "George", "James", "Andrew", "Mateo", "Richard"]

students.append("Alex")
students.append("Peter")
print(students)

print(students[3:7])

students[2] = "Timothy"
print(students)

if " James" not in students:
    students.append("Max")
    print(students)
print(students)







