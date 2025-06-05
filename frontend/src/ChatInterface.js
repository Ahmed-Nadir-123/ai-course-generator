import React, { useState, useRef } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './styles/ChatInterface.scss';

function ChatInterface({ setHistory }) {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [rateLimitInfo, setRateLimitInfo] = useState(null);
  const inputRef = useRef();

  const sendMessage = async () => {
    if (!input.trim()) return;
    setLoading(true);
    setRateLimitInfo(null);
    
    const userMessage = input;
    setMessages((prev) => [...prev, { user: userMessage }]);
    setInput('');
    
    try {
      const res = await axios.post('http://localhost:5000/chat', { message: userMessage });
      
      if (res.data.success) {
        const aiResponse = res.data.response;
        setMessages((prev) => [...prev, { ai: aiResponse }]);
        setHistory((prev) => [...prev, { user: userMessage, ai: aiResponse }]);
        
        // Show model info if available
        if (res.data.model_used) {
          setRateLimitInfo(`Response generated using ${res.data.model_used}`);
        }
      } else {
        // Handle API errors with suggestions
        let errorMessage = res.data.error || 'Error: Could not get response.';
        if (res.data.suggestion) {
          errorMessage += `\n\n💡 ${res.data.suggestion}`;
        }
        setMessages((prev) => [...prev, { ai: errorMessage, isError: true }]);
        
        // Show rate limit info
        if (res.data.error.includes('quota') || res.data.error.includes('rate limit')) {
          setRateLimitInfo('Rate limit reached. Trying again in a few moments...');
        }
      }
      
    } catch (err) {
      console.error('Chat error:', err);
      let errorMessage = 'Error: Could not connect to the server.';
      
      if (err.response) {
        if (err.response.status === 429) {
          errorMessage = 'Rate limit exceeded. Please wait a moment before trying again.';
          setRateLimitInfo('⏱️ Rate limit active - requests are being throttled to comply with API limits');
        } else if (err.response.data?.error) {
          errorMessage = err.response.data.error;
        }
      }
      
      setMessages((prev) => [...prev, { ai: errorMessage, isError: true }]);
    }
    
    setLoading(false);
    inputRef.current?.focus();
  };

  return (
    <div className="chat-interface">
      {rateLimitInfo && (
        <div className="rate-limit-info">
          ℹ️ {rateLimitInfo}
        </div>
      )}
      
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={`${msg.user ? 'user-msg' : 'ai-msg'} ${msg.isError ? 'error-msg' : ''}`}>
            <ReactMarkdown>{msg.user || msg.ai}</ReactMarkdown>
          </div>
        ))}
        {loading && (
          <div className="ai-msg loading">
            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
            AI is generating your course...
          </div>
        )}
      </div>
      
      <div className="input-area">
        <input
          ref={inputRef}
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && !loading && sendMessage()}
          placeholder="What do you want to learn? (e.g., 'Python programming', 'Machine Learning basics')"
          disabled={loading}
        />        <button onClick={sendMessage} disabled={loading || !input.trim()}>
          {loading ? 'Generating...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default ChatInterface;
