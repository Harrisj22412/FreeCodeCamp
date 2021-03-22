# Rewrite your pay computation with time-and-a half for overtime and create a function called computepay which takes two parameters(hours and rate)
def computepay(hours, rate):
        print("In computepay", hours, rate)
        if hours > 40 :
            reg = rate * hours
            overTimePay = (hours - 40.0) * (rate* 0.5)
            pay = reg + overTimePay
        else:
            pay = reg * rate
        print('Returning', pay)
        return pay

Hours = input("Enter hours: ")
Rate = input("Enter Rate: ")
floatHour = float(Hours)
floatRate = float(Rate)


overTimePay = computepay(floatHour, floatRate)


print("Pay:", overTimePay)