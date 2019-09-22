# Edward

Hours_Worked = float (input ('Enter hours worked: '))
if Hours_Worked == 0:
    print ("Go to work!")
elif Hours_Worked > 6000:
    print ("take a break!")
else:
    Hourly_Rate = float (input ('Enter hourly rate: '))
    if Hourly_Rate < 15:
        print ("I'm sorry",Hourly_Rate, "is lower than the minimum wage!")
    else:
        print ("Pay: ",Hours_Worked*Hourly_Rate)
