# Part#1
# Write a program that calculate
# the total amount of a meal purchased at a restaurant.
# Ask the user to enter the charge for the food,
# then calculate the amount with an 18% tip and 7% sales tax.
# Display each of amounts and total price.
charge = float(input("Enter the amount you were charged: "))
tip = charge * .18
tax = charge * .07
print("charge for the food: %.2f" % charge)
print("the tip amount:%.2f" %tip)
print("tax amount: %.2f" %tax)
print("total amount: %.2f" %(charge + tax))
# Part#2
# Write a Python program to solve a clock time
# using 24-hours clock ( 11 is 11am, 23 is 11pm, and 0 is midnight)
# Ask the user for the time now (in hours)and
# then ask for number of hours to wait for alarm.
# Ask the user for the current time in hours
current_time = int(input("Enter the current time (in hours): "))
# Ask the user number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for alarm: "))
# calculate the time when the alarm go off
alarm_time = (current_time + hours_to_wait)%24
print(f"the alarm will go off at {alarm_time}=0 (24-hours clock): ")