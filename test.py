from PyInquirer import prompt
from pprint import pprint


question = [
    { "type": "list",
      "name": "like",
      "message": "do you like",
      "choices": [
      {
     "name":"c1", "value" :1},{"name": "c2", "value": 2}
      ]
    }
]

answer = prompt(question)
pprint(answer)
