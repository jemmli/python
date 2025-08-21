#ctrl + ` to open a new terminal
import random

if 5 > 2:
    print("Five is greater than two!\n")
    print("Five is greater than two!")

fruits = ["apples", "bananas", "cherries"]
x, y, z = fruits
print(x, y, z)

x = "sucks"

def pythonsucks():
    print("Python " + x)

pythonsucks()
"""
i = 1
while i == 1:
    num = random.randrange(1, 10)
    user_number = input("Give me a number from 1-10 (): ")
    
    if isinstance(user_number, str) or user_number > 10 or user_number < 1:
        print("Give me a valid input not words")
    if user_number == num:
        print("You're a really lucky guy. Your number equaled the number I chose.")
        balance = 0
        total = balance + 10
        print("The money you have right now is $", total)
        break
    else:
        stopper = input("You unlucky lil bro, press enter to try again or type anything else to stop")
        if stopper == "stop":
            print("You're done")
            break
        else:
            break

"""