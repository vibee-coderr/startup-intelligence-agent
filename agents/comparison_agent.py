from utils.llm import generate_response
from utils.json_parser import parse_json

def generate_comparison(company1_name, analysis1, competitor1, swot1, company2_name, analysis2, competitor2, swot2):
    
    with open(
        "prompts/comparison_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:
        prompt = file.read()

    final_prompt = f"""
    {prompt}

    Company 1: {company1_name}
    
    Analysis:
    {analysis1}
    
    Competitors:
    {competitor1}
    
    SWOT:
    {swot1}

    ---

    Company 2: {company2_name}
    
    Analysis:
    {analysis2}
    
    Competitors:
    {competitor2}
    
    SWOT:
    {swot2}
    """

    response = generate_response(final_prompt)

    # Clean the response
    cleaned_text = response.strip()
    
    # Remove markdown code blocks
    cleaned_text = cleaned_text.replace("```json", "").replace("```", "")
    
    # Remove common instruction text
    lines = cleaned_text.split('\n')
    cleaned_text = '\n'.join(lines).strip()

    try:
        result = parse_json(cleaned_text)
        if "error" in result and len(result) == 2:
            print(f"Warning: {result['error']}")
        return result
    except Exception as e:
        print(f"Error parsing comparison JSON: {e}")
        return {"error": f"Comparison parsing failed: {str(e)}"}