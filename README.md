# FAQ Chatbot — AI Customer Support Assistant

An intelligent e-commerce customer support chatbot built with FastAPI, Groq AI, and vanilla JavaScript. Users ask natural language questions and get instant answers from a curated FAQ dataset.

## Features

- Natural language question answering
- Conversation history and follow-up questions
- 79 real e-commerce FAQ pairs
- Animated typing indicator
- Clean modern chat UI
- Fast responses via Groq LLaMA 3.1

## Tech Stack

- **Backend** — Python, FastAPI
- **AI Model** — Groq API, LLaMA 3.1 8B Instant
- **Frontend** — HTML, CSS, JavaScript
- **Dataset** — Kaggle Ecommerce FAQ Chatbot Dataset

## Project Structure

faq-chatbot/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── Ecommerce_FAQ_Chatbot_dataset.json
│   ├── services/
│   │   └── chat.py
│   └── frontend/
│       ├── index.html
│       ├── style.css
│       └── app.js

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot/backend
```

**2. Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Copy `.env.example` to `.env` and add your Groq API key:

Get a free key at console.groq.com

**5. Run**
```bash
uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000` in your browser.

## How It Works

1. User types a question in the chat UI
2. Frontend sends the question and conversation history to FastAPI
3. Backend loads the FAQ dataset and sends it to Groq AI
4. LLaMA 3.1 finds the best answer from the FAQs
5. Answer is displayed in the chat

## Sample Questions

- How can I create an account?
- What payment methods do you accept?
- How do I track my order?
- What is your return policy?
- Can I order without logging in?
- How long does shipping take?

## Environment Variables

| Variable | Description |
|----------|-------------|
| GROQ_API_KEY | Your Groq API key from console.groq.com |

## Author

Nagineni Kartheek

## License

MIT