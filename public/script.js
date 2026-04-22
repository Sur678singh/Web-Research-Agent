// API configuration
const API_URL = 'https://web-research-agent-eabm.onrender.com/ask';

// Get DOM elements
const chatBox = document.getElementById('chatBox');
const questionInput = document.getElementById('questionInput');
const questionForm = document.getElementById('questionForm');
const sendBtn = document.getElementById('sendBtn');

// Auto-scroll chat to bottom
function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Add message to chat
function addMessage(text, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    const p = document.createElement('p');
    p.textContent = text;
    
    messageDiv.appendChild(p);
    chatBox.appendChild(messageDiv);
    scrollToBottom();
}

// Show loading indicator
function showLoading() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    messageDiv.id = 'loadingIndicator';
    
    const loading = document.createElement('div');
    loading.className = 'loading';
    loading.innerHTML = `
        <span>Thinking</span>
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    `;
    
    messageDiv.appendChild(loading);
    chatBox.appendChild(messageDiv);
    scrollToBottom();
}

// Remove loading indicator
function removeLoading() {
    const loadingIndicator = document.getElementById('loadingIndicator');
    if (loadingIndicator) {
        loadingIndicator.remove();
    }
}

// Send question to backend
async function sendQuestion(question) {
    // Add user message to chat
    addMessage(question, true);
    questionInput.value = '';
    sendBtn.disabled = true;
    
    // Show loading
    showLoading();
    
    try {
        // Call backend API
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Response:", data);
        removeLoading();
        
        // Add bot response
        const answer = data.answer || 'No response received';
        addMessage(answer, false);
        
    } catch (error) {
        removeLoading();
        console.error('Error:', error);
        addMessage(`Sorry, I encountered an error: ${error.message}. Make sure the backend server is running.`, false);
    } finally {
        sendBtn.disabled = false;
        questionInput.focus();
    }
}

// Handle form submission
questionForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const question = questionInput.value.trim();
    if (question) {
        sendQuestion(question);
    }
});

// Focus input on page load
window.addEventListener('load', () => {
    questionInput.focus();
});

// Optional: Allow sending with Enter key (already works via form submission)
questionInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        questionForm.dispatchEvent(new Event('submit'));
    }
});
