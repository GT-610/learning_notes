from survey import AnonymousSurvey

question="What language did you first learn to speak?"
language_survey=AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' to quit at any time.")
while True:
    response=input("Language: ")
    if response=='q':
        break
    language_survey.store_response(response)

print("\nThank you to everyone who participed in the survey! ")
language_survey.show_results()