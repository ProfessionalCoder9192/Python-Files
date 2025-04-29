def is_letter_in_alphabet(char):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return char in alphabet


user_input = input("Enter a character: ")

if is_letter_in_alphabet(user_input):
    print(user_input, "is a letter in the alphabet.")
else:
    print(user_input, "is NOT a letter in the alphabet.")