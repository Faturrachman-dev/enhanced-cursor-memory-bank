These examples will explicitly show:
*   The user's input.
*   The AI's acknowledgment and state.
*   The `fetch_rules` calls that trigger specific `.mdc` rules.
*   The updates to Memory Bank files (`tasks.md`, `activeContext.md`, `progress.md`, `creative/`, `reflection/`, `archive/`).
*   Key decision points and transitions between modes.

---

## Comprehensive Workflow Examples for Cursor Memory Bank (CMB) System

These examples illustrate the practical application of the CMB system's structured workflows and optimized processes.

### Example 1: Level 1 Workflow - Quick Bug Fix

**Scenario:** A user identifies a minor bug: a login button on the mobile version of the website is not clickable. This is a very localized issue.

**User Input:** `VAN`

**AI Action (VAN Mode - Initial Problem Intake & Quick Triage)**

1.  **Acknowledge:** "OK VAN - Beginning Initialization Process."
2.  **Initial Triage:** "Performing initial problem intake and quick triage."
    *   `read_file` user's prompt: "Fix the login button, it's not clickable on mobile."
    *   `read_file` `frontend/src/components/LoginButton.js` (AI identifies this as the most likely implicated file based on keywords).
    *   **Quick Fix Assessment:**
        *   Single file modification (`LoginButton.js`): YES
        *   Clear, unambiguous root cause (e.g., event listener issue): YES (AI deduces this quickly)
        *   Simple, low-risk fix, no design decisions/new dependencies: YES
        *   Expected to take <30 minutes: YES
    *   **Decision:** All strict criteria met for Level 0/1 Quick Fix.
3.  **State Quick Fix:** "Initial analysis suggests a straightforward Level 0/1 fix for the login button not being clickable on mobile. Proceeding with optimized quick fix workflow."
4.  **Update `tasks.md`:**
    ```markdown
    # Tasks
    - [ ] L0/1 Quick Fix: Login button not clickable on mobile.
    ```
5.  **Update `activeContext.md`:**
    ```markdown
    # Active Context
    ## Current Mode: VAN
    ## Focus: L0/1 Quick Fix - Login button not clickable on mobile.
    ## Project Complexity Level: [To be determined]
    ## Initial diagnosis: Event listener issue. Proposed fix: Adapt event handling.
    ```
6.  **Fetch Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Level1/optimized-workflow-level1.mdc`.

**AI Action (Level 1 Optimized Workflow - `optimized-workflow-level1.mdc`)**

1.  **Acknowledge:** "Initiating Optimized Level 1 Workflow for Login button not clickable on mobile."
2.  **Analyze & Locate:** Confirms focus on `frontend/src/components/LoginButton.js`.
3.  **Implement Fix:** `edit_file frontend/src/components/LoginButton.js`
    *   (AI modifies the file, e.g., changes `onClick` to `onTouchEnd` or adds a universal event handler).
4.  **Verify:** `run_terminal_cmd npm test frontend/src/components/LoginButton.js` (hypothetical component test).
    *   (AI observes successful test output).
5.  **Document (Consolidated):**
    *   `edit_file memory-bank/tasks.md` (appends fix details under the task, marks complete):
        ```markdown
        # Tasks
        - [x] L0/1 Quick Fix: Login button not clickable on mobile.
          - **L1 Fix:** Login button not clickable on mobile
          - **Problem:** Button unresponsive on touch devices.
          - **Cause:** Event listener only registered for mouse events.
          - **Solution:** Updated event handler to support both `mousedown` and `touchstart`.
          - **Files:** `frontend/src/components/LoginButton.js`
          - **Tested:** `npm test frontend/src/components/LoginButton.js` passed. Manual verification on mobile.
          - **Status:** COMPLETED - [Current Date]
        ```
    *   `edit_file memory-bank/progress.md` (adds one-liner):
        ```markdown
        # Progress
        - [Current Date] - L1 Fix: Login button not clickable on mobile - Completed. See tasks.md for details.
        ```
    *   `edit_file memory-bank/activeContext.md` (clears focus):
        ```markdown
        # Active Context
        ## Current Mode: VAN
        ## Focus: Ready for new task.
        ## Project Complexity Level: [To be determined]
        ## Initial diagnosis: Event listener issue. Proposed fix: Adapt event handling.
        ## VAN Process Status: Level 1 Initialization Complete. Task ready for IMPLEMENT mode.
        ```
6.  **Notify Completion:** "Level 1 task 'Login button not clickable on mobile' completed and documented efficiently. Ready for next task."

**Workflow Benefits:**
*   **Rapid Resolution:** Bypasses extensive planning/design for trivial tasks.
*   **Token Efficiency:** Only essential rules loaded, minimal documentation overhead.
*   **Self-Contained:** The entire fix lifecycle is handled within one continuous flow.

---

### Example 2: Level 3 Workflow - Implement User Profile Feature

**Scenario:** A user wants to implement a new "User Profile" feature for an existing open-source project. This involves backend API changes (avatar upload, user info), database modifications, and a new frontend UI.

**User Input:** `VAN`

**AI Action (VAN Mode - Standard Path)**

1.  **Acknowledge:** "OK VAN - Beginning Initialization Process."
2.  **Initial Triage:** "Performing initial problem intake and quick triage."
    *   `read_file` user's prompt: "Implement a user profile feature where users can upload an avatar and view their basic info. This is for our open-source project."
    *   `read_file` `README.md`, `package.json` (to assess codebase size/type).
    *   **Quick Fix Assessment:** Fails criteria (multiple components, design needed, not <30 min).
    *   **Decision:** Not a quick fix.
3.  **State Standard Path:** "Initial triage indicates further analysis is needed or the task is more complex than a quick fix. Proceeding with standard VAN initialization."
4.  **Platform Detection:** "Performing platform detection."
    *   `fetch_rules` `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-platform-detection.mdc`.
    *   (AI executes platform detection, e.g., `run_terminal_cmd uname`, logs to `activeContext.md`).
5.  **File Verification:** "Performing Memory Bank file verification and setup."
    *   `fetch_rules` `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
    *   (AI verifies/creates `memory-bank/` structure, logs to `activeContext.md`).
6.  **Full Context Analysis & Complexity Determination:** "Performing detailed context analysis and determining task complexity."
    *   `read_file` relevant project files (e.g., `src/App.js`, `backend/server.py`).
    *   `fetch_rules` `.cursor/rules/isolation_rules/Core/complexity-decision-tree.mdc`.
    *   **AI Action (Complexity Determination - `complexity-decision-tree.mdc`):**
        *   **Assessment:** Multiple components (frontend, backend, DB), new distinct functionality, requires design (avatar storage, UI), medium-large codebase (open-source).
        *   **Determination:** Level 3 (Intermediate Feature).
    *   `edit_file memory-bank/activeContext.md`:
        ```markdown
        ## Task Complexity Assessment
        - Task: Implement User Profile Feature
        - Determined Complexity: Level 3 - Intermediate Feature
        - Rationale: New distinct functionality, multiple components, design needed for avatar/UI, open-source codebase.
        ```
    *   `edit_file memory-bank/tasks.md`:
        ```markdown
        # Tasks
        - [ ] Level 3: Implement User Profile Feature
        ```
7.  **Mode Transition:** "Assessed as Level 3: Intermediate Feature. 🚫 LEVEL 3 TASK DETECTED: Implement User Profile Feature. This task REQUIRES detailed planning. Transitioning to PLAN mode is necessary. Type 'PLAN' to proceed with planning."

**User Input:** `PLAN`

**AI Action (PLAN Mode - `plan-mode-map.mdc`)**

1.  **Acknowledge:** "OK PLAN - Initiating PLAN mode for Implement User Profile Feature."
2.  **Context Gathering:** `read_file memory-bank/tasks.md`, `activeContext.md`, `projectbrief.md`, `techContext.md`.
3.  **Pre-Planning Check:** Confirms task is Level 3.
4.  **Fetch Planning Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/planning-comprehensive.mdc`.
5.  **AI Action (Comprehensive Planning - `planning-comprehensive.mdc`):**
    *   **Define/Refine Task Entry:** `edit_file memory-bank/tasks.md` (populates the Level 3 task entry with detailed sections).
        ```markdown
        # Tasks
        ## Task: L3-001: Implement User Profile Feature
        - **Status:** IN_PROGRESS_PLANNING
        - **Priority:** Medium
        - **Complexity Level:** 3
        - **Assigned To:** AI
        ### 1. Feature Description & Goals
        ... (detailed description) ...
        ### 2. Detailed Requirements
        ... (functional & non-functional) ...
        ### 3. Component Analysis
        ... (new & modified components, interactions) ...
        ### 4. Implementation Strategy & High-Level Steps
        ... (e.g., Phase 1: Backend, Phase 2: Frontend) ...
        ### 5. Dependencies & Integrations
        ...
        ### 6. Risk Assessment & Mitigation
        ...
        ### 7. Creative Phase Requirements (CRITICAL for L3)
        - [ ] CREATIVE: Design UI/UX for the new User Profile page. (Type: UI/UX)
        - [ ] CREATIVE: Architect the avatar storage and processing pipeline. (Type: Architecture)
        ### 8. Testing Strategy Overview
        ...
        ### 9. Notes & Open Questions
        ...
        ### 9. Checkpoints & Phase Gates
        - [ ] **PLAN Phase Complete:** [Date]
        ```
    *   **Log Update:** `edit_file memory-bank/activeContext.md`: "[Timestamp] - Comprehensive plan for L3 feature Implement User Profile Feature updated in tasks.md. Creative phases identified."
6.  **Notify Completion & Recommend Next Mode:** "PLANNING COMPLETE for task Implement User Profile Feature. `tasks.md` has been updated with the detailed plan. The plan indicates that creative design is needed for UI/UX for the new User Profile page, Avatar Storage. Recommend transitioning to CREATIVE mode."

**User Input:** `CREATIVE`

**AI Action (CREATIVE Mode - `creative-mode-map.mdc`)**

1.  **Acknowledge:** "OK CREATIVE - Initiating CREATIVE mode. Identifying components requiring design."
2.  **Context Gathering:** `read_file memory-bank/tasks.md`, `activeContext.md`.
3.  **Iterate Through Pending Creative Sub-Tasks:**
    *   **Sub-Task 1: UI/UX for User Profile Page**
        *   **Announce:** "Starting CREATIVE phase for: User Profile UI - Design Type: UI/UX."
        *   **Update `activeContext.md`:** "Creative Focus: Designing User Profile UI (UI/UX)."
        *   **Fetch Specific Design Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-uiux.mdc`.
        *   **AI Action (UI/UX Design - `creative-phase-uiux.mdc`):**
            *   **Style Guide Integration:** `read_file memory-bank/style-guide.md`. (If not found, AI prompts user to create/link, then proceeds).
            *   **Define Problem & Requirements.**
            *   **Explore UI/UX Options:** (e.g., "Option A: Modal-based Profile Edit", "Option B: Dedicated Profile Page").
            *   **Make Decision & Justify:** (e.g., "Selected Option B for better user experience and future extensibility").
            *   **Outline Implementation Guidelines.**
            *   **Document Design:** `edit_file memory-bank/creative/creative-profile-ui-[date].md` (using `optimized-creative-template.mdc` structure).
            *   **Update `tasks.md`:** Mark `CREATIVE: Design UI/UX...` as complete, add link to `creative-profile-ui-[date].md`.
            *   **Update `activeContext.md`:** Add summary to "Creative Decisions Log."
        *   **Completion:** "UI/UX design for User Profile UI complete. Documented in `memory-bank/creative/creative-profile-ui-[date].md`."
    *   **Sub-Task 2: Architect Avatar Storage**
        *   **Announce:** "Starting CREATIVE phase for: Avatar Storage - Design Type: Architecture."
        *   **Update `activeContext.md`:** "Creative Focus: Designing Avatar Storage (Architecture)."
        *   **Fetch Specific Design Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-architecture.mdc`.
        *   **AI Action (Architecture Design - `creative-phase-architecture.mdc`):**
            *   **Define Problem & Requirements.**
            *   **Explore Architectural Options:** (e.g., "Option A: Direct S3 Upload", "Option B: Backend Proxy Upload").
            *   **Make Decision & Justify:** (e.g., "Selected Option B for security and backend processing needs").
            *   **Outline Implementation Guidelines.**
            *   **Document Design:** `edit_file memory-bank/creative/creative-avatar-storage-[date].md`.
            *   **Update `tasks.md`:** Mark `CREATIVE: Architect avatar storage...` as complete, add link.
            *   **Update `activeContext.md`:** Add summary to "Creative Decisions Log."
        *   **Completion:** "Architecture design for Avatar Storage complete. Documented in `memory-bank/creative/creative-avatar-storage-[date].md`."
4.  **Overall Verification & Transition:** "All CREATIVE design phases for Implement User Profile Feature are complete. Design documents are located in `memory-bank/creative/`. Recommend IMPLEMENT mode to build these components."

**User Input (Optional QA Check):** `VAN QA`

**AI Action (VAN QA Mode - `van_mode_split/van-qa-main.mdc`)**

1.  **Acknowledge:** "OK VAN QA - Initiating VAN QA Technical Validation."
2.  **Context:** `read_file activeContext.md`, `tasks.md`, `techContext.md`.
3.  **Log:** `edit_file activeContext.md`: "VAN QA Log - [Timestamp]: Starting technical validation."
4.  **Perform Four-Point Validation (sequential `fetch_rules` calls):**
    *   **Dependency Verification:** `fetch_rules` `van-qa-checks/dependency-check.mdc`. (AI runs `npm install`, `node -v` etc., logs to `activeContext.md`. Assume PASS).
    *   **Configuration Validation:** `fetch_rules` `van-qa-checks/config-check.mdc`. (AI reads `package.json`, `tsconfig.json`, logs. Assume PASS).
    *   **Environment Validation:** `fetch_rules` `van-qa-checks/environment-check.mdc`. (AI checks Git, Node/npm paths, logs. Assume PASS).
    *   **Minimal Build Test:** `fetch_rules` `van-qa-checks/build-test.mdc`. (AI creates temp project, runs `npm run build`, logs. Assume PASS).
5.  **Consolidate Results:** "Technical validation checks complete. Overall QA Status: PASS."
6.  **Generate Report:** `fetch_rules` `van-qa-utils/reports.mdc`. (AI generates and displays comprehensive success report, writes "PASS" to `memory-bank/.qa_validation_status`).
7.  **Determine Next Steps:** `fetch_rules` `van-qa-utils/mode-transitions.mdc`. (AI recommends BUILD mode).

**AI Action (IMPLEMENT Mode - `implement-mode-map.mdc`)**

1.  **Acknowledge:** "OK IMPLEMENT - Initiating IMPLEMENT mode for Implement User Profile Feature."
2.  **Context Gathering:** `read_file tasks.md`, `activeContext.md`, `progress.md`, `creative/` docs.
3.  **Pre-Implementation Checks:**
    *   PLAN Complete: YES (checked in `tasks.md`).
    *   CREATIVE Complete: YES (checked `tasks.md` and `creative-phase-enforcement.mdc` confirms).
    *   VAN QA Passed: YES (checked `memory-bank/.qa_validation_status`).
4.  **Fetch Guidelines:** `fetch_rules` `Core/command-execution.mdc`.
5.  **Fetch Implementation Rule:** `fetch_rules` `.cursor/rules/isolation_rules/Level3/implementation-intermediate.mdc`.
6.  **AI Action (Level 3 Implementation - `implementation-intermediate.mdc`):**
    *   **Review Plan/Design:** `read_file tasks.md`, `creative/creative-profile-ui-[date].md`, `creative/creative-avatar-storage-[date].md`.
    *   **Iterate through sub-tasks (from `tasks.md`):**
        *   **Sub-task: IMPL: Define data models for user profile and avatar.**
            *   `edit_file backend/models.py` (adds UserProfile, Avatar models).
            *   `edit_file memory-bank/progress.md`: "Implemented data models in `backend/models.py`."
            *   `edit_file memory-bank/tasks.md`: Marks this sub-task `[x]`.
            *   `edit_file memory-bank/activeContext.md`: Updates current progress.
        *   **Sub-task: IMPL: Create API endpoint for avatar image upload.**
            *   `edit_file backend/api.py` (adds upload endpoint).
            *   `edit_file backend/tests/test_api.py` (adds unit tests).
            *   `run_terminal_cmd pytest backend/tests/test_api.py` (logs output to `activeContext.md`).
            *   `edit_file memory-bank/progress.md`: "Implemented avatar upload API. Unit tests passed."
            *   `edit_file memory-bank/tasks.md`: Marks this sub-task `[x]`.
            *   `edit_file memory-bank/activeContext.md`: Updates current progress.
        *   ... (Continues for all implementation sub-tasks) ...
    *   **Final Memory Bank Updates:** `edit_file tasks.md` (marks IMPLEMENT phase complete), `edit_file activeContext.md`.
    *   **Notify Completion:** "Level 3 feature 'User Profile Feature' implementation complete. All sub-tasks and tests passed. Recommend REFLECT mode."

**User Input:** `REFLECT`

**AI Action (REFLECT Mode - `reflect-mode-map.mdc`)**

1.  **Acknowledge:** "OK REFLECT+ARCHIVE - Initiating REFLECT mode for Implement User Profile Feature."
2.  **Pre-Reflection Check:** Verifies IMPLEMENT is complete.
3.  **Fetch Reflection Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/reflection-intermediate.mdc`.
4.  **AI Action (Level 3 Reflection - `reflection-intermediate.mdc`):**
    *   **Context Gathering:** `read_file tasks.md`, `progress.md`, `creative/` docs, `activeContext.md`.
    *   **Prepare Reflection Content:** Synthesizes information from all sources.
    *   **Create Reflection File:** `edit_file memory-bank/reflection/reflect-user-profile-[date].md` (populates with detailed review of planning, creative, implementation, testing phases, lessons learned, etc.).
    *   **Update Memory Bank:**
        *   `edit_file memory-bank/tasks.md`: Marks REFLECT phase complete, adds link to reflection doc.
        *   `edit_file memory-bank/activeContext.md`: Updates focus.
    *   **Notify Completion & Prompt for Archiving:** "REFLECTION COMPLETE for task 'User Profile Feature'. Reflection document created/updated at `memory-bank/reflection/reflect-user-profile-[date].md`. Type 'ARCHIVE NOW' to proceed with archiving this task."

**User Input:** `ARCHIVE NOW`

**AI Action (REFLECT Mode Orchestrator continues)**

1.  **Detect Command:** AI detects "ARCHIVE NOW".
2.  **State:** "OK, proceeding with ARCHIVE process for User Profile Feature."
3.  **Fetch Archive Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/archive-mode-map.mdc`.

**AI Action (ARCHIVE Mode - `archive-mode-map.mdc`)**

1.  **Acknowledge:** "Initiating ARCHIVE mode for User Profile Feature."
2.  **Context Gathering:** `read_file activeContext.md`, `tasks.md`, `reflection/` doc, `progress.md`, `creative/` docs.
3.  **Pre-Archive Check:** Confirms REFLECT phase is complete and reflection document exists.
4.  **Fetch Level-Specific Archive Rule:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/archive-intermediate.mdc`.
5.  **AI Action (Level 3 Archiving - `archive-intermediate.mdc`):**
    *   **Prepare Archive Content:** Synthesizes information from all gathered documents.
    *   **Create Archive File:** `edit_file memory-bank/archive/archive-user-profile-[date].md` (populates with comprehensive summary, links to plan, creative, reflection docs, etc.).
    *   **Update Core Memory Bank Files:**
        *   `edit_file memory-bank/tasks.md`: Marks task "COMPLETED & ARCHIVED", adds link to archive doc.
        *   `edit_file memory-bank/progress.md`: Adds final entry for archiving.
        *   `edit_file memory-bank/activeContext.md`: Clears current task focus, states readiness for new task.
6.  **Notify Completion:** "Intermediate archiving for Level 3 feature 'User Profile Feature' complete. Archive document created at `memory-bank/archive/archive-user-profile-[date].md`. The Memory Bank is ready for the next task. Suggest using VAN mode to initiate a new task."

**Workflow Benefits:**
*   **Structured Development:** Enforces a disciplined approach from planning to archiving.
*   **Comprehensive Documentation:** All phases generate specific, linked documentation.
*   **Design Traceability:** Creative decisions are explicitly made and linked to implementation.
*   **Knowledge Preservation:** Lessons learned and task history are formally archived.
*   **Preventative QA:** Optional QA check ensures readiness before costly implementation.
*   **Token Optimization:** Only relevant rules are loaded at each step, maximizing context window.