def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print ("Please select the operation you would like to preform:")
print ("a. Add")
print ("b. Subtract")
print ("c. Multiply")
print ("d. Divide")

choice = input("Please enter your choice. (a/b/c/d):")

num1 = int(input("Please enter your first number."))
num2 = int(input("Please enter your second number."))

if choice == "a":
    print (num1, " + ", num2, " = ", num1+num2)
elif choice == "b":
    print (num1, " - ", num2, " = ", num1-num2)
elif choice == "c":
    print (num1, " * ", num2, " = ", num1*num2)
elif choice == "d":
    print (num1, " / ", num2, " = ", num1/num2)
