# Implementation Plan: RAG Chatbot

**Branch**: `002-rag-agent` | **Date**: 2025-12-07 | **Spec**: [specs/002-rag-agent/spec.md](spec.md)
**Input**: Feature specification from `specs/002-rag-agent/spec.md`

**Note**: This template is filled in by the `/sp.plan` command.

## Summary

The plan is to build a RAG (Retrieval-Augmented Generation) chatbot using Python, FastAPI, Qdrant, and the OpenAI Agents SDK. The chatbot will answer questions about "Physical AI and Humanoid Robotics" based on the provided `content.md` file, serving as an expert tutor for the course.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, Uvicorn, qdrant-client, openai-agents-sdk, google-generativeai, python-dotenv, chatkit
**Storage**: Qdrant (Cloud) for vector storage.
**Testing**: `pytest` for unit and integration tests.
**Target Platform**: Linux server environment.
**Project Type**: Single project located within the `/rag-chatbot` directory.
**Performance Goals**: 90% of in-scope questions should be answered within 5 seconds.
**Constraints**: The agent must exclusively use the provided `content.md` for answers and remember the entire conversation history within a session.
**Scale/Scope**: The system is designed for a single course, using one `content.md` file as its knowledge base.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- The plan adheres to the constitution by using specified technologies and focusing on a single, well-defined feature. No violations detected.

## Project Structure

### Documentation (this feature)

```text
specs/002-rag-agent/
├── plan.md              # This file
├── research.md          # Phase 0 output (skipped, user provided sufficient detail)
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (created by /sp.tasks)
```

### Source Code (repository root)

The implementation will be contained within the `rag-chatbot` directory.

```text
rag-chatbot/
├── .venv/
├── .env
├── content.md
├── ingest.py         # Script for data ingestion into Qdrant
├── main.py           # FastAPI application entry point
├── pyproject.toml    # Project dependencies managed by uv
└── src/
    ├── agent.py      # Agent definition and logic
    ├── models.py     # Pydantic models for API and data
    └── tools.py      # Custom tools for the agent (e.g., Qdrant search)
```

**Structure Decision**: A single project structure is chosen as the feature is self-contained within the `rag-chatbot` directory. This keeps the implementation focused and easy to manage.

## Phase 0: Outline & Research

The user prompt provided sufficient technical detail and library choices, so no research phase is required.

## Phase 1: Design & Contracts

### Data Model (`data-model.md`)

-   **`DocumentChunk`**:
    -   `id`: `UUID` - Unique identifier for the chunk.
    -   `text`: `string` - The text content of the document chunk.
    -   `embedding`: `vector` - The vector embedding of the text.
    -   `source`: `string` - The source of the document (e.g., `content.md`).

### API Contracts (`contracts/openapi.json`)

-   **Endpoint**: `/api/chatkit`
-   **Method**: `POST`
-   **Request Body**:
    ```json
    {
      "thread_id": "string",
      "message": "string"
    }
    ```
-   **Response**: A streaming response with server-sent events.

### Quickstart Guide (`quickstart.md`)

1.  **Setup**:
    -   Create a `.env` file in the `rag-chatbot` directory with the following variables:
        ```
        QDRAUNT_API_KEY=...
        QDRAUNT_DB_URL=...
        GOOGLE_API_KEY=...
        ```
    -   Install dependencies: `uv pip install -r requirements.txt`
2.  **Ingestion**:
    -   Run the ingestion script: `python ingest.py`
3.  **Run the application**:
    -   Start the FastAPI server: `uvicorn main:app --reload`