from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

# Import your existing MVP logic
from src.router import analyze_conversation_frame
from src.guardrails import check_compliance_violation
from src.mentor_voice import generate_mentor_reply

app = FastAPI()

# Data models for receiving web requests
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    chat_history: List[Message]
    user_input: str

# 1. Serve the Web UI Interface
@app.get("/")
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TradeVed Co-Pilot MVP</title>
        <style>
            body { font-family: -apple-system, sans-serif; max-width: 700px; margin: 40px auto; padding: 20px; background: #f4f4f9; }
            #chatbox { height: 500px; background: white; border: 1px solid #ccc; border-radius: 8px; overflow-y: auto; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .user-msg { color: #2c3e50; background: #e3f2fd; padding: 10px; border-radius: 8px; margin: 10px 0; max-width: 80%; margin-left: auto; }
            .mentor-msg { color: #27ae60; background: #eafeea; padding: 10px; border-radius: 8px; margin: 10px 0; max-width: 80%; }
            .controls { display: flex; gap: 10px; }
            input[type="text"] { flex-grow: 1; padding: 12px; border: 1px solid #ccc; border-radius: 5px; font-size: 16px; }
            button { padding: 12px 24px; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background: #1a252f; }
        </style>
    </head>
    <body>
        <h2>TradeVed AI Mentor Terminal</h2>
        <div id="chatbox">
            <div class="mentor-msg"><b>System:</b> Tradeved AI Mentor Co-Pilot Activated. How can I help your trading today?</div>
        </div>
        <div class="controls">
            <input type="text" id="userInput" placeholder="Type your message..." onkeypress="if(event.key === 'Enter') sendMessage()">
            <button onclick="sendMessage()" id="sendBtn">Send</button>
        </div>

        <script>
            let chatHistory = [];
            async function sendMessage() {
                const input = document.getElementById("userInput");
                const btn = document.getElementById("sendBtn");
                const text = input.value;
                if (!text) return;
                
                const chatbox = document.getElementById("chatbox");
                chatbox.innerHTML += `<div class="user-msg"><b>You:</b> ${text}</div>`;
                input.value = "";
                input.disabled = true;
                btn.innerText = "Thinking...";
                chatbox.scrollTop = chatbox.scrollHeight;
                
                try {
                    const response = await fetch("/api/chat", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ chat_history: chatHistory, user_input: text })
                    });
                    
                    const data = await response.json();
                    chatbox.innerHTML += `<div class="mentor-msg"><b>Mentor:</b> ${data.mentor_reply}</div>`;
                    
                    chatHistory.push({ role: "user", content: text });
                    chatHistory.push({ role: "assistant", content: data.mentor_reply });
                } catch(e) {
                    chatbox.innerHTML += `<div class="mentor-msg" style="color:red;"><b>Error:</b> Connection failed.</div>`;
                }
                
                input.disabled = false;
                btn.innerText = "Send";
                input.focus();
                chatbox.scrollTop = chatbox.scrollHeight;
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# 2. The AI Generation Endpoint
@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    # Reconstruct history
    history = [{"role": msg.role, "content": msg.content} for msg in request.chat_history]
    user_input = request.user_input
    history.append({"role": "user", "content": user_input})
    
    # Format history string for the router
    formatted_history = "\n".join([f"{m['role']}: {m['content']}" for m in history[-4:]])
    
    # Run MVP Pipeline
    evaluation = analyze_conversation_frame(formatted_history)
    guard_check = check_compliance_violation(evaluation)
    
    if guard_check["violation"]:
        reply = guard_check["fallback_response"]
    else:
        reply = generate_mentor_reply(history, evaluation)
        
    return {"mentor_reply": reply}