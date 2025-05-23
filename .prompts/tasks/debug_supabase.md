## TASK: Debug Supabase Integration Issues

Diagnose and fix Supabase-related errors in the InstaBids system.

### COMMON ISSUES AND SOLUTIONS

#### 1. RLS Policy Violations (403 Forbidden)
**Symptom**: `permission denied for table`

**Diagnosis Steps**:
1. Check current user role
2. Review RLS policies on affected table
3. Verify service role key usage

**Fix Template**:
```sql
-- Add policy for service role
CREATE POLICY "Service role full access" ON {{table_name}}
    FOR ALL
    TO service_role
    USING (true)
    WITH CHECK (true);

-- Add policy for authenticated users (own data only)
CREATE POLICY "Users manage own {{table_name}}" ON {{table_name}}
    FOR ALL
    TO authenticated
    USING (auth.uid() = owner_id)
    WITH CHECK (auth.uid() = owner_id);
```

#### 2. Missing Tables/Columns
**Symptom**: `relation "{{table}}" does not exist`

**Fix**: Create migration file `db/migrations/{{number}}_fix_{{issue}}.sql`:
```sql
-- Create missing table
CREATE TABLE IF NOT EXISTS {{table_name}} (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    {{columns}}
);

-- Add RLS
ALTER TABLE {{table_name}} ENABLE ROW LEVEL SECURITY;

-- Add indexes
CREATE INDEX idx_{{table}}_{{column}} ON {{table_name}}({{column}});
```

#### 3. Connection Issues
**Symptom**: `connection refused` or timeout

**Checklist**:
- [ ] Supabase service running: `supabase status`
- [ ] Correct URL in .env: `SUPABASE_URL`
- [ ] Valid keys: `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`
- [ ] Network connectivity to Supabase

#### 4. Storage Bucket Access
**Symptom**: 403 when uploading/fetching files

**Fix**:
```sql
-- Create bucket if missing
INSERT INTO storage.buckets (id, name, public)
VALUES ('generated-code', 'generated-code', false)
ON CONFLICT (id) DO NOTHING;

-- Add RLS policy for bucket
CREATE POLICY "Service role storage access" ON storage.objects
    FOR ALL
    TO service_role
    USING (bucket_id = 'generated-code')
    WITH CHECK (bucket_id = 'generated-code');
```

### DEBUGGING TOOLS

#### 1. Check RLS Policies
```python
def check_rls_policies(table_name: str):
    """List all RLS policies for a table."""
    query = """
        SELECT 
            pol.polname as policy_name,
            pol.polcmd as command,
            pol.polroles::regrole[] as roles,
            pol.polqual as using_expression,
            pol.polwithcheck as check_expression
        FROM pg_policies pol
        WHERE pol.tablename = %s
    """
    return supabase.rpc('check_policies', {'table': table_name})
```

#### 2. Test Service Role Access
```python
async def test_service_role_access():
    """Verify service role can access protected resources."""
    # Use service role client
    service_client = create_client(
        os.environ["SUPABASE_URL"],
        os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    )
    
    # Try operations that require elevated permissions
    result = await service_client.table('projects').select('*').execute()
    print(f"Service role access: {'✓' if result.data else '✗'}")
```

#### 3. Trace Query Execution
```python
import structlog
logger = structlog.get_logger()

def trace_query(query: str, params: dict = None):
    """Execute query with detailed logging."""
    logger.info("Executing query", query=query, params=params)
    try:
        result = supabase.rpc('execute_sql', {
            'query': query,
            'params': params
        })
        logger.info("Query successful", rows=len(result.data))
        return result
    except Exception as e:
        logger.error("Query failed", error=str(e), query=query)
        raise
```

### FIX VERIFICATION

After applying fixes:
1. Run integration tests: `pytest tests/integration/test_supabase.py`
2. Check agent functionality: `poetry run adk test`
3. Verify in UI: Create test project and check data flow

### RETURN FORMAT

Provide fix as either:
1. SQL migration file content
2. Python code patch
3. Configuration update
4. Step-by-step resolution guide