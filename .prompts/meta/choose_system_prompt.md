## META: System Prompt Selection Logic

Analyze the current conversation context and select the appropriate system prompt.

### SELECTION CRITERIA

#### master_code_builder.md
Use when:
- Task involves multiple agents or components
- General architecture or design decisions
- Orchestration of sub-tasks
- No specific agent is mentioned
- Keywords: "build", "implement", "create system", "architecture"

#### homeowner_agent_writer.md
Use when:
- Implementing HomeownerAgent specifically
- Project scoping features
- User interaction flows
- Image analysis integration
- Keywords: "homeowner", "project scoping", "Q&A", "bid card"

#### outbound_recruiter_agent_writer.md
Use when:
- Implementing OutboundRecruiterAgent
- Contractor matching logic
- Invitation systems
- A2A event handling for recruitment
- Keywords: "recruiter", "matching", "contractor invitation"

#### contractor_agent_writer.md
Use when:
- Implementing ContractorAgent
- Bid formulation features
- Contractor-side interactions
- Keywords: "contractor", "bidding", "bid submission"

#### prompt_selector.md
Use when:
- Meta-discussion about prompts
- Implementing prompt selection logic
- Uncertainty about which prompt to use
- Keywords: "which prompt", "prompt selection"

### DECISION FLOW

1. **Check for Specific Agent**
   - HomeownerAgent → homeowner_agent_writer.md
   - OutboundRecruiterAgent → outbound_recruiter_agent_writer.md
   - ContractorAgent → contractor_agent_writer.md

2. **Check Task Scope**
   - Multiple agents → master_code_builder.md
   - Single component → Specific system prompt
   - Meta/unclear → prompt_selector.md

3. **Default Selection**
   - When in doubt → master_code_builder.md
   - It can delegate to specialists

### OUTPUT FORMAT

Return ONLY the relative path:
```
system/master_code_builder.md
```

Or for multiple (max 2):
```
system/master_code_builder.md
system/homeowner_agent_writer.md
```