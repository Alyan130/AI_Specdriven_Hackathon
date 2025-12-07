from pydantic import BaseModel

class ChatRequest(BaseModel):
    thread_id: str
    message: str

class ChatResponse(BaseModel):
    # This will be a streaming response, but for now, we'll define a simple text response
    # The actual ChatKit integration might handle streaming differently
    response: str
