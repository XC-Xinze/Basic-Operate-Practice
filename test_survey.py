from survey import AnonymousSurvey


def test_survey():
    question = "What language?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("l")
    assert "l" in language_survey.response
