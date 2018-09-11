"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a valid integer "))
        finished = True
    except ValueError:
        print("Error: Please enter a valid integer to continue.")
print("Valid result is:", result)