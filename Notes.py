Money = (int(input("How many dollars do you have?")))
note100 = Money//100
note50 = (Money%100)//50
note20 = ((Money%100)%50)//20
note10 = (((Money%100)%50)%20)//10
print ("$100 notes:", note100)
print ("$50 notes:", note50)
print ("$20 notes:", note20)
print ("$10 notes:", note10)

