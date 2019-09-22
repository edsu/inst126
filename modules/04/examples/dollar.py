# jaylin

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if (rate >= 15):
     pay=(hours* rate)
     print("Pay: $", pay)
else:  
     print("I'm sorry " + str(rate) + " is lower than the minimum wage!")  
    
    
