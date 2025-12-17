import os
from dotenv import load_dotenv
from agents import Agent, tool, Runner,  set_tracing_disabled, set_default_openai_key, OpenAIChatCompletionsModel
from agents import OpenAIProvider
from agents.memory.sqlite_session import SQLiteSession
import os
# Correct import for Qdrant client
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from agents import function_tool
from openai import AsyncOpenAI
import google.generativeai as genai

set_tracing_disabled(disabled=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")


client = AsyncOpenAI(
         api_key=api_key, 
         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
             )

model = OpenAIChatCompletionsModel(
   model = "gemini-2.5-flash",
   openai_client=client
)

qdrant_client_instance = QdrantClient(
    url=os.getenv("QDRAUNT_DB_URL"),
    api_key=os.getenv("QDRAUNT_API_KEY")
)


COLLECTION_NAME = "book"
EMBEDDING_MODEL = "gemini-embedding-001"


def get_embedding(text: str) -> list[float]:
    """Generates an embedding for the given text."""
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="RETRIEVAL_QUERY"
    )
    return response['embedding']

@function_tool
def retrieve_docs(query: str) -> str:
    """
    retrieve_docs: Use this tool to retrieve relevant text chunks from the Qdrant knowledge base based on the user query.

    Args: 
        query (str): The user query.

    Returns: 
        str: The retrieved text chunks.
    """
    query_embedding = get_embedding(query)

    search_result = qdrant_client_instance.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding, 
        limit=3  
    )

    context = ""
    for hit in search_result.points:  
        context += hit.payload["text"] + "\n\n"

    print("Context:", context)
    return context


async def run_agent(session_id:str,user_prompt:str):
 
 
 session = SQLiteSession(session_id=session_id)

 tutor_agent = Agent(
    name="CourseTutor",
    instructions='''
    ## Role:
    You are an expert tutor for a 'Physical AI and Humanoid Robotics' course, asiitng students to provide information.
    
    ## Tool:
    Use the 'retrieve_docs' to find relevant information about course before answering.

    ## Rules:
     - Answer user queries strictly based on the provided course material.
     - Resposnes must be concise , not too long , just upto the point.
     - If you cannot find relevant information, just say we wrking on updating the course.
    ''',
    tools=[retrieve_docs],
    model=model
 )


 response = await Runner.run(  
                       starting_agent=tutor_agent,
                       input=user_prompt,
                       session=session
                       )
 

 return response.final_output

