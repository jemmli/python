import random

number = random.randrange(1, 10)
i = 1
while i == 1:

    user_number = int(input("Give me a number from 1-10 "))

    if isinstance(user_number, str):
        print("Stop messing around")
        break
    print("The number is ", number)

if user_number == number:
    print("You won")
        

