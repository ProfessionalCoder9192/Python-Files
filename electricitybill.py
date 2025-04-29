units = int(input("What is the ammount of Units you've consumned in the last year?:"))

if(units<50):
    ammount = units*2.60
    tax = 25

elif (units<=100):
    ammount = 130 + ((units-50)*3.25)
    tax = 35

elif (units<=200):
    ammount = 130 + 162.50 + ((units-100)*5.26)
    tax = 45

else:
    ammount = 130 + 162.50 + 526 + ((units-200)*8.45)
    tax = 75
total = ammount + tax
print ("\nElectricityBill = %.2f" %total)
