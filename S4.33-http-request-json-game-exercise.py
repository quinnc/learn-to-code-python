import requests
import random
import json


# https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple
# https://opentdb.com/api.php?amount=1

print ("Welcome to the Open Trivia Game")

quitgame = False

QUESTIONS = "results"
QUESTION = "question"
CORRECT = "correct_answer"
INCORRECT = "incorrect_answers"

correct_answers = 0
incorrect_answers = 0


while (not quitgame):
    print ("-0-0-0-0-0-0-0-0-0-0-0-")
    print ("Next question:")
    r = requests.get("https://opentdb.com/api.php?amount=1")
    if (r.status_code != 200):
        print ("Retrieving question failed. Exiting")
        break

    response = json.loads(r.text)
    print (response[QUESTIONS][0][QUESTION])
    print ("Type one of:")

    num_answers = len(response[QUESTIONS][0][INCORRECT])+1
    loc_correct_answer = random.randint(0, num_answers)
    curr_incorrect_idx = 0

    for x in range(num_answers):
        if (x == loc_correct_answer):
            print (response[QUESTIONS][0][CORRECT])
        else:
            print (response[QUESTIONS][0][INCORRECT][curr_incorrect_idx])
            curr_incorrect_idx += 1

    answer = input("? ")

    if (answer.lower() == response[QUESTIONS][0][CORRECT].lower()):
        print ("That is correct!")
        correct_answers += 1
    else:
        print ("Sorry, that is not the correct answer.")
        print ("The correct answer is '", response[QUESTIONS][0][CORRECT], "'.")
        incorrect_answers += 1

    continue_text = input ("Type 'quit' to end the game. ")
    quitgame = continue_text.lower() == 'quit'


print ("-0-0-0-0-0-0-0-0-0-0-0-")
print ("")
print ("Final score:", correct_answers, "/", correct_answers + incorrect_answers)
                   
