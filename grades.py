print("Enter marks obtained in 5 different subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

total = markOne + markTwo + markThree + markFour + markFive
average = total/5

if average>=91 and average<=100:
    print("Your grade is 1A.")
elif average>=81 and average<91:
    print("Your grade is A2")
elif average>=71 and average<81:
    print("Your grade is B1")
elif average>=61 and average<71:
    print("Your grade is B2")
elif average>=51 and average<61:
    print("Your grade is C1")
elif average>=41 and average<51:
    print("Your grade is C2")
elif average>=33 and average<41:
    print("Your grade is D")
elif average>=21 and average<33:
    print("Your grade is E1")
elif average>=0 and average<21:
    print("Your grade is E2")
else:
    print("Invalid input!")