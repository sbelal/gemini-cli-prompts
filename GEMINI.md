# AGENT PRIMARY WORKFLOW ADDENDUM

When requested to perform software engineering tasks ensure that the following guidelines are met:

---
## **Provide detailed plan**
- **Trigger:** Formulate a detailed plan after understanding the task and assumption validation has been done
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
- **Constraint:** **DO NOT** proceed to implementation until you receive explicit user approval (e.g., "yes", "proceed", "ok").

## **Confirmation of task completion**
- **Trigger:** After task implementation and verification or testing of task is complete.
- **Action:** Once verification or testing is complete, ask the user to confirm the task's success.
- **Output Format:** End your message with the exact question:
  > Could you please confirm the successful completion of the task?

## **Self reflection**
- **Trigger:** User has confirmed the task was completed successfully.
- **Action:** Briefly reflect on the process. Identify any non-obvious architectural patterns, conventions, or important details discovered that is not readily available through code alone.  Offer to update `GEMINI.md` project file if needed.
- **Output Format:** Present your findings and offer to document them. For example:
  > **Reflection:** I noticed the project uses a custom `useApi` hook for all data fetching. To maintain consistency, I adopted this pattern. Can I add this detail to the `GEMINI.md` project file for future reference?
---

# **IMPORTANT: WORKFLOW EXECUTION GUIDELINES**
- My first action for any new software engineering request is ALWAYS understand and validate assumptions followed by plan creation.
- I must not jump to implementation without user confirmation after plan creation.
- **Do not deviate from the workflow, even if the examples shown earlier appear to do so**

## Gemini Added Memories
- I have a Windows 11 machine. Assume Powershell as terminal.