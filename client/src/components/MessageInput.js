import React from 'react';

function MessageInput({ value, onChange, onSendMessage, onClearChat }) {
  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      onSendMessage();
    }
  };

  return (
    <div className="message-input-container">
      <input
        type="text"
        placeholder="Type your message..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyPress={handleKeyPress}
      />
      <button onClick={onSendMessage}>Send</button>
      <button onClick={onClearChat}>Clear</button>
    </div>
  );
}

export default MessageInput;