from utils.llm import generate_response
from utils.json_parser import parse_json

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

    response = generate_response(
        final_prompt
    )

    # Clean the response
    cleaned_text = response.strip()
    
    # Remove markdown code blocks
    cleaned_text = cleaned_text.replace("```json", "").replace("```", "")
    
    # Remove common instruction text
    lines = cleaned_text.split('\n')
    cleaned_text = '\n'.join(lines).strip()

    print("\nCOMPETITOR RESPONSE:\n")
    print(cleaned_text)
    print("\n" + "="*50 + "\n")

    try:
        result = parse_json(cleaned_text)
        if "error" in result and len(result) == 2:
            print(f"Warning: {result['error']}")
        return result
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return {"error": f"JSON parsing failed: {str(e)}"}