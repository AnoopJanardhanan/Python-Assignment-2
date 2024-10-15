# Conditional and Looping Statements Assignment

# Exercise 1 in MonthNames file


# Exercise 2 A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half
# price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user) Enter your age: 63 Your ticket costs £2.00.
age = int(input("Enter your age: "))
full_price = 6.00
if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price
print(f"Your ticket costs £{ticket_price:.2}")


# Exercise 3 in BodyMassIndex file


# Exercise 4 Write a Python program to receive 3 numbers from the user and print the greatest among them.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print("The greatest number is:", greatest)


# Exercise 5 Find the factorial of a given number using loops(note the number is received from the user).
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(f"The factorial of {number} is: {factorial}")


# Exercise 6 Reverse a number using while loop.
number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("The reversed number is:", reversed_number)


# Exercise 7 Finding the multiples of a number using loop.
number = int(input("Enter a number: "))
count = int(input("How many multiples do you want to find? "))
print(f"Multiples of {number} are:")
for i in range(1, count + 1):
    multiple = number * i
    print(multiple)


# Exercise 8 Write a program to print the inputted value as it is and break the loop if the value is 'done'. Example run
# of the program :hello there hello there :finished finished :done Done.
while True:
    user_input = input("Enter something (type 'done' to finish): ")
    if user_input == 'done':
        print("Done")
        break
    print(user_input)


# Exercise 9 Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of
# the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print
# "FizzBuzz".
for i in range(1, 11):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)


# Exercise 10 Write a program to print the following pattern: 5 4 3 2 1 4 3 2 1 3 2 1 2 1 1.
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
