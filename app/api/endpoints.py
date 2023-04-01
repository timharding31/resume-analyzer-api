from fastapi import APIRouter, UploadFile, File, Depends
from pydantic import BaseModel


# Init FastAPI router for API endpoints
api_routes = APIRouter(prefix="/api")

@api_routes.get('/hello/{name}')
async def get_hello(name: str = 'world'):
    return {"message": "Hello " + name}

class ParseRequest(BaseModel):
    name: str

@api_routes.post('/new')
async def new_parse_request(request: ParseRequest = Depends(), file: UploadFile = File(...)):
    name = request.dict().get('name')
    return { "filename": file.filename + ', uploaded by ' + name }
