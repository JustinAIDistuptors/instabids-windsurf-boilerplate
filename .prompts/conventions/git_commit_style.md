## Git Commit Message Convention

Follow the Conventional Commits specification for all commits.

### FORMAT

```
<type>(<scope>): <subject>

<body>

<footer>
```

### COMMIT TYPES

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, semicolons, etc)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system or dependencies
- `ci`: CI/CD configuration
- `chore`: Other changes (maintenance)
- `revert`: Revert a previous commit

### SCOPE

Use component/module names:
- `homeowner`: HomeownerAgent related
- `recruiter`: OutboundRecruiterAgent related
- `contractor`: ContractorAgent related
- `api`: FastAPI backend
- `frontend`: Next.js application
- `supabase`: Database/backend services
- `tools`: Agent tools
- `tests`: Test infrastructure

### SUBJECT LINE

- Use imperative mood: "add" not "adds" or "added"
- Don't capitalize first letter
- No period at the end
- Maximum 50 characters

### BODY

- Wrap at 72 characters
- Explain what and why, not how
- Separate from subject with blank line
- Use bullet points for multiple items

### FOOTER

- Reference issues: `Fixes #123`
- Breaking changes: `BREAKING CHANGE: description`
- Co-authors: `Co-authored-by: Name <email>`

### EXAMPLES

#### Simple Feature
```
feat(homeowner): add image analysis tool integration
```

#### Bug Fix with Details
```
fix(supabase): resolve RLS policy for service role access

The service role was unable to access user preferences due to
missing policy. Added explicit policy granting full access to
service_role for backend operations.

Fixes #45
```

#### Breaking Change
```
refactor(api)!: restructure project endpoints

Consolidated project-related endpoints under /api/v1/projects.
Old endpoints under /api/projects are removed.

BREAKING CHANGE: API endpoints have moved. Update frontend
configuration to use new paths:
- GET /api/projects -> GET /api/v1/projects
- POST /api/project -> POST /api/v1/projects
```

#### Multiple Changes
```
feat(contractor): implement bid submission flow

- Add bid creation endpoint
- Create bid validation logic  
- Implement real-time notifications
- Add comprehensive test coverage

Co-authored-by: AI Agent <agent@instabids.com>
```

### AUTOMATED ENFORCEMENT

1. **Pre-commit Hook**: Validates format
2. **CI Check**: Ensures PR titles follow convention
3. **Changelog Generation**: Auto-generates from commits

### AI AGENT GUIDELINES

When committing code:
1. Analyze changes to determine correct type
2. Identify the primary scope affected
3. Write clear, concise subject
4. Add body for complex changes
5. Reference any related issues
6. Note breaking changes prominently