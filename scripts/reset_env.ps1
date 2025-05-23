# Reset script for Windows environments
# Prevents "ghost Git wheel" issues and ensures clean environment

Write-Host "🧹 Resetting InstaBids development environment..." -ForegroundColor Green

# Clear Poetry cache
Write-Host "📦 Clearing Poetry cache..." -ForegroundColor Yellow
try {
    poetry cache clear pypi --all 2>$null
} catch {
    Write-Host "Poetry cache already clean" -ForegroundColor Gray
}

# Remove virtual environment
Write-Host "🗑️  Removing virtual environment..." -ForegroundColor Yellow
if (Test-Path .venv) {
    Remove-Item -Recurse -Force .venv
}

# Clear ADK model cache
Write-Host "🤖 Clearing ADK model cache..." -ForegroundColor Yellow
$adkCache = Join-Path $env:USERPROFILE ".cache\adk\model_catalog.json"
if (Test-Path $adkCache) {
    Remove-Item $adkCache -ErrorAction SilentlyContinue
}

# Regenerate lock file and install
Write-Host "🔄 Regenerating Poetry lock file..." -ForegroundColor Yellow
poetry lock --no-update

# Install dependencies
Write-Host "📥 Installing Python dependencies..." -ForegroundColor Yellow
poetry install --sync

# Install Node dependencies
Write-Host "📥 Installing Node dependencies..." -ForegroundColor Yellow
pnpm install

# Create necessary directories
Write-Host "📁 Creating directory structure..." -ForegroundColor Yellow
$directories = @(
    "src\instabids\agents",
    "src\instabids\api",
    "src\instabids\data",
    "src\instabids\tools",
    "src\frontend\components",
    "src\frontend\pages",
    "src\frontend\styles",
    "tests\unit",
    "tests\integration",
    "tests\e2e",
    "docs",
    "db\migrations"
)

foreach ($dir in $directories) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

Write-Host "✅ Environment reset complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Copy .env.template to .env and fill in your API keys"
Write-Host "  2. Run 'supabase start' to start local Supabase"
Write-Host "  3. Run 'poetry run adk web' to start ADK Dev UI"
Write-Host "  4. Run 'pnpm dev' to start Next.js frontend"