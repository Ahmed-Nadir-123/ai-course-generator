#!/usr/bin/env python3
"""
Test script for the AI Course Generator application.
Tests rate limiting, API functionality, and error handling.
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_chat_endpoint():
    """Test the chat endpoint with a simple request"""
    print("🧪 Testing chat endpoint...")
    
    try:
        response = requests.post(f"{BASE_URL}/chat", 
                               json={"message": "Create a basic Python course for beginners"},
                               timeout=30)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print("✅ Chat endpoint working!")
                print(f"Model used: {data.get('model_used', 'Unknown')}")
                print(f"Response length: {len(data.get('response', ''))}")
                print("First 200 chars:", data.get('response', '')[:200] + "...")
                return True
            else:
                print("❌ Chat failed:", data.get('error'))
                return False
        else:
            print(f"❌ HTTP Error {response.status_code}:", response.text)
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

def test_rate_limiting():
    """Test rate limiting behavior"""
    print("\n🧪 Testing rate limiting...")
    
    # Send multiple rapid requests
    for i in range(3):
        print(f"Request {i+1}/3...")
        try:
            response = requests.post(f"{BASE_URL}/chat", 
                                   json={"message": f"Test request {i+1}"},
                                   timeout=15)
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 429:
                print("  ⏱️ Rate limited (expected)")
            elif response.status_code == 200:
                data = response.json()
                print(f"  ✅ Success with model: {data.get('model_used', 'Unknown')}")
            else:
                print(f"  ❌ Error: {response.text}")
                
        except requests.Timeout:
            print("  ⏱️ Request timeout (rate limiting in effect)")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        
        # Small delay between requests
        time.sleep(1)

def test_server_status():
    """Test if server is running"""
    print("🧪 Testing server status...")
    
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
            return True
        else:
            print(f"❌ Server returned {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting AI Course Generator Tests\n")
    
    # Test server status first
    if not test_server_status():
        print("\n❌ Server is not running. Please start the Flask server first.")
        print("Run: python app.py")
        return
    
    # Test basic functionality
    chat_works = test_chat_endpoint()
    
    # Test rate limiting
    test_rate_limiting()
    
    # Summary
    print("\n📊 Test Summary:")
    print(f"Chat endpoint: {'✅ Working' if chat_works else '❌ Failed'}")
    print("\n💡 Tips:")
    print("- If you see 429 errors, rate limiting is working correctly")
    print("- The app will automatically try different models if one fails")
    print("- Check app.log for detailed error information")

if __name__ == "__main__":
    main()
