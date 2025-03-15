from openai import OpenAI
import os

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=200,
    temperature=0.1,
    messages=[
        {
            "role": "system",
            "content": "You are an experienced programmer. Return only clean and high-quality code."
        },
        {
            "role": "user",
            "content": "Write a Hello World code in Python."
        }
    ]
)

print(completion.choices[0].message.content)
