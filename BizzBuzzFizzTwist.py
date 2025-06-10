for x in range(21):
    if x % 20 == 0:
        print("Twist")

    elif x % 15 == 0:
        pass
    
    elif x % 5 == 0:
        print("Fizz")

    elif x % 3 == 0:
        print("buzz")

    else:
        print(x)