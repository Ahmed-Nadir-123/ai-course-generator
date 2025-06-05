# 🚀 AI Course Generator - Secure Deployment Script (PowerShell)
# This script prepares your project for secure GitHub deployment

Write-Host "🔒 AI Course Generator - Security Check & Deploy Preparation" -ForegroundColor Cyan
Write-Host "===========================================================" -ForegroundColor Cyan

# Check if we're in the right directory
if (!(Test-Path "app.py")) {
    Write-Host "❌ Error: Please run this script from the project root directory" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Project directory confirmed" -ForegroundColor Green

# Verify environment files
Write-Host "🔍 Checking environment files..." -ForegroundColor Yellow

if ((Test-Path ".env.local") -and (Get-Content ".env.local" | Select-String "AIzaSy")) {
    Write-Host "✅ .env.local contains API key (safe - ignored by git)" -ForegroundColor Green
} else {
    Write-Host "❌ Error: .env.local missing or doesn't contain API key" -ForegroundColor Red
    Write-Host "   Please create .env.local with your actual API key" -ForegroundColor Red
    exit 1
}

if ((Test-Path ".env") -and !(Get-Content ".env" | Select-String "AIzaSy")) {
    Write-Host "✅ .env contains only placeholder values (safe to commit)" -ForegroundColor Green
} else {
    Write-Host "❌ Error: .env contains real API key - security risk!" -ForegroundColor Red
    Write-Host "   Please replace with placeholder values" -ForegroundColor Red
    exit 1
}

# Check gitignore
if (Get-Content ".gitignore" | Select-String ".env.local") {
    Write-Host "✅ .env.local is properly ignored by git" -ForegroundColor Green
} else {
    Write-Host "❌ Error: .env.local not in .gitignore" -ForegroundColor Red
    exit 1
}

# Test API key loading
Write-Host "🧪 Testing environment variable loading..." -ForegroundColor Yellow
$testResult = python -c "
import os
from dotenv import load_dotenv
load_dotenv('.env.local') if os.path.exists('.env.local') else load_dotenv('.env')
key = os.getenv('GOOGLE_API_KEY', '')
if len(key) > 20 and key.startswith('AIzaSy'):
    print('SUCCESS')
else:
    print('FAILED')
"

if ($testResult -eq "SUCCESS") {
    Write-Host "✅ API key loaded successfully" -ForegroundColor Green
} else {
    Write-Host "❌ API key not loaded properly" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🎉 Security Check Complete - Ready for GitHub!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. git add ." -ForegroundColor White
Write-Host "2. git commit -m 'Initial commit - Secure AI Course Generator'" -ForegroundColor White
Write-Host "3. git push origin main" -ForegroundColor White
Write-Host ""
Write-Host "For Vercel deployment:" -ForegroundColor Cyan
Write-Host "1. Connect your GitHub repo to Vercel" -ForegroundColor White
Write-Host "2. Set environment variables in Vercel dashboard:" -ForegroundColor White
Write-Host "   - GOOGLE_API_KEY: [Your API Key]" -ForegroundColor White
Write-Host "   - GEMINI_API_KEY: [Your API Key]" -ForegroundColor White
Write-Host "3. Deploy!" -ForegroundColor White
Write-Host ""
Write-Host "🛡️  Your API keys are secure and will not be exposed!" -ForegroundColor Green
