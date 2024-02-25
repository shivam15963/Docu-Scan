import React, { useState } from 'react';
import './App.css';
import ChatContainer from './components/ChatContainer';
import MessageInput from './components/MessageInput';

function App() {
  const [userMessage, setUserMessage] = useState('');
  const [messageHistory, setMessageHistory] = useState([]);

  const sendMessage = async () => {
    if (userMessage.trim() === '') {
      return;
    }

    setMessageHistory([...messageHistory, { type: 'user', text: userMessage }]);
    
    // Simulate API call with a delay (replace this with your actual API call)
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();

    setMessageHistory((prevHistory) => [
      ...prevHistory,
      { type: 'bot', text: data.message },
    ]);

    setUserMessage('');
  };

  const clearChat = () => {
    setMessageHistory([]);
  };

  return (
    <div className="App">
      <h1>Docu Scan</h1>
      <h2>A sample Application that scans documents to extract answers.</h2>
      <ChatContainer messageHistory={messageHistory} />
      <MessageInput
        value={userMessage}
        onChange={setUserMessage}
        onSendMessage={sendMessage}
        onClearChat={clearChat}
      />
    </div>
  );
}

export default App;
