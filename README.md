# AI Course Generator 🎓

A comprehensive AI-powered course generation application that functions like ChatGPT but specializes in creating detailed educational content. Built with Flask (Python) backend and React frontend, integrated with Google's Gemini AI.

![AI Course Generator](https://img.shields.io/badge/AI-Course%20Generator-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![React](https://img.shields.io/badge/React-18+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-red)
![Gemini AI](https://img.shields.io/badge/Gemini%20AI-2.5%20Pro-purple)

## 🌟 Features

### 🎯 Core Functionality
- **AI-Powered Course Generation**: Creates comprehensive courses using Google's latest Gemini 2.5 Pro AI model
- **Real-time Chat Interface**: ChatGPT-like interface for interactive course creation
- **Multi-format Export**: Generate downloadable PowerPoint presentations and PDF documents
- **Smart Rate Limiting**: Automatic fallback to multiple AI models with retry logic
- **Course History**: Persistent chat history and session management

### 🚀 Advanced Features
- **Professional Course Structure**: 
  - Detailed learning objectives
  - Week-by-week timelines
  - Hands-on exercises and projects
  - Assessment criteria and rubrics
  - Industry resources and tools
- **File Management**: Upload, download, and manage generated course materials
- **Error Handling**: Comprehensive error handling with user-friendly feedback
- **Responsive Design**: Modern, mobile-friendly interface

## 🛠 Technology Stack

### Backend
- **Flask**: Python web framework
- **Google Gemini AI**: Advanced AI model for content generation
- **python-pptx**: PowerPoint generation
- **ReportLab**: PDF generation
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **React**: Modern JavaScript library
- **Axios**: HTTP client for API communication
- **React Markdown**: Markdown rendering
- **SCSS**: Advanced styling

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- Google AI API key (Gemini)
- Git (for cloning and version control)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Ahmed-Nadir-123/ai-course-generator.git
cd ai-course-generator
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install flask flask-cors google-generativeai python-pptx reportlab

# Set up environment variables
# Create a .env file in the root directory
echo "GOOGLE_API_KEY=your_gemini_api_key_here" > .env

# Start the Flask backend
python app.py
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start the React development server
npm start
```

### 4. Access the Application
- **Frontend**: http://localhost:3000 (or http://localhost:3001 if 3000 is occupied)
- **Backend API**: http://localhost:5000

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here  # Alternative key name
PORT=5000
DEBUG=True
```

### AI Model Configuration
The application uses multiple AI models with automatic fallback:
1. **Gemini 2.5 Pro Preview** (Primary - Most capable)
2. **Gemini 2.0 Flash Experimental** (Secondary)
3. **Gemini 2.0 Flash** (Stable fallback)
4. **Gemini 1.5 Pro Latest** (Backup)
5. **Gemini 1.5 Flash** (Final fallback)

## 📚 How to Use

### Creating a Course
1. **Start a Conversation**: Type what you want to learn (e.g., "Python programming for beginners")
2. **Review Generated Course**: The AI will create a comprehensive course with modules, objectives, and timeline
3. **Generate Files**: Ask for PowerPoint or PDF versions of your course
4. **Download Materials**: Use the download links to get your course files

### Example Prompts
- "Create a machine learning course for data scientists"
- "Design a web development bootcamp curriculum"
- "Generate a cybersecurity awareness training program"
- "Build a digital marketing course for small businesses"

### File Generation
```bash
# Generate PowerPoint
"Generate PowerPoint for this course"

# Generate PDF
"Create PDF for this course"

# Custom requests
"Make a presentation focusing on hands-on exercises"
```

## 🏗 Project Structure

```
ai-course-generator/
├── app.py                 # Main Flask backend
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
├── generated_files/      # Generated course files
├── frontend/
│   ├── package.json      # Node.js dependencies
│   ├── public/
│   │   └── index.html    # HTML template
│   └── src/
│       ├── App.js        # Main React component
│       ├── ChatInterface.js  # Chat interface
│       ├── CourseDisplay.js  # Course content display
│       ├── MessageHistory.js # Chat history
│       ├── api.js        # API service
│       └── styles/       # SCSS stylesheets
├── demo.py              # Demo script
├── test_backend.py      # Backend tests
└── README.md           # This file
```

## 🔗 API Endpoints

### Chat
- `POST /chat` - Generate course content
- `GET /` - Health check

### File Generation
- `POST /generate_ppt` - Create PowerPoint presentation
- `POST /generate_pdf` - Create PDF document
- `GET /download/<filename>` - Download generated files
- `GET /files` - List all generated files

### Example API Usage
```javascript
// Generate course
const response = await fetch('http://localhost:5000/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'Create a Python course' })
});

// Generate PowerPoint
const pptResponse = await fetch('http://localhost:5000/generate_ppt', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ course_content: courseText })
});
```

## 🧪 Testing

### Backend Tests
```bash
python test_backend.py
```

### Demo Script
```bash
python demo.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡 Security

- Never commit your API keys to the repository
- Use environment variables for sensitive configuration
- The `.env` file is included in `.gitignore` for security

## 🚨 Troubleshooting

### Common Issues

**Backend won't start:**
- Check if all Python dependencies are installed
- Verify your Google AI API key is set correctly
- Ensure port 5000 is not in use

**Frontend build errors:**
- Make sure Node.js dependencies are installed (`npm install`)
- Check for SCSS compilation errors
- Verify the backend is running on port 5000

**AI API errors:**
- Verify your Gemini API key is valid and has quota
- The app automatically falls back to different models if quota is exceeded
- Check the console for specific error messages

### Getting Help
- Check the [Issues](https://github.com/Ahmed-Nadir-123/ai-course-generator/issues) page
- Review the troubleshooting section above
- Ensure all prerequisites are met

## 🎯 Future Enhancements

- [ ] User authentication and personalized courses
- [ ] Course templates and customization
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Multi-language support
- [ ] Advanced analytics and progress tracking
- [ ] Collaborative course creation
- [ ] Video content generation integration

## 👨‍💻 Author

**Your Name**
- GitHub: [@Ahmed-Nadir-123](https://github.com/Ahmed-Nadir-123)
- Email: ahmednader2003331@gmail.com

## 🙏 Acknowledgments

- Google AI for providing the Gemini API
- React team for the amazing frontend framework
- Flask community for the robust backend framework
- All contributors and users of this project

---

**⭐ If you found this project helpful, please give it a star!**
