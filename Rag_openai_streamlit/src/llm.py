from openai import OpenAI
from config import OPENAI_API_KEY

client=OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(question,context):
    prompt=f'''
You are an HR Policy Assistant.

Rules:
- Answer only from provided context.
- Do not hallucinate.
- If answer is unavailable, say:
  "The HR policy does not contain this information."

Context:
{context}

Question:
{question}
'''
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are an HR policy assistant."},
            {"role":"user","content":prompt}
        ]
    )
    return response.choices[0].message.content
