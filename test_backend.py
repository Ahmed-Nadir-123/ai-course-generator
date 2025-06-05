import requests
import json

# Test the backend API endpoints
BASE_URL = "http://localhost:5000"

def test_backend():
    print("Testing AI Course Generator Backend...")
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✓ Server status: {response.json()}")
    except Exception as e:
        print(f"✗ Server connection failed: {e}")
        return
    
    # Test 2: Test chat endpoint with dummy data (no API key required)
    test_message = "Create a course on Python programming for beginners"
    try:
        response = requests.post(f"{BASE_URL}/chat", 
                               json={"message": test_message, "session_id": "test"},
                               timeout=30)
        if response.status_code == 200:
            print("✓ Chat endpoint working")
            content = response.json().get("response", "")
            print(f"Response preview: {content[:200]}...")
        else:
            print(f"✗ Chat endpoint error: {response.json()}")
    except Exception as e:
        print(f"✗ Chat test failed: {e}")
    
    # Test 3: Test file generation endpoints
    test_content = "# Course: Python Basics\n\n## Module 1: Introduction\n- Variables\n- Data types\n\n## Module 2: Control Flow\n- Loops\n- Conditionals"
    
    try:
        # Test PDF generation
        response = requests.post(f"{BASE_URL}/generate_pdf", 
                               json={"course_content": test_content})
        if response.status_code == 200:
            print("✓ PDF generation working")
            print(f"PDF info: {response.json()}")
        else:
            print(f"✗ PDF generation failed: {response.json()}")
    except Exception as e:
        print(f"✗ PDF test failed: {e}")
    
    try:
        # Test PowerPoint generation
        response = requests.post(f"{BASE_URL}/generate_ppt", 
                               json={"course_content": test_content})
        if response.status_code == 200:
            print("✓ PowerPoint generation working")
            print(f"PPT info: {response.json()}")
        else:
            print(f"✗ PowerPoint generation failed: {response.json()}")
    except Exception as e:
        print(f"✗ PowerPoint test failed: {e}")
    
    # Test 4: List files
    try:
        response = requests.get(f"{BASE_URL}/files")
        if response.status_code == 200:
            files = response.json()
            print(f"✓ Files endpoint working - {len(files)} files found")
        else:
            print(f"✗ Files endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Files test failed: {e}")

if __name__ == "__main__":
    test_backend()
