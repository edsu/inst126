# Antonio

# Prompt and gather user input
hrs = input("Enter hours: ")
hrsRate = input("Enter rate: ")

# Convert hours and hourly rate to float
newHr = float(hrs); newRt = float(hrsRate)
minWage = 17.50

# Pay ONLY calculated if hourly rate >= minWage; Otherwise error string is printed
if newRt >= minWage:
    # Multiply hour and hourly rate
    ratePay = newHr * newRt

    # Convert the ratePay to String; Creates new string that combines "$" and ratePay
    convertRt = str(ratePay)
    rtString = "$" + convertRt

    # Final result
    print("Pay:", rtString, "\n")
else:
    print("I'm sorry", hrsRate, "is lower than the minimum wage " + str(minWage))
