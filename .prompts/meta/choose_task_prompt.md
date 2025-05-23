## META: Task Prompt Selection Logic

Analyze the user's request and select the appropriate task prompt.

### TASK PROMPT MAPPING

#### create_llm_agent.md
- Creating standard LlmAgent
- Non-real-time agents
- Agents that process and respond
- Keywords: "create agent", "new agent", "LlmAgent"

#### create_live_agent.md  
- Creating LiveAgent for streaming
- Real-time interaction agents
- Audio/video processing agents
- Keywords: "live agent", "streaming", "real-time"

#### extend_tool.md
- Adding new tools to agents
- Modifying existing tools
- Tool integration
- Keywords: "add tool", "new function", "extend"

#### debug_supabase.md
- Supabase errors (403, 404)
- RLS policy issues
- Database connection problems
- Keywords: "supabase error", "permission denied", "RLS"

#### generate_tests.md
- Creating test files
- Unit test implementation
- Integration test setup
- Keywords: "test", "testing", "pytest"

#### critique_code.md
- Code review requests
- Improvement suggestions
- Refactoring guidance
- Keywords: "review", "improve", "critique", "better"

#### doctor_route.md
- Health check endpoints
- System status APIs
- Monitoring setup
- Keywords: "health check", "doctor", "status endpoint"

#### setup_rag.md
- RAG implementation
- pgvector configuration
- Embedding setup
- Keywords: "RAG", "vector", "embeddings", "knowledge base"

#### implement_a2a.md
- Agent-to-agent communication
- Event system setup
- A2A protocol implementation
- Keywords: "A2A", "agent communication", "events"

### SELECTION RULES

1. **Exact Match**: Look for keywords first
2. **Context Analysis**: Consider the broader request
3. **Multiple Tasks**: Can return up to 3 prompts
4. **Include Dependencies**: 
   - If creating agent → might need extend_tool
   - If debugging → might need generate_tests

### COMMON COMBINATIONS

```
tasks/create_llm_agent.md
tasks/extend_tool.md
tasks/generate_tests.md
```

```
tasks/debug_supabase.md
tasks/generate_tests.md
```

```
tasks/setup_rag.md
tasks/extend_tool.md
```

### OUTPUT FORMAT

Return file paths, one per line:
```
tasks/create_llm_agent.md
tasks/generate_tests.md
```