import os
import json
from urllib import response

from dotenv import load_dotenv
from google import genai

from utils.gemini_client import client

def find_competitors(company_name):

    with open(
        "prompts/competitor_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        prompt = file.read()

    final_prompt = f"""
    {prompt}

    Company:
    {company_name}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    cleaned_text = response.text.strip()

    cleaned_text = cleaned_text.replace(
    "```json",
    ""
)

    cleaned_text = cleaned_text.replace(
    "```",
    ""
)

    return json.loads(cleaned_text)