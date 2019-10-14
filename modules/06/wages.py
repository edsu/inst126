# I need to repeat until I get a wage that is greater than
# or equal to minimum wage.

# I need a function that computes the pay using the hours
# and the rate of pay

def compute_pay(hours, rate):
    if rate < 15:
        return None
    else:
        return hours * rate

while True:
    hours = float(input("hours: "))
    rate = float(input("rate: "))
    pay = compute_pay(hours, rate)

    if pay == None:
        print("That rate is lower than minimum wage!")
    else:
        print("Pay: " + str(pay))
        break



# I need to print out the pay using my function.