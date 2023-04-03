from app.services.openai import openai


def generateResponse():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="This is a test. Respond with a funny joke about how bad a developer I am.",
        temperature=0.6,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )
    return ''.join([choice.text for choice in response.choices])
