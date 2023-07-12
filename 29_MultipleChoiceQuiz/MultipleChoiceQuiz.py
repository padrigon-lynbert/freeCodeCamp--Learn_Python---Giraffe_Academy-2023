import os
from Question import Question


questionPrompts = [
    "What color are apples? \n(a) red/green \n(b) purple \n(c) orange\n\n",
    "What color are bananas? \n(a) teal \n(b) magenta \n(c) yellow\n\n",
    "What color are strawberries \n(a) yellow \n(b)red \n(c) blue\n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b")   
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer: score +=1
    os.system('cls'); print("you got "+ str(score) + "/" + str(len(questions)))

run_test(questions)
