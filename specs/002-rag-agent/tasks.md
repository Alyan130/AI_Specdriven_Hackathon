# Tasks: RAG Chatbot

**Branch**: `002-rag-agent` | **Spec**: [specs/002-rag-agent/spec.md](spec.md) | **Plan**: [specs/002-rag-agent/plan.md](plan.md)

This task list is generated from the implementation plan and feature specification.

## Phase 1: Setup

- [X] T001 Create the directory structure inside `rag-chatbot/`.
- [X] T002 Initialize the `pyproject.toml` file in `rag-chatbot/`.
- [X] T003 Activate the virtual environment: `.venv\Scripts\activate`. (Note: As each command runs in a new shell, subsequent commands will be prefixed with the activation command)
- [ ] T004 Install initial dependencies using uv: `uv pip install qdrant-client python-dotenv google-generativeai openai-agents-sdk fastapi uvicorn chatkit`.

## Phase 2: Foundational (Ingestion)
- [X] T005 Create the `.env` file in `rag-chatbot/` with `QDRAUNT_API_KEY`, `QDRAUNT_DB_URL`, and `GOOGLE_API_KEY`. Just refer them using os.getenv actual variables will be loaded automatically.

- [ ] T006 Fetch Context7 MCP Docs for Qdrant: `/qdrant/qdrant-client`.
- [X] T007 Create the `ingest.py` script in `rag-chatbot/`.
- [X] T008 Implement the logic in `ingest.py` to read `content.md`, chunk the text, generate embeddings using `google-generativeai` with `gemini-embedding-001` model and upsert the data into the Qdrant `book` collection.

## Phase 3: User Story 1 - Student gets answers to course questions

### Goal
As a student, I want to ask questions about the "Physical AI and Humanoid Robotics" course and get answers based on the official course material, so that I can clarify my doubts and deepen my understanding of the subject.

### Independent Test Criteria
The chatbot can be tested by asking a question that is answerable from `content.md` and verifying that the answer is accurate, relevant, and sourced from the document.

### Implementation Tasks

- [X] T009 [US1] Create Pydantic models for API requests and responses in `rag-chatbot/src/models.py`.
- [ ] T010 [US1] Fetch Context7 MCP Docs for OpenAI Agents SDK: `/websites/openai_github_io_openai-agents-python`.
- [X] T011 [US1] Implement the `retrieve_docs` tool in `rag-chatbot/src/tools.py`. This tool will embed the user's query and search the Qdrant `book` collection.
- [X] T012 [US1] Implement the agent in `rag-chatbot/src/agent.py`, configuring it to use Gemini 2.5 Flash and the `retrieve_docs` tool.
- [X] T013 [US1] Fetch Context7 MCP Docs for ChatKit: `/openai/chatkit-python`.
- [X] T014 [US1] Implement the FastAPI application in `rag-chatbot/main.py`, setting up the ChatKit server and the `/api/chatkit` endpoint.

## Dependencies

- User Story 1 is dependent on the completion of Phase 2 (Foundational).

## Parallel Execution

- Within User Story 1, the creation of models (`T009`) can be done in parallel with fetching documentation (`T010`, `T013`).

## Implementation Strategy

The implementation will follow a phased approach:
1.  **Setup and Ingestion**: The foundational data pipeline will be established first.
2.  **MVP (User Story 1)**: The core chatbot functionality will be implemented next, providing a testable end-to-end user experience.
3.  **Polish and Refinement**: Further enhancements and cross-cutting concerns will be addressed after the MVP is complete.
