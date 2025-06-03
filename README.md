# Enhanced Cursor Memory Bank System

A personal, token-optimized, and highly structured task management system for the Cursor AI IDE, designed to enhance AI agent autonomy and maintain persistent project context across development phases.

---

> **Maintainer's Note**:
>
> I am now the active maintainer of this Cursor Memory Bank system, continuing its evolution as a personal hobby project. My goal is to refine its capabilities based on real-world development workflows within Cursor, ensuring maximum efficiency, clarity, and adaptability for AI-assisted coding.
>
> While this remains a personal project without a formal issues tracker, its design emphasizes AI-driven adaptability. This means you can directly interact with the Cursor AI to modify or update the system's rules (`.mdc` files) to perfectly suit your specific needs. I regularly update the system based on my own development experiences and insights gained from using it.

## About the Enhanced Memory Bank

This system provides a structured, phase-driven approach to software development, leveraging Cursor's custom modes to create a highly efficient and disciplined workflow. It addresses the inherent context limitations of large language models (LLMs) by maintaining persistent, organized project memory and optimizing token usage.

### Key Architectural Principles

The Enhanced Memory Bank builds upon a modular, hierarchical architecture with significant optimizations:

*   **Hierarchical Rule Loading (Just-In-Time):** Only essential rules are loaded initially, with specialized rules lazy-loaded precisely when needed. This dramatically reduces token consumption and maximizes the AI's active context window.
*   **Adaptive Complexity Model:** Workflows and documentation depth automatically scale based on task complexity (Levels 1-4), ensuring appropriate rigor without unnecessary overhead.
*   **Mode-Specific Orchestration:** Each development phase (mode) is controlled by a dedicated top-level orchestrator rule (`visual-maps/*.mdc`) that guides the AI's actions.
*   **Single Source of Truth:** `memory-bank/tasks.md` serves as the central, authoritative record for all task statuses and progress, eliminating redundancy.
*   **Context Preservation:** `memory-bank/activeContext.md` acts as a dynamic handover document, maintaining critical context between mode transitions.
*   **Text-Only Rules:** All `.mdc` rule files contain only text-based instructions, ensuring direct and unambiguous AI digestion without reliance on visual interpretation.

### Beyond Basic Custom Modes

This system significantly extends Cursor's standard custom modes by transforming them into interconnected components of a cohesive development methodology:

*   **Integrated Workflow:** Modes are designed to transition logically (VAN → PLAN → CREATIVE → IMPLEMENT → REFLECT → ARCHIVE), forming a unified development process.
*   **Shared Memory:** Persistent state is maintained across mode transitions via dedicated Memory Bank files, ensuring continuous understanding.
*   **Adaptive Behavior:** Each mode dynamically adjusts its recommendations and depth of operation based on the project's assessed complexity level.
*   **Built-in QA Functions:** A flexible QA capability can be invoked from any mode to perform technical validation checks, acting as a critical gate before implementation.

### CREATIVE Mode and Claude's "Think" Tool Integration

The CREATIVE mode is conceptually aligned with Anthropic's Claude "Think" tool methodology, emphasizing structured problem-solving and design exploration. It implements:

*   **Progressive Documentation:** Concise templates for initial ideas, with detailed analysis available on demand, optimizing token usage.
*   **Structured Exploration:** Guides the AI through systematic brainstorming, option analysis, and justified decision-making.
*   **Context-Efficient Design:** Ensures that design decisions are thoroughly documented without overwhelming the context window.

## Key Features

*   **Token-Optimized Workflows:** Maximizes AI efficiency through intelligent rule loading and context management.
*   **Structured Development Phases:** Clear, sequential modes for each stage of the development lifecycle.
*   **Persistent Project Memory:** Centralized documentation for continuous context retention.
*   **Adaptive Complexity Scaling:** Tailored processes and documentation based on task size and intricacy.
*   **Automated Validation:** Integrated QA checks to ensure technical readiness and quality.
*   **Platform-Aware Commands:** Automatically adapts terminal commands for Windows, macOS, and Linux environments.
*   **Text-Only Rule Set:** All instructions are in plain text for optimal AI digestion.

## Installation Instructions

### Prerequisites

*   **Cursor Editor:** Version 0.48 or higher is required.
*   **Custom Modes:** Feature must be enabled in Cursor (Settings → Features → Chat → Custom modes).
*   **AI Model:** Claude 3.7 Sonnet is recommended for best results, especially for CREATIVE mode's "Think" tool methodology.
*   **Python:** Required to run the `refine_instructions.py` script.

### Step 1: Get the Files

Clone this repository into your project directory:

```bash
git clone https://github.com/vanzan01/cursor-memory-bank.git
```

Alternatively, download the ZIP file from GitHub and extract it to your project folder.

This provides you with all the necessary files, including:
*   Rule definitions in `.cursor/rules/isolation_rules/`
*   Custom mode prompt content in `custom_modes_refined/`
*   Template Memory Bank files in `memory-bank/`

### Step 2: Generate/Update `.mdc` Rule Files

Navigate to your project's root directory in your terminal and run the `refine_instructions.py` script. This script will generate or update all the `.mdc` rule files in the `.cursor/rules/isolation_rules/` directory with their latest, text-only content.

```bash
python custom_modes_refined/refine_instructions.py
```

### Step 3: Setting Up Custom Modes in Cursor

**This is a critical step.** You'll need to manually create six custom modes in Cursor and copy the concise instruction content from the `custom_modes_refined/` directory. These simplified prompts are essential for enabling the system's hierarchical rule loading.

#### How to Add a Custom Mode in Cursor

1.  Open Cursor and click on the mode selector in the chat panel.
2.  Select "Add custom mode."
3.  In the configuration screen:
    *   Enter the mode name (you can include emoji icons like 🔍, 📋, 🎨, ⚒️ by copy-pasting them at the beginning of the name).
    *   Select an icon from Cursor's limited predefined options.
    *   Add a shortcut (optional).
    *   Check the required tools.
    *   Click on **Advanced options**.
    *   In the empty text box that appears at the bottom, **paste the exact content** from the corresponding file in `custom_modes_refined/`.

#### Mode Configuration

For each mode, configure as follows:

1.  **VAN MODE** (Initialization)
    *   **Name**: 🔍 VAN
    *   **Tools**: Enable "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
    *   **Advanced options**: Paste from `custom_modes_refined/van.md`

2.  **PLAN MODE** (Task Planning)
    *   **Name**: 📋 PLAN
    *   **Tools**: Enable "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
    *   **Advanced options**: Paste from `custom_modes_refined/plan.md`

3.  **CREATIVE MODE** (Design Decisions)
    *   **Name**: 🎨 CREATIVE
    *   **Tools**: Enable "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
    *   **Advanced options**: Paste from `custom_modes_refined/creative.md`

4.  **IMPLEMENT MODE** (Code Implementation)
    *   **Name**: ⚒️ IMPLEMENT
    *   **Tools**: Enable all tools
    *   **Advanced options**: Paste from `custom_modes_refined/implement.md`

5.  **REFLECT MODE** (Review & Archive)
    *   **Name**: 🔍 REFLECT
    *   **Tools**: Enable "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
    *   **Advanced options**: Paste from `custom_modes_refined/reflect_archive.md`

> **Note**: The `REFLECT` custom mode handles both the reflection process and, upon the "ARCHIVE NOW" command, triggers the archiving process. This combines the final two stages into one custom mode for streamlined operation.

For additional help on setting up custom modes in Cursor, refer to the [official Cursor documentation on custom modes](https://docs.cursor.com/chat/custom-modes).

### QA Functionality

QA is not a separate custom mode but rather a set of validation functions that can be called from any mode. You can invoke QA capabilities by typing "QA" in any mode when you need to perform technical validation. This approach provides flexibility to conduct verification at any point in the development process.

## Core Files and Their Purposes

The Memory Bank system's persistent memory and operational state are maintained through a structured set of Markdown files within the `memory-bank/` directory:

*   **`tasks.md`**: The central source of truth for all task tracking, detailing task statuses, sub-tasks, and overall project roadmap.
*   **`activeContext.md`**: Maintains the current development focus, holds transient information, and acts as the primary handover document between different modes.
*   **`progress.md`**: Tracks the detailed implementation status and logs significant activities and milestones.
*   **`projectbrief.md`**: Provides a high-level overview of the project's purpose, core functionality, and key technologies.
*   **`productContext.md`**: Outlines the target users, key user needs, and product goals.
*   **`systemPatterns.md`**: Documents high-level architectural patterns and principles relevant to the project.
*   **`techContext.md`**: Details the project's technical stack, including backend, frontend, database, libraries, and operating system specifics.
*   **`style-guide.md`**: Defines coding style guidelines and UI/UX visual standards.
*   **`creative/` (directory)**: Stores detailed design decision documents generated during the CREATIVE mode.
*   **`reflection/` (directory)**: Contains post-task review documents created during the REFLECT mode.
*   **`archive/` (directory)**: Holds final, consolidated task archive documents upon task completion.
*   **`.qa_validation_status` (hidden file)**: A simple flag used internally to track the status of the last QA validation.

## Troubleshooting

### Common Issues

1.  **Mode not responding correctly:**
    *   Verify the exact content was copied from `custom_modes_refined/*.md` into Cursor's "Advanced options." This is the most common issue.
    *   Ensure the correct tools are enabled for each mode in Cursor's settings.
    *   Confirm you've switched to the correct mode before issuing commands.
2.  **Rules not loading:**
    *   Make sure the `.cursor/rules/isolation_rules/` directory exists directly under your project's root.
    *   Verify file permissions allow Cursor to read the `.mdc` files.
    *   Ensure you've run the `refine_instructions.py` script successfully.
3.  **Command execution issues:**
    *   Confirm you're running commands from the correct project directory.
    *   Verify that platform-specific commands are being correctly adapted (the system attempts this automatically, but manual confirmation may be needed if issues persist).
4.  **AI looping in quick fixes:**
    *   This indicates the task might be more complex than initially assessed. The system's quick triage has strict criteria.
    *   If the AI gets stuck, manually intervene and instruct it to re-assess the task's complexity via `VAN` mode, pushing it to a higher level (L2+).

## Version Information

This is version **v0.7-beta** of the Enhanced Memory Bank system. It incorporates significant token optimization improvements and workflow refinements.

### Ongoing Development

The Enhanced Memory Bank system is actively being developed and improved by its maintainer. Key points to understand:

*   **Work in Progress:** This is a beta version with ongoing development. Expect regular updates, optimizations, and new features based on real-world usage.
*   **Feature Optimization:** The modular architecture enables continuous refinement without breaking existing functionality.
*   **Community Contribution:** While a personal project, insights and feedback from users are always welcome and can inspire future enhancements.

## Resources

*   [Memory Bank Optimizations](MEMORY_BANK_OPTIMIZATIONS.md) - Detailed overview of token efficiency improvements.
*   [Memory Bank Upgrade Guide](memory_bank_upgrade_guide.md) - Explains the transition from monolithic to modular architecture.
*   [CREATIVE Mode and Claude's "Think" Tool](creative_mode_think_tool.md) - Explains the methodology behind the CREATIVE mode.
*   [Official Cursor Custom Modes Documentation](https://docs.cursor.com/chat/custom-modes) - For general Cursor custom mode setup.