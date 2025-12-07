---
id: 0001
title: Create Physical AI & Humanoid Robotics RAG Agent Specification
stage: spec
date: 2025-12-07
surface: agent
model: gemini-1.5-pro-api
feature: 002-rag-agent
branch: 002-rag-agent
user: user
command: /sp.specify
labels: ["specification", "rag", "agent"]
links:
  spec: specs/002-rag-agent/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/002-rag-agent/spec.md
- specs/002-rag-agent/checklists/requirements.md
tests:
null
---

## Prompt

**Project Title:** Physical AI & Humanoid Robotics RAG Agent **Domain:** The chatbot serves as an expert tutor for a "Physical AI and Humanoid Robotics" course, answering user queries based strictly on the provided `content.md` located at the project root. **Technical Stack & Architecture:** Please specify the following components in the technical design: 0. **Language**: Implement everyting in python. 1. **Backend & API:** - **FastAPI** running on **Uvicorn**. - Must implement **OpenAI ChatKit** integration (using `ChatKitServer`) to handle thread management and UI streaming. - Expose a POST endpoint (e.g., `/api/chatkit`) for the frontend. 2. **Agent Orchestration:** - Use **OpenAI Agents SDK** to define the agent behaviors and tools. - **Crucial:** The agent must be configured to use **Google Gemini 2.5 Flash** as the LLM, utilizing the OpenAI-compatibility client structure (injecting `base_url` and Google API key). 3. **Knowledge Base (RAG):** - **Vector Database:** Qdrant (Cloud). - **Embeddings:** Google `gemini-embedding-001`. - **Dimensionality:** 3072 dimensions. - **Ingestion:** A script to chunk `content.md`, generate embeddings, and upsert to Qdrant. 4. **Agent Tools:** - Create a custom function tool (e.g., `query_knowledge_base`) that the Agent calls to retrieve relevant chunks from Qdrant before answer 5. **Project Manager**: - Use **uv** as package manager to install dependencies. - For now uv is install and virtual envoirnemnt has been created you just need to run commands to install dependencies in virtual env and use them. ## Note: - Now write spec in 002-rag-agent , dont delete anything

## Response snapshot

Created the feature specification for 'Physical AI & Humanoid Robotics RAG Agent' in `specs/002-rag-agent/spec.md` and a corresponding checklist in `specs/002-rag-agent/checklists/requirements.md`. Clarified conversational memory length with the user and updated the spec. Committed changes to branch `002-rag-agent`.

## Outcome

- ✅ Impact: Created a clear and concise feature specification for the RAG agent.
- 🧪 Tests: No automated tests were run for this stage.
- 📁 Files: Created `specs/002-rag-agent/spec.md` and `specs/002-rag-agent/checklists/requirements.md`.
- 🔁 Next prompts: The next step is to proceed with `/sp.plan`.
- 🧠 Reflection: Faced issues with script execution due to argument parsing in PowerShell, leading to manual creation of branch and spec file. This highlights the need for robust script argument handling or alternative execution methods.

## Evaluation notes (flywheel)

- Failure modes observed: PowerShell script argument parsing issues.
- Graders run and results (PASS/FAIL): Not applicable.
- Prompt variant (if applicable): Not applicable.
- Next experiment (smallest change to try): Investigate PowerShell argument parsing for long strings and special characters in the `run_shell_command` context.