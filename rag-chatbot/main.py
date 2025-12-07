from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.agent import run_agent
from src.models import ChatRequest, ChatResponse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/chat-agent",response_model=ChatResponse)
async def chat_agent(chat_request: ChatRequest):
     try:
      result =  await run_agent(chat_request.sesson_id,chat_request.message)
      return {"response": result}
     except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
     


