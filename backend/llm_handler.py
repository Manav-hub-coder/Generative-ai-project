# import os
# from openai import OpenAI

# client = OpenAI(api_key="YOUR_API_KEY")


# def generate_sql(question: str):
#     prompt = f"""
#     Convert this question into SQL:
#     {question}
#     Table: sales(product, region, revenue, date)
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content.strip()


# def generate_insights(df):
#     prompt = f"Analyze this data and give business insights: {df.head().to_string()}"

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]


def generate_sql(question: str):
    prompt = f"""
    Convert this question into SQL:
    {question}

    Table: sales(product, region, revenue, date)

    Only return SQL query.
    """
    return call_llm(prompt)


def generate_insights(df):
    prompt = f"""
    Analyze this data and give business insights:
    {df.head().to_string()}
    """
    return call_llm(prompt)