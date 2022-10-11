# Tuples Data Type
# Unchangeable, Orderded, Allow duplicates
# Brackets ()
courses = ("Android", "Data Science", "Python")
language = ("Python",)
# type()

print(type(courses))
print(type(language))

# Accessing Elements-> Ordered index ,starts from zero,[]
print(courses[1])
print(courses)

x = list(courses)
print(x)

x.append("IoT")
print(courses)

# create a tuple of 5 schools
# add 3 more schools

schools = ("Moringa", "Modcom",  "Tiyon", "Lyons", "Chania")
language = ("python")

print(type(schools))
print(type(language))

print(type(schools))
print(schools)

x = list(schools)
print(x)

x.append("Kiambu")
x.append("Molly")
x.append("Destiny")
print(x)

schools = tuple(x)
print(schools)

boys = ("mark", "john", "peter")
print(type(boys))
print(boys)
print(x)

x = list(boys)
print(x)

x .append("ruth")
x .append("daina")
x .append("treo")
print(x)

x[2] = "rael"
print(x)

boys = tuple(x)
print(boys)











