try:
    number1, number2 = eval(input("Enter two numbers, seperated by a comma:"))
    result = number1 / number2
    print("Result is",  result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing, Please enter numbers seperated with a comma like this: 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what.")