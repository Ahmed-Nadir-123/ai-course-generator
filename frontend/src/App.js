import React, { useState } from 'react';
import ChatInterface from './ChatInterface';
import CourseDisplay from './CourseDisplay';
import MessageHistory from './MessageHistory';
import './styles/App.scss';

function App() {
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [history, setHistory] = useState([]);

  return (
    <div className="app-container">
      <aside className="sidebar">
        <MessageHistory history={history} onSelect={setSelectedCourse} />
      </aside>
      <main className="main-content">
        <ChatInterface setHistory={setHistory} />
        {selectedCourse && <CourseDisplay course={selectedCourse} />}
      </main>
    </div>
  );
}

export default App;
