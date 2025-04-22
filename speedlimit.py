biker1 = int(input("What is the speed of the first biker:"))
biker2 = int(input("What is the speed of the second biker:"))
biker3 = int(input("What is the speed of the third biker:"))
average = (biker1+biker2+biker3)/3
if biker1 < average:
    print("Biker 1 was going", (biker1-average), "below the speed limit.")

if biker2 < average:
    print("Biker 2 was going", (biker2-average), "below the speed limit.")

if biker3 < average:
    print("Biker 3 was going", (biker3-average), "below the speed limit.")