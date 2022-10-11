# Data Types
# 1. String ,Integers,Float , Booleans
# Arrays -> A Collection of items together
# list, Tuple ,Dictionary, Sets

# List Data Types
# It contains a list of changeable, ordered,allow duplicates items
# Enclosed inside Squared Brackets []

countries = ["Kenya", "Somalia", "Ghana", "Burundi"]
numbers = [10, 30, 20, 40]
instances = [True, False, False, True]

counties = ["Nairobi", 47, "Mombasa", 1, True, 20.45]

# lists Operations
# 1. Length-> len()
# Type -> type()

print(len(counties))
print(type(countries))

# Accessing Items on a list
# 1. Index-> Starts from zero []
# 2. range -> First item is included , the last item is excluded

print(numbers[0])
print(countries[1:3])

fruits = ["Pineapples", "Oranges", " Pawpaw", "Apple", "Mango"]
numbers = [10, 15, 12, 20, 30]
print(fruits[2:4])
print(fruits[4])

# Check existence of an element (in)

if "Apple" in fruits:
    print("Apple Exist")

# adding, Replacing an element ,add list to a list
# append ()-> Adds a new element to the list

fruits.append("banana")
print(fruits)

# Replacing an element

fruits.insert(1, "oranges")
print(fruits)

# extend() -> Add lists to a list
fruits.extend(countries)
print(fruits)

# Adding items from alist
# index -> pop ()
# element-> remove()


fruits.pop(7)
print(fruits)
fruits.remove("Pineapples")
print(fruits)

# all the element -> clear()

fruits.clear()
print(fruits)
del fruits













