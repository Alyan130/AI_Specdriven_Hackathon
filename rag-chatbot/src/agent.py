import os
import google.generativeai as genai
from dotenv import load_dotenv
from agents import Agent, tool
from agents.llm import LLM # Base LLM class
from .tools import retrieve_docs # Import the tool

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiLLM(LLM):
    def __init__(self, model_name: str = "gemini-2.5-flash", **kwargs):
        super().__init__(**kwargs)
        self.model_name = model_name
        self._model = genai.GenerativeModel(self.model_name)
        # Store tools passed to the LLM for potential use in generate_content_async
        self.tools_configured = kwargs.get("tools", []) # Expects a list of tool objects

    async def chat_completion(self, messages: list, functions: list = None, **kwargs):
        gemini_messages = []
        for msg in messages:
            if msg["role"] == "user":
                gemini_messages.append({"role": "user", "parts": [{"text": msg["content"]}]})
            elif msg["role"] == "assistant":
                gemini_messages.append({"role": "model", "parts": [{"text": msg["content"]}]})
            # TODO: Handle other roles (system, tool) and complex message parts for Gemini API compatibility

        gemini_tools_declarations = [t.tool_declaration() for t in self.tools_configured] if self.tools_configured else None

        response = await self._model.generate_content_async(
            gemini_messages,
            tools=gemini_tools_declarations,
            # Additional parameters like temperature, top_p etc. can be passed via kwargs
            **kwargs
        )

        text_response = ""
        tool_calls = []

        if response.candidates and response.candidates[0].content:
            for part in response.candidates[0].content.parts:
                if hasattr(part, "text"):
                    text_response += part.text
                elif hasattr(part, "function_call"):
                    tool_calls.append({
                        "id": "call_id_placeholder", # Agents SDK might need an ID
                        "function": {
                            "name": part.function_call.name,
                            "arguments": dict(part.function_call.args)
                        }
                    })

        message_content = {"role": "assistant"}
        if tool_calls:
            message_content["tool_calls"] = tool_calls
            if text_response:
                message_content["content"] = text_response # Can have text alongside tool calls
        else:
            message_content["content"] = text_response

        return {"choices": [{"message": message_content}]}


# Define the agent
agent = Agent(
    name="CourseTutor",
    instructions="You are an expert tutor for a 'Physical AI and Humanoid Robotics' course. "
                 "Answer user queries strictly based on the provided course material. "
                 "Use the 'retrieve_docs' tool to find relevant information before answering. "
                 "If you cannot find relevant information, state that you cannot answer the question from the provided material.",
    llm=GeminiLLM(tools=[retrieve_docs]), # Pass the tool as a list to the LLM for function calling definition
    tools=[retrieve_docs],
    # The agents SDK handles conversational memory within a session inherently.
    # For cross-session persistence, explicit session management (e.g., SQLAlchemySession) would be needed.
)
