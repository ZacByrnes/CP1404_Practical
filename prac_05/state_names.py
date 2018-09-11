"""
CP1404/CP5632 Practical - Suggested Solution
State names in a dictionary
File has been reformatted and state inputs can be any case
"""

LIST_OF_NAMES = {"QLD": "Queensland", "NSW": "New South Wales",
                 "NT": "Northern Territory", "WA": "Western Australia",
                 "ACT": "Australian Capital Territory", "VIC": "Victoria",
                 "TAS": "Tasmania"}

state = input("Enter state: ").upper()
while state != "":
    if state in LIST_OF_NAMES:
        print(state + " is " + LIST_OF_NAMES[state])
    else:
        print("Invalid state")
    state = input("Enter state: ").upper()
