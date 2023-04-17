from typing import Optional
from fastapi import APIRouter, UploadFile, Depends, HTTPException
from pydantic import BaseModel

from app.services.openai import generate_gpt_response
from app.services.pdf import get_text_from_pdf


# Init FastAPI router for API endpoints
api_routes = APIRouter(prefix="/api")


@api_routes.get('/hello/{name}')
async def get_hello(name: str = 'world'):
    return {"message": "Hello " + name}


class ParseRequest(BaseModel):
    name: Optional[str] = None
    text: Optional[str] = None


@api_routes.post('/new')
async def new_parse_request(request: ParseRequest = Depends(), file: Optional[UploadFile] = None):
    request_fields = request.dict()
    name: Optional[str] = request_fields.get('name')
    resume: Optional[str] = get_text_from_pdf(
        file) or request_fields.get('text')

    error_message: Optional[str] = None
    if name == None:
        error_message = 'Field `name` must be provided'
    if resume == None:
        error_message = 'Either `text` or `file` must be provided'
    if len(resume) > 3000:
        error_message = 'Your resume is too long. The maximum character count is 3000.'

    if error_message:
        raise HTTPException(status_code=400, detail=error_message)

    prompt = f"""
    Request:
    Given the following document, which is a professional resume provided by {name}, summarize the {name}'s work experience.

    Document:
    ### {'resume.txt' if file == None else file.filename} ###

    {resume}
    """

    return await generate_gpt_response(prompt)


@api_routes.get('/joke')
async def get_joke():
    return await generate_gpt_response('Tell me a joke. Include the punchline in your response. Do not wait for additional user input to complete the joke.', 1)
