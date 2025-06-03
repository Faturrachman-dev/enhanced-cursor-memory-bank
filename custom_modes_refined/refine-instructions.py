# IMPORTANT: put this script in the root of the project!

import os

# --- Define your MDC file data here ---
MDC_FILES_DATA = [
    # We will populate this list
]

def create_or_update_mdc_file(filepath, description, globs, always_apply, body_content):
    """Creates or updates an .mdc file with the given frontmatter and body."""
    
    always_apply_str = 'true' if always_apply else 'false'
    
    frontmatter = f"""---
description: {description}
globs: {globs}
alwaysApply: {always_apply_str}
---
"""
    
    full_content = frontmatter + body_content.strip()

    try:
        dir_name = os.path.dirname(filepath)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
            print(f"Created directory: {dir_name}")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"Successfully created/updated: {filepath}")
    except Exception as e:
        print(f"Error writing file {filepath}: {e}")

if __name__ == "__main__":
    # Add refined Core rules first
    MDC_FILES_DATA.extend([
        {
            "path": ".cursor/rules/isolation_rules/Core/command-execution.mdc",
            "description": "Core guidelines for AI command execution, emphasizing tool priority (edit_file, fetch_rules, run_terminal_cmd), platform awareness, and result documentation within the Memory Bank system.",
            "globs": "**/Core/command-execution.mdc",
            "alwaysApply": False,
            "body": """
# COMMAND EXECUTION SYSTEM

> **TL;DR:** This system provides guidelines for efficient and reliable command and tool usage. Prioritize `edit_file` for file content, `fetch_rules` for loading `.mdc` rules, and `run_terminal_cmd` for execution tasks. Always document actions and results in `memory-bank/activeContext.md`.

## 🛠️ TOOL PRIORITY & USAGE

1.  **`edit_file` (Primary for Content):**
    *   Use for ALL creation and modification of `.md` files in `memory-bank/` and `documentation/`.
    *   Use for ALL source code modifications.
    *   `edit_file` can create a new file if it doesn't exist and populate it.
    *   Provide clear instructions or full content blocks for `edit_file`.
2.  **`fetch_rules` (Primary for `.mdc` Rules):**
    *   Use to load and follow instructions from other `.mdc` rule files within `.cursor/rules/isolation_rules/`.
    *   Specify the full path to the target `.mdc` file.
3.  **`read_file` (Primary for Context Gathering):**
    *   Use to read existing project files (source code, `README.md`), `memory-bank/*.md` files for context, or `.mdc` files if `fetch_rules` is not appropriate for the specific need (e.g., just extracting a template).
4.  **`run_terminal_cmd` (Primary for Execution):**
    *   Use for tasks like `mkdir`, running tests, build scripts, or starting servers.
    *   **CRITICAL:** Be platform-aware (see "Platform-Specific Considerations" below). If unsure of the OS, state your default command (e.g., for Linux) and ask for the Windows PowerShell equivalent if needed.
5.  **`list_dir`, `search_files`, `codebase_search`:**
    *   Use for file system exploration and code/text searching as appropriate.

## 🔍 COMMAND EFFICIENCY & PLANNING WORKFLOW (Conceptual for AI)
```mermaid
graph TD
    Start["Command Planning"] --> Analyze["Analyze Requirements"]
    Analyze --> ToolSelect["Select Correct Tool<br>(edit_file, fetch_rules, run_terminal_cmd, etc.)"]
    ToolSelect --> Complexity{"Action Complexity?"}
    Complexity -->|"Simple File Edit"| SingleEdit["Use `edit_file` directly"]
    Complexity -->|"Simple Terminal Cmd"| SingleCmd["Use `run_terminal_cmd`"]
    Complexity -->|"Complex Sequence"| GroupedSteps["Break into Logical Textual Steps<br>using appropriate tools for each step"]
    SingleEdit & SingleCmd & GroupedSteps --> Verify["Verify Results<br>(e.g., `read_file` back, check terminal output)"]
    Verify --> Document["Document Action & Result<br>in `activeContext.md` using `edit_file`"]
    Document --> Next["Next Action"]
```
**Textual Guide for AI:**
1.  **Analyze Requirements:** Understand what needs to be achieved.
2.  **Select Correct Tool:** Choose `edit_file` for content, `fetch_rules` for rules, `run_terminal_cmd` for execution, etc.
3.  **Execute:** Perform the action. For complex sequences, break it down into clear, tool-specific steps.
4.  **Verify Results:** If you used `edit_file`, consider using `read_file` to confirm the content. If `run_terminal_cmd`, examine the output.
5.  **Document Action & Result:** Use `edit_file` to append a summary of the command/tool call and its outcome to the "Build Log" or relevant section in `memory-bank/activeContext.md`.

## 🚦 DIRECTORY VERIFICATION (for `run_terminal_cmd`)
**Textual Guide for AI:**
1.  Before running build scripts or package manager commands (npm, pip) via `run_terminal_cmd`, verify you are in the correct project root directory.
2.  Use `list_dir` to check for key files like `package.json` or `requirements.txt`.
3.  If not in the correct directory, use `run_terminal_cmd` with `cd [path_to_project_root]` to navigate.

## 📋 COMMAND DOCUMENTATION TEMPLATE (for `activeContext.md` "Build Log")
When documenting your actions, use `edit_file` to append entries like this to `memory-bank/activeContext.md`:
```markdown
### Action: [Purpose of the action]
- **Tool Used:** `[edit_file | fetch_rules | run_terminal_cmd | etc.]`
- **Target/Command:** `[file_path | rule_path | actual_terminal_command]`
- **Parameters (if applicable):** `[e.g., content for edit_file, search query]`
- **Expected Outcome:** `[Briefly what you expected]`
- **Actual Result:**
  \`\`\`
  [Output from run_terminal_cmd, or confirmation of file edit/read]
  \`\`\`
- **Effect:** `[Brief description of what changed in the system or Memory Bank]`
- **Next Steps:** `[What you plan to do next]`
```

## 🔍 PLATFORM-SPECIFIC CONSIDERATIONS (for `run_terminal_cmd`)
**Textual Guide for AI:**
*   **Windows (PowerShell):** Path separator: `\`, Dir creation: `mkdir my_dir` or `New-Item -ItemType Directory -Path my_dir`.
*   **Unix/Linux/Mac (Bash/Zsh):** Path separator: `/`, Dir creation: `mkdir -p my_dir`.
*   **Action:** If unsure of OS, state default (Linux) and ask for Windows PowerShell equivalent or user OS specification.

## 📝 COMMAND EXECUTION CHECKLIST (AI Self-Correction)
- Purpose clear? Correct tool chosen? Platform considerations for `run_terminal_cmd`? Action/result documented in `activeContext.md` via `edit_file`? Outcome verified?

## 🚨 WARNINGS
*   Avoid `run_terminal_cmd` with `echo > file` or `Add-Content` for multi-line content. **Always use `edit_file`**.
*   For destructive `run_terminal_cmd` (e.g., `rm`), seek user confirmation.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/complexity-decision-tree.mdc",
            "description": "Core rule for AI to determine task complexity (Level 1-4) and initiate appropriate workflow using Memory Bank principles.",
            "globs": "**/Core/complexity-decision-tree.mdc",
            "alwaysApply": False,
            "body": """
# TASK COMPLEXITY DETERMINATION

> **TL;DR:** This rule guides you to determine task complexity (Level 1-4). Based on the level, you will then be instructed to `fetch_rules` for the corresponding primary mode map.

## 🌳 COMPLEXITY DECISION TREE (Conceptual for AI)
**Textual Guide for AI:**
Based on user's request and initial analysis (e.g., from `read_file` on `README.md`):

1.  **Bug fix/error correction?**
    *   **Yes:** Single, isolated component? -> **Level 1 (Quick Bug Fix)**
    *   **Yes:** Multiple components, straightforward fix? -> **Level 2 (Simple Enhancement/Refactor)**
    *   **Yes:** Complex interactions, architectural impact? -> **Level 3 (Intermediate Feature/Bug)**
    *   **No (new feature/enhancement):**
        *   Small, self-contained addition? -> **Level 2 (Simple Enhancement)**
        *   Complete new feature, multiple components, needs design? -> **Level 3 (Intermediate Feature)**
        *   System-wide, major subsystem, deep architectural design? -> **Level 4 (Complex System)**

## 📝 ACTION: DOCUMENT & ANNOUNCE COMPLEXITY

1.  **Determine Level:** Decide Level 1, 2, 3, or 4.
2.  **Document in `activeContext.md`:** Use `edit_file` to update `memory-bank/activeContext.md`:
    ```markdown
    ## Task Complexity Assessment
    - Task: [User's request]
    - Determined Complexity: Level [1/2/3/4] - [Name]
    - Rationale: [Justification]
    ```
3.  **Update `tasks.md`:** Use `edit_file` to update `memory-bank/tasks.md` with the level, e.g., `Level 3: Implement user auth`.
4.  **Announce & Next Step:**
    *   State: "Assessed as Level [N]: [Name]."
    *   **Level 1:** "Proceeding with Level 1 workflow. Will `fetch_rules` for `.cursor/rules/isolation_rules/Level1/workflow-level1.mdc` (or directly to IMPLEMENT map if simple enough, e.g., `visual-maps/implement-mode-map.mdc` which might then fetch a Level 1 implement rule)."
    *   **Level 2-4:** "Requires detailed planning. Transitioning to PLAN mode. Will `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/plan-mode-map.mdc`."
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/creative-phase-enforcement.mdc",
            "description": "Core rule for enforcing Creative Phase completion for Level 3-4 tasks before allowing IMPLEMENT mode.",
            "globs": "**/Core/creative-phase-enforcement.mdc",
            "alwaysApply": False,
            "body": """
# CREATIVE PHASE ENFORCEMENT

> **TL;DR:** For L3/L4 tasks, if `tasks.md` flags items for "CREATIVE Phase", they MUST be completed before IMPLEMENT.

## 🔍 ENFORCEMENT WORKFLOW (AI Actions)
(Typically invoked by IMPLEMENT mode orchestrator for L3/L4 tasks, or by PLAN mode before suggesting IMPLEMENT)

1.  **Check Task Level & Creative Flags:**
    a.  `read_file` `memory-bank/activeContext.md` (for task level).
    b.  `read_file` `memory-bank/tasks.md`. Scan current feature's sub-tasks for incomplete "CREATIVE: Design..." entries.
2.  **Decision:**
    *   **If uncompleted CREATIVE tasks for L3/L4 feature:**
        a.  State: "🚨 IMPLEMENTATION BLOCKED for [feature]. Creative designs needed for: [list uncompleted creative tasks]."
        b.  Suggest: "Initiate CREATIVE mode (e.g., 'CREATIVE design [component]')." Await user.
    *   **Else (No uncompleted creative tasks or not L3/L4):**
        a.  State: "Creative phase requirements met/not applicable. Proceeding."
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/creative-phase-metrics.mdc",
            "description": "Core reference on metrics and quality assessment for Creative Phase outputs. For AI understanding of quality expectations.",
            "globs": "**/Core/creative-phase-metrics.mdc",
            "alwaysApply": False, 
            "body": """
# CREATIVE PHASE METRICS & QUALITY ASSESSMENT (AI Guidance)

> **TL;DR:** This outlines quality expectations for `creative-*.md` documents. Use this as a guide when generating or reviewing creative outputs.

## 📊 QUALITY EXPECTATIONS FOR `memory-bank/creative/creative-[feature_name].md` (AI Self-Guide)
A good creative document (created/updated via `edit_file`) should cover:
1.  **Problem & Objectives:** Clearly defined. What problem is this design solving? What are the goals?
2.  **Requirements & Constraints:** List functional and non-functional requirements. Note any technical or business constraints.
3.  **Options Explored:** At least 2-3 viable design options should be considered and briefly described.
4.  **Analysis of Options:** For each option:
    *   Pros (advantages).
    *   Cons (disadvantages).
    *   Feasibility (technical, time, resources).
    *   Impact (on other system parts, user experience).
5.  **Recommended Design & Justification:** Clearly state the chosen design option and provide a strong rationale for why it was selected over others, referencing the analysis.
6.  **Implementation Guidelines:** High-level steps or considerations for implementing the chosen design. This is not a full plan, but key pointers for the IMPLEMENT phase.
7.  **Visualizations (if applicable):** Reference or describe any diagrams (e.g., flowcharts, component diagrams) that clarify the design. (Actual diagram creation might be a separate step or user-provided).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/file-verification.mdc",
            "description": "Core rule for AI to verify and create Memory Bank file structures, prioritizing `edit_file` for content and `run_terminal_cmd` for `mkdir`.",
            "globs": "**/Core/file-verification.mdc",
            "alwaysApply": False,
            "body": """
# OPTIMIZED FILE VERIFICATION & CREATION SYSTEM (Memory Bank Setup)

> **TL;DR:** Verify/create essential Memory Bank directories and files. Use `edit_file` to create/populate files, `run_terminal_cmd` (platform-aware) for `mkdir`. Log actions.

## ⚙️ AI ACTIONS FOR MEMORY BANK SETUP (Typically during early VAN)

1.  **Acknowledge:** State: "Performing Memory Bank file verification and setup."
2.  **Reference Paths:** Mentally (or by `read_file` if necessary) refer to `.cursor/rules/isolation_rules/Core/memory-bank-paths.mdc` for canonical paths.
3.  **Verify/Create `memory-bank/` Root Directory:**
    a.  Use `list_dir .` (project root) to check if `memory-bank/` exists.
    b.  If missing:
        i.  `run_terminal_cmd` (platform-aware, e.g., `mkdir memory-bank` or `New-Item -ItemType Directory -Path memory-bank`).
        ii. Verify creation (e.g., `list_dir .` again).
4.  **Verify/Create Core Subdirectories in `memory-bank/`:**
    a.  The subdirectories are: `creative/`, `reflection/`, `archive/`.
    b.  For each (e.g., `creative`):
        i.  `list_dir memory-bank/` to check if `memory-bank/creative/` exists.
        ii. If missing: `run_terminal_cmd` (e.g., `mkdir memory-bank/creative`). Verify.
5.  **Verify/Create Core `.md` Files in `memory-bank/` (Using `edit_file`):**
    a.  The core files are: `tasks.md`, `activeContext.md`, `progress.md`, `projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `style-guide.md`.
    b.  For each file (e.g., `tasks.md`):
        i.  Attempt to `read_file memory-bank/tasks.md`.
        ii. If it fails (file doesn't exist) or content is empty/default placeholder:
            Use `edit_file memory-bank/tasks.md` to write an initial template. Example for `tasks.md`:
            ```markdown
            # Memory Bank: Tasks

            ## Current Task
            - Task ID: T000
            - Name: [Task not yet defined]
            - Status: PENDING_INITIALIZATION
            - Complexity: Not yet assessed
            - Assigned To: AI

            ## Backlog
            (Empty)
            ```
            *(Provide similar minimal templates for other core files if creating them anew. `activeContext.md` could start with `# Active Context - Initialized [Timestamp]`).*
        iii. Optionally, `read_file memory-bank/tasks.md` again to confirm content.
6.  **Log Verification Actions:**
    a.  Use `edit_file` to append a summary to `memory-bank/activeContext.md` under a "File Verification Log" heading. List directories/files checked, created, or found existing. Note any errors.
    b.  Example log entry:
        ```markdown
        ### File Verification Log - [Timestamp]
        - Checked/Created `memory-bank/` directory.
        - Checked/Created `memory-bank/creative/` directory.
        - Checked/Created `memory-bank/tasks.md` (initial template written).
        - ... (other files/dirs) ...
        - Status: All essential Memory Bank structures verified/created.
        ```
7.  **Completion:** State: "Memory Bank file structure verification and setup complete."
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/hierarchical-rule-loading.mdc",
            "description": "Core design principle for Memory Bank: hierarchical/lazy loading of `.mdc` rules via `fetch_rules`.",
            "globs": "**/Core/hierarchical-rule-loading.mdc",
            "alwaysApply": False, 
            "body": """
# HIERARCHICAL RULE LOADING SYSTEM (Design Principle for AI)

> **TL;DR:** You achieve hierarchical/lazy rule loading by following instructions in main mode prompts or other `.mdc` rules that direct you to use `fetch_rules` to load specific `.mdc` rule files only when needed.

## 🧠 HOW YOU EXECUTE HIERARCHICAL LOADING:
1.  **Mode Activation:** Your main custom prompt for a mode (e.g., VAN) tells you to `fetch_rules` for its primary orchestrating `.mdc` (e.g., `visual-maps/van_mode_split/van-mode-map.mdc`).
2.  **Following Instructions:** That `.mdc` guides you. Some steps might instruct: "If [condition], then `fetch_rules` to load and follow `[specific_sub_rule.mdc]`." For example, `van-mode-map.mdc` might tell you to `fetch_rules` for `Core/complexity-decision-tree.mdc`.
3.  **Current Rule Focus:** Always operate based on the instructions from the most recently fetched and relevant rule. Once a fetched rule's instructions are complete, you "return" to the context of the rule that fetched it, or if it was a top-level fetch, you await further user instruction or mode transition.
4.  **Acknowledge Fetches:** When you `fetch_rules` for an `.mdc`, briefly state: "Fetched `.cursor/rules/isolation_rules/[rule_path]`. Now proceeding with its instructions."
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/memory-bank-paths.mdc",
            "description": "Defines canonical paths for core Memory Bank files and directories. CRITICAL reference for all file operations.",
            "globs": "**/Core/memory-bank-paths.mdc",
            "alwaysApply": True, 
            "body": """
# CORE MEMORY BANK FILE & DIRECTORY LOCATIONS

**CRITICAL REFERENCE:** Adhere strictly to these paths for all file operations (`edit_file`, `read_file`, `list_dir`, `run_terminal_cmd` for `mkdir`).

## Root Memory Bank Directory:
*   `memory-bank/` (at project root)

## Core `.md` Files (in `memory-bank/`):
*   Tasks: `memory-bank/tasks.md`
*   Active Context: `memory-bank/activeContext.md`
*   Progress: `memory-bank/progress.md`
*   Project Brief: `memory-bank/projectbrief.md`
*   Product Context: `memory-bank/productContext.md`
*   System Patterns: `memory-bank/systemPatterns.md`
*   Tech Context: `memory-bank/techContext.md`
*   Style Guide: `memory-bank/style-guide.md`

## Subdirectories in `memory-bank/`:
*   Creative: `memory-bank/creative/` (Files: `creative-[feature_or_component_name]-[YYYYMMDD].md`)
*   Reflection: `memory-bank/reflection/` (Files: `reflect-[task_id_or_feature_name]-[YYYYMMDD].md`)
*   Archive: `memory-bank/archive/` (Files: `archive-[task_id_or_feature_name]-[YYYYMMDD].md`)

## Project Documentation Directory (Separate from Memory Bank, but related):
*   `documentation/` (at project root, for final, polished, user-facing docs)

## AI Verification Mandate:
*   Before using `edit_file` on Memory Bank artifacts, confirm the path starts with `memory-bank/` or one of its specified subdirectories.
*   When creating new core files (e.g., `tasks.md`), use `edit_file` with the exact path (e.g., `memory-bank/tasks.md`).
*   For `run_terminal_cmd mkdir`, ensure correct target paths (e.g., `mkdir memory-bank/creative`).
*   Filenames for creative, reflection, and archive documents should include a descriptive name and a date (YYYYMMDD format is good practice).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/mode-transition-optimization.mdc",
            "description": "Core design principles for optimized mode transitions using `activeContext.md` as the handover document.",
            "globs": "**/Core/mode-transition-optimization.mdc",
            "alwaysApply": False, 
            "body": """
# MODE TRANSITION OPTIMIZATION (AI Actions)

> **TL;DR:** Efficient mode transitions are achieved by updating `memory-bank/activeContext.md` (via `edit_file`) before a transition. The next mode's orchestrator rule then reads this file for context.

## 🔄 CONTEXT TRANSFER PROCESS (AI Actions):

1.  **Before Current Mode Exits (or suggests exiting):**
    a.  Your current instructions (from main prompt or an `.mdc` via `fetch_rules`) will guide you to use `edit_file` to update `memory-bank/activeContext.md`.
    b.  This update should include a section like:
        ```markdown
        ## Mode Transition Prepared - [Timestamp]
        - **From Mode:** [Current Mode, e.g., PLAN]
        - **To Mode Recommended:** [Target Mode, e.g., CREATIVE or IMPLEMENT]
        - **Current Task Focus:** [Specific task name or ID from tasks.md]
        - **Key Outputs/Decisions from [Current Mode]:**
            - [Summary of what was achieved, e.g., "Plan for user authentication feature is complete."]
            - [Reference to key artifacts created/updated, e.g., "See `memory-bank/tasks.md` for detailed sub-tasks. Creative design needed for UI components."]
        - **Primary Goal for [Target Mode]:** [What the next mode should focus on, e.g., "Design UI mockups for login and registration pages."]
        ```
2.  **When New Mode Starts:**
    a.  The new mode's main custom prompt (in Cursor's Advanced Settings) will instruct you to `fetch_rules` for its primary orchestrating `.mdc` file (e.g., `visual-maps/creative-mode-map.mdc`).
    b.  That orchestrating `.mdc` will (as an early step) instruct you to `read_file memory-bank/activeContext.md` to understand the incoming context, task focus, and goals.

**Key Principle:** `memory-bank/activeContext.md` is the primary "handover document" between modes, managed by `edit_file`. Keep its "Mode Transition Prepared" section concise and actionable for the next mode.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/optimization-integration.mdc",
            "description": "Design overview of Memory Bank optimization strategies. For AI understanding of system goals.",
            "globs": "**/Core/optimization-integration.mdc",
            "alwaysApply": False, 
            "body": """
# MEMORY BANK OPTIMIZATION INTEGRATION (AI Understanding)

> **TL;DR:** You enact Memory Bank optimizations by following specific instructions from other rule files that guide hierarchical rule loading, adaptive complexity, and progressive documentation. This is not a standalone process you run, but a result of adhering to the CMB framework.

## 🔄 HOW YOU ACHIEVE OPTIMIZATIONS:
You don't "run" an optimization integration flow. You achieve system optimizations by:
1.  **Hierarchical Rule Loading:** Following `fetch_rules` instructions in main prompts and other `.mdc` files to load only necessary rules when they are needed. This keeps your immediate context focused and relevant. (See `Core/hierarchical-rule-loading.mdc`).
2.  **Adaptive Complexity Model:** Following `Core/complexity-decision-tree.mdc` (when fetched in VAN mode) to assess task complexity. Then, loading level-specific rules (from `LevelX/` directories) as directed by subsequent instructions. This tailors the process to the task's needs.
3.  **Dynamic Context Management:** Diligently using `read_file` to get context from, and `edit_file` to update, key Memory Bank files like `memory-bank/activeContext.md`, `memory-bank/tasks.md`, and `memory-bank/progress.md`. This ensures context is current and progressively built.
4.  **Transition Optimization:** Following the process in `Core/mode-transition-optimization.mdc` (i.e., updating `activeContext.md` before a mode switch to ensure smooth handover).
5.  **Creative Phase Optimization:** Using templates and structured guidance like `Phases/CreativePhase/optimized-creative-template.mdc` (when fetched in CREATIVE mode) to ensure thorough but efficient design exploration.
6.  **Tool Prioritization:** Consistently using the right tool for the job (e.g., `edit_file` for content, `run_terminal_cmd` for execution) as outlined in `Core/command-execution.mdc`. This avoids inefficient or error-prone methods.

**This document explains the *design goals* of the CMB system. Your role is to execute the specific, actionable instructions in other `.mdc` files. By following those rules, you are inherently participating in and enabling these optimizations.**
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/Core/platform-awareness.mdc",
            "description": "Core guidelines for platform-aware command execution with `run_terminal_cmd`.",
            "globs": "**/Core/platform-awareness.mdc",
            "alwaysApply": True, 
            "body": """
# PLATFORM AWARENESS SYSTEM (for `run_terminal_cmd`)

> **TL;DR:** When using `run_terminal_cmd`, be aware of OS differences (paths, common commands). If unsure, state your default command (Linux-style) and ask the user to confirm or provide the platform-specific version (e.g., for Windows PowerShell).

## 🔍 AI ACTION FOR PLATFORM AWARENESS:

1.  **Identify Need for `run_terminal_cmd`:** This tool is for tasks like `mkdir`, running scripts (e.g., `npm run build`, `python manage.py test`), installing packages (`pip install`, `npm install`), or other shell operations. **Do NOT use it for creating or editing file content; use `edit_file` for that.**
2.  **Consider Platform Differences:**
    *   **Path Separators:** `/` (common for Linux, macOS, and often works in modern Windows PowerShell) vs. `\` (traditional Windows). When constructing paths for commands, be mindful.
    *   **Common Commands:**
        *   Directory Creation: `mkdir -p path/to/dir` (Linux/macOS) vs. `New-Item -ItemType Directory -Path path\to\dir` or `mkdir path\to\dir` (Windows PowerShell).
        *   Listing Directory Contents: `ls -la` (Linux/macOS) vs. `Get-ChildItem` or `dir` (Windows PowerShell).
        *   File Deletion: `rm path/to/file` (Linux/macOS) vs. `Remove-Item path\to\file` (Windows PowerShell).
        *   Environment Variables: `export VAR=value` (Linux/macOS) vs. `$env:VAR="value"` (Windows PowerShell).
3.  **Execution Strategy with `run_terminal_cmd`:**
    a.  **Check Context:** `read_file memory-bank/techContext.md` or `memory-bank/activeContext.md` to see if the OS has been previously identified.
    b.  **If OS is Known:** Use the appropriate command syntax for that OS.
    c.  **If OS is Unknown or Unsure:**
        i.  State your intended action and the command you would typically use (default to Linux-style if no other info). Example: "To create the directory `my_app/src`, I would use `run_terminal_cmd` with `mkdir -p my_app/src`."
        ii. Ask for Confirmation/Correction: "Is this command correct for your operating system? If you are on Windows, please provide the PowerShell equivalent."
        iii. Await user confirmation or correction before proceeding with `run_terminal_cmd`.
    d.  **Clearly State Command:** Before execution, always state the exact command you are about to run with `run_terminal_cmd`.
4.  **Document Action and Outcome:**
    a.  After `run_terminal_cmd` completes, use `edit_file` to log the command, its full output (or a summary if very long), and success/failure status in `memory-bank/activeContext.md` under a "Terminal Command Log" or similar section. (Refer to `Core/command-execution.mdc` for the log template).

**This is a guiding principle. The key is to be *aware* of potential differences, default to a common standard (like Linux commands), and proactively seek clarification from the user when unsure to ensure `run_terminal_cmd` is used safely and effectively.**
"""
        }
    ])

    MDC_FILES_DATA.extend([
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/archive-mode-map.mdc",
            "description": "Orchestrates ARCHIVE mode. Fetched when ARCHIVE process starts. Guides AI to finalize task documentation, create archive record, and update Memory Bank using level-specific rules and `edit_file`.",
            "globs": "**/visual-maps/archive-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# ARCHIVE MODE: TASK DOCUMENTATION PROCESS MAP (AI Instructions)

> **TL;DR:** Finalize task documentation, create an archive record, and update Memory Bank. Use `edit_file` for all document interactions. This rule orchestrates by fetching level-specific archive rules.

## 🧭 ARCHIVE MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating ARCHIVE mode for the current task."
    b.  `read_file memory-bank/activeContext.md` to identify the current task name/ID and its determined complexity level.
    c.  `read_file memory-bank/tasks.md` to confirm task details and status (especially if REFLECT phase is marked complete).
    d.  `read_file memory-bank/reflection/` (specifically the reflection document related to the current task, e.g., `reflect-[task_name_or_id]-[date].md`).
    e.  `read_file memory-bank/progress.md` for any relevant final notes.
2.  **Pre-Archive Check (AI Self-Correction):**
    a.  Verify from `tasks.md` that the REFLECT phase for the current task is marked as complete.
    b.  Verify that the corresponding reflection document (e.g., `memory-bank/reflection/reflect-[task_name_or_id]-[date].md`) exists and appears finalized.
    c.  If checks fail: State "ARCHIVE BLOCKED: Reflection phase is not complete or reflection document is missing/incomplete for task [task_name]. Please complete REFLECT mode first." Await user.
3.  **Fetch Level-Specific Archive Rule:**
    a.  Based on the complexity level identified in `activeContext.md` or `tasks.md`:
        *   **Level 1:** `fetch_rules` for `.cursor/rules/isolation_rules/Level1/archive-minimal.mdc`.
        *   **Level 2:** `fetch_rules` for `.cursor/rules/isolation_rules/Level2/archive-basic.mdc`.
        *   **Level 3:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/archive-intermediate.mdc`.
        *   **Level 4:** `fetch_rules` for `.cursor/rules/isolation_rules/Level4/archive-comprehensive.mdc`.
4.  **Follow Fetched Rule:**
    a.  The fetched level-specific `.mdc` rule will provide detailed instructions for:
        i.  Creating the main archive document (e.g., `memory-bank/archive/archive-[task_name_or_id]-[date].md`) using `edit_file`. This includes summarizing the task, requirements, implementation, testing, and lessons learned (drawing from reflection docs).
        ii.  Potentially archiving other relevant documents (e.g., creative phase documents for L3/L4) by copying their content or linking to them within the main archive document.
        iii. Updating `memory-bank/tasks.md` to mark the task as "ARCHIVED" or "COMPLETED" using `edit_file`.
        iv. Updating `memory-bank/progress.md` with a final entry about archiving using `edit_file`.
        v.  Updating `memory-bank/activeContext.md` to clear the current task focus and indicate readiness for a new task, using `edit_file`.
5.  **Notify Completion:**
    a.  Once the fetched rule's instructions are complete, state: "ARCHIVING COMPLETE for task [task_name]. The archive document is located at `[path_to_archive_doc]`."
    b.  Recommend: "The Memory Bank is ready for the next task. Suggest using VAN mode to initiate a new task." Await user.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/creative-mode-map.mdc",
            "description": "Orchestrates CREATIVE mode. Fetched by PLAN mode when design is needed. Guides AI to facilitate design for components flagged in `tasks.md`, using `fetch_rules` for design-type guidance and `edit_file` for documentation.",
            "globs": "**/visual-maps/creative-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# CREATIVE MODE: DESIGN PROCESS MAP (AI Instructions)

> **TL;DR:** Facilitate design for components flagged in `tasks.md` as needing creative input. Use `fetch_rules` to get specific design-type guidance (Arch, UI/UX, Algo) and `edit_file` to create/update `memory-bank/creative/creative-[component_name]-[date].md` documents.

## 🧭 CREATIVE MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating CREATIVE mode. Identifying components requiring design."
    b.  `read_file memory-bank/tasks.md`. Look for sub-tasks under the current main task that are marked like "CREATIVE: Design [Component Name] ([Design Type: Architecture/UI-UX/Algorithm])" and are not yet complete.
    c.  `read_file memory-bank/activeContext.md` for overall project context and the current main task focus.
    d.  If no active "CREATIVE: Design..." sub-tasks are found for the current main task, state: "No pending creative design tasks found for [main_task_name]. Please specify a component and design type, or transition to another mode." Await user.
2.  **Iterate Through Pending Creative Sub-Tasks:**
    a.  For each pending "CREATIVE: Design [Component Name] ([Design Type])" sub-task:
        i.  Announce: "Starting CREATIVE phase for: [Component Name] - Design Type: [Architecture/UI-UX/Algorithm]."
        ii. Update `memory-bank/activeContext.md` using `edit_file` to set current focus: "Creative Focus: Designing [Component Name] ([Design Type])."
        iii. **Fetch Specific Design-Type Rule:**
            *   If Design Type is Architecture: `fetch_rules` for `.cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-architecture.mdc`.
            *   If Design Type is UI/UX: `fetch_rules` for `.cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-uiux.mdc`.
            *   If Design Type is Algorithm: `fetch_rules` for `.cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-algorithm.mdc`.
            *   (If design type is other/generic, fetch `Phases/CreativePhase/optimized-creative-template.mdc` and adapt general design principles).
        iv. **Follow Fetched Rule:** The fetched rule will guide you through:
            *   Defining the problem for that component.
            *   Exploring options.
            *   Analyzing trade-offs.
            *   Making a design decision.
            *   Outlining implementation guidelines.
        v.  **Document Design:**
            *   The fetched rule will instruct you to use `edit_file` to create or update the specific creative document: `memory-bank/creative/creative-[component_name]-[date].md`.
            *   It will likely reference `.cursor/rules/isolation_rules/Phases/CreativePhase/optimized-creative-template.mdc` (which you can `read_file` if not fetched directly) for the structure of this document.
        vi. **Update `memory-bank/activeContext.md`:** Use `edit_file` to append a summary of the design decision for [Component Name] to a "Creative Decisions Log" section.
        vii. **Update `memory-bank/tasks.md`:** Use `edit_file` to mark the "CREATIVE: Design [Component Name]..." sub-task as complete.
3.  **Overall Verification & Transition:**
    a.  After all identified creative sub-tasks for the main task are complete, state: "All CREATIVE design phases for [main_task_name] are complete. Design documents are located in `memory-bank/creative/`."
    b.  Recommend next mode: "Recommend transitioning to IMPLEMENT mode to build these components, or VAN QA mode for technical pre-flight checks if applicable." Await user.

## 📊 PRE-CREATIVE CHECK (AI Self-Correction):
1.  `read_file memory-bank/tasks.md`: Is there a main task currently in a state that expects creative design (e.g., PLAN phase completed, and specific "CREATIVE: Design..." sub-tasks are listed and pending)?
2.  If not, or if PLAN phase is not complete for the main task, state: "CREATIVE mode requires a planned task with identified components for design. Please ensure PLAN mode is complete for [main_task_name] and creative sub-tasks are defined in `tasks.md`." Await user.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/implement-mode-map.mdc",
            "description": "Orchestrates IMPLEMENT mode. Fetched after PLAN/CREATIVE. Guides AI to implement features/fixes using level-specific rules, `edit_file` for code, `run_terminal_cmd` for builds/tests, and `Core/command-execution.mdc` for tool usage.",
            "globs": "**/visual-maps/implement-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# IMPLEMENT MODE: CODE EXECUTION PROCESS MAP (AI Instructions)

> **TL;DR:** Implement the planned and designed features or bug fixes. Use `edit_file` for all code and documentation changes. Use `run_terminal_cmd` for builds, tests, etc. Fetch level-specific implementation rules and `Core/command-execution.mdc` for detailed tool guidance.

## 🧭 IMPLEMENT MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating IMPLEMENT mode for the current task."
    b.  `read_file memory-bank/activeContext.md` to identify the current task, its complexity level, and any outputs from PLAN/CREATIVE modes.
    c.  `read_file memory-bank/tasks.md` for the detailed sub-tasks, implementation plan, and references to creative design documents.
    d.  `read_file memory-bank/progress.md` for any ongoing implementation status.
    e.  If L3/L4 task, `read_file` relevant `memory-bank/creative/creative-[component]-[date].md` documents.
2.  **Pre-Implementation Checks (AI Self-Correction):**
    a.  **PLAN Complete?** Verify in `tasks.md` that the planning phase for the current task is marked complete.
    b.  **CREATIVE Complete (for L3/L4)?** `fetch_rules` for `.cursor/rules/isolation_rules/Core/creative-phase-enforcement.mdc` to check. If it blocks, await user action (e.g., switch to CREATIVE mode).
    c.  **VAN QA Passed (if applicable)?** Check `activeContext.md` or a dedicated status file if VAN QA was run. If VAN QA failed, state: "IMPLEMENTATION BLOCKED: VAN QA checks previously failed. Please resolve issues and re-run VAN QA." Await user.
    d.  If any critical pre-check fails, state the blockage and await user instruction.
3.  **Fetch General Command Execution Guidelines:**
    a.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/command-execution.mdc`. Keep these guidelines in mind for all tool usage.
4.  **Fetch Level-Specific Implementation Rule:**
    a.  Based on the complexity level:
        *   **Level 1:** `fetch_rules` for `.cursor/rules/isolation_rules/Level1/workflow-level1.mdc` (or a more specific L1 implement rule if it exists, e.g., `Level1/implement-quick-fix.mdc`).
        *   **Level 2:** `fetch_rules` for `.cursor/rules/isolation_rules/Level2/workflow-level2.mdc` (or `Level2/implement-basic.mdc`).
        *   **Level 3:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/implementation-intermediate.mdc`.
        *   **Level 4:** `fetch_rules` for `.cursor/rules/isolation_rules/Level4/phased-implementation.mdc`.
5.  **Follow Fetched Rule (Iterative Implementation):**
    a.  The level-specific rule will guide you through the implementation steps, which will involve:
        i.  Identifying the next specific sub-task from `tasks.md`.
        ii. Creating/modifying source code files using `edit_file`.
        iii. Creating/modifying documentation (e.g., code comments, README sections) using `edit_file`.
        iv. Running build scripts or compilers using `run_terminal_cmd` (platform-aware).
        v.  Running tests using `run_terminal_cmd`.
        vi. Verifying file creation/modification (e.g., using `read_file` or `list_dir`).
        vii. Documenting each significant action (tool used, command, outcome) in `memory-bank/activeContext.md` (in a "Build Log" section) using `edit_file`.
        viii. Updating `memory-bank/progress.md` with detailed progress for each sub-task using `edit_file`.
        ix. Updating `memory-bank/tasks.md` to mark sub-tasks as complete using `edit_file`.
    b.  This is an iterative process. Continue until all implementation sub-tasks in `tasks.md` are complete.
6.  **Notify Completion:**
    a.  Once all implementation sub-tasks are complete, state: "IMPLEMENTATION COMPLETE for task [task_name]."
    b.  Update `memory-bank/tasks.md` to mark the main IMPLEMENT phase as complete.
    c.  Update `memory-bank/activeContext.md`: "Implementation phase complete for [task_name]. Ready for REFLECT mode."
    d.  Recommend: "Recommend transitioning to REFLECT mode for review and lessons learned." Await user.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/plan-mode-map.mdc",
            "description": "Orchestrates PLAN mode. Fetched by VAN for L2+ tasks. Guides AI to create detailed plans in `tasks.md` using level-specific rules, `edit_file`, and identifies needs for CREATIVE mode.",
            "globs": "**/visual-maps/plan-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# PLAN MODE: TASK PLANNING PROCESS MAP (AI Instructions)

> **TL;DR:** Create a detailed implementation plan for Level 2-4 tasks. Update `tasks.md` extensively using `edit_file`. Identify components needing CREATIVE design. Fetch level-specific planning rules for detailed guidance.

## 🧭 PLAN MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating PLAN mode for the current task."
    b.  `read_file memory-bank/activeContext.md` to understand the task name, determined complexity level (should be L2, L3, or L4), and any initial notes from VAN mode.
    c.  `read_file memory-bank/tasks.md` for the current state of the task entry.
    d.  `read_file memory-bank/projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md` for broader project understanding.
2.  **Pre-Planning Check (AI Self-Correction):**
    a.  Verify from `activeContext.md` or `tasks.md` that the task complexity is indeed Level 2, 3, or 4.
    b.  If complexity is Level 1 or not assessed, state: "PLAN mode is intended for Level 2-4 tasks. Current task is [Level/Status]. Please clarify or run VAN mode for complexity assessment." Await user.
3.  **Fetch Level-Specific Planning Rule:**
    a.  Based on the complexity level:
        *   **Level 2:** `fetch_rules` for `.cursor/rules/isolation_rules/Level2/task-tracking-basic.mdc` (or a dedicated L2 planning rule like `Level2/planning-basic.mdc` if it exists).
        *   **Level 3:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/planning-comprehensive.mdc`.
        *   **Level 4:** `fetch_rules` for `.cursor/rules/isolation_rules/Level4/architectural-planning.mdc`.
4.  **Follow Fetched Rule (Detailed Planning):**
    a.  The fetched level-specific rule will guide you through the detailed planning steps, which will involve extensive updates to `memory-bank/tasks.md` using `edit_file`. This includes:
        i.  Breaking down the main task into smaller, actionable sub-tasks.
        ii. Defining requirements, acceptance criteria for each sub-task.
        iii. Identifying affected components, files, or modules.
        iv. Estimating effort/dependencies for sub-tasks (qualitatively).
        v.  **Crucially for L3/L4:** Identifying specific components or aspects that require a dedicated CREATIVE design phase (e.g., "CREATIVE: Design User Authentication UI", "CREATIVE: Design Database Schema for Orders"). These should be added as specific sub-tasks in `tasks.md`.
        vi. Outlining a high-level implementation sequence.
        vii. Documenting potential challenges and mitigation strategies.
    b.  Throughout this process, use `edit_file` to meticulously update the relevant sections in `memory-bank/tasks.md`.
    c.  Update `memory-bank/activeContext.md` periodically with planning progress notes using `edit_file`.
5.  **Technology Validation (Conceptual - AI doesn't run code here but plans for it):**
    a.  The fetched planning rule might instruct you to consider and document the technology stack, any new dependencies, or build configurations needed. This is documented in `tasks.md` or `techContext.md` using `edit_file`.
    b.  If significant new technologies or complex configurations are involved, add a sub-task in `tasks.md` for "VAN QA: Technical Validation" to be performed before IMPLEMENT.
6.  **Notify Completion & Recommend Next Mode:**
    a.  Once the detailed plan is formulated in `tasks.md` as per the fetched rule, state: "PLANNING COMPLETE for task [task_name]. Detailed plan and sub-tasks are updated in `memory-bank/tasks.md`."
    b.  Update `memory-bank/tasks.md` to mark the main PLAN phase as complete.
    c.  Update `memory-bank/activeContext.md`: "Planning phase complete for [task_name]."
    d.  **Recommendation:**
        *   If "CREATIVE: Design..." sub-tasks were identified: "Recommend transitioning to CREATIVE mode to address design requirements."
        *   If no CREATIVE sub-tasks (e.g., simpler L2 task) and no VAN QA flagged: "Recommend transitioning to IMPLEMENT mode."
        *   If VAN QA was flagged as needed: "Recommend transitioning to VAN QA mode for technical pre-flight checks."
    e.  Await user instruction.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/qa-mode-map.mdc",
            "description": "Orchestrates general QA mode (distinct from VAN QA). Fetched when user invokes 'QA'. Guides AI to perform context-aware validation of Memory Bank consistency, task tracking, and phase-specific checks.",
            "globs": "**/visual-maps/qa-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# QA MODE: GENERAL VALIDATION PROCESS MAP (AI Instructions)

> **TL;DR:** Perform comprehensive validation of Memory Bank consistency, task tracking, and current phase status. This is a general QA mode, callable anytime, distinct from the pre-build VAN QA. Use `read_file` extensively and `edit_file` to log QA findings.

## 🧭 QA MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating general QA MODE. Analyzing current project state."
    b.  `read_file memory-bank/activeContext.md` to determine the current task, its perceived phase (VAN, PLAN, CREATIVE, IMPLEMENT, REFLECT, ARCHIVE), and complexity.
    c.  `read_file memory-bank/tasks.md` for task statuses and details.
    d.  `read_file memory-bank/progress.md` for activity log.
2.  **Universal Validation Checks (AI Self-Correction & Reporting):**
    a.  **Memory Bank Core File Integrity:**
        i.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/memory-bank-paths.mdc` to get list of core files.
        ii. For each core file: Attempt `read_file`. Report if any are missing or seem corrupted (e.g., empty when they shouldn't be).
    b.  **`tasks.md` Consistency:**
        i.  Is there a clearly defined current task?
        ii. Are statuses (PENDING, IN_PROGRESS, COMPLETE, BLOCKED, CREATIVE_NEEDED, QA_NEEDED, REFLECT_NEEDED, ARCHIVE_NEEDED) used consistently?
        iii. Do sub-tasks roll up logically to the main task's status?
    c.  **`activeContext.md` Relevance:**
        i.  Does the `activeContext.md` accurately reflect the current focus apparent from `tasks.md` and `progress.md`?
        ii. Is the "Last Updated" timestamp recent relative to `progress.md`?
    d.  **`progress.md` Completeness:**
        i.  Are there entries for recent significant activities?
        ii. Do entries clearly state actions taken and outcomes?
    e.  **Cross-Reference Check (Conceptual):**
        i.  Do task IDs in `progress.md` or `activeContext.md` match those in `tasks.md`?
        ii. Do references to creative/reflection/archive documents seem plausible (e.g., filenames match task names)?
3.  **Phase-Specific Validation (Based on perceived current phase from `activeContext.md`):**
    *   **If VAN phase:** Are `projectbrief.md`, `techContext.md` populated? Is complexity assessed in `tasks.md`?
    *   **If PLAN phase:** Is `tasks.md` detailed with sub-tasks, requirements? Are creative needs identified for L3/L4?
    *   **If CREATIVE phase:** Do `memory-bank/creative/` documents exist for components marked in `tasks.md`? Are decisions logged in `activeContext.md`?
    *   **If IMPLEMENT phase:** Is there a "Build Log" in `activeContext.md`? Is `progress.md` being updated with code changes and test results? Are sub-tasks in `tasks.md` being marked complete?
    *   **If REFLECT phase:** Does `memory-bank/reflection/reflect-[task_name]-[date].md` exist and seem complete? Is `tasks.md` updated for reflection?
    *   **If ARCHIVE phase:** Does `memory-bank/archive/archive-[task_name]-[date].md` exist? Is `tasks.md` marked fully complete/archived?
4.  **Report Generation:**
    a.  Use `edit_file` to create a new QA report in `memory-bank/qa_reports/qa-report-[date]-[time].md`.
    b.  **Structure of the report:**
        ```markdown
        # General QA Report - [Date] [Time]
        - Perceived Current Task: [Task Name/ID]
        - Perceived Current Phase: [Phase]
        - Perceived Complexity: [Level]

        ## Universal Validation Findings:
        - Memory Bank Core Files: [OK/Issues found: list them]
        - `tasks.md` Consistency: [OK/Issues found: list them]
        - `activeContext.md` Relevance: [OK/Issues found: list them]
        - `progress.md` Completeness: [OK/Issues found: list them]
        - Cross-References: [OK/Issues found: list them]

        ## Phase-Specific ([Phase]) Validation Findings:
        - [Check 1]: [OK/Issue]
        - [Check 2]: [OK/Issue]

        ## Summary & Recommendations:
        - Overall Status: [GREEN/YELLOW/RED]
        - [Specific recommendations for fixes or areas to improve]
        ```
    c.  Announce: "General QA validation complete. Report generated at `memory-bank/qa_reports/qa-report-[date]-[time].md`."
    d.  Present a summary of key findings (especially any RED/YELLOW status items) directly to the user.
5.  **Await User Action:** Await user instructions for addressing any reported issues or proceeding.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/reflect-mode-map.mdc",
            "description": "Orchestrates REFLECT mode. Fetched after IMPLEMENT. Guides AI to review implementation, document lessons in `reflection/...md`, and update Memory Bank using level-specific rules and `edit_file`.",
            "globs": "**/visual-maps/reflect-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# REFLECT MODE: TASK REVIEW PROCESS MAP (AI Instructions)

> **TL;DR:** Review the completed implementation, document insights and lessons learned in `memory-bank/reflection/reflect-[task_name]-[date].md`. Use `edit_file` for all documentation. Fetch level-specific reflection rules for detailed guidance.

## 🧭 REFLECT MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating REFLECT mode for the current task."
    b.  `read_file memory-bank/activeContext.md` to identify the current task, its complexity level, and confirmation that IMPLEMENT phase is complete.
    c.  `read_file memory-bank/tasks.md` for the original plan, sub-tasks, and requirements.
    d.  `read_file memory-bank/progress.md` to review the implementation journey and any challenges logged.
    e.  `read_file` any relevant `memory-bank/creative/creative-[component]-[date].md` documents (for L3/L4) to compare design with implementation.
2.  **Pre-Reflection Check (AI Self-Correction):**
    a.  Verify from `tasks.md` or `activeContext.md` that the IMPLEMENT phase for the current task is marked as complete.
    b.  If not, state: "REFLECT BLOCKED: Implementation phase is not yet complete for task [task_name]. Please complete IMPLEMENT mode first." Await user.
3.  **Fetch Level-Specific Reflection Rule:**
    a.  Based on the complexity level:
        *   **Level 1:** `fetch_rules` for `.cursor/rules/isolation_rules/Level1/reflection-basic.mdc`. (If not present, use L2)
        *   **Level 2:** `fetch_rules` for `.cursor/rules/isolation_rules/Level2/reflection-basic.mdc`. (Note: `rules-visual-maps.txt` refers to `reflection-standard.md` for L2, I'll use `reflection-basic` as per `STRUCTURE.md` or assume they are similar. If a specific `reflection-standard.mdc` exists, use that).
        *   **Level 3:** `fetch_rules` for `.cursor/rules/isolation_rules/Level3/reflection-intermediate.mdc`.
        *   **Level 4:** `fetch_rules` for `.cursor/rules/isolation_rules/Level4/reflection-comprehensive.mdc`.
4.  **Follow Fetched Rule (Structured Reflection):**
    a.  The fetched level-specific `.mdc` rule will guide you through the reflection process, which involves creating/updating `memory-bank/reflection/reflect-[task_name_or_id]-[date].md` using `edit_file`. Key sections to populate (guided by the fetched rule):
        i.  **Summary of Task & Outcome:** What was built, did it meet goals?
        ii. **What Went Well:** Successful aspects, efficient processes.
        iii. **Challenges Encountered:** Difficulties, roadblocks, unexpected issues. How were they overcome?
        iv. **Lessons Learned:** Key takeaways, new knowledge gained (technical, process-wise).
        v.  **Comparison with Plan/Design:** Deviations from original plan/design and why.
        vi. **Process Improvements:** Suggestions for future tasks.
        vii. **Technical Improvements/Alternatives:** Better technical approaches for similar future tasks.
        viii. **Code Quality/Maintainability Assessment (if applicable).**
    b.  Use `edit_file` to meticulously populate the reflection document.
    c.  Update `memory-bank/activeContext.md` with notes like "Reflection in progress for [task_name]."
5.  **Notify Completion:**
    a.  Once the reflection document is complete as per the fetched rule, state: "REFLECTION COMPLETE for task [task_name]. Reflection document created/updated at `memory-bank/reflection/reflect-[task_name_or_id]-[date].md`."
    b.  Use `edit_file` to update `memory-bank/tasks.md`, marking the REFLECT phase as complete for the task.
    c.  Use `edit_file` to update `memory-bank/activeContext.md`: "Reflection phase complete for [task_name]. Ready for ARCHIVE mode."
    d.  Recommend: "Recommend transitioning to ARCHIVE mode to finalize and store task documentation." Await user.
"""
        },
        # --- VAN Mode Split Files ---
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-mode-map.mdc",
            "description": "Main orchestrator for VAN mode: platform detection, file verification, complexity determination, and optional QA. Fetched when VAN mode starts.",
            "globs": "**/visual-maps/van_mode_split/van-mode-map.mdc",
            "alwaysApply": False,
            "body": """
# VAN MODE: INITIALIZATION PROCESS MAP (AI Instructions)

> **TL;DR:** Initialize project: platform detection, file verification, complexity determination. For L2+ tasks, transition to PLAN. For L1, complete initialization. If 'VAN QA' is called, perform technical validation. This rule orchestrates by fetching specific sub-rules.

## 🧭 VAN MODE PROCESS FLOW (AI Actions)

1.  **Acknowledge & Determine Entry Point:**
    *   If user typed "VAN": Respond "OK VAN - Beginning Initialization Process." Proceed with step 2.
    *   If user typed "VAN QA": Respond "OK VAN QA - Beginning Technical Validation." Skip to step 6.
2.  **Platform Detection (Sub-Rule):**
    a.  State: "Performing platform detection."
    b.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-platform-detection.mdc`.
    c.  (The fetched rule will guide OS detection and logging to `activeContext.md` via `edit_file`).
3.  **File Verification & Creation (Memory Bank Setup) (Sub-Rule):**
    a.  State: "Performing Memory Bank file verification and setup."
    b.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
    c.  (The fetched rule guides checking/creating `memory-bank/` dir, subdirs, and core `.md` files using `edit_file` and `run_terminal_cmd`).
4.  **Early Complexity Determination (Sub-Rule):**
    a.  State: "Determining task complexity."
    b.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/Core/complexity-decision-tree.mdc`.
    c.  (The fetched rule guides assessing Level 1-4 and updating `activeContext.md` and `tasks.md` via `edit_file`).
    d.  `read_file memory-bank/activeContext.md` to confirm the determined complexity level.
5.  **Mode Transition based on Complexity:**
    a.  **If Level 1 determined:**
        i.  State: "Task assessed as Level 1. Completing VAN initialization."
        ii. Use `edit_file` to update `memory-bank/activeContext.md` with: "VAN Process Status: Level 1 Initialization Complete. Task ready for IMPLEMENT mode."
        iii. State: "VAN Initialization Complete for Level 1 task [Task Name]. Recommend IMPLEMENT mode." Await user.
    b.  **If Level 2, 3, or 4 determined:**
        i.  State: "🚫 LEVEL [2/3/4] TASK DETECTED: [Task Name]. This task REQUIRES detailed planning."
        ii. State: "Transitioning to PLAN mode is necessary. Type 'PLAN' to proceed with planning." Await user.
        iii. (VAN mode is effectively paused here for L2-4 tasks. The user will initiate PLAN mode, which has its own orchestrator).
6.  **VAN QA - Technical Validation (Entry point if "VAN QA" was typed, or if called after CREATIVE mode by user):**
    a.  State: "Initiating VAN QA Technical Validation."
    b.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-main.mdc`.
    c.  (The `van-qa-main.mdc` will orchestrate the entire QA process, fetching further sub-rules for specific checks and reporting).
    d.  After `van-qa-main.mdc` completes, it will have provided a summary and recommended next steps (e.g., proceed to BUILD or fix issues). Await user action based on that QA report.

## 🔄 QA COMMAND PRECEDENCE (If user types "QA" during steps 2-4 of VAN Initialization)
1.  State: "General QA command received, pausing current VAN initialization step ([current step])."
2.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/visual-maps/qa-mode-map.mdc` (the general QA orchestrator).
3.  After general QA is complete (and any issues potentially addressed by the user):
    a.  State: "Resuming VAN initialization."
    b.  Re-evaluate or continue from the paused VAN initialization step. For example, if paused during complexity determination, complete it, then proceed to step 5.
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-platform-detection.mdc",
            "description": "VAN sub-rule for platform detection. Fetched by `van-mode-map.mdc`. Guides AI to detect OS and document in `activeContext.md`.",
            "globs": "**/visual-maps/van_mode_split/van-platform-detection.mdc",
            "alwaysApply": False,
            "body": """
# VAN MODE: PLATFORM DETECTION (AI Instructions)

> **TL;DR:** Detect the Operating System. Document the detected OS and path separator style in `memory-bank/activeContext.md` and `memory-bank/techContext.md` using `edit_file`. This rule is typically fetched by `van-mode-map.mdc`.

## ⚙️ AI ACTIONS FOR PLATFORM DETECTION:

1.  **Acknowledge:** State: "Attempting to determine Operating System."
2.  **Attempt Detection (via `run_terminal_cmd` - carefully):**
    *   **Strategy:** Use a simple, non-destructive command that has distinct output or behavior across OSes.
    *   Example 1 (Check for `uname`):
        *   `run_terminal_cmd uname`
        *   If output is "Linux", "Darwin" (macOS), or similar: OS is Unix-like. Path separator likely `/`.
        *   If command fails or output is unrecognized: OS might be Windows.
    *   Example 2 (Check PowerShell specific variable, if assuming PowerShell might be present):
        *   `run_terminal_cmd echo $PSVersionTable.PSVersion` (PowerShell)
        *   If successful with version output: OS is Windows (with PowerShell). Path separator likely `\`.
        *   If fails: Not PowerShell, or not Windows.
    *   **If still unsure after one attempt, DO NOT run many speculative commands.**
3.  **Decision & User Interaction if Unsure:**
    a.  **If Confident:** (e.g., `uname` returned "Linux")
        i.  Detected OS: Linux. Path Separator: `/`.
    b.  **If Unsure:**
        i.  State: "Could not definitively determine the OS automatically."
        ii. Ask User: "Please specify your Operating System (e.g., Windows, macOS, Linux) and preferred path separator (`/` or `\\`)."
        iii. Await user response.
        iv. Detected OS: [User's response]. Path Separator: [User's response].
4.  **Document Findings:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md` with a section:
        ```markdown
        ## Platform Detection Log - [Timestamp]
        - Detected OS: [Windows/macOS/Linux/User-Specified]
        - Path Separator Style: [/ or \\]
        - Confidence: [High/Medium/Low/User-Provided]
        ```
    b.  Use `edit_file` to update (or create if not exists) `memory-bank/techContext.md` with:
        ```markdown
        # Technical Context
        ## Operating System
        - OS: [Windows/macOS/Linux/User-Specified]
        - Path Separator: [/ or \\]
        ## Key Command Line Interface (if known)
        - CLI: [Bash/Zsh/PowerShell/CMD/User-Specified]
        ```
5.  **Completion:** State: "Platform detection complete. OS identified as [OS_Name]. Proceeding with VAN initialization."
    (Control returns to the fetching rule, likely `van-mode-map.mdc`).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-file-verification.mdc",
            "description": "VAN sub-rule for initial Memory Bank file structure verification (DEPRECATED - Logic moved to Core/file-verification.mdc). This file is a placeholder.",
            "globs": "**/visual-maps/van_mode_split/van-file-verification.mdc",
            "alwaysApply": False,
            "body": """
# VAN MODE: FILE VERIFICATION (Placeholder - Logic Moved)

> **TL;DR:** This rule is a placeholder. The primary Memory Bank file verification and creation logic has been consolidated into `.cursor/rules/isolation_rules/Core/file-verification.mdc`.

## ⚙️ AI ACTION:

1.  **Acknowledge:** State: "Note: `van_mode_split/van-file-verification.mdc` is a placeholder. The main file verification logic is in `Core/file-verification.mdc`."
2.  **Guidance:** If you were instructed to perform initial Memory Bank file verification, you should have been (or should be) directed to `fetch_rules` for `.cursor/rules/isolation_rules/Core/file-verification.mdc`.

(Control returns to the fetching rule, likely `van-mode-map.mdc` which should fetch the Core rule directly).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-complexity-determination.mdc",
            "description": "VAN sub-rule for task complexity determination (DEPRECATED - Logic moved to Core/complexity-decision-tree.mdc). This file is a placeholder.",
            "globs": "**/visual-maps/van_mode_split/van-complexity-determination.mdc",
            "alwaysApply": False,
            "body": """
# VAN MODE: COMPLEXITY DETERMINATION (Placeholder - Logic Moved)

> **TL;DR:** This rule is a placeholder. The primary task complexity determination logic has been consolidated into `.cursor/rules/isolation_rules/Core/complexity-decision-tree.mdc`.

## ⚙️ AI ACTION:

1.  **Acknowledge:** State: "Note: `van_mode_split/van-complexity-determination.mdc` is a placeholder. The main complexity determination logic is in `Core/complexity-decision-tree.mdc`."
2.  **Guidance:** If you were instructed to determine task complexity, you should have been (or should be) directed to `fetch_rules` for `.cursor/rules/isolation_rules/Core/complexity-decision-tree.mdc`.

(Control returns to the fetching rule, likely `van-mode-map.mdc` which should fetch the Core rule directly).
"""
        },
        # --- VAN QA Main Orchestrator ---
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-main.mdc",
            "description": "Main orchestrator for VAN QA technical validation. Fetched by `van-mode-map.mdc` when 'VAN QA' is triggered. Fetches specific check rules and utility rules.",
            "globs": "**/visual-maps/van_mode_split/van-qa-main.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: TECHNICAL VALIDATION - MAIN ORCHESTRATOR (AI Instructions)

> **TL;DR:** Orchestrate the four-point technical validation (Dependencies, Configuration, Environment, Minimal Build Test) by fetching specific check rules. Then, fetch reporting and mode transition rules based on results. Use `edit_file` for logging to `activeContext.md`.

## 🧭 VAN QA PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context:**
    a.  State: "VAN QA Main Orchestrator activated. Starting technical validation process."
    b.  `read_file memory-bank/activeContext.md` for current task, complexity, and any relevant tech stack info from CREATIVE phase.
    c.  `read_file memory-bank/tasks.md` for task details.
    d.  `read_file memory-bank/techContext.md` (if it exists and is populated).
    e.  Use `edit_file` to add to `memory-bank/activeContext.md`: "VAN QA Log - [Timestamp]: Starting technical validation."
2.  **Perform Four-Point Validation (Fetch sub-rules sequentially):**
    a.  **Dependency Verification:**
        i.  State: "Performing Dependency Verification."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/dependency-check.mdc`.
        iii. (This rule will guide checks and log results to `activeContext.md`). Let `pass_dep_check` be true/false based on its outcome.
    b.  **Configuration Validation (if `pass_dep_check` is true):**
        i.  State: "Performing Configuration Validation."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/config-check.mdc`.
        iii. Let `pass_config_check` be true/false.
    c.  **Environment Validation (if `pass_config_check` is true):**
        i.  State: "Performing Environment Validation."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/environment-check.mdc`.
        iii. Let `pass_env_check` be true/false.
    d.  **Minimal Build Test (if `pass_env_check` is true):**
        i.  State: "Performing Minimal Build Test."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/build-test.mdc`.
        iii. Let `pass_build_check` be true/false.
3.  **Consolidate Results & Generate Report:**
    a.  Overall QA Status: `pass_qa = pass_dep_check AND pass_config_check AND pass_env_check AND pass_build_check`.
    b.  State: "Technical validation checks complete. Overall QA Status: [PASS/FAIL]."
    c.  `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/reports.mdc`.
    d.  Follow instructions in `reports.mdc` to use `edit_file` to:
        i.  Generate the full QA report (success or failure format) and display it to the user.
        ii. Write "PASS" or "FAIL" to `memory-bank/.qa_validation_status` (a hidden file for programmatic checks).
4.  **Determine Next Steps:**
    a.  **If `pass_qa` is TRUE:**
        i.  State: "All VAN QA checks passed."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/mode-transitions.mdc`.
        iii. (This rule will guide recommending BUILD mode).
    b.  **If `pass_qa` is FALSE:**
        i.  State: "One or more VAN QA checks failed. Please review the report."
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/common-fixes.mdc`.
        iii. (This rule will provide general fix guidance).
        iv. State: "Please address the issues and then re-type 'VAN QA' to re-run the validation."
5.  **Completion of this Orchestrator:**
    a.  Use `edit_file` to add to `memory-bank/activeContext.md`: "VAN QA Log - [Timestamp]: Technical validation process orchestrated. Outcome: [PASS/FAIL]."
    b.  (Control returns to `van-mode-map.mdc` or awaits user input based on QA outcome).

## 🧰 Utility Rule Reminder:
*   For detailed guidance on how to structure `fetch_rules` calls, you can (if necessary for your own understanding) `read_file` `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/rule-calling-guide.mdc` or `rule-calling-help.mdc`. However, this orchestrator explicitly tells you which rules to fetch.
"""
        },
        # --- VAN QA Checks ---
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/dependency-check.mdc",
            "description": "VAN QA sub-rule for dependency verification. Fetched by `van-qa-main.mdc`. Guides AI to check required dependencies and log results.",
            "globs": "**/visual-maps/van_mode_split/van-qa-checks/dependency-check.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: DEPENDENCY VERIFICATION (AI Instructions)

> **TL;DR:** Verify project dependencies (e.g., Node.js, npm, Python, pip, specific libraries) are installed and versions are compatible. Log findings to `activeContext.md` using `edit_file`. This rule is fetched by `van-qa-main.mdc`.

## ⚙️ AI ACTIONS FOR DEPENDENCY VERIFICATION:

1.  **Acknowledge & Context:**
    a.  State: "Starting Dependency Verification."
    b.  `read_file memory-bank/techContext.md` and `memory-bank/tasks.md` (or `activeContext.md` if it has tech stack info from CREATIVE phase) to identify key technologies and expected dependencies (e.g., Node.js version, Python version, package manager, specific libraries).
2.  **Define Checks (Based on Context):**
    *   **Example for Node.js project:**
        *   Check Node.js installed and version (e.g., `node -v`).
        *   Check npm installed and version (e.g., `npm -v`).
        *   Check `package.json` exists (e.g., `list_dir .`).
        *   If `package-lock.json` or `yarn.lock` exists, consider running `npm ci` or `yarn install --frozen-lockfile` (or just `npm install`/`yarn install` if less strict) to verify/install packages.
    *   **Example for Python project:**
        *   Check Python installed and version (e.g., `python --version` or `python3 --version`).
        *   Check pip installed (usually comes with Python).
        *   Check `requirements.txt` exists.
        *   Consider creating a virtual environment and `pip install -r requirements.txt`.
3.  **Execute Checks (Using `run_terminal_cmd`):**
    a.  For each defined check:
        i.  Clearly state the command you are about to run.
        ii. `run_terminal_cmd` with the command.
        iii. Record the output.
4.  **Evaluate Results & Log:**
    a.  Based on command outputs, determine if dependencies are met.
    b.  Use `edit_file` to append detailed findings to the "VAN QA Log" in `memory-bank/activeContext.md`:
        ```markdown
        #### Dependency Check Log - [Timestamp]
        - Check: Node.js version
          - Command: `node -v`
          - Output: `v18.12.0`
          - Status: PASS (meets requirement >=16)
        - Check: npm install
          - Command: `npm install`
          - Output: `... up to date ...` or error messages
          - Status: [PASS/FAIL - with error summary if FAIL]
        - ... (other checks) ...
        - Overall Dependency Status: [PASS/FAIL]
        ```
5.  **Completion:**
    a.  State: "Dependency Verification complete. Overall Status: [PASS/FAIL]."
    b.  (The `van-qa-main.mdc` orchestrator will use this outcome).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/config-check.mdc",
            "description": "VAN QA sub-rule for configuration validation. Fetched by `van-qa-main.mdc`. Guides AI to check project configuration files.",
            "globs": "**/visual-maps/van_mode_split/van-qa-checks/config-check.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: CONFIGURATION VALIDATION (AI Instructions)

> **TL;DR:** Validate project configuration files (e.g., `package.json` syntax, `tsconfig.json`, linters, build tool configs). Log findings to `activeContext.md` using `edit_file`. This rule is fetched by `van-qa-main.mdc`.

## ⚙️ AI ACTIONS FOR CONFIGURATION VALIDATION:

1.  **Acknowledge & Context:**
    a.  State: "Starting Configuration Validation."
    b.  `read_file memory-bank/techContext.md` and `memory-bank/tasks.md` to identify relevant configuration files based on the project type and technology stack.
2.  **Define Checks (Based on Context):**
    *   **Example for a TypeScript/React project:**
        *   `package.json`: `read_file package.json`. Check for valid JSON structure (conceptually, AI doesn't parse JSON strictly but looks for malformations). Check for essential scripts (`build`, `start`, `test`).
        *   `tsconfig.json`: `read_file tsconfig.json`. Check for valid JSON. Check for key compiler options like `jsx`, `target`, `moduleResolution`.
        *   `.eslintrc.js` or `eslint.config.js`: `read_file [config_name]`. Check for basic structural integrity.
        *   `vite.config.js` or `webpack.config.js`: `read_file [config_name]`. Check for presence of key plugins (e.g., React plugin).
3.  **Execute Checks (Primarily using `read_file` and analysis):**
    a.  For each configuration file:
        i.  `read_file [config_filepath]`.
        ii. Analyze its content against expected structure or key settings.
        iii. For linting/formatting configs, note their presence. Actual linting runs are usually part of build/test steps.
4.  **Evaluate Results & Log:**
    a.  Based on file content analysis, determine if configurations seem correct and complete.
    b.  Use `edit_file` to append detailed findings to the "VAN QA Log" in `memory-bank/activeContext.md`:
        ```markdown
        #### Configuration Check Log - [Timestamp]
        - File: `package.json`
          - Check: Valid JSON structure, presence of `build` script.
          - Status: PASS
        - File: `tsconfig.json`
          - Check: Presence of `jsx: react-jsx`.
          - Status: FAIL (jsx option missing or incorrect)
        - ... (other checks) ...
        - Overall Configuration Status: [PASS/FAIL]
        ```
5.  **Completion:**
    a.  State: "Configuration Validation complete. Overall Status: [PASS/FAIL]."
    b.  (The `van-qa-main.mdc` orchestrator will use this outcome).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/environment-check.mdc",
            "description": "VAN QA sub-rule for environment validation. Fetched by `van-qa-main.mdc`. Guides AI to check build tools, permissions, etc.",
            "globs": "**/visual-maps/van_mode_split/van-qa-checks/environment-check.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: ENVIRONMENT VALIDATION (AI Instructions)

> **TL;DR:** Validate the development/build environment (e.g., required CLI tools available, necessary permissions, environment variables). Log findings to `activeContext.md` using `edit_file`. This rule is fetched by `van-qa-main.mdc`.

## ⚙️ AI ACTIONS FOR ENVIRONMENT VALIDATION:

1.  **Acknowledge & Context:**
    a.  State: "Starting Environment Validation."
    b.  `read_file memory-bank/techContext.md` to identify expected environment characteristics (e.g., OS, required CLIs like Git, Docker).
2.  **Define Checks (Based on Context):**
    *   **General Checks:**
        *   Git CLI: `run_terminal_cmd git --version`.
        *   Network connectivity (if external resources needed for build): (Conceptual check, or a simple `ping google.com` if allowed and relevant).
    *   **Example for Web Development:**
        *   Build tool (e.g., Vite, Webpack if used globally): `run_terminal_cmd vite --version` (if applicable).
        *   Port availability (e.g., for dev server): (Conceptual, AI can't directly check. Note if a common port like 3000 or 8080 is usually needed).
    *   **Permissions:**
        *   (Conceptual) Does the AI anticipate needing to write files outside `memory-bank/` or project dir during build? If so, note potential permission needs. Actual permission checks are hard for AI.
3.  **Execute Checks (Using `run_terminal_cmd` where appropriate):**
    a.  For each defined check:
        i.  State the command or check being performed.
        ii. If using `run_terminal_cmd`, record the output.
4.  **Evaluate Results & Log:**
    a.  Based on command outputs and conceptual checks, determine if the environment seems suitable.
    b.  Use `edit_file` to append detailed findings to the "VAN QA Log" in `memory-bank/activeContext.md`:
        ```markdown
        #### Environment Check Log - [Timestamp]
        - Check: Git CLI availability
          - Command: `git --version`
          - Output: `git version 2.30.0`
          - Status: PASS
        - Check: Port 3000 availability for dev server
          - Method: Conceptual (not directly testable by AI)
          - Assumption: Port 3000 should be free.
          - Status: NOTE (User should ensure port is free)
        - ... (other checks) ...
        - Overall Environment Status: [PASS/WARN/FAIL]
        ```
5.  **Completion:**
    a.  State: "Environment Validation complete. Overall Status: [PASS/WARN/FAIL]."
    b.  (The `van-qa-main.mdc` orchestrator will use this outcome).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/build-test.mdc",
            "description": "VAN QA sub-rule for minimal build test. Fetched by `van-qa-main.mdc`. Guides AI to attempt a basic build/compilation.",
            "globs": "**/visual-maps/van_mode_split/van-qa-checks/build-test.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: MINIMAL BUILD TEST (AI Instructions)

> **TL;DR:** Attempt a minimal or dry-run build of the project to catch early integration or setup issues. Log findings to `activeContext.md` using `edit_file`. This rule is fetched by `van-qa-main.mdc`.

## ⚙️ AI ACTIONS FOR MINIMAL BUILD TEST:

1.  **Acknowledge & Context:**
    a.  State: "Starting Minimal Build Test."
    b.  `read_file package.json` (or equivalent like `Makefile`, `pom.xml`) to identify build commands.
    c.  `read_file memory-bank/techContext.md` for info on build tools.
2.  **Define Build Command:**
    a.  Identify the primary build script (e.g., `npm run build`, `mvn package`, `make`).
    b.  Consider if a "dry run" or "lint-only" or "compile-only" version of the build command exists to test the toolchain without full artifact generation (e.g., `tsc --noEmit` for TypeScript). If so, prefer it for a *minimal* test. If not, use the standard build command.
3.  **Execute Build Command (Using `run_terminal_cmd`):**
    a.  State the exact build command you are about to run.
    b.  Ensure you are in the correct directory (usually project root). `list_dir .` to confirm presence of `package.json` etc. If not, use `cd` via `run_terminal_cmd`.
    c.  `run_terminal_cmd [build_command]`.
    d.  Capture the full output.
4.  **Evaluate Results & Log:**
    a.  Analyze the output for success messages or error codes/messages.
    b.  Use `edit_file` to append detailed findings to the "VAN QA Log" in `memory-bank/activeContext.md`:
        ```markdown
        #### Minimal Build Test Log - [Timestamp]
        - Command: `npm run build`
        - Output:
          \`\`\`
          [Full or summarized build output]
          \`\`\`
        - Status: [PASS/FAIL - with key error if FAIL]
        - Overall Minimal Build Test Status: [PASS/FAIL]
        ```
5.  **Completion:**
    a.  State: "Minimal Build Test complete. Overall Status: [PASS/FAIL]."
    b.  (The `van-qa-main.mdc` orchestrator will use this outcome).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-checks/file-verification.mdc",
            "description": "VAN QA sub-rule for specific file/artifact verification post-build or during QA. Fetched by `van-qa-main.mdc` if deeper file checks are needed.",
            "globs": "**/visual-maps/van_mode_split/van-qa-checks/file-verification.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: DETAILED FILE VERIFICATION (AI Instructions)

> **TL;DR:** Verify existence, content, or structure of specific project files or build artifacts, beyond initial Memory Bank setup. Log findings to `activeContext.md`. This rule is typically fetched by `van-qa-main.mdc` if specific file checks are part of the QA plan.

## ⚙️ AI ACTIONS FOR DETAILED FILE VERIFICATION:

1.  **Acknowledge & Context:**
    a.  State: "Starting Detailed File Verification."
    b.  `read_file memory-bank/tasks.md` or `activeContext.md` to understand which specific files or artifact locations need verification as part of the current QA scope (e.g., "ensure `dist/bundle.js` is created after build", "check `config.yaml` has specific keys").
    c.  If no specific files are targeted for this QA check, state so and this check can be considered trivially PASS.
2.  **Define Checks (Based on QA Scope):**
    *   **Existence Check:** `list_dir [path_to_dir]` to see if `[filename]` is present.
    *   **Content Snippet Check:** `read_file [filepath]` and then search for a specific string or pattern within the content.
    *   **File Size Check (Conceptual):** If a build artifact is expected, `list_dir -l [filepath]` (Unix-like) or `Get-ChildItem [filepath] | Select-Object Length` (PowerShell) might give size. AI notes if it's unexpectedly zero or very small.
    *   **Structure Check (Conceptual for complex files like XML/JSON):** `read_file [filepath]` and describe if it generally conforms to expected structure (e.g., "appears to be valid JSON with a root object containing 'data' and 'errors' keys").
3.  **Execute Checks (Using `list_dir`, `read_file`, or `run_terminal_cmd` for file system info):**
    a.  For each defined file check:
        i.  State the file and the check being performed.
        ii. Execute the appropriate tool/command.
        iii. Record the observation/output.
4.  **Evaluate Results & Log:**
    a.  Based on observations, determine if file verifications pass.
    b.  Use `edit_file` to append findings to the "VAN QA Log" in `memory-bank/activeContext.md`:
        ```markdown
        #### Detailed File Verification Log - [Timestamp]
        - File: `dist/app.js`
          - Check: Existence after build.
          - Observation: File exists.
          - Status: PASS
        - File: `src/config/settings.json`
          - Check: Contains key `"api_url"`.
          - Observation: `read_file` content shows `"api_url": "https://example.com"`.
          - Status: PASS
        - ... (other checks) ...
        - Overall Detailed File Verification Status: [PASS/FAIL]
        ```
5.  **Completion:**
    a.  State: "Detailed File Verification complete. Overall Status: [PASS/FAIL]."
    b.  (The `van-qa-main.mdc` orchestrator will use this outcome).
"""
        },
        # --- VAN QA Utils ---
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/common-fixes.mdc",
            "description": "VAN QA utility providing common fixes for validation failures. Fetched by `van-qa-main.mdc` on QA fail.",
            "globs": "**/visual-maps/van_mode_split/van-qa-utils/common-fixes.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: COMMON VALIDATION FIXES (AI Guidance)

> **TL;DR:** Provides common troubleshooting steps and fix suggestions when VAN QA checks fail. This rule is fetched by `van-qa-main.mdc` after a QA failure is reported.

## ⚙️ AI ACTIONS (Present this information to the user):

State: "Here are some common troubleshooting steps based on the type of QA failure. Please review the detailed failure report and attempt these fixes:"

### 1. Dependency Issues:
*   **Missing Tools (Node, Python, Git, etc.):**
    *   "Ensure the required tool ([Tool Name]) is installed and available in your system's PATH. You might need to download it from its official website or install it via your system's package manager."
*   **Incorrect Tool Version:**
    *   "The version of [Tool Name] found is [Found Version], but [Required Version] is expected. Consider using a version manager (like nvm for Node, pyenv for Python) to switch to the correct version, or update/downgrade the tool."
*   **Project Dependencies (`npm install` / `pip install` failed):**
    *   "Check the error messages from the package manager (`npm`, `pip`). Common causes include network issues, permission problems, or incompatible sub-dependencies."
    *   "Try deleting `node_modules/` and `package-lock.json` (or `venv/` and `requirements.txt` conflicts) and running the install command again."
    *   "Ensure your `package.json` or `requirements.txt` is correctly formatted and specifies valid package versions."

### 2. Configuration Issues:
*   **File Not Found:**
    *   "The configuration file `[filepath]` was not found. Ensure it exists at the correct location in your project."
*   **Syntax Errors (JSON, JS, etc.):**
    *   "The file `[filepath]` appears to have syntax errors. Please open it and check for typos, missing commas, incorrect brackets, etc. Using a code editor with linting can help."
*   **Missing Key Settings:**
    *   "The configuration file `[filepath]` is missing an expected setting: `[setting_name]`. Please add it according to the project's requirements (e.g., add `jsx: 'react-jsx'` to `tsconfig.json`)."

### 3. Environment Issues:
*   **Command Not Found (for build tools like `vite`, `tsc`):**
    *   "The command `[command_name]` was not found. If it's a project-local tool, ensure you've run `npm install` (or equivalent) and try prefixing with `npx` (e.g., `npx vite build`). If it's a global tool, ensure it's installed globally."
*   **Permission Denied:**
    *   "An operation failed due to insufficient permissions. You might need to run your terminal/IDE as an administrator (Windows) or use `sudo` (macOS/Linux) for specific commands, but be cautious with `sudo`."
    *   "Check file/folder permissions if trying to write to a restricted area."
*   **Port in Use:**
    *   "The build or dev server tried to use port `[port_number]`, which is already in use. Identify and stop the process using that port, or configure your project to use a different port."

### 4. Minimal Build Test Issues:
*   **Build Script Fails:**
    *   "The command `[build_command]` failed. Examine the full error output from the build process. It often points to missing dependencies, configuration errors, or code syntax issues."
    *   "Ensure all dependencies from `dependency-check.mdc` are resolved first."
*   **Entry Point Errors / Module Not Found:**
    *   "The build process reported it couldn't find a key file or module. Check paths in your configuration files (e.g., `vite.config.js`, `webpack.config.js`) and in your import statements in code."

**General Advice to User:**
"After attempting fixes, please type 'VAN QA' again to re-run the technical validation process."

(Control returns to `van-qa-main.mdc` which awaits user action).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/mode-transitions.mdc",
            "description": "VAN QA utility for handling mode transitions after QA. Fetched by `van-qa-main.mdc` on QA pass. Guides AI to recommend BUILD mode.",
            "globs": "**/visual-maps/van_mode_split/van-qa-utils/mode-transitions.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: MODE TRANSITIONS (AI Instructions)

> **TL;DR:** Handles mode transition recommendations after VAN QA validation. If QA passed, recommend BUILD mode. This rule is fetched by `van-qa-main.mdc` after a successful QA.

## ⚙️ AI ACTIONS FOR MODE TRANSITION (POST QA SUCCESS):

1.  **Acknowledge:** State: "VAN QA validation passed successfully."
2.  **Update `activeContext.md`:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md` with:
        ```markdown
        ## VAN QA Status - [Timestamp]
        - Overall Result: PASS
        - Next Recommended Mode: BUILD
        ```
3.  **Recommend BUILD Mode:**
    a.  State: "All technical pre-flight checks are green. The project appears ready for implementation."
    b.  State: "Recommend transitioning to BUILD mode. Type 'BUILD' to begin implementation."
4.  **Await User Confirmation:** Await the user to type 'BUILD' or another command.

## 🔒 BUILD MODE ACCESS (Conceptual Reminder for AI):
*   The system is designed such that if a user tries to enter 'BUILD' mode directly without VAN QA having passed (for tasks requiring it), the BUILD mode orchestrator (or a preceding check) should ideally verify the `.qa_validation_status` file or `activeContext.md` and block if QA was needed but not passed. This current rule (`mode-transitions.mdc`) focuses on the *recommendation* after a *successful* QA.

(Control returns to `van-qa-main.mdc` which awaits user input).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/reports.mdc",
            "description": "VAN QA utility for generating success/failure reports. Fetched by `van-qa-main.mdc`. Guides AI to format and present QA results using `edit_file`.",
            "globs": "**/visual-maps/van_mode_split/van-qa-utils/reports.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: VALIDATION REPORTS (AI Instructions)

> **TL;DR:** Generate and present a formatted success or failure report based on the outcomes of the VAN QA checks. Update `activeContext.md` and `.qa_validation_status`. This rule is fetched by `van-qa-main.mdc`.

## ⚙️ AI ACTIONS FOR GENERATING REPORTS:

You will be told by `van-qa-main.mdc` whether the overall QA passed or failed, and will have access to the detailed logs in `activeContext.md`.

1.  **Acknowledge:** State: "Generating VAN QA Report."
2.  **Gather Data from `activeContext.md`:**
    a.  `read_file memory-bank/activeContext.md`.
    b.  Extract the findings from the "VAN QA Log" sections for:
        *   Dependency Check Status & Details
        *   Configuration Check Status & Details
        *   Environment Check Status & Details
        *   Minimal Build Test Status & Details
3.  **Format the Report:**

    **If Overall QA Status is PASS:**
    ```markdown
    ╔═════════════════════ 🔍 QA VALIDATION REPORT ══════════════════════╗
    │ PROJECT: [Project Name from activeContext.md/projectbrief.md]
    │ TIMESTAMP: [Current Date/Time]
    ├─────────────────────────────────────────────────────────────────────┤
    │ 1️⃣ DEPENDENCIES:   ✓ PASS. [Brief summary, e.g., "Node & npm OK"]
    │ 2️⃣ CONFIGURATION:  ✓ PASS. [Brief summary, e.g., "package.json & tsconfig OK"]
    │ 3️⃣ ENVIRONMENT:    ✓ PASS. [Brief summary, e.g., "Git found, permissions assumed OK"]
    │ 4️⃣ MINIMAL BUILD:  ✓ PASS. [Brief summary, e.g., "npm run build script executed successfully"]
    ├─────────────────────────────────────────────────────────────────────┤
    │ 🚨 FINAL VERDICT: PASS                                              │
    │ ➡️ Clear to proceed to BUILD mode.                                  │
    ╚═════════════════════════════════════════════════════════════════════╝
    ```

    **If Overall QA Status is FAIL:**
    ```markdown
    ⚠️⚠️⚠️ QA VALIDATION FAILED ⚠️⚠️⚠️

    Project: [Project Name]
    Timestamp: [Current Date/Time]

    The following issues must be resolved before proceeding to BUILD mode:

    1️⃣ DEPENDENCY ISSUES: [Status: FAIL/WARN]
       - Details: [Extracted from activeContext.md log for dependencies]
       - Recommended Fix: (Refer to common-fixes.mdc or specific error messages)

    2️⃣ CONFIGURATION ISSUES: [Status: FAIL/WARN]
       - Details: [Extracted from activeContext.md log for configurations]
       - Recommended Fix: (Refer to common-fixes.mdc or specific error messages)

    3️⃣ ENVIRONMENT ISSUES: [Status: FAIL/WARN]
       - Details: [Extracted from activeContext.md log for environment]
       - Recommended Fix: (Refer to common-fixes.mdc or specific error messages)

    4️⃣ MINIMAL BUILD TEST ISSUES: [Status: FAIL/WARN]
       - Details: [Extracted from activeContext.md log for build test]
       - Recommended Fix: (Refer to common-fixes.mdc or specific error messages)

    ⚠️ BUILD MODE IS BLOCKED until these issues are resolved.
    Type 'VAN QA' after fixing the issues to re-validate.
    ```
4.  **Present Report to User:**
    a.  Display the formatted report directly to the user in the chat.
5.  **Update `.qa_validation_status` File:**
    a.  Use `edit_file` to write "PASS" or "FAIL" to `memory-bank/.qa_validation_status`. This file acts as a simple flag for other rules.
        *   Example content for PASS: `QA_STATUS: PASS - [Timestamp]`
        *   Example content for FAIL: `QA_STATUS: FAIL - [Timestamp]`
6.  **Log Report Generation in `activeContext.md`:**
    a.  Use `edit_file` to append to `memory-bank/activeContext.md`:
        ```markdown
        #### VAN QA Report Generation - [Timestamp]
        - Overall QA Status: [PASS/FAIL]
        - Report presented to user.
        - `.qa_validation_status` file updated.
        ```
7.  **Completion:** State: "VAN QA Report generated and presented."
    (Control returns to `van-qa-main.mdc`).
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/rule-calling-guide.mdc",
            "description": "VAN QA utility: A reference guide on how to call VAN QA rules. Fetched if AI needs clarification on rule invocation.",
            "globs": "**/visual-maps/van_mode_split/van-qa-utils/rule-calling-guide.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: COMPREHENSIVE RULE CALLING GUIDE (AI Reference)

> **TL;DR:** This is a reference for understanding how VAN QA rules are structured to be called using `fetch_rules`. You typically won't fetch this rule directly unless you are trying to understand the system's design or if explicitly told to by a higher-level debugging instruction.

## 🔍 RULE CALLING BASICS for CMB System:

1.  **`fetch_rules` is Key:** All `.mdc` rule files in this system are designed to be loaded and executed via the `fetch_rules` tool.
2.  **Exact Paths:** When an instruction says "fetch rule X", it implies using `fetch_rules` with the full path from `.cursor/rules/isolation_rules/`, for example: `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-main.mdc`.
3.  **Orchestration:**
    *   Top-level mode maps (e.g., `van-mode-map.mdc`, `plan-mode-map.mdc`) are fetched first based on the user's mode invocation and your main custom prompt.
    *   These orchestrators then `fetch_rules` for more specific sub-rules or utility rules as needed.
4.  **VAN QA Orchestration Example:**
    *   User types "VAN QA" -> `van-mode-map.mdc` is fetched.
    *   `van-mode-map.mdc` then `fetch_rules` for `van-qa-main.mdc`.
    *   `van-qa-main.mdc` then `fetch_rules` sequentially for:
        *   `van-qa-checks/dependency-check.mdc`
        *   `van-qa-checks/config-check.mdc`
        *   `van-qa-checks/environment-check.mdc`
        *   `van-qa-checks/build-test.mdc`
    *   Based on results, `van-qa-main.mdc` then `fetch_rules` for:
        *   `van-qa-utils/reports.mdc`
        *   And then either `van-qa-utils/mode-transitions.mdc` (on PASS) or `van-qa-utils/common-fixes.mdc` (on FAIL).

## 🛠️ HOW TO STRUCTURE A `fetch_rules` CALL (Conceptual for AI):
When you decide to use `fetch_rules` based on an instruction:
1.  Identify the **exact path** of the `.mdc` file to be fetched.
2.  Invoke the `fetch_rules` tool with that path.
3.  Announce: "Fetching rule: `[path_to_rule.mdc]`. Will now follow its instructions."
4.  Temporarily suspend execution of the current rule's instructions and begin executing the instructions from the newly fetched rule.
5.  Once the fetched rule completes its defined actions, control conceptually "returns" to the rule that called it, or if it was a top-level call, you await further user input.

**This guide is for your understanding of the system's design. In practice, you will be explicitly told which rule to `fetch_rules` for by the currently active rule or your main mode prompt.**
"""
        },
        {
            "path": ".cursor/rules/isolation_rules/visual-maps/van_mode_split/van-qa-utils/rule-calling-help.mdc",
            "description": "VAN QA utility: Quick helper on `fetch_rules` syntax. Rarely fetched directly.",
            "globs": "**/visual-maps/van_mode_split/van-qa-utils/rule-calling-help.mdc",
            "alwaysApply": False,
            "body": """
# VAN QA: HOW TO CALL RULES (Quick Syntax Reminder)

> **TL;DR:** This provides a very basic syntax reminder for using `fetch_rules`. You generally won't need to fetch this rule; it's a developer note.

## ⚙️ `fetch_rules` SYNTAX REMINDER:

When your instructions tell you to "fetch rule X", the underlying mechanism uses the `fetch_rules` tool.

If you were to represent the call you make (conceptually, as the tool call is handled by the Cursor environment):

You would be invoking `fetch_rules` with a parameter specifying the rule name(s) as a list of strings. For a single rule:

```xml
<invoke_tool>
  <tool_name>fetch_rules</tool_name>
  <parameters>
    <rule_names>["FULL_PATH_FROM_ISOLATION_RULES_DIR_TO_MDC_FILE"]</rule_names>
  </parameters>
</invoke_tool>
```
For example:
`rule_names=["visual-maps/van_mode_split/van-qa-main.mdc"]`
(Assuming the system resolves this relative to `.cursor/rules/isolation_rules/`)

**You typically don't construct this XML. You just follow the instruction "fetch rule X" and the system handles the invocation.** The key is providing the correct, full path to the `.mdc` file as specified in the instructions.
"""
        },
        # --- Level 1 Files ---
        {
            "path": ".cursor/rules/isolation_rules/Level1/optimized-workflow-level1.mdc",
    "description": "Optimized Level 1 workflow for quick bug fixes, emphasizing speed, token efficiency, and consolidated documentation using `edit_file`.",
    "globs": "**/Level1/optimized-workflow-level1.mdc",
    "alwaysApply": False,
    "body": """
# OPTIMIZED LEVEL 1 WORKFLOW (AI Instructions)

> **TL;DR:** This streamlined workflow for Level 1 tasks (quick bug fixes) optimizes for speed and token efficiency. Focus on direct implementation and consolidated documentation using `edit_file`.

## 🔧 LEVEL 1 PROCESS FLOW (AI Actions)

1.  **Acknowledge & Context (Assumes VAN mode has confirmed Level 1):**
    a.  State: "Initiating Optimized Level 1 Workflow for [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` to understand the specific issue.
    c.  `read_file memory-bank/activeContext.md` for any specific file paths or context.
2.  **Analyze & Locate:**
    a.  Briefly analyze the issue described in `tasks.md`.
    b.  If file paths are not provided, use `codebase_search` or `search_files` to locate the relevant code section(s).
3.  **Implement Fix:**
    a.  Use `edit_file` to make the necessary code changes directly.
    b.  Keep changes minimal and targeted, as expected for Level 1.
4.  **Verify (Conceptually or via Simple Test):**
    a.  Mentally review the change.
    b.  If a very simple test command is appropriate (e.g., linting the changed file, running a single specific test if available), use `run_terminal_cmd`.
5.  **Document (Consolidated):**
    a.  Use `edit_file` to update `memory-bank/tasks.md` with a concise record of the fix. Use a consolidated format.
        **Example Content for `tasks.md` (append under relevant task or in a 'Completed L1 Fixes' section):**
        ```markdown
        - **L1 Fix:** [Issue Name/ID]
          - **Problem:** [Brief description from original task]
          - **Cause:** [Brief root cause, if obvious]
          - **Solution:** [Implemented fix, e.g., "Corrected variable name in `auth.py` line 42."]
          - **Files Changed:** `[path/to/file.py]`
          - **Verification:** [e.g., "Visual inspection", "Ran linter"]
          - **Status:** COMPLETED - [Date]
        ```
    b.  Optionally, add a one-line entry to `memory-bank/progress.md` using `edit_file`:
        `[Date] - L1 Fix: [Issue Name] - Completed. See tasks.md for details.`
    c.  Update `memory-bank/activeContext.md` using `edit_file` to clear current L1 task focus and indicate readiness for next task.
6.  **Notify Completion:**
    a.  State: "Level 1 task '[Task Name]' completed and documented efficiently. Ready for next task."

## ⚡ TOKEN-OPTIMIZED TEMPLATE (for AI to structure the `tasks.md` update via `edit_file`)
When updating `tasks.md`, aim for a structure like this:
```markdown
- **L1 Fix:** [Issue Title]
  - **Problem:** [Brief description]
  - **Cause:** [Root cause, if clear]
  - **Solution:** [Implemented fix details]
  - **Files:** `[path/to/file1]`, `[path/to/file2]`
  - **Tested:** [How verified, e.g., "Visual check", "Linter pass"]
  - **Status:** COMPLETED - [Date]
```
This rule prioritizes direct action and minimal, consolidated documentation using `edit_file`.
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level1/quick-documentation.mdc",
    "description": "Defines the content and structure for quick documentation of Level 1 (Quick Bug Fix) tasks, primarily within `tasks.md` using `edit_file`.",
    "globs": "**/Level1/quick-documentation.mdc",
    "alwaysApply": False,
    "body": """
# QUICK DOCUMENTATION FOR LEVEL 1 TASKS (AI Instructions)

> **TL;DR:** This rule outlines the concise documentation approach for Level 1 tasks. The primary record is made in `memory-bank/tasks.md` using `edit_file`.

## 📋 DOCUMENTATION PRINCIPLES (AI Self-Guide)
*   **Conciseness:** Brief but complete.
*   **Focus:** Only essential information to understand the fix.
*   **Findability:** Ensure the fix can be referenced via `tasks.md`.

## 📝 QUICK FIX DOCUMENTATION TEMPLATE (For `tasks.md` update via `edit_file`)
When a Level 1 task is completed, use `edit_file` to update its entry or add a new entry in `memory-bank/tasks.md` under a "Completed Level 1 Fixes" or similar section, following this structure:

```markdown
- **L1 Fix:** [Issue Title/ID from original task]
  - **Issue:** [Brief description of the problem - 1-2 sentences]
  - **Root Cause:** [Concise description of what caused the issue - 1-2 sentences, if readily apparent]
  - **Solution:** [Brief description of the fix implemented - 2-3 sentences, e.g., "Modified `user_controller.js` line 75 to correctly handle null input for username."]
  - **Files Changed:**
    - `[path/to/file1.ext]`
    - `[path/to/file2.ext]` (if applicable)
  - **Verification:** [How the fix was tested/verified - 1-2 sentences, e.g., "Manually tested login with empty username field.", "Ran linter on changed file."]
  - **Status:** COMPLETED - [Date]
```

## 🔄 MEMORY BANK UPDATES (AI Actions)

1.  **`tasks.md` (Primary Record):**
    *   Use `edit_file` to add/update the entry as per the template above. This is the main documentation for L1 fixes.
2.  **`activeContext.md` (Minimal Update):**
    *   Use `edit_file` to append a brief note to `memory-bank/activeContext.md` if desired, e.g.:
        ```markdown
        ### Recent L1 Fixes - [Date]
        - Fixed [Issue Title] in `[main_file_changed]`. See `tasks.md` for details.
        ```
    *   More importantly, clear the L1 task from the "Current Focus" in `activeContext.md`.
3.  **`progress.md` (Optional Minimal Update):**
    *   Use `edit_file` to append a one-liner to `memory-bank/progress.md` if desired, e.g.:
        `[Date] - L1 Fix: Completed [Issue Title].`

**Focus:** The goal is efficient capture of essential information directly in `tasks.md` using `edit_file`.
(This rule provides the *content structure*. The actual workflow is often directed by `Level1/workflow-level1.mdc` or `Level1/optimized-workflow-level1.mdc` which might refer to these content guidelines).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level1/workflow-level1.mdc",
    "description": "Streamlined workflow for Level 1 (Quick Bug Fix) tasks. Guides AI through minimal initialization, direct implementation, and quick documentation using `edit_file`.",
    "globs": "**/Level1/workflow-level1.mdc",
    "alwaysApply": False,
    "body": """
# STREAMLINED WORKFLOW FOR LEVEL 1 TASKS (AI Instructions)

> **TL;DR:** This rule guides the AI through a minimal workflow for Level 1 (Quick Bug Fix) tasks. It emphasizes rapid issue resolution and concise documentation, primarily using `edit_file`.

## 🧭 LEVEL 1 WORKFLOW PHASES (AI Actions)

This workflow is typically fetched after VAN mode has confirmed the task as Level 1.

### Phase 1: INITIALIZATION (Quick Confirmation)

1.  **Acknowledge & Context:**
    a.  State: "Initiating Level 1 Workflow for [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` to confirm the specific issue details.
    c.  `read_file memory-bank/activeContext.md` for current focus.
2.  **Environment Setup (Conceptual):**
    a.  No complex setup expected for L1. Assume environment is ready.
3.  **Task Entry Check:**
    a.  Ensure a minimal task entry exists in `tasks.md` for the issue. If VAN mode created a detailed one, that's fine. If not, ensure at least a line item is there.
    b.  `edit_file memory-bank/activeContext.md` to confirm: "Focus: L1 Fix - [Task Name]".
4.  **Milestone:** State "L1 Initialization complete. Proceeding to Implementation."

### Phase 2: IMPLEMENTATION (Direct Fix)

1.  **Locate Issue Source:**
    a.  If `tasks.md` or `activeContext.md` specifies file(s) and line(s), use that.
    b.  If not, use `codebase_search` or `search_files` with keywords from the issue description to find the relevant code.
2.  **Develop & Apply Fix:**
    a.  Use `edit_file` to make the targeted code change.
    b.  The fix should be small and localized, consistent with Level 1.
3.  **Test & Verify:**
    a.  Perform a simple verification. This might be:
        *   Visual inspection of the change.
        *   Running a linter on the modified file (`run_terminal_cmd`).
        *   If a very specific unit test covers the change and is easy to run, consider `run_terminal_cmd` for that single test.
    b.  State the verification method and outcome.
4.  **Milestone:** State "L1 Implementation and verification complete. Proceeding to Documentation."

### Phase 3: DOCUMENTATION (Quick & Concise)

1.  **Update `tasks.md`:**
    a.  `fetch_rules` for `.cursor/rules/isolation_rules/Level1/quick-documentation.mdc`.
    b.  Follow the template provided in `quick-documentation.mdc` to update the task entry in `memory-bank/tasks.md` using `edit_file`. This includes issue, cause (if known), solution, files changed, and verification. Mark as COMPLETED with date.
2.  **Update `activeContext.md`:**
    a.  Use `edit_file` to clear the "Focus" section in `memory-bank/activeContext.md` or set it to "Awaiting next task."
    b.  Optionally, add a one-line summary to a "Recent L1 Fixes" log in `activeContext.md`.
3.  **Notify Stakeholders (Conceptual):**
    a.  For L1, direct notification is usually not needed unless specified. The `tasks.md` update serves as the record.
4.  **Milestone:** State "L1 Documentation complete. Task [Task Name] is fully resolved."

## 🚨 TASK ESCALATION
*   If during IMPLEMENTATION, the issue is found to be more complex than L1 (e.g., requires changes to multiple components, design decisions, or significant testing):
    a.  State: "ESCALATION: Issue [Task Name] is more complex than initially assessed. It appears to be Level [2/3]. Recommend halting L1 workflow and re-evaluating in VAN or PLAN mode."
    b.  Use `edit_file` to update `tasks.md` and `activeContext.md` with this assessment.
    c.  Await user guidance.

This workflow prioritizes speed and efficiency for simple fixes.
"""
},
# --- Level 2 Files ---
{
    "path": ".cursor/rules/isolation_rules/Level2/archive-basic.mdc",
    "description": "Basic archiving for Level 2 (Simple Enhancement) tasks. Guides AI to create a structured archive document using `edit_file`.",
    "globs": "**/Level2/archive-basic.mdc",
    "alwaysApply": False,
    "body": """
# BASIC ARCHIVING FOR LEVEL 2 TASKS (AI Instructions)

> **TL;DR:** This rule guides the creation of a basic archive document for a completed Level 2 task using `edit_file`. It ensures key information is preserved.

This rule is typically fetched by the Level 2 workflow orchestrator or the main ARCHIVE mode orchestrator if the task is L2.

## ⚙️ AI ACTIONS FOR LEVEL 2 ARCHIVING:

1.  **Acknowledge & Context:**
    a.  State: "Initiating Basic Archiving for Level 2 task: [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the completed task details (requirements, sub-tasks).
    c.  `read_file memory-bank/reflection/reflect-[task_name_or_id]-[date].md` for lessons learned.
    d.  `read_file memory-bank/progress.md` for implementation summary.
2.  **Prepare Archive Content (Based on Template Below):**
    a.  Synthesize information from `tasks.md`, `reflection-*.md`, and `progress.md`.
3.  **Create Archive File:**
    a.  Determine archive filename: `archive-[task_name_or_id]-[date].md` (e.g., `archive-user-profile-update-20250515.md`).
    b.  Use `edit_file` to create/update `memory-bank/archive/[archive_filename.md]` with the structured content.
        **Basic Archive Structure (Content for `edit_file`):**
        ```markdown
        # Enhancement Archive: [Feature Name from tasks.md]

        ## Task ID: [Task ID from tasks.md]
        ## Date Completed: [Date from tasks.md or reflection document]
        ## Complexity Level: 2

        ## 1. Summary of Enhancement
        [Brief summary of what was enhanced or added. Extract from tasks.md or reflection summary.]

        ## 2. Key Requirements Addressed
        [List the main requirements from tasks.md that this enhancement fulfilled.]
        - Requirement 1
        - Requirement 2

        ## 3. Implementation Overview
        [Brief description of how the enhancement was implemented. Summarize from progress.md or reflection document.]
        - Key files modified:
          - `[path/to/file1.ext]`
          - `[path/to/file2.ext]`
        - Main components changed: [List components]

        ## 4. Testing Performed
        [Summary of testing done, e.g., "Unit tests for new logic passed. Manual UI verification completed." From progress.md or reflection.]

        ## 5. Lessons Learned
        [Copy key lessons learned from `memory-bank/reflection/reflect-[task_name_or_id]-[date].md` or summarize them.]
        - Lesson 1
        - Lesson 2

        ## 6. Related Documents
        - Reflection: `../../reflection/reflect-[task_name_or_id]-[date].md`
        - (Link to specific creative docs if any were exceptionally made for L2)

        ## Notes
        [Any additional brief notes.]
        ```
4.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 2 task as "ARCHIVED".
        *   Add a link to the archive document: `Archived: ../archive/[archive_filename.md]`.
    b.  **`progress.md`:**
        *   Add a final entry: `[Date] - Task [Task Name] ARCHIVED. See archive/[archive_filename.md]`.
    c.  **`activeContext.md`:**
        *   Clear current task focus.
        *   Add to log: "Archived Level 2 task [Task Name]. Archive at `archive/[archive_filename.md]`."
5.  **Completion:**
    a.  State: "Basic archiving for Level 2 task [Task Name] complete. Archive document created at `memory-bank/archive/[archive_filename.md]`."
    b.  (Control returns to the fetching rule, e.g., `Level2/workflow-level2.mdc` or `visual-maps/archive-mode-map.mdc`).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level2/reflection-basic.mdc",
    "description": "Basic reflection for Level 2 (Simple Enhancement) tasks. Guides AI to create a structured reflection document using `edit_file`.",
    "globs": "**/Level2/reflection-basic.mdc",
    "alwaysApply": False,
    "body": """
# BASIC REFLECTION FOR LEVEL 2 TASKS (AI Instructions)

> **TL;DR:** This rule guides the creation of a basic reflection document for a completed Level 2 task using `edit_file`. It focuses on key outcomes, challenges, and lessons.

This rule is typically fetched by the Level 2 workflow orchestrator or the main REFLECT mode orchestrator if the task is L2.

## ⚙️ AI ACTIONS FOR LEVEL 2 REFLECTION:

1.  **Acknowledge & Context:**
    a.  State: "Initiating Basic Reflection for Level 2 task: [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the completed task details (original plan, requirements).
    c.  `read_file memory-bank/progress.md` for the implementation journey and any logged challenges/successes.
    d.  `read_file memory-bank/activeContext.md` to confirm implementation is marked complete.
2.  **Prepare Reflection Content (Based on Template Below):**
    a.  Synthesize information from `tasks.md` and `progress.md`.
3.  **Create Reflection File:**
    a.  Determine reflection filename: `reflect-[task_name_or_id]-[date].md` (e.g., `reflect-user-profile-update-20250515.md`).
    b.  Use `edit_file` to create/update `memory-bank/reflection/[reflection_filename.md]` with the structured content.
        **Basic Reflection Structure (Content for `edit_file`):**
        ```markdown
        # Level 2 Enhancement Reflection: [Feature Name from tasks.md]

        ## Task ID: [Task ID from tasks.md]
        ## Date of Reflection: [Current Date]
        ## Complexity Level: 2

        ## 1. Enhancement Summary
        [Brief one-paragraph summary of the enhancement: What was the goal? What was achieved?]

        ## 2. What Went Well?
        [Identify 2-3 specific positive aspects of the development process for this enhancement.]
        - Success point 1: [e.g., Integration with existing module was straightforward.]
        - Success point 2: [e.g., Testing covered all main use cases effectively.]

        ## 3. Challenges Encountered & Solutions
        [Identify 1-2 specific challenges and how they were addressed.]
        - Challenge 1: [e.g., Initial approach for X was inefficient.]
          - Solution: [e.g., Refactored to use Y pattern, improving performance.]
        - Challenge 2: (if any)

        ## 4. Key Learnings (Technical or Process)
        [List 1-2 key insights or lessons learned.]
        - Learning 1: [e.g., Realized library Z is better suited for this type of UI component.]
        - Learning 2: [e.g., Updating `tasks.md` more frequently for sub-tasks helps maintain clarity.]

        ## 5. Time Estimation Accuracy (If applicable)
        - Estimated time: [From tasks.md, if estimated]
        - Actual time: [Approximate actual time based on progress.md entries]
        - Variance & Reason: [Briefly, e.g., "+2 hours due to unexpected CSS conflict."]

        ## 6. Action Items for Future Work (Optional for L2, but good practice)
        [Any specific, actionable improvements for future tasks or for this feature.]
        - Action item 1: [e.g., Document the new CSS utility class created.]
        ```
4.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 2 task's REFLECT phase as "COMPLETE".
        *   Add a link to the reflection document: `Reflection: ../reflection/[reflection_filename.md]`.
    b.  **`activeContext.md`:**
        *   Update current focus: "Reflection complete for L2 task [Task Name]. Ready for ARCHIVE."
        *   Add to log: "Completed reflection for L2 task [Task Name]. Document at `reflection/[reflection_filename.md]`."
5.  **Completion:**
    a.  State: "Basic reflection for Level 2 task [Task Name] complete. Reflection document created at `memory-bank/reflection/[reflection_filename.md]`."
    b.  (Control returns to the fetching rule, e.g., `Level2/workflow-level2.mdc` or `visual-maps/reflect-mode-map.mdc`).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level2/task-tracking-basic.mdc",
    "description": "Basic task tracking for Level 2 (Simple Enhancement) tasks. Guides AI to structure `tasks.md` using `edit_file`.",
    "globs": "**/Level2/task-tracking-basic.mdc",
    "alwaysApply": False,
    "body": """
# BASIC TASK TRACKING FOR LEVEL 2 (AI Instructions)

> **TL;DR:** This rule outlines a streamlined task tracking approach for Level 2 (Simple Enhancement) tasks. Use `edit_file` to update `memory-bank/tasks.md` with the defined structure.

This rule is typically fetched by the PLAN mode orchestrator when a task is identified as Level 2.

## ⚙️ AI ACTIONS FOR LEVEL 2 TASK TRACKING (Updating `tasks.md`):

1.  **Acknowledge & Context:**
    a.  State: "Applying Basic Task Tracking for Level 2 task: [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` to locate the existing entry for this task (likely created minimally by VAN mode).
2.  **Update Task Entry in `tasks.md` (using `edit_file`):**
    a.  Ensure the task entry in `memory-bank/tasks.md` includes the following sections. If the task entry is new or minimal, create/populate these sections. If it exists, update them.

        **Task Structure for Level 2 (Content for `edit_file` on `tasks.md`):**
        ```markdown
        ## Task: [Task Name/ID - e.g., L2-001: Enhance User Profile Page]

        - **Status:** IN_PROGRESS_PLANNING (or update as planning proceeds)
        - **Priority:** [High/Medium/Low - user may specify, or default to Medium]
        - **Estimated Effort:** [Small/Medium - L2 tasks are generally not Large]
        - **Complexity Level:** 2
        - **Assigned To:** AI

        ### 1. Description
        [Brief description of the enhancement. What is the goal? What user problem does it solve? Synthesize from user request or `projectbrief.md`.]

        ### 2. Requirements / Acceptance Criteria
        [List 2-5 clear, testable requirements or acceptance criteria for the enhancement.]
        - [ ] Requirement 1: [e.g., User can upload a profile picture.]
        - [ ] Requirement 2: [e.g., Uploaded picture is displayed on the profile page.]
        - [ ] Requirement 3: [e.g., Error message shown if upload fails.]

        ### 3. Sub-tasks (Implementation Steps)
        [Break the enhancement into 3-7 high-level sub-tasks. These are for planning and will be checked off during IMPLEMENT mode.]
        - [ ] Sub-task 1: [e.g., Add file input field to profile form.]
        - [ ] Sub-task 2: [e.g., Implement backend endpoint for image upload.]
        - [ ] Sub-task 3: [e.g., Store image reference in user model.]
        - [ ] Sub-task 4: [e.g., Display uploaded image on profile page.]
        - [ ] Sub-task 5: [e.g., Add basic error handling for upload.]
        - [ ] Sub-task 6: [e.g., Write unit tests for upload endpoint.]
        - [ ] Sub-task 7: [e.g., Manual test of upload and display.]

        ### 4. Dependencies (If any)
        [List any other tasks, modules, or external factors this enhancement depends on. For L2, these should be minimal.]
        - Dependency 1: [e.g., User authentication module must be functional.]

        ### 5. Notes
        [Any additional brief notes, context, or links relevant to planning this enhancement.]
        - [e.g., Max image size should be 2MB.]
        ```
3.  **Log Update:**
    a.  Use `edit_file` to add a note to `memory-bank/activeContext.md`:
        `[Timestamp] - Updated `tasks.md` with detailed plan for L2 task: [Task Name].`
4.  **Completion:**
    a.  State: "Basic task tracking structure applied to `tasks.md` for Level 2 task [Task Name]."
    b.  (Control returns to the PLAN mode orchestrator, which will then typically recommend CREATIVE (if any minor design needed and flagged) or IMPLEMENT mode).

**Key Principle:** For L2 tasks, `tasks.md` should provide a clear, actionable plan without excessive detail. Sub-tasks guide implementation.
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level2/workflow-level2.mdc",
    "description": "Basic workflow for Level 2 (Simple Enhancement) tasks. Guides AI through Initialization, Documentation Setup, Planning, Implementation, Reflection, and Archiving using `fetch_rules` for level-specific details.",
    "globs": "**/Level2/workflow-level2.mdc",
    "alwaysApply": False,
    "body": """
# WORKFLOW FOR LEVEL 2 TASKS (AI Instructions)

> **TL;DR:** This rule orchestrates the workflow for Level 2 (Simple Enhancement) tasks. It guides the AI through 6 key phases, fetching specific Level 2 rules for planning, reflection, and archiving.

This workflow is typically fetched after VAN mode has confirmed the task as Level 2.

## 🧭 LEVEL 2 WORKFLOW PHASES (AI Actions)

### Phase 1: INITIALIZATION (Confirmation & Context)
1.  **Acknowledge & Confirm L2:**
    a.  State: "Initiating Level 2 Workflow for [Task Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` and `memory-bank/activeContext.md` to confirm task is indeed Level 2 and gather initial scope.
2.  **Platform & File Verification (If not done by VAN):**
    a.  If VAN mode didn't fully complete platform detection or Memory Bank setup (e.g., if transitioning from a different context), briefly ensure core setup:
        i.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/platform-awareness.mdc`.
        ii. `fetch_rules` for `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
3.  **Task Entry:**
    a.  Ensure `tasks.md` has an entry for this L2 task. `activeContext.md` should reflect "Focus: L2 Task - [Task Name]".
4.  **Milestone:** State "L2 Initialization complete. Proceeding to Documentation Setup."

### Phase 2: DOCUMENTATION SETUP (Minimal Context Update)
1.  **Update `projectbrief.md` (If necessary):**
    a.  `read_file memory-bank/projectbrief.md`.
    b.  If the L2 enhancement significantly alters or adds to project goals, use `edit_file` to add a brief note. Often not needed for L2.
2.  **Update `activeContext.md`:**
    a.  Use `edit_file` to ensure `memory-bank/activeContext.md` clearly states: "Current Focus: Planning Level 2 Enhancement - [Task Name]".
3.  **Milestone:** State "L2 Documentation Setup complete. Proceeding to Task Planning."

### Phase 3: TASK PLANNING (PLAN Mode Actions)
1.  **Fetch L2 Planning Rule:**
    a.  State: "Fetching Level 2 task planning guidelines."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level2/task-tracking-basic.mdc`.
2.  **Follow Fetched Rule:**
    a.  The `task-tracking-basic.mdc` rule will guide you to use `edit_file` to update `memory-bank/tasks.md` with:
        *   Clear requirements/acceptance criteria.
        *   A list of 3-7 high-level sub-tasks for implementation.
        *   Minimal dependencies and notes.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Planning complete for L2 task [Task Name]. Ready for Implementation."
    b.  State: "Level 2 Planning complete. Sub-tasks defined in `tasks.md`. Recommend IMPLEMENT mode."
4.  **Milestone:** Await user confirmation to proceed to IMPLEMENT mode.

### Phase 4: IMPLEMENTATION (IMPLEMENT Mode Actions)
1.  **Acknowledge & Review Plan:**
    a.  State: "Initiating Implementation for L2 task [Task Name]."
    b.  `read_file memory-bank/tasks.md` to review the sub-tasks.
    c.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/command-execution.mdc` for tool usage guidelines.
2.  **Implement Sub-tasks:**
    a.  Iterate through sub-tasks in `tasks.md`.
    b.  For each sub-task:
        i.  Use `edit_file` for code changes.
        ii. Use `run_terminal_cmd` for simple builds or tests if applicable (platform-aware).
        iii. Use `edit_file` to update `memory-bank/progress.md` with actions taken and outcomes.
        iv. Use `edit_file` to mark the sub-task as complete in `tasks.md`.
3.  **Final Verification:**
    a.  Perform basic overall verification of the enhancement.
4.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Implementation complete for L2 task [Task Name]. Ready for Reflection."
    b.  State: "Level 2 Implementation complete. Recommend REFLECT mode."
5.  **Milestone:** Await user confirmation to proceed to REFLECT mode.

### Phase 5: REFLECTION (REFLECT Mode Actions)
1.  **Fetch L2 Reflection Rule:**
    a.  State: "Fetching Level 2 reflection guidelines."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level2/reflection-basic.mdc`.
2.  **Follow Fetched Rule:**
    a.  The `reflection-basic.mdc` rule will guide you to use `edit_file` to create `memory-bank/reflection/reflect-[task_name_or_id]-[date].md` with sections for summary, what went well, challenges, and key learnings.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Reflection complete for L2 task [Task Name]. Ready for Archiving."
    b.  State: "Level 2 Reflection complete. Reflection document created. Recommend ARCHIVE mode."
4.  **Milestone:** Await user confirmation to proceed to ARCHIVE mode.

### Phase 6: ARCHIVING (ARCHIVE Mode Actions)
1.  **Fetch L2 Archiving Rule:**
    a.  State: "Fetching Level 2 archiving guidelines."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level2/archive-basic.mdc`.
2.  **Follow Fetched Rule:**
    a.  The `archive-basic.mdc` rule will guide you to use `edit_file` to create `memory-bank/archive/archive-[task_name_or_id]-[date].md`, summarizing the enhancement, implementation, and linking to the reflection doc.
    b.  It will also guide updates to `tasks.md` (mark ARCHIVED) and `progress.md`.
3.  **Finalize Context:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md` to clear focus from the completed L2 task and state: "L2 Task [Task Name] archived. Ready for new task (VAN mode)."
4.  **Milestone:** State "Level 2 Task [Task Name] fully completed and archived. Recommend VAN mode for new task."
"""
},
# --- Level 3 Files ---
{
    "path": ".cursor/rules/isolation_rules/Level3/archive-intermediate.mdc",
    "description": "Intermediate archiving for Level 3 features. Guides AI to create a detailed archive document, linking to creative/reflection docs, using `edit_file`.",
    "globs": "**/Level3/archive-intermediate.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 ARCHIVE: INTERMEDIATE FEATURE DOCUMENTATION (AI Instructions)

> **TL;DR:** This rule guides the creation of an intermediate archive document for a completed Level 3 feature using `edit_file`. It ensures key information, including links to creative and reflection documents, is preserved.

This rule is typically fetched by the Level 3 workflow orchestrator or the main ARCHIVE mode orchestrator if the task is L3.

## ⚙️ AI ACTIONS FOR LEVEL 3 ARCHIVING:

1.  **Acknowledge & Context:**
    a.  State: "Initiating Intermediate Archiving for Level 3 feature: [Feature Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the completed feature details (original plan, requirements, links to creative docs).
    c.  `read_file memory-bank/reflection/reflect-[feature_name_or_id]-[date].md` for detailed lessons learned.
    d.  `read_file memory-bank/progress.md` for implementation summary and key milestones.
    e.  `read_file` all relevant `memory-bank/creative/creative-[aspect_name]-[date].md` documents associated with this feature.
2.  **Pre-Archive Checklist (AI Self-Correction):**
    a.  Confirm from `tasks.md` that the REFLECT phase for this L3 feature is marked complete.
    b.  Verify `memory-bank/reflection/reflect-[feature_name_or_id]-[date].md` exists and is finalized.
    c.  Verify all `memory-bank/creative/creative-*.md` documents linked in `tasks.md` for this feature exist.
    d.  If checks fail, state: "L3 ARCHIVE BLOCKED: Prerequisite documents (Reflection, Creative) are missing or incomplete for feature [Feature Name]. Please complete REFLECT / CREATIVE modes first." Await user.
3.  **Prepare Archive Content (Based on Template Below):**
    a.  Synthesize information from all gathered documents.
4.  **Create Archive File:**
    a.  Determine archive filename: `archive-[feature_name_or_id]-[date].md` (e.g., `archive-user-profile-enhancement-20250515.md`).
    b.  Use `edit_file` to create/update `memory-bank/archive/[archive_filename.md]` with the structured content.
        **L3 Archive Structure (Content for `edit_file`):**
        ```markdown
        # Feature Archive: [Feature Name from tasks.md]

        ## Feature ID: [Feature ID from tasks.md]
        ## Date Archived: [Current Date]
        ## Complexity Level: 3
        ## Status: COMPLETED & ARCHIVED

        ## 1. Feature Overview
        [Brief description of the feature and its purpose. Extract from `tasks.md` (original plan) or `projectbrief.md`.]

        ## 2. Key Requirements Met
        [List the main functional and non-functional requirements this feature addressed, from `tasks.md`.]
        - Requirement 1
        - Requirement 2

        ## 3. Design Decisions & Creative Outputs
        [Summary of key design choices made during the CREATIVE phase(s).]
        - **Links to Creative Documents:**
          - `../../creative/creative-[aspect1_name]-[date].md`
          - `../../creative/creative-[aspect2_name]-[date].md`
          - (Add all relevant creative docs)
        - Link to Style Guide (if applicable): `../../style-guide.md` (version used, if known)

        ## 4. Implementation Summary
        [High-level overview of how the feature was implemented. Summarize from `progress.md` or reflection document.]
        - Primary new components/modules created: [List]
        - Key technologies/libraries utilized: [List]
        - Link to main feature branch merge commit / PR (if available from `progress.md`): [URL]

        ## 5. Testing Overview
        [Brief summary of the testing strategy (unit, integration, E2E) and outcomes. From `progress.md` or reflection.]

        ## 6. Reflection & Lessons Learned
        - **Link to Reflection Document:** `../../reflection/reflect-[feature_name_or_id]-[date].md`
        - **Critical Lessons (copied from reflection for quick summary):**
          - Lesson 1: [Critical lesson]
          - Lesson 2: [Critical lesson]

        ## 7. Known Issues or Future Considerations (Optional)
        [Any minor known issues deferred or potential future enhancements related to this feature, from reflection doc.]

        ## 8. Affected Files/Components (Summary from `tasks.md` plan)
        [List key files/components that were created or significantly modified.]
        ```
5.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 3 feature task as "ARCHIVED".
        *   Add a link to the archive document: `Archived: ../archive/[archive_filename.md]`.
    b.  **`progress.md`:**
        *   Add a final entry: `[Date] - Feature [Feature Name] ARCHIVED. See archive/[archive_filename.md]`.
    c.  **`activeContext.md`:**
        *   Clear current feature focus.
        *   Add to log: "Archived Level 3 feature [Feature Name]. Archive at `archive/[archive_filename.md]`."
6.  **Completion:**
    a.  State: "Intermediate archiving for Level 3 feature [Feature Name] complete. Archive document created at `memory-bank/archive/[archive_filename.md]`."
    b.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level3/implementation-intermediate.mdc",
    "description": "Implementation guidelines for Level 3 intermediate features. Guides AI on modular development, design adherence, testing, and documentation using `edit_file` and `run_terminal_cmd`.",
    "globs": "**/Level3/implementation-intermediate.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 IMPLEMENTATION: BUILDING INTERMEDIATE FEATURES (AI Instructions)

> **TL;DR:** This rule guides the systematic implementation of a planned and designed Level 3 feature. Emphasize modular development, strict adherence to creative decisions and style guide, integration, testing, and ongoing Memory Bank updates using `edit_file` and `run_terminal_cmd`.

This rule is typically fetched by the IMPLEMENT mode orchestrator if the task is L3.

## ⚙️ AI ACTIONS FOR LEVEL 3 IMPLEMENTATION:

1.  **Acknowledge & Preparation:**
    a.  State: "Initiating Level 3 Implementation for feature: [Feature Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the detailed feature plan, sub-tasks, and links to creative documents.
    c.  `read_file` all relevant `memory-bank/creative/creative-[aspect_name]-[date].md` documents.
    d.  `read_file memory-bank/style-guide.md`.
    e.  `read_file memory-bank/techContext.md` for existing tech stack details.
    f.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/command-execution.mdc` for tool usage guidelines.
2.  **Development Environment Setup (Conceptual):**
    a.  Assume user has set up the dev environment (branch, tools, dependencies). If specific new dependencies were noted in PLAN/CREATIVE, remind user if they haven't confirmed installation.
3.  **Iterative Module/Component Implementation (Follow `tasks.md` sub-tasks):**
    a.  For each implementation sub-task in `tasks.md` for the L3 feature:
        i.  State: "Starting sub-task: [Sub-task description]."
        ii. **Code Module/Component:**
            *   Use `edit_file` to create/modify source code files.
            *   Adhere strictly to designs from `creative-*.md` docs and `style-guide.md`.
            *   Implement with modularity, encapsulation, and coding standards in mind.
            *   Address state management, API interactions, error handling, performance, and security as per designs or best practices.
        iii. **Write & Run Unit Tests:**
            *   Use `edit_file` to write unit tests for new/modified logic.
            *   Use `run_terminal_cmd` to execute these tests (e.g., `npm test [test_file_spec]`). Log output.
        iv. **Self-Review/Linting:**
            *   Conceptually review code against requirements and style guide.
            *   If linters are part of the project, use `run_terminal_cmd` to run linter on changed files.
        v.  **Update Memory Bank:**
            *   Use `edit_file` to update `memory-bank/progress.md` with details of the completed sub-task, files changed, test results, and any decisions made.
            *   Use `edit_file` to mark the sub-task as complete in `memory-bank/tasks.md`.
            *   Use `edit_file` to update `memory-bank/activeContext.md` with current sub-task progress.
4.  **Integrate Feature Modules/Components:**
    a.  Once individual modules/components are built, ensure they integrate correctly.
    b.  This may involve `edit_file` changes to connect them.
5.  **Perform Integration Testing:**
    a.  Use `run_terminal_cmd` to execute integration tests that cover interactions between the new feature's components and with existing system parts. Log output.
    b.  If UI is involved, perform manual or automated UI integration tests.
6.  **End-to-End Feature Testing:**
    a.  Validate the complete feature against user stories and requirements from `tasks.md`.
    b.  If UI involved, check accessibility and responsiveness.
7.  **Code Cleanup & Refinement:**
    a.  Review all new/modified code for clarity, efficiency, and adherence to standards. Use `edit_file` for refinements.
8.  **Final Memory Bank Updates & Completion:**
    a.  Ensure `tasks.md` implementation phase is marked complete.
    b.  Ensure `progress.md` has a comprehensive log of the implementation.
    c.  Use `edit_file` to update `memory-bank/activeContext.md`: "Level 3 Implementation for [Feature Name] complete. Ready for REFLECT mode."
    d.  State: "Level 3 feature [Feature Name] implementation complete. All sub-tasks and tests passed. Recommend REFLECT mode."
    e.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level3/planning-comprehensive.mdc",
    "description": "Comprehensive planning for Level 3 intermediate features. Guides AI to update `tasks.md` with detailed requirements, components, strategy, risks, and flag CREATIVE needs, using `edit_file`.",
    "globs": "**/Level3/planning-comprehensive.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 COMPREHENSIVE PLANNING (AI Instructions)

> **TL;DR:** This rule guides the comprehensive planning for Level 3 (Intermediate Feature) tasks. Use `edit_file` to update `memory-bank/tasks.md` with detailed requirements, component analysis, implementation strategy, dependencies, risks, and critically, flag aspects needing CREATIVE mode.

This rule is typically fetched by the PLAN mode orchestrator when a task is identified as Level 3.

## ⚙️ AI ACTIONS FOR LEVEL 3 COMPREHENSIVE PLANNING (Updating `tasks.md`):

1.  **Acknowledge & Context:**
    a.  State: "Initiating Comprehensive Planning for Level 3 feature: [Feature Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` to locate the existing entry for this L3 feature.
    c.  `read_file memory-bank/projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md` for broader context.
2.  **Define/Refine Task Entry in `tasks.md` (using `edit_file`):**
    a.  Ensure the task entry in `memory-bank/tasks.md` for the L3 feature is structured with the following sections. Create or elaborate on these sections.

        **Comprehensive L3 Task Structure (Content for `edit_file` on `tasks.md`):**
        ```markdown
        ## Task: [Task Name/ID - e.g., L3-001: Implement User Profile Feature]

        - **Status:** IN_PROGRESS_PLANNING
        - **Priority:** [High/Medium/Low - user may specify, or default to Medium]
        - **Complexity Level:** 3
        - **Assigned To:** AI
        - **Target Completion Date (Optional):** [User may specify]

        ### 1. Feature Description & Goals
        [Detailed description of the feature, its purpose, business value, and key objectives. What problems does it solve? What are the success criteria?]

        ### 2. Detailed Requirements
        #### 2.1. Functional Requirements
        [List specific functional requirements. Use actionable language. e.g., "FR1: System MUST allow users to upload an avatar image." ]
        - [ ] FR1: ...
        - [ ] FR2: ...
        #### 2.2. Non-Functional Requirements
        [List NFRs like performance, security, usability, maintainability. e.g., "NFR1: Profile page MUST load within 2 seconds."]
        - [ ] NFR1: ...
        - [ ] NFR2: ...

        ### 3. Component Analysis
        #### 3.1. New Components to be Created
        [List new components/modules needed for this feature. For each, briefly describe its responsibility.]
        - Component A: [Responsibility]
        - Component B: [Responsibility]
        #### 3.2. Existing Components to be Modified
        [List existing components/modules that will be affected or need modification.]
        - Component X: [Nature of modification]
        - Component Y: [Nature of modification]
        #### 3.3. Component Interactions
        [Describe or diagram (textually) how new/modified components will interact with each other and existing system parts.]

        ### 4. Implementation Strategy & High-Level Steps
        [Outline the overall approach to building the feature. Break it down into major phases or steps. These will become more detailed sub-tasks later.]
        1.  Step 1: [e.g., Design database schema changes for user profile.]
        2.  Step 2: [e.g., Develop backend API endpoints for profile data.]
        3.  Step 3: [e.g., Build frontend UI for profile page.]
        4.  Step 4: [e.g., Integrate frontend with backend.]
        5.  Step 5: [e.g., Write comprehensive tests.]

        ### 5. Dependencies & Integrations
        [List any technical dependencies (libraries, tools), data dependencies, or integrations with other systems/features.]
        - Dependency 1: [e.g., Requires `ImageMagick` library for image processing.]
        - Integration 1: [e.g., Integrates with existing Authentication service.]

        ### 6. Risk Assessment & Mitigation
        [Identify potential risks (technical, resource, schedule) and suggest mitigation strategies.]
        - Risk 1: [e.g., Performance of image upload at scale.]
          - Mitigation: [e.g., Implement asynchronous processing and CDN for images.]
        - Risk 2: [e.g., Compatibility with older browsers.]
          - Mitigation: [e.g., Use polyfills and perform cross-browser testing.]

        ### 7. Creative Phase Requirements (CRITICAL for L3)
        [Identify specific aspects of this feature that require dedicated design exploration in CREATIVE mode. Be specific.]
        - [ ] CREATIVE: Design UI/UX for the new User Profile page. (Type: UI/UX)
        - [ ] CREATIVE: Architect the avatar storage and processing pipeline. (Type: Architecture)
        - [ ] CREATIVE: Develop algorithm for profile data recommendations (if applicable). (Type: Algorithm)
        (If no creative phase is deemed necessary for a particular aspect, note "CREATIVE: Not required for [aspect]" or omit.)

        ### 8. Testing Strategy Overview
        [Briefly outline the testing approach: unit tests, integration tests, E2E tests, UAT focus areas.]

        ### 9. Notes & Open Questions
        [Any other relevant notes, assumptions, or questions to be resolved.]
        ```
3.  **Log Update:**
    a.  Use `edit_file` to add a note to `memory-bank/activeContext.md`:
        `[Timestamp] - Comprehensive plan for L3 feature [Feature Name] updated in tasks.md. Creative phases identified.`
4.  **Completion & Recommendation:**
    a.  State: "Comprehensive planning for Level 3 feature [Feature Name] is complete. `tasks.md` has been updated with the detailed plan."
    b.  **If Creative Phase Requirements were identified:** "The plan indicates that creative design is needed for [list aspects]. Recommend transitioning to CREATIVE mode."
    c.  **If NO Creative Phase Requirements were identified (uncommon for L3 but possible):** "No specific creative design phases were flagged. Recommend proceeding to IMPLEMENT mode (or VAN QA if complex tech setup is anticipated)."
    d.  (Control returns to the PLAN mode orchestrator).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level3/reflection-intermediate.mdc",
    "description": "Intermediate reflection for Level 3 features. Guides AI to create a detailed reflection document in `memory-bank/reflection/`, reviewing all development phases using `edit_file`.",
    "globs": "**/Level3/reflection-intermediate.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 REFLECTION: INTERMEDIATE FEATURE REVIEW (AI Instructions)

> **TL;DR:** This rule structures the reflection process for a completed Level 3 intermediate feature. Use `edit_file` to create a comprehensive `memory-bank/reflection/reflect-[feature_name_or_id]-[date].md` document, analyzing the entire development lifecycle.

This rule is typically fetched by the REFLECT mode orchestrator if the task is L3.

## ⚙️ AI ACTIONS FOR LEVEL 3 REFLECTION:

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating Intermediate Reflection for Level 3 feature: [Feature Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the original plan, requirements, and links to creative docs.
    c.  `read_file memory-bank/progress.md` for the detailed implementation journey.
    d.  `read_file` all relevant `memory-bank/creative/creative-[aspect_name]-[date].md` documents.
    e.  `read_file memory-bank/activeContext.md` to confirm implementation is marked complete.
2.  **Prepare Reflection Content (Based on Template Below):**
    a.  Synthesize information from all gathered documents. Analyze each phase of the L3 workflow.
3.  **Create Reflection File:**
    a.  Determine reflection filename: `reflect-[feature_name_or_id]-[date].md`.
    b.  Use `edit_file` to create/update `memory-bank/reflection/[reflection_filename.md]` with the structured content.
        **L3 Reflection Structure (Content for `edit_file`):**
        ```markdown
        # Feature Reflection: [Feature Name from tasks.md]

        ## Feature ID: [Feature ID from tasks.md]
        ## Date of Reflection: [Current Date]
        ## Complexity Level: 3

        ## 1. Brief Feature Summary & Overall Outcome
        [What was the feature? What was its main goal? How well was the goal achieved? Did it meet all critical requirements from `tasks.md`?]

        ## 2. Planning Phase Review
        - How effective was the comprehensive planning (`Level3/planning-comprehensive.mdc`)?
        - Was the initial breakdown in `tasks.md` (components, strategy, risks) accurate?
        - What worked well in planning? What could have been planned better?
        - Were estimations (if made) accurate? Reasons for variance?

        ## 3. Creative Phase(s) Review (if applicable)
        - Were the correct aspects of the feature flagged for CREATIVE mode?
        - Review each `creative-*.md` document:
          - How effective were the design decisions?
          - Did the designs translate well into practical implementation? Any friction?
          - Was the `style-guide.md` sufficient?
        - What could improve the creative process for similar features?

        ## 4. Implementation Phase Review
        - What were the major successes during implementation (e.g., efficient module development, good use of libraries)?
        - What were the biggest challenges or roadblocks? How were they overcome?
        - Were there any unexpected technical difficulties or complexities?
        - How was adherence to the style guide and coding standards during implementation?
        - Review `progress.md` for key implementation notes: were there deviations from plan? Why?

        ## 5. Testing Phase Review
        - Was the testing strategy (unit, integration, E2E for the feature) effective?
        - Did testing uncover significant issues early enough?
        - What could improve the testing process for similar features?
        - Were there any bugs found post-implementation that testing should have caught?

        ## 6. What Went Well? (Overall - Highlight 3-5 key positives for this feature)
        - [Positive 1]
        - [Positive 2]
        - [Positive 3]

        ## 7. What Could Have Been Done Differently? (Overall - Identify 3-5 areas for improvement)
        - [Improvement Area 1]
        - [Improvement Area 2]
        - [Improvement Area 3]

        ## 8. Key Lessons Learned
        ### 8.1. Technical Lessons
        [New insights about technologies, patterns, architecture specific to this feature.]
        - Technical Lesson 1:
        ### 8.2. Process Lessons
        [Insights about the L3 workflow, communication, task management, tool usage.]
        - Process Lesson 1:
        ### 8.3. Estimation Lessons (if applicable)
        [Lessons about estimating work for features of this scale.]
        - Estimation Lesson 1:

        ## 9. Actionable Improvements for Future L3 Features
        [Specific, actionable suggestions for future intermediate feature development.]
        - Improvement 1: [e.g., "Standardize API error response format across modules."]
        - Improvement 2: [e.g., "Allocate more time for integration testing between X and Y components."]
        ```
4.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 3 feature's REFLECT phase as "COMPLETE".
        *   Add a link to the reflection document: `Reflection: ../reflection/[reflection_filename.md]`.
    b.  **`activeContext.md`:**
        *   Update current focus: "Reflection complete for L3 feature [Feature Name]. Ready for ARCHIVE."
        *   Add to log: "Completed reflection for L3 feature [Feature Name]. Document at `reflection/[reflection_filename.md]`."
5.  **Completion:**
    a.  State: "Intermediate reflection for Level 3 feature [Feature Name] complete. Reflection document created at `memory-bank/reflection/[reflection_filename.md]`."
    b.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level3/task-tracking-intermediate.mdc",
    "description": "Intermediate task tracking for Level 3 features. Guides AI to update `tasks.md` with structured components, steps, creative markers, and checkpoints using `edit_file`.",
    "globs": "**/Level3/task-tracking-intermediate.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 INTERMEDIATE TASK TRACKING (AI Instructions)

> **TL;DR:** This rule provides guidelines for structured task tracking in `memory-bank/tasks.md` for Level 3 (Intermediate Feature) tasks. Use `edit_file` to create and maintain this structure.

This rule is typically fetched by the PLAN mode orchestrator (`Level3/planning-comprehensive.mdc` will refer to this structure).

## ⚙️ AI ACTIONS FOR LEVEL 3 TASK TRACKING (Structure for `tasks.md`):

When `Level3/planning-comprehensive.mdc` guides you to detail the plan in `tasks.md`, use `edit_file` to ensure the entry for the Level 3 feature includes the following structure.

**Task Entry Template for `tasks.md` (L3 Feature):**
```markdown
## Task: [L3-ID: Feature Name, e.g., L3-001: Implement User Profile Page with Avatar Upload]

- **Status:** [e.g., IN_PROGRESS_PLANNING, PENDING_CREATIVE, IN_PROGRESS_IMPLEMENTATION, etc.]
- **Priority:** [High/Medium/Low]
- **Complexity Level:** 3
- **Assigned To:** AI
- **Target Completion Date (Optional):** [YYYY-MM-DD]
- **Links:**
    - Project Brief: `../projectbrief.md`
    - Creative Docs: (List links as they are created, e.g., `../creative/creative-profile-ui-20250515.md`)
    - Reflection Doc: (Link when created)
    - Archive Doc: (Link when created)

### 1. Feature Description & Goals
[As defined in `planning-comprehensive.mdc` guidance]

### 2. Detailed Requirements
#### 2.1. Functional Requirements
[As defined in `planning-comprehensive.mdc` guidance]
- [ ] FR1: ...
#### 2.2. Non-Functional Requirements
[As defined in `planning-comprehensive.mdc` guidance]
- [ ] NFR1: ...

### 3. Component Analysis
#### 3.1. New Components
[As defined in `planning-comprehensive.mdc` guidance]
- Component A: ...
#### 3.2. Modified Components
[As defined in `planning-comprehensive.mdc` guidance]
- Component X: ...
#### 3.3. Component Interactions
[As defined in `planning-comprehensive.mdc` guidance]

### 4. Implementation Strategy & Sub-Tasks
[Break down the high-level steps from `planning-comprehensive.mdc` into more granular, checkable sub-tasks for implementation. Prefix with `IMPL:`]
- **Phase 1: Backend API Development**
  - [ ] IMPL: Define data models for user profile and avatar.
  - [ ] IMPL: Create API endpoint for fetching profile data.
  - [ ] IMPL: Create API endpoint for updating profile data.
  - [ ] IMPL: Create API endpoint for avatar image upload.
  - [ ] IMPL: Write unit tests for API endpoints.
- **Phase 2: Frontend UI Development**
  - [ ] IMPL: Build profile display component.
  - [ ] IMPL: Build profile edit form component.
  - [ ] IMPL: Implement avatar upload UI.
  - [ ] IMPL: Integrate frontend components with backend APIs.
  - [ ] IMPL: Write component tests for UI.
- **Phase 3: Testing & Refinement**
  - [ ] IMPL: Perform integration testing.
  - [ ] IMPL: Address any bugs found.
  - [ ] IMPL: Code review and cleanup.

### 5. Dependencies & Integrations
[As defined in `planning-comprehensive.mdc` guidance]

### 6. Risk Assessment & Mitigation
[As defined in `planning-comprehensive.mdc` guidance]

### 7. Creative Phase Requirements & Outcomes
[List aspects flagged for CREATIVE mode in `planning-comprehensive.mdc`. Update with status and link to creative doc once done.]
- [ ] CREATIVE: Design UI/UX for the new User Profile page. (Type: UI/UX)
  - Status: [PENDING/IN_PROGRESS/COMPLETED]
  - Document: `../creative/creative-profile-ui-[date].md` (once created)
- [ ] CREATIVE: Architect avatar storage. (Type: Architecture)
  - Status: [PENDING/IN_PROGRESS/COMPLETED]
  - Document: `../creative/creative-avatar-storage-[date].md` (once created)

### 8. Testing Strategy Overview
[As defined in `planning-comprehensive.mdc` guidance]

### 9. Checkpoints & Phase Gates
- [ ] **PLAN Phase Complete:** [Date]
- [ ] **CREATIVE Phase(s) Complete:** [Date] (All creative sub-tasks in section 7 marked complete)
- [ ] **IMPLEMENT Phase Complete:** [Date] (All IMPL sub-tasks in section 4 marked complete)
- [ ] **REFLECT Phase Complete:** [Date]
- [ ] **ARCHIVE Phase Complete:** [Date] (Feature fully archived)

### 10. Notes & Open Questions
[As defined in `planning-comprehensive.mdc` guidance]
```

## 🔄 PROGRESS TRACKING (AI Actions during IMPLEMENT, REFLECT, etc.)
*   As sub-tasks (IMPL, CREATIVE, etc.) are completed, use `edit_file` to mark them `[x]` in `tasks.md`.
*   Update the main `Status:` field of the L3 task entry.
*   Update the `Checkpoints & Phase Gates` section as each major phase concludes.
*   Log detailed activities in `memory-bank/progress.md`.

**Key Principle:** `tasks.md` for L3 features should be a living document, meticulously updated via `edit_file` to reflect the comprehensive plan and ongoing progress through all CMB modes.
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level3/workflow-level3.mdc",
    "description": "Orchestrates the workflow for Level 3 (Intermediate Feature) tasks, guiding AI through comprehensive planning, creative design, structured implementation, reflection, and archiving by fetching specific L3 and Core rules.",
    "globs": "**/Level3/workflow-level3.mdc",
    "alwaysApply": False,
    "body": """
# LEVEL 3 WORKFLOW: INTERMEDIATE FEATURE DEVELOPMENT (AI Instructions)

> **TL;DR:** This rule orchestrates the structured workflow for Level 3 (Intermediate Feature) tasks. It guides the AI through comprehensive planning, targeted creative design, systematic implementation, in-depth reflection, and feature-specific archiving by fetching appropriate L3 and Core rules.

This workflow is typically fetched after VAN mode has confirmed the task as Level 3.

## 🧭 LEVEL 3 WORKFLOW PHASES (AI Actions)

### Phase 1: INITIALIZATION (Confirmation & Context)
1.  **Acknowledge & Confirm L3:**
    a.  State: "Initiating Level 3 Workflow for [Feature Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` and `memory-bank/activeContext.md` to confirm task is Level 3 and gather initial scope.
2.  **Core Setup Verification (If not fully done by VAN):**
    a.  Ensure platform awareness: `fetch_rules` for `.cursor/rules/isolation_rules/Core/platform-awareness.mdc`.
    b.  Ensure Memory Bank structure: `fetch_rules` for `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
3.  **Task Entry & Context:**
    a.  Verify `tasks.md` has an entry for this L3 feature.
    b.  `edit_file memory-bank/activeContext.md` to set focus: "Focus: L3 Feature - [Feature Name] - Initializing."
4.  **Milestone:** State "L3 Initialization complete. Proceeding to Documentation Setup."

### Phase 2: DOCUMENTATION SETUP (L3 Specific)
1.  **Update `projectbrief.md` (Briefly):**
    a.  `read_file memory-bank/projectbrief.md`. Use `edit_file` to add a note if this L3 feature significantly impacts overall project goals.
2.  **Update `activeContext.md`:**
    a.  Use `edit_file` to set `memory-bank/activeContext.md` focus: "Current Focus: Planning Level 3 Feature - [Feature Name]".
3.  **Prepare `tasks.md` for L3 Planning:**
    a.  Acknowledge that `tasks.md` will be updated extensively in the next phase.
4.  **Milestone:** State "L3 Documentation Setup complete. Proceeding to Feature Planning."

### Phase 3: FEATURE PLANNING (PLAN Mode Actions)
1.  **Fetch L3 Planning Rules:**
    a.  State: "Fetching Level 3 comprehensive planning and task tracking guidelines."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level3/planning-comprehensive.mdc`.
    c.  (The `planning-comprehensive.mdc` rule will internally reference the structure from `Level3/task-tracking-intermediate.mdc` for `tasks.md` updates).
2.  **Follow Fetched Rule (`planning-comprehensive.mdc`):**
    a.  This rule will guide you to use `edit_file` to update `memory-bank/tasks.md` with:
        *   Detailed feature description, goals, requirements (functional & non-functional).
        *   Component analysis (new, modified, interactions).
        *   Implementation strategy and high-level steps.
        *   Dependencies, risks, and mitigations.
        *   **Crucially: Flag aspects requiring CREATIVE mode.**
        *   Testing strategy overview.
3.  **Update Context & Recommend Next Mode:**
    a.  `read_file memory-bank/tasks.md` to see if any "CREATIVE: ..." items were flagged.
    b.  Use `edit_file` to update `memory-bank/activeContext.md`: "Planning complete for L3 feature [Feature Name]. Creative phases [identified/not identified]."
    c.  **If CREATIVE phases flagged:** State "Level 3 Planning complete. Creative design phases identified in `tasks.md`. Recommend CREATIVE mode." Await user.
    d.  **If NO CREATIVE phases flagged:** State "Level 3 Planning complete. No specific creative design phases flagged. Recommend IMPLEMENT mode (or VAN QA if complex tech setup anticipated)." Await user.
4.  **Milestone:** Planning phase complete. Await user confirmation for next mode.

### Phase 4: CREATIVE PHASES (CREATIVE Mode Actions - If Triggered)
1.  **Acknowledge & Fetch Creative Orchestrator:**
    a.  State: "Initiating CREATIVE mode for L3 feature [Feature Name] as per plan."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/creative-mode-map.mdc`.
2.  **Follow Fetched Rule (`creative-mode-map.mdc`):**
    a.  This rule will guide you to:
        *   Identify "CREATIVE: Design..." sub-tasks from `tasks.md`.
        *   For each, fetch the appropriate `Phases/CreativePhase/[design-type].mdc` rule.
        *   Generate design options, make decisions, and document in `memory-bank/creative/creative-[aspect]-[date].md` using `edit_file`.
        *   Update `tasks.md` to mark creative sub-tasks complete and link to documents.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Creative design phases complete for L3 feature [Feature Name]. Ready for Implementation."
    b.  State: "Level 3 Creative phases complete. Design documents created. Recommend IMPLEMENT mode."
4.  **Milestone:** Creative phase complete. Await user confirmation for IMPLEMENT mode.

### Phase 5: IMPLEMENTATION (IMPLEMENT Mode Actions)
1.  **Fetch L3 Implementation Rule:**
    a.  State: "Initiating Implementation for L3 feature [Feature Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level3/implementation-intermediate.mdc`.
2.  **Follow Fetched Rule (`implementation-intermediate.mdc`):**
    a.  This rule will guide you to:
        *   Review `tasks.md` (plan) and `creative-*.md` (designs).
        *   Implement feature modules iteratively using `edit_file` for code.
        *   Adhere to `style-guide.md`.
        *   Write and run unit/integration tests using `run_terminal_cmd`.
        *   Update `tasks.md` (sub-tasks) and `progress.md` regularly.
        *   Perform end-to-end feature testing.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Implementation complete for L3 feature [Feature Name]. Ready for Reflection."
    b.  State: "Level 3 Implementation complete. Recommend REFLECT mode."
4.  **Milestone:** Implementation phase complete. Await user confirmation for REFLECT mode.

### Phase 6: REFLECTION (REFLECT Mode Actions)
1.  **Fetch L3 Reflection Rule:**
    a.  State: "Initiating Reflection for L3 feature [Feature Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level3/reflection-intermediate.mdc`.
2.  **Follow Fetched Rule (`reflection-intermediate.mdc`):**
    a.  This rule will guide you to use `edit_file` to create `memory-bank/reflection/reflect-[feature_name_or_id]-[date].md`, analyzing all development phases, lessons learned, and improvements.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Reflection complete for L3 feature [Feature Name]. Ready for Archiving."
    b.  State: "Level 3 Reflection complete. Reflection document created. Recommend ARCHIVE mode."
4.  **Milestone:** Reflection phase complete. Await user confirmation for ARCHIVE mode.

### Phase 7: ARCHIVING (ARCHIVE Mode Actions)
1.  **Fetch L3 Archiving Rule:**
    a.  State: "Initiating Archiving for L3 feature [Feature Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level3/archive-intermediate.mdc`.
2.  **Follow Fetched Rule (`archive-intermediate.mdc`):**
    a.  This rule will guide you to use `edit_file` to create `memory-bank/archive/archive-[feature_name_or_id]-[date].md`, summarizing the feature and linking to plan, creative, and reflection docs.
    b.  It will also guide updates to `tasks.md` (mark ARCHIVED) and `progress.md`.
3.  **Finalize Context:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md` to clear focus from the completed L3 feature: "L3 Feature [Feature Name] archived. Ready for new task (VAN mode)."
4.  **Milestone:** State "Level 3 Feature [Feature Name] fully completed and archived. Recommend VAN mode for new task."
"""
},
# --- Level 4 Files ---
{
    "path": ".cursor/rules/isolation_rules/Level4/architectural-planning.mdc",
    "description": "Architectural planning guidelines for Level 4 (Complex System) tasks. Guides AI to create comprehensive architectural documentation using `edit_file` and link to `tasks.md`.",
    "globs": "**/Level4/architectural-planning.mdc",
    "alwaysApply": False,
    "body": """
# ARCHITECTURAL PLANNING FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule guides comprehensive architectural planning for Level 4 (Complex System) tasks. Use `edit_file` to create detailed architectural documents (or sections within `tasks.md` / linked documents), covering requirements, context, vision, principles, alternatives, decisions (ADRs), and diagrams (descriptively).

This rule is typically fetched by the PLAN mode orchestrator (`Level4/workflow-level4.mdc` will fetch this after `Level4/task-tracking-advanced.mdc`).

## ⚙️ AI ACTIONS FOR LEVEL 4 ARCHITECTURAL PLANNING:

1.  **Acknowledge & Context:**
    a.  State: "Initiating Architectural Planning for Level 4 system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` (for the L4 task structure created by `task-tracking-advanced.mdc`).
    c.  `read_file memory-bank/projectbrief.md`, `productContext.md`, `systemPatterns.md` (existing patterns), `techContext.md`.
2.  **Document Architectural Plan (using `edit_file` to update `tasks.md` or a dedicated `memory-bank/architecture/system-[system_name]-arch-plan-[date].md` linked from `tasks.md`):**

    Create/Populate the following sections:

    ```markdown
    ### Section X: Architectural Planning for [System Name] (L4)

    #### X.1. Architectural Requirements Analysis (Derived from main requirements)
    - **Key Functional Drivers for Architecture:** [e.g., High concurrency user access, Real-time data processing, Complex workflow orchestration]
    - **Key Non-Functional Requirements (Quality Attributes):**
      - Performance: [Specific targets, e.g., Sub-second API response under X load]
      - Scalability: [e.g., Support Y concurrent users, Z TPS, linear scaling strategy]
      - Availability: [e.g., 99.99% uptime, fault tolerance mechanisms]
      - Security: [e.g., Compliance with PCI-DSS, data encryption at rest and in transit, robust authN/authZ]
      - Maintainability: [e.g., Modular design, clear interfaces, comprehensive testability]
      - Extensibility: [e.g., Ability to add new service types with minimal core changes]
    - **Domain Model Overview:** [Briefly describe key entities and relationships relevant to architecture].

    #### X.2. Business Context for Architecture
    - **Business Objectives Driving Architecture:** [e.g., Reduce operational costs by 20%, Enable new market entry]
    - **Key Stakeholder Concerns (Architectural):** [e.g., CTO requires use of existing Kubernetes infrastructure]
    - **Architectural Constraints (Technical, Organizational, External, Regulatory):**
      - Technical: [e.g., Must integrate with legacy System Z via SOAP API]
      - Organizational: [e.g., Development team skill set primarily Java and Python]
      - Budgetary: [e.g., Preference for open-source technologies where feasible]

    #### X.3. Architectural Vision & Goals
    - **Vision Statement:** [A concise statement for the system's architecture, e.g., "A resilient, scalable microservices architecture enabling rapid feature development..."]
    - **Strategic Architectural Goals:** [e.g., Achieve loose coupling between services, Ensure data consistency across distributed components]

    #### X.4. Architectural Principles (Guiding Decisions)
    [List 3-5 core architectural principles for this system, e.g.:]
    - Principle 1: Event-Driven Design for asynchronous operations.
    - Principle 2: API-First approach for all service interactions.
    - Principle 3: Design for Failure - anticipate and handle component failures gracefully.

    #### X.5. Architectural Alternatives Explored (High-Level)
    [Briefly describe 1-2 major architectural patterns/styles considered and why the chosen one (or a hybrid) is preferred. E.g., "Considered monolithic vs. microservices. Chose microservices for scalability..."]

    #### X.6. Key Architectural Decisions (ADRs - Create separate ADRs or summarize here)
    [For each major architectural decision, document using an ADR-like format or link to separate ADR files in `memory-bank/architecture/adrs/`.]
    - **ADR-001: Choice of Messaging Queue**
      - Status: Decided
      - Context: Need for asynchronous communication between services A and B.
      - Decision: Use RabbitMQ.
      - Rationale: Proven reliability, supports required messaging patterns, team familiarity.
      - Alternatives Considered: Kafka (overkill for current needs), Redis Streams (less mature).
    - **ADR-002: Database Technology for Service C**
      - ...

    #### X.7. High-Level Architecture Diagrams (Textual Descriptions)
    [AI describes diagrams. User might create actual diagrams based on these descriptions.]
    - **System Context Diagram Description:** [Describe the system, its users, and external systems it interacts with.]
    - **Component Diagram Description:** [Describe major logical components/services and their primary interactions/dependencies.]
    - **Data Flow Diagram Description (Key Flows):** [Describe how data flows through the system for 1-2 critical use cases.]
    - **Deployment View Description (Conceptual):** [Describe how components might be deployed, e.g., "Services A, B, C as Docker containers in Kubernetes. Database D as a managed cloud service."]

    #### X.8. Technology Stack (Key Choices)
    [List key technologies chosen for backend, frontend, database, messaging, caching, etc., with brief rationale if not covered in ADRs.]
    - Backend: [e.g., Java Spring Boot]
    - Database: [e.g., PostgreSQL]

    #### X.9. Architectural Risks & Mitigation
    [Identify key risks related to the chosen architecture and how they will be mitigated.]
    - Risk: [e.g., Complexity of managing distributed transactions in microservices.]
      - Mitigation: [e.g., Employ SAGA pattern, implement robust monitoring and compensating transactions.]
    ```
3.  **Log Update:**
    a.  Use `edit_file` to add a note to `memory-bank/activeContext.md`:
        `[Timestamp] - Architectural planning for L4 system [System Name] documented in tasks.md / linked architecture plan.`
4.  **Completion & Recommendation:**
    a.  State: "Architectural planning for Level 4 system [System Name] is complete. Key decisions and structure documented."
    b.  "Recommend proceeding to CREATIVE phases for detailed design of specific components/services identified in the architectural plan, or directly to Phased Implementation planning if architecture is sufficiently detailed."
    c.  (Control returns to the PLAN mode orchestrator / L4 Workflow orchestrator).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level4/archive-comprehensive.mdc",
    "description": "Comprehensive archiving for Level 4 (Complex System) tasks. Guides AI to create extensive archive documentation using `edit_file`, consolidating all project artifacts.",
    "globs": "**/Level4/archive-comprehensive.mdc",
    "alwaysApply": False,
    "body": """
# COMPREHENSIVE ARCHIVING FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule guides the creation of a comprehensive archive for a completed Level 4 (Complex System) task using `edit_file`. It involves consolidating all system knowledge, design decisions, implementation details, and lessons learned into a structured archive.

This rule is typically fetched by the Level 4 workflow orchestrator or the main ARCHIVE mode orchestrator if the task is L4.

## ⚙️ AI ACTIONS FOR LEVEL 4 COMPREHENSIVE ARCHIVING:

1.  **Acknowledge & Context Gathering:**
    a.  State: "Initiating Comprehensive Archiving for Level 4 system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` (for the entire L4 task history, links to architectural plans, creative docs, etc.).
    c.  `read_file memory-bank/reflection/reflect-[system_name_or_id]-[date].md` (for the comprehensive reflection).
    d.  `read_file memory-bank/progress.md` (for the full development log).
    e.  `read_file` all relevant `memory-bank/architecture/`, `memory-bank/creative/`, and other supporting documents.
    f.  `read_file memory-bank/projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`.
2.  **Pre-Archive Checklist (AI Self-Correction):**
    a.  Confirm from `tasks.md` that the REFLECT phase for this L4 system is marked complete.
    b.  Verify `memory-bank/reflection/reflect-[system_name_or_id]-[date].md` exists and is finalized.
    c.  If checks fail, state: "L4 ARCHIVE BLOCKED: Comprehensive Reflection is not complete for system [System Name]. Please complete REFLECT mode first." Await user.
3.  **Create Archive Document Structure (Main Archive File):**
    a.  Determine archive filename: `archive-system-[system_name_or_id]-[date].md`.
    b.  Use `edit_file` to create/update `memory-bank/archive/[archive_filename.md]`. This will be the main archive document.
4.  **Populate Archive Document (Using `edit_file` and Template Below):**
    a.  Iteratively populate the sections of the main archive document by synthesizing information from all gathered Memory Bank files.
        **L4 Comprehensive Archive Structure (Content for `edit_file` into `archive-system-*.md`):**
        ```markdown
        # System Archive: [System Name from tasks.md]

        ## System ID: [System ID from tasks.md]
        ## Date Archived: [Current Date]
        ## Complexity Level: 4
        ## Status: COMPLETED & ARCHIVED

        ## 1. System Overview
        ### 1.1. System Purpose and Scope
        [Synthesize from `projectbrief.md`, initial `tasks.md` description.]
        ### 1.2. Final System Architecture
        [Summarize key architectural decisions from architectural planning docs/ADRs. Link to detailed architecture documents if they exist in `memory-bank/architecture/` or `documentation/`.]
        ### 1.3. Key Components & Modules
        [List final key components and their purpose. From `tasks.md` component breakdown and implementation details.]
        ### 1.4. Integration Points
        [Describe internal and external integration points. From architectural plan / `techContext.md`.]
        ### 1.5. Technology Stack
        [Final technology stack used. From `techContext.md` / implementation details.]
        ### 1.6. Deployment Environment Overview
        [Brief overview of how the system is deployed. From `techContext.md` / deployment plans.]

        ## 2. Requirements and Design Documentation Links
        - Business Requirements: [Link to relevant section in `productContext.md` or `tasks.md`]
        - Functional Requirements: [Link to detailed FRs in `tasks.md`]
        - Non-Functional Requirements: [Link to NFRs in `tasks.md` or architectural plan]
        - Architecture Decision Records (ADRs): [Link to `memory-bank/architecture/adrs/` or summaries in arch plan]
        - Creative Design Documents:
          - [Link to `../../creative/creative-[aspect1]-[date].md`]
          - [Link to `../../creative/creative-[aspect2]-[date].md`]
          - (List all relevant creative docs)

        ## 3. Implementation Documentation Summary
        ### 3.1. Phased Implementation Overview (if applicable)
        [Summary of how phased implementation (`Level4/phased-implementation.mdc`) was executed. From `progress.md`.]
        ### 3.2. Key Implementation Details & Challenges
        [Highlight significant implementation details or challenges overcome. From `progress.md` / reflection doc.]
        ### 3.3. Code Repository & Key Branches/Tags
        [Link to Git repository. Note main branch, key feature branches, and final release tag/commit.]
        ### 3.4. Build and Packaging Details
        [Summary of build process and key artifacts. From `techContext.md` / `progress.md`.]

        ## 4. API Documentation (If applicable)
        [Link to or summarize key API endpoint documentation. If extensive, this might be a separate document in `documentation/` linked here.]

        ## 5. Data Model and Schema Documentation (If applicable)
        [Link to or summarize data model and schema. If extensive, separate document in `documentation/` linked here.]

        ## 6. Security Documentation Summary
        [Summary of key security measures implemented. Link to detailed security design if available.]

        ## 7. Testing Documentation Summary
        - Test Strategy: [Overall strategy. From `tasks.md` / reflection.]
        - Test Results: [Summary of final test outcomes, key bugs fixed. Link to detailed test reports if any.]
        - Known Issues & Limitations (at time of archive): [From reflection doc.]

        ## 8. Deployment Documentation Summary
        [Link to or summarize deployment procedures, environment configs. From `techContext.md` / `progress.md`.]

        ## 9. Operational Documentation Summary
        [Link to or summarize key operational procedures, monitoring, backup/recovery. From `techContext.md` / reflection.]

        ## 10. Knowledge Transfer & Lessons Learned
        - **Link to Comprehensive Reflection Document:** `../../reflection/reflect-[system_name_or_id]-[date].md`
        - **Key Strategic Learnings (copied from reflection):**
          - [Learning 1]
          - [Learning 2]
        - **Recommendations for Future Similar Systems (copied from reflection):**
          - [Recommendation 1]

        ## 11. Project History Summary
        [Brief overview of project timeline and key milestones achieved. From `progress.md`.]
        ```
5.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 4 system task as "ARCHIVED".
        *   Add a link to the main archive document: `Archived: ../archive/[archive_filename.md]`.
    b.  **`progress.md`:**
        *   Add a final entry: `[Date] - System [System Name] ARCHIVED. Comprehensive archive at archive/[archive_filename.md]`.
    c.  **`activeContext.md`:**
        *   Clear current system focus.
        *   Add to log: "Archived Level 4 system [System Name]. Archive at `archive/[archive_filename.md]`."
    d.  Consider updating `projectbrief.md` with a note about the system's completion and link to its archive.
6.  **Completion:**
    a.  State: "Comprehensive archiving for Level 4 system [System Name] complete. Main archive document created at `memory-bank/archive/[archive_filename.md]`."
    b.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level4/phased-implementation.mdc",
    "description": "Phased Implementation for Level 4 (Complex System) tasks. Guides AI to manage implementation in distinct phases (Foundation, Core, Extension, Integration, Finalization) using `edit_file` and `run_terminal_cmd`.",
    "globs": "**/Level4/phased-implementation.mdc",
    "alwaysApply": False,
    "body": """
# PHASED IMPLEMENTATION FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule guides the structured, phased implementation of a Level 4 (Complex System) task. It involves breaking down the implementation into logical phases, each with its own objectives, tasks, and verification. Use `edit_file` for code and documentation, `run_terminal_cmd` for builds/tests.

This rule is typically fetched by the IMPLEMENT mode orchestrator if the task is L4.

## ⚙️ AI ACTIONS FOR LEVEL 4 PHASED IMPLEMENTATION:

1.  **Acknowledge & Preparation:**
    a.  State: "Initiating Phased Implementation for Level 4 system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` for the architectural plan, component breakdown, and any pre-defined implementation phases.
    c.  `read_file` all relevant `memory-bank/architecture/` and `memory-bank/creative/` documents.
    d.  `read_file memory-bank/style-guide.md` and `memory-bank/techContext.md`.
    e.  `fetch_rules` for `.cursor/rules/isolation_rules/Core/command-execution.mdc` for tool usage guidelines.
2.  **Define/Confirm Implementation Phases (if not already detailed in `tasks.md`):**
    a.  Based on the architectural plan, propose or confirm a phased approach (e.g., Foundation, Core Services, Feature Extensions, Integration, Finalization).
    b.  For each phase, define:
        *   Primary objectives.
        *   Key components/modules to be built/integrated.
        *   High-level sub-tasks within that phase.
        *   Exit criteria / verification for the phase.
    c.  Use `edit_file` to document these phases and their sub-tasks within the L4 task entry in `memory-bank/tasks.md`.
3.  **Iterate Through Implementation Phases:**
    a.  For each defined phase (e.g., "Foundation Phase"):
        i.  State: "Starting [Phase Name] for system [System Name]."
        ii. `edit_file memory-bank/activeContext.md` to set focus: "Current Focus: L4 Implementation - [System Name] - [Phase Name]."
        iii. **Implement Sub-tasks for the Current Phase (from `tasks.md`):**
            *   For each sub-task in the current phase:
                *   Perform coding using `edit_file`, adhering to architectural designs, creative specs, and style guide.
                *   Write unit tests using `edit_file`.
                *   Run tests using `run_terminal_cmd`.
                *   Log actions, code changes, test results in `memory-bank/progress.md` using `edit_file`.
                *   Mark sub-task complete in `memory-bank/tasks.md` using `edit_file`.
        iv. **Phase Verification:**
            *   Once all sub-tasks for the phase are complete, perform verification as per the phase's exit criteria (e.g., specific integration tests, review of foundational components).
            *   Log verification results in `memory-bank/progress.md`.
        v.  If phase verification fails, identify issues, create new sub-tasks in `tasks.md` to address them, and re-iterate implementation/verification for those parts.
        vi. State: "[Phase Name] complete and verified for system [System Name]."
        vii. `edit_file memory-bank/tasks.md` to mark the phase as complete.
4.  **System-Wide Integration & Testing (Typically after Core/Extension phases):**
    a.  Perform broader integration tests across major components.
    b.  Conduct end-to-end system testing against key user scenarios and NFRs.
    c.  Log results in `memory-bank/progress.md`.
5.  **Finalization Phase (Last Phase):**
    a.  Performance tuning, final security reviews, documentation cleanup.
    b.  User Acceptance Testing (UAT) coordination (AI supports by providing info, user executes UAT).
    c.  Preparation for deployment (e.g., final build scripts, deployment notes).
6.  **Final Memory Bank Updates & Completion:**
    a.  Ensure `tasks.md` L4 implementation is marked complete.
    b.  Ensure `progress.md` has a comprehensive log.
    c.  Use `edit_file` to update `memory-bank/activeContext.md`: "Level 4 Phased Implementation for [System Name] complete. Ready for REFLECT mode."
    d.  State: "Level 4 system [System Name] phased implementation complete. All phases and tests passed. Recommend REFLECT mode."
    e.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level4/reflection-comprehensive.mdc",
    "description": "Comprehensive reflection for Level 4 (Complex System) tasks. Guides AI to create an extensive reflection document in `memory-bank/reflection/` using `edit_file`.",
    "globs": "**/Level4/reflection-comprehensive.mdc",
    "alwaysApply": False,
    "body": """
# COMPREHENSIVE REFLECTION FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule structures the comprehensive reflection process for a completed Level 4 (Complex System) task. Use `edit_file` to create an extensive `memory-bank/reflection/reflect-[system_name_or_id]-[date].md` document, analyzing all aspects of the project lifecycle.

This rule is typically fetched by the REFLECT mode orchestrator if the task is L4.

## ⚙️ AI ACTIONS FOR LEVEL 4 COMPREHENSIVE REFLECTION:

1.  **Acknowledge & Extensive Context Gathering:**
    a.  State: "Initiating Comprehensive Reflection for Level 4 system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` (for the entire L4 task history, architectural plans, links to creative docs, phased implementation details).
    c.  `read_file memory-bank/progress.md` (for the full development log, challenges, decisions).
    d.  `read_file` all relevant `memory-bank/architecture/`, `memory-bank/creative/` documents.
    e.  `read_file memory-bank/projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`.
    f.  `read_file memory-bank/activeContext.md` to confirm implementation is marked complete.
2.  **Prepare Reflection Content (Based on Detailed Template Below):**
    a.  Synthesize information from all gathered documents. Analyze each phase of the L4 workflow (VAN, Plan (Arch), Creative, Phased Implement).
3.  **Create Reflection File:**
    a.  Determine reflection filename: `reflect-[system_name_or_id]-[date].md`.
    b.  Use `edit_file` to create/update `memory-bank/reflection/[reflection_filename.md]` with the structured content.
        **L4 Comprehensive Reflection Structure (Content for `edit_file`):**
        ```markdown
        # System Reflection: [System Name from tasks.md]

        ## System ID: [System ID from tasks.md]
        ## Date of Reflection: [Current Date]
        ## Complexity Level: 4

        ## 1. System Overview & Final State
        - **Original Purpose & Scope:** [From `projectbrief.md` / initial `tasks.md`]
        - **Achieved Functionality:** [Describe the final state of the system and its key features.]
        - **Alignment with Business Objectives:** [How well did the final system meet the business goals?]

        ## 2. Project Performance Analysis
        - **Timeline Performance:**
          - Planned vs. Actual Duration (Overall and per phase): [Details]
          - Reasons for major variances: [Analysis]
        - **Resource Utilization (if tracked):** [Planned vs. Actual]
        - **Quality Metrics (if defined):** [How did the project fare against quality targets? E.g., bug density, test coverage achieved.]
        - **Risk Management Effectiveness:** [Were identified risks managed well? Any unforeseen major risks?]

        ## 3. Architectural Planning & Design Phase Review
        - **Effectiveness of Architectural Plan:** [Review `Level4/architectural-planning.mdc` outputs. Were decisions sound? Did the architecture scale/perform as expected?]
        - **Creative Phase Outcomes:** [Review key `creative-*.md` documents. How well did designs translate to implementation? Any design flaws discovered late?]
        - **Adherence to Architectural Principles & Patterns:** [From `systemPatterns.md` and arch plan.]

        ## 4. Phased Implementation Review (`Level4/phased-implementation.mdc`)
        - **Foundation Phase:** [Successes, challenges]
        - **Core Phase:** [Successes, challenges]
        - **Extension Phase(s):** [Successes, challenges]
        - **Integration Phase:** [Successes, challenges, integration issues]
        - **Finalization Phase:** [Successes, challenges]
        - **Overall Implementation Challenges & Solutions:** [Major hurdles and how they were overcome.]

        ## 5. Testing & Quality Assurance Review
        - **Effectiveness of Testing Strategy:** [Unit, integration, system, UAT. Were tests comprehensive? Did they catch critical issues?]
        - **Test Automation:** [Successes, challenges with test automation.]
        - **Post-Release Defect Rate (if applicable/known):**

        ## 6. Achievements and Successes (Overall Project)
        [List 3-5 significant achievements or successes beyond just feature completion.]
        - Achievement 1: [e.g., Successful integration of a complex new technology.]
        - Achievement 2: [e.g., High team collaboration leading to rapid problem-solving.]

        ## 7. Major Challenges & How They Were Addressed (Overall Project)
        [List 3-5 major challenges encountered throughout the project and their resolutions.]
        - Challenge 1: [e.g., Unexpected performance bottlenecks in Service X.]
          - Resolution: [e.g., Re-architected data flow and implemented caching.]

        ## 8. Key Lessons Learned
        ### 8.1. Technical Lessons
        [Deep technical insights, e.g., "Using GraphQL for this specific data aggregation pattern proved highly effective because..."]
        ### 8.2. Architectural Lessons
        [e.g., "The decision to use event sourcing for X module added complexity but significantly improved auditability..."]
        ### 8.3. Process & Workflow Lessons (CMB Usage)
        [e.g., "The phased implementation approach for L4 was crucial for managing complexity. More detailed upfront planning for inter-service contracts would have been beneficial."]
        ### 8.4. Team & Collaboration Lessons
        [e.g., "Regular cross-functional syncs for API design were vital."]

        ## 9. Strategic Actions & Recommendations
        ### 9.1. For This System (Maintenance, Future Enhancements)
        [e.g., "Recommend refactoring Module Y for better testability in Q3."]
        ### 9.2. For Future L4 Projects (Process, Tools, Architecture)
        [e.g., "Adopt a more formal ADR process for all L4 architectural decisions."]
        [e.g., "Invest in better performance testing tools earlier in the lifecycle."]

        ## 10. Knowledge Transfer Summary
        - Key areas of knowledge to transfer: [e.g., Service Z's deployment intricacies, Data model for Module A.]
        - Suggested methods for transfer: [e.g., Update `documentation/`, conduct team workshops.]

        ## 11. Final Assessment
        [Overall summary of the project's execution, outcomes, and strategic value.]
        ```
4.  **Update Core Memory Bank Files (using `edit_file`):**
    a.  **`tasks.md`:**
        *   Mark the Level 4 system's REFLECT phase as "COMPLETE".
        *   Add a link to the reflection document: `Reflection: ../reflection/[reflection_filename.md]`.
    b.  **`activeContext.md`:**
        *   Update current focus: "Comprehensive reflection complete for L4 system [System Name]. Ready for ARCHIVE."
        *   Add to log: "Completed comprehensive reflection for L4 system [System Name]. Document at `reflection/[reflection_filename.md]`."
5.  **Completion:**
    a.  State: "Comprehensive reflection for Level 4 system [System Name] complete. Reflection document created at `memory-bank/reflection/[reflection_filename.md]`."
    b.  (Control returns to the fetching rule).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level4/task-tracking-advanced.mdc",
    "description": "Advanced task tracking for Level 4 (Complex System) tasks. Guides AI to structure `tasks.md` with detailed hierarchy, dependencies, milestones, risks, and progress visualization using `edit_file`.",
    "globs": "**/Level4/task-tracking-advanced.mdc",
    "alwaysApply": False,
    "body": """
# ADVANCED TASK TRACKING FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule outlines a comprehensive task tracking approach for Level 4 (Complex System) tasks. Use `edit_file` to structure `memory-bank/tasks.md` with a detailed hierarchy (System > Component > Feature > Task > Subtask), explicit dependencies, milestones, risk register, resource allocation, and progress visualizations (textual descriptions).

This rule is typically fetched by the PLAN mode orchestrator (`Level4/workflow-level4.mdc` will fetch this as part of architectural planning).

## ⚙️ AI ACTIONS FOR LEVEL 4 ADVANCED TASK TRACKING (Structuring `tasks.md`):

1.  **Acknowledge & Context:**
    a.  State: "Applying Advanced Task Tracking for Level 4 system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` (to establish or update the L4 system entry).
    c.  This rule works in conjunction with `Level4/architectural-planning.mdc`. The architectural plan will define many of the components and features.
2.  **Establish/Update L4 System Entry in `tasks.md` (using `edit_file`):**
    a.  Ensure the main entry for the L4 system in `memory-bank/tasks.md` is structured to accommodate advanced tracking details.

        **Comprehensive L4 Task Structure (Main Sections in `tasks.md` for the L4 System):**
        ```markdown
        # System: [System-ID: System Name, e.g., L4-001: Enterprise Resource Planning System]

        - **Overall Status:** [e.g., IN_PROGRESS_PLANNING, PENDING_ARCH_REVIEW, IN_PROGRESS_IMPLEMENT_FOUNDATION_PHASE, etc.]
        - **Complexity Level:** 4
        - **Lead Architect/Team (if known):** [User may specify]
        - **Target Go-Live Date (Optional):** [User may specify]
        - **Links:**
            - Project Brief: `../projectbrief.md`
            - Architectural Plan: `../architecture/system-[System_Name]-arch-plan-[date].md` (or relevant section in this tasks.md)
            - Comprehensive Reflection: (Link when created)
            - Comprehensive Archive: (Link when created)

        ## 1. System Overview & Goals
        [Brief summary from architectural plan or project brief.]

        ## 2. Key Milestones
        [List major project milestones with target dates and status. Update as project progresses.]
        - [ ] MILE-01: Architectural Plan Approved - Target: [YYYY-MM-DD] - Status: [PENDING/COMPLETE]
        - [ ] MILE-02: Foundation Phase Complete - Target: [YYYY-MM-DD] - Status: [PENDING/COMPLETE]
        - [ ] MILE-03: Core Services Implemented & Tested - Target: [YYYY-MM-DD] - Status: [PENDING/COMPLETE]
        - ...
        - [ ] MILE-XX: System Go-Live - Target: [YYYY-MM-DD] - Status: [PENDING/COMPLETE]

        ## 3. Work Breakdown Structure (WBS) - Components & Features
        [This section will detail Components, their Features, and then Tasks/Sub-tasks. Update iteratively as planning and implementation proceed.]

        ### 3.1. Component: [COMP-ID-A: Component A Name, e.g., User Management Service]
        - **Purpose:** [Brief description]
        - **Status:** [PLANNING/IN_PROGRESS/COMPLETED]
        - **Lead (if applicable):**
        - **Dependencies (other components):** [e.g., COMP-ID-B: Authentication Service]

        #### 3.1.1. Feature: [FEAT-ID-A1: Feature A1 Name, e.g., User Registration]
        - **Description:** [Detailed description]
        - **Status:** [PLANNING/PENDING_CREATIVE/IN_PROGRESS_IMPL/COMPLETED]
        - **Priority:** [Critical/High/Medium/Low]
        - **Quality Criteria:** [Specific acceptance criteria]
        - **Creative Docs (if any):** `../../creative/creative-[Feature_A1_aspect]-[date].md`

        ##### Tasks for Feature A1:
        - [ ] TASK-A1.1: [Detailed task description] - Status: [TODO/WIP/DONE] - Assignee: [AI/User] - Est. Effort: [e.g., 2d]
          - Sub-tasks:
            - [ ] SUB-A1.1.1: [Sub-task description]
            - [ ] SUB-A1.1.2: [Sub-task description]
          - Dependencies: [e.g., TASK-B2.3]
          - Risks: [Brief risk note]
        - [ ] TASK-A1.2: [...]

        #### 3.1.2. Feature: [FEAT-ID-A2: Feature A2 Name, e.g., Profile Update]
        [...]

        ### 3.2. Component: [COMP-ID-B: Component B Name, e.g., Authentication Service]
        [...]

        ## 4. System-Wide Tasks (Cross-Cutting Concerns)
        [Tasks that span multiple components, e.g., setting up CI/CD, defining logging standards.]
        - [ ] SYS-TASK-01: Establish CI/CD Pipeline - Status: [...]
        - [ ] SYS-TASK-02: Define System-Wide Logging Strategy - Status: [...]

        ## 5. Dependency Matrix (High-Level Inter-Component/Inter-Feature)
        [Summarize critical dependencies. Detailed task dependencies are within WBS.]
        - Feature A1 (COMP-A) depends on Core Auth API (COMP-B).
        - Component C integration requires completion of Feature B2 (COMP-B).

        ## 6. Risk Register
        [Track major system-level risks. Task-specific risks can be in WBS.]
        | ID      | Risk Description                     | Probability | Impact | Mitigation Strategy                      | Status    |
        |---------|--------------------------------------|-------------|--------|------------------------------------------|-----------|
        | RISK-01 | Scalability of notification service  | Medium      | High   | Load testing, optimize message queue     | OPEN      |
        | RISK-02 | Integration with legacy System X     | High        | Medium | Develop anti-corruption layer, mock tests | MITIGATED |

        ## 7. Resource Allocation Overview (Optional - User Managed)
        [High-level notes on team allocation if provided by user.]

        ## 8. Progress Visualization (Textual - AI describes, user might visualize)
        - **Overall System Progress (Conceptual):** [e.g., "Estimated 20% complete based on milestone tracking."]
        - **Component Progress (Conceptual):**
          - User Management Service: [e.g., "Foundation built, registration feature in progress."]
          - Authentication Service: [e.g., "Core APIs complete, awaiting integration."]

        ## 9. Latest Updates & Decisions Log
        [Chronological log of major updates, decisions, or changes to the plan. More detailed logs go in `progress.md`.]
        - [Date]: Architectural decision ADR-003 (Data Storage) finalized.
        - [Date]: Milestone MILE-01 (Arch Plan Approved) completed.
        ```
3.  **Iterative Updates:**
    a.  This `tasks.md` structure for L4 is a living document. As the project progresses through architectural planning, creative phases, and phased implementation, use `edit_file` to:
        *   Add/refine components, features, tasks, and sub-tasks.
        *   Update statuses and progress percentages.
        *   Mark milestones as complete.
        *   Log new risks or update existing ones.
        *   Record key decisions in the "Latest Updates" section.
4.  **Log Update:**
    a.  Use `edit_file` to add a note to `memory-bank/activeContext.md`:
        `[Timestamp] - Advanced task tracking structure for L4 system [System Name] established/updated in tasks.md.`
5.  **Completion (of this rule's execution):**
    a.  State: "Advanced task tracking structure for Level 4 system [System Name] applied to `tasks.md`. This document will be updated throughout the project lifecycle."
    b.  (Control returns to the PLAN mode orchestrator / L4 Workflow orchestrator).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Level4/workflow-level4.mdc",
    "description": "Orchestrates the comprehensive workflow for Level 4 (Complex System) tasks, guiding AI through all 7 CMB modes by fetching specific L4 and Core rules.",
    "globs": "**/Level4/workflow-level4.mdc",
    "alwaysApply": False,
    "body": """
# COMPREHENSIVE WORKFLOW FOR LEVEL 4 TASKS (AI Instructions)

> **TL;DR:** This rule orchestrates the full, comprehensive workflow for Level 4 (Complex System) tasks. It guides the AI through all 7 CMB modes (Initialization, Documentation Setup, Architectural Planning, Creative Phases, Phased Implementation, Reflection, and Archiving) by fetching specific L4 and Core rules.

This workflow is typically fetched after VAN mode has confirmed the task as Level 4.

## 🧭 LEVEL 4 WORKFLOW PHASES (AI Actions)

### Phase 1: INITIALIZATION (Confirmation & Deep Context)
1.  **Acknowledge & Confirm L4:**
    a.  State: "Initiating Level 4 Workflow for system: [System Name from activeContext.md]."
    b.  `read_file memory-bank/tasks.md` and `memory-bank/activeContext.md` to confirm task is Level 4 and gather initial high-level scope.
2.  **Core Setup Verification (Crucial for L4):**
    a.  Ensure platform awareness: `fetch_rules` for `.cursor/rules/isolation_rules/Core/platform-awareness.mdc`.
    b.  Ensure Memory Bank structure: `fetch_rules` for `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
3.  **Task Framework & Enterprise Context:**
    a.  Verify `tasks.md` has a main entry for this L4 system.
    b.  `edit_file memory-bank/activeContext.md` to set focus: "Focus: L4 System - [System Name] - Initializing & Documentation Setup."
    c.  (User might provide initial enterprise context, or AI might need to synthesize from `projectbrief.md`).
4.  **Milestone:** State "L4 Initialization complete. Proceeding to Documentation Setup."

### Phase 2: DOCUMENTATION SETUP (L4 Comprehensive)
1.  **Load Comprehensive Templates (Conceptual):** AI should be aware of the need for detailed documentation.
2.  **Update Core Memory Bank Files:**
    a.  Use `edit_file` to extensively update/populate:
        *   `memory-bank/projectbrief.md` (detailed system description, goals, scope).
        *   `memory-bank/productContext.md` (business drivers, stakeholders, market needs).
        *   `memory-bank/systemPatterns.md` (any known enterprise patterns to adhere to, or placeholder for new patterns).
        *   `memory-bank/techContext.md` (existing tech landscape, constraints, preferred stack).
3.  **Establish Documentation Framework:**
    a.  If not already present, use `run_terminal_cmd` to create `memory-bank/architecture/` and `memory-bank/architecture/adrs/` directories.
4.  **Milestone:** State "L4 Documentation Setup complete. Proceeding to Architectural Planning."

### Phase 3: ARCHITECTURAL PLANNING (PLAN Mode Actions for L4)
1.  **Fetch L4 Planning Rules:**
    a.  State: "Fetching Level 4 architectural planning and advanced task tracking guidelines."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level4/task-tracking-advanced.mdc`. (This sets up the detailed structure in `tasks.md`).
    c.  `fetch_rules` for `.cursor/rules/isolation_rules/Level4/architectural-planning.mdc`.
2.  **Follow Fetched Rules:**
    a.  `task-tracking-advanced.mdc` guides structuring `tasks.md` for L4 complexity.
    b.  `architectural-planning.mdc` guides defining the architecture (requirements, context, vision, principles, alternatives, ADRs, diagrams) within `tasks.md` or linked documents. Use `edit_file` for all documentation.
3.  **Update Context & Recommend Next Mode:**
    a.  `read_file memory-bank/tasks.md` (specifically the architectural plan and WBS) to identify components/features needing CREATIVE design.
    b.  Use `edit_file` to update `memory-bank/activeContext.md`: "Architectural planning complete for L4 system [System Name]. Creative phases for [list key components/features] identified."
    c.  State: "Level 4 Architectural Planning complete. Detailed plan and architecture documented. Recommend CREATIVE mode for designated components." Await user.
4.  **Milestone:** Architectural Planning phase complete. Await user confirmation for CREATIVE mode.

### Phase 4: CREATIVE PHASES (CREATIVE Mode Actions for L4)
1.  **Acknowledge & Fetch Creative Orchestrator:**
    a.  State: "Initiating CREATIVE mode for L4 system [System Name] components as per architectural plan."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/visual-maps/creative-mode-map.mdc`.
2.  **Follow Fetched Rule (`creative-mode-map.mdc`):**
    a.  This orchestrator will guide identifying "CREATIVE: Design..." tasks from the L4 plan in `tasks.md` and fetching specific `Phases/CreativePhase/*.mdc` rules for each.
    b.  Ensure detailed design documents are created in `memory-bank/creative/` using `edit_file`.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Creative design phases complete for L4 system [System Name]. Ready for Phased Implementation."
    b.  State: "Level 4 Creative phases complete. Design documents finalized. Recommend IMPLEMENT mode for phased development."
4.  **Milestone:** Creative phase complete. Await user confirmation for IMPLEMENT mode.

### Phase 5: PHASED IMPLEMENTATION (IMPLEMENT Mode Actions for L4)
1.  **Fetch L4 Implementation Rule:**
    a.  State: "Initiating Phased Implementation for L4 system [System Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level4/phased-implementation.mdc`.
2.  **Follow Fetched Rule (`phased-implementation.mdc`):**
    a.  This rule guides defining implementation phases (Foundation, Core, Extension, Integration, Finalization) in `tasks.md`.
    b.  For each phase, implement sub-tasks using `edit_file` for code, `run_terminal_cmd` for builds/tests.
    c.  Perform rigorous verification at each phase gate.
    d.  Update `tasks.md` and `progress.md` meticulously.
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Phased Implementation complete for L4 system [System Name]. Ready for Comprehensive Reflection."
    b.  State: "Level 4 Phased Implementation complete. System built and tested. Recommend REFLECT mode."
4.  **Milestone:** Phased Implementation complete. Await user confirmation for REFLECT mode.

### Phase 6: COMPREHENSIVE REFLECTION (REFLECT Mode Actions for L4)
1.  **Fetch L4 Reflection Rule:**
    a.  State: "Initiating Comprehensive Reflection for L4 system [System Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level4/reflection-comprehensive.mdc`.
2.  **Follow Fetched Rule (`reflection-comprehensive.mdc`):**
    a.  This rule guides creating an extensive reflection document in `memory-bank/reflection/` using `edit_file`, analyzing all project aspects (performance, architecture, process, lessons, strategic actions).
3.  **Update Context & Recommend:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "Comprehensive Reflection complete for L4 system [System Name]. Ready for Archiving."
    b.  State: "Level 4 Comprehensive Reflection complete. Reflection document created. Recommend ARCHIVE mode."
4.  **Milestone:** Reflection phase complete. Await user confirmation for ARCHIVE mode.

### Phase 7: COMPREHENSIVE ARCHIVING (ARCHIVE Mode Actions for L4)
1.  **Fetch L4 Archiving Rule:**
    a.  State: "Initiating Comprehensive Archiving for L4 system [System Name]."
    b.  `fetch_rules` for `.cursor/rules/isolation_rules/Level4/archive-comprehensive.mdc`.
2.  **Follow Fetched Rule (`archive-comprehensive.mdc`):**
    a.  This rule guides creating a detailed system archive document in `memory-bank/archive/` (or `documentation/`) using `edit_file`, consolidating all project artifacts and knowledge.
    b.  Update `tasks.md` marking the L4 system ARCHIVED.
3.  **Finalize Context:**
    a.  Use `edit_file` to update `memory-bank/activeContext.md`: "L4 System [System Name] comprehensively archived. Memory Bank ready for new top-level task (VAN mode)."
4.  **Milestone:** State "Level 4 System [System Name] fully completed and archived. Recommend VAN mode for new system/project."
"""
},
# --- End of Level 4 Files ---
# --- Main Orchestrator Files ---
{
    "path": ".cursor/rules/isolation_rules/main.mdc",
    "description": "Primary entry point for the Cursor Memory Bank system. Verifies Memory Bank existence and typically initiates VAN mode.",
    "globs": "main.mdc", # This might be a special glob if it's an initial rule.
    "alwaysApply": False, # Should be fetched by a very high-level prompt or system trigger.
    "body": """
# ISOLATION-FOCUSED MEMORY BANK SYSTEM (AI Instructions)

> **TL;DR:** This is the main entry rule. It ensures Memory Bank is set up and then typically transitions to VAN mode to start project analysis.

## ⚙️ AI ACTIONS - SYSTEM STARTUP:

1.  **Acknowledge System Start:**
    a.  State: "Memory Bank System initiated. Performing mandatory Memory Bank verification."
2.  **CRITICAL: Memory Bank Verification & Setup:**
    a.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/Core/file-verification.mdc`.
    b.  This rule will guide you to check if `memory-bank/` and its core subdirectories/files exist. If not, it will instruct you to create them using `run_terminal_cmd` for directories and `edit_file` for initial file content.
    c.  **If `Core/file-verification.mdc` reports critical failure (e.g., cannot create `memory-bank/`):**
        i.  State: "🚨 CRITICAL ERROR: Memory Bank structure could not be verified or created. Cannot proceed with CMB workflow. Please check permissions or manually create the `memory-bank/` directory."
        ii. Await user intervention. Do not proceed.
    d.  **If verification/creation is successful:**
        i.  State: "Memory Bank structure verified/initialized successfully."
3.  **Transition to VAN Mode (Default Initial Mode):**
    a.  State: "Transitioning to VAN mode for initial project analysis and complexity determination."
    b.  `fetch_rules` to load and follow `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-mode-map.mdc`.
    c.  (The `van-mode-map.mdc` will then orchestrate the VAN mode process).

## 🧭 MODE-SPECIFIC VISUAL MAPS (For AI's Conceptual Understanding)
The CMB system uses distinct orchestrator rules for each mode. You will be directed to `fetch_rules` for these as needed:
-   VAN Mode: `visual-maps/van_mode_split/van-mode-map.mdc` (Initial Analysis & Complexity)
-   PLAN Mode: `visual-maps/plan-mode-map.mdc` (Task Planning)
-   CREATIVE Mode: `visual-maps/creative-mode-map.mdc` (Design Decisions)
-   IMPLEMENT Mode: `visual-maps/implement-mode-map.mdc` (Code Implementation)
-   REFLECT Mode: `visual-maps/reflect-mode-map.mdc` (Task Review)
-   ARCHIVE Mode: `visual-maps/archive-mode-map.mdc` (Documentation & Closure)

## 💻 PLATFORM-SPECIFIC COMMANDS & EFFICIENCY (General Reminder)
*   Always be mindful of platform differences when using `run_terminal_cmd`. Refer to `Core/platform-awareness.mdc` principles.
*   Strive for command efficiency. Refer to `Core/command-execution.mdc` principles.
"""
},
{
    "path": ".cursor/rules/isolation_rules/main-optimized.mdc",
    "description": "Describes the design principles of the Optimized Memory Bank system, focusing on token efficiency, adaptive complexity, and hierarchical rule loading. For AI's conceptual understanding.",
    "globs": "main-optimized.mdc",
    "alwaysApply": False, # This is a design document, not typically fetched for direct execution.
    "body": """
# OPTIMIZED MEMORY BANK SYSTEM (Design Principles - AI Understanding)

> **TL;DR:** This document explains the design principles behind the Memory Bank's optimizations. You, the AI, enact these optimizations by following the specific instructions in other `.mdc` rules that guide hierarchical rule loading, adaptive complexity, progressive documentation, and efficient Memory Bank updates.

## 🚨 CRITICAL PREMISE: MEMORY BANK EXISTENCE
*   The entire CMB system, optimized or not, relies on the `memory-bank/` directory and its core files being present. This is typically ensured by the `main.mdc` rule fetching `Core/file-verification.mdc` at startup.

## 🧭 OPTIMIZED MODE ARCHITECTURE (Conceptual Overview)
The system uses:
*   **Context Manager (Conceptual):** Achieved by your diligent use of `read_file` for relevant context from `activeContext.md`, `tasks.md`, etc., and `edit_file` to update them.
*   **Rule Loader (Conceptual):** This is the `fetch_rules` tool, which you use as instructed by prompts or other `.mdc` files.
*   **File Manager (Conceptual):** This is primarily the `edit_file` tool for content, and `run_terminal_cmd` for directory operations.
*   **Mode Transition (Conceptual):** Managed by updating `activeContext.md` before switching modes, as guided by `Core/mode-transition-optimization.mdc` principles.

## 📈 ADAPTIVE COMPLEXITY MODEL (How You Implement This)
*   You determine task complexity (Level 1-4) by following `Core/complexity-decision-tree.mdc` (usually fetched in VAN mode).
*   Based on the determined level, the workflow orchestrators (e.g., `LevelX/workflow-levelX.mdc` or main mode maps) will guide you through a process tailored to that complexity, fetching appropriate level-specific rules.
    *   L1: Streamlined (e.g., VAN → IMPLEMENT → Minimal REFLECT/ARCHIVE).
    *   L2: Balanced (e.g., VAN → PLAN → IMPLEMENT → REFLECT).
    *   L3: Comprehensive (e.g., VAN → PLAN → CREATIVE → IMPLEMENT → REFLECT).
    *   L4: Full Governance (e.g., VAN → PLAN (Arch) → CREATIVE → Phased IMPLEMENT → REFLECT → ARCHIVE).

## 🧠 HIERARCHICAL RULE LOADING (How You Implement This)
*   You achieve this by starting with a high-level orchestrator rule (e.g., `visual-maps/van_mode_split/van-mode-map.mdc`) fetched via your main custom prompt.
*   This orchestrator then instructs you to `fetch_rules` for more specific sub-rules (from `Core/`, `LevelX/`, `Phases/`, or other `visual-maps/`) only when they are needed for the current step or context.
*   This keeps your active instruction set focused and token-efficient.

## 🔄 TOKEN-OPTIMIZED CREATIVE PHASE (How You Implement This)
*   When in CREATIVE mode, and guided by rules like `Phases/CreativePhase/creative-phase-architecture.mdc` or `Phases/CreativePhase/creative-phase-uiux.mdc`, you will be instructed to use the structure from `Phases/CreativePhase/optimized-creative-template.mdc`.
*   This template encourages progressive documentation: define the problem, list options briefly, then provide detailed analysis *for selected options* or as requested, rather than exhaustively for all.

## 🔀 OPTIMIZED MODE TRANSITIONS (How You Implement This)
*   Before transitioning from one mode to another, the current mode's orchestrator will instruct you to use `edit_file` to update `memory-bank/activeContext.md` with a summary of outputs and focus for the next mode.
*   The next mode's orchestrator will then instruct you to `read_file memory-bank/activeContext.md` to pick up this context. (See `Core/mode-transition-optimization.mdc`).

## 📊 MEMORY BANK EFFICIENT UPDATES (How You Implement This)
*   When using `edit_file` to update Memory Bank files (`tasks.md`, `activeContext.md`, etc.):
    *   Be precise. Modify only the relevant sections.
    *   If appending, add to the correct section.
    *   This avoids rewriting entire large files for small changes.

## 💻 COMPLEXITY-BASED DOCUMENTATION (How You Implement This)
*   The `LevelX/*.mdc` rules for planning, reflection, and archiving will guide the *depth* of documentation required.
    *   Level 1: Minimal documentation, often consolidated.
    *   Level 4: Extensive, comprehensive documentation.
*   Follow the specific documentation structure and content requirements outlined in the active Level-specific rule.

## 💡 USAGE GUIDANCE (Summary for AI)
1.  The CMB workflow typically starts with VAN mode, triggered by `main.mdc`.
2.  Follow the instructions from the currently fetched `.mdc` rule.
3.  Use `fetch_rules` only when explicitly instructed, to load more specific rules.
4.  Use `edit_file` for all content creation/modification in Memory Bank files.
5.  Adhere to the principles of platform awareness and command execution from Core rules.
By following these specific, contextual instructions, you inherently enact the system's optimizations.
"""
},
# --- Creative Phase Files ---
{
    "path": ".cursor/rules/isolation_rules/Phases/CreativePhase/optimized-creative-template.mdc",
    "description": "Optimized template for documenting creative phase outputs (design, architecture, UI/UX decisions). Provides a structure for `edit_file` operations.",
    "globs": "**/Phases/CreativePhase/optimized-creative-template.mdc",
    "alwaysApply": False, # This is a template, referenced by other rules.
    "body": """
# OPTIMIZED CREATIVE PHASE TEMPLATE (Structure for `creative-*.md` files)

> **TL;DR:** This rule provides a structured template for documenting outputs of a creative phase (e.g., architecture, UI/UX, algorithm design). Use this structure when `edit_file` is used to create or update a `memory-bank/creative/creative-[aspect_name]-[date].md` document.

## 📝 PROGRESSIVE DOCUMENTATION MODEL (Principle for AI)
*   Start with concise summaries for problem and options.
*   Provide detailed analysis primarily for the selected option(s) or when comparing top contenders.
*   This keeps the document focused and token-efficient initially, allowing for expansion if needed.

## 📋 TEMPLATE STRUCTURE (Guide for `edit_file` content)

```markdown
📌 CREATIVE PHASE START: [Specific Aspect Being Designed, e.g., User Authentication Module Architecture]
Date: [Current Date]
Related Task ID (from tasks.md): [Task ID]
Designer: AI

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### 1️⃣ PROBLEM DEFINITION
- **Description:** [Clear and concise description of the specific problem this design phase addresses. What needs to be designed or decided?]
- **Key Requirements (Functional & Non-Functional):**
  - [ ] Requirement 1: [e.g., System must support JWT-based authentication.]
  - [ ] Requirement 2: [e.g., Token validation must occur within 50ms.]
  - [ ] Requirement 3: [e.g., Design must allow for future integration with OAuth providers.]
- **Constraints:** [Any technical, business, or resource constraints impacting design choices. e.g., Must use existing PostgreSQL database for user store.]

### 2️⃣ OPTIONS EXPLORED
[List 2-3 viable options considered. Provide a brief one-line description for each.]
- **Option A:** [Name of Option A, e.g., Monolithic Auth Service] - [One-line description]
- **Option B:** [Name of Option B, e.g., Microservice for Auth with API Gateway] - [One-line description]
- **Option C:** [Name of Option C, e.g., Leverage Third-Party Auth Provider (Auth0/Okta)] - [One-line description]

### 3️⃣ ANALYSIS OF OPTIONS
[Provide a comparative analysis. A table is good for summaries. Detailed pros/cons for each option can follow, especially for top contenders or the chosen one.]

**Summary Comparison Table:**
| Criterion         | Option A: [Name] | Option B: [Name] | Option C: [Name] |
|-------------------|------------------|------------------|------------------|
| Scalability       | [e.g., Medium]   | [e.g., High]     | [e.g., High]     |
| Complexity        | [e.g., Low]      | [e.g., Medium]   | [e.g., Low-Med]  |
| Development Effort| [e.g., Low]      | [e.g., High]     | [e.g., Medium]   |
| Maintainability   | [e.g., Medium]   | [e.g., Medium]   | [e.g., High (external)] |
| Cost (Operational)| [e.g., Low]      | [e.g., Medium]   | [e.g., Potentially High] |
| Security (Control)| [e.g., High]     | [e.g., High]     | [e.g., Medium (dependency)] |
| Alignment w/ Reqs | [e.g., Good]     | [e.g., Excellent]| [e.g., Good, some gaps] |

**Detailed Analysis (Focus on top 1-2 options or as requested):**

<details>
  <summary>Detailed Analysis: Option B: Microservice for Auth</summary>

  **Description:**
  [Detailed description of how Option B works, key components involved, data flows, etc.]

  **Pros:**
  - Pro 1: [e.g., Independent scalability of auth service.]
  - Pro 2: [e.g., Clear separation of concerns, improving maintainability of other services.]

  **Cons:**
  - Con 1: [e.g., Increased operational complexity due to distributed system.]
  - Con 2: [e.g., Potential for network latency between services.]

  **Implementation Complexity:** [Low/Medium/High]
  [Explanation of complexity factors specific to this option.]

  **Resource Requirements:**
  [Details on specific resource needs: e.g., separate database, more compute instances.]

  **Risk Assessment:**
  [Analysis of risks specific to this option: e.g., inter-service communication failures.]
</details>

*(Repeat `<details>` block for other significantly considered options if necessary)*

### 4️⃣ DECISION & RATIONALE
- **Selected Option:** [Clearly state the chosen option, e.g., Option B: Microservice for Auth with API Gateway]
- **Rationale:** [Provide a detailed justification for why this option was selected over others. Refer to the analysis, requirements, and constraints. e.g., "Option B was chosen despite higher initial complexity due to its superior scalability and alignment with our long-term microservices strategy. It best meets NFR for scalability and maintainability..."]

### 5️⃣ IMPLEMENTATION GUIDELINES (for the selected option)
[Provide high-level guidelines, key considerations, or next steps for implementing the chosen design. This is not the full implementation plan but pointers for the IMPLEMENT phase.]
- [Guideline 1: e.g., Define clear API contracts for the new auth service using OpenAPI spec.]
- [Guideline 2: e.g., Implement robust error handling and retry mechanisms for inter-service calls.]
- [Guideline 3: e.g., Ensure comprehensive logging and monitoring for the auth service.]
- [Guideline 4: e.g., Key technologies to use: Spring Boot for service, JWT for tokens, PostgreSQL for user data.]
- [Guideline 5: e.g., First implementation phase should focus on core token generation and validation.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 CREATIVE PHASE END: [Specific Aspect Being Designed]
Outcome: Design decision made and documented. Ready for implementation planning or further creative phases if needed.
```

## ✅ VERIFICATION CHECKLIST (AI Self-Guide when using this template)
Before finalizing a `creative-*.md` document using `edit_file`:
- [ ] Problem clearly defined?
- [ ] Multiple (2-3) viable options considered and listed?
- [ ] Analysis (summary table and/or detailed pros/cons) provided?
- [ ] Decision clearly stated with strong rationale?
- [ ] Implementation guidelines for the chosen decision included?
- [ ] Document saved to `memory-bank/creative/creative-[aspect_name]-[date].md`?
- [ ] `tasks.md` updated to mark this creative sub-task complete and link to this document?
"""
},
{
    "path": ".cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-architecture.mdc",
    "description": "Guides the AI through the architectural design process within a CREATIVE phase. Instructs on using `edit_file` to document architectural decisions in a `creative-architecture-*.md` file, referencing the `optimized-creative-template.mdc`.",
    "globs": "**/Phases/CreativePhase/creative-phase-architecture.mdc",
    "alwaysApply": False, # Fetched by creative-mode-map.mdc
    "body": """
# CREATIVE PHASE: ARCHITECTURE DESIGN (AI Instructions)

> **TL;DR:** This rule guides you through designing and documenting architectural solutions for a specific component or system aspect. Use `edit_file` to create/update a `memory-bank/creative/creative-architecture-[component_name]-[date].md` document, structured using the `optimized-creative-template.mdc`.

This rule is typically fetched by `visual-maps/creative-mode-map.mdc` when an architectural design task is active.

## ⚙️ AI ACTIONS FOR ARCHITECTURE DESIGN:

1.  **Acknowledge & Context:**
    a.  State: "Initiating CREATIVE phase for Architecture Design: [Component/System Aspect from tasks.md]."
    b.  `read_file memory-bank/tasks.md` for specific requirements, constraints, and scope for this architectural design task.
    c.  `read_file memory-bank/activeContext.md` for overall project context.
    d.  `read_file memory-bank/systemPatterns.md` and `techContext.md` for existing architectural patterns and technology landscape.
    e.  `read_file .cursor/rules/isolation_rules/Phases/CreativePhase/optimized-creative-template.mdc` to understand the documentation structure.
2.  **Define Problem & Requirements (Section 1 of `optimized-creative-template.mdc`):**
    a.  Clearly state the architectural problem being solved (e.g., "Design a scalable backend for real-time notifications").
    b.  List key functional requirements (e.g., "Must handle 1000 concurrent users," "Deliver notifications within 500ms").
    c.  List key non-functional requirements (quality attributes) like scalability, performance, security, maintainability, cost.
    d.  Identify architectural constraints (e.g., "Must use AWS services," "Integrate with existing user database").
3.  **Explore Architectural Options (Section 2 & 3 of `optimized-creative-template.mdc`):**
    a.  Brainstorm 2-3 distinct architectural patterns or high-level design options (e.g., Microservices vs. Monolith, Event-driven vs. Request-response, SQL vs. NoSQL for a specific data store).
    b.  For each option, briefly describe it.
    c.  Analyze each option against the requirements and constraints. Consider:
        *   Pros & Cons.
        *   Impact on scalability, performance, security, maintainability, cost.
        *   Complexity of implementation.
        *   Team familiarity with technologies.
    d.  Use a summary table for quick comparison if helpful.
4.  **Make Decision & Justify (Section 4 of `optimized-creative-template.mdc`):**
    a.  Select the most suitable architectural option.
    b.  Provide a clear and detailed rationale for the decision, explaining why it's preferred over alternatives, referencing the analysis.
5.  **Outline Implementation Guidelines (Section 5 of `optimized-creative-template.mdc`):**
    a.  Describe key components of the chosen architecture.
    b.  Suggest primary technologies, frameworks, or libraries.
    c.  Outline high-level interaction patterns between components (textually describe data flows or sequence diagrams if complex).
    d.  Identify major interfaces or APIs to be defined.
    e.  Note any critical next steps for detailed design or implementation planning.
6.  **Document in `creative-architecture-*.md`:**
    a.  Determine filename: `creative-architecture-[component_name_or_aspect]-[date].md`.
    b.  Use `edit_file` to create/update `memory-bank/creative/[filename]` with all the above information, structured according to the `optimized-creative-template.mdc`.
7.  **Update Core Memory Bank Files:**
    a.  Use `edit_file` to update `memory-bank/tasks.md`:
        *   Mark the specific "CREATIVE: Architect [component/aspect]" sub-task as complete.
        *   Add a link to the created `creative-architecture-*.md` document.
    b.  Use `edit_file` to add a summary of the architectural decision to the "Creative Decisions Log" in `memory-bank/activeContext.md`.
8.  **Completion:**
    a.  State: "Architecture design for [Component/Aspect] complete. Documented in `memory-bank/creative/[filename]`."
    b.  (Control returns to `visual-maps/creative-mode-map.mdc` to check for more creative tasks or recommend next mode).
"""
},
{
    "path": ".cursor/rules/isolation_rules/Phases/CreativePhase/creative-phase-uiux.mdc",
    "description": "Guides AI through UI/UX design within a CREATIVE phase. Emphasizes style guide adherence, user-centricity, and documenting decisions in `creative-uiux-*.md` using `edit_file` and `optimized-creative-template.mdc`.",
    "globs": "**/Phases/CreativePhase/creative-phase-uiux.mdc",
    "alwaysApply": False, # Fetched by creative-mode-map.mdc
    "body": """
# CREATIVE PHASE: UI/UX DESIGN GUIDELINES (AI Instructions)

> **TL;DR:** This rule guides you through designing and documenting UI/UX solutions. CRITICAL: Check for and adhere to `memory-bank/style-guide.md`. If missing, prompt user to create/link it. Document decisions in `memory-bank/creative/creative-uiux-[component_name]-[date].md` using `edit_file` and the `optimized-creative-template.mdc` structure.

This rule is typically fetched by `visual-maps/creative-mode-map.mdc` when a UI/UX design task is active.

## ⚙️ AI ACTIONS FOR UI/UX DESIGN:

1.  **Acknowledge & Context:**
    a.  State: "Initiating CREATIVE phase for UI/UX Design: [Component/Feature from tasks.md]."
    b.  `read_file memory-bank/tasks.md` for specific UI/UX requirements, user stories, and scope.
    c.  `read_file memory-bank/activeContext.md` for overall project context.
    d.  `read_file .cursor/rules/isolation_rules/Phases/CreativePhase/optimized-creative-template.mdc` to understand the documentation structure.
2.  **Style Guide Integration (CRITICAL):**
    a.  **Check Primary Location:** `read_file memory-bank/style-guide.md`.
    b.  **If Found:** State "Style guide `memory-bank/style-guide.md` loaded. All UI/UX proposals will adhere to it." Proceed to step 3.
    c.  **If NOT Found at Primary Location:**
        i.  Prompt User: "Style guide `memory-bank/style-guide.md` not found. Is there an existing style guide at a different path or URL? If so, please provide it. Otherwise, I can help create a basic one now, or we can proceed without (not recommended for new UI)." Await user response.
        ii. **If User Provides Path/URL:** Attempt to `read_file [user_provided_path]` or conceptually access URL. If successful, state "Style guide loaded from [source]. All UI/UX proposals will adhere to it." Proceed to step 3. If fails, revert to "Style guide not available."
        iii. **If User Opts to Create:**
            1.  State: "Okay, let's define a basic style guide in `memory-bank/style-guide.md`. Please provide preferences for: Core Color Palette (primary, secondary, accent, neutrals, status colors - hex codes if possible), Typography (font families, sizes, weights for headings/body), Spacing System (base unit, Tailwind scale usage if known), Key Component Styles (buttons, inputs - general look/feel or Tailwind examples)."
            2.  Based on user input (or analysis of provided examples like screenshots if user offers them), generate content for `memory-bank/style-guide.md`. (Example structure: Headings for Colors, Typography, Spacing, Components; list defined styles under each).
            3.  Use `edit_file` to create and save this content to `memory-bank/style-guide.md`.
            4.  State: "Basic style guide created at `memory-bank/style-guide.md`. All UI/UX proposals will adhere to it." Proceed to step 3.
        iv. **If User Opts to Proceed Without:** State: "Proceeding with UI/UX design without a style guide. WARNING: This may lead to inconsistencies. I will aim for internal consistency within this component." Proceed to step 3.
3.  **Define Problem & UI/UX Requirements (Section 1 of `optimized-creative-template.mdc`):**
    a.  Clearly state the UI/UX problem (e.g., "Design an intuitive interface for user registration").
    b.  List key user stories/goals for this UI (e.g., "As a new user, I want to register quickly with minimal fields").
    c.  List functional requirements for the UI (e.g., "Must include fields for email, password, confirm password").
    d.  List relevant NFRs (e.g., "Must be responsive," "Adhere to WCAG AA accessibility").
    e.  Note any constraints (e.g., "Must use existing React component library X if possible").
4.  **Explore UI/UX Options (Section 2 & 3 of `optimized-creative-template.mdc`):**
    a.  Propose 2-3 distinct UI/UX solutions. For each, describe:
        *   Layout and structure (Information Architecture).
        *   Key interaction patterns (User Flows).
        *   Visual design approach (referencing `style-guide.md` elements like colors, fonts, spacing, component styles. If no style guide, describe choices made for consistency).
        *   How it addresses user needs and requirements.
    b.  Analyze options considering usability, A11y, feasibility (React/Tailwind), aesthetics, and **strict adherence to `style-guide.md` if available.**
5.  **Make Decision & Justify (Section 4 of `optimized-creative-template.mdc`):**
    a.  Select the most suitable UI/UX solution.
    b.  Provide clear rationale, referencing the style guide and how the chosen design meets user needs and requirements effectively.
6.  **Outline Implementation Guidelines (Section 5 of `optimized-creative-template.mdc`):**
    a.  Describe key React components to be built/used.
    b.  Suggest specific Tailwind CSS utility classes or custom CSS (if extending Tailwind per style guide) for styling key elements.
    c.  Note important states (hover, focus, disabled, error) and how they should appear (per style guide).
    d.  Mention responsive design considerations (breakpoints, mobile-first approach if applicable, per style guide).
7.  **Document in `creative-uiux-*.md`:**
    a.  Determine filename: `creative-uiux-[component_name_or_feature]-[date].md`.
    b.  Use `edit_file` to create/update `memory-bank/creative/[filename]` with all the above, structured per `optimized-creative-template.mdc`.
8.  **Update Core Memory Bank Files:**
    a.  Use `edit_file` to update `memory-bank/tasks.md`:
        *   Mark "CREATIVE: Design UI/UX for [component/feature]" sub-task as complete.
        *   Link to the created `creative-uiux-*.md` document.
    b.  Use `edit_file` to add a summary of the UI/UX decision to "Creative Decisions Log" in `memory-bank/activeContext.md`.
9.  **Completion:**
    a.  State: "UI/UX design for [Component/Feature] complete. Documented in `memory-bank/creative/[filename]`. Adherence to style guide `memory-bank/style-guide.md` [was maintained / was attempted due to no guide existing]."
    b.  (Control returns to `visual-maps/creative-mode-map.mdc`).
"""
}
# --- End of Creative Phase Files ---
    ])

    if not MDC_FILES_DATA:
        print("No file data provided. Please populate the MDC_FILES_DATA list.")
    else:
        # Ensure the base path for rules exists, relative to where the script is run
        # This assumes the script is run from the project root.
        project_root = os.getcwd() 
        base_rules_path_abs = os.path.join(project_root, ".cursor", "rules", "isolation_rules")

        if not os.path.exists(base_rules_path_abs):
            # This case should ideally not happen if Core rules were already made,
            # but it's a safeguard if only visual-maps are being generated by a modified script.
            print(f"Base directory {base_rules_path_abs} does not exist. Please ensure Core rules are generated first or the path is correct.")
            # os.makedirs(base_rules_path_abs, exist_ok=True) # Optionally create it

        for file_data in MDC_FILES_DATA:
            # Construct absolute path for file operations
            absolute_filepath = os.path.join(project_root, file_data["path"])
            
            create_or_update_mdc_file(
                absolute_filepath, # Use absolute path for writing
                file_data["description"],
                file_data["globs"], # Globs are relative to .cursor/rules/ for Cursor's matching
                file_data["alwaysApply"],
                file_data["body"]
            )
        print("\n--- MDC file generation process complete. ---")
        print(f"NOTE: This script overwrites existing files with the defined content in their respective paths, relative to project root: {project_root}")
        print("Ensure that the 'globs' in the .mdc files are correctly specified for Cursor's rule matching (usually relative to the .cursor/rules/ directory).")