# SDD Book Publishing Constitution

## Role: Senior Systems Architect

## Global Format Structure

## The Book Layout Protocol

- Sidebar is persistent
- Modules (parents) = collapsible accordions
- Chapters (children) = pages rendered on click

## Explicit Hierarchy Rules

- Modules = noun-based domain names
- Chapters = action/specific names
- No orphan chapters

## Core Principles

### I. Structural Integrity
All components must maintain structural soundness, ensuring robust and predictable behavior across the system.

### II. Modular Isolation
Each module must be self-contained and operate independently, minimizing interdependencies and facilitating easier maintenance and updates.

### III. Scalability First
Architectural decisions prioritize scalability to accommodate future growth and increased demand without significant re-architecture.

### IV. UX Consistency
User experience must be consistent across all interfaces, adhering to established design guidelines and interaction patterns.

## Governance

- Constitution is highest authority
- Structural changes need Architect approval
- PRs violating hierarchy must be rejected

**Version**: 1.2.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-06

## Technical Requirements & Grounding

### I. Mandatory Search Rule (Grounding)

All content generation (for Chapters and Module documentation) must be grounded using the provided `context7` MCP server. The content retrieval must be strictly scoped to the Docusaurus documentation library with the specific Library ID: `/websites/docusaurus_io`.

## Design System & Theming

### I. Mandatory Color Palette

The entire documentation platform (using a Docusaurus/Sidebar layout) must strictly adhere to the following color palette:

- Primary Color: `#000000` (Black)
- Secondary Color: `#5DADE2` (Light blue)

