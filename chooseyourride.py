print("Choose one of the options below:")
print("1. Bike")
print("2. Car")
vehicle = int(input("Choose one of the above numerically:"))

if (vehicle == 1):
    print("Which type of bike?")
    print ("1. Scooty\n")
    print ("2. Scooter\n")
    choice2 = int(input("Choose one of the bikes above numerically:"))
    if (choice2 == 1):
        print("You have selected Scooty.")
    else:
        print ("You have selected Scooter.")
if (vehicle == 2):
    print("Which type of car?:")
    print ("1. Sedan")
    print ("2. BMW")
    choice3 = int(input("Choose one of the cars above numerically:"))
    if (choice3 == 1):
        print("You have selected Sedan.")
    else:
        print("You have chosen BMW")



    