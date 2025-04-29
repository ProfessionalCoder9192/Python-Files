medical_cause = input("Do you have a medical cause? yes or no:")
attendence = int(input("What is your attendence percentage?:"))
if medical_cause == "yes":
    print ("You can take the test.")
else:
    if attendence > 75:
        print("You can take the test.")
    else:
        print("Sorry, you aren't eligible for this test.")
