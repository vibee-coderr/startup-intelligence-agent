from ollama import chat

response = chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Analyze Nvidia in 5 bullet points."
        }
    ]
)

print(response["message"]["content"])