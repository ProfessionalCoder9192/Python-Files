num = int(input("Give any number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("The number is an armstrong number.")
else:
    print("This number is NOT an armstrong number.")
