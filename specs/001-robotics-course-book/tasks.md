---
description: "Task list for Docusaurus Physical AI & Humanoid Robotics Course Book implementation"
---

# Tasks: Physical AI & Humanoid Robotics Course Book

**Input**: Design documents from `/specs/001-robotics-course-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), content.md

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

- [X] T001 Create the root Docusaurus project using `npx create-docusaurus@latest book classic` at the repository root.
- [X] T002 Verify that the `book/` directory contains the initial Docusaurus project structure.

---

## Phase 2: Foundational (Website Structure)

**Purpose**: Establish the core navigation and chapter files.

- [X] T003 Create `book/overview.md` as the main homepage for the book.
- [X] T004 Create `book/module1/overview.md` as the overview page for Module 1.
- [X] T005 Create `book/module2/overview.md` as the overview page for Module 2.
- [X] T006 Create `book/module3/overview.md` as the overview page for Module 3.
- [X] T007 Create `book/module4/overview.md` as the overview page for Module 4.
- [X] T008 Create `book/module1/chapter1.md`: Foundations of Physical AI.
- [X] T009 Create `book/module1/chapter2.md`: ROS 2 Fundamentals.
- [X] T010 Create `book/module1/chapter3.md`: Advanced ROS 2 Concepts.
- [X] T011 Create `book/module2/chapter1.md`: Robot Simulation with Gazebo.
- [X] T012 Create `book/module2/chapter2.md`: High-Fidelity Rendering with Unity.
- [X] T013 Create `book/module3/chapter1.md`: Introduction to the NVIDIA Isaac Platform.
- [X] T014 Create `book/module3/chapter2.md`: AI-Powered Perception and Navigation.
- [X] T015 Create `book/module3/chapter3.md`: Reinforcement Learning and Sim-to-Real.
- [X] T016 Create `book/module4/chapter1.md`: Humanoid Development and Control.
- [X] T017 Create `book/module4/chapter2.md`: Conversational Robotics with LLMs.
- [X] T018 Create `book/module4/chapter3.md`: Capstone Project: The Autonomous Humanoid.

---

## Phase 3: User Story 1 - Student Journey (P1) 🎯 MVP

**Goal**: Populate all chapters with core content, enabling a student to follow the learning path.

**Independent Test**: A student can navigate through all chapters, and each chapter contains relevant and formatted content extracted from `content.md`.

### Implementation for User Story 1

- [X] T019 [P] [US1] Populate `book/overview.md` with an introduction and links to modules, integrating "Why Physical AI Matters" from `content.md`.
- [X] T020 [P] [US1] Populate `book/module1/overview.md` using the focus and overview from `content.md` for Module 1.
- [X] T021 [P] [US1] Populate `book/overview.md` with an introduction and links to modules, integrating "Why Physical AI Matters" from `content.md`.
- [ ] T022 [P] [US1] Populate `book/module1/chapter2.md` with content from "Weeks 3-5: ROS 2 Fundamentals" in `content.md`.
- [ ] T023 [P] [US1] Populate `book/module1/chapter3.md` by synthesizing "ROS 2 Nodes, Topics, and Services", "Bridging Python Agents to ROS controllers using rclpy" and "Understanding URDF (Unified Robot Description Format) for humanoids" from `content.md`.
- [ ] T024 [P] [US1] Populate `book/module2/overview.md` using the focus and overview from `content.md` for Module 2.
- [ ] T025 [P] [US1] Populate `book/module2/chapter1.md` with content from "Weeks 6-7: Robot Simulation with Gazebo" in `content.md`.
- [ ] T026 [P] [US1] Populate `book/module2/chapter2.md` with "High-fidelity rendering and human-robot interaction in Unity" and "Simulating sensors: LiDAR, Depth Cameras, and IMUs" from `content.md`.
- [ ] T027 [P] [US1] Populate `book/module3/overview.md` using the focus and overview from `content.md` for Module 3.
- [ ] T028 [P] [US1] Populate `book/module3/chapter1.md` with introductory content on "NVIDIA Isaac SDK and Isaac Sim" from `content.md`.
- [ ] T029 [P] [US1] Populate `book/module3/chapter2.md` with "AI-powered perception and manipulation" and "Isaac ROS: Hardware-accelerated VSLAM (Visual SLAM) and navigation" from `content.md`.
- [ ] T030 [P] [US1] Populate `book/module3/chapter3.md` with "Reinforcement learning for robot control" and "Sim-to-real transfer techniques" from `content.md`.
- [ ] T031 [P] [US1] Populate `book/module4/overview.md` using the focus and overview from `content.md` for Module 4.
- [ ] T032 [P] [US1] Populate `book/module4/chapter1.md` with content from "Weeks 11-12: Humanoid Robot Development" in `content.md`.
- [ ] T033 [P] [US1] Populate `book/module4/chapter2.md` with content from "Week 13: Conversational Robotics" in `content.md`.
- [ ] T034 [P] [US1] Populate `book/module4/chapter3.md` with the "Capstone Project: The Autonomous Humanoid" description and relevant sections from `content.md`.

---

## Phase 4: User Story 2 - Instructor Curriculum Planning (P2)

**Goal**: Ensure the book structure is logical and easy to use for curriculum development.

**Independent Test**: An instructor can easily navigate the website, and the modular breakdown in the plan clearly maps to the website's structure.

### Implementation for User Story 2

- [ ] T035 [US2] Review the overall website structure and `sidebars.js` configuration against the `plan.md` to ensure clarity and logical flow for curriculum planning.

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Add visual elements and finalize navigation.

- [ ] T036 [P] Create `book/static/img/diagrams/` directory.
- [ ] T037 [P] Generate the "High-Level Book Structure Diagram" Mermaid code and render/save as `book/static/img/diagrams/book_structure.svg`. Update `book/overview.md` to reference this SVG.
- [ ] T038 [P] Generate the "ROS 2 Architecture Diagram" Mermaid code and render/save as `book/static/img/diagrams/ros2_architecture.svg`. Update `book/module1/chapter2.md` to reference this SVG.
- [ ] T039 [P] Generate the "Sim-to-Real Workflow Diagram" Mermaid code and render/save as `book/static/img/diagrams/sim_to_real_workflow.svg`. Update `book/module3/chapter3.md` to reference this SVG.
- [ ] T040 Configure Docusaurus `sidebars.js` to create the nested navigation structure as defined in `plan.md`, using categories for modules and docs for chapters.
- [ ] T041 Configure Docusaurus `docusaurus.config.js` for the homepage and other site-wide settings.
- [ ] T042 Incorporate "Learning Outcomes", "Assessments", "Hardware Requirements", "Lab Setup Options", "Getting Started", "Prerequisites", and "Support & Resources" from `content.md` into appropriate places on the homepage, module overviews, or dedicated new chapters/pages (e.g., a "Getting Started" page).

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Phase 1 completion.
- **User Story 1 (Phase 3)**: Depends on Phase 2 completion. Tasks within this phase can be executed in parallel.
- **User Story 2 (Phase 4)**: Can run in parallel with Phase 3, but relies on the structure created in Phase 2.
- **Final Phase (Polish & Cross-Cutting Concerns)**: Depends on Phase 2 and 3 completion.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational Phase 2 is complete.
- **User Story 2 (P2)**: Can start after Foundational Phase 2 is complete.

### Parallel Opportunities

- All tasks marked [P] can run in parallel if they operate on different files and have no inter-dependencies within the same phase.

---

## Implementation Strategy

### MVP First (User Story 1 Core Content)

1. Complete Phase 1: Setup.
2. Complete Phase 2: Foundational (creating all overview and empty chapter files).
3. Complete Phase 3: User Story 1 (populating all chapters with more content).
4. **STOP and VALIDATE**: Review the populated content and navigation.

### Incremental Delivery

1. Complete Setup + Foundational → Basic website structure with empty chapters.
2. Add User Story 1 (Content Population) → Website with full content (write more content in all chapters).
3. Add User Story 2 (Instructor Review) → Review and refine for curriculum use.
4. Add Final Phase (Polish) → Integrate diagrams and finalize navigation.

---

## Notes

- Explicitly source content sections from `content.md` for each chapter and add extra content in chapters from yourself also
- Use appropriate Markdown formatting, headings, and frontmatter.
- Ensure all relative links within the Docusaurus site are correct.
- Write more ocntent in chapters
