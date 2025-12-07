---
id: 0002
title: Create RAG Chatbot Implementation Plan
stage: plan
date: 2025-12-07
surface: agent
model: gemini-1.5-pro-api
feature: 002-rag-agent
branch: 002-rag-agent
user: user
command: /sp.plan
labels: ["planning", "rag", "agent"]
links:
  spec: specs/002-rag-agent/spec.md
  plan: specs/002-rag-agent/plan.md
  ticket: null
  adr: null
  pr: null
files:
- specs/002-rag-agent/plan.md
tests:
null
---

## Prompt

/sp.plan Project: RAG Chatbot Implementation Plan


Project Manager:
    - Use **uv** as package manager to install dependencies.
    - For now uv is install and virtual envoirnment has been created you just need to run commands to install dependencies in virtual env and use them.
   - Install all the dependencies after activating virual envoirnment first
 **.venv\Scripts\activate**
  - uv uses pyproject.toml for managing dependencies.

Location: Whole projectm ust be implemented inside the /rag-chatbot directory.

We are building a RAG (Retrieval-Augmented Generation) chatbot using Qdrant, the OpenAI Agents SDK, and FastAPI with ChatKit. The LLM will be Gemini 2.5 Flash, and we will use Gemini Embeddings for vectorization.


Context & Documentation Source
Use the Context7 MCP Server to fetch the specific documentation required for each phase. Do not hallucinate library syntax; check the docs first.

Qdrant: read_resource("/qdrant/qdrant-client")

OpenAI Agents SDK: read_resource("/websites/openai_github_io_openai-agents-python")

ChatKit / FastAPI: read_resource("/openai/chatkit-python")

Implementation Phases
Phase 1: Qdrant Setup & Ingestion (The Knowledge Base)
Goal: Create a script to ingest content.md into a vector database.

Dependencies: Install qdrant-client, python-dotenv, and google-generativeai (for embeddings).

Environment: Load QDRAUNT_API_KEY and QDRAUNT_DB_URL from .env.

Embedding Setup:

Configure the embedding model using google-generativeai.

Model: Use models/text-embedding-004 (or embedding-001 if preferred).

Ingestion Script:

Create a script (e.g., ingest.py).

Read content.md.

Chunk the text appropriately.

Generate embeddings for chunks.

Upsert points into Qdrant collection named book.

Phase 2: Agent Development (The Brain)
Goal: Build an agent using the OpenAI Agents SDK that uses Gemini as the LLM.

Dependencies: Install the openai-agents-sdk (check exact package name via MCP docs).

Model Configuration:

The agent must use Google Gemini 2.5 Flash as its core LLM.

Retrieve GOOGLE_API_KEY from .env.

Note: Ensure the Agent SDK is configured to accept a Gemini client or compatible adapter.

Tool Creation:

Create a Python tool function: retrieve_docs(query: str).

This tool should embed the query (using the same Gemini embedding model from Phase 1) and search the Qdrant book collection.

Return the relevant text chunks to the agent.

Agent Definition:

Define the agent with instructions to answer questions based strictly on the retrieved context.

Phase 3: Backend API (The Interface)
Goal: Serve the agent via a robust API using FastAPI and ChatKit.

Dependencies: Install fastapi, uvcorn, and the chatkit server library.

Integration:

Use the ChatKit integration patterns (fetch docs via ID /openai/chatkit-python).

Set up a FastAPI app (main.py) running with Uvcorn.

Features:

Threads: Handle conversation threads/persistence.

Streaming: Ensure the UI receives streaming responses from the agent.

Structured Output: Use Pydantic models for all API requests/responses.

Testing: Ensure the API is functional and can handle concurrent requests.


How to execute:
Start by creating the folder structure.

Crucial: Before writing code for Qdrant, Agents, or ChatKit, call the Context7 MCP server with the respective library IDs listed above to understand the correct API methods.

Prioritize clean, modular code.

**FOR NOW ONLY CREATE PALN DONT IMPLEMENT**

## Response snapshot

Created the implementation plan for the RAG chatbot in `specs/002-rag-agent/plan.md`.

## Outcome

- ✅ Impact: Created a detailed implementation plan for the RAG chatbot.
- 🧪 Tests: No automated tests were run for this stage.
- 📁 Files: Created `specs/002-rag-agent/plan.md`.
- 🔁 Next prompts: The next step is to proceed with `/sp.tasks`.
- 🧠 Reflection: The user's detailed prompt allowed for the creation of a comprehensive plan without a research phase.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not applicable.
- Prompt variant (if applicable): Not applicable.
- Next experiment (smallest change to try): Not applicable.
