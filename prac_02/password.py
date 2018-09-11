"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input(">> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input(">> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    Count_lower = 0
    Count_upper = 0
    Count_digit = 0
    Count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.isdigit():
            Count_digit += 1
        elif char.islower():
            Count_lower += 1
        elif char.isupper():
            Count_upper += 1
        elif char in SPECIAL_CHARACTERS:
            Count_special += 1

    if Count_lower == 0 or Count_upper == 0 or Count_digit == 0:
        return False
    elif Count_special == 0:
        return True

    if SPECIAL_CHARS_REQUIRED == 0:
        if Count_special == 0:
            return True

    return True


main()
