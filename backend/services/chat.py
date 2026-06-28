from dotenv import load_dotenv
load_dotenv()
import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "Ecommerce_FAQ_Chatbot_dataset.json")

def load_dataset():
    with open(DATASET_PATH, encoding="utf-8") as f:
        data = json.load(f)
    faqs = data["questions"]
    print(f"Loaded {len(faqs)} FAQs from dataset")
    return faqs

FAQS = load_dataset()

def build_faq_text():
    return "\n".join([
        "Q: " + faq["question"] + "\nA: " + faq["answer"]
        for faq in FAQS
    ])

FAQ_TEXT = build_faq_text()

async def get_answer(user_question: str, history: list) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful e-commerce customer support chatbot.\n"
                "Answer ONLY using the FAQ knowledge base below.\n"
                "Give short, direct, friendly answers.\n"
                "If the question is not covered say: I do not have that information. Please email support@store.com\n\n"
                "FAQ Knowledge Base:\n" + FAQ_TEXT
            )
        }
    ]

    for msg in history[-6:]:
        messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_question})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()