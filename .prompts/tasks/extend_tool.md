## TASK: Extend or Add Tool to Agent

Add a new tool or modify an existing tool for an ADK agent.

### INPUTS REQUIRED
- `agent_path`: Path to agent package
- `tool_name`: Name of the tool
- `tool_function`: Function implementation
- `description`: What the tool does
- `parameters`: List of parameters with types
- `returns`: Return type and structure

### IMPLEMENTATION STEPS

1. **Create/Update Tool Module**
   Location: `src/instabids/tools/{{module_name}}.py`
   
   ```python
   from google.adk.types import ToolContext
   from typing import Dict, Any, Optional
   import structlog
   
   logger = structlog.get_logger()
   
   def {{tool_name}}(
       tool_context: ToolContext,
       {{parameters}}
   ) -> dict:
       """
       {{description}}
       
       Args:
           tool_context (ToolContext): ADK tool context for state access
           {{parameter_docs}}
       
       Returns:
           dict: {{return_description}}
               Example: {"status": "success", "result": ...}
       """
       try:
           # Implementation
           {{implementation}}
           
           return {
               "status": "success",
               "result": result
           }
       except Exception as e:
           logger.error(f"Error in {{tool_name}}", error=str(e))
           return {
               "status": "error",
               "message": str(e)
           }
   ```

2. **Register Tool in Agent**
   Update agent initialization:
   ```python
   from instabids.tools.{{module_name}} import {{tool_name}}
   
   class {{AgentClass}}({{AgentType}}):
       def __init__(self):
           super().__init__(
               # ... other params ...
               tools=[
                   # ... existing tools ...
                   {{tool_name}}
               ]
           )
   ```

3. **Add Tool Tests**
   Create `tests/unit/test_{{tool_name}}.py`:
   ```python
   import pytest
   from unittest.mock import Mock
   from google.adk.types import ToolContext
   from instabids.tools.{{module_name}} import {{tool_name}}
   
   @pytest.fixture
   def mock_tool_context():
       context = Mock(spec=ToolContext)
       context.state = {}
       return context
   
   def test_{{tool_name}}_success(mock_tool_context):
       result = {{tool_name}}(
           mock_tool_context,
           {{test_parameters}}
       )
       
       assert result["status"] == "success"
       assert "result" in result
       {{additional_assertions}}
   
   def test_{{tool_name}}_error_handling(mock_tool_context):
       # Test error cases
       result = {{tool_name}}(
           mock_tool_context,
           {{invalid_parameters}}
       )
       
       assert result["status"] == "error"
       assert "message" in result
   ```

4. **Update Documentation**
   Add to `docs/TOOL_LIBRARY.md`:
   ```markdown
   ### {{tool_name}}
   - **Module**: `instabids.tools.{{module_name}}`
   - **Purpose**: {{description}}
   - **Parameters**: {{parameter_list}}
   - **Returns**: {{return_structure}}
   - **Used by**: {{agent_list}}
   ```

### TOOL DESIGN PRINCIPLES

1. **First Parameter**: Always `tool_context: ToolContext`
2. **Return Format**: Always return dict with `status` field
3. **Error Handling**: Catch exceptions and return error dict
4. **Logging**: Use structlog for debugging
5. **Docstring**: Minimum 5 lines with Args/Returns
6. **State Access**: Use tool_context.state with proper prefixes
7. **Async Support**: Use `async def` if I/O operations

### VALIDATION CHECKLIST
- [ ] Tool has comprehensive docstring (≥5 lines)
- [ ] First parameter is tool_context
- [ ] Returns dict with status field
- [ ] Error handling implemented
- [ ] Unit tests written and passing
- [ ] Agent successfully uses tool
- [ ] Documentation updated