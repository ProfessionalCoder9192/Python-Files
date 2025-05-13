num = int(input("Enter a number: "))
num = abs(num)

if num == 0:
    digit_count = 1
else:
    digit_count = 0
    while num > 0:
        num = num // 10
        digit_count += 1

print("Number of digits:", digit_count)
