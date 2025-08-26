def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True


r = (7, 0, 3, 0, 7)

if(palind(r)):
    print("The sequence of numbers is a plaindrome!")
else:
    print("This sequence of numbers is not a palindrome.")