import json


with open ('data.json', 'r') as file:
    data = json.load(file)
    cont = True
    while (cont is not False):
        found = False
        user_question = input("Enter your question (Enter 'q' to quit):\n")

        if user_question.lower() == "q":
            cont = False
            break
        for question in data['questions']:
            if question['question'] == user_question:
                print(question['answer'])
                found = True

        if not found:
            print("Sorry, I didn't get that, please try again.\n")

