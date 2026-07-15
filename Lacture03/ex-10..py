hour_worked = int(input("Please enter the number of hours worked: "))
hour_payrate = float(input("Please enter your hour_payrate: "))
income = hour_worked * hour_payrate

if hour_worked > 40:
    income = income + (hour_worked - 40) * (hour_payrate * 0.5)

print("Your gross pay is: ", income)