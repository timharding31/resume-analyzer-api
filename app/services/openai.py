from os import environ
from dotenv import dotenv_values

from fastapi import HTTPException
import openai


def get_env_var(key: str) -> str:
    return dict(environ).get(key) or dotenv_values('.env').get(key)


openai.organization = get_env_var('OPENAI_ORG_ID')
openai.api_key = get_env_var('OPENAI_API_KEY')


async def generate_gpt_response(prompt: str, temperature: float = 0.2) -> str:
    try:
        response = await openai.Completion.acreate(
            model='text-davinci-003',
            prompt=prompt,
            temperature=temperature,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text

    except openai.error.APIError as e:
        raise HTTPException(
            status_code=500, detail=f"OpenAI API returned an API Error: {e}")

    except openai.error.APIConnectionError as e:
        raise HTTPException(
            status_code=401, detail=f"Failed to connect to OpenAI API: {e}")

    except openai.error.RateLimitError as e:
        raise HTTPException(
            status_code=429, detail=f"OpenAI API request exceeded rate limit: {e}")

    except openai.error.InvalidRequestError as e:
        raise HTTPException(
            status_code=400, detail=f"OpenAI API invalid request: {e}")
