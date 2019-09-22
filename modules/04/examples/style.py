# Joel

hours = input("Enter hours: " )
rate = input("Enter rate: ")

if float(rate) < 15:
    print("Im sorry " + rate + " is lower than the minimum wage!")
else:
    pay = float(hours) * float(rate)
    print("Pay:" + str(pay))
