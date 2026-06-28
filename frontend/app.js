const API_URL = "http://127.0.0.1:8000/api/chat";
let history = [];

function getTime() {
  return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addBotMessage(text) {
  const messages = document.getElementById("messages");
  const row = document.createElement("div");
  row.className = "msg-row bot";
  row.innerHTML =
    '<div class="avatar-sm">🛒</div>' +
    '<div class="msg-col">' +
      '<div class="bubble bot">' + text + '</div>' +
      '<div class="msg-time">' + getTime() + '</div>' +
    '</div>';
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
  return row;
}

function addUserMessage(text) {
  const messages = document.getElementById("messages");
  const row = document.createElement("div");
  row.className = "msg-row user";
  row.innerHTML =
    '<div class="msg-col">' +
      '<div class="bubble user">' + text + '</div>' +
      '<div class="msg-time">' + getTime() + '</div>' +
    '</div>';
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

function showTyping() {
  const messages = document.getElementById("messages");
  const row = document.createElement("div");
  row.className = "msg-row bot";
  row.innerHTML =
    '<div class="avatar-sm">🛒</div>' +
    '<div class="msg-col">' +
      '<div class="bubble typing">' +
        '<div class="dots"><span></span><span></span><span></span></div>' +
      '</div>' +
    '</div>';
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
  return row;
}

async function sendMessage() {
  const input = document.getElementById("userInput");
  const btn = document.getElementById("sendBtn");
  const question = input.value.trim();
  if (!question) return;

  document.getElementById("chips").style.display = "none";
  addUserMessage(question);
  history.push({ role: "user", content: question });
  input.value = "";
  btn.disabled = true;

  const typingEl = showTyping();

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: question, history: history })
    });
    const data = await res.json();
    typingEl.remove();
    addBotMessage(data.answer);
    history.push({ role: "assistant", content: data.answer });
  } catch (err) {
    typingEl.remove();
    addBotMessage("Sorry, I could not connect. Please try again.");
  } finally {
    btn.disabled = false;
    input.focus();
  }
}

function ask(question) {
  document.getElementById("userInput").value = question;
  sendMessage();
}