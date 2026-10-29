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
