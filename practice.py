"""
This is a multi-line comment
"""

day = int(input("Give me a number between 1-5: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case _:
        print("Idk what day it is")