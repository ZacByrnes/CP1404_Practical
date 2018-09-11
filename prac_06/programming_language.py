"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
# Return the self values

class ProgrammingLanguage:
    # Defining init
    def __init__(self, name, typing, boolean, year):
        self.name = name
        self.typing = typing
        self.boolean = boolean
        self.year = year
    # Defining String Example: Python, Dynamic Typing, Reflection=True, First appeared in 1991
    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.boolean, self.year)

    def is_dynamic(self):
        # True or False NOTE: WONT TAKE ANY OTHER PARAMETER BUT >>>(SELF)<<<
        return self.typing == "Dynamic"

def start_testing():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]
    print(python)
    #For Loop, Referred to assessment piece.
    print("The dynamically typed languages are:")
    for language in languages:
        #Checks through my is_dynamic program to ensure that it only prints dynamics.
        if language.is_dynamic():
            print(language.name)
start_testing()
