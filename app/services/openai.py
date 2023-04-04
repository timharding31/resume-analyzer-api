from os import environ
from dotenv import dotenv_values

import openai


def get_env_var(key: str) -> str:
    return dict(environ).get(key) or dotenv_values('.env').get(key)


openai.organization = get_env_var('OPENAI_ORG_ID')
openai.api_key = get_env_var('OPENAI_API_KEY')


async def generateResponse(prompt: str, temperature: float = 0.2) -> str:
    response = await openai.Completion.acreate(
        model='text-davinci-003',
        prompt=prompt,
        temperature=temperature,
        max_tokens=128,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text
