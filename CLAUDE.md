# Engineering Principles & Rules

1. **Think Before Coding:**
   - Do not make silent assumptions.
   - If requirements or edge cases are unclear, ask for clarification first.
   - State assumptions explicitly before modifying files.

2. **Keep Implementations Simple:**
   - The simplest working solution is the correct solution.
   - Do not add unrequested abstractions, extra utility functions, or future-proofing.
   - Prefer shorter, clear, readable code.

3. **Make Surgical Changes:**
   - Touch ONLY files required for the requested feature or fix.
   - Do not refactor adjacent code, change code formatting in untouched lines, or make orthogonal edits.

4. **Explicit Verification:**
   - Never report a task as complete without testing it.
   - Run the project's typechecker, linter, or tests (whichever exist for the stack in use) to verify changes before concluding.

5. **Commit and Push Automatically:**
   - After any meaningful change, once it's verified, commit it and push to GitHub without asking.
   - Use a clear commit message that describes the change.

@AGENTS.md

# Hackathon Context

This repo is for a time-boxed hackathon. The problem statement will be given at the start.

- **Ship a working demo first.** Prefer the fastest path to an end-to-end working flow; polish after.
- **Plan before building.** When the problem statement arrives, agree on scope, stack, and a short milestone list before writing code. Record key decisions in `docs/adr/`.
- **Keep secrets and large files out of git.** API keys go in `.env` (gitignored) with a committed `.env.example`; videos and model weights stay local (see `.gitignore`).
- **Keep the README current** with setup and run instructions so judges and teammates can run the project.
