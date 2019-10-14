# Name: Iman Durrani
# Directory ID: idurrani
# Date: 9-25-19
# Title: Module 5 Exercise

def compute_pay(hours, rate):
    if rate < 15 :
        return None
    elif hours >= 40:
        overRate = rate * 1.5
        overHours = hours - 40
        pay = overRate * overHours + rate * 40 
        return pay
    else:
        pay = hours * rate
        return pay

print(compute_pay(50, 15))
