# AGENT PRIMARY WORKFLOW ADDENDUM

**IMPORTANT: YOU MUST FOLLOW THESE STEPS FOR EVERY TASK. DO NOT DEVIATE.**

Before taking any other action, you MUST start with Step 1 of this workflow.

---
### **Step 1: Understand**
1. **Action:** Think about the user's request and the relevant codebase context. Run appropriate tools to understand file structures, existing code patterns, and conventions first.  Use tools to read files and validate your assumptions.  Only proceed to "Step 2: Plan" after your assumptions are validated.  Do not jump to editing file yet.

### **Step 2: Plan**
- **Action:** Analyze the user's request and create a detailed, step-by-step implementation plan.  Only provide the plan and do not implement.
- **Output Format:** Your response for this step MUST contain ONLY the plan, formatted as follows:

  Plan of Action:
  1. File: [path/to/file.ts] (MODIFIED/NEW)
     Target: `ClassName` or `functionName`
     Change/Action: [A concise summary of the specific change]
  2. Command: `[shell command to run]`
     Purpose: [Reason for running the command]

- **User Confirmation:** After providing the complete plan, end your message with the exact question:
  > Should I proceed with this plan?

- **Constraint:** **DO NOT** proceed to Step 3 until you receive explicit user approval (e.g., "yes", "proceed", "ok").

### **Step 3: Implementation**
- **Trigger:** User has approved the plan from Step 2.
- **Action:** Execute the approved plan using the available tools (e.g., modifying files, running shell commands).
- **Output Format:** Provide a brief, factual summary of the actions taken. For example: "Modified `path/to/file.ts` and ran `npm install` as per the plan."

### **Step 4: Verification**
- **Action:** After implementation, verify the changes. This may involve running tests, linting, or other quality checks relevant to the task.
- **Output Format:** Report the results of the verification. For example: "All 15 unit tests passed successfully." or "Linting reported 2 minor style issues."

### **Step 5: Confirmation**
- **Action:** Once verification is complete, ask the user to confirm the task's success.
- **Output Format:** End your message with the exact question:
  > Could you please confirm the successful completion of the task?

### **Step 6: Reflection**
- **Trigger:** User has confirmed the task was completed successfully.
- **Action:** Briefly reflect on the process. Identify any non-obvious architectural patterns, conventions, or important details discovered.  Offer to update `GEMINI.md` project file if needed.
- **Output Format:** Present your findings and offer to document them. For example:
  > **Reflection:** I noticed the project uses a custom `useApi` hook for all data fetching. To maintain consistency, I adopted this pattern. Can I add this detail to the `GEMINI.md` project file for future reference?

---

**FINAL REMINDER: Your first action for any new request is ALWAYS to create a plan as described in Step 2 and end with Step 6 after successful completion.  Ensure workflow is followed from step 1 to step 6.**
**During "Step 1: Understand" make sure you validate assumptions by running tools to search and read existing code.**

## Gemini Added Memories
- Always try to provide details and expand your search to find relevant code.