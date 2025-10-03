import requests

import json


# https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple

"""
{
  "response_code": 0,
  "results": [
    {
      "type": "multiple",
      "difficulty": "easy",
      "category": "Entertainment: Music",
      "question": "According to a song by Belinda Carlisle, Heaven is a place on what?",
      "correct_answer": "Earth",
      "incorrect_answers": [
        "Venus",
        "Mars",
        "Uranus"
      ]
    }
  ]
}
"""

r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
print (r.status_code)
print ("-=-------------------")
print (r.text)
print ("------------------")
print (type(r.text))

question = json.loads(r.text)
print (type(question))

cat = question['results'][0]['category']


person = {'Name': 'John', 'Age': 30 }
person_json = json.dumps(person)

print ("Person type after dumps: ", type(person_json))

