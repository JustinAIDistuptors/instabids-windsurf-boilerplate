#!/bin/bash
# Reset script for Unix/Linux/macOS environments
# Prevents "ghost Git wheel" issues and ensures clean environment

echo "🧹 Resetting InstaBids development environment..."

# Clear Poetry cache
echo "📦 Clearing Poetry cache..."
poetry cache clear pypi --all 2>/dev/null || echo "Poetry cache already clean"

# Remove virtual environment
echo "🗑️  Removing virtual environment..."
rm -rf .venv

# Clear ADK model cache
echo "🤖 Clearing ADK model cache..."
rm -rf ~/.cache/adk/model_catalog.json 2>/dev/null || echo "ADK cache already clean"

# Regenerate lock file and install
echo "🔄 Regenerating Poetry lock file..."
poetry lock --no-update

# Install dependencies
echo "📥 Installing Python dependencies..."
poetry install --sync

# Install Node dependencies
echo "📥 Installing Node dependencies..."
pnpm install

# Create necessary directories
echo "📁 Creating directory structure..."
mkdir -p src/instabids/{agents,api,data,tools}
mkdir -p src/frontend/{components,pages,styles}
mkdir -p tests/{unit,integration,e2e}
mkdir -p docs
mkdir -p db/migrations

# Set executable permissions
chmod +x scripts/*.sh 2>/dev/null || true

echo "✅ Environment reset complete!"
echo ""
echo "Next steps:"
echo "  1. Copy .env.template to .env and fill in your API keys"
echo "  2. Run 'supabase start' to start local Supabase"
echo "  3. Run 'poetry run adk web' to start ADK Dev UI"
echo "  4. Run 'pnpm dev' to start Next.js frontend"