from openai import OpenAI


client= OpenAI(
    api_key="",
    base_url="https://openrouter.ai/api/v1"
)

completion = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct:free",  # free daily usage available
    messages=[{"role": "system", "content": "You are virtual assistant named jarvis skilled in general task like alexa and google cloud!"},
       {"role":"user", "content": "What is coding."}         
    ]
)

print(completion.choices[0].message.content)


# pip install openai
