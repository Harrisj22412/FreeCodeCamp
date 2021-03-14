# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program . The following shows  two executions of the program:

hour = input('Enter Hours:')
rate = input("Enter Rate:")
floatingPointRate = float(rate)
floatingHourRate = float(hour)
try:
    floatingHourRate =float(hour)
    floatingPointRate = float(rate)
except:
    print('Error, please enter numeric input')

#print(floatingHourRate, floatingPointRate)

print(floatingPointRate, floatingHourRate)
if floatingHourRate> 40:
    
    reg = floatingHourRate * floatingPointRate
    overtimePay = (floatingHourRate - 40.0) * (floatingHourRate * 0.5)
    extraPay = reg + overtimePay
else:
    payroll = floatingPointRate * floatingHourRate
print("Pay:", payroll) 