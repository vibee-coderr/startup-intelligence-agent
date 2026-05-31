import json
from utils.json_parser import parse_json
from utils.llm import generate_response

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

    response = generate_response(
        final_prompt
    )

    # Clean the response
    cleaned_text = response.strip()
    
    # Remove markdown code blocks
    cleaned_text = cleaned_text.replace("```json", "").replace("```", "")
    
    # Remove common instruction text that appears after JSON
    lines = cleaned_text.split('\n')
    cleaned_text = '\n'.join(lines).strip()

    try:
        result = parse_json(cleaned_text)
        # If parse_json returned an error dict, log it and return the error
        if "error" in result and len(result) == 2:
            print(f"Warning: {result['error']}")
        return result
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return {"error": f"JSON parsing failed: {str(e)}"}