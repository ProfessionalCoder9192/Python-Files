test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:", test_dict)

value = int(input("Enter the value to check frequency: "))

frequency = list(test_dict.values()).count(value)

print(f"The frequency of value {value} is:", frequency)