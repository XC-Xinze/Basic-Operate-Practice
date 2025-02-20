# test 类
# work with language_survey.py
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.response.append(new_response)

    def show_result(self):
        print("survey results:")
        for response in self.response:
            print(f"-{response}")
