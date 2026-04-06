def to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

user_input = input("Enter an integer: ")
if user_input.isdigit():
    number = int(user_input)
    if 0 < number < 4000:
        print(f"Roman Numeral: {to_roman(number)}")
    else:
        print("Please enter a number between 1 and 3999.")
else:
    print("Invalid input. Please enter a whole number.")
