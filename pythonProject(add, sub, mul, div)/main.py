#Write Python program to find addition, subtraction, Multiplication,
# and Division of two numbers.
# Ask the user to input two numbers (num1 and num2).
import numpy as np
#Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Preform addition operation
result_add = num1 + num2
print("addition: ", num1, "+", num2, "=", result_add)
#Preform Subtraction operation
result_sub = num1 - num2
print("Subtraction: ", num1, "-", num2, "=", result_sub)
#preform multiplication operation
result_mul = num1 * num2
print("Multiplication: ", num1, "*", num2, "=", result_mul)
#Prefrom Division operation
#Using if statement _div = mum1 / num2 to check if num2 is not zero
if num2 != 0:
    result_div = num1/ num2
    print("Division: ", num1, "/", num2, "=",  result_div)
else:
    print("Cannot divide by zero")


