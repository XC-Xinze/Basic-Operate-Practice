from survey import AnonymousSurvey

question = "what language did first learn to speak?"
language_survey = AnonymousSurvey(question)
language_survey.show_question()
print("Enter q at anytime to quit!")
while True:
    response = input("language:")
    if response == "q":
        break
    language_survey.store_response(response)

print("\nThank you everyone who join this survey.")
language_survey.show_result()
