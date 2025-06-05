# 🚀 AI Course Generator - Complete Setup Guide

This guide will help you set up the AI Course Generator application from scratch.

## 📋 Prerequisites

- **Python 3.8+** installed on your system
- **Node.js 16+** and npm installed
- **Google AI API Key** (get from [Google AI Studio](https://makersuite.google.com/app/apikey))
- **Git** installed for version control

## 🔧 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-course-generator.git
cd ai-course-generator
```

### 2. Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Create local environment file with your API key
cp .env.example .env.local
```

**Edit `.env.local` and add your API key:**
```
GOOGLE_API_KEY=your_actual_api_key_here
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Frontend Setup

```bash
cd frontend
npm install
cd ..
```

### 4. Start the Application

**Terminal 1 - Backend:**
```bash
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### 5. Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000

## 🔐 Security Configuration

### Environment Variables

**NEVER commit your actual API key to git!**

- `.env` - Contains placeholder values (safe to commit)
- `.env.local` - Contains your real API key (ignored by git)
- `.env.example` - Template for other developers

### File Structure After Setup

```
ai-course-generator/
├── .env                 # Placeholder values (committed)
├── .env.local          # Your API key (ignored by git)
├── .env.example        # Template (committed)
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── frontend/           # React frontend
│   ├── src/
│   ├── package.json
│   └── ...
└── ...
```

## 🧪 Testing Your Setup

### Quick Test

1. Start both backend and frontend
2. Open http://localhost:3000
3. Type: "Create a course about Python programming"
4. Verify course generation works
5. Test PowerPoint and PDF download buttons

### Run Test Scripts

```bash
# Test backend functionality
python test_backend.py

# Run comprehensive demo
python demo.py
```

## 🚨 Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
pip install -r requirements.txt
```

**API key errors:**
- Verify your API key is correct in `.env.local`
- Check if your Google AI API has quota remaining
- Ensure the API key has proper permissions

**Port already in use:**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :5000   # Windows
```

**Frontend build errors:**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Getting Help

1. Check the [main README.md](README.md) for detailed documentation
2. Review the [Issues page](https://github.com/yourusername/ai-course-generator/issues)
3. Ensure all prerequisites are properly installed

## 🎯 Next Steps

Once everything is working:

1. **Customize the UI** - Modify components in `frontend/src/`
2. **Enhance AI Prompts** - Edit prompt engineering in `app.py`
3. **Add Features** - Extend the API with new endpoints
4. **Deploy** - Follow the deployment guide in README.md

## 📚 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs/)
- [Google AI Documentation](https://ai.google.dev/docs)
- [Gemini API Guide](https://ai.google.dev/api/rest)

---

**🎉 Congratulations! Your AI Course Generator is now ready to use!**
