from pydantic import BaseModel

class ChatRequest(BaseModel):
    sesson_id: str
    message: str

class ChatResponse(BaseModel):
    response: str


