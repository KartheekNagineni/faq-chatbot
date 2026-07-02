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

with open(DATASET_PATH, encoding="utf-8") as f:
    data = json.load(f)

FAQS = data["questions"]


def search_faq(question):

    question = question.lower()

    results = []

    for faq in FAQS:

        text = (faq["question"] + " " + faq["answer"]).lower()

        score = 0

        for word in question.split():
            if word in text:
                score += 1

        if score > 0:
            results.append((score, faq))

    results.sort(reverse=True, key=lambda x: x[0])

    return [faq for _, faq in results[:5]]


async def get_answer(user_question, history):

    faqs = search_faq(user_question)

    faq_text = ""

    for faq in faqs:

        faq_text += f"Q: {faq['question']}\n"
        faq_text += f"A: {faq['answer']}\n\n"

    messages = [
        {
            "role": "system",
            "content":
            "Answer ONLY using the FAQ below.\n\n"
            + faq_text
        }
    ]

    messages.extend(history[-2:])

    messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=messages,

        temperature=0,

        max_tokens=80

    )

    return response.choices[0].message.content.strip()
