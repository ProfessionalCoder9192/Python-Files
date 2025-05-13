num = int(input("Enter a number that you want to use:"))
t = num
numLength = 0

while t>0:
    numLength = numLength + 1
    t = int(t/10)

if numLength>=4:
    numLength = int(numLength/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk==(numLength-1):
            midOne = rem
        elif chk==(numLength-1):
            midTwo = rem
        num = int(num/10)
        chk=chk+1
    product = midOne * midTwo
    print ("\nProduct of the middle digits" (" +str(midOne)+ "*" +str(midTwo)+ "))

else:
    print("\nThis number needs to be 4 or more digits.")