"""
Ask User for Name
"""
#Start
Name = input("What is your name? ")
OUTPUT_FILE = Name
out_file = open("name.txt", "w")
print("Your name is ", file=out_file)
out_file.close()

#Second Part
in_file = open('name.txt', "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

#Getting Numbers from a document and adding them together
in_file = open('numbers.txt')
Number_1 = int(in_file.readline())
Number_2 = int(in_file.readline())
Sum_Of_Num = Number_1 + Number_2
print(Sum_Of_Num)
in_file.close()

#Helpful Source https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

