from dotenv import load_dotenv
from google import genai
import os
import json

from utils.gemini_client import client

def analyze_company(company_name):

    with open(
        "prompts/analyst_prompt.txt",
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

    return json.loads(
    response.text
)