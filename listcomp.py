n = int(input("Enter a number: "))

odd_numbers = [x for x in range(n) if x % 2 != 0]
print("Odd numbers:", odd_numbers)


fruits = ['apple', 'banana', 'mango', 'grape']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)