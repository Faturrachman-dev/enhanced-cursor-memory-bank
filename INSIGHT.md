# System Archive: Cursor Memory Bank (CMB) System

## System ID: CMB-V0.7-Optimized
## Date Archived: [Current Date, e.g., 2025-06-04]
## Complexity Level: 4 (Complex System Documentation)
## Status: COMPLETED & ARCHIVED

## 1. System Overview

### 1.1. System Purpose and Scope
The Cursor Memory Bank (CMB) system is a modular, documentation-driven framework designed to enhance AI agent capabilities within the Cursor IDE. Its primary purpose is to overcome the inherent context limitations of large language models (LLMs) by providing a structured, persistent memory and an optimized development workflow. It guides AI agents through a disciplined, efficient, and well-documented software engineering process.

The system's scope covers the entire software development lifecycle, from initial task analysis and planning through design, implementation, reflection, and archiving, all within the Cursor IDE environment.

### 1.2. Final System Architecture
The CMB system employs a hierarchical, event-driven architecture based on Cursor's custom modes and a set of interconnected Markdown rule files (`.mdc`) and data files (`.md`).

**Key Architectural Principles:**
*   **Hierarchical Rule Loading:** Rules are organized in a tree-like structure and loaded just-in-time (JIT) to optimize token usage.
*   **Single Source of Truth:** `tasks.md` serves as the central, authoritative record for all task statuses and progress.
*   **Adaptive Complexity Model:** Workflows and documentation depth scale automatically based on task complexity (Levels 1-4).
*   **Mode-Specific Orchestration:** Each development phase (mode) has a dedicated orchestrator rule that guides the AI's actions.
*   **Context Preservation:** `activeContext.md` acts as a dynamic handover document between modes.
*   **Text-Only Rules:** All `.mdc` rule files contain only text-based instructions, ensuring direct AI digestion without reliance on visual interpretation.

### 1.3. Key Components & Modules
The CMB system is composed of several logical modules:

*   **Custom Modes (User-Facing Interface):**
    *   **VAN:** Project initialization, complexity assessment, quick triage.
    *   **PLAN:** Detailed task planning, dependency identification, creative flagging.
    *   **CREATIVE:** Structured design exploration (Architecture, UI/UX, Algorithm).
    *   **IMPLEMENT:** Code modification, execution, and progress tracking.
    *   **REFLECT:** Post-implementation review and learning.
    *   **ARCHIVE:** Final documentation consolidation and task closure.
    *   **QA:** On-demand technical validation (callable from any mode).

*   **Memory Bank Files (Persistent Memory):**
    *   `tasks.md`: Central task tracking.
    *   `activeContext.md`: Current operational context.
    *   `progress.md`: Detailed activity log.
    *   `projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `style-guide.md`: Foundational project context.
    *   `memory-bank/creative/`: Stores design documents.
    *   `memory-bank/reflection/`: Stores reflection documents.
    *   `memory-bank/archive/`: Stores final archive documents.

*   **Rule Files (`.cursor/rules/isolation_rules/`):**
    *   **Core Rules (`Core/`):** Fundamental behaviors (command execution, file verification, platform awareness, mode transitions, optimization principles).
    *   **Visual Maps (`visual-maps/`):** Top-level orchestrators for each custom mode, defining high-level process flows and fetching sub-rules.
    *   **Level-Specific Rules (`LevelX/`):** Tailored instructions for each complexity level (L1-L4 planning, implementation, reflection, archiving).
    *   **Phase-Specific Rules (`Phases/CreativePhase/`):** Detailed guidance for specific creative design types (architecture, UI/UX, algorithm) and an optimized template.
    *   **VAN Split Rules (`visual-maps/van_mode_split/`):** Sub-orchestrators for VAN mode, including QA checks and utilities.

### 1.4. Integration Points
The CMB system integrates primarily with the Cursor AI IDE's built-in functionalities:

*   **Cursor Custom Modes Feature:** Leverages Cursor's ability to define custom AI behaviors with specific prompts and tool sets.
*   **Cursor AI Tools:**
    *   `fetch_rules`: Critical for hierarchical rule loading.
    *   `edit_file`: Primary for all content creation/modification (code, documentation).
    *   `read_file`: Primary for context gathering (reading code, existing Memory Bank files, rules).
    *   `run_terminal_cmd`: For execution tasks (mkdir, builds, tests), with platform awareness.
    *   `list_dir`, `search_files`, `codebase_search`: For file system exploration and content searching.
*   **User Interaction:** Relies on user commands (e.g., `VAN`, `PLAN`, `ARCHIVE NOW`) to trigger mode transitions and provide feedback.

### 1.5. Technology Stack
*   **Primary Language:** Markdown (`.md`, `.mdc`) for all rules and documentation.
*   **Scripting:** Python (`refine_instructions.py`) for automated generation/update of `.mdc` files.
*   **Platform:** Cursor AI IDE (version 0.48+ recommended).
*   **Underlying AI Model:** Claude 3.7 Sonnet (recommended for optimal performance, especially in CREATIVE mode).
*   **Shell Environments:** Supports both Windows PowerShell and Unix/Linux/macOS Bash/Zsh via platform-aware commands.

### 1.6. Deployment Environment Overview
The CMB system is "deployed" by copying its files into the user's local project directory and configuring Cursor's custom modes. It operates entirely locally within the Cursor IDE environment, ensuring data privacy and direct access to the codebase.

## 2. Requirements and Design Documentation Links

The CMB system's design is implicitly documented across its `.mdc` rule files, particularly within the `Core/` directory and the `optimization-journey/` documents.

*   **Business Requirements:**
    *   **Context Retention:** Addressed by persistent Memory Bank files (`memory-bank-paths.mdc`).
    *   **Structured Development:** Implemented through distinct modes and workflow orchestration (`main-optimized.mdc`, `visual-maps/*.mdc`).
    *   **Efficiency:** Achieved via token optimization strategies (`optimization-integration.mdc`, `hierarchical-rule-loading.mdc`).
*   **Functional Requirements:**
    *   **Mode-Specific Tasks:** Each mode's `.mdc` rule defines its specific functional responsibilities (e.g., `Level3/planning-comprehensive.mdc` for L3 planning).
    *   **Automated Documentation:** Templates guide structured output (`Phases/CreativePhase/optimized-creative-template.mdc`, `Level1/quick-documentation.mdc`).
    *   **Technical Validation:** QA mode rules define validation checks (`van_mode_split/van-qa-main.mdc`).
*   **Non-Functional Requirements:**
    *   **Token Efficiency:** Central to the system's design (`main-optimized.mdc`, `hierarchical-rule-loading.mdc`, `optimization-integration.mdc`).
    *   **Reliability:** Ensured by explicit tool prioritization (`Core/command-execution.mdc`), file verification (`Core/file-verification.mdc`), and QA gates.
    *   **Adaptability:** Achieved through the adaptive complexity model (`Core/complexity-decision-tree.mdc`) and user-modifiable rules.
*   **Architecture Decision Records (ADRs):** The `optimization-journey/` documents (e.g., `04-single-source-of-truth.md`, `09-context-optimization.md`) serve as implicit ADRs, detailing design problems, alternatives considered, and rationales for key architectural shifts in the CMB system itself.
*   **Creative Design Documents:** The `Phases/CreativePhase/` rules (e.g., `creative-phase-architecture.mdc`, `creative-phase-uiux.mdc`) act as templates for the *AI's* design outputs, demonstrating the system's own design principles.

## 3. Implementation Documentation Summary

### 3.1. Phased Implementation Overview
The CMB system itself is "implemented" through the meticulous definition and refinement of its `.mdc` rule files. This implementation journey has been iterative, marked by distinct optimization rounds that incrementally built upon previous improvements. The `refine_instructions.py` script serves as the primary "build tool" for generating these `.mdc` files from a centralized Python definition.

### 3.2. Key Implementation Details & Challenges
*   **Rule Definition:** Each `.mdc` file is a self-contained unit of instruction, designed to be loaded on-demand.
*   **`refine_instructions.py`:** This Python script is critical. It programmatically generates all `.mdc` files, ensuring consistent frontmatter (description, globs, alwaysApply) and embedding the detailed textual content. This simplifies maintenance and ensures all rules adhere to the latest formatting standards.
*   **Mermaid Diagram Conversion:** A significant implementation detail was the conversion of all Mermaid diagrams within the `.mdc` rules to textual descriptions. This was a direct response to the challenge of LLMs not being able to "see" or reliably interpret diagrams, ensuring all instructions are purely text-based for optimal AI digestion.
*   **`fetch_rules` Integration:** The implementation heavily relies on explicit `fetch_rules` calls within `.mdc` files to achieve hierarchical loading. This required careful structuring of the rule content to guide the AI to fetch the correct sub-rules at the right time.
*   **Custom Mode Prompt Simplification:** A key implementation step was drastically simplifying the custom mode prompts (`custom_modes_refined/*.md`) to only contain an acknowledgment and a single `fetch_rules` call to the mode's top-level orchestrator (`visual-maps/*.mdc`). This resolved issues where the AI bypassed hierarchical loading due to having all instructions upfront.

### 3.3. Code Repository & Key Branches/Tags
*   **Repository:** `https://github.com/vanzan01/cursor-memory-bank.git`
*   **Main Branch:** `main` (assumed for active development).
*   **Key Tags:** `v0.1-legacy`, `0.6-beta.1`, `0.7-beta` (representing major architectural shifts and optimization milestones).

### 3.4. Build and Packaging Details
The "build" process for the CMB system involves:
1.  Running the `refine_instructions.py` script to generate/update the `.mdc` files in `.cursor/rules/isolation_rules/`.
2.  Manually copying the content from `custom_modes_refined/*.md` into the "Advanced options" of Cursor's custom mode settings.
3.  Ensuring the `memory-bank/` directory structure is present in the project root.

## 4. API Documentation (Conceptual)

The "API" of the CMB system is defined by the user commands that trigger modes and the expected interactions within those modes.

*   **API Overview:** The system exposes a set of commands (modes) that initiate structured development workflows. Each mode expects certain contextual inputs (files, user prompts) and produces specific outputs (updated Memory Bank files, code changes, terminal outputs).

*   **API Endpoints (Commands):**
    *   **`VAN`**:
        *   **Purpose:** Initialize project, assess complexity, perform quick triage.
        *   **Expected Input:** User command "VAN", initial project files (README, source).
        *   **Expected Output:** Updated `activeContext.md` (OS, complexity), `tasks.md` (initial task), `memory-bank/` structure.
    *   **`PLAN`**:
        *   **Purpose:** Create detailed implementation plan.
        *   **Expected Input:** User command "PLAN", `tasks.md` (with task), `activeContext.md`.
        *   **Expected Output:** Detailed plan in `tasks.md` (sub-tasks, requirements, creative flags), updated `activeContext.md`.
    *   **`CREATIVE`**:
        *   **Purpose:** Explore design options for complex components.
        *   **Expected Input:** User command "CREATIVE", `tasks.md` (with creative flags), `activeContext.md`.
        *   **Expected Output:** `memory-bank/creative/creative-*.md` documents, updated `tasks.md` (creative tasks marked complete), updated `activeContext.md`.
    *   **`IMPLEMENT`**:
        *   **Purpose:** Build planned changes.
        *   **Expected Input:** User command "IMPLEMENT", `tasks.md` (with plan), `activeContext.md`, `creative/` docs (if applicable).
        *   **Expected Output:** Modified source code, updated `tasks.md` (sub-tasks complete), `progress.md` (build log), `activeContext.md`.
    *   **`REFLECT`**:
        *   **Purpose:** Review completed task, document lessons.
        *   **Expected Input:** User command "REFLECT", `tasks.md` (implement complete), `progress.md`, `activeContext.md`, `creative/` docs.
        *   **Expected Output:** `memory-bank/reflection/reflect-*.md`, updated `tasks.md` (reflection complete), `activeContext.md`.
    *   **`ARCHIVE NOW`**: (Triggered within `REFLECT` mode)
        *   **Purpose:** Consolidate and formally archive task documentation.
        *   **Expected Input:** User command "ARCHIVE NOW" (after reflection), `reflection/` doc, `tasks.md`, `activeContext.md`.
        *   **Expected Output:** `memory-bank/archive/archive-*.md`, `tasks.md` (task marked `COMPLETED & ARCHIVED`), `progress.md`, `activeContext.md` (reset).
    *   **`QA`**: (Callable from any mode)
        *   **Purpose:** Perform technical validation checks.
        *   **Expected Input:** User command "QA", current project state, `activeContext.md`.
        *   **Expected Output:** QA report (displayed to user), updated `activeContext.md` (QA log), `memory-bank/.qa_validation_status` file.

## 5. Data Model and Schema Documentation

### 5.1. Data Model Overview
The CMB system's data model is centered around Markdown files, organized hierarchically within the `memory-bank/` directory. This structure facilitates human readability and AI processing.

### 5.2. Database Schema (Memory Bank File Structure)
The primary "database schema" is the file system structure and the internal Markdown formatting within these files.

*   **`memory-bank/` (Root Directory):**
    *   **`tasks.md`:**
        *   **Purpose:** Central task registry.
        *   **Schema:** Markdown headings for tasks (`## Task: [Name]`), bullet points for status (`- **Status:**`), sub-tasks (`- [ ] Sub-task`), and links to related documents.
        *   **Key Fields:** Task Name/ID, Status, Priority, Complexity Level, Assigned To, Requirements, Sub-tasks, Dependencies, Creative Phase Requirements, Checkpoints.
    *   **`activeContext.md`:**
        *   **Purpose:** Dynamic operational context and mode transition handover.
        *   **Schema:** Markdown headings for sections (e.g., `## Current Mode`, `## Focus`, `## Task Complexity Assessment`, `## Mode Transition Prepared`, `## File Verification Log`, `## Terminal Command Log`, `## VAN QA Log`).
        *   **Key Fields:** Current Mode, Focus, Project Complexity Level, Task Name, Log entries (Timestamp, Tool Used, Command, Result, Effect, Next Steps).
    *   **`progress.md`:**
        *   **Purpose:** Detailed activity log and implementation status.
        *   **Schema:** Markdown headings for sections (e.g., `# Build Progress`, `## Directory Structure`). Entries typically include Date, Component/Feature, Files Created/Modified, Key Changes, Testing Results, Next Steps.
    *   **`projectbrief.md`:**
        *   **Purpose:** High-level project description.
        *   **Schema:** Markdown headings for Purpose, Core Functionality, Key Technologies.
    *   **`productContext.md`:**
        *   **Purpose:** User needs and product goals.
        *   **Schema:** Markdown headings for Target Users, Key User Needs/Goals.
    *   **`systemPatterns.md`:**
        *   **Purpose:** Document architectural patterns and principles.
        *   **Schema:** Markdown headings for Overall Architecture, Main Components & Interactions.
    *   **`techContext.md`:**
        *   **Purpose:** Detailed technical stack and environment.
        *   **Schema:** Markdown headings for Backend, Frontend, Database, Key Libraries/Frameworks, Operating System, Path Separator, CLI.
    *   **`style-guide.md`:**
        *   **Purpose:** Document coding style and UI/UX visual guidelines.
        *   **Schema:** Markdown headings for Backend Code Style, Frontend Code Style, Commit Messages (can be expanded for UI/UX with Colors, Typography, Spacing, Components).
    *   **`memory-bank/creative/` (Directory):**
        *   **Purpose:** Stores detailed design documents.
        *   **Naming Convention:** `creative-[component_name_or_aspect]-[YYYYMMDD].md`
        *   **Schema:** Adheres to `optimized-creative-template.mdc` (Problem Definition, Options Explored, Analysis, Decision & Rationale, Implementation Guidelines).
    *   **`memory-bank/reflection/` (Directory):**
        *   **Purpose:** Stores post-task review documents.
        *   **Naming Convention:** `reflect-[task_name_or_id]-[YYYYMMDD].md`
        *   **Schema:** Varies by level (Basic, Intermediate, Comprehensive) but includes Summary, What Went Well, Challenges, Lessons Learned, Improvements.
    *   **`memory-bank/archive/` (Directory):**
        *   **Purpose:** Stores final, consolidated task archives.
        *   **Naming Convention:** `archive-[task_name_or_id]-[YYYYMMDD].md`
        *   **Schema:** Varies by level but includes Task Summary, Requirements Met, Implementation Overview, Testing, Lessons Learned, Links to all related documents.
    *   **`memory-bank/.qa_validation_status` (Hidden File):**
        *   **Purpose:** Simple flag for programmatic checks of QA status.
        *   **Schema:** Plain text "PASS" or "FAIL" followed by timestamp.

## 6. Security Documentation Summary

The CMB system's security is primarily derived from its local, file-based nature and its operation within the Cursor IDE.

*   **Security Architecture:** The system itself does not introduce new network interfaces or external data storage. All data resides locally on the user's machine.
*   **Data Protection Measures:** Data is protected by the user's local file system permissions and the security measures of the Cursor IDE itself. The system does not implement its own encryption or access controls.
*   **User Control:** The user retains full control over the files and can manage their security as they would any other local project files.
*   **Sensitive Information:** Users should be aware that detailed project information, including potential sensitive details from code or logs, is stored in plaintext Markdown files. Handling of this file should align with the security posture of the original repository.

## 7. Testing Documentation Summary

The CMB system's "testing" is primarily internal and rule-driven, with a dedicated QA mode.

*   **Test Strategy:** The system's rules define a structured approach to testing within development workflows (e.g., unit tests, integration tests, E2E tests for the *user's project*). For the *CMB system itself*, validation is achieved through:
    *   **Rule-based Verification Checklists:** Embedded `✓` checklists within `.mdc` files guide the AI to self-verify adherence to process steps and documentation completeness.
    *   **QA Mode:** A dedicated, on-demand QA mode performs technical validation of the development environment and project setup *before* implementation phases.
*   **Test Results:** The `QA` mode generates structured success or failure reports, logging details in `activeContext.md` and a hidden `.qa_validation_status` file.
*   **Known Issues & Limitations:** The system's primary limitation is the inherent non-determinism of LLMs, which means the AI may occasionally deviate from the intended workflow despite clear instructions. This requires user guidance to re-align. Manual setup of custom modes is also a known friction point.

## 8. Deployment Documentation Summary

The CMB system does not have a traditional "deployment" process but rather an "installation" and "configuration" procedure.

*   **Deployment Architecture:** The system runs entirely within the local Cursor IDE environment. There are no server-side components or complex infrastructure requirements for the CMB system itself.
*   **Environment Configuration:** Requires Cursor IDE (v0.48+) and a compatible LLM (Claude 3.7 Sonnet recommended). Python is needed for the `refine_instructions.py` script.
*   **Deployment Procedures:**
    1.  Clone/download the repository into the user's project root.
    2.  Run `refine_instructions.py` to generate/update `.mdc` rules in `.cursor/rules/isolation_rules/`.
    3.  Manually configure Cursor custom modes by copying content from `custom_modes_refined/*.md` into their "Advanced options."

## 9. Operational Documentation Summary

The CMB system operates by guiding the AI through a structured workflow based on user commands and file-based context.

*   **Operating Procedures:**
    1.  User activates a custom mode (e.g., `VAN`).
    2.  The custom mode's prompt triggers the mode's top-level orchestrator rule (`visual-maps/*.mdc`) via `fetch_rules`.
    3.  The orchestrator guides the AI through the phase's steps, performing actions using Cursor tools (`read_file`, `edit_file`, `run_terminal_cmd`, `codebase_search`).
    4.  The AI updates Memory Bank files (`tasks.md`, `activeContext.md`, `progress.md`) to maintain state.
    5.  The AI recommends the next logical mode or action.
    6.  User provides the next command or input.
*   **Maintenance Tasks:**
    *   Regularly run `refine_instructions.py` if the underlying rule definitions are updated.
    *   Manually update Cursor custom mode prompts if the `custom_modes_refined/*.md` files are updated.
    *   Periodically review Memory Bank files for consistency and clarity.
*   **Troubleshooting Guide:** Common issues include:
    *   **Mode not responding:** Verify custom mode prompt content, tool enablement, and correct mode activation.
    *   **Rules not loading:** Check `.cursor/rules/isolation_rules/` directory path and file permissions.
    *   **Command execution issues:** Verify current directory, platform awareness, and correct command syntax.
    *   **Looping in quick fixes:** Indicates a task might be more complex than L1, requiring re-assessment.

## 10. Knowledge Transfer & Lessons Learned

### Key Strategic Learnings (from CMB's optimization journey):
*   **Context Efficiency is Paramount:** Direct impact on LLM performance. Hierarchical rule loading (65% token reduction), progressive documentation (60% token reduction), and differential Memory Bank updates (30% token reduction) are critical.
*   **Text-Only Rules for AI Digestion:** Eliminating Mermaid diagrams and relying solely on structured Markdown text ensures unambiguous AI processing.
*   **Hierarchical Orchestration is Key:** Top-level orchestrator rules (`visual-maps/*.mdc`) fetching specific sub-rules (from `Core/`, `LevelX/`, `Phases/`) is essential for modularity and token efficiency.
*   **Single Source of Truth:** Centralizing task status in `tasks.md` eliminates redundancy and synchronization issues.
*   **Adaptive Complexity is Effective:** Scaling process rigor and documentation depth based on task complexity (L1-L4) optimizes resource allocation.
*   **Explicit `fetch_rules` Calls:** Custom mode prompts must explicitly instruct the AI to `fetch_rules` the mode's orchestrator to ensure the hierarchical loading mechanism is engaged.
*   **QA as a Gate:** Implementing a mandatory QA validation phase before implementation (especially for L2+ tasks) prevents costly errors and ensures readiness.

### Recommendations for Future Similar Systems:
*   Prioritize token efficiency from the ground up.
*   Design workflows around clear, text-based instructions.
*   Implement strict hierarchical rule loading.
*   Establish a single source of truth for dynamic data.
*   Incorporate adaptive complexity models.
*   Build in automated validation gates.
*   Acknowledge and design for LLM non-determinism by providing clear recovery paths or re-assessment points.

## 11. Project History Summary

The Cursor Memory Bank system has undergone an extensive optimization journey, evolving from an initial concept to a highly refined, token-optimized framework.

*   **Early Optimization (Rounds 1-5):** Focused on foundational efficiency, clarity, redundancy elimination, establishing `tasks.md` as the single source of truth, and introducing the adaptive complexity model.
*   **Process Refinement (Rounds 6-9):** Refined creative phase handling, enforced structured thinking, and introduced context optimization through visual navigation (which later evolved to text-only descriptions).
*   **Latest Developments (Rounds 10-13):** Integrated with Claude's "Think" tool methodology, implemented strict mode-specific isolation, and refined the overall system architecture for scalability and future directions.
*   **Current State (V0.7-beta):** Represents a robust, token-optimized system with hierarchical rule loading, adaptive complexity, and a comprehensive, text-based rule set.

**Key Decisions & Rationale during Evolution:**
*   **Monolithic to Modular:** Shifted from a single large rule file to multiple specialized `.mdc` files to improve context utilization and maintainability.
*   **Visual to Text-Only Rules:** Transitioned from Mermaid diagrams to purely textual descriptions in `.mdc` files to ensure direct AI digestion and eliminate interpretation ambiguity.
*   **Simplified Custom Mode Prompts:** Reduced custom mode prompts to minimal `fetch_rules` calls to enforce hierarchical rule loading and maximize LLM context window.
*   **Refined Complexity Definitions:** Adjusted L1-L4 definitions to better reflect task nature, codebase size, and iteration requirements, improving AI's initial task assessment.