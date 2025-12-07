import os
import google.generativeai as genai
from dotenv import load_dotenv
from agents import Agent, tool
from agents.extensions.models.litellm_model import LitellmModel # Import LitellmModel
from .tools import retrieve_docs # Import the tool

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the agent
agent = Agent(
    name="CourseTutor",
    instructions="You are an expert tutor for a 'Physical AI and Humanoid Robotics' course. "
                 "Answer user queries strictly based on the provided course material. "
                 "Use the 'retrieve_docs' tool to find relevant information before answering. "
                 "If you cannot find relevant information, state that you cannot answer the question from the provided material.",
    llm=LitellmModel(
        model="gemini/gemini-2.5-flash", # Use the LiteLLM model string for Gemini
        api_key=os.getenv("GOOGLE_API_KEY")
    ),
    tools=[retrieve_docs],
    # The agents SDK handles conversational memory within a session inherently.
    # For cross-session persistence, explicit session management (e.g., SQLAlchemySession) would be needed.
)
