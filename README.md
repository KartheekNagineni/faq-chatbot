# 🤖 FAQ Chatbot — AI Customer Support Assistant

An AI-powered customer support chatbot for e-commerce websites that answers customer queries using **Groq's LLaMA 3.1 8B Instant** model and a curated FAQ knowledge base. The application provides natural language question answering through a modern chat interface built with FastAPI and JavaScript.

## 🌐 Live Demo

**Frontend:** https://resilient-lolly-285ab4.netlify.app/

**Backend:** Render

---

## ✨ Features

* 💬 Natural language question answering
* 🧠 AI-powered responses using Groq LLaMA 3.1
* 📚 79 curated e-commerce FAQ pairs
* 🔄 Conversation history support
* ⚡ FastAPI REST API backend
* 🎨 Clean and responsive chat interface
* ⌨️ Animated typing indicator
* ☁️ Cloud deployment using Netlify and Render

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* Groq API
* LLaMA 3.1 8B Instant

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript

### Dataset

* Kaggle Ecommerce FAQ Chatbot Dataset (79 FAQ pairs)

### Deployment

* Netlify (Frontend)
* Render (Backend)

---

## 📂 Project Structure

```text
faq-chatbot/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── Ecommerce_FAQ_Chatbot_dataset.json
│   └── services/
│       └── chat.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── app.js
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot/backend
```

### 2. Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env`

Add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

You can obtain a free API key from the Groq Console.

### 5. Run the Application

```bash
uvicorn main:app --reload --port 8000
```

Visit:

```
http://localhost:8000
```

---

## ⚙️ How It Works

1. The user enters a question in the chat interface.
2. The frontend sends the question and conversation history to the FastAPI backend.
3. The backend processes the request and loads the FAQ knowledge base.
4. Groq LLaMA 3.1 generates the most relevant answer based on the FAQ dataset.
5. The response is returned to the frontend and displayed to the user.

---

## 💡 Sample Questions

* How can I create an account?
* What payment methods do you accept?
* How do I track my order?
* What is your return policy?
* Can I order without logging in?
* How long does shipping take?

---

## 🔑 Environment Variables

| Variable     | Description       |
| ------------ | ----------------- |
| GROQ_API_KEY | Your Groq API key |

---

## 📌 Challenges Solved

* Integrated Groq LLaMA API with FastAPI
* Managed conversation history
* Built a responsive chat interface
* Connected frontend and backend through REST APIs
* Deployed a full-stack AI application using Netlify and Render

---

## 🚀 Future Improvements

* Semantic search using embeddings
* Vector database integration
* Response streaming
* Voice input support
* Multi-language support
* User authentication

---

## ⚠️ Note

The backend is hosted on Render's free tier. The first request may take slightly longer if the service has been inactive due to cold start behavior. Subsequent responses are significantly faster.

---

## 👨‍💻 Author

**Nagineni Kartheek**

* MSc in Artificial Intelligence
* University of Jyväskylä, Finland

---

## 📄 License

This project is licensed under the MIT License.
