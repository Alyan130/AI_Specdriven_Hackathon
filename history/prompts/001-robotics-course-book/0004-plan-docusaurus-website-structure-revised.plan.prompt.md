---
id: 0004
title: Plan Docusaurus Website Structure (Revised)
stage: plan
date: 2025-12-06
surface: agent
model: gemini
feature: 001-robotics-course-book
branch: 001-robotics-course-book
user: user
command: |
  /sp.plan # System Prompt: Docusaurus Documentation Website Builder

  ## Role Definition
  You are a technical documentation specialist creating a structured learning platform using Docusaurus. Your task is to build a four-module educational website with clear navigation and visual diagrams based on actual Docusaurus documentation.

  ---

  ## Planning Phase

  ### **Step 1: Research & Analysis**
  1. **Connect to Context7 MCP Server**
     - Fetch Docusaurus docs with this library : /websites/docusaurus_io
     - Fetch Docusaurus official documentation
     - Understand available features, structure, and best practices

  2. **Analyze Book Content**
     - Read `content.md` file at root level
     - Identify main topics and themes
     - Determine logical groupings for 4 modules
     - In the planning phase, you only ANALYZE the content from `content.md` and Docusaurus documentation, then CREATE a proposed module/chapter structure plan. You do NOT write any actual module content or chapter markdown files until the plan is approved.

  3. **Create Module Structure Plan**
     - Based on Docusaurus capabilities + book content
     - Design 4 modules with clear learning progression
     - Define chapters per module (2-4 chapters each)
     - Map content from `content.md` to appropriate modules/chapters

  ---

  ## Module Planning Requirements

  ### **Analysis Checklist**
  - [ ] Review Docusaurus documentation structure
  - [ ] Read complete `content.md` content
  - [ ] Identify 4 main topic areas
  - [ ] Create logical content hierarchy
  - [ ] Plan chapter breakdown per module
  - [ ] Determine which diagrams are needed
  - [ ] Map Docusaurus features to content needs

  ---

  ## Output: Module Plan Document

  After research, create a detailed plan including:

  ### **1. Module Breakdown**
  ```
  Module 1: [Title]
  ├── Overview: [Brief description]
  ├── Chapter 1: [Topic]
  ├── Chapter 2: [Topic]
  └── Chapter 3: [Topic]

  Module 2: [Title]
  ├── Overview: [Brief description]
  ├── Chapter 1: [Topic]
  └── Chapter 2: [Topic]

  Module 3: [Title]
  ├── Overview: [Brief description]
  ├── Chapter 1: [Topic]
  └── Chapter 2: [Topic]

  Module 4: [Title]
  ├── Overview: [Brief description]
  ├── Chapter 1: [Topic]
  └── Chapter 2: [Topic]
  ```

  ### **2. Content Mapping**
  - Which sections from `content.md` go to which module/chapter
  - Learning flow and progression logic
  - Cross-references between modules

  ### **3. Docusaurus Features to Use**
  - Navigation structure
  - Sidebar configuration
  - Special components (tabs, admonitions, code blocks)
  - Plugin requirements

  ### **4. Diagram Requirements**
  - List essential diagrams needed
  - Which modules/chapters need visual aids
  - Diagram types (flowcharts, architecture, etc.)

  ---

  ## Architecture Overview

  ### **Navigation Structure**
  1. **Homepage**: Display 4 module cards with links to respective module pages
  2. **Sidebar**: 
     - Root level: Shows all 4 modules
     - Module level: Shows module overview + chapter list
  3. **Module Page**: Displays module overview with sidebar showing chapters
  4. **Chapter Page**: Displays chapter content when sidebar item clicked

  ### **User Flow**
  ```
  Homepage → Click Module Card → Module Overview Page → Click Chapter (Sidebar) → Chapter Content
  ```

  ---

  ## Implementation Requirements

  ### **1. Content Generation**
  - **Source**: Context7 MCP server with library ID `/websites/docusaurus_io`
  - **Content Source**: `content.md` file at root level
  - **Scope**: Fetch only Docusaurus official documentation for structure guidance
  - **Format**: Write all content as Markdown files

  ### **2. Visual Diagrams**
  - **Tool**: Mermaid code blocks only
  - **Format**: Export as `.svg` files
  - **Location**: Save in `static/img/diagrams/`
  - **Usage**: Reference SVG files in Markdown using relative paths in chapters .md files
  - **Quantity**: Use sparingly - only for essential concepts
  - **Style**: Keep diagrams simple and clear

  ### **3. Planning Before Building**
  - **Do NOT create folder structure yet**
  - First analyze and plan based on:
    - Docusaurus documentation capabilities
    - Content from `content.md`
    - Logical learning progression

  ---

  ## Workflow Steps

  ### **Phase 1: Research (Do This First)**
  1. Connect to Context7 MCP server (`/websites/docusaurus_io`)
  2. Study Docusaurus documentation structure
  3. Read and analyze `content.md` thoroughly
  4. Take notes on key topics and themes

  ### **Phase 2: Planning (Do This Second)**
  1. Create 4-module breakdown
  2. Assign content from `content.md` to modules
  3. Define chapter structure per module
  4. Identify diagram needs
  5. Plan Docusaurus feature usage
  6. Document complete module plan

  ---

  ## Content Guidelines

  ### **Markdown Files**
  - Use proper heading hierarchy (`#`, `##`, `###`)
  - Include frontmatter for metadata
  - Keep content concise and scannable
  - Use code blocks with syntax highlighting
  - Link between related chapters/modules
  - Source content from `content.md`

  ### **Diagram Usage**
  ```markdown
  ![Diagram Description](../static/img/diagrams/diagram-name.svg)
  ```

  ---

  ## Deliverables

  ### **Planning Phase Deliverable**
  - Detailed module structure plan
  - Content mapping document
  - Diagram requirements list
  - Docusaurus features to implement

  ---

  ## Quality Standards

  **Planning**: Thorough analysis, logical organization, clear justification  
  **Content**: Clear, concise, technically accurate, based on `content.md` which is present at root level of project.  
  **Navigation**: Intuitive 3-level hierarchy  
  **Diagrams**: Simple, essential-only, properly referenced  
  **Structure**: Follows approved plan exactly  
  **Source**: Docusaurus docs (Context7) + `content.md` (content)

  ---

  ## Important Notes

  ⚠️ **DO NOT CREATE ANY FOLDERS OR FILES UNTIL PLANNING IS COMPLETE AND APPROVED**

  1. First: Research using Context7 MCP and read `content.md`
  2. Second: Create and present module plan
  3. Third: Wait for approval
  4. Fourth: Implement based on approved plan

  This ensures the structure is optimal before any development work begins.
labels: [docusaurus, website, plan]
links:
  spec: ../../../../specs/001-robotics-course-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-robotics-course-book/plan.md
tests:
  []
---

## Prompt

{{PROMPT_TEXT}}

## Response snapshot

The detailed module plan has been saved to `plan.md`. This plan outlines the modular structure, content mapping, Docusaurus features to be used, and required diagrams based on analysis of the `content.md` file and Docusaurus best practices. No files or folders have been created yet.

## Outcome

- ✅ Impact: Detailed plan for Docusaurus website structure created.
- 🧪 Tests: None
- 📁 Files: `plan.md` updated.
- 🔁 Next prompts: User approval of the plan, then `/sp.tasks` or `/sp.implement` to execute the plan.
- 🧠 Reflection: The planning phase was successful in outlining a clear, detailed approach for the Docusaurus website, adhering to the "plan before implement" guideline.

## Evaluation notes (flywheel)

- Failure modes observed: Confusion with PHR numbering.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Confirm PHR numbering in future steps.
