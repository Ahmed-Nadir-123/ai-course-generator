# Vercel Deployment Guide

## Prerequisites
1. Vercel account (free)
2. GitHub repository
3. Google AI API key

## Deployment Steps

### 1. Connect Repository to Vercel
1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "New Project"
4. Import your `ai-course-generator` repository
5. Vercel will auto-detect the framework

### 2. Configure Environment Variables
In Vercel dashboard:
1. Go to Project Settings → Environment Variables
2. Add these variables:
   - `GOOGLE_API_KEY` = your_actual_gemini_api_key
   - `GEMINI_API_KEY` = your_actual_gemini_api_key

### 3. Deploy
1. Click "Deploy"
2. Vercel will build and deploy automatically
3. You'll get a live URL like: `https://ai-course-generator-xyz.vercel.app`

## Configuration Files Already Set Up

### vercel.json ✅
- Python backend configured
- React frontend configured
- Environment variables mapped
- Routing configured

### Build Configuration ✅
- Backend: Python app.py
- Frontend: React build process
- Static file serving

## Post-Deployment
- Backend API: `https://your-app.vercel.app/api/*`
- Frontend: `https://your-app.vercel.app/`
- File downloads: `https://your-app.vercel.app/api/download/*`

## Troubleshooting
- Check Vercel function logs for errors
- Verify environment variables are set
- Ensure API quotas are sufficient
