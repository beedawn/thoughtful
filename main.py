import json


with open ('data.json', 'r') as file:
    data = json.load(file)
    while (True):
        found = False
        user_question = input("Enter your question (Enter 'q' to quit):\n")

        if user_question.lower() == "q":
            break
        for question in data['questions']:
            if question['question'].lower() == user_question.lower():
                print(question['answer'])
                found = True

        if not found:
            print("Sorry, I didn't get that, please try again.\n")

