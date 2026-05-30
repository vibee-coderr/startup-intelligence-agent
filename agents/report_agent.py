from utils.gemini_client import client

def generate_report(
    analysis_data,
    competitor_data,
    swot_data
):

    with open(
        "prompts/report_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        prompt = file.read()

    final_prompt = f"""
    {prompt}

    Analysis Data:
    {analysis_data}

    Competitor Data:
    {competitor_data}

    SWOT Data:
    {swot_data}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return response.text