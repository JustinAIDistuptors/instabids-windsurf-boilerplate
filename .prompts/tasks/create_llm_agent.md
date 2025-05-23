## TASK: Create New LlmAgent

Generate a new LlmAgent implementation for the InstaBids project.

### INPUTS REQUIRED
- `agent_name_snake`: Snake case name (e.g., `bid_analyzer`)
- `class_name`: Pascal case class name (e.g., `BidAnalyzerAgent`)
- `description`: Agent purpose and capabilities
- `model_id`: Model to use (default: `"gemini-2.0-flash-exp"`)
- `instructions`: System instructions for the agent
- `tools`: List of tool names to include
- `path`: Package path under `src/instabids/agents/`

### IMPLEMENTATION STEPS

1. **Create Directory Structure**
   ```
   src/instabids/agents/{{agent_name_snake}}/
   ├── __init__.py
   ├── agent.py
   └── prompts.py
   ```

2. **Write agent.py**
   ```python
   from google.adk.agents import LlmAgent
   from google.adk.types import ToolContext
   from .prompts import {{AGENT_NAME_UPPER}}_INSTRUCTIONS
   
   class {{class_name}}(LlmAgent):
       def __init__(self):
           super().__init__(
               name="{{agent_name_snake}}",
               model="{{model_id}}",
               instructions={{AGENT_NAME_UPPER}}_INSTRUCTIONS,
               tools=[{{tools}}],
               description="{{description}}"
           )
   
   # Required export for ADK
   agent = {{class_name}}()
   ```

3. **Write prompts.py**
   ```python
   {{AGENT_NAME_UPPER}}_INSTRUCTIONS = """
   {{instructions}}
   
   Remember to:
   - Use state prefixes (user:, app:, temp:)
   - Return structured responses
   - Handle errors gracefully
   """
   ```

4. **Update __init__.py**
   ```python
   from .agent import agent
   
   __all__ = ["agent"]
   ```

5. **Update .adk/components.json**
   Add entry:
   ```json
   {
     "name": "{{agent_name_snake}}",
     "class": "instabids.agents.{{agent_name_snake}}.agent.{{class_name}}",
     "description": "{{description}}",
     "type": "llm"
   }
   ```

6. **Generate Tests**
   Create `tests/unit/test_{{agent_name_snake}}.py`:
   ```python
   import pytest
   from instabids.agents.{{agent_name_snake}} import agent
   
   def test_{{agent_name_snake}}_initialization():
       assert agent.name == "{{agent_name_snake}}"
       assert agent.model == "{{model_id}}"
       assert len(agent.tools) == {{tool_count}}
   
   @pytest.mark.asyncio
   async def test_{{agent_name_snake}}_basic_query():
       # Test implementation
       pass
   ```

### VALIDATION CHECKLIST
- [ ] Agent exports as `agent` variable
- [ ] All tools have proper ToolContext parameter
- [ ] Instructions include state prefix reminder
- [ ] Tests pass: `pytest tests/unit/test_{{agent_name_snake}}.py`
- [ ] Agent appears in ADK Dev UI

### COMMON PITFALLS TO AVOID
- Don't use `root_agent` - always export as `agent`
- Don't forget the ToolContext parameter in tools
- Don't use deprecated import patterns
- Don't hardcode sensitive data