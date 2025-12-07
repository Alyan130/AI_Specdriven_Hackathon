from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse
from chatkit.server import ChatKitServer, ThreadStreamEvent, StreamingResult
from chatkit.models import UserMessageItem, ThreadMetadata
from chatkit.stores import Store # Assuming a simple in-memory store for now
from chatkit.agents import AgentContext, stream_agent_response
from agents import Runner, simple_to_agent_input
from typing import Any, AsyncIterator
import uvicorn

# Import the agent
from src.agent import agent as course_tutor_agent

app = FastAPI()

# Placeholder for data store and attachment store
# In a real application, you would use a persistent store (e.g., PostgresStore)
class InMemoryStore(Store):
    async def get_thread_metadata(self, thread_id: str) -> ThreadMetadata:
        return ThreadMetadata(id=thread_id, externalId=thread_id) # Simplified
    
    async def create_thread(self, thread_id: str, external_id: str) -> ThreadMetadata:
        return ThreadMetadata(id=thread_id, externalId=external_id) # Simplified

    async def add_thread_item(self, thread_id: str, item: UserMessageItem) -> None:
        pass # Not implemented for in-memory example

class MyChatKitServer(ChatKitServer):
    def __init__(self, data_store: Store):
        super().__init__(data_store, attachment_store=None) # No attachment store for now

    async def respond(
        self,
        thread: ThreadMetadata,
        input: UserMessageItem | None,
        context: Any,
    ) -> AsyncIterator[ThreadStreamEvent]:
        agent_context = AgentContext(
            thread=thread,
            store=self.store,
            request_context=context,
        )
        
        # Convert ChatKit input to Agents SDK input
        agent_input = await simple_to_agent_input(input) if input else []

        result = Runner.run_streamed(
            course_tutor_agent, # Our agent instance
            agent_input,
            context=agent_context,
        )
        
        async for event in stream_agent_response(
            agent_context,
            result,
        ):
            yield event

# Initialize the ChatKit server
chatkit_server = MyChatKitServer(InMemoryStore())

@app.post("/api/chatkit")
async def chatkit_endpoint(request: Request):
    # The ChatKit server expects a raw request body for processing
    raw_body = await request.body()
    result = await chatkit_server.process(raw_body, {})
    
    if isinstance(result, StreamingResult):
        return StreamingResponse(result, media_type="text/event-stream")
    else:
        # Fallback for non-streaming results, though ChatKit typically streams
        # Ensure result.json() is called if it's a method
        return Response(content=result.json() if hasattr(result, 'json') and callable(result.json) else str(result), media_type="application/json")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)