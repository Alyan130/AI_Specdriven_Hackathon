import os
from dotenv import load_dotenv
from agents import Agent, tool, Runner,  set_tracing_disabled, set_default_openai_key
from agents import OpenAIProvider
from .tools import retrieve_docs 
from agents.memory.sqlite_session import SQLiteSession

set_tracing_disabled(disabled=True)


load_dotenv()
set_default_openai_key(key = os.getenv("OPENAI_API_KEY"))

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
    tools=[retrieve_docs]
 )


 response = await Runner.run(  
                       starting_agent=tutor_agent,
                       input=user_prompt,
                       session=session
                       )
 return response.final_output

