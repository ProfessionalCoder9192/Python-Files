N1 = int(input("What is the numerator:"))
N2 = int(input("What is the denominator:"))
if N1%N2==0:
    print("\n" + str(N1)+ " is divisible by " +str(N2))
else:
    print("\n" + str(N1)+ " is not divisible by " +str(N2))