"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? A value error will occur when a float/ decimal number is entered.
2. When will a ZeroDivisionError occur?  A Zero Division Error will occur when the denominator is set to a value of 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? You can change the code by adding in floats
"""

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

