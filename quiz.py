QUESTIONS = [
    ("What is the brainrot word used to refer to a gigantic butt?", "gyat" or "Gyat"),
    ("What term is used by a big back taking a portion of your food?", "Fanum Tax" or "Fanum tax" or "fanum tax")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print(f"You're right It was {correct_answer}.")
    else:
        print(f"The answer is {correct_answer}, not {answer}")
# make it take alternatives