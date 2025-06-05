#!/usr/bin/env python3
"""
Demo script for the AI Course Generator application.
Demonstrates the complete workflow from course generation to file downloads.
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def demo_course_generation():
    """Demo the course generation functionality"""
    print("🎓 AI Course Generator Demo")
    print("=" * 50)
    
    # Test course requests
    test_topics = [
        "Machine Learning fundamentals for beginners",
        "Web Development with React and Node.js",
        "Data Science with Python"
    ]
    
    for i, topic in enumerate(test_topics, 1):
        print(f"\n📚 Demo {i}: Generating course on '{topic}'")
        print("-" * 40)
        
        try:
            start_time = time.time()
            response = requests.post(f"{BASE_URL}/chat", 
                                   json={"message": f"Create a comprehensive course on {topic}"},
                                   timeout=60)
            
            elapsed_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print(f"✅ Course generated successfully!")
                    print(f"⏱️  Generation time: {elapsed_time:.2f} seconds")
                    print(f"🤖 Model used: {data.get('model_used', 'Unknown')}")
                    print(f"📝 Content length: {len(data.get('response', ''))} characters")
                    print(f"📋 Preview: {data.get('response', '')[:200]}...")
                    
                    # Test file generation
                    test_file_generation(data.get('response', ''), f"demo_{i}")
                    
                else:
                    print(f"❌ Generation failed: {data.get('error')}")
                    if data.get('suggestion'):
                        print(f"💡 Suggestion: {data.get('suggestion')}")
            else:
                print(f"❌ HTTP Error {response.status_code}: {response.text}")
                
        except requests.Timeout:
            print("⏱️ Request timed out - this is normal for long course generation")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Wait between requests to respect rate limiting
        print("⏳ Waiting 5 seconds to respect rate limits...")
        time.sleep(5)

def test_file_generation(course_content, demo_name):
    """Test PowerPoint and PDF generation"""
    print(f"\n📄 Testing file generation for {demo_name}...")
    
    # Test PowerPoint generation
    try:
        response = requests.post(f"{BASE_URL}/generate_ppt", 
                               json={"course_content": course_content})
        if response.status_code == 200:
            data = response.json()
            print(f"📊 PowerPoint generated: {data.get('download_url')}")
        else:
            print(f"❌ PowerPoint generation failed: {response.text}")
    except Exception as e:
        print(f"❌ PowerPoint error: {e}")
    
    # Test PDF generation
    try:
        response = requests.post(f"{BASE_URL}/generate_pdf", 
                               json={"course_content": course_content})
        if response.status_code == 200:
            data = response.json()
            print(f"📄 PDF generated: {data.get('download_url')}")
        else:
            print(f"❌ PDF generation failed: {response.text}")
    except Exception as e:
        print(f"❌ PDF error: {e}")

def show_usage_tips():
    """Show usage tips for the application"""
    print("\n💡 Usage Tips:")
    print("=" * 50)
    print("1. 🌐 Frontend: http://localhost:3000")
    print("2. 🔗 Backend API: http://localhost:5000")
    print("3. 📝 Try these example prompts:")
    print("   • 'Create a Python programming course for beginners'")
    print("   • 'Design a machine learning fundamentals course'")
    print("   • 'Build a web development course with HTML, CSS, and JavaScript'")
    print("4. ⚡ Features:")
    print("   • Real-time chat interface")
    print("   • Automatic rate limiting")
    print("   • Multiple AI model fallbacks")
    print("   • PowerPoint and PDF generation")
    print("   • File downloads")
    print("5. 🔧 Technical details:")
    print("   • Uses Gemini 1.5 Flash for efficiency")
    print("   • Rate limited to respect API quotas")
    print("   • Fallback to multiple models if needed")
    print("   • Structured course content generation")

def main():
    """Run the demo"""
    print("🚀 Starting AI Course Generator Demo\n")
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code != 200:
            print("❌ Server is not responding properly")
            return
    except Exception:
        print("❌ Cannot connect to server. Please ensure both backend and frontend are running:")
        print("   Backend: python app.py")
        print("   Frontend: cd frontend && npm start")
        return
    
    print("✅ Server is running!")
    
    # Run demos
    demo_course_generation()
    show_usage_tips()
    
    print("\n🎉 Demo completed!")
    print("Open http://localhost:3000 to use the web interface")

if __name__ == "__main__":
    main()
