# Python Dictionaries
# Holds a collection of keys with  their value
# Changeable , Ordered , no Duplicates allowed
# JSON file -> dictionary (ApIs)
# JavaScript Object Notation
# created using braces{}

students = {
    "name": "Robin",
    "age": 20,
    "course" : "Software Development",
    "gender" : "Male",
    "age": 34,
    "courses": ["Android", "Python", "Machine learning"]
}

# Operation
# accessing elements

print(students["name"])
print(students)

x = students.keys()
y = students.values()

z = students. items()
print(x)
print(y)
print(z)

students["height"] = 1.8
print(students)

students["course"] = "Cyber Security"
print(students)

students.pop("gender")
print(students)

# Sets
# Conditions (COMPARISON AND LOGICAL OPERATIONS)
