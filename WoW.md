# Ways of Working

While working on these tasks, you are expected to do the following:

- Follow the partial-disclosure rule. Do not read files in .tasks that you have not already been informed about in the current or previous steps.
- Write architectural decision records (ADRs) covering both the network and systems aspects. Store them as Markdown files in the ADR folder.
- Standardize your design and deployment methods. Use the templates directory to store reusable information for this purpose.
- Keep any state that does not fit elsewhere in the state folder.
- You are free to decide the order in which you solve tasks within a stage, but you may not continue until you resolve an issue or decide to stop.
- You are free  to install tools on the system, your job is to be a NetDevOps engineer, following modern practices.
- Verification is mandatory.
- Use of automation and scripting (Netmiko, Ansible, openTofu, etc) is highly encouraged
- At the end of each stage, create a folder for that stage in the eval directory, back up all VyOS device configurations into a subfolder called backups, and write an EVALUATION.md file describing how you think the stage went. Once you move past a stage, updates to that evaluation are not allowed; any changes in your assessment should be documented in future evaluations.
- You are in full control of both the servers and the network devices and do not need approval before making changes.
- Follow modern best practices when no explicit instructions are provided for solving a task.
- On VyOS devices, do not leave the VyOS CLI unless it is absolutely necessary. If you must use bash for a task, document the reason in an ADR.
- After you finish verification for each stage, add, commit, and push your changes to git.
- After the git commit succeeds, record the current step and time in TIME.MD. This file is append-only and represents your finish time for that section.
- ONLY after the git commit is successful and the time has been logged may you proceed to read the next stage file.
