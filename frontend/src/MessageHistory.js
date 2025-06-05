import React from 'react';
import './styles/MessageHistory.scss';

function MessageHistory({ history, onSelect }) {
  return (
    <div className="message-history">
      <h3>Chat History</h3>
      <ul>
        {history.map((item, idx) => (
          <li key={idx} onClick={() => onSelect(item)}>
            {item.user?.slice(0, 30)}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MessageHistory;
