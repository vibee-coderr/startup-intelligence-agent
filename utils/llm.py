from ollama import chat

def generate_response(prompt):

    response = chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]