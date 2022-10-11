# Functions Return Statements
# They are used to return the results of a function after execution , therefore the returned
# Values can be stored inside variable , to be used on another program

def multiply(a, b, c):
    print(a*b*c)


result = multiply(10, 10, 10)
print(result)

def sum(A, B, C):
    return A+B+C

def product(D):
    return D*4

answer = product(sum(20, 20, 20))
print(answer)


