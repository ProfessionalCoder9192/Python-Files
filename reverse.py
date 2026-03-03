class Reverse:
    def __init__(self, s="s"):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


user_input = input("Enter a word: ")
obj = Reverse(user_input)
print("Reversed string:", obj.reverse_string())
