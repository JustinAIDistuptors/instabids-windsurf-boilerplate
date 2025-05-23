# InstaBids Windsurf Boilerplate 🚀

> Production-ready boilerplate for building AI-driven multi-agent systems using Google ADK 1.0.0+ and Supabase, optimized for 100% autonomous development

[![Google ADK](https://img.shields.io/badge/Google%20ADK-1.0.0-blue)](https://pypi.org/project/google-adk/)
[![Python](https://img.shields.io/badge/Python-3.12-green)](https://www.python.org/)
[![Supabase](https://img.shields.io/badge/Supabase-Backend-orange)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🎯 Mission Statement

This boilerplate is designed for the future of software development: **100% AI-driven coding**. Every line of code, every test, every deployment will be written and maintained by AI agents. The repository structure, prompts, and conventions are optimized for AI comprehension and execution.

## 🏗️ Architecture Overview

InstaBids is a multi-agent bidding platform that revolutionizes home improvement project management:

- **HomeownerAgent**: Interactive project scoping with AI-powered Q&A
- **BidCard Generation**: Automatic project summarization with vision analysis
- **OutboundRecruiterAgent**: Intelligent contractor matching and invitation
- **ContractorAgent**: AI-assisted bid formulation and submission
- **Messaging System**: Real-time communication with conversation memory

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Golden Development Environment](#-golden-development-environment)
- [AI Agent Architecture](#-ai-agent-architecture)
- [Common Pitfalls & Solutions](#-common-pitfalls--solutions)
- [Testing Strategy](#-testing-strategy)
- [Deployment Guide](#-deployment-guide)
- [Contributing](#-contributing)

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker (for local Supabase)
- Poetry 1.8.2+
- pnpm 8+

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/JustinAIDistuptors/instabids-windsurf-boilerplate.git
cd instabids-windsurf-boilerplate

# Run the environment setup script
./scripts/reset_env.sh  # or .ps1 for Windows

# Copy environment variables
cp .env.template .env
# Edit .env with your API keys

# Install dependencies
poetry install --sync
pnpm install

# Start Supabase locally
supabase start

# Apply database migrations
supabase db push

# Start the development servers
poetry run adk web  # ADK Dev UI on http://localhost:8000
pnpm dev           # Next.js on http://localhost:3000
```

## 📁 Project Structure

```
instabids-windsurf-boilerplate/
├── .adk/
│   └── components.json          # ADK agent registry
├── .github/
│   └── workflows/
│       └── ci_cd_for_ai.yml    # AI-driven CI/CD pipeline
├── .prompts/                    # AI instruction repository
│   ├── system/                  # Agent role definitions
│   ├── tasks/                   # Reusable task templates
│   ├── conventions/             # Coding standards
│   └── meta/                    # Prompt selection logic
├── docs/                        # AI-consumable documentation
│   ├── README_FOR_AI_CODERS.md
│   ├── COMMON_PITFALLS.md
│   ├── ADK_BEST_PRACTICES.md
│   └── SUPABASE_PATTERNS.md
├── src/
│   ├── instabids/
│   │   ├── agents/             # ADK agent implementations
│   │   ├── api/                # FastAPI backend
│   │   ├── data/               # Database repositories
│   │   └── tools/              # Agent tools
│   └── frontend/               # Next.js application
├── tests/                      # Comprehensive test suite
├── scripts/                    # Development utilities
├── db/                         # Database migrations
├── pyproject.toml             # Python dependencies
├── package.json               # Node dependencies
└── README.md                  # This file
```

## 🔧 Golden Development Environment

Based on extensive real-world testing with ADK 1.0.0:

| Component | Version/Config | Rationale |
|-----------|---------------|------------|
| Python | 3.12-slim | Consistent across dev/CI/prod |
| Poetry | 1.8.2+ | Fixes cache bugs from 1.7.x |
| ADK | ~1.0.0 with [vertexai] | Production-ready release |
| Protobuf | ==5.29.4 | Prevents pb2 import errors |
| Supabase | Latest | Backend for everything |

## 🤖 AI Agent Architecture

### Core Agents

1. **HomeownerAgent** (LiveAgent)
   - Interactive project scoping
   - Vision analysis for photos
   - Preference learning
   - State management with user:/app:/temp: prefixes

2. **OutboundRecruiterAgent** (BaseAgent)
   - Contractor matching algorithm
   - Invitation management
   - A2A communication

3. **ContractorAgent** (LlmAgent)
   - Bid formulation assistance
   - Project analysis
   - Communication facilitation

### Agent Communication

```python
# A2A Event Flow
ProjectCreated → BidCardGenerated → ContractorsInvited → BidsReceived
```

## 🚨 Common Pitfalls & Solutions

Top 5 issues from production deployments:

1. **Wrong Import**: `from google import genai` (NOT `import google.generativeai`)
2. **Ghost Git Wheel**: Run `./scripts/reset_env.sh` if module errors persist
3. **Agent Export**: Always export as `agent` in `__init__.py`
4. **Tool Context**: First parameter must be `tool_context: ToolContext`
5. **Windows Streaming**: Add Proactor loop initialization

See `docs/COMMON_PITFALLS.md` for the complete list of 30+ issues and fixes.

## 🧪 Testing Strategy

```bash
# Run all tests
poetry run pytest              # Unit & integration tests
pnpm run test                  # Frontend tests
pnpm run cypress:run          # E2E tests

# AI-specific validations
poetry run pytest tests/critical_validations.py
```

## 🚀 Deployment Guide

### Local Development
```bash
poetry run adk web            # ADK Dev UI
uvicorn api.main:app --reload # FastAPI backend
pnpm dev                      # Next.js frontend
```

### Production Deployment
```bash
# Validate deployment configuration
gcloud agent-engines deploy --validate-only

# Deploy to Vertex AI Agent Engine
gcloud agent-engines deploy --project=$PROJECT_ID
```

## 🤝 Contributing

This project is designed for AI agents to contribute autonomously. Human contributions should focus on:

1. Updating prompt templates in `.prompts/`
2. Adding new AI-readable documentation in `docs/`
3. Enhancing test coverage for AI-generated code

### Before Committing (AI Checklist)

```markdown
- [ ] Run `scripts/reset_env.sh`
- [ ] All tests pass: `pytest -q && poetry run adk test`
- [ ] No common pitfalls triggered (check `docs/COMMON_PITFALLS.md`)
- [ ] Tool docstrings ≥ 5 lines with Args/Returns
- [ ] State keys use proper prefixes (user:/app:/temp:)
- [ ] Using model ID: "gemini-2.0-flash-exp"
```

## 📚 Documentation

- **For AI Agents**: Start with `docs/README_FOR_AI_CODERS.md`
- **Architecture**: See `docs/PROJECT_ARCHITECTURE.md`
- **ADK Patterns**: Review `docs/ADK_BEST_PRACTICES.md`
- **Supabase Guide**: Check `docs/SUPABASE_PATTERNS.md`

## 🔮 Roadmap

### Sprint 0: Bootstrap ✅
- Project structure
- Environment setup
- CI/CD pipeline

### Sprint 1: Core Agents (Current)
- HomeownerAgent implementation
- BidCard generation
- Messaging MVP

### Sprint 2: Contractor Flow
- OutboundRecruiterAgent
- Contractor matching v1
- Invitation system

### Sprint 3: Bidding System
- ContractorAgent
- Bid submission flow
- Real-time updates

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- Google ADK team for the agent framework
- Supabase for the backend infrastructure
- The future AI agents who will build upon this foundation

---

*"The best code is written by those who never tire, never err, and scale infinitely."* - Built for AI, by AI