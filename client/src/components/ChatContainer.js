import React from 'react';
import ChatMessage from './ChatMessage';

const ChatContainer = ({ messageHistory }) => (
  <div className="chat-container">
    {messageHistory.map((message, index) => (
      <ChatMessage key={index} type={message.type} text={message.text} />
    ))}
  </div>
);

export default ChatContainer;
