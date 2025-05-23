## ADK Tool Docstring Convention

All Python functions intended for use as ADK FunctionTools MUST have comprehensive docstrings. The LLM relies critically on these for understanding and correct usage.

### REQUIRED STRUCTURE

```python
def tool_name(tool_context: ToolContext, param1: str, param2: int = None) -> dict:
    """
    One-sentence summary of what the tool does.
    
    Longer description if needed, explaining the tool's purpose,
    behavior, and any important context or limitations.
    
    Args:
        tool_context (ToolContext): The ADK tool context providing access 
            to session state and other resources.
        param1 (str): Description of param1, including valid values
            or format requirements.
        param2 (int, optional): Description of param2. Defaults to None.
            Explain when/why to use this parameter.
    
    Returns:
        dict: Description of the return structure.
            - status (str): 'success' or 'error'
            - result (Any): The actual result data (type varies)
            - message (str): Error message if status is 'error'
            
            Example:
            {
                "status": "success",
                "result": {
                    "id": "123",
                    "data": "processed value"
                }
            }
    
    Raises:
        ValueError: If param1 is invalid format
        ConnectionError: If database is unreachable
    
    Examples:
        >>> result = tool_name(ctx, "test_value", 42)
        >>> print(result["status"])
        'success'
    """
```

### MINIMUM REQUIREMENTS

1. **Length**: At least 5 lines
2. **Sections**: Must include `Args:` and `Returns:`
3. **First Parameter**: Always document `tool_context`
4. **Type Annotations**: Include types for all parameters
5. **Return Structure**: Clearly describe dict structure

### STYLE GUIDELINES

1. **Summary Line**: 
   - Single line, ends with period
   - Uses imperative mood ("Analyze", not "Analyzes")
   - Under 80 characters

2. **Args Section**:
   - List each parameter on its own line
   - Format: `param_name (type): Description`
   - Note optional parameters and defaults
   - Explain valid values/formats

3. **Returns Section**:
   - Specify the type (usually `dict`)
   - Detail the structure with sub-items
   - Provide example return values
   - Always include `status` field documentation

4. **Optional Sections**:
   - `Raises:` for exceptions
   - `Examples:` for usage patterns
   - `Note:` for important caveats
   - `See Also:` for related tools

### BAD EXAMPLE ❌

```python
def get_data(ctx, id):
    """Gets data."""
    # Implementation
```

### GOOD EXAMPLE ✅

```python
def fetch_project_details(tool_context: ToolContext, project_id: str, 
                         include_messages: bool = False) -> dict:
    """
    Fetch comprehensive details for a specific project.
    
    Retrieves project information from the database, including
    basic metadata, bid card details, and optionally all associated
    messages. Uses the service role for elevated access.
    
    Args:
        tool_context (ToolContext): ADK context for state management.
            Expects 'user:id' to be set for ownership verification.
        project_id (str): UUID of the project to retrieve.
            Must be a valid UUID format.
        include_messages (bool, optional): Whether to include the full
            message history. Defaults to False to reduce payload size.
    
    Returns:
        dict: Project information with the following structure:
            - status (str): 'success' or 'error'
            - result (dict): Project data including:
                - id (str): Project UUID
                - title (str): Project title
                - description (str): Full description
                - bid_card (dict): Generated bid card data
                - messages (list): Chat messages (if requested)
            - message (str): Error description if status is 'error'
    
    Raises:
        ValueError: If project_id is not valid UUID format
        PermissionError: If user doesn't own the project
    """
```

### ENFORCEMENT

- CI will fail if docstrings don't meet requirements
- Use `tests/tool_schema_test.py` to validate
- AI agents will reject tools with poor documentation