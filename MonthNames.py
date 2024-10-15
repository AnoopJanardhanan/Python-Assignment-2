# Conditional and Looping Statements Assignment

# Exercise 1 Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user
# and prints output the corresponding month of the year. An example run of the program (numbers in bold are typed in by
# the user) Enter the month: 3 Month 3 is March
month_number = int(input("Enter the month: "))
if month_number == 1:
    print("Month 1 is January")
elif month_number == 2:
    print("Month 2 is February")
elif month_number == 3:
    print("Month 3 is March")
elif month_number == 4:
    print("Month 4 is April")
elif month_number == 5:
    print("Month 5 is May")
elif month_number == 6:
    print("Month 6 is June")
elif month_number == 7:
    print("Month 7 is July")
elif month_number == 8:
    print("Month 8 is August")
elif month_number == 9:
    print("Month 9 is September")
elif month_number == 10:
    print("Month 10 is October")
elif month_number == 11:
    print("Month 11 is November")
elif month_number == 12:
    print("Month 12 is December")
else:
    print("Please enter a valid month number between 1 and 12.")
