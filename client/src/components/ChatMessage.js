import React from 'react';

const ChatMessage = ({ type, text }) => (
  <div className={`message ${type === 'user' ? 'user-message' : 'bot-message'}`}>
    <div className="bubble">
      <strong>{type === 'user' ? 'You:' : 'Docu Scan:'}</strong> {text}
    </div>
  </div>
);

export default ChatMessage;
