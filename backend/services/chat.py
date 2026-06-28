from dotenv import load_dotenv
load_dotenv()

import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

DATASET_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Ecommerce_FAQ_Chatbot_dataset.json"
)


def load_dataset():
    with open(DATASET_PATH, encoding="utf-8") as f:
        data = json.load(f)

    faqs = data["questions"]
    print(f"Loaded {len(faqs)} FAQs from dataset")
    return faqs


FAQS = load_dataset()


def build_faq_text():
    return "\n\n".join(
        [
            f"Q: {faq['question']}\nA: {faq['answer']}"
            for faq in FAQS
        ]
    )


FAQ_TEXT = build_faq_text()


async def get_answer(user_question: str, history: list) -> str:

    messages = [
        {
            "role": "system",
            "content": f"""
You are an e-commerce customer support assistant.

Rules:
- Answer ONLY from the FAQ knowledge below.
- Be short and helpful.
- If the answer is not available, reply:
'I do not have that information. Please contact support.'

FAQ Knowledge Base:

{FAQ_TEXT}
"""
        }
    ]

    for msg in history[-6:]:
        messages.append(msg)

    messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0,
            max_tokens=300,
        )

        answer = response.choices[0].message.content.strip()

        print("Question:", user_question)
        print("Answer:", answer)

        return answer

    except Exception as e:

        print("Groq Error:", str(e))

        return "Sorry, I encountered an error while processing your request."
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
