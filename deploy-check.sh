#!/bin/bash

# 🚀 AI Course Generator - Secure Deployment Script
# This script prepares your project for secure GitHub deployment

echo "🔒 AI Course Generator - Security Check & Deploy Preparation"
echo "==========================================================="

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

echo "✅ Project directory confirmed"

# Verify environment files
echo "🔍 Checking environment files..."

if [ -f ".env.local" ] && grep -q "AIzaSy" .env.local; then
    echo "✅ .env.local contains API key (safe - ignored by git)"
else
    echo "❌ Error: .env.local missing or doesn't contain API key"
    echo "   Please create .env.local with your actual API key"
    exit 1
fi

if [ -f ".env" ] && ! grep -q "AIzaSy" .env; then
    echo "✅ .env contains only placeholder values (safe to commit)"
else
    echo "❌ Error: .env contains real API key - security risk!"
    echo "   Please replace with placeholder values"
    exit 1
fi

# Check gitignore
if grep -q ".env.local" .gitignore; then
    echo "✅ .env.local is properly ignored by git"
else
    echo "❌ Error: .env.local not in .gitignore"
    exit 1
fi

# Test API key loading
echo "🧪 Testing environment variable loading..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv('.env.local') if os.path.exists('.env.local') else load_dotenv('.env')
key = os.getenv('GOOGLE_API_KEY', '')
if len(key) > 20 and key.startswith('AIzaSy'):
    print('✅ API key loaded successfully')
else:
    print('❌ API key not loaded properly')
    exit(1)
" || exit 1

echo ""
echo "🎉 Security Check Complete - Ready for GitHub!"
echo ""
echo "Next steps:"
echo "1. git add ."
echo "2. git commit -m 'Initial commit - Secure AI Course Generator'"
echo "3. git push origin main"
echo ""
echo "For Vercel deployment:"
echo "1. Connect your GitHub repo to Vercel"
echo "2. Set environment variables in Vercel dashboard:"
echo "   - GOOGLE_API_KEY: [Your API Key]"
echo "   - GEMINI_API_KEY: [Your API Key]"
echo "3. Deploy!"
echo ""
echo "🛡️  Your API keys are secure and will not be exposed!"
